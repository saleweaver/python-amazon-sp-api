from sp_api.api.catalog.models.get_catalog_item_response import GetCatalogItemResponse
from sp_api.api.catalog.models.list_catalog_items_response import ListCatalogItemsResponse
from sp_api.base import Client, sp_endpoint, Marketplaces, fill_query_params


class Catalog(Client):
    def __init__(self, marketplace=Marketplaces.US, *, refresh_token=None):
        super().__init__(marketplace, refresh_token)

    @sp_endpoint('/catalog/v0/items/{}')
    def get_item(self, asin, **kwargs):
        return GetCatalogItemResponse(
            **self._request(fill_query_params(kwargs.pop('path'), asin), params=kwargs).json()
        )

    @sp_endpoint('/catalog/v0/items')
    def list_items(self, **kwargs):
        return ListCatalogItemsResponse(
            **self._request(kwargs.pop('path'), params=kwargs).json()
        )
