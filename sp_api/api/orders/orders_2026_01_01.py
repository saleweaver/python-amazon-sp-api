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
        Returns orders that are created or updated during the time period that you specify.
        You can filter the response for specific types of orders.

        **Usage Plan:**

        ======================================  =====================
        Rate (requests per second)               Burst
        ======================================  =====================
        See x-amzn-ratelimit-limit response      See Amazon docs
        ======================================  =====================

        Note:
            The SP-API returns an `x-amzn-ratelimit-limit` (or similar) response header indicating the rate limit
            applied to the request. Rate and burst can vary by seller/account and by any Amazon-granted overrides.

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Examples:
            literal blocks::

                OrdersV20260101().search_orders(
                    createdAfter="2026-01-01T00:00:00Z",
                    marketplaceIds=["A1PA6795UKMFR9"]
                )

        Args:
            key createdAfter: str
            key createdBefore: str
            key lastUpdatedAfter: str
            key lastUpdatedBefore: str
            key fulfillmentStatuses: [str] | str
            key marketplaceIds: [str] | str
            key fulfilledBy: [str] | str
            key includedData: [str] | str
            key paginationToken: str
            key maxResultsPerPage: int

        Returns:
            ApiResponse:


        """

        normalize_csv_param(kwargs, "fulfillmentStatuses")
        normalize_csv_param(kwargs, "marketplaceIds")
        normalize_csv_param(kwargs, "fulfilledBy")
        normalize_csv_param(kwargs, "includedData")
        return self._request(kwargs.pop("path"), params={**kwargs})

    @sp_endpoint("/orders/2026-01-01/orders/{}")
    def get_order(self, order_id: str, **kwargs: Any) -> ApiResponse:
        """
        get_order(self, order_id: str, **kwargs) -> ApiResponse
        Returns the order that you specify.

        **Usage Plan:**

        ======================================  =====================
        Rate (requests per second)               Burst
        ======================================  =====================
        See x-amzn-ratelimit-limit response      See Amazon docs
        ======================================  =====================

        Note:
            The SP-API returns an `x-amzn-ratelimit-limit` (or similar) response header indicating the rate limit
            applied to the request. Rate and burst can vary by seller/account and by any Amazon-granted overrides.

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Examples:
            literal blocks::

                OrdersV20260101().get_order(
                    "306-9860906-6213927",
                    includedData=["orderItems"]
                )

        Args:
            order_id: str
            key includedData: [str] | str

        Returns:
            ApiResponse:


        """

        normalize_csv_param(kwargs, "includedData")
        return self._request(
            fill_query_params(kwargs.pop("path"), order_id),
            params={**kwargs},
            add_marketplace=False,
        )
