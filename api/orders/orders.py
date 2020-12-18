from api.orders.models.get_order_items_response import GetOrderItemsResponse
from api.orders.models.get_order_response import GetOrderResponse
from api.orders.models.get_orders_response import GetOrdersResponse
from base.client import Client
from base.helpers import fill_query_params, sp_endpoint
from base.marketplaces import Marketplaces


class Orders(Client):
    def __init__(self, marketplace=Marketplaces.US, refresh_token=None):
        super().__init__(marketplace, refresh_token)

    @sp_endpoint('/orders/v0/orders')
    def get_orders(self, **kwargs):
        return GetOrdersResponse(
            **self.request(kwargs.pop('path'), params={**kwargs}).json())

    @sp_endpoint('/orders/v0/orders/{}')
    def get_order(self, order_id, **kwargs):
        return GetOrderResponse(
            **self.request(fill_query_params(kwargs.pop('path'), order_id),
                           params={**kwargs}).json())

    @sp_endpoint('/orders/v0/orders/{}/orderItems')
    def get_order_items(self, order_id, **kwargs):
        return GetOrderItemsResponse(
            **self.request(fill_query_params(kwargs.pop('path'), order_id), params={**kwargs}).json())
