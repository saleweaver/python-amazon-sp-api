import requests

import logging
from cachetools import TTLCache

from .credentials import Credentials
from .access_token_response import AccessTokenResponse
from sp_api.base import BaseClient

cache = TTLCache(maxsize=10, ttl=3600)
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

        try:
            access_token = cache['access_token']
            logger.debug('from cache')
        except KeyError:
            response = requests.post(self.scheme + self.host + self.path, data=self.data, headers=self.headers)
            logger.debug('token refreshed')
            cache = TTLCache(maxsize=10, ttl=3600)
            cache['access_token'] = response.json()
            access_token = response.json()

        return AccessTokenResponse(**access_token)

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
