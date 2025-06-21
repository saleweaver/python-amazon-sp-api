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
from sp_api.api.models.orders.orders_v0 import *
from sp_api.base import ApiResponse, Client, fill_query_params, sp_endpoint

T = TypeVar("T")


class Orders_V_v0(Client):
    """
    Selling Partner API for Orders - v0

    Use the Orders Selling Partner API to programmatically retrieve order information. With this API, you can develop fast, flexible, and custom applications to manage order synchronization, perform order research, and create demand-based decision support tools.
    _Note:_ For the JP, AU, and SG marketplaces, the Orders API supports orders from 2016 onward. For all other marketplaces, the Orders API supports orders for the last two years (orders older than this don't show up in the response).
    """

    @overload
    def get_orders(
        self, request: GetOrdersRequest, *args, **kwargs
    ) -> ApiResponse[GetOrdersResponse]:
        """
        Returns orders that are created or updated during the specified time period. If you want to return specific types of orders, you can apply filters to your request. `NextToken` doesn't affect any filters that you include in your request; it only impacts the pagination for the filtered orders response.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                       0.0167 |      20 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that are applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may receive higher rate and burst values then those shown here. For more information, refer to [Usage Plans and Rate Limits](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api) in the Selling Partner API documentation.
        """
        ...

    @sp_endpoint("/orders/v0/orders", method="GET")
    def get_orders(self, *args, **kwargs) -> ApiResponse[GetOrdersResponse]:
        """
        Returns orders that are created or updated during the specified time period. If you want to return specific types of orders, you can apply filters to your request. `NextToken` doesn't affect any filters that you include in your request; it only impacts the pagination for the filtered orders response.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                       0.0167 |      20 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that are applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may receive higher rate and burst values then those shown here. For more information, refer to [Usage Plans and Rate Limits](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api) in the Selling Partner API documentation.
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, GetOrdersRequest):
            request = GetOrdersRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path, query=query, body=body, method=method, _type=GetOrdersResponse
        )

    @overload
    def get_order(
        self, request: GetOrderRequest, *args, **kwargs
    ) -> ApiResponse[GetOrderResponse]:
        """
        Returns the order that you specify.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                          0.5 |      30 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may receive higher rate and burst values then those shown here. For more information, refer to [Usage Plans and Rate Limits](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        ...

    @sp_endpoint("/orders/v0/orders/{orderId}", method="GET")
    def get_order(self, *args, **kwargs) -> ApiResponse[GetOrderResponse]:
        """
        Returns the order that you specify.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                          0.5 |      30 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may receive higher rate and burst values then those shown here. For more information, refer to [Usage Plans and Rate Limits](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, GetOrderRequest):
            request = GetOrderRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path, query=query, body=body, method=method, _type=GetOrderResponse
        )

    @overload
    def get_order_buyer_info(
        self, request: GetOrderBuyerInfoRequest, *args, **kwargs
    ) -> ApiResponse[GetOrderBuyerInfoResponse]:
        """
        Returns buyer information for the order that you specify.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                          0.5 |      30 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may receive higher rate and burst values then those shown here. For more information, refer to [Usage Plans and Rate Limits](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        ...

    @sp_endpoint("/orders/v0/orders/{orderId}/buyerInfo", method="GET")
    def get_order_buyer_info(
        self, *args, **kwargs
    ) -> ApiResponse[GetOrderBuyerInfoResponse]:
        """
        Returns buyer information for the order that you specify.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                          0.5 |      30 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may receive higher rate and burst values then those shown here. For more information, refer to [Usage Plans and Rate Limits](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, GetOrderBuyerInfoRequest):
            request = GetOrderBuyerInfoRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path, query=query, body=body, method=method, _type=GetOrderBuyerInfoResponse
        )

    @overload
    def get_order_address(
        self, request: GetOrderAddressRequest, *args, **kwargs
    ) -> ApiResponse[GetOrderAddressResponse]:
        """
        Returns the shipping address for the order that you specify.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                          0.5 |      30 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may receive higher rate and burst values then those shown here. For more information, refer to [Usage Plans and Rate Limits](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        ...

    @sp_endpoint("/orders/v0/orders/{orderId}/address", method="GET")
    def get_order_address(
        self, *args, **kwargs
    ) -> ApiResponse[GetOrderAddressResponse]:
        """
        Returns the shipping address for the order that you specify.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                          0.5 |      30 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may receive higher rate and burst values then those shown here. For more information, refer to [Usage Plans and Rate Limits](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, GetOrderAddressRequest):
            request = GetOrderAddressRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path, query=query, body=body, method=method, _type=GetOrderAddressResponse
        )

    @overload
    def get_order_items(
        self, request: GetOrderItemsRequest, *args, **kwargs
    ) -> ApiResponse[GetOrderItemsResponse]:
        """
        Returns detailed order item information for the order that you specify. If `NextToken` is provided, it's used to retrieve the next page of order items.

        __Note__: When an order is in the Pending state (the order has been placed but payment has not been authorized), the getOrderItems operation does not return information about pricing, taxes, shipping charges, gift status or promotions for the order items in the order. After an order leaves the Pending state (this occurs when payment has been authorized) and enters the Unshipped, Partially Shipped, or Shipped state, the getOrderItems operation returns information about pricing, taxes, shipping charges, gift status and promotions for the order items in the order.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                          0.5 |      30 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may receive higher rate and burst values then those shown here. For more information, refer to [Usage Plans and Rate Limits](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        ...

    @sp_endpoint("/orders/v0/orders/{orderId}/orderItems", method="GET")
    def get_order_items(self, *args, **kwargs) -> ApiResponse[GetOrderItemsResponse]:
        """
        Returns detailed order item information for the order that you specify. If `NextToken` is provided, it's used to retrieve the next page of order items.

        __Note__: When an order is in the Pending state (the order has been placed but payment has not been authorized), the getOrderItems operation does not return information about pricing, taxes, shipping charges, gift status or promotions for the order items in the order. After an order leaves the Pending state (this occurs when payment has been authorized) and enters the Unshipped, Partially Shipped, or Shipped state, the getOrderItems operation returns information about pricing, taxes, shipping charges, gift status and promotions for the order items in the order.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                          0.5 |      30 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may receive higher rate and burst values then those shown here. For more information, refer to [Usage Plans and Rate Limits](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, GetOrderItemsRequest):
            request = GetOrderItemsRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path, query=query, body=body, method=method, _type=GetOrderItemsResponse
        )

    @overload
    def get_order_items_buyer_info(
        self, request: GetOrderItemsBuyerInfoRequest, *args, **kwargs
    ) -> ApiResponse[GetOrderItemsBuyerInfoResponse]:
        """
        Returns buyer information for the order items in the order that you specify.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                          0.5 |      30 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may receive higher rate and burst values then those shown here. For more information, refer to [Usage Plans and Rate Limits](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        ...

    @sp_endpoint("/orders/v0/orders/{orderId}/orderItems/buyerInfo", method="GET")
    def get_order_items_buyer_info(
        self, *args, **kwargs
    ) -> ApiResponse[GetOrderItemsBuyerInfoResponse]:
        """
        Returns buyer information for the order items in the order that you specify.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                          0.5 |      30 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may receive higher rate and burst values then those shown here. For more information, refer to [Usage Plans and Rate Limits](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, GetOrderItemsBuyerInfoRequest):
            request = GetOrderItemsBuyerInfoRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path,
            query=query,
            body=body,
            method=method,
            _type=GetOrderItemsBuyerInfoResponse,
        )

    @overload
    def update_shipment_status(
        self, request: UpdateShipmentStatusRequest, *args, **kwargs
    ) -> ApiResponse[UpdateShipmentStatusErrorResponse]:
        """
        Update the shipment status for an order that you specify.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            5 |      15 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may receive higher rate and burst values then those shown here. For more information, refer to [Usage Plans and Rate Limits](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        ...

    @sp_endpoint("/orders/v0/orders/{orderId}/shipment", method="POST")
    def update_shipment_status(
        self, *args, **kwargs
    ) -> ApiResponse[UpdateShipmentStatusErrorResponse]:
        """
        Update the shipment status for an order that you specify.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            5 |      15 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may receive higher rate and burst values then those shown here. For more information, refer to [Usage Plans and Rate Limits](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, UpdateShipmentStatusRequest):
            request = UpdateShipmentStatusRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path,
            query=query,
            body=body,
            method=method,
            _type=UpdateShipmentStatusErrorResponse,
        )

    @overload
    def get_order_regulated_info(
        self, request: GetOrderRegulatedInfoRequest, *args, **kwargs
    ) -> ApiResponse[GetOrderRegulatedInfoResponse]:
        """
        Returns regulated information for the order that you specify.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                          0.5 |      30 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may receive higher rate and burst values then those shown here. For more information, refer to [Usage Plans and Rate Limits](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        ...

    @sp_endpoint("/orders/v0/orders/{orderId}/regulatedInfo", method="GET")
    def get_order_regulated_info(
        self, *args, **kwargs
    ) -> ApiResponse[GetOrderRegulatedInfoResponse]:
        """
        Returns regulated information for the order that you specify.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                          0.5 |      30 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may receive higher rate and burst values then those shown here. For more information, refer to [Usage Plans and Rate Limits](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, GetOrderRegulatedInfoRequest):
            request = GetOrderRegulatedInfoRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path,
            query=query,
            body=body,
            method=method,
            _type=GetOrderRegulatedInfoResponse,
        )

    @overload
    def update_verification_status(
        self, request: UpdateVerificationStatusRequest, *args, **kwargs
    ) -> ApiResponse[UpdateVerificationStatusErrorResponse]:
        """
        Updates (approves or rejects) the verification status of an order containing regulated products.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                          0.5 |      30 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may receive higher rate and burst values then those shown here. For more information, refer to [Usage Plans and Rate Limits](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        ...

    @sp_endpoint("/orders/v0/orders/{orderId}/regulatedInfo", method="PATCH")
    def update_verification_status(
        self, *args, **kwargs
    ) -> ApiResponse[UpdateVerificationStatusErrorResponse]:
        """
        Updates (approves or rejects) the verification status of an order containing regulated products.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                          0.5 |      30 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may receive higher rate and burst values then those shown here. For more information, refer to [Usage Plans and Rate Limits](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, UpdateVerificationStatusRequest):
            request = UpdateVerificationStatusRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path,
            query=query,
            body=body,
            method=method,
            _type=UpdateVerificationStatusErrorResponse,
        )

    @overload
    def confirm_shipment(
        self, request: ConfirmShipmentRequest, *args, **kwargs
    ) -> ApiResponse[ConfirmShipmentErrorResponse]:
        """
        Updates the shipment confirmation status for a specified order.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            2 |      10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may receive higher rate and burst values then those shown here. For more information, refer to [Usage Plans and Rate Limits](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        ...

    @sp_endpoint("/orders/v0/orders/{orderId}/shipmentConfirmation", method="POST")
    def confirm_shipment(
        self, *args, **kwargs
    ) -> ApiResponse[ConfirmShipmentErrorResponse]:
        """
        Updates the shipment confirmation status for a specified order.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            2 |      10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may receive higher rate and burst values then those shown here. For more information, refer to [Usage Plans and Rate Limits](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, ConfirmShipmentRequest):
            request = ConfirmShipmentRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path,
            query=query,
            body=body,
            method=method,
            _type=ConfirmShipmentErrorResponse,
        )
