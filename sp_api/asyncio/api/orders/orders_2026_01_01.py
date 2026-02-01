from __future__ import annotations

from typing import Any

from sp_api.asyncio.base import AsyncBaseClient
from sp_api.base import ApiResponse, fill_query_params, sp_endpoint
from sp_api.util import normalize_csv_param


class OrdersV20260101(AsyncBaseClient):
    """Orders API (version 2026-01-01) - async client.

    This is a newer Orders API version that uses different endpoints/parameters
    than the legacy v0 Orders API implemented by :class:`sp_api.asyncio.api.orders.orders.Orders`.

    Model source:
    https://github.com/amzn/selling-partner-api-models/blob/main/models/orders-api-model/orders_2026-01-01.json
    """

    @sp_endpoint("/orders/2026-01-01/orders")
    async def search_orders(self, **kwargs: Any) -> ApiResponse:
        """Search orders (async)."""

        normalize_csv_param(kwargs, "fulfillmentStatuses")
        normalize_csv_param(kwargs, "marketplaceIds")
        normalize_csv_param(kwargs, "fulfilledBy")
        normalize_csv_param(kwargs, "includedData")

        return await self._request(kwargs.pop("path"), params={**kwargs})

    @sp_endpoint("/orders/2026-01-01/orders/{}")
    async def get_order(self, order_id: str, **kwargs: Any) -> ApiResponse:
        """Get order by orderId (async)."""

        normalize_csv_param(kwargs, "includedData")
        return await self._request(
            fill_query_params(kwargs.pop("path"), order_id),
            params={**kwargs},
            add_marketplace=False,
        )
