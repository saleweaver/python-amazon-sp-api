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
        """Search orders.

        Corresponds to GET /orders/2026-01-01/orders (operationId: searchOrders).

        Notes:
        - Parameters are lowerCamelCase in this version (e.g. createdAfter).
        - List parameters can be passed as Python lists; they will be normalized
          into a comma-delimited string.
        """

        normalize_csv_param(kwargs, "fulfillmentStatuses")
        normalize_csv_param(kwargs, "marketplaceIds")
        normalize_csv_param(kwargs, "fulfilledBy")
        normalize_csv_param(kwargs, "includedData")
        print(kwargs)
        return self._request(kwargs.pop("path"), params={**kwargs})

    @sp_endpoint("/orders/2026-01-01/orders/{}")
    def get_order(self, order_id: str, **kwargs: Any) -> ApiResponse:
        """Get order by orderId.

        Corresponds to GET /orders/2026-01-01/orders/{orderId} (operationId: getOrder).

        Args:
            order_id: The Amazon order identifier.
            includedData: Optional list of datasets to include in the response.
        """

        normalize_csv_param(kwargs, "includedData")
        return self._request(
            fill_query_params(kwargs.pop("path"), order_id),
            params={**kwargs},
            add_marketplace=False,
        )
