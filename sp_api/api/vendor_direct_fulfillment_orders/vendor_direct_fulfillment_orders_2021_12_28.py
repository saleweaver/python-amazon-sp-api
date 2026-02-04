import urllib.parse

from sp_api.base import Client, sp_endpoint, fill_query_params, ApiResponse


class VendorDirectFulfillmentOrdersV20211228(Client):
    """
    VendorDirectFulfillmentOrders SP-API Client
    :link:

    The Selling Partner API for Direct Fulfillment Orders provides programmatic access to a direct fulfillment vendor's order data.
    """

    @sp_endpoint("/vendor/directFulfillment/orders/2021-12-28/purchaseOrders", method="GET")
    def get_orders(self, **kwargs) -> ApiResponse:
        """
        get_orders(self, **kwargs) -> ApiResponse
        
        Returns a list of purchase orders created during the time frame that you specify. You define the time frame using the createdAfter and createdBefore parameters. You must use both parameters. You can choose to get only the purchase order numbers by setting the includeDetails parameter to false. In that case, the operation returns a list of purchase order numbers. You can then call the getOrder operation to return the details of a specific order.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        10                                      10
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                VendorDirectFulfillmentOrdersV20211228().get_orders()
        
        Args:
            key shipFromPartyId: object |  The vendor warehouse identifier for the fulfillment warehouse. If not specified, the result will contain orders for all warehouses.
            key status: object |  Returns only the purchase orders that match the specified status. If not specified, the result will contain orders that match any status.
            key limit: object |  The limit to the number of purchase orders returned.
            key createdAfter: object | required Purchase orders that became available after this date and time will be included in the result. Must be in ISO-8601 date/time format.
            key createdBefore: object | required Purchase orders that became available before this date and time will be included in the result. Must be in ISO-8601 date/time format.
            key sortOrder: object |  Sort the list in ascending or descending order by order creation date.
            key nextToken: object |  Used for pagination when there are more orders than the specified result size limit. The token value is returned in the previous API call.
            key includeDetails: object |  When true, returns the complete purchase order details. Otherwise, only purchase order numbers are returned.
        
        Returns:
            ApiResponse
        """

        return self._request(kwargs.pop("path"), params=kwargs)

    @sp_endpoint("/vendor/directFulfillment/orders/2021-12-28/purchaseOrders/{}", method="GET")
    def get_order(self, purchaseOrderNumber, **kwargs) -> ApiResponse:
        """
        get_order(self, purchaseOrderNumber, **kwargs) -> ApiResponse
        
        Returns purchase order information for the purchaseOrderNumber that you specify.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        10                                      10
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                VendorDirectFulfillmentOrdersV20211228().get_order("value")
        
        Args:
            purchaseOrderNumber: object | required The order identifier for the purchase order that you want. Formatting Notes: alpha-numeric code.
        
        Returns:
            ApiResponse
        """

        return self._request(
            fill_query_params(kwargs.pop("path"), purchaseOrderNumber), params=kwargs
        )

    @sp_endpoint("/vendor/directFulfillment/orders/2021-12-28/acknowledgements", method="POST")
    def submit_acknowledgement(self, **kwargs) -> ApiResponse:
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
            
                VendorDirectFulfillmentOrdersV20211228().submit_acknowledgement()
        
        Args:
            body: SubmitAcknowledgementRequest | required The request body containing the acknowledgement to an order
        
        Returns:
            ApiResponse
        """

        return self._request(kwargs.pop("path"), data=kwargs, add_marketplace=False)
