import urllib.parse

from sp_api.base import Client, sp_endpoint, fill_query_params, ApiResponse
from sp_api.asyncio.base import AsyncBaseClient


class FulfillmentOutbound(AsyncBaseClient):
    """
    FulfillmentOutbound SP-API Client
    :link:

    The Selling Partner API for Fulfillment Outbound lets you create applications that help a seller fulfill Multi-Channel Fulfillment orders using their inventory in Amazon's fulfillment network. You can get information on both potential and existing fulfillment orders.
    """

    @sp_endpoint("/fba/outbound/2020-07-01/fulfillmentOrders/preview", method="POST")
    async def get_fulfillment_preview(self, **kwargs) -> ApiResponse:
        """
        get_fulfillment_preview(self, **kwargs) -> ApiResponse
        
        Returns a list of fulfillment order previews based on shipping criteria that you specify.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        2                                       30
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await FulfillmentOutbound().get_fulfillment_preview()
        
        Args:
            body: GetFulfillmentPreviewRequest | required GetFulfillmentPreviewRequest parameter
        
        Returns:
            ApiResponse
        """

        return await self._request(kwargs.pop("path"), data=kwargs)

    @sp_endpoint("/fba/outbound/2020-07-01/deliveryOffers", method="POST")
    async def delivery_offers(self, **kwargs) -> ApiResponse:
        """
        delivery_offers(self, **kwargs) -> ApiResponse
        
        Returns delivery options that include an estimated delivery date and offer expiration, based on criteria that you specify.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        5                                       30
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await FulfillmentOutbound().delivery_offers()
        
        Args:
            body: GetDeliveryOffersRequest | required GetDeliveryOffersRequest parameter
        
        Returns:
            ApiResponse
        """

        return await self._request(kwargs.pop("path"), data=kwargs)

    @sp_endpoint("/fba/outbound/2020-07-01/fulfillmentOrders", method="GET")
    async def list_all_fulfillment_orders(self, **kwargs) -> ApiResponse:
        """
        list_all_fulfillment_orders(self, **kwargs) -> ApiResponse
        
        Returns a list of fulfillment orders fulfilled after (or at) a specified date-time, or indicated by the `nextToken` parameter.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        2                                       30
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await FulfillmentOutbound().list_all_fulfillment_orders()
        
        Args:
            key queryStartDate: object |  A date used to select fulfillment orders that were last updated after (or at) a specified time. An update is defined as any change in fulfillment order status, including the creation of a new fulfillment order.
            key nextToken: object |  A string token returned in the response to your previous request.
        
        Returns:
            ApiResponse
        """

        return await self._request(kwargs.pop("path"), params=kwargs)

    @sp_endpoint("/fba/outbound/2020-07-01/fulfillmentOrders", method="POST")
    async def create_fulfillment_order(self, **kwargs) -> ApiResponse:
        """
        create_fulfillment_order(self, **kwargs) -> ApiResponse
        
        Requests that Amazon ship items from the seller's inventory in Amazon's fulfillment network to a destination address.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        2                                       30
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await FulfillmentOutbound().create_fulfillment_order()
        
        Args:
            body: CreateFulfillmentOrderRequest | required CreateFulfillmentOrderRequest parameter
        
        Returns:
            ApiResponse
        """

        return await self._request(kwargs.pop("path"), data=kwargs)

    @sp_endpoint("/fba/outbound/2020-07-01/tracking", method="GET")
    async def get_package_tracking_details(self, **kwargs) -> ApiResponse:
        """
        get_package_tracking_details(self, **kwargs) -> ApiResponse
        
        Returns delivery tracking information for a package in an outbound shipment for a Multi-Channel Fulfillment order.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        2                                       30
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await FulfillmentOutbound().get_package_tracking_details()
        
        Args:
            key packageNumber: object | required The unencrypted package identifier. You can obtain this value from the `getFulfillmentOrder` operation.
        
        Returns:
            ApiResponse
        """

        return await self._request(kwargs.pop("path"), params=kwargs)

    @sp_endpoint("/fba/outbound/2020-07-01/returnReasonCodes", method="GET")
    async def list_return_reason_codes(self, **kwargs) -> ApiResponse:
        """
        list_return_reason_codes(self, **kwargs) -> ApiResponse
        
        Returns a list of return reason codes for a seller SKU in a given marketplace. The parameters for this operation may contain special characters that require URL encoding. To avoid errors with SKUs when encoding URLs, refer to [URL Encoding](https://developer-docs.amazon.com/sp-api/docs/url-encoding).
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        2                                       30
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await FulfillmentOutbound().list_return_reason_codes()
        
        Args:
            key sellerSku: object | required The seller SKU for which return reason codes are required.
            key marketplaceId: object |  The marketplace for which the seller wants return reason codes.
            key sellerFulfillmentOrderId: object |  The identifier assigned to the item by the seller when the fulfillment order was created. The service uses this value to determine the marketplace for which the seller wants return reason codes.
            key language: object |  The language that the `TranslatedDescription` property of the `ReasonCodeDetails` response object should be translated into.
        
        Returns:
            ApiResponse
        """

        return await self._request(kwargs.pop("path"), params=kwargs)

    @sp_endpoint("/fba/outbound/2020-07-01/fulfillmentOrders/{}/return", method="PUT")
    async def create_fulfillment_return(
        self, sellerFulfillmentOrderId, **kwargs
    ) -> ApiResponse:
        """
        create_fulfillment_return(self, sellerFulfillmentOrderId, **kwargs) -> ApiResponse
        
        Creates a fulfillment return.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        2                                       30
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await FulfillmentOutbound().create_fulfillment_return("value")
        
        Args:
            body: CreateFulfillmentReturnRequest | required The request body of the `createFulfillmentReturn` operation.
            sellerFulfillmentOrderId: object | required An identifier the seller assigns to the fulfillment order at the time it was created. The seller uses their own records to find the correct `sellerFulfillmentOrderId` value based on the buyer's request to return items.
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), sellerFulfillmentOrderId), data=kwargs
        )

    @sp_endpoint("/fba/outbound/2020-07-01/fulfillmentOrders/{}", method="GET")
    async def get_fulfillment_order(self, sellerFulfillmentOrderId, **kwargs) -> ApiResponse:
        """
        get_fulfillment_order(self, sellerFulfillmentOrderId, **kwargs) -> ApiResponse
        
        Returns the fulfillment order indicated by the specified order identifier.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        2                                       30
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await FulfillmentOutbound().get_fulfillment_order("value")
        
        Args:
            sellerFulfillmentOrderId: object | required The identifier assigned to the item by the seller when the fulfillment order was created.
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), sellerFulfillmentOrderId),
            params=kwargs,
        )

    @sp_endpoint("/fba/outbound/2020-07-01/fulfillmentOrders/{}", method="PUT")
    async def update_fulfillment_order(
        self, sellerFulfillmentOrderId, **kwargs
    ) -> ApiResponse:
        """
        update_fulfillment_order(self, sellerFulfillmentOrderId, **kwargs) -> ApiResponse
        
        Updates and/or requests shipment for a fulfillment order with an order hold on it.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        2                                       30
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await FulfillmentOutbound().update_fulfillment_order("value")
        
        Args:
            body: UpdateFulfillmentOrderRequest | required The request body of the `updateFulfillmentOrder` operation.
            sellerFulfillmentOrderId: object | required The identifier assigned to the item by the seller when the fulfillment order was created.
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), sellerFulfillmentOrderId), data=kwargs
        )

    @sp_endpoint(
        "/fba/outbound/2020-07-01/fulfillmentOrders/{}/status", method="PUT"
    )
    async def submit_fulfillment_order_status_update(
        self, sellerFulfillmentOrderId, **kwargs
    ) -> ApiResponse:
        """
        submit_fulfillment_order_status_update(self, sellerFulfillmentOrderId, **kwargs) -> ApiResponse
        
        Requests that Amazon update the status of an order in the sandbox testing environment. This is a sandbox-only operation and must be directed to a sandbox endpoint. Refer to [Fulfillment Outbound Dynamic Sandbox Guide](https://developer-docs.amazon.com/sp-api/docs/fulfillment-outbound-dynamic-sandbox-guide) and [Selling Partner API sandbox](https://developer-docs.amazon.com/sp-api/docs/the-selling-partner-api-sandbox) for more information.
        
        Examples:
            literal blocks::
            
                await FulfillmentOutbound().submit_fulfillment_order_status_update("value")
        
        Args:
            sellerFulfillmentOrderId: object | required The identifier assigned to the item by the seller when the fulfillment order was created.
            body: SubmitFulfillmentOrderStatusUpdateRequest | required The identifier assigned to the item by the seller when the fulfillment order was created.
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), sellerFulfillmentOrderId), data=kwargs
        )

    @sp_endpoint("/fba/outbound/2020-07-01/fulfillmentOrders/{}/cancel", method="PUT")
    async def cancel_fulfillment_order(
        self, sellerFulfillmentOrderId, **kwargs
    ) -> ApiResponse:
        """
        cancel_fulfillment_order(self, sellerFulfillmentOrderId, **kwargs) -> ApiResponse
        
        Requests that Amazon stop attempting to fulfill the fulfillment order indicated by the specified order identifier.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        2                                       30
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await FulfillmentOutbound().cancel_fulfillment_order("value")
        
        Args:
            sellerFulfillmentOrderId: object | required The identifier assigned to the item by the seller when the fulfillment order was created.
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), sellerFulfillmentOrderId), data=kwargs
        )

    @sp_endpoint("/fba/outbound/2020-07-01/features", method="GET")
    async def get_features(self, **kwargs) -> ApiResponse:
        """
        get_features(self, **kwargs) -> ApiResponse
        
        Returns a list of features available for Multi-Channel Fulfillment orders in the marketplace you specify, and whether the seller for which you made the call is enrolled for each feature.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        2                                       30
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await FulfillmentOutbound().get_features()
        
        Args:
            key marketplaceId: object | required The marketplace for which to return the list of features.
        
        Returns:
            ApiResponse
        """

        return await self._request(kwargs.pop("path"), params=kwargs)

    @sp_endpoint("/fba/outbound/2020-07-01/features/inventory/{}", method="GET")
    async def get_feature_inventory(self, featureName, **kwargs) -> ApiResponse:
        """
        get_feature_inventory(self, featureName, **kwargs) -> ApiResponse
        
        Returns a list of inventory items that are eligible for the fulfillment feature you specify.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        2                                       30
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await FulfillmentOutbound().get_feature_inventory("value")
        
        Args:
            key marketplaceId: object | required The marketplace for which to return a list of the inventory that is eligible for the specified feature.
            featureName: object | required The name of the feature for which to return a list of eligible inventory.
            key nextToken: object |  A string token returned in the response to your previous request that is used to return the next response page. A value of `null` will return the first page.
            key queryStartDate: object |  A date that you can use to select inventory that has been updated since a specified date. An update is defined as any change in feature-enabled inventory availability. The date must be in the format `yyyy-MM-ddTHH:mm:ss.sssZ`
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), featureName), params=kwargs
        )

    @sp_endpoint(
        "/fba/outbound/2020-07-01/features/inventory/{}/{}", method="GET"
    )
    async def get_feature_sku(self, featureName, sellerSku, **kwargs) -> ApiResponse:
        """
        get_feature_sku(self, featureName, sellerSku, **kwargs) -> ApiResponse
        
        Returns the number of items with the `sellerSku` you specify that can have orders fulfilled using the specified feature. Note that if the `sellerSku` isn't eligible, the response will contain an empty `skuInfo` object. The parameters for this operation may contain special characters that require URL encoding. To avoid errors with SKUs when encoding URLs, refer to [URL Encoding](https://developer-docs.amazon.com/sp-api/docs/url-encoding).
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        2                                       30
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await FulfillmentOutbound().get_feature_sku("value", "value")
        
        Args:
            key marketplaceId: object | required The marketplace for which to return the count.
            featureName: object | required The name of the feature.
            sellerSku: object | required Used to identify an item in the given marketplace. `sellerSku` is qualified by the seller's `sellerId`, which is included with every operation that you submit.
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), featureName, sellerSku), params=kwargs
        )

    @sp_endpoint("/fba/outbound/2020-07-01/features/inventory/{}", method="GET")
    async def get_feature_s_k_u(self, featureName, **kwargs) -> ApiResponse:
        """
        get_feature_s_k_u(self, featureName, **kwargs) -> ApiResponse
        
        Returns a list of inventory items that are eligible for the fulfillment feature you specify.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        2                                       30
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await FulfillmentOutbound().get_feature_s_k_u("value")
        
        Args:
            key marketplaceId: object | required The marketplace for which to return a list of the inventory that is eligible for the specified feature.
            featureName: object | required The name of the feature for which to return a list of eligible inventory.
            key nextToken: object |  A string token returned in the response to your previous request that is used to return the next response page. A value of `null` will return the first page.
            key queryStartDate: object |  A date that you can use to select inventory that has been updated since a specified date. An update is defined as any change in feature-enabled inventory availability. The date must be in the format `yyyy-MM-ddTHH:mm:ss.sssZ`
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), featureName), params=kwargs
        )
