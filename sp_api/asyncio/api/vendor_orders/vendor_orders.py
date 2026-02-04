import urllib.parse

from sp_api.base import Client, sp_endpoint, fill_query_params, ApiResponse
from sp_api.asyncio.base import AsyncBaseClient


class VendorOrders(AsyncBaseClient):
    """
    VendorOrders SP-API Client
    :link:

    The Selling Partner API for Retail Procurement Orders provides programmatic access to vendor orders data.
    """

    @sp_endpoint("/vendor/orders/v1/purchaseOrders", method="GET")
    async def get_purchase_orders(self, **kwargs) -> ApiResponse:
        """
        get_purchase_orders(self, **kwargs) -> ApiResponse
        
        Returns a list of purchase orders created or changed during the time frame that you specify. You define the time frame using the `createdAfter`, `createdBefore`, `changedAfter` and `changedBefore` parameters. The date range to search must not be more than 7 days. You can choose to get only the purchase order numbers by setting `includeDetails` to false. You can then use the `getPurchaseOrder` operation to receive details for a specific purchase order.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        10                                      10
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await VendorOrders().get_purchase_orders()
        
        Args:
            key limit: object |  The limit to the number of records returned. Default value is 100 records.
            key createdAfter: object |  Purchase orders that became available after this time will be included in the result. Must be in ISO-8601 date/time format.
            key createdBefore: object |  Purchase orders that became available before this time will be included in the result. Must be in ISO-8601 date/time format.
            key sortOrder: object |  Sort in ascending or descending order by purchase order creation date.
            key nextToken: object |  Used for pagination when there is more purchase orders than the specified result size limit. The token value is returned in the previous API call
            key includeDetails: object |  When true, returns purchase orders with complete details. Otherwise, only purchase order numbers are returned. Default value is true.
            key changedAfter: object |  Purchase orders that changed after this timestamp will be included in the result. Must be in ISO-8601 date/time format.
            key changedBefore: object |  Purchase orders that changed before this timestamp will be included in the result. Must be in ISO-8601 date/time format.
            key poItemState: object |  Current state of the purchase order item. If this value is Cancelled, this API will return purchase orders which have one or more items cancelled by Amazon with updated item quantity as zero.
            key isPOChanged: object |  When true, returns purchase orders which were modified after the order was placed. Vendors are required to pull the changed purchase order and fulfill the updated purchase order and not the original one. Default value is false.
            key purchaseOrderState: object |  Filters purchase orders based on the purchase order state.
            key orderingVendorCode: object |  Filters purchase orders based on the specified ordering vendor code. This value should be same as 'sellingParty.partyId' in the purchase order. If not included in the filter, all purchase orders for all of the vendor codes that exist in the vendor group used to authorize the API client application are returned.
        
        Returns:
            ApiResponse
        """

        return await self._request(kwargs.pop("path"), params=kwargs)

    @sp_endpoint("/vendor/orders/v1/purchaseOrders/{}", method="GET")
    async def get_purchase_order(self, purchaseOrderNumber, **kwargs) -> ApiResponse:
        """
        get_purchase_order(self, purchaseOrderNumber, **kwargs) -> ApiResponse
        
        Returns a purchase order based on the `purchaseOrderNumber` value that you specify.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        10                                      10
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await VendorOrders().get_purchase_order("value")
        
        Args:
            purchaseOrderNumber: object | required The purchase order identifier for the order that you want. Formatting Notes: 8-character alpha-numeric code.
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), purchaseOrderNumber), params=kwargs
        )

    @sp_endpoint("/vendor/orders/v1/acknowledgements", method="POST")
    async def submit_acknowledgement(self, **kwargs) -> ApiResponse:
        """
        submit_acknowledgement(self, **kwargs) -> ApiResponse
        
        Submits acknowledgements for one or more purchase orders.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        10                                      10
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await VendorOrders().submit_acknowledgement()
        
        Args:
            body: SubmitAcknowledgementRequest | required Submits acknowledgements for one or more purchase orders from a vendor.
        
        Returns:
            ApiResponse
        """

        return await self._request(kwargs.pop("path"), data=kwargs, add_marketplace=False)

    @sp_endpoint("/vendor/orders/v1/purchaseOrdersStatus", method="GET")
    async def get_purchase_orders_status(self, **kwargs) -> ApiResponse:
        """
        get_purchase_orders_status(self, **kwargs) -> ApiResponse
        
        Returns purchase order statuses based on the filters that you specify. Date range to search must not be more than 7 days. You can return a list of purchase order statuses using the available filters, or a single purchase order status by providing the purchase order number.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        10                                      10
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await VendorOrders().get_purchase_orders_status()
        
        Args:
            key limit: object |  The limit to the number of records returned. Default value is 100 records.
            key sortOrder: object |  Sort in ascending or descending order by purchase order creation date.
            key nextToken: object |  Used for pagination when there are more purchase orders than the specified result size limit.
            key createdAfter: object |  Purchase orders that became available after this timestamp will be included in the result. Must be in ISO-8601 date/time format.
            key createdBefore: object |  Purchase orders that became available before this timestamp will be included in the result. Must be in ISO-8601 date/time format.
            key updatedAfter: object |  Purchase orders for which the last purchase order update happened after this timestamp will be included in the result. Must be in ISO-8601 date/time format.
            key updatedBefore: object |  Purchase orders for which the last purchase order update happened before this timestamp will be included in the result. Must be in ISO-8601 date/time format.
            key purchaseOrderNumber: object |  Provides purchase order status for the specified purchase order number.
            key purchaseOrderStatus: object |  Filters purchase orders based on the specified purchase order status. If not included in filter, this will return purchase orders for all statuses.
            key itemConfirmationStatus: object |  Filters purchase orders based on their item confirmation status. If the item confirmation status is not included in the filter, purchase orders for all confirmation statuses are included.
            key itemReceiveStatus: object |  Filters purchase orders based on the purchase order's item receive status. If the item receive status is not included in the filter, purchase orders for all receive statuses are included.
            key orderingVendorCode: object |  Filters purchase orders based on the specified ordering vendor code. This value should be same as 'sellingParty.partyId' in the purchase order. If not included in filter, all purchase orders for all the vendor codes that exist in the vendor group used to authorize API client application are returned.
            key shipToPartyId: object |  Filters purchase orders for a specific buyer's Fulfillment Center/warehouse by providing ship to location id here. This value should be same as 'shipToParty.partyId' in the purchase order. If not included in filter, this will return purchase orders for all the buyer's warehouses used for vendor group purchase orders.
        
        Returns:
            ApiResponse
        """

        return await self._request(kwargs.pop("path"), params=kwargs)
