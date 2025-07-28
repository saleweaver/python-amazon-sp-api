import uuid

from sp_api.base import Client, sp_endpoint, ApiResponse, fill_query_params


class ExternalFulfillment(Client):
    """
    ExternalFulfillment SP-API Client
    :link:

    The Selling Partner API to work with Amazon External Fulfillment shipments management/processing services.
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

    @sp_endpoint("/externalFulfillment/returns/2021-08-19/returns", method="GET")
    def list_returns(self, **kwargs) -> ApiResponse:
        """
        list_returns(self, **kwargs) -> ApiResponse

        Get a list of return items dropped for the seller in the specified node, and in the specified status. Returns can be further filtered based on their creation date/time

        **Usage Plans:**

        ======================================
        Rate (requests per second)
        ======================================
        5
        ======================================

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            key returnLocationId:string | The SmartConnect location identifier for which return items are to be retrieved
            key rmaId:string | The RMA id of the return items to be listed
            key status:string | Retrieves only those return items which are in the specified status. The most common use-case would be to fetch all new return items which would be in the CREATED status
            key reverseTrackingId:string | The reverseTrackingId of the return items to be listed
            key createdSince:string | Return items whose creation is after the specified date/time are included in the response. This field should be in the ISO8601 date/time format.
            key createdUntil:string | Return items whose creation is before the specified date/time are included in the response. This field should be in the ISO8601 date/time format.
            key lastUpdatedSince:string | Return items whose last update is after the specified date/time are included in the response. This field should be in the ISO8601 date/time format. Only to be used along with returnLocationId and status params.
            key lastUpdatedUntil:string | Return items whose last update is before the specified date/time are included in the response. This field should be in the ISO8601 date/time format. Only to be used along with returnLocationId and status params.
            key lastUpdatedAfter:string | DEPRECATED. Use createdFrom param instead for same results. Return items whose creation is after the specified date/time are included in the response. This field should be in the ISO8601 date/time format.
            key lastUpdatedBefore:string | DEPRECATED. Use createdTo param instead for same results. Return items whose creation is before the specified date/time are included in the response. This field should be in the ISO8601 date/time format.
            key maxResults:integer | Specify the number of return items to be included in the response. It will default to 10 in case not provided. Maximum limit is 100.
            key nextToken:string | A cursor representing information about the next page of returns. Use the value returned in previous calls to page through the complete list of returns.

        Returns:
            ApiResponse:
        """

        return self._request(kwargs.pop("path"), params=kwargs, add_marketplace=False)

    @sp_endpoint("/externalFulfillment/returns/2021-08-19/returns/{}", method="GET")
    def get_return(self, returnId, **kwargs) -> ApiResponse:
        """
        get_return(self, returnId, **kwargs) -> ApiResponse

        Get a single return item with the specified id.

        **Usage Plan:**

        ======================================
        Rate (requests per second)
        ======================================
        5
        ======================================

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            returnId:string | * REQUIRED The id of the return item to be retrieved.

        Returns:
            ApiResponse:
        """
        return self._request(
            fill_query_params(kwargs.pop("path"), returnId),
            params=kwargs,
            add_marketplace=False,
        )

    @sp_endpoint("/externalFulfillment/returns/2021-08-19/returns/{}", method="PATCH")
    def process_return_item(self, returnId, **kwargs) -> ApiResponse:
        """
        process_return_item(self, returnId, **kwargs) -> ApiResponse

        Process a return by grading. Determine the item condition and update the quantities for each item condition.

        **Usage Plan:**

        ======================================
        Rate (requests per second)
        ======================================
        5
        ======================================

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            returnId:string | * REQUIRED The id of the return item to be retrieved.

            body: {
              "op": "increment",
              "path": "/processedReturns",
              "value": {
                "Sellable": 0,
                "Defective": 0,
                "CustomerDamaged": 0,
                "CarrierDamaged": 0,
                "Fraud": 0,
                "WrongItem": 0
              }
            }

        Returns:
            ApiResponse:
        """

        headers = self.headers.copy()
        if "x-amzn-idempotency-token" in kwargs:
            headers["x-amzn-idempotency-token"] = kwargs.pop("x-amzn-idempotency-token")
        else:
            headers["x-amzn-idempotency-token"] = str(uuid.uuid4())

        return self._request(
            fill_query_params(kwargs.pop("path"), returnId),
            data=kwargs,
            headers=headers,
            add_marketplace=False,
        )

    @sp_endpoint("/externalFulfillment/inventory/2021-01-06/locations/{}/skus/{}", method="GET")
    def get_inventory(self, locationId, skuId, **kwargs) -> ApiResponse:
        """
        get_inventory(self, locationId, skuId, **kwargs) -> ApiResponse

        Get the current inventory for a given SKU at a given location.

        **Usage Plan:**

        ======================================
        Rate (requests per second)
        ======================================
        5
        ======================================

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            locationId:string | * REQUIRED The node identifier for the seller's location in smart connect for which inventory is being updated
            skuId:string | * REQUIRED The seller's identifier for the SKU for which inventory is being updated

        Returns:
            ApiResponse:
        """
        return self._request(
            fill_query_params(kwargs.pop("path"), locationId, skuId),
            params=kwargs,
            add_marketplace=False,
        )

    @sp_endpoint("/externalFulfillment/inventory/2021-01-06/locations/{}/skus/{}", method="PUT")
    def update_inventory(self, locationId, skuId, quantity, **kwargs) -> ApiResponse:
        """
        update_inventory(self, locationId, skuId, quantity, **kwargs) -> ApiResponse

        Get the current inventory for a given SKU at a given location.

        **Usage Plan:**

        ======================================
        Rate (requests per second)
        ======================================
        5
        ======================================

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            locationId:string | * REQUIRED The node identifier for the seller's location in smart connect for which inventory is being updated
            skuId:string | * REQUIRED The seller's identifier for the SKU for which inventory is being updated
            quantity:integer | * REQUIRED The absolute number of items of the specified SKU available at the specified node. This value should always be a non-zero or zero positive integer
            key if_match:string | A unique number provided with each call to update the inventory. This number must be latest version of entity that exist in system. It will be equal to comparison against existing version of entity.
            key if_unmodified_since:string | Timestamp or increasing number which does greater than comparison before applying the change. This is different than version of entity and used to overwrite the latest data. It should follow data/time format of rfc2616

        Returns:
            ApiResponse:
        """
        kwargs["quantity"] = quantity

        headers = self.headers.copy()
        if "if_match" in kwargs:
            headers["If-Match"] = kwargs.pop("if_match")
        if "if_unmodified_since" in kwargs:
            headers["If-Unmodified-Since"] = kwargs.pop("if_unmodified_since")

        return self._request(
            fill_query_params(kwargs.pop("path"), locationId, skuId),
            params=kwargs,
            add_marketplace=False,
        )

    @sp_endpoint("/externalFulfillment/inventory/2024-09-11/inventories", method="POST")
    def batch_inventory(self, **kwargs) -> ApiResponse:
        """
        batch_inventory(self, **kwargs) -> ApiResponse

        Returns the set of responses that correspond to the batched list of up to 10 requests defined in the request
        body. The response for each successful (HTTP status code 200) request in the set includes the inventory count
        for provided sku and locationId pair

        **Usage Plan:**

        ======================================
        Rate (requests per second)
        ======================================
        5
        ======================================

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            body: {
              "requests": [
                {
                  "method": "POST",
                  "uri": "/inventory/update?locationId=EXSB&skuId=efptestsku1",
                  "body": {
                    "quantity": 15,
                    "clientSequenceNumber": 12345678,
                    "marketplaceAttributes": {
                      "marketplaceId": "AXJDDKDFDKDF",
                      "channelName": "FBA"
                    }
                  }
                },
                {
                  "method": "POST",
                  "uri": "/inventory/fetch?locationId=EXSB&skuId=efptestsku2",
                  "body": {
                    "marketplaceAttributes": {
                      "marketplaceId": "AXJDDKDFDKDF",
                      "channelName": "FBA"
                    }
                  }
                }
              ]
            }

        Returns:
            ApiResponse:
        """

        return self._request(
            kwargs.pop("path"),
            data=kwargs,
            add_marketplace=False,
        )
