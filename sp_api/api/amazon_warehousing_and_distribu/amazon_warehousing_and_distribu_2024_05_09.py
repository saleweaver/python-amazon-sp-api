import urllib.parse

from sp_api.base import Client, sp_endpoint, fill_query_params, ApiResponse


class AmazonWarehousingAndDistributionV20240509(Client):
    """
    AmazonWarehousingAndDistribu SP-API Client
    :link:

    The Selling Partner API for Amazon Warehousing and Distribution (AWD).
    """

    @sp_endpoint("/awd/2024-05-09/inboundShipments/{}", method="GET")
    def get_inbound_shipment(self, shipmentId, **kwargs) -> ApiResponse:
        """
        get_inbound_shipment(self, shipmentId, **kwargs) -> ApiResponse
        
        Retrieves an AWD inbound shipment.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        2                                       2
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                AmazonWarehousingAndDistributionV20240509().get_inbound_shipment("value")
        
        Args:
            shipmentId: object | required ID for the shipment. A shipment contains the cases being inbounded.
            key skuQuantities: object |  If equal to `SHOW`, the response includes the shipment SKU quantity details.
                Defaults to `HIDE`, in which case the response does not contain SKU quantities
        
        Returns:
            ApiResponse
        """

        return self._request(
            fill_query_params(kwargs.pop("path"), shipmentId), params=kwargs
        )

    @sp_endpoint("/awd/2024-05-09/inboundShipments", method="GET")
    def list_inbound_shipments(self, **kwargs) -> ApiResponse:
        """
        list_inbound_shipments(self, **kwargs) -> ApiResponse
        
        Retrieves a summary of all the inbound AWD shipments associated with a merchant, with the ability to apply optional filters.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       1
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                AmazonWarehousingAndDistributionV20240509().list_inbound_shipments()
        
        Args:
            key sortBy: object |  Field to sort results by. By default, the response will be sorted by UPDATED_AT.
            key sortOrder: object |  Sort the response in ASCENDING or DESCENDING order. By default, the response will be sorted in DESCENDING order.
            key shipmentStatus: object |  Filter by inbound shipment status.
            key updatedAfter: object |  List the inbound shipments that were updated after a certain time (inclusive). The date must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format.
            key updatedBefore: object |  List the inbound shipments that were updated before a certain time (inclusive). The date must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format.
            key maxResults: object |  Maximum number of results to return.
            key nextToken: object |  A token that is used to retrieve the next page of results. The response includes `nextToken` when the number of results exceeds the specified `maxResults` value. To get the next page of results, call the operation with this token and include the same arguments as the call that produced the token. To get a complete list, call this operation until `nextToken` is null. Note that this operation can return empty pages.
        
        Returns:
            ApiResponse
        """

        return self._request(kwargs.pop("path"), params=kwargs)

    @sp_endpoint("/awd/2024-05-09/inventory", method="GET")
    def list_inventory(self, **kwargs) -> ApiResponse:
        """
        list_inventory(self, **kwargs) -> ApiResponse
        
        Lists AWD inventory associated with a merchant with the ability to apply optional filters.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        2                                       2
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                AmazonWarehousingAndDistributionV20240509().list_inventory()
        
        Args:
            key sku: object |  Filter by seller or merchant SKU for the item.
            key sortOrder: object |  Sort the response in `ASCENDING` or `DESCENDING` order.
            key details: object |  Set to `SHOW` to return summaries with additional inventory details. Defaults to `HIDE,` which returns only inventory summary totals.
            key nextToken: object |  A token that is used to retrieve the next page of results. The response includes `nextToken` when the number of results exceeds the specified `maxResults` value. To get the next page of results, call the operation with this token and include the same arguments as the call that produced the token. To get a complete list, call this operation until `nextToken` is null. Note that this operation can return empty pages.
            key maxResults: object |  Maximum number of results to return.
        
        Returns:
            ApiResponse
        """

        return self._request(kwargs.pop("path"), params=kwargs)

    @sp_endpoint("/awd/2024-05-09/inboundOrders", method="POST")
    def create_inbound(self, **kwargs) -> ApiResponse:
        """
        create_inbound(self, **kwargs) -> ApiResponse
        
        Creates a draft AWD inbound order with a list of packages for inbound shipment. The operation creates one shipment per order.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       1
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                AmazonWarehousingAndDistributionV20240509().create_inbound()
        
        Args:
            body: InboundOrderCreationData | required Payload for creating an inbound order.
        
        Returns:
            ApiResponse
        """
        return self._request(kwargs.pop("path"), data=kwargs)

    @sp_endpoint("/awd/2024-05-09/inboundOrders/{}", method="GET")
    def get_inbound(self, orderId, **kwargs) -> ApiResponse:
        """
        get_inbound(self, orderId, **kwargs) -> ApiResponse
        
        Retrieves an AWD inbound order.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        2                                       2
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                AmazonWarehousingAndDistributionV20240509().get_inbound("value")
        
        Args:
            orderId: object | required The ID of the inbound order that you want to retrieve.
        
        Returns:
            ApiResponse
        """
        return self._request(fill_query_params(kwargs.pop("path"), orderId), params=kwargs)

    @sp_endpoint("/awd/2024-05-09/inboundOrders/{}", method="PUT")
    def update_inbound(self, orderId, **kwargs) -> ApiResponse:
        """
        update_inbound(self, orderId, **kwargs) -> ApiResponse
        
        Updates an AWD inbound order that is in `DRAFT` status and not yet confirmed. Use this operation to update the `packagesToInbound`, `originAddress` and `preferences` attributes.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       1
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                AmazonWarehousingAndDistributionV20240509().update_inbound("value")
        
        Args:
            orderId: object | required The ID of the inbound order that you want to update.
            body: InboundOrder | required Represents an AWD inbound order.
        
        Returns:
            ApiResponse
        """
        return self._request(fill_query_params(kwargs.pop("path"), orderId), data=kwargs)

    @sp_endpoint("/awd/2024-05-09/inboundOrders/{}/cancellation", method="POST")
    def cancel_inbound(self, orderId, **kwargs) -> ApiResponse:
        """
        cancel_inbound(self, orderId, **kwargs) -> ApiResponse
        
        Cancels an AWD Inbound order and its associated shipment.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       1
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                AmazonWarehousingAndDistributionV20240509().cancel_inbound("value")
        
        Args:
            orderId: object | required The ID of the inbound order you want to cancel.
        
        Returns:
            ApiResponse
        """
        return self._request(fill_query_params(kwargs.pop("path"), orderId), data=kwargs)

    @sp_endpoint("/awd/2024-05-09/inboundOrders/{}/confirmation", method="POST")
    def confirm_inbound(self, orderId, **kwargs) -> ApiResponse:
        """
        confirm_inbound(self, orderId, **kwargs) -> ApiResponse
        
        Confirms an AWD inbound order in `DRAFT` status.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       1
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                AmazonWarehousingAndDistributionV20240509().confirm_inbound("value")
        
        Args:
            orderId: object | required The ID of the inbound order that you want to confirm.
        
        Returns:
            ApiResponse
        """
        return self._request(fill_query_params(kwargs.pop("path"), orderId), data=kwargs)


    @sp_endpoint("/awd/2024-05-09/inboundShipments/{}/labels", method="GET")
    def get_inbound_shipment_labels(self, shipmentId, **kwargs) -> ApiResponse:
        """
        get_inbound_shipment_labels(self, shipmentId, **kwargs) -> ApiResponse
        
        Retrieves the box labels for a shipment ID that you specify. This is an asynchronous operation. If the label status is `GENERATED`, then the label URL is available.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       2
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                AmazonWarehousingAndDistributionV20240509().get_inbound_shipment_labels("value")
        
        Args:
            shipmentId: object | required ID for the shipment.
            key pageType: object |  Page type for the generated labels. The default is `PLAIN_PAPER`.
            key formatType: object |  The format type of the output file that contains your labels. The default format type is `PDF`.
        
        Returns:
            ApiResponse
        """
        return self._request(fill_query_params(kwargs.pop("path"), shipmentId), params=kwargs)

    @sp_endpoint("/awd/2024-05-09/inboundShipments/{}/transport", method="PUT")
    def update_inbound_shipment_transport_details(self, shipmentId, **kwargs) -> ApiResponse:
        """
        update_inbound_shipment_transport_details(self, shipmentId, **kwargs) -> ApiResponse
        
        Updates transport details for an AWD shipment.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       1
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                AmazonWarehousingAndDistributionV20240509().update_inbound_shipment_transport_details("value")
        
        Args:
            shipmentId: object | required The shipment ID.
            body: TransportationDetails | required Transportation details for the shipment.
        
        Returns:
            ApiResponse
        """
        return self._request(fill_query_params(kwargs.pop("path"), shipmentId), data=kwargs)

    @sp_endpoint("/awd/2024-05-09/inboundEligibility", method="POST")
    def check_inbound_eligibility(self, **kwargs) -> ApiResponse:
        """
        check_inbound_eligibility(self, **kwargs) -> ApiResponse
        
        Determines if the packages you specify are eligible for an AWD inbound order and contains error details for ineligible packages.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       1
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                AmazonWarehousingAndDistributionV20240509().check_inbound_eligibility()
        
        Args:
            body: InboundPackages | required Represents the packages you want to inbound.
        
        Returns:
            ApiResponse
        """
        return self._request(kwargs.pop("path"), data=kwargs)



    @sp_endpoint("/awd/2024-05-09/replenishmentOrders", method="GET")
    def list_replenishment_orders(self, **kwargs) -> ApiResponse:
        """
        list_replenishment_orders(self, **kwargs) -> ApiResponse
        
        Retrieves all the AWD replenishment orders pertaining to a merchant with optional filters.
        API by default will sort orders by updatedAt attribute in descending order.
        
        Examples:
            literal blocks::
            
                AmazonWarehousingAndDistributionV20240509().list_replenishment_orders()
        
        Args:
            key updatedAfter: object |  Get the replenishment orders updated after certain time (Inclusive)
                Date should be in ISO 8601 format as defined by date-time in - https://www.rfc-editor.org/rfc/rfc3339.
            key updatedBefore: object |  Get the replenishment orders updated before certain time (Inclusive)
                Date should be in ISO 8601 format as defined by date-time in - https://www.rfc-editor.org/rfc/rfc3339.
            key sortOrder: object |  Sort the response in ASCENDING or DESCENDING order. The default sort order is DESCENDING.
            key maxResults: object |  Maximum results to be returned in a single response.
            key nextToken: object |  A token that is used to retrieve the next page of results. The response includes `nextToken` when the number of results exceeds the specified `maxResults` value. To get the next page of results, call the operation with this token and include the same arguments as the call that produced the token. To get a complete list, call this operation until `nextToken` is null. Note that this operation can return empty pages.
        
        Returns:
            ApiResponse
        """
        return self._request(kwargs.pop("path"), params=kwargs)

    @sp_endpoint("/awd/2024-05-09/replenishmentOrders", method="POST")
    def create_replenishment_order(self, **kwargs) -> ApiResponse:
        """
        create_replenishment_order(self, **kwargs) -> ApiResponse
        
        Creates an AWD replenishment order with given products to replenish.
        The API will return the order ID of the newly created order and also start an async validation check on the products to e.
        The order status will transition to ELIGIBLE/INELIGIBLE status from VALIDATING post validation check
        
        Examples:
            literal blocks::
            
                AmazonWarehousingAndDistributionV20240509().create_replenishment_order()
        
        Args:
            body: ReplenishmentOrderCreationData | required Payload for creating a replenishment order.
        
        Returns:
            ApiResponse
        """
        return self._request(kwargs.pop("path"), data=kwargs)

    @sp_endpoint("/awd/2024-05-09/replenishmentOrders/{}", method="GET")
    def get_replenishment_order(self, orderId, **kwargs) -> ApiResponse:
        """
        get_replenishment_order(self, orderId, **kwargs) -> ApiResponse
        
        Retrieves an AWD Replenishment order with a set of shipments containing items that is/was planned to be replenished into an FBA node.
        
        Examples:
            literal blocks::
            
                AmazonWarehousingAndDistributionV20240509().get_replenishment_order("value")
        
        Args:
            orderId: object | required ID of the replenishment order to be retrieved.
        
        Returns:
            ApiResponse
        """
        return self._request(fill_query_params(kwargs.pop("path"), orderId), params=kwargs)

    @sp_endpoint("/awd/2024-05-09/replenishmentOrders/{}/confirmation", method="POST")
    def confirm_replenishment_order(self, orderId, **kwargs) -> ApiResponse:
        """
        confirm_replenishment_order(self, orderId, **kwargs) -> ApiResponse
        
        Confirms an AWD replenishment order in ELIGIBLE state with a set of shipments containing items that are needed to be replenished to an FBA node.
        Order can only be confirmed in ELIGIBLE state.
        
        Examples:
            literal blocks::
            
                AmazonWarehousingAndDistributionV20240509().confirm_replenishment_order("value")
        
        Args:
            orderId: object | required ID of the replenishment order to be confirmed.
        
        Returns:
            ApiResponse
        """
        return self._request(fill_query_params(kwargs.pop("path"), orderId), data=kwargs)
