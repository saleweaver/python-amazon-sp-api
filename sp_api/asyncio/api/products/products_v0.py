from typing import Optional, List, Dict, Union

from sp_api.base import ApiResponse, fill_query_params, sp_endpoint
from sp_api.asyncio.base import AsyncBaseClient
from sp_api.api.products.products_definitions import (
    GetItemOffersBatchRequest,
    GetListingOffersBatchRequest,
)
from sp_api.util import ensure_csv


class ProductsV0(AsyncBaseClient):
    """
    :links:
        https://github.com/amzn/selling-partner-api-docs/blob/main/references/product-pricing-api/productPricingV0.md
        https://developer-docs.amazon.com/sp-api/docs/product-pricing-api-v2022-05-01-reference
    """

    @sp_endpoint("/products/pricing/v0/price", method="GET")
    async def get_product_pricing_for_skus(
        self, seller_sku_list: [str], item_condition=None, offer_type=None, **kwargs
    ) -> ApiResponse:
        """
        get_product_pricing_for_skus(self, seller_sku_list, item_condition, offer_type, **kwargs) -> ApiResponse
        
        Returns pricing information for a seller's offer listings based on seller SKU or ASIN.
        
        **Note:** The parameters associated with this operation may contain special characters that require URL encoding to call the API. To avoid errors with SKUs when encoding URLs, refer to [URL Encoding](https://developer-docs.amazon.com/sp-api/docs/url-encoding).
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        0.5                                     1
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await ProductsV0().get_product_pricing_for_skus("value", "value", "value")
        
        Args:
            key MarketplaceId: object | required A marketplace identifier. Specifies the marketplace for which prices are returned.
            key Asins: object |  A list of up to twenty Amazon Standard Identification Number (ASIN) values used to identify items in the given marketplace.
            key Skus: object |  A list of up to twenty seller SKU values used to identify items in the given marketplace.
            key ItemType: object | required Indicates whether ASIN values or seller SKU values are used to identify items. If you specify Asin, the information in the response will be dependent on the list of Asins you provide in the Asins parameter. If you specify Sku, the information in the response will be dependent on the list of Skus you provide in the Skus parameter.
            key ItemCondition: object |  Filters the offer listings based on item condition. Possible values: New, Used, Collectible, Refurbished, Club.
            key OfferType: object |  Indicates whether to request pricing information for the seller's B2C or B2B offers. Default is B2C.
        
        Returns:
            ApiResponse
        """
        if item_condition is not None:
            kwargs["ItemCondition"] = item_condition
        if offer_type is not None:
            kwargs["OfferType"] = offer_type

        return await self._create_get_pricing_request(seller_sku_list, "Sku", **kwargs)

    @sp_endpoint("/products/pricing/v0/price", method="GET")
    async def get_product_pricing_for_asins(
        self, asin_list: [str], item_condition=None, offer_type=None, **kwargs
    ) -> ApiResponse:
        """
        get_product_pricing_for_asins(self, asin_list, item_condition, offer_type, **kwargs) -> ApiResponse
        
        Returns pricing information for a seller's offer listings based on seller SKU or ASIN.
        
        **Note:** The parameters associated with this operation may contain special characters that require URL encoding to call the API. To avoid errors with SKUs when encoding URLs, refer to [URL Encoding](https://developer-docs.amazon.com/sp-api/docs/url-encoding).
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        0.5                                     1
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await ProductsV0().get_product_pricing_for_asins("value", "value", "value")
        
        Args:
            key MarketplaceId: object | required A marketplace identifier. Specifies the marketplace for which prices are returned.
            key Asins: object |  A list of up to twenty Amazon Standard Identification Number (ASIN) values used to identify items in the given marketplace.
            key Skus: object |  A list of up to twenty seller SKU values used to identify items in the given marketplace.
            key ItemType: object | required Indicates whether ASIN values or seller SKU values are used to identify items. If you specify Asin, the information in the response will be dependent on the list of Asins you provide in the Asins parameter. If you specify Sku, the information in the response will be dependent on the list of Skus you provide in the Skus parameter.
            key ItemCondition: object |  Filters the offer listings based on item condition. Possible values: New, Used, Collectible, Refurbished, Club.
            key OfferType: object |  Indicates whether to request pricing information for the seller's B2C or B2B offers. Default is B2C.
        
        Returns:
            ApiResponse
        """
        if item_condition is not None:
            kwargs["ItemCondition"] = item_condition
        if offer_type is not None:
            kwargs["OfferType"] = offer_type

        return await self._create_get_pricing_request(asin_list, "Asin", **kwargs)

    @sp_endpoint("/products/pricing/v0/competitivePrice", method="GET")
    async def get_competitive_pricing_for_skus(
        self, seller_sku_list: [str], customer_type=None, **kwargs
    ) -> ApiResponse:
        """
        get_competitive_pricing_for_skus(self, seller_sku_list, customer_type, **kwargs) -> ApiResponse
        
        Returns competitive pricing information for a seller's offer listings based on seller SKU or ASIN.
        
        **Note:** The parameters associated with this operation may contain special characters that require URL encoding to call the API. To avoid errors with SKUs when encoding URLs, refer to [URL Encoding](https://developer-docs.amazon.com/sp-api/docs/url-encoding).
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        0.5                                     1
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await ProductsV0().get_competitive_pricing_for_skus("value", "value")
        
        Args:
            key MarketplaceId: object | required A marketplace identifier. Specifies the marketplace for which prices are returned.
            key Asins: object |  A list of up to twenty Amazon Standard Identification Number (ASIN) values used to identify items in the given marketplace.
            key Skus: object |  A list of up to twenty seller SKU values used to identify items in the given marketplace.
            key ItemType: object | required Indicates whether ASIN values or seller SKU values are used to identify items. If you specify Asin, the information in the response will be dependent on the list of Asins you provide in the Asins parameter. If you specify Sku, the information in the response will be dependent on the list of Skus you provide in the Skus parameter. Possible values: Asin, Sku.
            key CustomerType: object |  Indicates whether to request pricing information from the point of view of Consumer or Business buyers. Default is Consumer.
        
        Returns:
            ApiResponse
        """

        if customer_type is not None:
            kwargs["CustomerType"] = customer_type

        return await self._create_get_pricing_request(seller_sku_list, "Sku", **kwargs)

    @sp_endpoint("/products/pricing/v0/competitivePrice", method="GET")
    async def get_competitive_pricing_for_asins(
        self, asin_list: [str], customer_type=None, **kwargs
    ) -> ApiResponse:
        """
        get_competitive_pricing_for_asins(self, asin_list, customer_type, **kwargs) -> ApiResponse
        
        Returns competitive pricing information for a seller's offer listings based on seller SKU or ASIN.
        
        **Note:** The parameters associated with this operation may contain special characters that require URL encoding to call the API. To avoid errors with SKUs when encoding URLs, refer to [URL Encoding](https://developer-docs.amazon.com/sp-api/docs/url-encoding).
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        0.5                                     1
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await ProductsV0().get_competitive_pricing_for_asins("value", "value")
        
        Args:
            key MarketplaceId: object | required A marketplace identifier. Specifies the marketplace for which prices are returned.
            key Asins: object |  A list of up to twenty Amazon Standard Identification Number (ASIN) values used to identify items in the given marketplace.
            key Skus: object |  A list of up to twenty seller SKU values used to identify items in the given marketplace.
            key ItemType: object | required Indicates whether ASIN values or seller SKU values are used to identify items. If you specify Asin, the information in the response will be dependent on the list of Asins you provide in the Asins parameter. If you specify Sku, the information in the response will be dependent on the list of Skus you provide in the Skus parameter. Possible values: Asin, Sku.
            key CustomerType: object |  Indicates whether to request pricing information from the point of view of Consumer or Business buyers. Default is Consumer.
        
        Returns:
            ApiResponse
        """
        if customer_type is not None:
            kwargs["CustomerType"] = customer_type

        return await self._create_get_pricing_request(asin_list, "Asin", **kwargs)

    @sp_endpoint("/products/pricing/v0/listings/{}/offers", method="GET")
    async def get_listings_offer(
        self, seller_sku: str, item_condition: str, customer_type: str = None, **kwargs
    ) -> ApiResponse:
        """
        get_listings_offer(self, seller_sku, item_condition, customer_type, **kwargs) -> ApiResponse
        
        Returns the lowest priced offers for a single SKU listing.
        
        **Note:** The parameters associated with this operation may contain special characters that require URL encoding to call the API. To avoid errors with SKUs when encoding URLs, refer to [URL Encoding](https://developer-docs.amazon.com/sp-api/docs/url-encoding).
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       2
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await ProductsV0().get_listings_offer("value", "value", "value")
        
        Args:
            key MarketplaceId: object | required A marketplace identifier. Specifies the marketplace for which prices are returned.
            key ItemCondition: object | required Filters the offer listings based on item condition. Possible values: New, Used, Collectible, Refurbished, Club.
            SellerSKU: object | required Identifies an item in the given marketplace. SellerSKU is qualified by the seller's SellerId, which is included with every operation that you submit.
            key CustomerType: object |  Indicates whether to request Consumer or Business offers. Default is Consumer.
        
        Returns:
            ApiResponse
        """
        kwargs["ItemCondition"] = item_condition

        if customer_type is not None:
            kwargs["CustomerType"] = customer_type

        return await self._request(
            fill_query_params(kwargs.pop("path"), seller_sku), params={**kwargs}
        )

    @sp_endpoint("/products/pricing/v0/items/{}/offers", method="GET")
    async def get_item_offers(
        self, asin: str, item_condition: str, customer_type: str = None, **kwargs
    ) -> ApiResponse:
        """
        get_item_offers(self, asin, item_condition, customer_type, **kwargs) -> ApiResponse
        
        Returns the lowest priced offers for a single item based on ASIN.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        0.5                                     1
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await ProductsV0().get_item_offers("value", "value", "value")
        
        Args:
            key MarketplaceId: object | required A marketplace identifier. Specifies the marketplace for which prices are returned.
            key ItemCondition: object | required Filters the offer listings to be considered based on item condition. Possible values: New, Used, Collectible, Refurbished, Club.
            Asin: object | required The Amazon Standard Identification Number (ASIN) of the item.
            key CustomerType: object |  Indicates whether to request Consumer or Business offers. Default is Consumer.
        
        Returns:
            ApiResponse
        """
        kwargs["ItemCondition"] = item_condition

        if customer_type is not None:
            kwargs["CustomerType"] = customer_type

        return await self._request(
            fill_query_params(kwargs.pop("path"), asin), params={**kwargs}
        )

    @sp_endpoint("/batches/products/pricing/v0/itemOffers", method="POST")
    async def get_item_offers_batch(
        self,
        requests_: Optional[Union[List[Dict], GetItemOffersBatchRequest]] = None,
        **kwargs,
    ) -> ApiResponse:
        """
        get_item_offers_batch(self, requests_, **kwargs) -> ApiResponse
        
        Returns the lowest priced offers for a batch of items based on ASIN.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        0.1                                     1
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await ProductsV0().get_item_offers_batch("value")
        
        Args:
            getItemOffersBatchRequestBody: GetItemOffersBatchRequest | required The request associated with the `getItemOffersBatch` API call.
        
        Returns:
            ApiResponse
        """
        if isinstance(requests_, GetItemOffersBatchRequest):
            get_item_offers_batch_request = requests_.to_dict()
        else:
            get_item_offers_batch_request = {"requests": requests_}

        return await self._request(
            kwargs.pop("path"),
            data=get_item_offers_batch_request,
            params={**kwargs},
            add_marketplace=False,
        )

    @sp_endpoint("/batches/products/pricing/v0/listingOffers", method="POST")
    async def get_listing_offers_batch(
        self,
        requests_: Optional[Union[List[Dict], GetListingOffersBatchRequest]] = None,
        **kwargs,
    ) -> ApiResponse:
        """
        get_listing_offers_batch(self, requests_, **kwargs) -> ApiResponse
        
        Returns the lowest priced offers for a batch of listings by SKU.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        0.5                                     1
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await ProductsV0().get_listing_offers_batch("value")
        
        Args:
            getListingOffersBatchRequestBody: GetListingOffersBatchRequest | required The request associated with the `getListingOffersBatch` API call.
        
        Returns:
            ApiResponse
        """
        if isinstance(requests_, GetListingOffersBatchRequest):
            get_listing_offers_batch_request = requests_.to_dict()
        else:
            get_listing_offers_batch_request = {"requests": requests_}

        return await self._request(
            kwargs.pop("path"),
            data=get_listing_offers_batch_request,
            params={**kwargs},
            add_marketplace=False,
        )

    async def _create_get_pricing_request(self, item_list, item_type, **kwargs):
        items_csv = ensure_csv(item_list)
        return await self._request(
            kwargs.pop("path"),
            params={
                **{f"{item_type}s": items_csv},
                "ItemType": item_type,
                **(
                    {"ItemCondition": kwargs.pop("ItemCondition")}
                    if "ItemCondition" in kwargs
                    else {}
                ),
                **(
                    {"CustomerType": kwargs.pop("CustomerType")}
                    if "CustomerType" in kwargs
                    else {}
                ),
                **(
                    {"OfferType": kwargs.pop("OfferType")}
                    if "OfferType" in kwargs
                    else {}
                ),
                "MarketplaceId": kwargs.get("MarketplaceId", self.marketplace_id),
            },
        )
