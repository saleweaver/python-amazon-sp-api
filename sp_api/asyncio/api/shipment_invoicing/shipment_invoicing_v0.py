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
        
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1.133 | 25 |
        
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        
        Args:
            shipmentId:string | * REQUIRED The identifier for the shipment. Get this value from the FBAOutboundShipmentStatus notification. For information about subscribing to notifications, see the [Notifications API Use Case Guide](doc:notifications-api-v1-use-case-guide).
        
        Returns:
            ApiResponse:
        """
        return await self._request(fill_query_params(kwargs.pop("path"), shipmentId), params=kwargs, add_marketplace=False)

    @sp_endpoint("/fba/outbound/brazil/v0/shipments/{shipmentId}/invoice", method="POST")
    async def submit_invoice(self, shipmentId, **kwargs) -> ApiResponse:
        """
        submit_invoice(self, shipmentId, **kwargs) -> ApiResponse
        
        Submits a shipment invoice document for a given shipment.
        
        **Usage Plan:**
        
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1.133 | 25 |
        
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        
        Args:
            shipmentId:string | * REQUIRED The identifier for the shipment.
            body: | * REQUIRED {'description': 'The request schema for the submitInvoice operation.',
         'properties': {'ContentMD5Value': {'description': 'MD5 sum for validating the invoice data. For more information about calculating this value, see [Working with Content-MD5 '
                                                           'Checksums](https://docs.developer.amazonservices.com/en_US/dev_guide/DG_MD5.html).',
                                            'type': 'string'},
                        'InvoiceContent': {'$ref': '#/definitions/Blob'},
                        'MarketplaceId': {'description': 'An Amazon marketplace identifier.', 'type': 'string'}},
         'required': ['ContentMD5Value', 'InvoiceContent'],
         'type': 'object'}
        
        Returns:
            ApiResponse:
        """
        return await self._request(fill_query_params(kwargs.pop("path"), shipmentId), data=kwargs, add_marketplace=False)

    @sp_endpoint("/fba/outbound/brazil/v0/shipments/{shipmentId}/invoice/status", method="GET")
    async def get_invoice_status(self, shipmentId, **kwargs) -> ApiResponse:
        """
        get_invoice_status(self, shipmentId, **kwargs) -> ApiResponse
        
        Returns the invoice status for the shipment you specify.
        
        **Usage Plan:**
        
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1.133 | 25 |
        
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        
        Args:
            shipmentId:string | * REQUIRED The shipment identifier for the shipment.
        
        Returns:
            ApiResponse:
        """
        return await self._request(fill_query_params(kwargs.pop("path"), shipmentId), params=kwargs, add_marketplace=False)
