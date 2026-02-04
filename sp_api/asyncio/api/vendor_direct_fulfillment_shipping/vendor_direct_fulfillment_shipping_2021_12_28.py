import urllib.parse

from sp_api.base import sp_endpoint, fill_query_params, ApiResponse
from sp_api.asyncio.base import AsyncBaseClient


class VendorDirectFulfillmentShippingV20211228(AsyncBaseClient):
    """
    VendorDirectFulfillmentShipping SP-API Client
    :link:

    The Selling Partner API for Direct Fulfillment Shipping provides programmatic access to a direct fulfillment vendor's shipping data.
    """

    @sp_endpoint("/vendor/directFulfillment/shipping/2021-12-28/shippingLabels", method="GET")
    async def get_shipping_labels(self, **kwargs) -> ApiResponse:
        """
        get_shipping_labels(self, **kwargs) -> ApiResponse

        Returns a list of shipping labels created during the time frame that you specify. You define that time frame using the createdAfter and createdBefore parameters. You must use both of these parameters. The date range to search must not be more than 7 days.

        **Usage Plans:**

        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        10                                      10
        ======================================  ==============

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            key shipFromPartyId:string |  The vendor warehouseId for order fulfillment. If not specified, the result will contain orders for all warehouses.
            key limit:integer |  The limit to the number of records returned.
            key createdAfter:string | * REQUIRED Shipping labels that became available after this date and time will be included in the result. Must be in ISO-8601 date/time format.
            key createdBefore:string | * REQUIRED Shipping labels that became available before this date and time will be included in the result. Must be in ISO-8601 date/time format.
            key sortOrder:string |  Sort ASC or DESC by order creation date.
            key nextToken:string |  Used for pagination when there are more ship labels than the specified result size limit. The token value is returned in the previous API call.

        Returns:
            ApiResponse:
        """

        return await self._request(kwargs.pop("path"), params=kwargs)


    @sp_endpoint("/vendor/directFulfillment/shipping/2021-12-28/shippingLabels", method="POST")
    async def submit_shipping_label_request(self, **kwargs) -> ApiResponse:
        """
        submit_shipping_label_request(self, **kwargs) -> ApiResponse

        Creates a shipping label for a purchase order and returns a transactionId for reference.

        **Usage Plans:**


        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        10                                      10
        ======================================  ==============

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            body: {
              "shippingLabelRequests": [
                {
                  "purchaseOrderNumber": "string",
                  "sellingParty": {
                    "partyId": "string",
                    "address": {
                      "name": "string",
                      "addressLine1": "string",
                      "addressLine2": "string",
                      "addressLine3": "string",
                      "city": "string",
                      "county": "string",
                      "district": "string",
                      "stateOrRegion": "string",
                      "postalCode": "string",
                      "countryCode": "string",
                      "phone": "string"
                    },
                    "taxRegistrationDetails": [
                      {
                        "taxRegistrationType": "VAT",
                        "taxRegistrationNumber": "string",
                        "taxRegistrationAddress": {
                          "name": "string",
                          "addressLine1": "string",
                          "addressLine2": "string",
                          "addressLine3": "string",
                          "city": "string",
                          "county": "string",
                          "district": "string",
                          "stateOrRegion": "string",
                          "postalCode": "string",
                          "countryCode": "string",
                          "phone": "string"
                        },
                        "taxRegistrationMessages": "string"
                      }
                    ]
                  },
                  "shipFromParty": {
                    "partyId": "string",
                    "address": {
                      "name": "string",
                      "addressLine1": "string",
                      "addressLine2": "string",
                      "addressLine3": "string",
                      "city": "string",
                      "county": "string",
                      "district": "string",
                      "stateOrRegion": "string",
                      "postalCode": "string",
                      "countryCode": "string",
                      "phone": "string"
                    },
                    "taxRegistrationDetails": [
                      {
                        "taxRegistrationType": "VAT",
                        "taxRegistrationNumber": "string",
                        "taxRegistrationAddress": {
                          "name": "string",
                          "addressLine1": "string",
                          "addressLine2": "string",
                          "addressLine3": "string",
                          "city": "string",
                          "county": "string",
                          "district": "string",
                          "stateOrRegion": "string",
                          "postalCode": "string",
                          "countryCode": "string",
                          "phone": "string"
                        },
                        "taxRegistrationMessages": "string"
                      }
                    ]
                  },
                  "containers": [
                    {
                      "containerType": "carton",
                      "containerIdentifier": "string",
                      "trackingNumber": "string",
                      "manifestId": "string",
                      "manifestDate": "string",
                      "shipMethod": "string",
                      "scacCode": "string",
                      "carrier": "string",
                      "containerSequenceNumber": 0,
                      "dimensions": {
                        "length": "string",
                        "width": "string",
                        "height": "string",
                        "unitOfMeasure": "IN"
                      },
                      "weight": {
                        "unitOfMeasure": "KG",
                        "value": "string"
                      },
                      "packedItems": [
                        {
                          "itemSequenceNumber": 0,
                          "buyerProductIdentifier": "string",
                          "vendorProductIdentifier": "string",
                          "packedQuantity": {
                            "amount": 0,
                            "unitOfMeasure": "string"
                          }
                        }
                      ]
                    }
                  ]
                }
              ]
            }

        Returns:
            ApiResponse:
        """

        return await self._request(kwargs.pop("path"), data=kwargs, add_marketplace=False)

    @sp_endpoint(
        "/vendor/directFulfillment/shipping/2021-12-28/shippingLabels/{}", method="GET"
    )
    async def get_shipping_label(self, purchaseOrderNumber, **kwargs) -> ApiResponse:
        """
        get_shipping_label(self, purchaseOrderNumber, **kwargs) -> ApiResponse

        Returns a shipping label for the purchaseOrderNumber that you specify.

        **Usage Plans:**


        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        10                                      10
        ======================================  ==============

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            purchaseOrderNumber:string | * REQUIRED The purchase order number for which you want to return the shipping label. It should be the same purchaseOrderNumber as received in the order.

        Returns:
            ApiResponse:
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), purchaseOrderNumber), params=kwargs
        )

    @sp_endpoint(
        "/vendor/directFulfillment/shipping/2021-12-28/shipmentConfirmations", method="POST"
    )
    async def submit_shipment_confirmations(self, **kwargs) -> ApiResponse:
        """
        submit_shipment_confirmations(self, **kwargs) -> ApiResponse

        Submits one or more shipment confirmations for vendor orders.

        **Usage Plans:**


        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        10                                      10
        ======================================  ==============

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            body: {
              "shipmentConfirmations": [
                {
                  "purchaseOrderNumber": "string",
                  "shipmentDetails": {
                    "shippedDate": "2019-08-24T14:15:22Z",
                    "shipmentStatus": "SHIPPED",
                    "isPriorityShipment": true,
                    "vendorOrderNumber": "string",
                    "estimatedDeliveryDate": "2019-08-24T14:15:22Z"
                  },
                  "sellingParty": {
                    "partyId": "string",
                    "address": {
                      "name": "string",
                      "addressLine1": "string",
                      "addressLine2": "string",
                      "addressLine3": "string",
                      "city": "string",
                      "county": "string",
                      "district": "string",
                      "stateOrRegion": "string",
                      "postalCode": "string",
                      "countryCode": "string",
                      "phone": "string"
                    },
                    "taxRegistrationDetails": [
                      {
                        "taxRegistrationType": "VAT",
                        "taxRegistrationNumber": "string",
                        "taxRegistrationAddress": {
                          "name": "string",
                          "addressLine1": "string",
                          "addressLine2": "string",
                          "addressLine3": "string",
                          "city": "string",
                          "county": "string",
                          "district": "string",
                          "stateOrRegion": "string",
                          "postalCode": "string",
                          "countryCode": "string",
                          "phone": "string"
                        },
                        "taxRegistrationMessages": "string"
                      }
                    ]
                  },
                  "shipFromParty": {
                    "partyId": "string",
                    "address": {
                      "name": "string",
                      "addressLine1": "string",
                      "addressLine2": "string",
                      "addressLine3": "string",
                      "city": "string",
                      "county": "string",
                      "district": "string",
                      "stateOrRegion": "string",
                      "postalCode": "string",
                      "countryCode": "string",
                      "phone": "string"
                    },
                    "taxRegistrationDetails": [
                      {
                        "taxRegistrationType": "VAT",
                        "taxRegistrationNumber": "string",
                        "taxRegistrationAddress": {
                          "name": "string",
                          "addressLine1": "string",
                          "addressLine2": "string",
                          "addressLine3": "string",
                          "city": "string",
                          "county": "string",
                          "district": "string",
                          "stateOrRegion": "string",
                          "postalCode": "string",
                          "countryCode": "string",
                          "phone": "string"
                        },
                        "taxRegistrationMessages": "string"
                      }
                    ]
                  },
                  "items": [
                    {
                      "itemSequenceNumber": 0,
                      "buyerProductIdentifier": "string",
                      "vendorProductIdentifier": "string",
                      "shippedQuantity": {
                        "amount": 0,
                        "unitOfMeasure": "string"
                      }
                    }
                  ],
                  "containers": [
                    {
                      "containerType": "carton",
                      "containerIdentifier": "string",
                      "trackingNumber": "string",
                      "manifestId": "string",
                      "manifestDate": "string",
                      "shipMethod": "string",
                      "scacCode": "string",
                      "carrier": "string",
                      "containerSequenceNumber": 0,
                      "dimensions": {
                        "length": "string",
                        "width": "string",
                        "height": "string",
                        "unitOfMeasure": "IN"
                      },
                      "weight": {
                        "unitOfMeasure": "KG",
                        "value": "string"
                      },
                      "packedItems": [
                        {
                          "itemSequenceNumber": 0,
                          "buyerProductIdentifier": "string",
                          "vendorProductIdentifier": "string",
                          "packedQuantity": {
                            "amount": 0,
                            "unitOfMeasure": "string"
                          }
                        }
                      ]
                    }
                  ]
                }
              ]
            }

        Returns:
            ApiResponse:
        """

        return await self._request(kwargs.pop("path"), data=kwargs, add_marketplace=False)

    @sp_endpoint(
        "/vendor/directFulfillment/shipping/2021-12-28/shipmentStatusUpdates", method="POST"
    )
    async def submit_shipment_status_updates(self, **kwargs) -> ApiResponse:
        """
        submit_shipment_status_updates(self, **kwargs) -> ApiResponse

        This API call is only to be used by Vendor-Own-Carrier (VOC) vendors. Calling this API will submit a shipment status update for the package that a vendor has shipped. It will provide the Amazon customer visibility on their order, when the package is outside of Amazon Network visibility.

        **Usage Plans:**

        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        10                                      10
        ======================================  ==============

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            body: {
              "shipmentStatusUpdates": [
                {
                  "purchaseOrderNumber": "string",
                  "sellingParty": {
                    "partyId": "string",
                    "address": {
                      "name": "string",
                      "addressLine1": "string",
                      "addressLine2": "string",
                      "addressLine3": "string",
                      "city": "string",
                      "county": "string",
                      "district": "string",
                      "stateOrRegion": "string",
                      "postalCode": "string",
                      "countryCode": "string",
                      "phone": "string"
                    },
                    "taxRegistrationDetails": [
                      {
                        "taxRegistrationType": "VAT",
                        "taxRegistrationNumber": "string",
                        "taxRegistrationAddress": {
                          "name": "string",
                          "addressLine1": "string",
                          "addressLine2": "string",
                          "addressLine3": "string",
                          "city": "string",
                          "county": "string",
                          "district": "string",
                          "stateOrRegion": "string",
                          "postalCode": "string",
                          "countryCode": "string",
                          "phone": "string"
                        },
                        "taxRegistrationMessages": "string"
                      }
                    ]
                  },
                  "shipFromParty": {
                    "partyId": "string",
                    "address": {
                      "name": "string",
                      "addressLine1": "string",
                      "addressLine2": "string",
                      "addressLine3": "string",
                      "city": "string",
                      "county": "string",
                      "district": "string",
                      "stateOrRegion": "string",
                      "postalCode": "string",
                      "countryCode": "string",
                      "phone": "string"
                    },
                    "taxRegistrationDetails": [
                      {
                        "taxRegistrationType": "VAT",
                        "taxRegistrationNumber": "string",
                        "taxRegistrationAddress": {
                          "name": "string",
                          "addressLine1": "string",
                          "addressLine2": "string",
                          "addressLine3": "string",
                          "city": "string",
                          "county": "string",
                          "district": "string",
                          "stateOrRegion": "string",
                          "postalCode": "string",
                          "countryCode": "string",
                          "phone": "string"
                        },
                        "taxRegistrationMessages": "string"
                      }
                    ]
                  },
                  "statusUpdateDetails": {
                    "trackingNumber": "string",
                    "statusCode": "string",
                    "reasonCode": "string",
                    "statusDateTime": "2019-08-24T14:15:22Z",
                    "statusLocationAddress": {
                      "name": "string",
                      "addressLine1": "string",
                      "addressLine2": "string",
                      "addressLine3": "string",
                      "city": "string",
                      "county": "string",
                      "district": "string",
                      "stateOrRegion": "string",
                      "postalCode": "string",
                      "countryCode": "string",
                      "phone": "string"
                    },
                    "shipmentSchedule": {
                      "estimatedDeliveryDateTime": "2019-08-24T14:15:22Z",
                      "apptWindowStartDateTime": "2019-08-24T14:15:22Z",
                      "apptWindowEndDateTime": "2019-08-24T14:15:22Z"
                    }
                  }
                }
              ]
            }

        Returns:
            ApiResponse:
        """

        return await self._request(kwargs.pop("path"), data=kwargs)

    @sp_endpoint("/vendor/directFulfillment/shipping/2021-12-28/customerInvoices", method="GET")
    async def get_customer_invoices(self, **kwargs) -> ApiResponse:
        """
        get_customer_invoices(self, **kwargs) -> ApiResponse

        Returns a list of customer invoices created during a time frame that you specify. You define the  time frame using the createdAfter and createdBefore parameters. You must use both of these parameters. The date range to search must be no more than 7 days.

        **Usage Plans:**


        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        10                                      10
        ======================================  ==============

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            key shipFromPartyId:string |  The vendor warehouseId for order fulfillment. If not specified, the result will contain orders for all warehouses.
            key limit:integer |  The limit to the number of records returned
            key createdAfter:string | * REQUIRED Orders that became available after this date and time will be included in the result. Must be in ISO-8601 date/time format.
            key createdBefore:string | * REQUIRED Orders that became available before this date and time will be included in the result. Must be in ISO-8601 date/time format.
            key sortOrder:string |  Sort ASC or DESC by order creation date.
            key nextToken:string |  Used for pagination when there are more orders than the specified result size limit. The token value is returned in the previous API call.

        Returns:
            ApiResponse:
        """

        return await self._request(kwargs.pop("path"), params=kwargs)

    @sp_endpoint(
        "/vendor/directFulfillment/shipping/2021-12-28/customerInvoices/{}", method="GET"
    )
    async def get_customer_invoice(self, purchaseOrderNumber, **kwargs) -> ApiResponse:
        """
        get_customer_invoice(self, purchaseOrderNumber, **kwargs) -> ApiResponse

        Returns a customer invoice based on the purchaseOrderNumber that you specify.

        **Usage Plans:**


        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        10                                      10
        ======================================  ==============

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            purchaseOrderNumber:string | * REQUIRED Purchase order number of the shipment for which to return the invoice.

        Returns:
            ApiResponse:
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), purchaseOrderNumber), params=kwargs
        )

    @sp_endpoint("/vendor/directFulfillment/shipping/2021-12-28/packingSlips", method="GET")
    async def get_packing_slips(self, **kwargs) -> ApiResponse:
        """
        get_packing_slips(self, **kwargs) -> ApiResponse

        Returns a list of packing slips for the purchase orders that match the criteria specified. Date range to search must not be more than 7 days.

        **Usage Plans:**


        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        10                                      10
        ======================================  ==============

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            key shipFromPartyId:string |  The vendor warehouseId for order fulfillment. If not specified the result will contain orders for all warehouses.
            key limit:integer |  The limit to the number of records returned
            key createdAfter:string | * REQUIRED Packing slips that became available after this date and time will be included in the result. Must be in ISO-8601 date/time format.
            key createdBefore:string | * REQUIRED Packing slips that became available before this date and time will be included in the result. Must be in ISO-8601 date/time format.
            key sortOrder:string |  Sort ASC or DESC by packing slip creation date.
            key nextToken:string |  Used for pagination when there are more packing slips than the specified result size limit. The token value is returned in the previous API call.

        Returns:
            ApiResponse:
        """

        return await self._request(kwargs.pop("path"), params=kwargs)

    @sp_endpoint("/vendor/directFulfillment/shipping/2021-12-28/packingSlips/{}", method="GET")
    async def get_packing_slip(self, purchaseOrderNumber, **kwargs) -> ApiResponse:
        """
        get_packing_slip(self, purchaseOrderNumber, **kwargs) -> ApiResponse

        Returns a packing slip based on the purchaseOrderNumber that you specify.

        **Usage Plans:**


        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        10                                      10
        ======================================  ==============

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            purchaseOrderNumber:string | * REQUIRED The purchaseOrderNumber for the packing slip you want.

        Returns:
            ApiResponse:
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), purchaseOrderNumber), params=kwargs
        )




    @sp_endpoint("/vendor/directFulfillment/shipping/2021-12-28/shippingLabels/{}", method="POST")
    async def create_shipping_labels(self, purchaseOrderNumber, **kwargs) -> ApiResponse:
        """
        create_shipping_labels(self, purchaseOrderNumber, **kwargs) -> ApiResponse

        Creates shipping labels for a purchase order and returns the labels.
        
        **Usage Plan:**
        
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 10 | 10 |
        
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values then those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits).

        Args:
            purchaseOrderNumber:string | * REQUIRED The purchase order number for which you want to return the shipping labels. It should be the same number as the `purchaseOrderNumber` in the order.
            body:CreateShippingLabelsRequest | * REQUIRED {'description': 'The request body for the createShippingLabels operation.',
             'properties': {'containers': {'description': 'A list of the packages in this shipment.', 'items': {'$ref': '#/definitions/Container'}, 'type': 'array'},
                            'sellingParty': {'$ref': '#/definitions/PartyIdentification', 'description': 'ID of the selling party or vendor.'},
                            'shipFromParty': {'$ref': '#/definitions/PartyIdentification', 'description': 'Warehouse code of vendor.'}},
             'required': ['sellingParty', 'shipFromParty'],
             'type': 'object'}

        Returns:
            ApiResponse:
        """
        return await self._request(fill_query_params(kwargs.pop("path"), purchaseOrderNumber), data=kwargs)







    @sp_endpoint("/vendor/directFulfillment/shipping/2021-12-28/containerLabel", method="POST")
    async def create_container_label(self, **kwargs) -> ApiResponse:
        """
        create_container_label(self, **kwargs) -> ApiResponse

        Creates a container (pallet) label for the associated shipment package.
        
        **Usage Plan:**
        
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 10 | 10 |
        
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:
            body:CreateContainerLabelRequest | * REQUIRED {'description': 'The request body schema for the `createContainerLabel` operation.',
             'properties': {'carrierId': {'$ref': '#/definitions/CarrierId', 'description': "The container (pallet) label's carrier."},
                            'packages': {'$ref': '#/definitions/Packages', 'description': 'An array of package objects that associate shipment packages with a container.'},
                            'sellingParty': {'$ref': '#/definitions/PartyIdentification', 'description': 'The ID of the selling party or vendor.'},
                            'shipFromParty': {'$ref': '#/definitions/PartyIdentification', 'description': 'The warehouse code of the vendor.'},
                            'vendorContainerId': {'$ref': '#/definitions/VendorContainerId', 'description': "The vendor's unique identifier for the container."}},
             'required': ['sellingParty', 'shipFromParty', 'carrierId', 'vendorContainerId', 'packages'],
             'type': 'object'}

        Returns:
            ApiResponse:
        """
        return await self._request(kwargs.pop("path"), data=kwargs)
