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
        
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1.133 | 25 |
        
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        
        Args:
            key orderId:string | The identifier for the order.
            key shipmentId:string | The identifier for the shipment.
            body: | * REQUIRED {'description': 'The request schema for the `submitInvoice` operation.',
         'properties': {'contentMD5Value': {'description': 'MD5 sum for validating the invoice data. For more information about calculating this value, see [Working with Content-MD5 '
                                                           'Checksums](https://docs.developer.amazonservices.com/en_US/dev_guide/DG_MD5.html).',
                                            'type': 'string'},
                        'invoiceContent': {'$ref': '#/definitions/Blob', 'description': "The binary object representing an invoice's content."},
                        'invoiceType': {'$ref': '#/definitions/InvoiceType', 'description': 'The type of an invoice.'},
                        'marketplaceId': {'description': 'An Amazon marketplace identifier.', 'type': 'string'},
                        'programType': {'$ref': '#/definitions/ProgramType', 'description': 'The Amazon program that the seller is currently enrolled.'}},
         'required': ['contentMD5Value', 'invoiceContent', 'invoiceType', 'programType', 'marketplaceId'],
         'type': 'object'}
        
        Returns:
            ApiResponse:
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
        
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1.133 | 25 |
        
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        
        Args:
            key orderId:string | The order identifier.
            key shipmentId:string | The shipment identifier.
            key marketplaceId:string | * REQUIRED The marketplace identifier.
            key invoiceType:string | * REQUIRED The invoice's type.
            key programType:string | * REQUIRED The Amazon program that seller is currently enrolled.
        
        Returns:
            ApiResponse:
        """
        return await self._request(kwargs.pop("path"), params=kwargs, add_marketplace=False)
