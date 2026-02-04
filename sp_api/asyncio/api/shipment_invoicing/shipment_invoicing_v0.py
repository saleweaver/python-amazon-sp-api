from sp_api.base import ApiResponse, sp_endpoint, fill_query_params
from sp_api.asyncio.base import AsyncBaseClient


class ShipmentInvoicingV0(AsyncBaseClient):
    """
    ShipmentInvoicing SP-API Client
    :link:

    The Selling Partner API for Shipment Invoicing helps you programmatically retrieve shipment invoice information in the Brazil marketplace for a selling partner’s Fulfillment by Amazon (FBA) orders.
    """

    @sp_endpoint("/fba/outbound/brazil/v0/shipments/{shipmentId}", method="GET")
    async def get_shipment_details(self, shipmentId, **kwargs) -> ApiResponse:
        """
        get_shipment_details(self, shipmentId, **kwargs) -> ApiResponse
        
        Returns the shipment details required to issue an invoice for the specified shipment.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1.133                                   25
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await ShipmentInvoicingV0().get_shipment_details("value")
        
        Args:
            shipmentId: object | required The identifier for the shipment. Get this value from the FBAOutboundShipmentStatus notification. For information about subscribing to notifications, see the [Notifications API Use Case Guide](doc:notifications-api-v1-use-case-guide).
        
        Returns:
            ApiResponse
        """
        return await self._request(fill_query_params(kwargs.pop("path"), shipmentId), params=kwargs, add_marketplace=False)

    @sp_endpoint("/fba/outbound/brazil/v0/shipments/{shipmentId}/invoice", method="POST")
    async def submit_invoice(self, shipmentId, **kwargs) -> ApiResponse:
        """
        submit_invoice(self, shipmentId, **kwargs) -> ApiResponse
        
        Submits a shipment invoice document for a given shipment.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1.133                                   25
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await ShipmentInvoicingV0().submit_invoice("value")
        
        Args:
            shipmentId: object | required The identifier for the shipment.
            body: SubmitInvoiceRequest | required
        
        Returns:
            ApiResponse
        """
        return await self._request(fill_query_params(kwargs.pop("path"), shipmentId), data=kwargs, add_marketplace=False)

    @sp_endpoint("/fba/outbound/brazil/v0/shipments/{shipmentId}/invoice/status", method="GET")
    async def get_invoice_status(self, shipmentId, **kwargs) -> ApiResponse:
        """
        get_invoice_status(self, shipmentId, **kwargs) -> ApiResponse
        
        Returns the invoice status for the shipment you specify.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1.133                                   25
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await ShipmentInvoicingV0().get_invoice_status("value")
        
        Args:
            shipmentId: object | required The shipment identifier for the shipment.
        
        Returns:
            ApiResponse
        """
        return await self._request(fill_query_params(kwargs.pop("path"), shipmentId), params=kwargs, add_marketplace=False)
