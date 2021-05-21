import urllib.parse

from sp_api.base import Client, sp_endpoint, fill_query_params, ApiResponse


class VendorShipments(Client):
    """
    VendorShipments SP-API Client
    :link: 

    The Selling Partner API for Retail Procurement Shipments provides programmatic access to retail shipping data for vendors.
    """


    @sp_endpoint('/vendor/shipping/v1/shipmentConfirmations', method='POST')
    def submit_shipment_confirmations(self, **kwargs) -> ApiResponse:
        """
        submit_shipment_confirmations(self, **kwargs) -> ApiResponse

        Submits one or more shipment confirmations for vendor orders.

**Usage Plans:**

| Plan type | Rate (requests per second) | Burst |
| ---- | ---- | ---- |
|Default| 10 | 10 |
|Selling partner specific| Variable | Variable |

The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

         Args:
        
            body: | * REQUIRED {'description': 'The request schema for the SubmitShipmentConfirmations operation.', 'properties': {'shipmentConfirmations': {'items': {'$ref': '#/definitions/ShipmentConfirmation'}, 'type': 'array'}}, 'type': 'object'}
        

         Returns:
            ApiResponse:
        """
    
        return self._request(kwargs.pop('path'),  data=kwargs)
    
