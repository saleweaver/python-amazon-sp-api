from __future__ import annotations

from typing import Any

from sp_api.base import ApiResponse, Client, fill_query_params, sp_endpoint
from sp_api.util import normalize_csv_param


class OrdersV20260101(Client):
    """Orders API (version 2026-01-01).

    This is a newer Orders API version that uses different endpoints/parameters
    than the legacy v0 Orders API implemented by :class:`sp_api.api.orders.orders.Orders`.

    Model source:
    https://github.com/amzn/selling-partner-api-models/blob/main/models/orders-api-model/orders_2026-01-01.json
    """

    @sp_endpoint("/orders/2026-01-01/orders")
    def search_orders(self, **kwargs: Any) -> ApiResponse:
        """
        search_orders(self, **kwargs) -> ApiResponse
        
        Returns orders that are created or updated during the time period that you specify. You can filter the response for specific types of orders.
        
        Examples:
            literal blocks::
            
                OrdersV20260101().search_orders()
        
        Args:
            **kwargs:
        
        Returns:
            ApiResponse
        """

        normalize_csv_param(kwargs, "fulfillmentStatuses")
        normalize_csv_param(kwargs, "marketplaceIds")
        normalize_csv_param(kwargs, "fulfilledBy")
        normalize_csv_param(kwargs, "includedData")
        return self._request(kwargs.pop("path"), params={**kwargs})

    @sp_endpoint("/orders/2026-01-01/orders/{}")
    def get_order(self, order_id: str, **kwargs: Any) -> ApiResponse:
        """
        get_order(self, order_id, **kwargs) -> ApiResponse
        
        Returns the order that you specify.
        
        Examples:
            literal blocks::
            
                OrdersV20260101().get_order("value")
        
        Args:
            order_id:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """

        normalize_csv_param(kwargs, "includedData")
        return self._request(
            fill_query_params(kwargs.pop("path"), order_id),
            params={**kwargs},
            add_marketplace=False,
        )
