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
from sp_api.api.models.vendor_direct_fulfillment_shipping.vendor_direct_fulfillment_shipping_v1 import *
from sp_api.base import ApiResponse, Client, fill_query_params, sp_endpoint

T = TypeVar("T")


class VendorDirectFulfillmentShipping_V_v1(Client):
    """
    Selling Partner API for Direct Fulfillment Shipping - v1

    The Selling Partner API for Direct Fulfillment Shipping provides programmatic access to a direct fulfillment vendor's shipping data.
    """

    @overload
    def get_shipping_labels(
        self, request: GetShippingLabelsRequest, *args, **kwargs
    ) -> ApiResponse[GetShippingLabelListResponse]:
        """
        Returns a list of shipping labels created during the time frame that you specify. You define that time frame using the createdAfter and createdBefore parameters. You must use both of these parameters. The date range to search must not be more than 7 days.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                           10 |      10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        ...

    @sp_endpoint("/vendor/directFulfillment/shipping/v1/shippingLabels", method="GET")
    def get_shipping_labels(
        self, *args, **kwargs
    ) -> ApiResponse[GetShippingLabelListResponse]:
        """
        Returns a list of shipping labels created during the time frame that you specify. You define that time frame using the createdAfter and createdBefore parameters. You must use both of these parameters. The date range to search must not be more than 7 days.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                           10 |      10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, GetShippingLabelsRequest):
            request = GetShippingLabelsRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path,
            query=query,
            body=body,
            method=method,
            _type=GetShippingLabelListResponse,
        )

    @overload
    def submit_shipping_label_request_body(
        self, request: SubmitShippingLabelRequestBodyRequest, *args, **kwargs
    ) -> ApiResponse[SubmitShippingLabelsResponse]:
        """
        Creates a shipping label for a purchase order and returns a transactionId for reference.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                           10 |      10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        ...

    @sp_endpoint("/vendor/directFulfillment/shipping/v1/shippingLabels", method="POST")
    def submit_shipping_label_request_body(
        self, *args, **kwargs
    ) -> ApiResponse[SubmitShippingLabelsResponse]:
        """
        Creates a shipping label for a purchase order and returns a transactionId for reference.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                           10 |      10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, SubmitShippingLabelRequestBodyRequest):
            request = SubmitShippingLabelRequestBodyRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path,
            query=query,
            body=body,
            method=method,
            _type=SubmitShippingLabelsResponse,
        )

    @overload
    def get_shipping_label(
        self, request: GetShippingLabelRequest, *args, **kwargs
    ) -> ApiResponse[GetShippingLabelResponse]:
        """
        Returns a shipping label for the purchaseOrderNumber that you specify.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                           10 |      10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        ...

    @sp_endpoint(
        "/vendor/directFulfillment/shipping/v1/shippingLabels/{purchaseOrderNumber}",
        method="GET",
    )
    def get_shipping_label(
        self, *args, **kwargs
    ) -> ApiResponse[GetShippingLabelResponse]:
        """
        Returns a shipping label for the purchaseOrderNumber that you specify.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                           10 |      10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, GetShippingLabelRequest):
            request = GetShippingLabelRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path, query=query, body=body, method=method, _type=GetShippingLabelResponse
        )

    @overload
    def submit_shipment_confirmations(
        self, request: SubmitShipmentConfirmationsRequest, *args, **kwargs
    ) -> ApiResponse[SubmitShipmentConfirmationsResponse]:
        """
        Submits one or more shipment confirmations for vendor orders.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                           10 |      10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        ...

    @sp_endpoint(
        "/vendor/directFulfillment/shipping/v1/shipmentConfirmations", method="POST"
    )
    def submit_shipment_confirmations(
        self, *args, **kwargs
    ) -> ApiResponse[SubmitShipmentConfirmationsResponse]:
        """
        Submits one or more shipment confirmations for vendor orders.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                           10 |      10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, SubmitShipmentConfirmationsRequest):
            request = SubmitShipmentConfirmationsRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path,
            query=query,
            body=body,
            method=method,
            _type=SubmitShipmentConfirmationsResponse,
        )

    @overload
    def submit_shipment_status_updates(
        self, request: SubmitShipmentStatusUpdatesRequest, *args, **kwargs
    ) -> ApiResponse[SubmitShipmentStatusUpdatesResponse]:
        """
        This API call is only to be used by Vendor-Own-Carrier (VOC) vendors. Calling this API will submit a shipment status update for the package that a vendor has shipped. It will provide the Amazon customer visibility on their order, when the package is outside of Amazon Network visibility.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                           10 |      10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        ...

    @sp_endpoint(
        "/vendor/directFulfillment/shipping/v1/shipmentStatusUpdates", method="POST"
    )
    def submit_shipment_status_updates(
        self, *args, **kwargs
    ) -> ApiResponse[SubmitShipmentStatusUpdatesResponse]:
        """
        This API call is only to be used by Vendor-Own-Carrier (VOC) vendors. Calling this API will submit a shipment status update for the package that a vendor has shipped. It will provide the Amazon customer visibility on their order, when the package is outside of Amazon Network visibility.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                           10 |      10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, SubmitShipmentStatusUpdatesRequest):
            request = SubmitShipmentStatusUpdatesRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path,
            query=query,
            body=body,
            method=method,
            _type=SubmitShipmentStatusUpdatesResponse,
        )

    @overload
    def get_customer_invoices(
        self, request: GetCustomerInvoicesRequest, *args, **kwargs
    ) -> ApiResponse[GetCustomerInvoicesResponse]:
        """
        Returns a list of customer invoices created during a time frame that you specify. You define the  time frame using the createdAfter and createdBefore parameters. You must use both of these parameters. The date range to search must be no more than 7 days.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                           10 |      10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        ...

    @sp_endpoint("/vendor/directFulfillment/shipping/v1/customerInvoices", method="GET")
    def get_customer_invoices(
        self, *args, **kwargs
    ) -> ApiResponse[GetCustomerInvoicesResponse]:
        """
        Returns a list of customer invoices created during a time frame that you specify. You define the  time frame using the createdAfter and createdBefore parameters. You must use both of these parameters. The date range to search must be no more than 7 days.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                           10 |      10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, GetCustomerInvoicesRequest):
            request = GetCustomerInvoicesRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path,
            query=query,
            body=body,
            method=method,
            _type=GetCustomerInvoicesResponse,
        )

    @overload
    def get_customer_invoice(
        self, request: GetCustomerInvoiceRequest, *args, **kwargs
    ) -> ApiResponse[GetCustomerInvoiceResponse]:
        """
        Returns a customer invoice based on the purchaseOrderNumber that you specify.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                           10 |      10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        ...

    @sp_endpoint(
        "/vendor/directFulfillment/shipping/v1/customerInvoices/{purchaseOrderNumber}",
        method="GET",
    )
    def get_customer_invoice(
        self, *args, **kwargs
    ) -> ApiResponse[GetCustomerInvoiceResponse]:
        """
        Returns a customer invoice based on the purchaseOrderNumber that you specify.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                           10 |      10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, GetCustomerInvoiceRequest):
            request = GetCustomerInvoiceRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path,
            query=query,
            body=body,
            method=method,
            _type=GetCustomerInvoiceResponse,
        )

    @overload
    def get_packing_slips(
        self, request: GetPackingSlipsRequest, *args, **kwargs
    ) -> ApiResponse[GetPackingSlipListResponse]:
        """
        Returns a list of packing slips for the purchase orders that match the criteria specified. Date range to search must not be more than 7 days.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                           10 |      10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        ...

    @sp_endpoint("/vendor/directFulfillment/shipping/v1/packingSlips", method="GET")
    def get_packing_slips(
        self, *args, **kwargs
    ) -> ApiResponse[GetPackingSlipListResponse]:
        """
        Returns a list of packing slips for the purchase orders that match the criteria specified. Date range to search must not be more than 7 days.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                           10 |      10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, GetPackingSlipsRequest):
            request = GetPackingSlipsRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path,
            query=query,
            body=body,
            method=method,
            _type=GetPackingSlipListResponse,
        )

    @overload
    def get_packing_slip(
        self, request: GetPackingSlipRequest, *args, **kwargs
    ) -> ApiResponse[GetPackingSlipResponse]:
        """
        Returns a packing slip based on the purchaseOrderNumber that you specify.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                           10 |      10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        ...

    @sp_endpoint(
        "/vendor/directFulfillment/shipping/v1/packingSlips/{purchaseOrderNumber}",
        method="GET",
    )
    def get_packing_slip(self, *args, **kwargs) -> ApiResponse[GetPackingSlipResponse]:
        """
        Returns a packing slip based on the purchaseOrderNumber that you specify.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                           10 |      10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, GetPackingSlipRequest):
            request = GetPackingSlipRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path, query=query, body=body, method=method, _type=GetPackingSlipResponse
        )
