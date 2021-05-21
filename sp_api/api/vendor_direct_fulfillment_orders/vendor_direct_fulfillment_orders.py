import urllib.parse

from sp_api.base import Client, sp_endpoint, fill_query_params, ApiResponse


class VendorDirectFulfillmentOrders(Client):
    """
    VendorDirectFulfillmentOrders SP-API Client
    :link: 

    The Selling Partner API for Direct Fulfillment Orders provides programmatic access to a direct fulfillment vendor's order data.
    """


    @sp_endpoint('/vendor/directFulfillment/orders/v1/purchaseOrders', method='GET')
    def get_orders(self, **kwargs) -> ApiResponse:
        """
        get_orders(self, **kwargs) -> ApiResponse

        Returns a list of purchase orders created during the time frame that you specify. You define the time frame using the createdAfter and createdBefore parameters. You must use both parameters. You can choose to get only the purchase order numbers by setting the includeDetails parameter to false. In that case, the operation returns a list of purchase order numbers. You can then call the getOrder operation to return the details of a specific order.

**Usage Plans:**

| Plan type | Rate (requests per second) | Burst |
| ---- | ---- | ---- |
|Default| 10 | 10 |
|Selling partner specific| Variable | Variable |

The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

         Args:
        
            key shipFromPartyId:string |  The vendor warehouse identifier for the fulfillment warehouse. If not specified, the result will contain orders for all warehouses.
        
            key status:string |  Returns only the purchase orders that match the specified status. If not specified, the result will contain orders that match any status.
        
            key limit:integer |  The limit to the number of purchase orders returned.
        
            key createdAfter:string | * REQUIRED Purchase orders that became available after this date and time will be included in the result. Must be in ISO-8601 date/time format.
        
            key createdBefore:string | * REQUIRED Purchase orders that became available before this date and time will be included in the result. Must be in ISO-8601 date/time format.
        
            key sortOrder:string |  Sort the list in ascending or descending order by order creation date.
        
            key nextToken:string |  Used for pagination when there are more orders than the specified result size limit. The token value is returned in the previous API call.
        
            key includeDetails:string |  When true, returns the complete purchase order details. Otherwise, only purchase order numbers are returned.
        

         Returns:
            ApiResponse:
        """
    
        return self._request(kwargs.pop('path'),  params=kwargs)
    

    @sp_endpoint('/vendor/directFulfillment/orders/v1/purchaseOrders/{}', method='GET')
    def get_order(self, purchaseOrderNumber, **kwargs) -> ApiResponse:
        """
        get_order(self, purchaseOrderNumber, **kwargs) -> ApiResponse

        Returns purchase order information for the purchaseOrderNumber that you specify.

**Usage Plans:**

| Plan type | Rate (requests per second) | Burst |
| ---- | ---- | ---- |
|Default| 10 | 10 |
|Selling partner specific| Variable | Variable |

The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

         Args:
        
            purchaseOrderNumber:string | * REQUIRED The order identifier for the purchase order that you want. Formatting Notes: alpha-numeric code.
        

         Returns:
            ApiResponse:
        """
    
        return self._request(fill_query_params(kwargs.pop('path'), purchaseOrderNumber), params=kwargs)
    

    @sp_endpoint('/vendor/directFulfillment/orders/v1/acknowledgements', method='POST')
    def submit_acknowledgement(self, **kwargs) -> ApiResponse:
        """
        submit_acknowledgement(self, **kwargs) -> ApiResponse

        Submits acknowledgements for one or more purchase orders.

**Usage Plans:**

| Plan type | Rate (requests per second) | Burst |
| ---- | ---- | ---- |
|Default| 10 | 10 |
|Selling partner specific| Variable | Variable |

The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

         Args:
        
            body: | * REQUIRED {'description': 'The request schema for the submitAcknowledgement operation.',
 'properties': {'orderAcknowledgements': {'description': 'A list of one or more purchase orders.', 'items': {'$ref': '#/definitions/OrderAcknowledgementItem'}, 'type': 'array'}},
 'type': 'object'}
        

         Returns:
            ApiResponse:
        """
    
        return self._request(kwargs.pop('path'),  data=kwargs)
    
