import urllib.parse

from sp_api.base import Client, sp_endpoint, fill_query_params, ApiResponse
from sp_api.asyncio.base import AsyncBaseClient


class VendorDirectFulfillmentPayments(AsyncBaseClient):
    """
    VendorDirectFulfillmentPayments SP-API Client
    :link:

    The Selling Partner API for Direct Fulfillment Payments provides programmatic access to a direct fulfillment vendor's invoice data.
    """

    @sp_endpoint("/vendor/directFulfillment/payments/v1/invoices", method="POST")
    async def submit_invoice(self, **kwargs) -> ApiResponse:
        """
        submit_invoice(self, **kwargs) -> ApiResponse
        
        Submits one or more invoices for a vendor's direct fulfillment orders.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        10                                      10
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await VendorDirectFulfillmentPayments().submit_invoice()
        
        Args:
            body: SubmitInvoiceRequest | required The request body containing one or more invoices for vendor orders.
        
        Returns:
            ApiResponse
        """

        return await self._request(kwargs.pop("path"), data=kwargs, add_marketplace=False)