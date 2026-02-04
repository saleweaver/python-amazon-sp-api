from sp_api.base import Client, sp_endpoint, ApiResponse, fill_query_params


class ExternalFulfillmentShippingV20240911(Client):
    """
    External Fulfillment Shipments API (version 2024-09-11).
    """

    @sp_endpoint("/externalFulfillment/2024-09-11/shipments", method="GET")
    def get_shipments(self, **kwargs) -> ApiResponse:
        """
        get_shipments(self, **kwargs) -> ApiResponse

        Get a list of shipments dropped for the seller in the specified status. Shipments can be further filtered based on the fulfillment node and/or shipments' last updated date and time.

        **Usage Plans:**

        ======================================
        Rate (requests per second)
        ======================================
        5
        ======================================

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            key locationId:string | The SmartConnect location identifier for which shipments are to be retrieved
            key channelName:string | The channel name associated with the location. Valid values are FBA, MFN
            key status*:string | * REQUIRED Retrieves only those shipments which are in the specified status. The most common use-case would be to fetch all new shipments which would be in the ACCEPTED status. Valid values are ACCEPTED, CONFIRMED, PACKAGE_CREATED, PICKUP_SLOT_RETRIEVED, INVOICE_GENERATED, SHIPLABEL_GENERATED, SHIPPED, DELIVERED and CANCELLED.
            key lastUpdatedAfter:string | Shipments whose latest update is after the specified date/time are included in the response. This field should be in the ISO8601 date/time format.
            key lastUpdatedBefore:string | Shipments whose latest update is before the specified date/time are included in the response. This field should be in the ISO8601 date/time format.
            key maxResults:integer | Specify the number of shipments to be included in the response.
            key paginationToken:string | The nexToken value returned from a previous call to get shipments. Use this to retrieve the next page of shipments.
        Returns:
            ApiResponse:
        """

        return self._request(kwargs.pop("path"), params=kwargs)

    @sp_endpoint("/externalFulfillment/2024-09-11/shipments/{}", method="GET")
    def get_shipment(self, shipmentId, **kwargs) -> ApiResponse:
        """
        get_shipment(self, shipmentId, **kwargs) -> ApiResponse

        Get a single shipment with the specified id.

        **Usage Plan:**

        ======================================
        Rate (requests per second)
        ======================================
        5
        ======================================

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipmentId:string | * REQUIRED The id of the shipment to be retrieved.

        Returns:
            ApiResponse:
        """
        return self._request(
            fill_query_params(kwargs.pop("path"), shipmentId),
            params=kwargs,
            add_marketplace=False,
        )



    @sp_endpoint("/externalFulfillment/2024-09-11/shipments/{}", method="POST")
    def process_shipment(self, shipmentId, **kwargs) -> ApiResponse:
        """
        process_shipment(self, shipmentId, **kwargs) -> ApiResponse

        Confirm or reject the specified shipment.

        Args:
            shipmentId:string | * REQUIRED The ID of the shipment you want to confirm or reject.
            key operation:string | * REQUIRED The status of the shipment.
            body:ShipmentAcknowledgementRequest |  {'description': 'Information about the shipment and its line items, used to confirm or reject line items.',
             'example': {'lineItems': [{'lineItem': {'id': '1', 'quantity': 0}, 'reason': 'OUT_OF_STOCK'}], 'referenceId': 'cancellation-reference-identifier1'},
             'properties': {'lineItems': {'description': 'Details about the line items from the shipment that are being confirmed or rejected by the seller.', 'items': {'$ref': '#/definitions/LineItemWithReason'}, 'minItems': 0, 'type': 'array'},
                            'referenceId': {'description': 'A unique identifier for every shipment rejection.', 'type': 'string'}},
             'required': ['lineItems'],
             'type': 'object'}

        Returns:
            ApiResponse:
        """
        return self._request(fill_query_params(kwargs.pop("path"), shipmentId), data=kwargs, add_marketplace=False)

    @sp_endpoint("/externalFulfillment/2024-09-11/shipments/{}/packages", method="POST")
    def create_packages(self, shipmentId, **kwargs) -> ApiResponse:
        """
        create_packages(self, shipmentId, **kwargs) -> ApiResponse

        Provide details about the packages in the specified shipment.

        Args:
            shipmentId:string | * REQUIRED The ID of the shipment.
            body:Packages | * REQUIRED {'description': 'The request schema of the `createPackages` operation.',
             'example': {'packages': [{'dimensions': {'height': {'dimensionUnit': 'CM', 'value': '10.0'}, 'length': {'dimensionUnit': 'CM', 'value': '10.0'}, 'width': {'dimensionUnit': 'CM', 'value': '10.0'}},
                                       'hazmatLabels': [],
                                       'id': '001',
                                       'packageLineItems': [{'countryOfOrigin': 'IN', 'itemValue': {'currencyCode': 'INR', 'value': '10'}, 'packageLineItemId': '1', 'pieces': 1, 'quantity': 1, 'serialNumbers': []},
                                                            {'packageLineItemId': '2', 'quantity': 1, 'serialNumbers': []}],
                                       'status': 'CREATED',
                                       'weight': {'value': '200.0', 'weightUnit': 'G'}}]},
             'properties': {'packages': {'description': 'A list of packages.', 'items': {'$ref': '#/definitions/Package'}, 'minItems': 1, 'type': 'array'}},
             'required': ['packages'],
             'type': 'object'}

        Returns:
            ApiResponse:
        """
        return self._request(fill_query_params(kwargs.pop("path"), shipmentId), data=kwargs, add_marketplace=False)

    @sp_endpoint("/externalFulfillment/2024-09-11/shipments/{}/packages/{}", method="PUT")
    def update_package(self, shipmentId, packageId, **kwargs) -> ApiResponse:
        """
        update_package(self, shipmentId, packageId, **kwargs) -> ApiResponse

        Updates the details about the packages that will be used to fulfill the specified shipment.

        Args:
            shipmentId:string | * REQUIRED The ID of the shipment to which the package belongs.
            packageId:string | * REQUIRED The ID of the package whose information you want to update.
            body:Package | * REQUIRED {'description': "A package that is created to ship one or more of a shipment's line items.",
             'properties': {'dimensions': {'$ref': '#/definitions/PackageDimensions', 'description': 'The dimensions of the package.'},
                            'hazmatLabels': {'description': 'The optional list of HAZMAT labels applied to the package.', 'items': {'type': 'string'}, 'minItems': 0, 'type': 'array'},
                            'id': {'description': 'An ID that uniquely identifies a package within a shipment.', 'type': 'string'},
                            'packageHandlingRequirements': {'description': 'Whether the package requires standard handling or extra care.',
                                                            'enum': ['NORMAL', 'FRAGILE'],
                                                            'example': 'FRAGILE',
                                                            'type': 'string',
                                                            'x-docgen-enum-table-extension': [{'description': 'The package requires standard handling.', 'value': 'NORMAL'}, {'description': 'The package requires extra care in handling.', 'value': 'FRAGILE'}]},
                            'packageLineItems': {'$ref': '#/definitions/PackageLineItems', 'description': 'The list of line items in a package.'},
                            'status': {'description': 'The current status of the package.',
                                       'enum': ['CREATED', 'PICKUP_SLOT_RETRIEVED', 'INVOICE_GENERATED', 'SHIPLABEL_GENERATED', 'SHIPPED', 'DELIVERED', 'CANCELLED'],
                                       'type': 'string',
                                       'x-docgen-enum-table-extension': [{'description': 'The package is created.', 'value': 'CREATED'},
                                                                         {'description': 'The pickup slot is retrieved.', 'value': 'PICKUP_SLOT_RETRIEVED'},
                                                                         {'description': 'The invoice is generated.', 'value': 'INVOICE_GENERATED'},
                                                                         {'description': 'The shipping label is generated.', 'value': 'SHIPLABEL_GENERATED'},
                                                                         {'description': 'The package is shipped.', 'value': 'SHIPPED'},
                                                                         {'description': 'The package is delivered.', 'value': 'DELIVERED'},
                                                                         {'description': 'The shipment is cancelled.', 'value': 'CANCELLED'}]},
                            'weight': {'$ref': '#/definitions/Weight', 'description': 'The weight of the package. The package must weigh at least 5 grams.'}},
             'required': ['dimensions', 'id', 'weight', 'packageLineItems'],
             'type': 'object'}

        Returns:
            ApiResponse:
        """
        return self._request(fill_query_params(kwargs.pop("path"), shipmentId, packageId), data=kwargs, add_marketplace=False)

    @sp_endpoint("/externalFulfillment/2024-09-11/shipments/{}/packages/{}", method="PATCH")
    def update_package_status(self, shipmentId, packageId, **kwargs) -> ApiResponse:
        """
        update_package_status(self, shipmentId, packageId, **kwargs) -> ApiResponse

        Updates the status of the packages.

        Args:
            shipmentId:string | * REQUIRED The ID of the shipment to which the package belongs.
            packageId:string | * REQUIRED The ID of the package whose status you want to update.
            key status:string |  **DEPRECATED**. Do not use. Package status is defined in the body parameter.
            body:PackageDeliveryStatus |  {'description': 'The delivery status of the package.',
             'example': {'reason': 'Delivered Successfully', 'status': 'DELIVERED', 'subStatus': 'DELIVERED'},
             'properties': {'reason': {'description': 'The reason for the sub-status.', 'maxLength': 128, 'type': 'string'},
                            'status': {'$ref': '#/definitions/PackageStatus', 'description': 'The status of the package.'},
                            'subStatus': {'$ref': '#/definitions/PackageSubStatus', 'description': 'The sub-status of the package.'}},
             'type': 'object'}

        Returns:
            ApiResponse:
        """
        return self._request(fill_query_params(kwargs.pop("path"), shipmentId, packageId), data=kwargs, add_marketplace=False)

    @sp_endpoint("/externalFulfillment/2024-09-11/shipments/{}/shippingOptions", method="GET")
    def retrieve_shipping_options(self, shipmentId, **kwargs) -> ApiResponse:
        """
        retrieve_shipping_options(self, shipmentId, **kwargs) -> ApiResponse

        Get a list of shipping options for a package in a shipment given the shipment's marketplace and channel. If the marketplace and channel have a pre-determined shipping option, then this operation returns an empty response.

        Args:
            shipmentId:string | * REQUIRED The ID of the shipment to which the package belongs.
            key packageId:string | * REQUIRED The ID of the package for which you want to retrieve shipping options.

        Returns:
            ApiResponse:
        """
        return self._request(fill_query_params(kwargs.pop("path"), shipmentId), params=kwargs, add_marketplace=False)

    @sp_endpoint("/externalFulfillment/2024-09-11/shipments/{}/invoice", method="POST")
    def generate_invoice(self, shipmentId, **kwargs) -> ApiResponse:
        """
        generate_invoice(self, shipmentId, **kwargs) -> ApiResponse

        Get invoices for the shipment you specify.

        Args:
            shipmentId:string | * REQUIRED The ID of the shipment whose invoice you want.

        Returns:
            ApiResponse:
        """
        return self._request(fill_query_params(kwargs.pop("path"), shipmentId), data=kwargs, add_marketplace=False)

    @sp_endpoint("/externalFulfillment/2024-09-11/shipments/{}/invoice", method="GET")
    def retrieve_invoice(self, shipmentId, **kwargs) -> ApiResponse:
        """
        retrieve_invoice(self, shipmentId, **kwargs) -> ApiResponse

        Retrieve invoices for the shipment you specify.

        Args:
            shipmentId:string | * REQUIRED The ID of the shipment whose invoice you want to retrieve.

        Returns:
            ApiResponse:
        """
        return self._request(fill_query_params(kwargs.pop("path"), shipmentId), params=kwargs, add_marketplace=False)

    @sp_endpoint("/externalFulfillment/2024-09-11/shipments/{}/shipLabels", method="PUT")
    def generate_ship_labels(self, shipmentId, **kwargs) -> ApiResponse:
        """
        generate_ship_labels(self, shipmentId, **kwargs) -> ApiResponse

        Generate and retrieve all shipping labels for one or more packages in the shipment you specify.

        Args:
            shipmentId:string | * REQUIRED The ID of the shipment whose shipping labels you want to generate and retrieve.
            key shippingOptionId:string |  The ID of the shipping option whose shipping labels you want.
            key operation:string | * REQUIRED Specify whether you want to generate or regenerate a label.
            body:ShipLabelsInput |  {'description': 'Tracking details for multiple packages.',
             'example': {'courierSupportedAttributes': {'carrierName': 'ATS', 'trackingId': '151958276037'}, 'packageIds': ['TEST_CASE_200_PACKAGE_ID']},
             'properties': {'courierSupportedAttributes': {'$ref': '#/definitions/CourierSupportedAttributes'},
                            'packageIds': {'description': 'The subset of package IDs used to generate a label.', 'items': {'description': 'The ID of a package for which you want a shipping label.', 'type': 'string'}, 'maxItems': 50, 'type': 'array'}},
             'required': ['packageIds'],
             'type': 'object'}

        Returns:
            ApiResponse:
        """
        return self._request(fill_query_params(kwargs.pop("path"), shipmentId), data=kwargs, add_marketplace=False)
