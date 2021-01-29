from sp_api.api.orders.models.get_order_address_response import GetOrderAddressResponse
from sp_api.api.orders.models.get_order_buyer_info_response import GetOrderBuyerInfoResponse
from sp_api.base import sp_endpoint, fill_query_params
from sp_api.api.orders.models.get_order_items_response import GetOrderItemsResponse
from sp_api.api.orders.models.get_order_response import GetOrderResponse
from sp_api.api.orders.models.get_orders_response import GetOrdersResponse
from sp_api.base import Client, Marketplaces


class Orders(Client):
    """
    :link: https://github.com/amzn/selling-partner-api-docs/tree/main/references/orders-api
    """

    def __init__(self, marketplace=Marketplaces.US, *, refresh_token=None, account='default', credentials=None):
        super().__init__(marketplace, refresh_token, account, credentials)

    @sp_endpoint('/orders/v0/orders')
    def get_orders(self, **kwargs) -> GetOrdersResponse:
        """
        get_orders(self, **kwargs) -> GetOrdersResponse
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
            GetOrdersResponse:


        """
        return GetOrdersResponse(
            **self._request(kwargs.pop('path'), params={**kwargs}).json())

    @sp_endpoint('/orders/v0/orders/{}')
    def get_order(self, order_id: str, **kwargs) -> GetOrderResponse:
        """
        get_order(self, order_id: str, **kwargs) -> GetOrderResponse
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
            GetOrderResponse:


        """
        return GetOrderResponse(
            **self._request(fill_query_params(kwargs.pop('path'), order_id), params={**kwargs}, add_marketplace=False).json()
        )

    @sp_endpoint('/orders/v0/orders/{}/orderItems')
    def get_order_items(self, order_id: str, **kwargs) -> GetOrderItemsResponse:
        """
        get_order_items(self, order_id: str, **kwargs) -> GetOrderItemsResponse
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
            GetOrderItemsResponse:

        """
        return GetOrderItemsResponse(
            **self._request(fill_query_params(kwargs.pop('path'), order_id), params={**kwargs}).json())

    @sp_endpoint('/orders/v0/orders/{}/address')
    def get_order_address(self, order_id, **kwargs):
        """
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

        """
        return GetOrderAddressResponse(
            **self._request(fill_query_params(kwargs.pop('path'), order_id), params={**kwargs}).json()
        )

    @sp_endpoint('/orders/v0/orders/{}/buyerInfo')
    def get_order_buyer_info(self, order_id: str, **kwargs) -> GetOrderBuyerInfoResponse:
        """
        get_order_buyer_info(self, order_id: str, **kwargs) -> GetOrderBuyerInfoResponse
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
        return GetOrderBuyerInfoResponse(
            **self._request(fill_query_params(kwargs.pop('path'), order_id), params={**kwargs}).json()
        )
