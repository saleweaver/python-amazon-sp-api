from sp_api.api.orders.models.get_order_address_response import GetOrderAddressResponse
from sp_api.api.orders.models.get_order_buyer_info_response import GetOrderBuyerInfoResponse
from sp_api.base import sp_endpoint, fill_query_params
from sp_api.api.orders.models.get_order_items_response import GetOrderItemsResponse
from sp_api.api.orders.models.get_order_response import GetOrderResponse
from sp_api.api.orders.models.get_orders_response import GetOrdersResponse
from sp_api.base import Client, Marketplaces


class Orders(Client):
    def __init__(self, marketplace=Marketplaces.US, refresh_token=None):
        super().__init__(marketplace, refresh_token)

    @sp_endpoint('/orders/v0/orders')
    def get_orders(self, **kwargs):
        """
        Returns orders created or updated during the time frame indicated by the specified parameters.
        You can also apply a range of filtering criteria to narrow the list of orders returned.
        If NextToken is present, that will be used to retrieve the orders instead of other criteria.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 1 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        :param kwargs:
        :return:
        """
        return GetOrdersResponse(
            **self._request(kwargs.pop('path'), params={**kwargs}).json())

    @sp_endpoint('/orders/v0/orders/{}')
    def get_order(self, order_id, **kwargs):
        """
        Returns the order indicated by the specified order ID.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 1 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        :param order_id:
        :param kwargs:
        :return:
        """
        return GetOrderResponse(
            **self._request(fill_query_params(kwargs.pop('path'), order_id),
                            params={**kwargs}).json())

    @sp_endpoint('/orders/v0/orders/{}/orderItems')
    def get_order_items(self, order_id, **kwargs):
        """
        Returns detailed order item information for the order indicated by the specified order ID.
        If NextToken is provided, it's used to retrieve the next page of order items.

        Note: When an order is in the Pending state (the order has been placed but payment has not been authorized),
        the getOrderItems operation does not return information about pricing, taxes, shipping charges, gift status or
        promotions for the order items in the order.
        After an order leaves the Pending state (this occurs when payment has been authorized) and enters the Unshipped,
        Partially Shipped, or Shipped state, the getOrderItems operation returns information about pricing, taxes,
        shipping charges, gift status and promotions for the order items in the order.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 1 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        :param order_id:
        :param kwargs:
        :return:
        """
        return GetOrderItemsResponse(
            **self._request(fill_query_params(kwargs.pop('path'), order_id), params={**kwargs}).json())

    @sp_endpoint('/orders/v0/orders/{}/address')
    def get_order_address(self, order_id, **kwargs):
        return GetOrderAddressResponse(
            **self._request(fill_query_params(kwargs.pop('path'), order_id), params={**kwargs}).json()
        )

    @sp_endpoint('/orders/v0/orders/{}/buyerInfo')
    def get_order_buyer_info(self, order_id, **kwargs):
        return GetOrderBuyerInfoResponse(
            **self._request(fill_query_params(kwargs.pop('path'), order_id), params={**kwargs}).json()
        )
