import urllib.parse

from sp_api.base import sp_endpoint, fill_query_params, ApiResponse
from sp_api.asyncio.base import AsyncBaseClient


class AmazonWarehousingAndDistributionV20240509(AsyncBaseClient):
    """
    AmazonWarehousingAndDistribu SP-API Client
    :link:

    The Selling Partner API for Amazon Warehousing and Distribution (AWD).
    """

    @sp_endpoint("/awd/2024-05-09/inboundShipments/{}", method="GET")
    async def get_inbound_shipment(self, shipmentId, **kwargs) -> ApiResponse:
        """
                get_inbound_shipment(self, shipmentId, **kwargs) -> ApiResponse

                Retrieves an AWD inbound shipment.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 2 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api)

                Args:

                    shipmentId:string | * REQUIRED ID for the shipment. A shipment contains the cases being inbounded.


                Returns:
                    ApiResponse:
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), shipmentId), params=kwargs
        )

    @sp_endpoint("/awd/2024-05-09/inboundShipments", method="GET")
    async def list_inbound_shipments(self, **kwargs) -> ApiResponse:
        """
                list_inbound_shipments(self, **kwargs) -> ApiResponse

                Retrieves a summary for all the inbound AWD shipments associated with a merchant, with the ability to apply optional filters.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 1 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

                Args:

                    key sortBy:string |  Field to sort results by. Required if `sortOrder` is provided.

                    key sortOrder:string |  Sort the response in `ASCENDING` or `DESCENDING` order.

                    key shipmentStatus:string |  Filter by inbound shipment status.

                    key updatedAfter:string |  List the inbound shipments that were updated after a certain time (inclusive). The date must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format.

                    key updatedBefore:string |  List the inbound shipments that were updated before a certain time (inclusive). The date must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format.

                    key maxResults:integer |  Maximum number of results to return.

                    key nextToken:string |  Token to retrieve the next set of paginated results.


                Returns:
                    ApiResponse:
        """

        return await self._request(kwargs.pop("path"), params=kwargs)

    @sp_endpoint("/awd/2024-05-09/inventory", method="GET")
    async def list_inventory(self, **kwargs) -> ApiResponse:
        """
                list_inventory(self, **kwargs) -> ApiResponse

                Lists AWD inventory associated with a merchant with the ability to apply optional filters.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 2 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

                Args:

                    key sku:string |  Filter by seller or merchant SKU for the item.

                    key sortOrder:string |  Sort the response in `ASCENDING` or `DESCENDING` order.

                    key details:string |  Set to `SHOW` to return summaries with additional inventory details. Defaults to `HIDE,` which returns only inventory summary totals.

                    key nextToken:string |  Token to retrieve the next set of paginated results.

                    key maxResults:integer |  Maximum number of results to return.


                Returns:
                    ApiResponse:
        """

        return await self._request(kwargs.pop("path"), params=kwargs)

    @sp_endpoint("/awd/2024-05-09/inboundOrders", method="POST")
    async def create_inbound(self, **kwargs) -> ApiResponse:
        """
        create_inbound(self, **kwargs) -> ApiResponse

        Creates a draft AWD inbound order with a list of packages for inbound shipment. The operation creates one shipment per order. 
        
        **Usage Plan:**
        
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 1 |
        
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:
            body:InboundOrderCreationData | * REQUIRED {'description': 'Payload for creating an inbound order.',
             'example': {'externalReferenceId': 'TestReferenceId',
                         'originAddress': {'addressLine1': 'address_1',
                                           'addressLine2': 'address_2',
                                           'addressLine3': 'address_3',
                                           'city': 'City1',
                                           'countryCode': 'CC',
                                           'district': 'District1',
                                           'name': 'address_name',
                                           'postalCode': '123456',
                                           'stateOrRegion': 'State1'},
                         'packagesToInbound': [{'count': 1,
                                                'distributionPackage': {'contents': {'products': [{'quantity': 1, 'sku': 'testPen'}]},
                                                                        'measurements': {'dimensions': {'height': 1, 'length': 1, 'unitOfMeasurement': 'INCHES', 'width': 1},
                                                                                         'volume': {'unitOfMeasurement': 'CUIN', 'volume': 1},
                                                                                         'weight': {'unitOfMeasurement': 'POUNDS', 'weight': 1}},
                                                                        'type': 'CASE'}}],
                         'preferences': {'destinationRegion': 'us-west'}},
             'properties': {'externalReferenceId': {'description': 'Reference ID that can be used to correlate the order with partner resources.', 'example': 'TestReferenceId', 'type': 'string'},
                            'originAddress': {'$ref': '#/definitions/Address', 'description': 'Origin address from where the inbound order will be shipped.'},
                            'packagesToInbound': {'description': 'List of packages to be inbounded.',
                                                  'example': [{'count': 1,
                                                               'distributionPackage': {'contents': {'products': [{'quantity': 1, 'sku': 'testPen'}]},
                                                                                       'measurements': {'dimensions': {'height': 1, 'length': 1, 'unitOfMeasurement': 'INCHES', 'width': 1},
                                                                                                        'volume': {'unitOfMeasurement': 'CUIN', 'volume': 1},
                                                                                                        'weight': {'unitOfMeasurement': 'POUNDS', 'weight': 1}},
                                                                                       'type': 'CASE'}}],
                                                  'items': {'$ref': '#/definitions/DistributionPackageQuantity'},
                                                  'minItems': 1,
                                                  'type': 'array'},
                            'preferences': {'$ref': '#/definitions/InboundPreferences'}},
             'required': ['originAddress', 'packagesToInbound'],
             'type': 'object'}

        Returns:
            ApiResponse:
        """
        return await self._request(kwargs.pop("path"), data=kwargs)

    @sp_endpoint("/awd/2024-05-09/inboundOrders/{}", method="GET")
    async def get_inbound(self, orderId, **kwargs) -> ApiResponse:
        """
        get_inbound(self, orderId, **kwargs) -> ApiResponse

        Retrieves an AWD inbound order.
        
        **Usage Plan:**
        
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2 | 2 |
        
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:
            orderId:string | * REQUIRED The ID of the inbound order that you want to retrieve.

        Returns:
            ApiResponse:
        """
        return await self._request(fill_query_params(kwargs.pop("path"), orderId), params=kwargs)

    @sp_endpoint("/awd/2024-05-09/inboundOrders/{}", method="PUT")
    async def update_inbound(self, orderId, **kwargs) -> ApiResponse:
        """
        update_inbound(self, orderId, **kwargs) -> ApiResponse

        Updates an AWD inbound order that is in `DRAFT` status and not yet confirmed. Use this operation to update the `packagesToInbound`, `originAddress` and `preferences` attributes.
        
        **Usage Plan:**
        
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 1 |
        
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:
            orderId:string | * REQUIRED The ID of the inbound order that you want to update.
            body:InboundOrder | * REQUIRED {'description': 'Represents an AWD inbound order.',
             'example': {'createdAt': '2023-06-07T12:12:09.061Z',
                         'destinationDetails': {'destinationAddress': {'addressLine1': 'address_1',
                                                                       'addressLine2': 'address_2',
                                                                       'addressLine3': 'address_3',
                                                                       'city': 'Seattle',
                                                                       'countryCode': 'US',
                                                                       'county': 'Washington',
                                                                       'district': 'District1',
                                                                       'name': 'address_name',
                                                                       'phoneNumber': '+14155552671',
                                                                       'postalCode': '123456',
                                                                       'stateOrRegion': 'Washington'},
                                                'destinationRegion': 'us-east',
                                                'shipmentId': 'TestShipmentId'},
                         'externalReferenceId': 'TestReferenceId',
                         'orderId': 'TestOrderId',
                         'orderStatus': 'DRAFT',
                         'originAddress': {'addressLine1': 'address_1',
                                           'addressLine2': 'address_2',
                                           'addressLine3': 'address_3',
                                           'city': 'Seattle',
                                           'countryCode': 'US',
                                           'county': 'Washington',
                                           'district': 'District1',
                                           'name': 'address_name',
                                           'phoneNumber': '+14155552671',
                                           'postalCode': '123456',
                                           'stateOrRegion': 'Washington'},
                         'packagesToInbound': [{'count': 1,
                                                'distributionPackage': {'contents': {'packages': [],
                                                                                     'products': [{'expiration': '2025-06-07T12:12:09.061Z',
                                                                                                   'prepDetails': {'labelOwner': 'SELF',
                                                                                                                   'prepCategory': 'PERFORATED',
                                                                                                                   'prepInstructions': [{'prepOwner': 'AMAZON', 'prepType': 'ITEM_POLYBAGGING'}],
                                                                                                                   'prepOwner': 'AMAZON'},
                                                                                                   'quantity': 1,
                                                                                                   'sku': 'testPen'}]},
                                                                        'measurements': {'dimensions': {'height': 2.54, 'length': 2.54, 'unitOfMeasurement': 'CENTIMETERS', 'width': 2.54}, 'weight': {'unitOfMeasurement': 'KILOGRAMS', 'weight': 0.453592}},
                                                                        'type': 'CASE'}}],
                         'preferences': {'destinationRegion': 'us-west'},
                         'updatedAt': '2023-06-07T12:12:09.061Z'},
             'properties': {'createdAt': {'description': 'Date when this order was created.', 'format': 'date-time', 'type': 'string'},
                            'destinationDetails': {'$ref': '#/definitions/DestinationDetails', 'description': 'Destination details of an inbound order based on the assigned region and DC for the order.'},
                            'externalReferenceId': {'description': 'Reference ID that can be used to correlate the order with partner resources.', 'example': 'TestReferenceId', 'type': 'string'},
                            'orderId': {'description': 'Inbound order ID.', 'type': 'string'},
                            'orderStatus': {'$ref': '#/definitions/InboundStatus', 'description': 'Inbound order status.'},
                            'originAddress': {'$ref': '#/definitions/Address', 'description': 'Origin address from where the inbound order will be shipped.'},
                            'packagesToInbound': {'description': 'List of packages to be inbounded.', 'items': {'$ref': '#/definitions/DistributionPackageQuantity'}, 'minItems': 1, 'type': 'array'},
                            'preferences': {'$ref': '#/definitions/InboundPreferences'},
                            'updatedAt': {'description': 'Date when this order was last updated.', 'format': 'date-time', 'type': 'string'}},
             'required': ['createdAt', 'orderId', 'orderStatus', 'originAddress', 'packagesToInbound'],
             'type': 'object'}

        Returns:
            ApiResponse:
        """
        return await self._request(fill_query_params(kwargs.pop("path"), orderId), data=kwargs)

    @sp_endpoint("/awd/2024-05-09/inboundOrders/{}/cancellation", method="POST")
    async def cancel_inbound(self, orderId, **kwargs) -> ApiResponse:
        """
        cancel_inbound(self, orderId, **kwargs) -> ApiResponse

        Cancels an AWD Inbound order and its associated shipment.
        
        **Usage Plan:**
        
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 1 |
        
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:
            orderId:string | * REQUIRED The ID of the inbound order you want to cancel.

        Returns:
            ApiResponse:
        """
        return await self._request(fill_query_params(kwargs.pop("path"), orderId), data=kwargs)

    @sp_endpoint("/awd/2024-05-09/inboundOrders/{}/confirmation", method="POST")
    async def confirm_inbound(self, orderId, **kwargs) -> ApiResponse:
        """
        confirm_inbound(self, orderId, **kwargs) -> ApiResponse

        Confirms an AWD inbound order in `DRAFT` status.
        
        **Usage Plan:**
        
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 1 |
        
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:
            orderId:string | * REQUIRED The ID of the inbound order that you want to confirm.

        Returns:
            ApiResponse:
        """
        return await self._request(fill_query_params(kwargs.pop("path"), orderId), data=kwargs)


    @sp_endpoint("/awd/2024-05-09/inboundShipments/{}/labels", method="GET")
    async def get_inbound_shipment_labels(self, shipmentId, **kwargs) -> ApiResponse:
        """
        get_inbound_shipment_labels(self, shipmentId, **kwargs) -> ApiResponse

        Retrieves the box labels for a shipment ID that you specify. This is an asynchronous operation. If the label status is `GENERATED`, then the label URL is available.
        
        **Usage Plan:**
        
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 2 |
        
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:
            shipmentId:string | * REQUIRED ID for the shipment.
            key pageType:string |  Page type for the generated labels. The default is `PLAIN_PAPER`.
            key formatType:string |  The format type of the output file that contains your labels. The default format type is `PDF`.

        Returns:
            ApiResponse:
        """
        return await self._request(fill_query_params(kwargs.pop("path"), shipmentId), params=kwargs)

    @sp_endpoint("/awd/2024-05-09/inboundShipments/{}/transport", method="PUT")
    async def update_inbound_shipment_transport_details(self, shipmentId, **kwargs) -> ApiResponse:
        """
        update_inbound_shipment_transport_details(self, shipmentId, **kwargs) -> ApiResponse

        Updates transport details for an AWD shipment.
        
        **Usage Plan:**
        
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 1 |
        
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:
            shipmentId:string | * REQUIRED The shipment ID.
            body:TransportationDetails | * REQUIRED {'description': 'Transportation details for the shipment.',
             'example': {'trackingDetails': [{'bookingId': 'TRACKING_ID', 'carrierCode': {'carrierCodeType': 'SCAC'}}]},
             'properties': {'trackingDetails': {'description': 'Tracking details for the shipment. If using SPD transportation, this can be for each case. If not using SPD transportation, this is a single tracking entry for the entire shipment.',
                                                'items': {'$ref': '#/definitions/TrackingDetails'},
                                                'type': 'array'}},
             'required': ['trackingDetails'],
             'type': 'object'}

        Returns:
            ApiResponse:
        """
        return await self._request(fill_query_params(kwargs.pop("path"), shipmentId), data=kwargs)

    @sp_endpoint("/awd/2024-05-09/inboundEligibility", method="POST")
    async def check_inbound_eligibility(self, **kwargs) -> ApiResponse:
        """
        check_inbound_eligibility(self, **kwargs) -> ApiResponse

        Determines if the packages you specify are eligible for an AWD inbound order and contains error details for ineligible packages.
        
        **Usage Plan:**
        
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 1 |
        
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:
            body:InboundPackages | * REQUIRED {'description': 'Represents the packages to inbound.',
             'example': {'packagesToInbound': [{'count': 1,
                                                'distributionPackage': {'contents': {'products': [{'quantity': 1, 'sku': 'testPen'}]},
                                                                        'measurements': {'dimensions': {'height': 1, 'length': 1, 'unitOfMeasurement': 'INCHES', 'width': 1},
                                                                                         'volume': {'unitOfMeasurement': 'CUIN', 'volume': 1},
                                                                                         'weight': {'unitOfMeasurement': 'POUNDS', 'weight': 1}},
                                                                        'type': 'CASE'}}]},
             'properties': {'packagesToInbound': {'description': 'List of packages to be inbounded.',
                                                  'example': [{'count': 1,
                                                               'distributionPackage': {'contents': {'products': [{'quantity': 1, 'sku': 'testPen'}]},
                                                                                       'measurements': {'dimensions': {'height': 1, 'length': 1, 'unitOfMeasurement': 'INCHES', 'width': 1},
                                                                                                        'volume': {'unitOfMeasurement': 'CUIN', 'volume': 1},
                                                                                                        'weight': {'unitOfMeasurement': 'POUNDS', 'weight': 1}},
                                                                                       'type': 'CASE'}}],
                                                  'items': {'$ref': '#/definitions/DistributionPackageQuantity'},
                                                  'minItems': 1,
                                                  'type': 'array'}},
             'required': ['packagesToInbound'],
             'type': 'object'}

        Returns:
            ApiResponse:
        """
        return await self._request(kwargs.pop("path"), data=kwargs)



    @sp_endpoint("/awd/2024-05-09/replenishmentOrders", method="GET")
    async def list_replenishment_orders(self, **kwargs) -> ApiResponse:
        """
        list_replenishment_orders(self, **kwargs) -> ApiResponse

        Retrieves all the AWD replenishment orders pertaining to a merchant with optional filters.
        API by default will sort orders by updatedAt attribute in descending order.

        Args:
            key updatedAfter:string |  Get the replenishment orders updated after certain time (Inclusive)
            Date should be in ISO 8601 format as defined by date-time in - https://www.rfc-editor.org/rfc/rfc3339.
            key updatedBefore:string |  Get the replenishment orders updated before certain time (Inclusive)
            Date should be in ISO 8601 format as defined by date-time in - https://www.rfc-editor.org/rfc/rfc3339.
            key sortOrder:string |  Sort the response in ASCENDING or DESCENDING order. The default sort order is DESCENDING.
            key maxResults:integer |  Maximum results to be returned in a single response.
            key nextToken:string |  A token that is used to retrieve the next page of results. The response includes `nextToken` when the number of results exceeds the specified `maxResults` value. To get the next page of results, call the operation with this token and include the same arguments as the call that produced the token. To get a complete list, call this operation until `nextToken` is null. Note that this operation can return empty pages.

        Returns:
            ApiResponse:
        """
        return await self._request(kwargs.pop("path"), params=kwargs)

    @sp_endpoint("/awd/2024-05-09/replenishmentOrders", method="POST")
    async def create_replenishment_order(self, **kwargs) -> ApiResponse:
        """
        create_replenishment_order(self, **kwargs) -> ApiResponse

        Creates an AWD replenishment order with given products to replenish.
        The API will return the order ID of the newly created order and also start an async validation check on the products to e.
        The order status will transition to ELIGIBLE/INELIGIBLE status from VALIDATING post validation check

        Args:
            body:ReplenishmentOrderCreationData | * REQUIRED {'description': 'This structure represents the payload for creating an AFN Replenishment Order.\nBy default, all replenishment orders created support Partial order preferences.',
             'example': {'preferences': {'confirmation': 'AUTO'}, 'products': [{'quantity': 1, 'sku': 'testPen'}]},
             'properties': {'preferences': {'$ref': '#/definitions/ReplenishmentPreferences'},
                            'products': {'description': 'Requested amount of single product units to be replenished.', 'example': [{'quantity': 1, 'sku': 'TestSKU'}], 'items': {'$ref': '#/definitions/DistributionProduct'}, 'type': 'array'}},
             'type': 'object'}

        Returns:
            ApiResponse:
        """
        return await self._request(kwargs.pop("path"), data=kwargs)

    @sp_endpoint("/awd/2024-05-09/replenishmentOrders/{}", method="GET")
    async def get_replenishment_order(self, orderId, **kwargs) -> ApiResponse:
        """
        get_replenishment_order(self, orderId, **kwargs) -> ApiResponse

        Retrieves an AWD Replenishment order with a set of shipments containing items that is/was planned to be replenished into an FBA node.

        Args:
            orderId:string | * REQUIRED ID of the replenishment order to be retrieved.

        Returns:
            ApiResponse:
        """
        return await self._request(fill_query_params(kwargs.pop("path"), orderId), params=kwargs)

    @sp_endpoint("/awd/2024-05-09/replenishmentOrders/{}/confirmation", method="POST")
    async def confirm_replenishment_order(self, orderId, **kwargs) -> ApiResponse:
        """
        confirm_replenishment_order(self, orderId, **kwargs) -> ApiResponse

        Confirms an AWD replenishment order in ELIGIBLE state with a set of shipments containing items that are needed to be replenished to an FBA node.
        Order can only be confirmed in ELIGIBLE state.

        Args:
            orderId:string | * REQUIRED ID of the replenishment order to be confirmed.

        Returns:
            ApiResponse:
        """
        return await self._request(fill_query_params(kwargs.pop("path"), orderId), data=kwargs)
