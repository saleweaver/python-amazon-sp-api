from sp_api.base import Client, sp_endpoint, fill_query_params, ApiResponse
from sp_api.util import normalize_csv_param


class OrdersV0(Client):

    @sp_endpoint("/orders/v0/orders")
    def get_orders(self, **kwargs) -> ApiResponse:
        """
        get_orders(self, **kwargs) -> ApiResponse
        
        Returns orders that are created or updated during the specified time period. If you want to return specific types of orders, you can apply filters to your request. `NextToken` doesn't affect any filters that you include in your request; it only impacts the pagination for the filtered orders response.
        
        Examples:
            literal blocks::
            
                OrdersV0().get_orders()
        
        Args:
            **kwargs:
        
        Returns:
            ApiResponse
        """
        normalize_csv_param(kwargs, "OrderStatuses")
        normalize_csv_param(kwargs, "MarketplaceIds")
        normalize_csv_param(kwargs, "FulfillmentChannels")
        normalize_csv_param(kwargs, "PaymentMethods")
        normalize_csv_param(kwargs, "AmazonOrderIds")

        if "RestrictedResources" in kwargs:
            return self._access_restricted(kwargs)
        return self._request(kwargs.pop("path"), params={**kwargs})

    @sp_endpoint("/orders/v0/orders/{}")
    def get_order(self, order_id: str, **kwargs) -> ApiResponse:
        """
        get_order(self, order_id, **kwargs) -> ApiResponse
        
        Returns the order that you specify.
        
        Examples:
            literal blocks::
            
                OrdersV0().get_order("value")
        
        Args:
            order_id:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """
        if "RestrictedResources" in kwargs:
            kwargs.update(
                {"original_path": fill_query_params(kwargs.get("path"), order_id)}
            )
            return self._access_restricted(kwargs)
        return self._request(
            fill_query_params(kwargs.pop("path"), order_id),
            params={**kwargs},
            add_marketplace=False,
        )

    @sp_endpoint("/orders/v0/orders/{}/orderItems")
    def get_order_items(self, order_id: str, **kwargs) -> ApiResponse:
        """
        get_order_items(self, order_id, **kwargs) -> ApiResponse
        
        Returns detailed order item information for the order that you specify. If `NextToken` is provided, it's used to retrieve the next page of order items.
                        __Note__: When an order is in the Pending state (the order has been placed but payment has not been authorized), the getOrderItems operation does not return information about pricing, taxes, shipping charges, gift status or promotions for the order items in the order. After an order leaves the Pending state (this occurs when payment has been authorized) and enters the Unshipped, Partially Shipped, or Shipped state, the getOrderItems operation returns information about pricing, taxes, shipping charges, gift status and promotions for the order items in the order.
        
        Examples:
            literal blocks::
            
                OrdersV0().get_order_items("value")
        
        Args:
            order_id:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """
        if "RestrictedResources" in kwargs:
            kwargs.update(
                {"original_path": fill_query_params(kwargs.get("path"), order_id)}
            )
            return self._access_restricted(kwargs)
        return self._request(
            fill_query_params(kwargs.pop("path"), order_id), params={**kwargs}
        )

    @sp_endpoint("/orders/v0/orders/{}/address")
    def get_order_address(self, order_id, **kwargs) -> ApiResponse:
        """
        get_order_address(self, order_id, **kwargs) -> ApiResponse
        
        Returns the shipping address for the order that you specify.
        
        Examples:
            literal blocks::
            
                OrdersV0().get_order_address("value")
        
        Args:
            order_id:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """
        return self._request(
            fill_query_params(kwargs.pop("path"), order_id), params={**kwargs}
        )

    @sp_endpoint("/orders/v0/orders/{}/buyerInfo")
    def get_order_buyer_info(self, order_id: str, **kwargs) -> ApiResponse:
        """
        get_order_buyer_info(self, order_id, **kwargs) -> ApiResponse
        
        Returns buyer information for the order that you specify.
        
        Examples:
            literal blocks::
            
                OrdersV0().get_order_buyer_info("value")
        
        Args:
            order_id:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """
        return self._request(
            fill_query_params(kwargs.pop("path"), order_id), params={**kwargs}
        )

    @sp_endpoint("/orders/v0/orders/{}/orderItems/buyerInfo")
    def get_order_items_buyer_info(self, order_id: str, **kwargs) -> ApiResponse:
        """
        get_order_items_buyer_info(self, order_id, **kwargs) -> ApiResponse
        
        Returns buyer information for the order items in the order that you specify.
        
        Examples:
            literal blocks::
            
                OrdersV0().get_order_items_buyer_info("value")
        
        Args:
            order_id:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """
        return self._request(
            fill_query_params(kwargs.pop("path"), order_id), params=kwargs
        )

    @sp_endpoint("/orders/v0/orders/{}/shipment", method="POST")
    def update_shipment_status(self, order_id: str, **kwargs) -> ApiResponse:
        """
        update_shipment_status(self, order_id, **kwargs) -> ApiResponse
        
        Update the shipment status for an order that you specify.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        5                                       15
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                OrdersV0().update_shipment_status("value")
        
        Args:
            orderId: object | required An Amazon-defined order identifier, in 3-7-7 format.
            payload: UpdateShipmentStatusRequest | required The request body for the `updateShipmentStatus` operation.
        
        Returns:
            ApiResponse
        """
        return self._request(
            fill_query_params(kwargs.pop("path"), order_id),
            res_no_data=True,
            data=kwargs,
        )

    @sp_endpoint("/orders/v0/orders/{}/shipmentConfirmation", method="POST")
    def confirm_shipment(self, order_id: str, **kwargs) -> ApiResponse:
        """
        confirm_shipment(self, order_id, **kwargs) -> ApiResponse
        
        Updates the shipment confirmation status for a specified order.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        2                                       10
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                OrdersV0().confirm_shipment("value")
        
        Args:
            orderId: object | required An Amazon-defined order identifier, in 3-7-7 format.
            payload: ConfirmShipmentRequest | required Request body of `confirmShipment`.
        
        Returns:
            ApiResponse
        """
        return self._request(
            fill_query_params(kwargs.pop("path"), order_id),
            add_marketplace=False,
            res_no_data=True,
            data=kwargs,
        )

    @sp_endpoint("/tokens/2021-03-01/restrictedDataToken", method="POST")
    def _get_token(self, **kwargs):
        data_elements = kwargs.pop("RestrictedResources")

        restricted_resources = [
            {
                "method": "GET",
                "path": kwargs.get("original_path"),
                "dataElements": data_elements,
            }
        ]

        return self._request(
            kwargs.pop("path"),
            data={"restrictedResources": restricted_resources, **kwargs},
        )

    def _access_restricted(self, kwargs):
        if "original_path" not in kwargs:
            kwargs.update({"original_path": kwargs["path"]})
        token = self._get_token(**kwargs).payload
        self.restricted_data_token = token["restrictedDataToken"]
        r = self._request(kwargs.pop("original_path"), params={**kwargs})
        if not self.keep_restricted_data_token:
            self.restricted_data_token = None
        return r








    @sp_endpoint("/orders/v0/orders/{}/regulatedInfo", method="GET")
    def get_order_regulated_info(self, orderId, **kwargs) -> ApiResponse:
        """
        get_order_regulated_info(self, orderId, **kwargs) -> ApiResponse
        
        Returns regulated information for the order that you specify.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        0.5                                     30
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                OrdersV0().get_order_regulated_info("value")
        
        Args:
            orderId: object | required The Amazon order identifier in 3-7-7 format.
        
        Returns:
            ApiResponse
        """
        return self._request(fill_query_params(kwargs.pop("path"), orderId), params=kwargs)

    @sp_endpoint("/orders/v0/orders/{}/regulatedInfo", method="PATCH")
    def update_verification_status(self, orderId, **kwargs) -> ApiResponse:
        """
        update_verification_status(self, orderId, **kwargs) -> ApiResponse
        
        Updates (approves or rejects) the verification status of an order containing regulated products.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        0.5                                     30
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                OrdersV0().update_verification_status("value")
        
        Args:
            orderId: object | required The Amazon order identifier in 3-7-7 format.
            payload: UpdateVerificationStatusRequest | required The request body for the `updateVerificationStatus` operation.
        
        Returns:
            ApiResponse
        """
        return self._request(fill_query_params(kwargs.pop("path"), orderId), data=kwargs)
