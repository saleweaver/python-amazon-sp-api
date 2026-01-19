from datetime import datetime
import logging
import os

from sp_api.auth import AccessTokenResponse
from sp_api.base.ApiResponse import ApiResponse
from sp_api.base.credential_provider import CredentialProvider
from sp_api.base.marketplaces import Marketplaces
from sp_api.base._core import parse_response, prepare_request, resolve_method

from ._transport_httpx import AsyncHttpxTransport
from .base_client import BaseClient
from ..auth import AccessTokenClient
from sp_api.base.exceptions import MissingScopeException

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)  # Set default to DEBUG; users can override externally


class Client(BaseClient):
    grantless_scope: str = ""
    keep_restricted_data_token: bool = False
    version = None

    def __init__(
        self,
        marketplace: Marketplaces = Marketplaces[
            os.environ.get("SP_API_DEFAULT_MARKETPLACE", Marketplaces.US.name)
        ],
        *,
        refresh_token=None,
        account="default",
        credentials=None,
        restricted_data_token=None,
        proxies=None,
        verify=True,
        timeout=None,
        version=None,
        credential_providers=None,
        auth_token_client_class=AccessTokenClient,
    ):
        if os.environ.get("SP_API_DEFAULT_MARKETPLACE", None):
            marketplace = Marketplaces[os.environ.get("SP_API_DEFAULT_MARKETPLACE")]
        self.credentials = CredentialProvider(
            account,
            credentials,
            credential_providers=credential_providers,
        ).credentials

        self.endpoint = marketplace.endpoint
        self.marketplace_id = marketplace.marketplace_id
        self.region = marketplace.region
        self.restricted_data_token = restricted_data_token
        self._auth = auth_token_client_class(
            refresh_token=refresh_token,
            credentials=self.credentials,
            proxies=proxies,
            verify=verify,
        )
        self.proxies = proxies
        self.timeout = timeout
        self.version = version
        self.verify = verify
        self._transport = AsyncHttpxTransport(
            timeout=timeout,
            proxies=proxies,
            verify=verify,
        )

    async def _get_headers(self, access_token=None):
        token = access_token or self.restricted_data_token
        if token is None:
            token = (await self.auth).access_token
        return {
            "host": self.endpoint[8:],
            "user-agent": self.user_agent,
            "x-amz-access-token": token,
            "x-amz-date": datetime.utcnow().strftime("%Y%m%dT%H%M%SZ"),
            "content-type": "application/json",
        }

    @property
    async def auth(self) -> AccessTokenResponse:
        return await self._auth.get_auth()

    @property
    async def grantless_auth(self) -> AccessTokenResponse:
        if not self.grantless_scope:
            raise MissingScopeException("Grantless operations require scope")
        return await self._auth.get_grantless_auth(self.grantless_scope)

    async def _request(
        self,
        path: str,
        *,
        data: dict = None,
        params: dict = None,
        headers=None,
        add_marketplace=True,
        res_no_data: bool = False,
        bulk: bool = False,
        wrap_list: bool = False,
    ) -> ApiResponse:
        method, params, data = resolve_method(params, data)
        self.method = method

        request_headers = headers or await self._get_headers()

        log.debug("HTTP Method: %s", method)
        log.debug("Making request to URL: %s", self.endpoint + self._check_version(path))
        log.debug("Request Params: %s", params)
        log.debug(
            "Request Data: %s",
            data if method in ("POST", "PUT", "PATCH") else None,
        )
        log.debug("Request Headers: %s", request_headers)

        prepared = prepare_request(
            method=method,
            endpoint=self.endpoint,
            path=path,
            params=params,
            data=data,
            headers=request_headers,
            add_marketplace=add_marketplace,
            marketplace_id=self.marketplace_id,
            version=self.version,
        )
        res = await self._transport.request(**prepared)
        return parse_response(
            res,
            method=self.method,
            res_no_data=res_no_data,
            bulk=bulk,
            wrap_list=wrap_list,
        )

    async def _request_grantless_operation(
        self, path: str, *, data: dict = None, params: dict = None
    ):
        headers = await self._get_headers(
            access_token=(await self.grantless_auth).access_token
        )
        log.debug("HTTP Method: %s", self.method)
        log.debug("Making request to URL: %s", self.endpoint + self._check_version(path))
        log.debug("Request Params: %s", params)
        log.debug(
            "Request Data: %s",
            data if self.method in ("POST", "PUT", "PATCH") else None,
        )
        log.debug("Request Headers: %s", headers)
        return await self._request(path, data=data, params=params, headers=headers)

    def _check_version(self, path):
        if "<version>" not in path:
            return path
        return path.replace("<version>", self.version)

    async def __aenter__(self):
        self.keep_restricted_data_token = True
        return self

    async def __aexit__(self, *args, **kwargs):
        self.restricted_data_token = None
        self.keep_restricted_data_token = False
        await self.aclose()

    async def aclose(self):
        await self._transport.aclose()
