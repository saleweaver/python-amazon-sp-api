import urllib.parse

from sp_api.base import ApiResponse, fill_query_params, sp_endpoint
from sp_api.util import encode_kwarg
from sp_api.asyncio.base import AsyncBaseClient


class Catalog(AsyncBaseClient):
    """
    :link: https://github.com/amzn/selling-partner-api-docs/blob/main/references/catalog-items-api/catalogItemsV0.md

    """

    @sp_endpoint("/catalog/v0/items/{}")
    async def get_item(self, asin: str, **kwargs) -> ApiResponse:
        """
        get_item(self, asin, **kwargs) -> ApiResponse
        
        Returns a specified item and its attributes.
        
        Examples:
            literal blocks::
            
                await Catalog().get_item("value")
        
        Args:
            asin:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """
        return await self._request(
            fill_query_params(kwargs.pop("path"), asin), params=kwargs
        )

    @sp_endpoint("/catalog/v0/items")
    async def list_items(self, **kwargs) -> ApiResponse:
        """
        list_items(self, **kwargs) -> ApiResponse
        
        Returns a list of items and their attributes, based on a search query or item identifiers that you specify. When based on a search query, provide the Query parameter and optionally, the QueryContextId parameter. When based on item identifiers, provide a single appropriate parameter based on the identifier type, and specify the associated item value. MarketplaceId is always required.
        
        Examples:
            literal blocks::
            
                await Catalog().list_items()
        
        Args:
            **kwargs:
        
        Returns:
            ApiResponse
        """
        encode_kwarg(kwargs, "Query", urllib.parse.quote_plus)
        return await self._request(kwargs.pop("path"), params=kwargs)

    @sp_endpoint("/catalog/v0/categories")
    async def list_categories(self, **kwargs) -> ApiResponse:
        """
        list_categories(self, **kwargs) -> ApiResponse
        
        Returns the parent categories to which an item belongs, based on the specified ASIN or SellerSKU
        
        Examples:
            literal blocks::
            
                await Catalog().list_categories()
        
        Args:
            **kwargs:
        
        Returns:
            ApiResponse
        """
        encode_kwarg(kwargs, "Query", urllib.parse.quote_plus)
        return await self._request(kwargs.pop("path"), params=kwargs)
