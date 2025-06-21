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
from sp_api.api.models.fulfillment_outbound.fulfillment_outbound_2020_07_01 import *
from sp_api.base import ApiResponse, Client, fill_query_params, sp_endpoint

T = TypeVar("T")


class FulfillmentOutbound_V_2020_07_01(Client):
    """
    Selling Partner APIs for Fulfillment Outbound - 2020-07-01

    The Selling Partner API for Fulfillment Outbound lets you create applications that help a seller fulfill Multi-Channel Fulfillment orders using their inventory in Amazon's fulfillment network. You can get information on both potential and existing fulfillment orders.
    """

    @overload
    def get_fulfillment_preview(
        self, request: GetFulfillmentPreviewRequest, *args, **kwargs
    ) -> ApiResponse[GetFulfillmentPreviewResponse]:
        """
        Returns a list of fulfillment order previews based on shipping criteria that you specify.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            2 |      30 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        ...

    @sp_endpoint("/fba/outbound/2020-07-01/fulfillmentOrders/preview", method="POST")
    def get_fulfillment_preview(
        self, *args, **kwargs
    ) -> ApiResponse[GetFulfillmentPreviewResponse]:
        """
        Returns a list of fulfillment order previews based on shipping criteria that you specify.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            2 |      30 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, GetFulfillmentPreviewRequest):
            request = GetFulfillmentPreviewRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path,
            query=query,
            body=body,
            method=method,
            _type=GetFulfillmentPreviewResponse,
        )

    @overload
    def delivery_offers(
        self, request: DeliveryOffersRequest, *args, **kwargs
    ) -> ApiResponse[GetDeliveryOffersResponse]:
        """
        Returns delivery options that include an estimated delivery date and offer expiration, based on criteria that you specify.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            5 |      30 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        ...

    @sp_endpoint("/fba/outbound/2020-07-01/deliveryOffers", method="POST")
    def delivery_offers(
        self, *args, **kwargs
    ) -> ApiResponse[GetDeliveryOffersResponse]:
        """
        Returns delivery options that include an estimated delivery date and offer expiration, based on criteria that you specify.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            5 |      30 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, DeliveryOffersRequest):
            request = DeliveryOffersRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path, query=query, body=body, method=method, _type=GetDeliveryOffersResponse
        )

    @overload
    def list_all_fulfillment_orders(
        self, request: ListAllFulfillmentOrdersRequest, *args, **kwargs
    ) -> ApiResponse[ListAllFulfillmentOrdersResponse]:
        """
        Returns a list of fulfillment orders fulfilled after (or at) a specified date-time, or indicated by the next token parameter.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            2 |      30 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api)
        """
        ...

    @sp_endpoint("/fba/outbound/2020-07-01/fulfillmentOrders", method="GET")
    def list_all_fulfillment_orders(
        self, *args, **kwargs
    ) -> ApiResponse[ListAllFulfillmentOrdersResponse]:
        """
        Returns a list of fulfillment orders fulfilled after (or at) a specified date-time, or indicated by the next token parameter.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            2 |      30 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api)
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, ListAllFulfillmentOrdersRequest):
            request = ListAllFulfillmentOrdersRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path,
            query=query,
            body=body,
            method=method,
            _type=ListAllFulfillmentOrdersResponse,
        )

    @overload
    def create_fulfillment_order(
        self, request: CreateFulfillmentOrderRequest, *args, **kwargs
    ) -> ApiResponse[CreateFulfillmentOrderResponse]:
        """
        Requests that Amazon ship items from the seller's inventory in Amazon's fulfillment network to a destination address.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            2 |      30 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api)
        """
        ...

    @sp_endpoint("/fba/outbound/2020-07-01/fulfillmentOrders", method="POST")
    def create_fulfillment_order(
        self, *args, **kwargs
    ) -> ApiResponse[CreateFulfillmentOrderResponse]:
        """
        Requests that Amazon ship items from the seller's inventory in Amazon's fulfillment network to a destination address.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            2 |      30 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api)
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, CreateFulfillmentOrderRequest):
            request = CreateFulfillmentOrderRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path,
            query=query,
            body=body,
            method=method,
            _type=CreateFulfillmentOrderResponse,
        )

    @overload
    def get_package_tracking_details(
        self, request: GetPackageTrackingDetailsRequest, *args, **kwargs
    ) -> ApiResponse[GetPackageTrackingDetailsResponse]:
        """
        Returns delivery tracking information for a package in an outbound shipment for a Multi-Channel Fulfillment order.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            2 |      30 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        ...

    @sp_endpoint("/fba/outbound/2020-07-01/tracking", method="GET")
    def get_package_tracking_details(
        self, *args, **kwargs
    ) -> ApiResponse[GetPackageTrackingDetailsResponse]:
        """
        Returns delivery tracking information for a package in an outbound shipment for a Multi-Channel Fulfillment order.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            2 |      30 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, GetPackageTrackingDetailsRequest):
            request = GetPackageTrackingDetailsRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path,
            query=query,
            body=body,
            method=method,
            _type=GetPackageTrackingDetailsResponse,
        )

    @overload
    def list_return_reason_codes(
        self, request: ListReturnReasonCodesRequest, *args, **kwargs
    ) -> ApiResponse[ListReturnReasonCodesResponse]:
        """
        Returns a list of return reason codes for a seller SKU in a given marketplace. The parameters for this operation may contain special characters that require URL encoding. To avoid errors with SKUs when encoding URLs, refer to [URL Encoding](https://developer-docs.amazon.com/sp-api/docs/url-encoding).

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            2 |      30 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        ...

    @sp_endpoint("/fba/outbound/2020-07-01/returnReasonCodes", method="GET")
    def list_return_reason_codes(
        self, *args, **kwargs
    ) -> ApiResponse[ListReturnReasonCodesResponse]:
        """
        Returns a list of return reason codes for a seller SKU in a given marketplace. The parameters for this operation may contain special characters that require URL encoding. To avoid errors with SKUs when encoding URLs, refer to [URL Encoding](https://developer-docs.amazon.com/sp-api/docs/url-encoding).

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            2 |      30 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, ListReturnReasonCodesRequest):
            request = ListReturnReasonCodesRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path,
            query=query,
            body=body,
            method=method,
            _type=ListReturnReasonCodesResponse,
        )

    @overload
    def create_fulfillment_return(
        self, request: CreateFulfillmentReturnRequest, *args, **kwargs
    ) -> ApiResponse[CreateFulfillmentReturnResponse]:
        """
        Creates a fulfillment return.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            2 |      30 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        ...

    @sp_endpoint(
        "/fba/outbound/2020-07-01/fulfillmentOrders/{sellerFulfillmentOrderId}/return",
        method="PUT",
    )
    def create_fulfillment_return(
        self, *args, **kwargs
    ) -> ApiResponse[CreateFulfillmentReturnResponse]:
        """
        Creates a fulfillment return.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            2 |      30 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, CreateFulfillmentReturnRequest):
            request = CreateFulfillmentReturnRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path,
            query=query,
            body=body,
            method=method,
            _type=CreateFulfillmentReturnResponse,
        )

    @overload
    def get_fulfillment_order(
        self, request: GetFulfillmentOrderRequest, *args, **kwargs
    ) -> ApiResponse[GetFulfillmentOrderResponse]:
        """
        Returns the fulfillment order indicated by the specified order identifier.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            2 |      30 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        ...

    @sp_endpoint(
        "/fba/outbound/2020-07-01/fulfillmentOrders/{sellerFulfillmentOrderId}",
        method="GET",
    )
    def get_fulfillment_order(
        self, *args, **kwargs
    ) -> ApiResponse[GetFulfillmentOrderResponse]:
        """
        Returns the fulfillment order indicated by the specified order identifier.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            2 |      30 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, GetFulfillmentOrderRequest):
            request = GetFulfillmentOrderRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path,
            query=query,
            body=body,
            method=method,
            _type=GetFulfillmentOrderResponse,
        )

    @overload
    def update_fulfillment_order(
        self, request: UpdateFulfillmentOrderRequest, *args, **kwargs
    ) -> ApiResponse[UpdateFulfillmentOrderResponse]:
        """
        Updates and/or requests shipment for a fulfillment order with an order hold on it.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            2 |      30 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        ...

    @sp_endpoint(
        "/fba/outbound/2020-07-01/fulfillmentOrders/{sellerFulfillmentOrderId}",
        method="PUT",
    )
    def update_fulfillment_order(
        self, *args, **kwargs
    ) -> ApiResponse[UpdateFulfillmentOrderResponse]:
        """
        Updates and/or requests shipment for a fulfillment order with an order hold on it.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            2 |      30 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, UpdateFulfillmentOrderRequest):
            request = UpdateFulfillmentOrderRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path,
            query=query,
            body=body,
            method=method,
            _type=UpdateFulfillmentOrderResponse,
        )

    @overload
    def cancel_fulfillment_order(
        self, request: CancelFulfillmentOrderRequest, *args, **kwargs
    ) -> ApiResponse[CancelFulfillmentOrderResponse]:
        """
        Requests that Amazon stop attempting to fulfill the fulfillment order indicated by the specified order identifier.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            2 |      30 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        ...

    @sp_endpoint(
        "/fba/outbound/2020-07-01/fulfillmentOrders/{sellerFulfillmentOrderId}/cancel",
        method="PUT",
    )
    def cancel_fulfillment_order(
        self, *args, **kwargs
    ) -> ApiResponse[CancelFulfillmentOrderResponse]:
        """
        Requests that Amazon stop attempting to fulfill the fulfillment order indicated by the specified order identifier.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            2 |      30 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, CancelFulfillmentOrderRequest):
            request = CancelFulfillmentOrderRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path,
            query=query,
            body=body,
            method=method,
            _type=CancelFulfillmentOrderResponse,
        )

    @overload
    def submit_fulfillment_order_status_update(
        self, request: SubmitFulfillmentOrderStatusUpdateRequest, *args, **kwargs
    ) -> ApiResponse[SubmitFulfillmentOrderStatusUpdateResponse]:
        """
        Requests that Amazon update the status of an order in the sandbox testing environment. This is a sandbox-only operation and must be directed to a sandbox endpoint. Refer to [Fulfillment Outbound Dynamic Sandbox Guide](https://developer-docs.amazon.com/sp-api/docs/fulfillment-outbound-dynamic-sandbox-guide) and [Selling Partner API sandbox](https://developer-docs.amazon.com/sp-api/docs/the-selling-partner-api-sandbox) for more information.
        """
        ...

    @sp_endpoint(
        "/fba/outbound/2020-07-01/fulfillmentOrders/{sellerFulfillmentOrderId}/status",
        method="PUT",
    )
    def submit_fulfillment_order_status_update(
        self, *args, **kwargs
    ) -> ApiResponse[SubmitFulfillmentOrderStatusUpdateResponse]:
        """
        Requests that Amazon update the status of an order in the sandbox testing environment. This is a sandbox-only operation and must be directed to a sandbox endpoint. Refer to [Fulfillment Outbound Dynamic Sandbox Guide](https://developer-docs.amazon.com/sp-api/docs/fulfillment-outbound-dynamic-sandbox-guide) and [Selling Partner API sandbox](https://developer-docs.amazon.com/sp-api/docs/the-selling-partner-api-sandbox) for more information.
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, SubmitFulfillmentOrderStatusUpdateRequest):
            request = SubmitFulfillmentOrderStatusUpdateRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path,
            query=query,
            body=body,
            method=method,
            _type=SubmitFulfillmentOrderStatusUpdateResponse,
        )

    @overload
    def get_features(
        self, request: GetFeaturesRequest, *args, **kwargs
    ) -> ApiResponse[GetFeaturesResponse]:
        """
        Returns a list of features available for Multi-Channel Fulfillment orders in the marketplace you specify, and whether the seller for which you made the call is enrolled for each feature.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            2 |      30 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        ...

    @sp_endpoint("/fba/outbound/2020-07-01/features", method="GET")
    def get_features(self, *args, **kwargs) -> ApiResponse[GetFeaturesResponse]:
        """
        Returns a list of features available for Multi-Channel Fulfillment orders in the marketplace you specify, and whether the seller for which you made the call is enrolled for each feature.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            2 |      30 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, GetFeaturesRequest):
            request = GetFeaturesRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path, query=query, body=body, method=method, _type=GetFeaturesResponse
        )

    @overload
    def get_feature_inventory(
        self, request: GetFeatureInventoryRequest, *args, **kwargs
    ) -> ApiResponse[GetFeatureInventoryResponse]:
        """
        Returns a list of inventory items that are eligible for the fulfillment feature you specify.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            2 |      30 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api)..
        """
        ...

    @sp_endpoint(
        "/fba/outbound/2020-07-01/features/inventory/{featureName}", method="GET"
    )
    def get_feature_inventory(
        self, *args, **kwargs
    ) -> ApiResponse[GetFeatureInventoryResponse]:
        """
        Returns a list of inventory items that are eligible for the fulfillment feature you specify.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            2 |      30 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api)..
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, GetFeatureInventoryRequest):
            request = GetFeatureInventoryRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path,
            query=query,
            body=body,
            method=method,
            _type=GetFeatureInventoryResponse,
        )

    @overload
    def get_feature_s_k_u(
        self, request: GetFeatureSKURequest, *args, **kwargs
    ) -> ApiResponse[GetFeatureSkuResponse]:
        """
        Returns the number of items with the sellerSKU you specify that can have orders fulfilled using the specified feature. Note that if the sellerSKU isn't eligible, the response will contain an empty skuInfo object. The parameters for this operation may contain special characters that require URL encoding. To avoid errors with SKUs when encoding URLs, refer to [URL Encoding](https://developer-docs.amazon.com/sp-api/docs/url-encoding).

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            2 |      30 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        ...

    @sp_endpoint(
        "/fba/outbound/2020-07-01/features/inventory/{featureName}/{sellerSku}",
        method="GET",
    )
    def get_feature_s_k_u(self, *args, **kwargs) -> ApiResponse[GetFeatureSkuResponse]:
        """
        Returns the number of items with the sellerSKU you specify that can have orders fulfilled using the specified feature. Note that if the sellerSKU isn't eligible, the response will contain an empty skuInfo object. The parameters for this operation may contain special characters that require URL encoding. To avoid errors with SKUs when encoding URLs, refer to [URL Encoding](https://developer-docs.amazon.com/sp-api/docs/url-encoding).

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            2 |      30 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, GetFeatureSKURequest):
            request = GetFeatureSKURequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path, query=query, body=body, method=method, _type=GetFeatureSkuResponse
        )
