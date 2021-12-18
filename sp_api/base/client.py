import hashlib
import json
from datetime import datetime
import logging
import os
from json import JSONDecodeError

import boto3
from cachetools import TTLCache
from requests import request

from sp_api.auth import AccessTokenClient, AccessTokenResponse
from .ApiResponse import ApiResponse
from .base_client import BaseClient
from .exceptions import get_exception_for_code, MissingScopeException
from .marketplaces import Marketplaces
from sp_api.base import AWSSigV4
from sp_api.base.credential_provider import CredentialProvider

log = logging.getLogger(__name__)

role_cache = TTLCache(maxsize=10, ttl=3600)


class Client(BaseClient):
    boto3_client = None
    grantless_scope = ''

    def __init__(
            self,
            marketplace: Marketplaces = Marketplaces[os.environ['SP_API_DEFAULT_MARKETPLACE']] if 'SP_API_DEFAULT_MARKETPLACE' in os.environ else Marketplaces.US,
            *,
            refresh_token=None,
            account='default',
            credentials=None,
            restricted_data_token=None
    ):
        self.credentials = CredentialProvider(account, credentials).credentials
        self.boto3_client = boto3.client(
            'sts',
            aws_access_key_id=self.credentials.aws_access_key,
            aws_secret_access_key=self.credentials.aws_secret_key
        )
        self.endpoint = marketplace.endpoint
        self.marketplace_id = marketplace.marketplace_id
        self.region = marketplace.region
        self.restricted_data_token = restricted_data_token
        self._auth = AccessTokenClient(refresh_token=refresh_token, credentials=self.credentials)

    def _get_cache_key(self, token_flavor=''):
        return 'role_' + hashlib.md5(
            (token_flavor + self._auth.cred.refresh_token).encode('utf-8')
        ).hexdigest()

    def set_role(self, cache_key='role'):
        role = self.boto3_client.assume_role(
            RoleArn=self.credentials.role_arn,
            RoleSessionName='guid'
        )
        role_cache[cache_key] = role
        return role

    @property
    def headers(self):
        return {
            'host': self.endpoint[8:],
            'user-agent': self.user_agent,
            'x-amz-access-token': self.restricted_data_token or self.auth.access_token,
            'x-amz-date': datetime.utcnow().strftime('%Y%m%dT%H%M%SZ'),
            'content-type': 'application/json'
        }

    @property
    def auth(self) -> AccessTokenResponse:
        return self._auth.get_auth()

    @property
    def grantless_auth(self) -> AccessTokenResponse:
        if not self.grantless_scope:
            raise MissingScopeException("Grantless operations require scope")
        return self._auth.get_grantless_auth(self.grantless_scope)

    @property
    def role(self):
        cache_key = self._get_cache_key()
        try:
            role = role_cache[cache_key]
        except KeyError:
            role = self.set_role(cache_key)
        return role.get('Credentials')

    def _sign_request(self):
        aws_session_token = None
        aws_access_key_id = self.credentials.aws_access_key
        aws_secret_access_key = self.credentials.aws_secret_key
        if self.credentials.role_arn:
            role = self.role
            aws_session_token = role.get('SessionToken')
            aws_access_key_id = role.get('AccessKeyId')
            aws_secret_access_key = role.get('SecretAccessKey')
        return AWSSigV4('execute-api',
                        aws_access_key_id=aws_access_key_id,
                        aws_secret_access_key=aws_secret_access_key,
                        region=self.region,
                        aws_session_token=aws_session_token
                        )

    def _request(self, path: str, *, data: dict = None, params: dict = None, headers=None,
                 add_marketplace=True) -> ApiResponse:
        if params is None:
            params = {}
        if data is None:
            data = {}

        self.method = params.pop('method', data.pop('method', 'GET'))

        if add_marketplace:
            self._add_marketplaces(data if self.method in ('POST', 'PUT') else params)

        res = request(self.method, self.endpoint + path, params=params,
                      data=json.dumps(data) if data and self.method in ('POST', 'PUT', 'PATCH') else None, headers=headers or self.headers,
                      auth=self._sign_request())
        return self._check_response(res)

    def _check_response(self, res) -> ApiResponse:
        if self.method == 'DELETE' and 200 <= res.status_code < 300:
            try:
                js = res.json() or {}
            except JSONDecodeError:
                js = {'status_code': res.status_code}
        else:
            js = res.json() or {}
        if isinstance(js, list):
            js = js[0]
        error = js.get('errors', None)
        if error:
            exception = get_exception_for_code(res.status_code)
            raise exception(error, headers=res.headers)
        return ApiResponse(**js, headers=res.headers)

    def _add_marketplaces(self, data):
        POST = ['marketplaceIds', 'MarketplaceIds']
        GET = ['MarketplaceId', 'MarketplaceIds', 'marketplace_ids', 'marketplaceIds']

        if self.method == 'POST':
            if any(x in data.keys() for x in POST):
                return
            return data.update({k: self.marketplace_id if not k.endswith('s') else [self.marketplace_id] for k in POST})
        if any(x in data.keys() for x in GET):
            return
        return data.update({k: self.marketplace_id if not k.endswith('s') else [self.marketplace_id] for k in GET})

    def _request_grantless_operation(self, path: str, *, data: dict = None, params: dict = None):
        headers = {
            'host': self.endpoint[8:],
            'user-agent': self.user_agent,
            'x-amz-access-token': self.grantless_auth.access_token,
            'x-amz-date': datetime.utcnow().strftime('%Y%m%dT%H%M%SZ'),
            'content-type': 'application/json'
        }

        return self._request(path, data=data, params=params, headers=headers)
