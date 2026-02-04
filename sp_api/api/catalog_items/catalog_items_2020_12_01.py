from sp_api.base import Client, sp_endpoint, fill_query_params, ApiResponse
from sp_api.util import normalize_included_data


class CatalogItemsV20201201(Client):
    """
    CatalogItems SP-API Client
    :link:

    The Selling Partner API for Catalog Items provides programmatic access to information about items in the Amazon catalog.
    """

    @sp_endpoint("/catalog/2020-12-01/items", method="GET")
    def search_catalog_items(self, **kwargs) -> ApiResponse:
        """
        search_catalog_items(self, **kwargs) -> ApiResponse
        
        Search for and return a list of Amazon catalog items and associated information.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        2                                       2
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                CatalogItemsV20201201().search_catalog_items()
        
        Args:
            key keywords: object | required A comma-delimited list of words or item identifiers to search the Amazon catalog for.
            key marketplaceIds: object | required A comma-delimited list of Amazon marketplace identifiers for the request.
            key includedData: object |  A comma-delimited list of data sets to include in the response. Default: summaries.
            key brandNames: object |  A comma-delimited list of brand names to limit the search to.
            key classificationIds: object |  A comma-delimited list of classification identifiers to limit the search to.
            key pageSize: object |  Number of results to be returned per page.
            key pageToken: object |  A token to fetch a certain page when there are multiple pages worth of results.
            key keywordsLocale: object |  The language the keywords are provided in. Defaults to the primary locale of the marketplace.
            key locale: object |  Locale for retrieving localized summaries. Defaults to the primary locale of the marketplace.
        
        Returns:
            ApiResponse
        """

        normalize_included_data(kwargs)
        return self._request(kwargs.pop("path"), params=kwargs)

    @sp_endpoint("/catalog/2020-12-01/items/{}", method="GET")
    def get_catalog_item(self, asin, **kwargs) -> ApiResponse:
        """
        get_catalog_item(self, asin, **kwargs) -> ApiResponse
        
        Retrieves details for an item in the Amazon catalog.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        2                                       2
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                CatalogItemsV20201201().get_catalog_item("value")
        
        Args:
            asin: object | required The Amazon Standard Identification Number (ASIN) of the item.
            key marketplaceIds: object | required A comma-delimited list of Amazon marketplace identifiers. Data sets in the response contain data only for the specified marketplaces.
            key includedData: object |  A comma-delimited list of data sets to include in the response. Default: summaries.
            key locale: object |  Locale for retrieving localized summaries. Defaults to the primary locale of the marketplace.
        
        Returns:
            ApiResponse
        """

        normalize_included_data(kwargs)
        return self._request(fill_query_params(kwargs.pop("path"), asin), params=kwargs)
