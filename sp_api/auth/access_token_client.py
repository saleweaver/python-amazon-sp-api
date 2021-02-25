import requests

import hashlib
import logging
from cachetools import TTLCache

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
            logger.debug('from cache')
        except KeyError:
            request_url = self.scheme + self.host + self.path
            access_token = self._request(request_url, self.data, self.headers)
            logger.debug('token refreshed')
            cache = TTLCache(maxsize=10, ttl=3600)
            cache[cache_key] = access_token
        return AccessTokenResponse(**access_token)

    def get_grantless_auth(self):
        """
        POST /auth/o2/token HTTP/l.l
        Host: api.amazon.com
        Content-Type: application/x-www-form-urlencoded;charset=UTF-8
        grant_type=client_credentials
        &scope=sellingpartnerapi::notifications
        &client_id=foodev
        &client_secret=Y76SDl2F
        :return:
        """
        global grantless_cache
        cache_key = self._get_cache_key()
        try:
            access_token = grantless_cache[cache_key]
            logger.debug('from_cache')
        except KeyError:
            request_url = self.scheme + self.host + self.path
            access_token = self._request(request_url, data=self.grantless_data, headers=self.headers)
            logger.debug('token_refreshed')
            grantless_cache = TTLCache(maxsize=10, ttl=3600)
            grantless_cache[cache_key] = access_token

        return AccessTokenResponse(**access_token)

    @property
    def grantless_data(self):
        return {
            'grant_type': 'client_credentials',
            'client_id': self.cred.client_id,
            'scope': 'sellingpartnerapi::notifications',
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

    def _get_cache_key(self):
        return 'access_token_' + hashlib.md5(self.cred.refresh_token.encode('utf-8')).hexdigest()
