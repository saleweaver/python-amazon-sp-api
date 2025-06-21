"""
Generated API client from Swagger/OpenAPI specification.
This file was auto-generated. Do not edit manually.
"""

import json
from typing import (Any, Dict, Generic, List, Optional, TypeVar, Union, cast,
                    overload)

import httpx
from pydantic import BaseModel
# Import all models
from sp_api.api.models.vendor_orders.vendor_orders_v1 import *
from sp_api.base import ApiResponse, Client, fill_query_params, sp_endpoint

T = TypeVar("T")


class VendorOrders_V_v1(Client):
    """
    Selling Partner API for Retail Procurement Orders - v1

    The Selling Partner API for Retail Procurement Orders provides programmatic access to vendor orders data.
    """

    @overload
    def get_purchase_orders(
        self, request: GetPurchaseOrdersRequest, *args, **kwargs
    ) -> ApiResponse[GetPurchaseOrdersResponse]:
        """
        Returns a list of purchase orders created or changed during the time frame that you specify. You define the time frame using the `createdAfter`, `createdBefore`, `changedAfter` and `changedBefore` parameters. The date range to search must not be more than 7 days. You can choose to get only the purchase order numbers by setting `includeDetails` to false. You can then use the `getPurchaseOrder` operation to receive details for a specific purchase order.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                           10 |      10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        ...

    @sp_endpoint("/vendor/orders/v1/purchaseOrders", method="GET")
    def get_purchase_orders(
        self, *args, **kwargs
    ) -> ApiResponse[GetPurchaseOrdersResponse]:
        """
        Returns a list of purchase orders created or changed during the time frame that you specify. You define the time frame using the `createdAfter`, `createdBefore`, `changedAfter` and `changedBefore` parameters. The date range to search must not be more than 7 days. You can choose to get only the purchase order numbers by setting `includeDetails` to false. You can then use the `getPurchaseOrder` operation to receive details for a specific purchase order.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                           10 |      10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, GetPurchaseOrdersRequest):
            request = GetPurchaseOrdersRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path, query=query, body=body, method=method, _type=GetPurchaseOrdersResponse
        )

    @overload
    def get_purchase_order(
        self, request: GetPurchaseOrderRequest, *args, **kwargs
    ) -> ApiResponse[GetPurchaseOrderResponse]:
        """
        Returns a purchase order based on the `purchaseOrderNumber` value that you specify.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                           10 |      10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        ...

    @sp_endpoint("/vendor/orders/v1/purchaseOrders/{purchaseOrderNumber}", method="GET")
    def get_purchase_order(
        self, *args, **kwargs
    ) -> ApiResponse[GetPurchaseOrderResponse]:
        """
        Returns a purchase order based on the `purchaseOrderNumber` value that you specify.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                           10 |      10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, GetPurchaseOrderRequest):
            request = GetPurchaseOrderRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path, query=query, body=body, method=method, _type=GetPurchaseOrderResponse
        )

    @overload
    def submit_acknowledgement(
        self, request: SubmitAcknowledgementRequest, *args, **kwargs
    ) -> ApiResponse[SubmitAcknowledgementResponse]:
        """
        Submits acknowledgements for one or more purchase orders.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                           10 |      10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        ...

    @sp_endpoint("/vendor/orders/v1/acknowledgements", method="POST")
    def submit_acknowledgement(
        self, *args, **kwargs
    ) -> ApiResponse[SubmitAcknowledgementResponse]:
        """
        Submits acknowledgements for one or more purchase orders.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                           10 |      10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, SubmitAcknowledgementRequest):
            request = SubmitAcknowledgementRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path,
            query=query,
            body=body,
            method=method,
            _type=SubmitAcknowledgementResponse,
        )

    @overload
    def get_purchase_orders_status(
        self, request: GetPurchaseOrdersStatusRequest, *args, **kwargs
    ) -> ApiResponse[GetPurchaseOrdersStatusResponse]:
        """
        Returns purchase order statuses based on the filters that you specify. Date range to search must not be more than 7 days. You can return a list of purchase order statuses using the available filters, or a single purchase order status by providing the purchase order number.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                           10 |      10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        ...

    @sp_endpoint("/vendor/orders/v1/purchaseOrdersStatus", method="GET")
    def get_purchase_orders_status(
        self, *args, **kwargs
    ) -> ApiResponse[GetPurchaseOrdersStatusResponse]:
        """
        Returns purchase order statuses based on the filters that you specify. Date range to search must not be more than 7 days. You can return a list of purchase order statuses using the available filters, or a single purchase order status by providing the purchase order number.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                           10 |      10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, GetPurchaseOrdersStatusRequest):
            request = GetPurchaseOrdersStatusRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path,
            query=query,
            body=body,
            method=method,
            _type=GetPurchaseOrdersStatusResponse,
        )
