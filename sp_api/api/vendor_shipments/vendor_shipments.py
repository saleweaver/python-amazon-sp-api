import urllib.parse

from sp_api.base import Client, sp_endpoint, fill_query_params, ApiResponse


class VendorShipments(Client):
    """
    VendorShipments SP-API Client
    :link:

    The Selling Partner API for Retail Procurement Shipments provides programmatic access to retail shipping data for vendors.
    """

    @sp_endpoint("/vendor/shipping/v1/shipmentConfirmations", method="POST")
    def submit_shipment_confirmations(self, **kwargs) -> ApiResponse:
        """
        submit_shipment_confirmations(self, **kwargs) -> ApiResponse

        Submits one or more shipment confirmations for vendor orders.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 10 | 10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

                Args:

                    body: | * REQUIRED {'description': 'The request schema for the SubmitShipmentConfirmations operation.',
         'properties': {'shipmentConfirmations': {'description': 'A list of one or more shipment confirmations.', 'items': {'$ref': '#/definitions/ShipmentConfirmation'}, 'type': 'array'}},
         'type': 'object'}


                Returns:
                    ApiResponse:
        """

        return self._request(kwargs.pop("path"), data=kwargs)

    @sp_endpoint("/vendor/shipping/v1/shipments", method="POST")
    def submit_shipments(self, **kwargs) -> ApiResponse:
        """
        submit_shipments(self, **kwargs) -> ApiResponse

        Submits one or more shipment request for vendor Orders.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 10 | 10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

                Args:

                    body: | * REQUIRED {'description': 'The request schema for the SubmitShipments operation.',
         'properties': {'shipments': {'description': 'A list of one or more shipments with underlying details.', 'items': {'$ref': '#/definitions/Shipment'}, 'type': 'array'}},
         'type': 'object'}


                Returns:
                    ApiResponse:
        """

        return self._request(kwargs.pop("path"), data=kwargs)

    @sp_endpoint("/vendor/shipping/v1/shipments", method="GET")
    def get_shipment_details(self, **kwargs) -> ApiResponse:
        """
        get_shipment_details(self, **kwargs) -> ApiResponse

        Returns the Details about Shipment, Carrier Details,  status of the shipment, container details and other details related to shipment based on the filter parameters value that you specify.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 10 | 10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:

            key limit:integer |  The limit to the number of records returned. Default value is 50 records.
            key sortOrder:string |  Sort in ascending or descending order by purchase order creation date.
            key nextToken:string |  Used for pagination when there are more shipments than the specified result size limit.
            key createdAfter:string |  Get Shipment Details that became available after this timestamp will be included in the result. Must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format.
            key createdBefore:string |  Get Shipment Details that became available before this timestamp will be included in the result. Must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format.
            key shipmentConfirmedBefore:string |  Get Shipment Details by passing Shipment confirmed create Date Before. Must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format.
            key shipmentConfirmedAfter:string |  Get Shipment Details by passing Shipment confirmed create Date After. Must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format.
            key packageLabelCreatedBefore:string |  Get Shipment Details by passing Package label create Date by buyer. Must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format.
            key packageLabelCreatedAfter:string |  Get Shipment Details by passing Package label create Date After by buyer. Must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format.
            key shippedBefore:string |  Get Shipment Details by passing Shipped Date Before. Must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format.
            key shippedAfter:string |  Get Shipment Details by passing Shipped Date After. Must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format.
            key estimatedDeliveryBefore:string |  Get Shipment Details by passing Estimated Delivery Date Before. Must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format.
            key estimatedDeliveryAfter:string |  Get Shipment Details by passing Estimated Delivery Date Before. Must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format.
            key shipmentDeliveryBefore:string |  Get Shipment Details by passing Shipment Delivery Date Before. Must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format.
            key shipmentDeliveryAfter:string |  Get Shipment Details by passing Shipment Delivery Date After. Must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format.
            key requestedPickUpBefore:string |  Get Shipment Details by passing Before Requested pickup date. Must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format.
            key requestedPickUpAfter:string |  Get Shipment Details by passing After Requested pickup date. Must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format.
            key scheduledPickUpBefore:string |  Get Shipment Details by passing Before scheduled pickup date. Must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format.
            key scheduledPickUpAfter:string |  Get Shipment Details by passing After Scheduled pickup date. Must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format.
            key currentShipmentStatus:string |  Get Shipment Details by passing Current shipment status.
            key vendorShipmentIdentifier:string |  Get Shipment Details by passing Vendor Shipment ID
            key buyerReferenceNumber:string |  Get Shipment Details by passing buyer Reference ID
            key buyerWarehouseCode:string |  Get Shipping Details based on buyer warehouse code. This value should be same as 'shipToParty.partyId' in the Shipment.
            key sellerWarehouseCode:string |  Get Shipping Details based on vendor warehouse code. This value should be same as 'sellingParty.partyId' in the Shipment.


        Returns:
            ApiResponse:
        """

        return self._request(kwargs.pop("path"), params=kwargs)
