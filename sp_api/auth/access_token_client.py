import requests

import logging
from cachetools import TTLCache

from .credentials import Credentials
from .access_token_response import AccessTokenResponse
from sp_api.base import BaseClient
import hashlib

cache = TTLCache(maxsize=10, ttl=3600)
grantless_cache = TTLCache(maxsize=10, ttl=3600)

logger = logging.getLogger(__name__)


class AccessTokenClient(BaseClient):
    host = 'api.amazon.com'
    grant_type = 'refresh_token'
    path = '/auth/o2/token'

    def __init__(self, refresh_token=None):
        self.credentials = Credentials(refresh_token)

    def get_auth(self) -> AccessTokenResponse:
        """
        Get's the access token
        :return:AccessTokenResponse
        """
        global cache

        cache_key = self.get_cache_key()
        try:
            access_token = cache[cache_key]
            logger.debug('from cache')
        except KeyError:
            response = requests.post(self.scheme + self.host + self.path, data=self.data, headers=self.headers)
            logger.debug('token refreshed')
            cache = TTLCache(maxsize=10, ttl=3600)
            cache[cache_key] = response.json()
            access_token = response.json()

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
        cache_key = self.get_cache_key()
        try:
            access_token = grantless_cache[cache_key]
            logger.debug('from_cache')
        except KeyError:
            response = requests.post(self.scheme + self.host + self.path, data=self.grantless_data, headers=self.headers)
            logger.debug('token_refreshed')
            grantless_cache = TTLCache(maxsize=10, ttl=3600)
            grantless_cache[cache_key] = response.json()
            access_token = response.json()

        return AccessTokenResponse(**access_token)

    @property
    def grantless_data(self):
        return {
            'grant_type': 'client_credentials',
            'client_id': self.credentials.client_id,
            'scope': 'sellingpartnerapi::notifications',
            'client_secret': self.credentials.client_secret
        }

    @property
    def data(self):
        return {
            'grant_type': self.grant_type,
            'client_id': self.credentials.client_id,
            'refresh_token': self.credentials.refresh_token,
            'client_secret': self.credentials.client_secret
        }

    @property
    def headers(self):
        return {
            'User-Agent': self.user_agent,
            'content-type': self.content_type
        }

    def get_cache_key(self):
        return 'access_token_' + hashlib.md5(self.credentials.refresh_token.encode('utf-8')).hexdigest()
