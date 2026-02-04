import urllib.parse

from sp_api.base import Client, sp_endpoint, fill_query_params, ApiResponse


class VendorInvoices(Client):
    """
    VendorInvoices SP-API Client
    :link:

    The Selling Partner API for Retail Procurement Payments provides programmatic access to vendors payments data.
    """

    @sp_endpoint("/vendor/payments/v1/invoices", method="POST")
    def submit_invoices(self, data, **kwargs) -> ApiResponse:
        """
        submit_invoices(self, data, **kwargs) -> ApiResponse
        
        Submit new invoices to Amazon.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        10                                      10
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                VendorInvoices().submit_invoices("value")
        
        Args:
            body: SubmitInvoicesRequest | required The request body containing the invoice data to submit.
        
        Returns:
            ApiResponse
        """

        return self._request(
            kwargs.pop("path"), data={**data, **kwargs}, add_marketplace=False
        )
