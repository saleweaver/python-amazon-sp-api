from sp_api.base import Client, sp_endpoint, fill_query_params, ApiResponse
from sp_api.util import normalize_included_data


class CatalogItemsV20220401(Client):
    """
    CatalogItems SP-API Client
    :link:

    The Selling Partner API for Catalog Items provides programmatic access to information about items in the Amazon catalog.
    """

    @sp_endpoint("/catalog/2022-04-01/items", method="GET")
    def search_catalog_items(self, **kwargs) -> ApiResponse:
        """
        search_catalog_items(self, **kwargs) -> ApiResponse
        
        Search for a list of Amazon catalog items and item-related information. You can search by identifier or by keywords.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        2                                       2
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                CatalogItemsV20220401().search_catalog_items()
        
        Args:
            key identifiers: object |  A comma-delimited list of product identifiers that you can use to search the Amazon catalog. **Note:** You cannot include `identifiers` and `keywords` in the same request.
            key identifiersType: object |  The type of product identifiers that you can use to search the Amazon catalog. **Note:** `identifiersType` is required when `identifiers` is in the request.
            key marketplaceIds: object | required A comma-delimited list of Amazon marketplace identifiers. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).
            key includedData: object |  A comma-delimited list of datasets to include in the response.
            key locale: object |  The locale for which you want to retrieve localized summaries. Defaults to the primary locale of the marketplace.
            key sellerId: object |  A selling partner identifier, such as a seller account or vendor code. **Note:** Required when `identifiersType` is `SKU`.
            key keywords: object |  A comma-delimited list of keywords that you can use to search the Amazon catalog. **Note:** You cannot include `keywords` and `identifiers` in the same request.
            key brandNames: object |  A comma-delimited list of brand names that you can use to limit the search in queries based on `keywords`. **Note:** Cannot be used with `identifiers`.
            key classificationIds: object |  A comma-delimited list of classification identifiers that you can use to limit the search in queries based on `keywords`. **Note:** Cannot be used with `identifiers`.
            key pageSize: object |  The number of results to include on each page.
            key pageToken: object |  A token that you can use to fetch a specific page when there are multiple pages of results.
            key keywordsLocale: object |  The language of the keywords that are included in queries based on `keywords`. Defaults to the primary locale of the marketplace. **Note:** Cannot be used with `identifiers`.
        
        Returns:
            ApiResponse
        """

        normalize_included_data(kwargs)
        return self._request(kwargs.pop("path"), params=kwargs)

    @sp_endpoint("/catalog/2022-04-01/items/{}", method="GET")
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
            
                CatalogItemsV20220401().get_catalog_item("value")
        
        Args:
            asin: object | required The Amazon Standard Identification Number (ASIN) of the item.
            key marketplaceIds: object | required A comma-delimited list of Amazon marketplace identifiers. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).
            key includedData: object |  A comma-delimited list of datasets to include in the response.
            key locale: object |  The locale for which you want to retrieve localized summaries. Defaults to the primary locale of the marketplace.
        
        Returns:
            ApiResponse
        """

        normalize_included_data(kwargs)
        return self._request(fill_query_params(kwargs.pop("path"), asin), params=kwargs)
