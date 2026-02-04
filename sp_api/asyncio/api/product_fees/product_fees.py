from typing import List
from urllib.parse import quote_plus

from sp_api.base.helpers import sp_endpoint, fill_query_params
from sp_api.base import ApiResponse
from sp_api.asyncio.base import AsyncBaseClient
from sp_api.util.product_fees import create_fees_body


class ProductFees(AsyncBaseClient):
    """
    :link: https://github.com/amzn/selling-partner-api-docs/tree/main/references/product-fees-api
    """

    @sp_endpoint("/products/fees/v0/listings/{}/feesEstimate", method="POST")
    async def get_product_fees_estimate_for_sku(
        self,
        seller_sku,
        price: float,
        shipping_price=None,
        currency="USD",
        is_fba=False,
        points: dict = None,
        marketplace_id: str = None,
        optional_fulfillment_program: str = None,
        force_safe_sku: bool = True,
        **kwargs
    ) -> ApiResponse:
        """
        get_product_fees_estimate_for_sku(self, seller_sku, price, shipping_price, currency, is_fba, points, marketplace_id, optional_fulfillment_program, force_safe_sku, **kwargs) -> ApiResponse
        
        Returns the estimated fees for the item indicated by the specified seller SKU in the marketplace specified in the request body.
        
        **Note:** The parameters associated with this operation may contain special characters that require URL encoding to call the API. To avoid errors with SKUs when encoding URLs, refer to [URL Encoding](https://developer-docs.amazon.com/sp-api/docs/url-encoding).
        
        You can call `getMyFeesEstimateForSKU` for an item on behalf of a selling partner before the selling partner sets the item's price. The selling partner can then take any estimated fees into account. Each fees estimate request must include an original identifier. This identifier is included in the fees estimate so that you can correlate a fees estimate with the original request.
        
        **Note:** This identifier value is used to identify an estimate. Actual costs may vary. Search "fees" in [Seller Central](https://sellercentral.amazon.com/) and consult the store-specific fee schedule for the most up-to-date information.
        
        **Note:** When sellers use the `getMyFeesEstimateForSKU` operation with their `SellerSKU`, they get accurate fees based on real item measurements, but only after they've sent their items to Amazon.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       2
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await ProductFees().get_product_fees_estimate_for_sku("value", "value", "value", "value", "value", "value", "value", "value", "value")
        
        Args:
            body: GetMyFeesEstimateRequest | required The request body schema for the getMyFeesEstimates operation
            SellerSKU: object | required Used to identify an item in the given marketplace. SellerSKU is qualified by the seller's SellerId, which is included with every operation that you submit.
        
        Returns:
            ApiResponse
        """

        if force_safe_sku:
            # handle `forward slash` issue in SKU
            seller_sku = quote_plus(seller_sku)

        kwargs.update(
            create_fees_body(
                price=price,
                shipping_price=shipping_price,
                currency=currency,
                is_fba=is_fba,
                identifier=seller_sku,
                points=points,
                marketplace_id=marketplace_id or self.marketplace_id,
                optional_fulfillment_program=optional_fulfillment_program,
            )
        )
        return await self._request(
            fill_query_params(kwargs.pop("path"), seller_sku), data=kwargs
        )

    @sp_endpoint("/products/fees/v0/items/{}/feesEstimate", method="POST")
    async def get_product_fees_estimate_for_asin(
        self,
        asin,
        price: float,
        currency="USD",
        shipping_price=None,
        is_fba=False,
        points: dict = None,
        marketplace_id: str = None,
        optional_fulfillment_program: str = None,
        **kwargs
    ) -> ApiResponse:
        """
        get_product_fees_estimate_for_asin(self, asin, price, currency, shipping_price, is_fba, points, marketplace_id, optional_fulfillment_program, **kwargs) -> ApiResponse
        
        Returns the estimated fees for the item indicated by the specified ASIN in the marketplace specified in the request body.
        
        You can call `getMyFeesEstimateForASIN` for an item on behalf of a selling partner before the selling partner sets the item's price. The selling partner can then take estimated fees into account. Each fees request must include an original identifier. This identifier is included in the fees estimate so you can correlate a fees estimate with the original request.
        
        **Note:** This identifier value is used to identify an estimate. Actual costs may vary. Search "fees" in [Seller Central](https://sellercentral.amazon.com/) and consult the store-specific fee schedule for the most up-to-date information.
        
        **Note:** When using the `getMyFeesEstimateForASIN` operation with an ASIN, the fee estimates might be different. This is because these estimates use the item's catalog size, which might not always match the actual size of the item sent to Amazon.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       2
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await ProductFees().get_product_fees_estimate_for_asin("value", "value", "value", "value", "value", "value", "value", "value")
        
        Args:
            body: GetMyFeesEstimateRequest | required The request body schema for the getMyFeesEstimates operation
            Asin: object | required The Amazon Standard Identification Number (ASIN) of the item.
        
        Returns:
            ApiResponse
        """
        kwargs.update(
            create_fees_body(
                price=price,
                shipping_price=shipping_price,
                currency=currency,
                is_fba=is_fba,
                identifier=asin,
                points=points,
                marketplace_id=marketplace_id or self.marketplace_id,
                optional_fulfillment_program=optional_fulfillment_program,
            )
        )
        return await self._request(fill_query_params(kwargs.pop("path"), asin), data=kwargs)

    @sp_endpoint("/products/fees/v0/feesEstimate", method="POST")
    async def get_my_fees_estimates(
        self, estimate_requests: List[dict], **kwargs
    ) -> ApiResponse:
        """
        get_my_fees_estimates(self, estimate_requests, **kwargs) -> ApiResponse
        
        Returns the estimated fees for a list of products.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        0.5                                     1
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await ProductFees().get_my_fees_estimates("value")
        
        Args:
            body: GetMyFeesEstimatesRequest | required The request body schema for the getMyFeesEstimates operation
        
        Returns:
            ApiResponse
        """
        kwargs.pop("path", None)
        kwargs.pop("method", None)
        return await self.get_product_fees_estimate(estimate_requests)

    async def get_product_fees_estimate(self, estimate_requests: List[dict]) -> ApiResponse:
        """
        get_product_fees_estimate(self, estimate_requests) -> ApiResponse
        
        Return fees for multiple products
        
        Examples:
            literal blocks::
            
                await ProductFees().get_product_fees_estimate("value")
        
        Args:
            estimate_requests:  | required
        
        Returns:
            ApiResponse
        """
        data = []
        for estimate in estimate_requests:
            estimate_payload = dict(estimate)
            marketplace_id = estimate_payload.pop("marketplace_id", None)
            data.append(
                dict(
                    **create_fees_body(
                        marketplace_id=marketplace_id or self.marketplace_id,
                        **estimate_payload,
                    )
                )
            )
        return await self._request(
            "/products/fees/v0/feesEstimate",
            data=data,
            params=dict(method="POST"),
            add_marketplace=False,
            wrap_list=True,
        )

    def _add_marketplaces(self, data):
        # MarketplaceID is a property of the body's FeesEstimateRequest for this section, and does
        # not need to be added. Additionally, Client._add_marketplaces will fail as it assumes
        # data is a dict, which is not the case for get_product_fees_estimate.
        pass
