from sp_api.base import Client, sp_endpoint, ApiResponse, fill_query_params


class ExternalFulfillmentShippingV20210106(Client):
    """
    External Fulfillment Shipments API (version 2021-01-06).
    """

    @sp_endpoint("/externalFulfillment/shipments/2021-01-06/shipments/{}", method="POST")
    def process_shipment(self, shipmentId, operation, **kwargs) -> ApiResponse:
        """
        process_shipment(self, shipmentId, **kwargs) -> ApiResponse

        Confirms/Rejects that a seller will be fulfilling or cancelling the specified shipment.

        **Usage Plan:**

        ======================================
        Rate (requests per second)
        ======================================
        5
        ======================================

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipmentId:string | * REQUIRED The id of the shipment which is to be confirmed for fulfillment.
            operation:string | * REQUIRED The status in which shipment should be moved. Valid values are CONFIRM and REJECT.

            body: {
                "referenceId": "string",
                "lineItems": [
                    {
                        "lineItem": {
                            "id": "string",
                            "quantity": 1
                        },
                        "reason": "OUT_OF_STOCK"
                    }
                ]
            }

        Returns:
            ApiResponse:
        """
        return self._request(
            fill_query_params(kwargs.pop("path"), shipmentId),
            params={"operation": operation},
            data=kwargs,
            add_marketplace=False,
        )

    @sp_endpoint("/externalFulfillment/shipments/2021-01-06/shipments/{}/packages", method="POST")
    def create_packages(self, shipmentId, **kwargs) -> ApiResponse:
        """
        create_packages(self, shipmentId, **kwargs) -> ApiResponse

        Provides details about the packages that will be used to fulfill the specified shipment.

        **Usage Plan:**

        ======================================
        Rate (requests per second)
        ======================================
        5
        ======================================

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipmentId:string | * REQUIRED The id of the shipment for which package information is being provided.

            body: {
                "packages": [
                    {
                        "id": "string",
                        "dimensions": {
                            "length": {
                                "value": "string",
                                "dimensionUnit": "CM"
                            },
                            "width": {
                                "value": "string",
                                "dimensionUnit": "CM"
                            },
                            "height": {
                                "value": "string",
                                "dimensionUnit": "CM"
                            },
                        },
                        "weight": {
                            "value": "string",
                            "weightUnit": "kilograms"
                        },
                        "hazmatLabels": [],
                        "packageLineItems": [
                            {
                                "packageLineItemId": "string",
                                "quantity": 1,
                                "serialNumbers": [],
                                "pieces": 1,
                                "countryOfOrigin": "ES"
                            }
                        ],
                        "status": "CREATED"
                    }
                ]
            }
        Returns:
            ApiResponse:
        """

        return self._request(
            fill_query_params(kwargs.pop("path"), shipmentId),
            data=kwargs,
            add_marketplace=False
        )

    @sp_endpoint("/externalFulfillment/shipments/2021-01-06/shipments/{}/packages/{}", method="PUT")
    def update_package(self, shipmentId, packageId, **kwargs) -> ApiResponse:
        """
        update_package(self, shipmentId, packageId, **kwargs) -> ApiResponse

        Updates the details about the packages that will be used to fulfill the specified shipment.

        **Usage Plan:**

        ======================================
        Rate (requests per second)
        ======================================
        5
        ======================================

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipmentId:string | * REQUIRED The id of the shipment for which package information is being updated.
            packageId:string | * REQUIRED The id of the shipment for which package information is being updated.

            body: {
                "packages": [
                    {
                        "id": "string",
                        "dimensions": {
                            "length": {
                                "value": "string",
                                "dimensionUnit": "CM"
                            },
                            "width": {
                                "value": "string",
                                "dimensionUnit": "CM"
                            },
                            "height": {
                                "value": "string",
                                "dimensionUnit": "CM"
                            },
                        },
                        "weight": {
                            "value": "string",
                            "weightUnit": "kilograms"
                        },
                        "hazmatLabels": [],
                        "packageLineItems": [
                            {
                                "packageLineItemId": "string",
                                "quantity": 1,
                                "serialNumbers": [],
                                "pieces": 1,
                                "countryOfOrigin": "ES"
                            }
                        ],
                        "status": "SHIPPED"
                    }
                ]
            }
        Returns:
            ApiResponse:
        """

        return self._request(
            fill_query_params(kwargs.pop("path"), shipmentId, packageId),
            data=kwargs,
            add_marketplace=False
        )

    @sp_endpoint("/externalFulfillment/shipments/2021-01-06/shipments/{}/packages/{}", method="PATCH")
    def update_package_status(self, shipmentId, packageId, **kwargs) -> ApiResponse:
        """
        update_package_status(self, shipmentId, **kwargs) -> ApiResponse

        Updates the status of the packages.

        **Usage Plan:**

        ======================================
        Rate (requests per second)
        ======================================
        5
        ======================================

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipmentId:string | * REQUIRED The id of the shipment for which package information is being updated.
            packageId:string | * REQUIRED The id of the shipment for which package information is being updated.
            key status:string | * REQUIRED This field is deprecated. All the package status details should be defined in the body parameter.

            body: {
                "status": "SHIPPED",
                "subStatus": "OUT_FOR_DELIVERY",
                "reason": "OutForDelivery"
            }

        Returns:
            ApiResponse:
        """
        params = {}
        if "status" in kwargs:
            params["status"] = kwargs.get("status")

        return self._request(
            fill_query_params(kwargs.pop("path"), shipmentId, packageId),
            params=params,
            data=kwargs,
            add_marketplace=False
        )

    @sp_endpoint("/externalFulfillment/shipments/2021-01-06/shipments/{}/invoice", method="POST")
    def generate_invoice(self, shipmentId, **kwargs) -> ApiResponse:
        """
        generate_invoice(self, shipmentId, **kwargs) -> ApiResponse

        Generates and retrieves the invoice for the specified shipment.

        **Usage Plan:**

        ======================================
        Rate (requests per second)
        ======================================
        5
        ======================================

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipmentId:string | * REQUIRED The id of the shipment whose invoice is to be generated and retrieved.

        Returns:
            ApiResponse:
        """

        return self._request(
            fill_query_params(kwargs.pop("path"), shipmentId),
            data=kwargs,
            add_marketplace=False
        )

    @sp_endpoint("/externalFulfillment/shipments/2021-01-06/shipments/{}/invoice", method="GET")
    def retrieve_invoice(self, shipmentId, **kwargs) -> ApiResponse:
        """
        retrieve_invoice(self, shipmentId, **kwargs) -> ApiResponse

        Retrieves invoice for the specified shipment.

        **Usage Plan:**

        ======================================
        Rate (requests per second)
        ======================================
        5
        ======================================

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipmentId:string | * REQUIRED The id of the shipment whose invoice is to be retrieved.

        Returns:
            ApiResponse:

        """

        return self._request(
            fill_query_params(kwargs.pop("path"), shipmentId),
            params=kwargs,
            add_marketplace=False
        )

    @sp_endpoint("/externalFulfillment/shipments/2021-01-06/shippingOptions", method="GET")
    def retrieve_shipping_options(self, shipmentId, packageId, **kwargs) -> ApiResponse:
        """
        retrieve_shipping_options(self, shipmentId, packageId, **kwargs) -> ApiResponse

        An API for a client to retrieve an optional list of shippingOptions that marketplace/channel provides
        for the pickup of the packages of an shipment. This API will return a list of shippingOptions if the
        marketplace/channel provides transportation and allows the seller to choose a shippingOption. If the
        marketplace/channel does not allow for a shippingOption to be selected, but has a pre-determined shippingOption,
        then this API will return an empty response.

        **Usage Plan:**

        ======================================
        Rate (requests per second)
        ======================================
        1
        ======================================

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipmentId:string | * REQUIRED The id of the shipment for which available shipping option needs to be fetched.
            packageId:string | * REQUIRED The id of the package for which available shipping option needs to be fetched.

        Returns:
            ApiResponse:
        """
        params = {"shipmentId": shipmentId, "packageId": packageId}
        return self._request(kwargs.pop("path"), params=params, add_marketplace=False)

    @sp_endpoint("/externalFulfillment/shipments/2021-01-06/shipments/{}/shipLabels", method="PUT")
    def generate_ship_labels(self, shipmentId, operation, **kwargs) -> ApiResponse:
        """
        generate_ship_labels(self, shipmentId, operation, **kwargs) -> ApiResponse

        Generates and retrieves all ship-labels for one or more packages in the specified shipment.

        **Usage Plan:**

        ======================================
        Rate (requests per second)
        ======================================
        1
        ======================================

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipmentId:string | * REQUIRED The id of the shipment whose ship-label is to be generated and retrieved.
            key shippingOptionId:string | The id of the shippingOption for which a ship-label is to be generated and retrieved. Applicable only for MFN channels.
            operation:string | * REQUIRED The operation which says it is generation or regeneration of label. Valid values are GENERATE, REGENERATE

            body: {
              "packageIds": [
                "string"
              ],
              "courierSupportedAttributes": {
                "carrierName": "string",
                "trackingId": "string"
              }
            }
        Returns:
            ApiResponse:
        """

        params = {"operation": operation}
        if "shippingOptionId" in kwargs:
            params["shippingOptionId"] = kwargs.pop("shippingOptionId")

        return self._request(
            fill_query_params(kwargs.pop("path"), shipmentId),
            params=params,
            data=kwargs,
            add_marketplace=False
        )

    @sp_endpoint("/externalFulfillment/shipments/2021-01-06/shipments/{}/packages/{}/shipLabel", method="GET")
    def retrieve_ship_label(self, shipmentId, packageId, **kwargs) -> ApiResponse:
        """
        retrieve_ship_label(self, shipmentId, packageId, **kwargs) -> ApiResponse

        retrieves a ship-label for the specified package in the specified shipment.

        **Usage Plan:**

        ======================================
        Rate (requests per second)
        ======================================
        1
        ======================================

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            shipmentId:string | * REQUIRED The id of the shipment whose ship-label is to be generated and retrieved.
            packageId:string | * REQUIRED The id of the package for which a ship-label is to be generated and retrieved.

        Returns:
            ApiResponse:
        """

        return self._request(
            fill_query_params(kwargs.pop("path"), shipmentId, packageId),
            params=kwargs,
            add_marketplace=False
        )
