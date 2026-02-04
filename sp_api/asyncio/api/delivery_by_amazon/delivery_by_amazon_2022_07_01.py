from sp_api.base import ApiResponse, sp_endpoint, fill_query_params
from sp_api.asyncio.base import AsyncBaseClient


class DeliveryByAmazonV20220701(AsyncBaseClient):
    """
    DeliveryByAmazon SP-API Client
    :link:

    The Selling Partner API for Delivery Shipment Invoicing helps you programmatically retrieve shipment invoice information in the Brazil marketplace for a selling partner’s orders.
    """

    @sp_endpoint("/delivery/2022-07-01/invoice", method="POST")
    async def submit_invoice(self, **kwargs) -> ApiResponse:
        """
        submit_invoice(self, **kwargs) -> ApiResponse
        
        Submits a shipment invoice for a given order or shipment. You must specify either an `orderId` or `shipmentId` as query parameter. If both parameters are supplied, `orderId` takes precedence over `shipmentId`.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1.133                                   25
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await DeliveryByAmazonV20220701().submit_invoice()
        
        Args:
            key orderId: object |  The identifier for the order.
            key shipmentId: object |  The identifier for the shipment.
            body: SubmitInvoiceRequest | required The request body that specifies invoice, program and marketplace values.
        
        Returns:
            ApiResponse
        """
        params = {}
        if "orderId" in kwargs:
            params["orderId"] = kwargs.pop("orderId")
        if "shipmentId" in kwargs:
            params["shipmentId"] = kwargs.pop("shipmentId")
        return await self._request(kwargs.pop("path"), params=params, data=kwargs, add_marketplace=False)

    @sp_endpoint("/delivery/2022-07-01/invoice/status", method="GET")
    async def get_invoice_status(self, **kwargs) -> ApiResponse:
        """
        get_invoice_status(self, **kwargs) -> ApiResponse
        
        Returns the invoice status for the order or shipment you specify. You must specify either an `orderId` or `shipmentId` as query parameter. If both parameters are supplied, `orderId` takes precedence over `shipmentId`.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1.133                                   25
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await DeliveryByAmazonV20220701().get_invoice_status()
        
        Args:
            key orderId: object |  The order identifier.
            key shipmentId: object |  The shipment identifier.
            key marketplaceId: object | required The marketplace identifier.
            key invoiceType: object | required The invoice's type.
            key programType: object | required The Amazon program that seller is currently enrolled.
        
        Returns:
            ApiResponse
        """
        return await self._request(kwargs.pop("path"), params=kwargs, add_marketplace=False)
