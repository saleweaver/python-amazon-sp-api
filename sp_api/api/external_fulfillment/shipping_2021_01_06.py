from sp_api.base import Client, sp_endpoint, ApiResponse, fill_query_params


class ExternalFulfillmentShippingV20210106(Client):
    """
    External Fulfillment Shipments API (version 2021-01-06).
    """

    @sp_endpoint("/externalFulfillment/shipments/2021-01-06/shipments/{}", method="POST")
    def process_shipment(self, shipmentId, operation, **kwargs) -> ApiResponse:
        """
        process_shipment(self, shipmentId, operation, **kwargs) -> ApiResponse
        
        Confirms/Rejects that a seller will be fulfilling or cancelling the specified shipment.
        
        Examples:
            literal blocks::
            
                ExternalFulfillmentShippingV20210106().process_shipment("value", "value")
        
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
            
                ExternalFulfillmentShippingV20210106().create_packages("value")
        
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
            
                ExternalFulfillmentShippingV20210106().update_package("value", "value")
        
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
            
                ExternalFulfillmentShippingV20210106().update_package_status("value", "value")
        
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
            
                ExternalFulfillmentShippingV20210106().generate_invoice("value")
        
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
            
                ExternalFulfillmentShippingV20210106().retrieve_invoice("value")
        
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
            
                ExternalFulfillmentShippingV20210106().retrieve_shipping_options("value", "value")
        
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
            
                ExternalFulfillmentShippingV20210106().generate_ship_labels("value", "value")
        
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
            
                ExternalFulfillmentShippingV20210106().retrieve_ship_label("value", "value")
        
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
