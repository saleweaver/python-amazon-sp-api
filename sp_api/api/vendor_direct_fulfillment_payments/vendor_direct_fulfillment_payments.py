import urllib.parse

from sp_api.base import Client, sp_endpoint, fill_query_params, ApiResponse


class VendorDirectFulfillmentPayments(Client):
    """
    VendorDirectFulfillmentPayments SP-API Client
    :link: 

    The Selling Partner API for Direct Fulfillment Payments provides programmatic access to a direct fulfillment vendor's invoice data.
    """


    @sp_endpoint('/vendor/directFulfillment/payments/v1/invoices', method='POST')
    def submit_invoice(self, **kwargs) -> ApiResponse:
        """
        submit_invoice(self, **kwargs) -> ApiResponse

        Submits one or more invoices for a vendor's direct fulfillment orders.

**Usage Plans:**

| Plan type | Rate (requests per second) | Burst |
| ---- | ---- | ---- |
|Default| 10 | 10 |
|Selling partner specific| Variable | Variable |

The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

         Args:
        
            body: | * REQUIRED {'description': 'The request schema for the submitInvoice operation.', 'properties': {'invoices': {'items': {'$ref': '#/definitions/InvoiceDetail'}, 'type': 'array'}}, 'type': 'object'}
        

         Returns:
            ApiResponse:
        """
    
        return self._request(kwargs.pop('path'),  data=kwargs)
    
