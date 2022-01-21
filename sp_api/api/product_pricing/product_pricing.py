import urllib.parse

from sp_api.base import Client, sp_endpoint, fill_query_params, ApiResponse


class ProductPricing(Client):
    """
    ProductPricing SP-API Client
    :link: 

    The Selling Partner API for Pricing helps you programmatically retrieve product pricing and offer information for Amazon Marketplace products.
    """


    @sp_endpoint('/products/pricing/v0/price', method='GET')
    def get_pricing(self, **kwargs) -> ApiResponse:
        """
        get_pricing(self, **kwargs) -> ApiResponse

        Returns pricing information for a seller's offer listings based on seller SKU or ASIN.

**Usage Plans:**

| Plan type | Rate (requests per second) | Burst |
| ---- | ---- | ---- |
|Default| 10 | 20 |
|Selling partner specific| Variable | Variable |

The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
        
            key MarketplaceId:string | * REQUIRED A marketplace identifier. Specifies the marketplace for which prices are returned.
        
            key Asins:array |  A list of up to twenty Amazon Standard Identification Number (ASIN) values used to identify items in the given marketplace.
        
            key Skus:array |  A list of up to twenty seller SKU values used to identify items in the given marketplace.
        
            key ItemType:string | * REQUIRED Indicates whether ASIN values or seller SKU values are used to identify items. If you specify Asin, the information in the response will be dependent on the list of Asins you provide in the Asins parameter. If you specify Sku, the information in the response will be dependent on the list of Skus you provide in the Skus parameter.
        
            key ItemCondition:string |  Filters the offer listings based on item condition. Possible values: New, Used, Collectible, Refurbished, Club.
        
            key OfferType:string |  Indicates whether to request pricing information for the seller's B2C or B2B offers. Default is B2C.
        

        Returns:
            ApiResponse:
        """
    
        return self._request(kwargs.pop('path'),  params=kwargs)
    

    @sp_endpoint('/products/pricing/v0/competitivePrice', method='GET')
    def get_competitive_pricing(self, **kwargs) -> ApiResponse:
        """
        get_competitive_pricing(self, **kwargs) -> ApiResponse

        Returns competitive pricing information for a seller's offer listings based on seller SKU or ASIN.

**Usage Plans:**

| Plan type | Rate (requests per second) | Burst |
| ---- | ---- | ---- |
|Default| 10 | 20 |
|Selling partner specific| Variable | Variable |

The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
        
            key MarketplaceId:string | * REQUIRED A marketplace identifier. Specifies the marketplace for which prices are returned.
        
            key Asins:array |  A list of up to twenty Amazon Standard Identification Number (ASIN) values used to identify items in the given marketplace.
        
            key Skus:array |  A list of up to twenty seller SKU values used to identify items in the given marketplace.
        
            key ItemType:string | * REQUIRED Indicates whether ASIN values or seller SKU values are used to identify items. If you specify Asin, the information in the response will be dependent on the list of Asins you provide in the Asins parameter. If you specify Sku, the information in the response will be dependent on the list of Skus you provide in the Skus parameter. Possible values: Asin, Sku.
        
            key CustomerType:string |  Indicates whether to request pricing information from the point of view of Consumer or Business buyers. Default is Consumer.
        

        Returns:
            ApiResponse:
        """
    
        return self._request(kwargs.pop('path'),  params=kwargs)
    

    @sp_endpoint('/products/pricing/v0/listings/{}/offers', method='GET')
    def get_listing_offers(self, SellerSKU, **kwargs) -> ApiResponse:
        """
        get_listing_offers(self, SellerSKU, **kwargs) -> ApiResponse

        Returns the lowest priced offers for a single SKU listing.

**Usage Plans:**

| Plan type | Rate (requests per second) | Burst |
| ---- | ---- | ---- |
|Default| 5 | 10 |
|Selling partner specific| Variable | Variable |

The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
        
            key MarketplaceId:string | * REQUIRED A marketplace identifier. Specifies the marketplace for which prices are returned.
        
            key ItemCondition:string | * REQUIRED Filters the offer listings based on item condition. Possible values: New, Used, Collectible, Refurbished, Club.
        
            SellerSKU:string | * REQUIRED Identifies an item in the given marketplace. SellerSKU is qualified by the seller's SellerId, which is included with every operation that you submit.
        
            key CustomerType:string |  Indicates whether to request Consumer or Business offers. Default is Consumer.
        

        Returns:
            ApiResponse:
        """
    
        return self._request(fill_query_params(kwargs.pop('path'), SellerSKU), params=kwargs)
    

    @sp_endpoint('/products/pricing/v0/items/{}/offers', method='GET')
    def get_item_offers(self, Asin, **kwargs) -> ApiResponse:
        """
        get_item_offers(self, Asin, **kwargs) -> ApiResponse

        Returns the lowest priced offers for a single item based on ASIN.

**Usage Plans:**

| Plan type | Rate (requests per second) | Burst |
| ---- | ---- | ---- |
|Default| 5 | 10 |
|Selling partner specific| Variable | Variable |

The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
        
            key MarketplaceId:string | * REQUIRED A marketplace identifier. Specifies the marketplace for which prices are returned.
        
            key ItemCondition:string | * REQUIRED Filters the offer listings to be considered based on item condition. Possible values: New, Used, Collectible, Refurbished, Club.
        
            Asin:string | * REQUIRED The Amazon Standard Identification Number (ASIN) of the item.
        
            key CustomerType:string |  Indicates whether to request Consumer or Business offers. Default is Consumer.
        

        Returns:
            ApiResponse:
        """
    
        return self._request(fill_query_params(kwargs.pop('path'), Asin), params=kwargs)
    
