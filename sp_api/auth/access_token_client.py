import os

import logging
from cachetools import TTLCache
from sp_api.base import BaseClient
from sp_api.base._transport_httpx import HttpxTransport

from .credentials import Credentials
from .access_token_response import AccessTokenResponse
from .exceptions import AuthorizationError
from ._core import (
    build_auth_code_request_body,
    build_cache_key,
    build_grantless_data,
    build_headers,
    build_refresh_token_data,
)

cache = TTLCache(maxsize=int(os.environ.get('SP_API_AUTH_CACHE_SIZE', 10)), ttl=int(os.environ.get('SP_API_AUTH_CACHE_TTL', 3200)))
grantless_cache = TTLCache(maxsize=int(os.environ.get('SP_API_AUTH_CACHE_SIZE', 10)), ttl=int(os.environ.get('SP_API_AUTH_CACHE_TTL', 3200)))

logger = logging.getLogger(__name__)


class AccessTokenClient(BaseClient):
    host = 'api.amazon.com'
    grant_type = 'refresh_token'
    path = '/auth/o2/token'

    def __init__(self, refresh_token=None, credentials=None, proxies=None, verify=True):
        self.cred = Credentials(refresh_token, credentials)
        self.proxies = proxies
        self.verify = verify
        self._transport = HttpxTransport(
            proxies=proxies,
            verify=verify,
        )

    def _request(self, url, data, headers):
        response = self._transport.request("POST", url, data=data, headers=headers)
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

        cache_key = self._get_cache_key()
        try:
            access_token = cache[cache_key]
        except KeyError:
            request_url = self.scheme + self.host + self.path
            access_token = self._request(request_url, self.data, self.headers)
            cache[cache_key] = access_token
        return AccessTokenResponse(**access_token)

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
        return build_auth_code_request_body(self.cred, auth_code)

    def grantless_data(self, scope_value: str):
        return build_grantless_data(self.cred, scope_value)

    @property
    def data(self):
        return build_refresh_token_data(self.cred, self.grant_type)

    @property
    def headers(self):
        return build_headers(self.user_agent, self.content_type)

    def _get_cache_key(self, token_flavor=''):
        return build_cache_key(self.cred.refresh_token, token_flavor)
