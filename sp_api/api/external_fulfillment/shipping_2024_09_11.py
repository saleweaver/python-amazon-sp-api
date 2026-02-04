from sp_api.base import Client, sp_endpoint, ApiResponse, fill_query_params


class ExternalFulfillmentShippingV20240911(Client):
    """
    External Fulfillment Shipments API (version 2024-09-11).
    """

    @sp_endpoint("/externalFulfillment/2024-09-11/shipments", method="GET")
    def get_shipments(self, **kwargs) -> ApiResponse:
        """
        get_shipments(self, **kwargs) -> ApiResponse
        
        Get a list of shipments created for the seller in the status you specify. Shipments can be further filtered based on the fulfillment node or the time of the shipments' last update.
        
        Examples:
            literal blocks::
            
                ExternalFulfillmentShippingV20240911().get_shipments()
        
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
            
                ExternalFulfillmentShippingV20240911().get_shipment("value")
        
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



    @sp_endpoint("/externalFulfillment/2024-09-11/shipments/{}", method="POST")
    def process_shipment(self, shipmentId, **kwargs) -> ApiResponse:
        """
        process_shipment(self, shipmentId, **kwargs) -> ApiResponse
        
        Confirm or reject the specified shipment.
        
        Examples:
            literal blocks::
            
                ExternalFulfillmentShippingV20240911().process_shipment("value")
        
        Args:
            shipmentId: object | required The ID of the shipment you want to confirm or reject.
            key operation: object | required The status of the shipment.
            body: ShipmentAcknowledgementRequest |  Information about the shipment and its line items.
        
        Returns:
            ApiResponse
        """
        return self._request(fill_query_params(kwargs.pop("path"), shipmentId), data=kwargs, add_marketplace=False)

    @sp_endpoint("/externalFulfillment/2024-09-11/shipments/{}/packages", method="POST")
    def create_packages(self, shipmentId, **kwargs) -> ApiResponse:
        """
        create_packages(self, shipmentId, **kwargs) -> ApiResponse
        
        Provide details about the packages in the specified shipment.
        
        Examples:
            literal blocks::
            
                ExternalFulfillmentShippingV20240911().create_packages("value")
        
        Args:
            shipmentId: object | required The ID of the shipment.
            body: Packages | required A list of packages in the shipment.
        
        Returns:
            ApiResponse
        """
        return self._request(fill_query_params(kwargs.pop("path"), shipmentId), data=kwargs, add_marketplace=False)

    @sp_endpoint("/externalFulfillment/2024-09-11/shipments/{}/packages/{}", method="PUT")
    def update_package(self, shipmentId, packageId, **kwargs) -> ApiResponse:
        """
        update_package(self, shipmentId, packageId, **kwargs) -> ApiResponse
        
        Updates the details about the packages that will be used to fulfill the specified shipment.
        
        Examples:
            literal blocks::
            
                ExternalFulfillmentShippingV20240911().update_package("value", "value")
        
        Args:
            shipmentId: object | required The ID of the shipment to which the package belongs.
            packageId: object | required The ID of the package whose information you want to update.
            body: Package | required The body of the request.
        
        Returns:
            ApiResponse
        """
        return self._request(fill_query_params(kwargs.pop("path"), shipmentId, packageId), data=kwargs, add_marketplace=False)

    @sp_endpoint("/externalFulfillment/2024-09-11/shipments/{}/packages/{}", method="PATCH")
    def update_package_status(self, shipmentId, packageId, **kwargs) -> ApiResponse:
        """
        update_package_status(self, shipmentId, packageId, **kwargs) -> ApiResponse
        
        Updates the status of the packages.
        
        Examples:
            literal blocks::
            
                ExternalFulfillmentShippingV20240911().update_package_status("value", "value")
        
        Args:
            shipmentId: object | required The ID of the shipment to which the package belongs.
            packageId: object | required The ID of the package whose status you want to update.
            key status: object |  **DEPRECATED**. Do not use. Package status is defined in the body parameter.
            body: PackageDeliveryStatus |  The body of the request.
        
        Returns:
            ApiResponse
        """
        return self._request(fill_query_params(kwargs.pop("path"), shipmentId, packageId), data=kwargs, add_marketplace=False)

    @sp_endpoint("/externalFulfillment/2024-09-11/shipments/{}/shippingOptions", method="GET")
    def retrieve_shipping_options(self, shipmentId, **kwargs) -> ApiResponse:
        """
        retrieve_shipping_options(self, shipmentId, **kwargs) -> ApiResponse
        
        Get a list of shipping options for a package in a shipment given the shipment's marketplace and channel. If the marketplace and channel have a pre-determined shipping option, then this operation returns an empty response.
        
        Examples:
            literal blocks::
            
                ExternalFulfillmentShippingV20240911().retrieve_shipping_options("value")
        
        Args:
            shipmentId: object | required The ID of the shipment to which the package belongs.
            key packageId: object | required The ID of the package for which you want to retrieve shipping options.
        
        Returns:
            ApiResponse
        """
        return self._request(fill_query_params(kwargs.pop("path"), shipmentId), params=kwargs, add_marketplace=False)

    @sp_endpoint("/externalFulfillment/2024-09-11/shipments/{}/invoice", method="POST")
    def generate_invoice(self, shipmentId, **kwargs) -> ApiResponse:
        """
        generate_invoice(self, shipmentId, **kwargs) -> ApiResponse
        
        Get invoices for the shipment you specify.
        
        Examples:
            literal blocks::
            
                ExternalFulfillmentShippingV20240911().generate_invoice("value")
        
        Args:
            shipmentId: object | required The ID of the shipment whose invoice you want.
        
        Returns:
            ApiResponse
        """
        return self._request(fill_query_params(kwargs.pop("path"), shipmentId), data=kwargs, add_marketplace=False)

    @sp_endpoint("/externalFulfillment/2024-09-11/shipments/{}/invoice", method="GET")
    def retrieve_invoice(self, shipmentId, **kwargs) -> ApiResponse:
        """
        retrieve_invoice(self, shipmentId, **kwargs) -> ApiResponse
        
        Retrieve invoices for the shipment you specify.
        
        Examples:
            literal blocks::
            
                ExternalFulfillmentShippingV20240911().retrieve_invoice("value")
        
        Args:
            shipmentId: object | required The ID of the shipment whose invoice you want to retrieve.
        
        Returns:
            ApiResponse
        """
        return self._request(fill_query_params(kwargs.pop("path"), shipmentId), params=kwargs, add_marketplace=False)

    @sp_endpoint("/externalFulfillment/2024-09-11/shipments/{}/shipLabels", method="PUT")
    def generate_ship_labels(self, shipmentId, **kwargs) -> ApiResponse:
        """
        generate_ship_labels(self, shipmentId, **kwargs) -> ApiResponse
        
        Generate and retrieve all shipping labels for one or more packages in the shipment you specify.
        
        Examples:
            literal blocks::
            
                ExternalFulfillmentShippingV20240911().generate_ship_labels("value")
        
        Args:
            shipmentId: object | required The ID of the shipment whose shipping labels you want to generate and retrieve.
            key shippingOptionId: object |  The ID of the shipping option whose shipping labels you want.
            key operation: object | required Specify whether you want to generate or regenerate a label.
            body: ShipLabelsInput |  Shipping details for when shipping is not done by the marketplace channel.
        
        Returns:
            ApiResponse
        """
        return self._request(fill_query_params(kwargs.pop("path"), shipmentId), data=kwargs, add_marketplace=False)
