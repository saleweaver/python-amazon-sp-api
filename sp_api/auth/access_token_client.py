import json
import os

import requests
from botocore.exceptions import ClientError
import hashlib
import logging
from cachetools import TTLCache
import boto3
from sp_api.base import BaseClient

from .credentials import Credentials
from .access_token_response import AccessTokenResponse
from .exceptions import AuthorizationError

cache = TTLCache(maxsize=10, ttl=3600)
grantless_cache = TTLCache(maxsize=10, ttl=3600)

logger = logging.getLogger(__name__)


class AccessTokenClient(BaseClient):
    host = 'api.amazon.com'
    grant_type = 'refresh_token'
    path = '/auth/o2/token'

    def __init__(self, refresh_token=None, account='default', credentials=None):
        super().__init__(account, credentials)
        self.cred = Credentials(refresh_token, self.credentials)

    def _request(self, url, data, headers):
        response = requests.post(url, data=data, headers=headers)
        response_data = response.json()
        if response.status_code != 200:
            error_message = response_data.get('error_description')
            error_code = response_data.get('error')
            raise AuthorizationError(error_code, error_message, response.status_code)
        return response_data

    def get_auth(self) -> AccessTokenResponse:
        """
        Get's the access token
        :return:AccessTokenResponse
        """
        global cache

        cache_key = self._get_cache_key()
        try:
            access_token = cache[cache_key]
        except KeyError:
            cache_ttl = 3600
            access_token = None
            if self.use_secrets():
                access_token = self.get_secret()
            if not access_token:
                request_url = self.scheme + self.host + self.path
                access_token = self._request(request_url, self.data, self.headers)
                if self.use_secrets():
                    self.put_access_token(access_token)
            else:
                cache_ttl = access_token.get('expires_in')
            cache = TTLCache(maxsize=10, ttl=cache_ttl - 15)
            cache[cache_key] = access_token
        return AccessTokenResponse(**access_token)

    def use_secrets(self):
        return os.environ.get('SP_API_AWS_SECRET_ID') and os.environ.get('SP_API_USE_SECRET_ACCESS_TOKEN_ROTATION')

    def get_grantless_auth(self, scope='sellingpartnerapi::notifications'):
        """
        :param scope: One of allowed scope for grantless operations:
            sellingpartnerapi::notifications or sellingpartnerapi::migration
            See: https://github.com/amzn/selling-partner-api-docs/blob/main/guides/en-US/developer-guide/SellingPartnerApiDeveloperGuide.md#step-3-configure-your-lwa-credentials

        POST /auth/o2/token HTTP/l.l
        Host: api.amazon.com
        Content-Type: application/x-www-form-urlencoded;charset=UTF-8
        grant_type=client_credentials
        &scope=sellingpartnerapi::notifications
        &client_id=foodev
        &client_secret=Y76SDl2F
        :return: AccessTokenResponse
        """
        global grantless_cache
        cache_key = self._get_cache_key(scope)
        try:
            access_token = grantless_cache[cache_key]
            logger.debug('from_cache. scope: %s', scope)
        except KeyError:
            request_url = self.scheme + self.host + self.path
            access_token = self._request(
                request_url,
                data=self.grantless_data(scope),
                headers=self.headers
            )
            logger.debug('token_refreshed')
            grantless_cache.clear()
            grantless_cache[cache_key] = access_token

        return AccessTokenResponse(**access_token)

    def authorize_auth_code(self, auth_code):
        request_url = self.scheme + self.host + self.path
        res = self._request(
            request_url,
            data=self._auth_code_request_body(auth_code),
            headers=self.headers
        )
        return res

    def _auth_code_request_body(self, auth_code):
        return {
            'grant_type': 'authorization_code',
            'code': auth_code,
            'client_id': self.cred.client_id,
            'client_secret': self.cred.client_secret
        }

    def grantless_data(self, scope_value: str):
        return {
            'grant_type': 'client_credentials',
            'client_id': self.cred.client_id,
            'scope': scope_value,
            'client_secret': self.cred.client_secret
        }

    @property
    def data(self):
        return {
            'grant_type': self.grant_type,
            'client_id': self.cred.client_id,
            'refresh_token': self.cred.refresh_token,
            'client_secret': self.cred.client_secret
        }

    @property
    def headers(self):
        return {
            'User-Agent': self.user_agent,
            'content-type': self.content_type
        }

    def _get_cache_key(self, token_flavor=''):
        return 'access_token_' + hashlib.md5(
            (token_flavor + self.cred.refresh_token).encode('utf-8')
        ).hexdigest()

    def get_secret(self):

        try:
            client = boto3.client('secretsmanager')
            response = client.get_secret_value(
                SecretId=os.environ.get('SP_API_AWS_SECRET_ID')
            )
            secret = json.loads(response.get('SecretString'))
        except ClientError:
            pass
        else:
            try:
                return json.loads(secret.get(f'SP_API_ACCESS_TOKEN__{self._get_cache_key()}'))
            except TypeError:
                return

    def put_access_token(self, access_token):
        try:
            client = boto3.client('secretsmanager')
            response = client.get_secret_value(
                SecretId=os.environ.get('SP_API_AWS_SECRET_ID')
            )
            secret = json.loads(response.get('SecretString'))
            secret.update({f'SP_API_ACCESS_TOKEN__{self._get_cache_key()}': json.dumps(access_token)})
            client.put_secret_value(SecretId=os.environ.get('SP_API_AWS_SECRET_ID'), SecretString=json.dumps(secret))
        except ClientError:
            pass
