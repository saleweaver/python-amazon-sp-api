import urllib.parse

from sp_api.base import Client, sp_endpoint, fill_query_params, ApiResponse


class ListingsItems(Client):
    """
    ListingsItems SP-API Client
    :link: 

    The Selling Partner API for Listings Items (Listings Items API) provides programmatic access to selling partner listings on Amazon. Use this API in collaboration with the Selling Partner API for Product Type Definitions, which you use to retrieve the information about Amazon product types needed to use the Listings Items API.
    """


    @sp_endpoint('/listings/2020-09-01/items/{}/{}', method='DELETE')
    def delete_listings_item(self, sellerId, sku, **kwargs) -> ApiResponse:
        """
        delete_listings_item(self, sellerId, **kwargs) -> ApiResponse

        Delete a listings item for a selling partner.

**Usage Plans:**

| Plan type | Rate (requests per second) | Burst |
| ---- | ---- | ---- |
|Default| 5 | 10 |
|Selling partner specific| Variable | Variable |

The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

         Args:
        
            sellerId:string | * REQUIRED A selling partner identifier, such as a merchant account or vendor code.
        
            sku:string | * REQUIRED A selling partner provided identifier for an Amazon listing.
        
            key marketplaceIds:array | * REQUIRED A comma-delimited list of Amazon marketplace identifiers for the request.
        
            key issueLocale:string |  A locale for localization of issues. When not provided, the default language code of the first marketplace is used. Examples: "en_US", "fr_CA", "fr_FR". Localized messages default to "en_US" when a localization is not available in the specified locale.
        

         Returns:
            ApiResponse:
        """
    
        return self._request(fill_query_params(kwargs.pop('path'), sellerId, sku), params=kwargs)
    

    @sp_endpoint('/listings/2020-09-01/items/{}/{}', method='PATCH')
    def patch_listings_item(self, sellerId, sku, **kwargs) -> ApiResponse:
        """
        patch_listings_item(self, sellerId, **kwargs) -> ApiResponse

        Partially update (patch) a listings item for a selling partner. Only top-level listings item attributes can be patched. Patching nested attributes is not supported.

**Usage Plans:**

| Plan type | Rate (requests per second) | Burst |
| ---- | ---- | ---- |
|Default| 5 | 10 |
|Selling partner specific| Variable | Variable |

The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

         Args:
        
            sellerId:string | * REQUIRED A selling partner identifier, such as a merchant account or vendor code.
        
            sku:string | * REQUIRED A selling partner provided identifier for an Amazon listing.
        
            key marketplaceIds:array | * REQUIRED A comma-delimited list of Amazon marketplace identifiers for the request.
        
            key issueLocale:string |  A locale for localization of issues. When not provided, the default language code of the first marketplace is used. Examples: "en_US", "fr_CA", "fr_FR". Localized messages default to "en_US" when a localization is not available in the specified locale.
        
            body: | * REQUIRED {'description': 'The request body schema for the patchListingsItem operation.',
 'properties': {'patches': {'description': 'One or more JSON Patch operations to perform on the listings item.', 'items': {'$ref': '#/definitions/PatchOperation'}, 'minItems': 1, 'type': 'array'},
                'productType': {'description': 'The Amazon product type of the listings item.', 'type': 'string'}},
 'required': ['productType', 'patches'],
 'type': 'object'}
        

         Returns:
            ApiResponse:
        """
    
        return self._request(fill_query_params(kwargs.pop('path'), sellerId, sku), data=kwargs.pop('body'), params=kwargs)
    

    @sp_endpoint('/listings/2020-09-01/items/{}/{}', method='PUT')
    def put_listings_item(self, sellerId, sku, **kwargs) -> ApiResponse:
        """
        put_listings_item(self, sellerId, **kwargs) -> ApiResponse

        Creates a new or fully-updates an existing listings item for a selling partner.

**Usage Plans:**

| Plan type | Rate (requests per second) | Burst |
| ---- | ---- | ---- |
|Default| 5 | 10 |
|Selling partner specific| Variable | Variable |

The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

         Args:
        
            sellerId:string | * REQUIRED A selling partner identifier, such as a merchant account or vendor code.
        
            sku:string | * REQUIRED A selling partner provided identifier for an Amazon listing.
        
            key marketplaceIds:array | * REQUIRED A comma-delimited list of Amazon marketplace identifiers for the request.
        
            key issueLocale:string |  A locale for localization of issues. When not provided, the default language code of the first marketplace is used. Examples: "en_US", "fr_CA", "fr_FR". Localized messages default to "en_US" when a localization is not available in the specified locale.
        
            body: | * REQUIRED {'description': 'The request body schema for the putListingsItem operation.',
 'properties': {'attributes': {'additionalProperties': True, 'description': 'JSON object containing structured listings item attribute data keyed by attribute name.', 'type': 'object'},
                'productType': {'description': 'The Amazon product type of the listings item.', 'type': 'string'},
                'requirements': {'description': 'The name of the requirements set for the provided data.',
                                 'enum': ['LISTING', 'LISTING_PRODUCT_ONLY', 'LISTING_OFFER_ONLY'],
                                 'type': 'string',
                                 'x-docgen-enum-table-extension': [{'description': 'Indicates the submitted data contains product facts and sales terms.', 'value': 'LISTING'},
                                                                   {'description': 'Indicates the submitted data contains product facts only.', 'value': 'LISTING_PRODUCT_ONLY'},
                                                                   {'description': 'Indicates the submitted data contains sales terms only.', 'value': 'LISTING_OFFER_ONLY'}]}},
 'required': ['productType', 'attributes'],
 'type': 'object'}
        

         Returns:
            ApiResponse:
        """
    
        return self._request(fill_query_params(kwargs.pop('path'), sellerId, sku), data=kwargs.pop('body'), params=kwargs)
    
