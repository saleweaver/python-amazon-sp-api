from sp_api.base import (
    sp_endpoint,
    fill_query_params,
    ApiResponse,
    IncludedData,
)
from sp_api.util import normalize_included_data
from sp_api.asyncio.base import AsyncBaseClient


class ListingsItemsV20210801(AsyncBaseClient):
    """
        ListingsItems SP-API Client
        :link:

        The Selling Partner API for Listings Items (Listings Items API) provides programmatic access to selling partner listings on Amazon. Use this API in collaboration with the Selling Partner API for Product Type Definitions, which you use to retrieve the information about Amazon product types needed to use the Listings Items API.

    For more information, see the [Listings Items API Use Case Guide](https://github.com/amzn/selling-partner-api-docs/blob/main/guides/en-US/use-case-guides/listings-items-api-use-case-guide/listings-items-api-use-case-guide_2021-08-01.md).
    """

    @sp_endpoint("/listings/2021-08-01/items/{}/{}", method="DELETE")
    async def delete_listings_item(self, sellerId, sku, **kwargs) -> ApiResponse:
        """
        delete_listings_item(self, sellerId, sku, **kwargs) -> ApiResponse
        
        Delete a listings item for a selling partner.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        5                                       5
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await ListingsItemsV20210801().delete_listings_item("value", "value")
        
        Args:
            sellerId: object | required A selling partner identifier, such as a merchant account or vendor code.
            sku: object | required A selling partner provided identifier for an Amazon listing.
            key marketplaceIds: object | required A comma-delimited list of Amazon marketplace identifiers for the request.
            key issueLocale: object |  A locale for localization of issues. When not provided, the default language code of the first marketplace is used. Examples: `en_US`, `fr_CA`, `fr_FR`. Localized messages default to `en_US` when a localization is not available in the specified locale.
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), sellerId, sku), data=kwargs
        )

    @sp_endpoint("/listings/2021-08-01/items/{}/{}", method="GET")
    async def get_listings_item(self, sellerId, sku, **kwargs) -> ApiResponse:
        """
        get_listings_item(self, sellerId, sku, **kwargs) -> ApiResponse
        
        Returns details about a listings item for a selling partner.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        5                                       10
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await ListingsItemsV20210801().get_listings_item("value", "value")
        
        Args:
            sellerId: object | required A selling partner identifier, such as a merchant account or vendor code.
            sku: object | required A selling partner provided identifier for an Amazon listing.
            key marketplaceIds: object | required A comma-delimited list of Amazon marketplace identifiers for the request.
            key issueLocale: object |  A locale for localization of issues. When not provided, the default language code of the first marketplace is used. Examples: `en_US`, `fr_CA`, `fr_FR`. Localized messages default to `en_US` when a localization is not available in the specified locale.
            key includedData: object |  A comma-delimited list of data sets to include in the response. Default: `summaries`.
        
        Returns:
            ApiResponse
        """
        normalize_included_data(kwargs, enum_cls=IncludedData)

        return await self._request(
            fill_query_params(kwargs.pop("path"), sellerId, sku), params=kwargs
        )

    @sp_endpoint("/listings/2021-08-01/items/{}", method="GET")
    async def search_listings_items(self, sellerId, **kwargs) -> ApiResponse:
        """
        search_listings_items(self, sellerId, **kwargs) -> ApiResponse
        
        Search for and return a list of selling partner listings items and their respective details.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        5                                       5
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await ListingsItemsV20210801().search_listings_items("value")
        
        Args:
            sellerId: object | required A selling partner identifier, such as a merchant account or vendor code.
            key marketplaceIds: object | required A comma-delimited list of Amazon marketplace identifiers for the request.
            key issueLocale: object |  A locale that is used to localize issues. When not provided, the default language code of the first marketplace is used. Examples: "en_US", "fr_CA", "fr_FR". When a localization is not available in the specified locale, localized messages default to "en_US".
            key includedData: object |  A comma-delimited list of datasets that you want to include in the response. Default: `summaries`.
            key identifiers: object |  A comma-delimited list of product identifiers that you can use to search for listings items.
                **Note**:
                1. This is required when you specify `identifiersType`.
                2. You cannot use 'identifiers' if you specify `variationParentSku` or `packageHierarchySku`.
            key identifiersType: object |  A type of product identifiers that you can use to search for listings items.
                **Note**:
                This is required when `identifiers` is provided.
            key variationParentSku: object |  Filters results to include listing items that are variation children of the specified SKU.
                **Note**: You cannot use `variationParentSku` if you include `identifiers` or `packageHierarchySku` in your request.
            key packageHierarchySku: object |  Filter results to include listing items that contain or are contained by the specified SKU.
                **Note**: You cannot use `packageHierarchySku` if you include `identifiers` or `variationParentSku` in your request.
            key createdAfter: object |  A date-time that is used to filter listing items. The response includes listings items that were created at or after this time. Values are in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format.
            key createdBefore: object |  A date-time that is used to filter listing items. The response includes listings items that were created at or before this time. Values are in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format.
            key lastUpdatedAfter: object |  A date-time that is used to filter listing items. The response includes listings items that were last updated at or after this time. Values are in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format.
            key lastUpdatedBefore: object |  A date-time that is used to filter listing items. The response includes listings items that were last updated at or before this time. Values are in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format.
            key withIssueSeverity: object |  Filter results to include only listing items that have issues that match one or more of the specified severity levels.
            key withStatus: object |  Filter results to include only listing items that have the specified status.
            key withoutStatus: object |  Filter results to include only listing items that don't contain the specified statuses.
            key sortBy: object |  An attribute by which to sort the returned listing items.
            key sortOrder: object |  The order in which to sort the result items.
            key pageSize: object |  The number of results that you want to include on each page.
            key pageToken: object |  A token that you can use to fetch a specific page when there are multiple pages of results.
        
        Returns:
            ApiResponse
        """
        normalize_included_data(kwargs, enum_cls=IncludedData)

        return await self._request(
            fill_query_params(kwargs.pop("path"), sellerId), params=kwargs
        )

    @sp_endpoint("/listings/2021-08-01/items/{}/{}", method="PATCH")
    async def patch_listings_item(self, sellerId, sku, **kwargs) -> ApiResponse:
        """
        patch_listings_item(self, sellerId, sku, **kwargs) -> ApiResponse
        
        Partially update (patch) a listings item for a selling partner. Only top-level listings item attributes can be patched. Patching nested attributes is not supported.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        5                                       5
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await ListingsItemsV20210801().patch_listings_item("value", "value")
        
        Args:
            sellerId: object | required A selling partner identifier, such as a merchant account or vendor code.
            sku: object | required A selling partner provided identifier for an Amazon listing.
            key marketplaceIds: object | required A comma-delimited list of Amazon marketplace identifiers for the request.
            key includedData: object |  A comma-delimited list of data sets to include in the response. Default: `issues`.
            key mode: object |  The mode of operation for the request.
            key issueLocale: object |  A locale for localization of issues. When not provided, the default language code of the first marketplace is used. Examples: `en_US`, `fr_CA`, `fr_FR`. Localized messages default to `en_US` when a localization is not available in the specified locale.
            body: ListingsItemPatchRequest | required The request body schema for the `patchListingsItem` operation.
        
        Returns:
            ApiResponse
        """
        return await self._request(
            fill_query_params(kwargs.pop("path"), sellerId, sku),
            data=kwargs.pop("body"),
            params=kwargs,
        )

    @sp_endpoint("/listings/2021-08-01/items/{}/{}", method="PUT")
    async def put_listings_item(self, sellerId, sku, **kwargs) -> ApiResponse:
        """
        put_listings_item(self, sellerId, sku, **kwargs) -> ApiResponse
        
        Creates a new or fully-updates an existing listings item for a selling partner.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        5                                       10
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await ListingsItemsV20210801().put_listings_item("value", "value")
        
        Args:
            sellerId: object | required A selling partner identifier, such as a merchant account or vendor code.
            sku: object | required A selling partner provided identifier for an Amazon listing.
            key marketplaceIds: object | required A comma-delimited list of Amazon marketplace identifiers for the request.
            key includedData: object |  A comma-delimited list of data sets to include in the response. Default: `issues`.
            key mode: object |  The mode of operation for the request.
            key issueLocale: object |  A locale for localization of issues. When not provided, the default language code of the first marketplace is used. Examples: `en_US`, `fr_CA`, `fr_FR`. Localized messages default to `en_US` when a localization is not available in the specified locale.
            body: ListingsItemPutRequest | required The request body schema for the `putListingsItem` operation.
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), sellerId, sku),
            data=kwargs.pop("body"),
            params=kwargs,
        )
