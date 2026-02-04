import urllib.parse

from sp_api.base import Client, sp_endpoint, fill_query_params, ApiResponse


class ListingsRestrictions(Client):
    """
    ListingsRestrictions SP-API Client

    The Selling Partner API for Listings Restrictions provides programmatic access to restrictions on Amazon catalog listings.

    For more information, see the [Listings Restrictions API Use Case Guide](https://github.com/amzn/selling-partner-api-docs/blob/main/guides/en-US/use-case-guides/listings-restrictions-api-use-case-guide/listings-restrictions-api-use-case-guide_2021-08-01.md).
    """

    @sp_endpoint("/listings/2021-08-01/restrictions", method="GET")
    def get_listings_restrictions(self, **kwargs) -> ApiResponse:
        """
        get_listings_restrictions(self, **kwargs) -> ApiResponse
        
        Returns listing restrictions for an item in the Amazon Catalog.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        5                                       10
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                ListingsRestrictions().get_listings_restrictions()
        
        Args:
            key asin: object | required The Amazon Standard Identification Number (ASIN) of the item.
            key conditionType: object |  The condition used to filter restrictions.
            key sellerId: object | required A selling partner identifier, such as a merchant account.
            key marketplaceIds: object | required A comma-delimited list of Amazon marketplace identifiers for the request.
            key reasonLocale: object |  A locale for reason text localization. When not provided, the default language code of the first marketplace is used. Examples: "en_US", "fr_CA", "fr_FR". Localized messages default to "en_US" when a localization is not available in the specified locale.
        
        Returns:
            ApiResponse
        """

        return self._request(kwargs.pop("path"), params=kwargs)
