import urllib.parse

from sp_api.base import Client, sp_endpoint, fill_query_params, ApiResponse
from sp_api.asyncio.base import AsyncBaseClient


class Tokens(AsyncBaseClient):
    """
    Tokens SP-API Client
    :link:

    The Selling Partner API for Tokens provides a secure way to access a customers's PII (Personally Identifiable Information). You can call the Tokens API to get a Restricted Data Token (RDT) for one or more restricted resources that you specify. The RDT authorizes you to make subsequent requests to access these restricted resources.
    """

    @sp_endpoint("/tokens/2021-03-01/restrictedDataToken", method="POST")
    async def create_restricted_data_token(self, **kwargs) -> ApiResponse:
        """
        create_restricted_data_token(self, **kwargs) -> ApiResponse
        
        Returns a Restricted Data Token (RDT) for one or more restricted resources that you specify. A restricted resource is the HTTP method and path from a restricted operation that returns Personally Identifiable Information (PII), plus a dataElements value that indicates the type of PII requested. See the Tokens API Use Case Guide for a list of restricted operations. Use the RDT returned here as the access token in subsequent calls to the corresponding restricted operations.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       10
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await Tokens().create_restricted_data_token()
        
        Args:
            body: CreateRestrictedDataTokenRequest | required The restricted data token request details.
        
        Returns:
            ApiResponse
        """

        return await self._request(kwargs.pop("path"), data=kwargs)