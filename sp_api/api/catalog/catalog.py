import urllib.parse

from sp_api.base import Client, sp_endpoint, fill_query_params, ApiResponse
from sp_api.util import encode_kwarg


class Catalog(Client):
    """
    :link: https://github.com/amzn/selling-partner-api-docs/blob/main/references/catalog-items-api/catalogItemsV0.md

    """

    @sp_endpoint("/catalog/v0/items/{}")
    def get_item(self, asin: str, **kwargs) -> ApiResponse:
        """
        get_item(self, asin, **kwargs) -> ApiResponse
        
        Returns a specified item and its attributes.
        
        Examples:
            literal blocks::
            
                Catalog().get_item("value")
        
        Args:
            asin:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """
        return self._request(fill_query_params(kwargs.pop("path"), asin), params=kwargs)

    @sp_endpoint("/catalog/v0/items")
    def list_items(self, **kwargs) -> ApiResponse:
        """
        list_items(self, **kwargs) -> ApiResponse
        
        Returns a list of items and their attributes, based on a search query or item identifiers that you specify. When based on a search query, provide the Query parameter and optionally, the QueryContextId parameter. When based on item identifiers, provide a single appropriate parameter based on the identifier type, and specify the associated item value. MarketplaceId is always required.
        
        Examples:
            literal blocks::
            
                Catalog().list_items()
        
        Args:
            **kwargs:
        
        Returns:
            ApiResponse
        """
        encode_kwarg(kwargs, "Query", urllib.parse.quote_plus)
        return self._request(kwargs.pop("path"), params=kwargs)

    @sp_endpoint("/catalog/v0/categories")
    def list_categories(self, **kwargs) -> ApiResponse:
        """
        list_categories(self, **kwargs) -> ApiResponse
        
        Returns the parent categories to which an item belongs, based on the specified ASIN or SellerSKU
        
        Examples:
            literal blocks::
            
                Catalog().list_categories()
        
        Args:
            **kwargs:
        
        Returns:
            ApiResponse
        """
        encode_kwarg(kwargs, "Query", urllib.parse.quote_plus)
        return self._request(kwargs.pop("path"), params=kwargs)
