import uuid

from sp_api.base import Client, sp_endpoint, ApiResponse, fill_query_params


class ExternalFulfillment(Client):
    """
    ExternalFulfillment SP-API Client
    :link:

    The Selling Partner API to work with Amazon External Fulfillment shipments management/processing services.

    Deprecated: use ExternalFulfillmentInventory, ExternalFulfillmentReturns, and
    ExternalFulfillmentShipping for versioned access. This facade remains for backward compatibility.
    """

    @sp_endpoint("/externalFulfillment/2024-09-11/shipments", method="GET")
    def get_shipments(self, **kwargs) -> ApiResponse:
        """
        get_shipments(self, **kwargs) -> ApiResponse
        
        Get a list of shipments created for the seller in the status you specify. Shipments can be further filtered based on the fulfillment node or the time of the shipments' last update.
        
        Examples:
            literal blocks::
            
                ExternalFulfillment().get_shipments()
        
        Args:
            key locationId: object |  The Amazon channel location identifier for the shipments you want to retrieve.
            key marketplaceId: object |  The marketplace ID associated with the location. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).
            key channelName: object |  The channel name associated with the location.
            key status: object | required The status of shipment you want to include in the response. To retrieve all new shipments, set this value to `ACCEPTED`.
            key lastUpdatedAfter: object |  The response includes shipments whose latest update is after the specified time. In [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format.
            key lastUpdatedBefore: object |  The response includes shipments whose latest update is before the specified time. In [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format.
            key maxResults: object |  The maximum number of shipments to include in the response.
            key paginationToken: object |  A token that you use to retrieve the next page of results. The response includes `nextToken` when there are multiple pages of results. To get the next page of results, call the operation with this token and include the same arguments as the call that produced the token. To get a complete list, call this operation until `nextToken` is null. Note that this operation can return empty pages.
        
        Returns:
            ApiResponse
        """

        return self._request(kwargs.pop("path"), params=kwargs)

    @sp_endpoint("/externalFulfillment/2024-09-11/shipments/{}", method="GET")
    def get_shipment(self, shipmentId, **kwargs) -> ApiResponse:
        """
        get_shipment(self, shipmentId, **kwargs) -> ApiResponse
        
        Get a single shipment with the ID you specify.
        
        Examples:
            literal blocks::
            
                ExternalFulfillment().get_shipment("value")
        
        Args:
            shipmentId: object | required The ID of the shipment you want to retrieve.
        
        Returns:
            ApiResponse
        """
        return self._request(
            fill_query_params(kwargs.pop("path"), shipmentId),
            params=kwargs,
            add_marketplace=False,
        )

    @sp_endpoint("/externalFulfillment/shipments/2021-01-06/shipments/{}", method="POST")
    def process_shipment(self, shipmentId, operation, **kwargs) -> ApiResponse:
        """
        process_shipment(self, shipmentId, operation, **kwargs) -> ApiResponse
        
        Confirms/Rejects that a seller will be fulfilling or cancelling the specified shipment.
        
        Examples:
            literal blocks::
            
                ExternalFulfillment().process_shipment("value", "value")
        
        Args:
            shipmentId:  | required
            operation:  | required
            **kwargs:
        
        Returns:
            ApiResponse
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
        
        Examples:
            literal blocks::
            
                ExternalFulfillment().create_packages("value")
        
        Args:
            shipmentId:  | required
            **kwargs:
        
        Returns:
            ApiResponse
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
        
        Examples:
            literal blocks::
            
                ExternalFulfillment().update_package("value", "value")
        
        Args:
            shipmentId:  | required
            packageId:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """

        return self._request(
            fill_query_params(kwargs.pop("path"), shipmentId, packageId),
            data=kwargs,
            add_marketplace=False
        )

    @sp_endpoint("/externalFulfillment/shipments/2021-01-06/shipments/{}/packages/{}", method="PATCH")
    def update_package_status(self, shipmentId, packageId, **kwargs) -> ApiResponse:
        """
        update_package_status(self, shipmentId, packageId, **kwargs) -> ApiResponse
        
        Updates the status of the packages.
        
        Examples:
            literal blocks::
            
                ExternalFulfillment().update_package_status("value", "value")
        
        Args:
            shipmentId:  | required
            packageId:  | required
            **kwargs:
        
        Returns:
            ApiResponse
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
        
        Examples:
            literal blocks::
            
                ExternalFulfillment().generate_invoice("value")
        
        Args:
            shipmentId:  | required
            **kwargs:
        
        Returns:
            ApiResponse
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
        
        Examples:
            literal blocks::
            
                ExternalFulfillment().retrieve_invoice("value")
        
        Args:
            shipmentId:  | required
            **kwargs:
        
        Returns:
            ApiResponse
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
        
        Examples:
            literal blocks::
            
                ExternalFulfillment().retrieve_shipping_options("value", "value")
        
        Args:
            shipmentId:  | required
            packageId:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """
        params = {"shipmentId": shipmentId, "packageId": packageId}
        return self._request(kwargs.pop("path"), params=params, add_marketplace=False)

    @sp_endpoint("/externalFulfillment/shipments/2021-01-06/shipments/{}/shipLabels", method="PUT")
    def generate_ship_labels(self, shipmentId, operation, **kwargs) -> ApiResponse:
        """
        generate_ship_labels(self, shipmentId, operation, **kwargs) -> ApiResponse
        
        Generates and retrieves all ship-labels for one or more packages in the specified shipment.
        
        Examples:
            literal blocks::
            
                ExternalFulfillment().generate_ship_labels("value", "value")
        
        Args:
            shipmentId:  | required
            operation:  | required
            **kwargs:
        
        Returns:
            ApiResponse
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
        
        Examples:
            literal blocks::
            
                ExternalFulfillment().retrieve_ship_label("value", "value")
        
        Args:
            shipmentId:  | required
            packageId:  | required
            **kwargs:
        
        Returns:
            ApiResponse
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
        
        Examples:
            literal blocks::
            
                ExternalFulfillment().list_returns()
        
        Args:
            **kwargs:
        
        Returns:
            ApiResponse
        """

        return self._request(kwargs.pop("path"), params=kwargs, add_marketplace=False)

    @sp_endpoint("/externalFulfillment/returns/2021-08-19/returns/{}", method="GET")
    def get_return(self, returnId, **kwargs) -> ApiResponse:
        """
        get_return(self, returnId, **kwargs) -> ApiResponse
        
        Get a single return item with the specified id.
        
        Examples:
            literal blocks::
            
                ExternalFulfillment().get_return("value")
        
        Args:
            returnId:  | required
            **kwargs:
        
        Returns:
            ApiResponse
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
        
        Examples:
            literal blocks::
            
                ExternalFulfillment().process_return_item("value")
        
        Args:
            returnId:  | required
            **kwargs:
        
        Returns:
            ApiResponse
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
        
        Examples:
            literal blocks::
            
                ExternalFulfillment().get_inventory("value", "value")
        
        Args:
            locationId:  | required
            skuId:  | required
            **kwargs:
        
        Returns:
            ApiResponse
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
        
        Examples:
            literal blocks::
            
                ExternalFulfillment().update_inventory("value", "value", "value")
        
        Args:
            locationId:  | required
            skuId:  | required
            quantity:  | required
            **kwargs:
        
        Returns:
            ApiResponse
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
        
        Make up to 10 inventory requests. The response includes the set of responses that correspond to requests. The response for each successful request in the set includes the  inventory count for the provided `sku` and `locationId` pair.
        
        Examples:
            literal blocks::
            
                ExternalFulfillment().batch_inventory()
        
        Args:
            body: BatchInventoryRequest | required A list of inventory requests.
        
        Returns:
            ApiResponse
        """

        return self._request(
            kwargs.pop("path"),
            data=kwargs,
            add_marketplace=False,
        )
