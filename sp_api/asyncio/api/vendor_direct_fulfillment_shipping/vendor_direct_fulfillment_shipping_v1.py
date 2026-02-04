import urllib.parse

from sp_api.base import sp_endpoint, fill_query_params, ApiResponse
from sp_api.asyncio.base import AsyncBaseClient


class VendorDirectFulfillmentShippingV1(AsyncBaseClient):
    """
    VendorDirectFulfillmentShipping SP-API Client
    :link:

    The Selling Partner API for Direct Fulfillment Shipping provides programmatic access to a direct fulfillment vendor's shipping data.
    """

    @sp_endpoint("/vendor/directFulfillment/shipping/v1/shippingLabels", method="GET")
    async def get_shipping_labels(self, **kwargs) -> ApiResponse:
        """
        get_shipping_labels(self, **kwargs) -> ApiResponse
        
        Returns a list of shipping labels created during the time frame that you specify. You define that time frame using the createdAfter and createdBefore parameters. You must use both of these parameters. The date range to search must not be more than 7 days.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        10                                      10
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await VendorDirectFulfillmentShippingV1().get_shipping_labels()
        
        Args:
            key shipFromPartyId: object |  The vendor warehouseId for order fulfillment. If not specified, the result will contain orders for all warehouses.
            key limit: object |  The limit to the number of records returned.
            key createdAfter: object | required Shipping labels that became available after this date and time will be included in the result. Must be in ISO-8601 date/time format.
            key createdBefore: object | required Shipping labels that became available before this date and time will be included in the result. Must be in ISO-8601 date/time format.
            key sortOrder: object |  Sort ASC or DESC by order creation date.
            key nextToken: object |  Used for pagination when there are more ship labels than the specified result size limit. The token value is returned in the previous API call.
        
        Returns:
            ApiResponse
        """

        return await self._request(kwargs.pop("path"), params=kwargs)

    @sp_endpoint("/vendor/directFulfillment/shipping/v1/shippingLabels", method="POST")
    async def submit_shipping_label_request(self, **kwargs) -> ApiResponse:
        """
        submit_shipping_label_request(self, **kwargs) -> ApiResponse
        
        Creates a shipping label for a purchase order and returns a transactionId for reference.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        10                                      10
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await VendorDirectFulfillmentShippingV1().submit_shipping_label_request()
        
        Args:
            body: SubmitShippingLabelsRequest | required Request body containing one or more shipping labels data.
        
        Returns:
            ApiResponse
        """

        return await self._request(kwargs.pop("path"), data=kwargs, add_marketplace=False)

    @sp_endpoint(
        "/vendor/directFulfillment/shipping/v1/shippingLabels/{}", method="GET"
    )
    async def get_shipping_label(self, purchaseOrderNumber, **kwargs) -> ApiResponse:
        """
        get_shipping_label(self, purchaseOrderNumber, **kwargs) -> ApiResponse
        
        Returns a shipping label for the purchaseOrderNumber that you specify.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        10                                      10
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await VendorDirectFulfillmentShippingV1().get_shipping_label("value")
        
        Args:
            purchaseOrderNumber: object | required The purchase order number for which you want to return the shipping label. It should be the same purchaseOrderNumber as received in the order.
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), purchaseOrderNumber), params=kwargs
        )

    @sp_endpoint(
        "/vendor/directFulfillment/shipping/v1/shipmentConfirmations", method="POST"
    )
    async def submit_shipment_confirmations(self, **kwargs) -> ApiResponse:
        """
        submit_shipment_confirmations(self, **kwargs) -> ApiResponse
        
        Submits one or more shipment confirmations for vendor orders.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        10                                      10
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await VendorDirectFulfillmentShippingV1().submit_shipment_confirmations()
        
        Args:
            body: SubmitShipmentConfirmationsRequest | required Request body containing the shipment confirmations data.
        
        Returns:
            ApiResponse
        """

        return await self._request(kwargs.pop("path"), data=kwargs, add_marketplace=False)

    @sp_endpoint(
        "/vendor/directFulfillment/shipping/v1/shipmentStatusUpdates", method="POST"
    )
    async def submit_shipment_status_updates(self, **kwargs) -> ApiResponse:
        """
        submit_shipment_status_updates(self, **kwargs) -> ApiResponse
        
        This API call is only to be used by Vendor-Own-Carrier (VOC) vendors. Calling this API will submit a shipment status update for the package that a vendor has shipped. It will provide the Amazon customer visibility on their order, when the package is outside of Amazon Network visibility.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        10                                      10
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await VendorDirectFulfillmentShippingV1().submit_shipment_status_updates()
        
        Args:
            body: SubmitShipmentStatusUpdatesRequest | required Request body containing the shipment status update data.
        
        Returns:
            ApiResponse
        """

        return await self._request(kwargs.pop("path"), data=kwargs)

    @sp_endpoint("/vendor/directFulfillment/shipping/v1/customerInvoices", method="GET")
    async def get_customer_invoices(self, **kwargs) -> ApiResponse:
        """
        get_customer_invoices(self, **kwargs) -> ApiResponse
        
        Returns a list of customer invoices created during a time frame that you specify. You define the  time frame using the createdAfter and createdBefore parameters. You must use both of these parameters. The date range to search must be no more than 7 days.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        10                                      10
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await VendorDirectFulfillmentShippingV1().get_customer_invoices()
        
        Args:
            key shipFromPartyId: object |  The vendor warehouseId for order fulfillment. If not specified, the result will contain orders for all warehouses.
            key limit: object |  The limit to the number of records returned
            key createdAfter: object | required Orders that became available after this date and time will be included in the result. Must be in ISO-8601 date/time format.
            key createdBefore: object | required Orders that became available before this date and time will be included in the result. Must be in ISO-8601 date/time format.
            key sortOrder: object |  Sort ASC or DESC by order creation date.
            key nextToken: object |  Used for pagination when there are more orders than the specified result size limit. The token value is returned in the previous API call.
        
        Returns:
            ApiResponse
        """

        return await self._request(kwargs.pop("path"), params=kwargs)

    @sp_endpoint(
        "/vendor/directFulfillment/shipping/v1/customerInvoices/{}", method="GET"
    )
    async def get_customer_invoice(self, purchaseOrderNumber, **kwargs) -> ApiResponse:
        """
        get_customer_invoice(self, purchaseOrderNumber, **kwargs) -> ApiResponse
        
        Returns a customer invoice based on the purchaseOrderNumber that you specify.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        10                                      10
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await VendorDirectFulfillmentShippingV1().get_customer_invoice("value")
        
        Args:
            purchaseOrderNumber: object | required Purchase order number of the shipment for which to return the invoice.
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), purchaseOrderNumber), params=kwargs
        )

    @sp_endpoint("/vendor/directFulfillment/shipping/v1/packingSlips", method="GET")
    async def get_packing_slips(self, **kwargs) -> ApiResponse:
        """
        get_packing_slips(self, **kwargs) -> ApiResponse
        
        Returns a list of packing slips for the purchase orders that match the criteria specified. Date range to search must not be more than 7 days.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        10                                      10
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await VendorDirectFulfillmentShippingV1().get_packing_slips()
        
        Args:
            key shipFromPartyId: object |  The vendor warehouseId for order fulfillment. If not specified the result will contain orders for all warehouses.
            key limit: object |  The limit to the number of records returned
            key createdAfter: object | required Packing slips that became available after this date and time will be included in the result. Must be in ISO-8601 date/time format.
            key createdBefore: object | required Packing slips that became available before this date and time will be included in the result. Must be in ISO-8601 date/time format.
            key sortOrder: object |  Sort ASC or DESC by packing slip creation date.
            key nextToken: object |  Used for pagination when there are more packing slips than the specified result size limit. The token value is returned in the previous API call.
        
        Returns:
            ApiResponse
        """

        return await self._request(kwargs.pop("path"), params=kwargs)

    @sp_endpoint("/vendor/directFulfillment/shipping/v1/packingSlips/{}", method="GET")
    async def get_packing_slip(self, purchaseOrderNumber, **kwargs) -> ApiResponse:
        """
        get_packing_slip(self, purchaseOrderNumber, **kwargs) -> ApiResponse
        
        Returns a packing slip based on the purchaseOrderNumber that you specify.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        10                                      10
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await VendorDirectFulfillmentShippingV1().get_packing_slip("value")
        
        Args:
            purchaseOrderNumber: object | required The purchaseOrderNumber for the packing slip you want.
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), purchaseOrderNumber), params=kwargs
        )
