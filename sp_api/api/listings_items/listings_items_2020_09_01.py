from sp_api.base import (
    Client,
    sp_endpoint,
    fill_query_params,
    ApiResponse,
    IncludedData,
)
from sp_api.util import normalize_included_data


class ListingsItemsV20200901(Client):
    """
        ListingsItems SP-API Client
        :link:

        The Selling Partner API for Listings Items (Listings Items API) provides programmatic access to selling partner listings on Amazon. Use this API in collaboration with the Selling Partner API for Product Type Definitions, which you use to retrieve the information about Amazon product types needed to use the Listings Items API.

    For more information, see the [Listings Items API Use Case Guide](https://github.com/amzn/selling-partner-api-docs/blob/main/guides/en-US/use-case-guides/listings-items-api-use-case-guide/listings-items-api-use-case-guide_2020-09-01.md).
    """

    @sp_endpoint("/listings/2020-09-01/items/{}/{}", method="DELETE")
    def delete_listings_item(self, sellerId, sku, **kwargs) -> ApiResponse:
        """
        delete_listings_item(self, sellerId, sku, **kwargs) -> ApiResponse
        
        Delete a listings item for a selling partner.
        
        **Note:** The parameters associated with this operation may contain special characters that must be encoded to successfully call the API. To avoid errors with SKUs when encoding URLs, refer to [URL Encoding](https://developer-docs.amazon.com/sp-api/docs/url-encoding).
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        5                                       10
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                ListingsItemsV20200901().delete_listings_item("value", "value")
        
        Args:
            sellerId: object | required A selling partner identifier, such as a merchant account or vendor code.
            sku: object | required A selling partner provided identifier for an Amazon listing.
            key marketplaceIds: object | required A comma-delimited list of Amazon marketplace identifiers for the request.
            key issueLocale: object |  A locale for localization of issues. When not provided, the default language code of the first marketplace is used. Examples: "en_US", "fr_CA", "fr_FR". Localized messages default to "en_US" when a localization is not available in the specified locale.
        
        Returns:
            ApiResponse
        """

        return self._request(
            fill_query_params(kwargs.pop("path"), sellerId, sku), data=kwargs
        )

    @sp_endpoint("/listings/2020-09-01/items/{}/{}", method="GET")
    def get_listings_item(self, sellerId, sku, **kwargs) -> ApiResponse:
        """
        get_listings_item(self, sellerId, sku, **kwargs) -> ApiResponse
        
        Returns details about a listings item for a selling partner.
        
        Examples:
            literal blocks::
            
                ListingsItemsV20200901().get_listings_item("value", "value")
        
        Args:
            sellerId:  | required
            sku:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """
        normalize_included_data(kwargs, enum_cls=IncludedData)

        return self._request(
            fill_query_params(kwargs.pop("path"), sellerId, sku), params=kwargs
        )

    @sp_endpoint("/listings/2020-09-01/items/{}", method="GET")
    def search_listings_items(self, sellerId, **kwargs) -> ApiResponse:
        """
        search_listings_items(self, sellerId, **kwargs) -> ApiResponse
        
        Search for and return list of listings items and respective details for a selling partner.
        
        Examples:
            literal blocks::
            
                ListingsItemsV20200901().search_listings_items("value")
        
        Args:
            sellerId:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """
        normalize_included_data(kwargs, enum_cls=IncludedData)

        return self._request(
            fill_query_params(kwargs.pop("path"), sellerId), params=kwargs
        )

    @sp_endpoint("/listings/2020-09-01/items/{}/{}", method="PATCH")
    def patch_listings_item(self, sellerId, sku, **kwargs) -> ApiResponse:
        """
        patch_listings_item(self, sellerId, sku, **kwargs) -> ApiResponse
        
        Partially update (patch) a listings item for a selling partner. Only top-level listings item attributes can be patched. Patching nested attributes is not supported.
        
        **Note:** The parameters associated with this operation may contain special characters that must be encoded to successfully call the API. To avoid errors with SKUs when encoding URLs, refer to [URL Encoding](https://developer-docs.amazon.com/sp-api/docs/url-encoding).
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        5                                       10
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                ListingsItemsV20200901().patch_listings_item("value", "value")
        
        Args:
            sellerId: object | required A selling partner identifier, such as a merchant account or vendor code.
            sku: object | required A selling partner provided identifier for an Amazon listing.
            key marketplaceIds: object | required A comma-delimited list of Amazon marketplace identifiers for the request.
            key issueLocale: object |  A locale for localization of issues. When not provided, the default language code of the first marketplace is used. Examples: "en_US", "fr_CA", "fr_FR". Localized messages default to "en_US" when a localization is not available in the specified locale.
            body: ListingsItemPatchRequest | required The request body schema for the patchListingsItem operation.
        
        Returns:
            ApiResponse
        """
        return self._request(
            fill_query_params(kwargs.pop("path"), sellerId, sku),
            data=kwargs.pop("body"),
            params=kwargs,
        )

    @sp_endpoint("/listings/2020-09-01/items/{}/{}", method="PUT")
    def put_listings_item(self, sellerId, sku, **kwargs) -> ApiResponse:
        """
        put_listings_item(self, sellerId, sku, **kwargs) -> ApiResponse
        
        Creates a new or fully-updates an existing listings item for a selling partner.
        
        **Note:** The parameters associated with this operation may contain special characters that must be encoded to successfully call the API. To avoid errors with SKUs when encoding URLs, refer to [URL Encoding](https://developer-docs.amazon.com/sp-api/docs/url-encoding).
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        5                                       10
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                ListingsItemsV20200901().put_listings_item("value", "value")
        
        Args:
            sellerId: object | required A selling partner identifier, such as a merchant account or vendor code.
            sku: object | required A selling partner provided identifier for an Amazon listing.
            key marketplaceIds: object | required A comma-delimited list of Amazon marketplace identifiers for the request.
            key issueLocale: object |  A locale for localization of issues. When not provided, the default language code of the first marketplace is used. Examples: "en_US", "fr_CA", "fr_FR". Localized messages default to "en_US" when a localization is not available in the specified locale.
            body: ListingsItemPutRequest | required The request body schema for the putListingsItem operation.
        
        Returns:
            ApiResponse
        """

        return self._request(
            fill_query_params(kwargs.pop("path"), sellerId, sku),
            data=kwargs.pop("body"),
            params=kwargs,
        )
