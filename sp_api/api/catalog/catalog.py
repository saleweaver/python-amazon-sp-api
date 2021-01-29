from sp_api.api.catalog.models.get_catalog_item_response import GetCatalogItemResponse
from sp_api.api.catalog.models.list_catalog_items_response import ListCatalogItemsResponse
from sp_api.base import Client, sp_endpoint, Marketplaces, fill_query_params


class Catalog(Client):
    """
    :link: https://github.com/amzn/selling-partner-api-docs/blob/main/references/catalog-items-api/catalogItemsV0.md
    """
    def __init__(self, marketplace=Marketplaces.US, *, refresh_token=None, account='default', credentials=None):
        super().__init__(marketplace, refresh_token, account, credentials)

    @sp_endpoint('/catalog/v0/items/{}')
    def get_item(self, asin: str, **kwargs) -> GetCatalogItemResponse:
        """
        get_item(self, asin: str, **kwargs) -> GetCatalogItemResponse
        Returns a specified item and its attributes.

        **Usage Plan:**

        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       1
        ======================================  ==============

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            asin: str
            key MarketplaceId: str
            **kwargs:

        Returns:
            GetCatalogItemResponse:
        """
        return GetCatalogItemResponse(
            **self._request(fill_query_params(kwargs.pop('path'), asin), params=kwargs).json()
        )

    @sp_endpoint('/catalog/v0/items')
    def list_items(self, **kwargs) -> ListCatalogItemsResponse:
        """
        list_items(self, **kwargs) -> ListCatalogItemsResponse
        Returns a list of items and their attributes, based on a search query or item identifiers that you specify. When based on a search query, provide the Query parameter and optionally, the QueryContextId parameter. When based on item identifiers, provide a single appropriate parameter based on the identifier type, and specify the associated item value. MarketplaceId is always required.

        **Usage Plan:**

        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       1
        ======================================  ==============


        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            key MarketplaceId: str
            key Query: str
            key QueryContextId: str
            key SellerSKU: str
            key UPC: str
            key EAN: str
            key ISBN: str
            key JAN: str

        Returns:
            ListCatalogItemsResponse:
        """
        return ListCatalogItemsResponse(
            **self._request(kwargs.pop('path'), params=kwargs).json()
        )
