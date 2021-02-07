from sp_api.base import sp_endpoint, fill_query_params, ApiResponse
from sp_api.base import Client, Marketplaces


class Orders(Client):
    """
    :link: https://github.com/amzn/selling-partner-api-docs/tree/main/references/orders-api
    """

    @sp_endpoint('/orders/v0/orders')
    def get_orders(self, **kwargs) -> ApiResponse:
        """
        get_orders(self, **kwargs) -> ApiResponse
        Returns orders created or updated during the time frame indicated by the specified parameters.
        You can also apply a range of filtering criteria to narrow the list of orders returned.
        If NextToken is present, that will be used to retrieve the orders instead of other criteria.

        **Usage Plan:**

        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       1
        ======================================  ==============


        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            key CreatedAfter: date
            key CreatedBefore: date
            key LastUpdatedAfter: date
            key LastUpdatedBefore: date
            key OrderStatuses: [str]
            key MarketplaceIds: [str]
            key FulfillmentChannels: [str]
            key PaymentMethods: [str]
            key BuyerEmail: str
            key SellerOrderId: str
            key MaxResultsPerPage: int
            key EasyShipShipmentStatuses: [str]
            key NextToken: str
            key AmazonOrderIds: [str]


        Returns:
            ApiResponse:


        """
        return self._request(kwargs.pop('path'), params={**kwargs})

    @sp_endpoint('/orders/v0/orders/{}')
    def get_order(self, order_id: str, **kwargs) -> ApiResponse:
        """
        get_order(self, order_id: str, **kwargs) -> ApiResponse
        Returns the order indicated by the specified order ID.

        **Usage Plan:**

        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       1
        ======================================  ==============


        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            order_id: str
            **kwargs:

        Returns:
            ApiResponse:


        """
        return self._request(fill_query_params(kwargs.pop('path'), order_id), params={**kwargs}, add_marketplace=False)

    @sp_endpoint('/orders/v0/orders/{}/orderItems')
    def get_order_items(self, order_id: str, **kwargs) -> ApiResponse:
        """
        get_order_items(self, order_id: str, **kwargs) -> ApiResponse

        Returns detailed order item information for the order indicated by the specified order ID.
        If NextToken is provided, it's used to retrieve the next page of order items.

        Note: When an order is in the Pending state (the order has been placed but payment has not been authorized),
        the getOrderItems operation does not return information about pricing, taxes, shipping charges, gift status or
        promotions for the order items in the order.
        After an order leaves the Pending state (this occurs when payment has been authorized) and enters the Unshipped,
        Partially Shipped, or Shipped state, the getOrderItems operation returns information about pricing, taxes,
        shipping charges, gift status and promotions for the order items in the order.


        **Usage Plan:**

        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       1
        ======================================  ==============



        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            order_id: str
            **kwargs:

        Returns:
            ApiResponse:

        """
        return self._request(fill_query_params(kwargs.pop('path'), order_id), params={**kwargs})

    @sp_endpoint('/orders/v0/orders/{}/address')
    def get_order_address(self, order_id, **kwargs) -> ApiResponse:
        """
        get_order_address(self, order_id, **kwargs) -> ApiResponse

        Returns the shipping address for the order indicated by the specified order ID.

        :note: To get useful information from this method, you need to have access to PII.

        **Usage Plan:**

        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       1
        ======================================  ==============


        Args:
            order_id: str
            **kwargs:

        Returns:
            ApiResponse
        """
        return self._request(fill_query_params(kwargs.pop('path'), order_id), params={**kwargs})

    @sp_endpoint('/orders/v0/orders/{}/buyerInfo')
    def get_order_buyer_info(self, order_id: str, **kwargs) -> ApiResponse:
        """
        get_order_buyer_info(self, order_id: str, **kwargs) -> ApiResponse
        Returns buyer information for the order indicated by the specified order ID.

        :note: To get useful information from this method, you need to have access to PII.


        **Usage Plan:**

        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       1
        ======================================  ==============


        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            order_id: str
            **kwargs:

        Returns:
            GetOrderBuyerInfoResponse:

        """
        return self._request(fill_query_params(kwargs.pop('path'), order_id), params={**kwargs})

    @sp_endpoint('/orders/v0/orders/{}/orderItems/buyerInfo')
    def get_order_items_buyer_info(self, order_id: str, **kwargs) -> ApiResponse:
        """
        get_order_items_buyer_info(self, order_id: str, **kwargs) -> ApiResponse

        Returns buyer information in the order items of the order indicated by the specified order ID.

        **Usage Plan:**

        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       1
        ======================================  ==============

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            order_id: str
            key NextToken: str | retrieve data by next token

        Returns:
            ApiResponse
        """
        return self._request(fill_query_params(kwargs.pop('path'), order_id), params=kwargs)
