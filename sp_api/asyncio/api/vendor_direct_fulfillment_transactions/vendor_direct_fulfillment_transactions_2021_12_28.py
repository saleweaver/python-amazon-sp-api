from sp_api.asyncio.base import AsyncBaseClient

import urllib.parse

from sp_api.base import sp_endpoint, fill_query_params, ApiResponse


class VendorDirectFulfillmentTransactionsV20211228(AsyncBaseClient):
    """
    VendorDirectFulfillmentTransactions SP-API Client
    :link:

    The Selling Partner API for Direct Fulfillment Transaction Status provides programmatic access to a direct fulfillment vendor's transaction status.
    """

    @sp_endpoint(
        "/vendor/directFulfillment/transactions/2021-12-28/transactions/{}", method="GET"
    )
    async def get_transaction_status(self, transactionId, **kwargs) -> ApiResponse:
        """
        get_transaction_status(self, transactionId, **kwargs) -> ApiResponse
        
        Returns the status of the transaction indicated by the specified transactionId.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        10                                      10
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await VendorDirectFulfillmentTransactionsV20211228().get_transaction_status("value")
        
        Args:
            transactionId: object | required Previously returned in the response to the POST request of a specific transaction.
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), transactionId), params=kwargs
        )
