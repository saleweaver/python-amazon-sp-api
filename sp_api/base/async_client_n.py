"""
Asynchronous client implementation for Amazon Selling Partner API.
This module provides an async version of the client with modern Python practices.
"""

import hashlib
import json
import logging
import os
from datetime import datetime
from typing import Dict, List, Optional, Union, Any, Type

import aiohttp
from aiohttp import ClientResponse
import asyncio

from sp_api.auth import AccessTokenClient, AccessTokenResponse
from .ApiResponse import ApiResponse
from .base_client import BaseClient
from .exceptions import get_exception_for_code, MissingScopeException
from .marketplaces import Marketplaces
from sp_api.base.credential_provider import CredentialProvider

logger = logging.getLogger(__name__)


class AsyncClient(BaseClient):
    """
    Asynchronous client for interacting with Amazon Selling Partner API.
    
    This client handles authentication, request building, and response parsing for
    the Amazon Selling Partner API with a cleaner, async implementation.
    """
    
    grantless_scope: str = ""
    version: Optional[str] = None
    
    def __init__(
        self,
        marketplace: Marketplaces = Marketplaces[
            os.environ.get("SP_API_DEFAULT_MARKETPLACE", Marketplaces.US.name)
        ],
        *,
        refresh_token: Optional[str] = None,
        account: str = "default",
        credentials: Optional[Dict[str, str]] = None,
        restricted_data_token: Optional[str] = None,
        proxies: Optional[Dict[str, str]] = None,
        verify: bool = True,
        timeout: Optional[int] = None,
        version: Optional[str] = None,
        credential_providers: Optional[List[Any]] = None,
        auth_token_client_class: Type = AccessTokenClient,
    ):
        """
        Initialize a new asynchronous Amazon Selling Partner API client.
        
        Args:
            marketplace: The marketplace to use for requests
            refresh_token: OAuth refresh token for authorization
            account: Account name in configuration
            credentials: Manual credential configuration
            restricted_data_token: Token for accessing restricted data
            proxies: Proxy configuration for requests
            verify: Whether to verify SSL certificates
            timeout: Request timeout in seconds
            version: API version to use
            credential_providers: List of credential providers
            auth_token_client_class: Class to use for authentication
        """
        # Override marketplace from environment if set
        if os.environ.get("SP_API_DEFAULT_MARKETPLACE"):
            marketplace = Marketplaces[os.environ.get("SP_API_DEFAULT_MARKETPLACE")]
            
        # Initialize credential provider
        self.credentials = CredentialProvider(
            account,
            credentials,
            credential_providers=credential_providers,
        ).credentials

        # Store configuration
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
        self.keep_restricted_data_token = False
        self.method = "GET"  # Default method
        self._session = None

    async def __aenter__(self):
        """
        Async context manager entry point.
        
        Returns:
            Self for context manager
        """
        self.keep_restricted_data_token = True
        self._session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """
        Async context manager exit point to clean up resources.
        """
        if self._session and not self._session.closed:
            await self._session.close()
            
        if not self.keep_restricted_data_token:
            self.restricted_data_token = None
        self.keep_restricted_data_token = False

    @property
    def headers(self) -> Dict[str, str]:
        """
        Generate request headers including authentication tokens.
        
        Returns:
            Dictionary of headers for API requests
        """
        return {
            "host": self.endpoint[8:],  # Remove 'https://' prefix
            "user-agent": self.user_agent,
            "x-amz-access-token": self.restricted_data_token or self.auth.access_token,
            "x-amz-date": datetime.utcnow().strftime("%Y%m%dT%H%M%SZ"),
            "content-type": "application/json",
        }

    @property
    def auth(self) -> AccessTokenResponse:
        """
        Get the authentication token response.
        
        Returns:
            AccessTokenResponse object with the current token
        """
        return self._auth.get_auth()

    @property
    def grantless_auth(self) -> AccessTokenResponse:
        """
        Get the grantless authentication token response.
        
        Returns:
            AccessTokenResponse object with the grantless token
            
        Raises:
            MissingScopeException: If grantless_scope is not set
        """
        if not self.grantless_scope:
            raise MissingScopeException("Grantless operations require scope")
        return self._auth.get_grantless_auth(self.grantless_scope)

    async def _request(
        self,
        path: str,
        *,
        data: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        add_marketplace: bool = True,
        res_no_data: bool = False,
        bulk: bool = False,
        wrap_list: bool = False,
    ) -> ApiResponse:
        """
        Make an asynchronous request to the Amazon Selling Partner API.
        
        Args:
            path: API endpoint path
            data: Request body data
            params: Query parameters
            headers: Custom headers to override defaults
            add_marketplace: Whether to add marketplace IDs automatically
            res_no_data: Whether the response contains no data
            bulk: Whether this is a bulk request
            wrap_list: Whether to wrap list responses in a dict
            
        Returns:
            ApiResponse object containing the parsed response
        """
        params = params or {}
        data = data or {}

        # Extract method from parameters or use default
        if isinstance(data, dict) and "method" in data:
            self.method = data.pop("method")
        elif isinstance(params, dict) and "method" in params:
            self.method = params.pop("method")
        else:
            self.method = "GET"

        # Add marketplace IDs if needed
        if add_marketplace:
            self._add_marketplaces(data if self.method in ("POST", "PUT") else params)

        # Log request details
        logger.debug("HTTP Method: %s", self.method)
        logger.debug("Making request to URL: %s", self.endpoint + self._check_version(path))
        logger.debug("Request Params: %s", params)
        
        if self.method in ("POST", "PUT", "PATCH"):
            logger.debug("Request Data: %s", data)
            
        logger.debug("Request Headers: %s", headers or self.headers)

        # Create aiohttp session if not existing
        if not self._session:
            self._session = aiohttp.ClientSession()
            
        # Prepare request payload for methods that need it
        json_data = None
        if data and self.method in ("POST", "PUT", "PATCH"):
            json_data = data

        # Make the async request
        timeout = aiohttp.ClientTimeout(total=self.timeout) if self.timeout else None
        
        # Create proxy URL format that aiohttp expects
        proxy_url = None
        if self.proxies:
            proxy_protocol = "http"
            if self.endpoint.startswith("https"):
                proxy_protocol = "https"
                
            if proxy_protocol in self.proxies:
                proxy_url = self.proxies[proxy_protocol]
        
        async with self._session.request(
            method=self.method,
            url=self.endpoint + self._check_version(path),
            params=params,
            json=json_data,
            headers=headers or self.headers,
            timeout=timeout,
            proxy=proxy_url,
            ssl=self.verify,
        ) as response:
            return await self._check_response(response, res_no_data, bulk, wrap_list)

    async def _check_response(
        self,
        response: ClientResponse,
        res_no_data: bool = False,
        bulk: bool = False,
        wrap_list: bool = False,
    ) -> ApiResponse:
        """
        Process an API response and handle errors asynchronously.
        
        Args:
            response: Response object from aiohttp
            res_no_data: Whether the response contains no data
            bulk: Whether this is a bulk request
            wrap_list: Whether to wrap list responses in a dict
            
        Returns:
            ApiResponse object containing the parsed response
            
        Raises:
            Exception based on the error code if the request failed
        """
        # Handle DELETE or no-data responses
        if (self.method == "DELETE" or res_no_data) and 200 <= response.status < 300:
            try:
                js = await response.json() or {}
            except (json.JSONDecodeError, aiohttp.ContentTypeError):
                js = {"status_code": response.status}
        else:
            # Parse JSON response
            try:
                js = await response.json() or {}
            except (json.JSONDecodeError, aiohttp.ContentTypeError):
                js = {}

        logger.debug("Response before list handling: %s", js)

        # Handle list responses
        if isinstance(js, list):
            if wrap_list:
                # Support responses that are an array at the top level
                js = dict(payload=js)
            else:
                js = js[0]

        # Check for errors
        error = js.get("errors", None)
        if error:
            logger.error("Error Response: %s", error)
            exception = get_exception_for_code(response.status)
            raise exception(error, headers=response.headers)

        logger.debug("Response: %s", js)
        return ApiResponse(**js, headers=dict(response.headers))

    def _add_marketplaces(self, data: Dict[str, Any]) -> None:
        """
        Add marketplace IDs to the request data.
        
        Args:
            data: Request data to augment with marketplace IDs
        """
        post_keys = ["marketplaceIds", "MarketplaceIds"]
        get_keys = ["MarketplaceId", "MarketplaceIds", "marketplace_ids", "marketplaceIds"]

        if self.method == "POST":
            # Skip if any marketplace ID key already exists
            if any(key in data.keys() for key in post_keys):
                return
                
            # Add marketplace IDs with appropriate format (single ID or list)
            data.update({
                key: (
                    self.marketplace_id if not key.endswith("s") else [self.marketplace_id]
                ) for key in post_keys
            })
            return
            
        # For GET and other methods
        if any(key in data.keys() for key in get_keys):
            return
            
        data.update({
            key: self.marketplace_id if not key.endswith("s") else [self.marketplace_id]
            for key in get_keys
        })

    async def _request_grantless_operation(
        self, 
        path: str, 
        *, 
        data: Optional[Dict[str, Any]] = None, 
        params: Optional[Dict[str, Any]] = None
    ) -> ApiResponse:
        """
        Make an asynchronous request that requires grantless authentication.
        
        Args:
            path: API endpoint path
            data: Request body data
            params: Query parameters
            
        Returns:
            ApiResponse object containing the parsed response
        """
        headers = {
            "host": self.endpoint[8:],
            "user-agent": self.user_agent,
            "x-amz-access-token": self.grantless_auth.access_token,
            "x-amz-date": datetime.utcnow().strftime("%Y%m%dT%H%M%SZ"),
            "content-type": "application/json",
        }
        
        logger.debug("HTTP Method: %s", self.method)
        logger.debug("Making grantless request to URL: %s", self.endpoint + self._check_version(path))
        logger.debug("Request Params: %s", params)
        
        if self.method in ("POST", "PUT", "PATCH"):
            logger.debug("Request Data: %s", data)
            
        logger.debug("Request Headers: %s", headers)
        
        return await self._request(path, data=data, params=params, headers=headers)

    def _check_version(self, path: str) -> str:
        """
        Replace version placeholder with actual version in the path.
        
        Args:
            path: API endpoint path possibly containing a version placeholder
            
        Returns:
            Path with version placeholder replaced
        """
        if "<version>" not in path:
            return path
        return path.replace("<version>", self.version)
        
    # Helper methods for common operations
    async def get(
        self, 
        path: str, 
        params: Optional[Dict[str, Any]] = None, 
        headers: Optional[Dict[str, str]] = None,
        **kwargs
    ) -> ApiResponse:
        """
        Make a GET request to the API.
        
        Args:
            path: API endpoint path
            params: Query parameters
            headers: Custom headers
            **kwargs: Additional parameters for _request
            
        Returns:
            ApiResponse object containing the parsed response
        """
        params = params or {}
        params["method"] = "GET"
        return await self._request(path, params=params, headers=headers, **kwargs)
        
    async def post(
        self, 
        path: str, 
        data: Optional[Dict[str, Any]] = None, 
        headers: Optional[Dict[str, str]] = None,
        **kwargs
    ) -> ApiResponse:
        """
        Make a POST request to the API.
        
        Args:
            path: API endpoint path
            data: Request body data
            headers: Custom headers
            **kwargs: Additional parameters for _request
            
        Returns:
            ApiResponse object containing the parsed response
        """
        data = data or {}
        data["method"] = "POST"
        return await self._request(path, data=data, headers=headers, **kwargs)
        
    async def put(
        self, 
        path: str, 
        data: Optional[Dict[str, Any]] = None, 
        headers: Optional[Dict[str, str]] = None,
        **kwargs
    ) -> ApiResponse:
        """
        Make a PUT request to the API.
        
        Args:
            path: API endpoint path
            data: Request body data
            headers: Custom headers
            **kwargs: Additional parameters for _request
            
        Returns:
            ApiResponse object containing the parsed response
        """
        data = data or {}
        data["method"] = "PUT"
        return await self._request(path, data=data, headers=headers, **kwargs)
        
    async def delete(
        self, 
        path: str, 
        params: Optional[Dict[str, Any]] = None, 
        headers: Optional[Dict[str, str]] = None,
        **kwargs
    ) -> ApiResponse:
        """
        Make a DELETE request to the API.
        
        Args:
            path: API endpoint path
            params: Query parameters
            headers: Custom headers
            **kwargs: Additional parameters for _request
            
        Returns:
            ApiResponse object containing the parsed response
        """
        params = params or {}
        params["method"] = "DELETE"
        return await self._request(path, params=params, headers=headers, **kwargs)
