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
from sp_api.api.models.shipping.shipping_v1 import *
from sp_api.base import ApiResponse, Client, fill_query_params, sp_endpoint

T = TypeVar("T")


class Shipping_V_v1(Client):
    """
    Selling Partner API for Shipping - v1

    Provides programmatic access to Amazon Shipping APIs.
    **Note:** If you are new to the Amazon Shipping API, refer to the latest version of <a href='https://developer-docs.amazon.com/amazon-shipping/docs/shipping-api-v2-reference'>Amazon Shipping API (v2)</a> on the <a href='https://developer-docs.amazon.com/amazon-shipping/'>Amazon Shipping Developer Documentation</a> site.
    """

    @overload
    def create_shipment(
        self, request: CreateShipmentRequest, *args, **kwargs
    ) -> ApiResponse[CreateShipmentResponse]:
        """
        Create a new shipment.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            5 |      15 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        ...

    @sp_endpoint("/shipping/v1/shipments", method="POST")
    def create_shipment(self, *args, **kwargs) -> ApiResponse[CreateShipmentResponse]:
        """
        Create a new shipment.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            5 |      15 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, CreateShipmentRequest):
            request = CreateShipmentRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path, query=query, body=body, method=method, _type=CreateShipmentResponse
        )

    @overload
    def get_shipment(
        self, request: GetShipmentRequest, *args, **kwargs
    ) -> ApiResponse[GetShipmentResponse]:
        """
        Return the entire shipment object for the shipmentId.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            5 |      15 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        ...

    @sp_endpoint("/shipping/v1/shipments/{shipmentId}", method="GET")
    def get_shipment(self, *args, **kwargs) -> ApiResponse[GetShipmentResponse]:
        """
        Return the entire shipment object for the shipmentId.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            5 |      15 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, GetShipmentRequest):
            request = GetShipmentRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path, query=query, body=body, method=method, _type=GetShipmentResponse
        )

    @overload
    def cancel_shipment(
        self, request: CancelShipmentRequest, *args, **kwargs
    ) -> ApiResponse[CancelShipmentResponse]:
        """
        Cancel a shipment by the given shipmentId.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            5 |      15 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        ...

    @sp_endpoint("/shipping/v1/shipments/{shipmentId}/cancel", method="POST")
    def cancel_shipment(self, *args, **kwargs) -> ApiResponse[CancelShipmentResponse]:
        """
        Cancel a shipment by the given shipmentId.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            5 |      15 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, CancelShipmentRequest):
            request = CancelShipmentRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path, query=query, body=body, method=method, _type=CancelShipmentResponse
        )

    @overload
    def purchase_labels(
        self, request: PurchaseLabelsRequest, *args, **kwargs
    ) -> ApiResponse[PurchaseLabelsResponse]:
        """
        Purchase shipping labels based on a given rate.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            5 |      15 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        ...

    @sp_endpoint("/shipping/v1/shipments/{shipmentId}/purchaseLabels", method="POST")
    def purchase_labels(self, *args, **kwargs) -> ApiResponse[PurchaseLabelsResponse]:
        """
        Purchase shipping labels based on a given rate.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            5 |      15 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, PurchaseLabelsRequest):
            request = PurchaseLabelsRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path, query=query, body=body, method=method, _type=PurchaseLabelsResponse
        )

    @overload
    def retrieve_shipping_label(
        self, request: RetrieveShippingLabelRequest, *args, **kwargs
    ) -> ApiResponse[RetrieveShippingLabelResponse]:
        """
        Retrieve shipping label based on the shipment id and tracking id.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            5 |      15 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        ...

    @sp_endpoint(
        "/shipping/v1/shipments/{shipmentId}/containers/{trackingId}/label",
        method="POST",
    )
    def retrieve_shipping_label(
        self, *args, **kwargs
    ) -> ApiResponse[RetrieveShippingLabelResponse]:
        """
        Retrieve shipping label based on the shipment id and tracking id.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            5 |      15 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, RetrieveShippingLabelRequest):
            request = RetrieveShippingLabelRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path,
            query=query,
            body=body,
            method=method,
            _type=RetrieveShippingLabelResponse,
        )

    @overload
    def purchase_shipment(
        self, request: PurchaseShipmentRequest, *args, **kwargs
    ) -> ApiResponse[PurchaseShipmentResponse]:
        """
        Purchase shipping labels.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            5 |      15 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        ...

    @sp_endpoint("/shipping/v1/purchaseShipment", method="POST")
    def purchase_shipment(
        self, *args, **kwargs
    ) -> ApiResponse[PurchaseShipmentResponse]:
        """
        Purchase shipping labels.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            5 |      15 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, PurchaseShipmentRequest):
            request = PurchaseShipmentRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path, query=query, body=body, method=method, _type=PurchaseShipmentResponse
        )

    @overload
    def get_rates(
        self, request: GetRatesRequest, *args, **kwargs
    ) -> ApiResponse[GetRatesResponse]:
        """
        Get service rates.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            5 |      15 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        ...

    @sp_endpoint("/shipping/v1/rates", method="POST")
    def get_rates(self, *args, **kwargs) -> ApiResponse[GetRatesResponse]:
        """
        Get service rates.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            5 |      15 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, GetRatesRequest):
            request = GetRatesRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path, query=query, body=body, method=method, _type=GetRatesResponse
        )

    @overload
    def get_account(
        self, request: None, *args, **kwargs
    ) -> ApiResponse[GetAccountResponse]:
        """
        Verify if the current account is valid.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            5 |      15 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        ...

    @sp_endpoint("/shipping/v1/account", method="GET")
    def get_account(self, *args, **kwargs) -> ApiResponse[GetAccountResponse]:
        """
        Verify if the current account is valid.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            5 |      15 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, None):
            request = None(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path, query=query, body=body, method=method, _type=GetAccountResponse
        )

    @overload
    def get_tracking_information(
        self, request: GetTrackingInformationRequest, *args, **kwargs
    ) -> ApiResponse[GetTrackingInformationResponse]:
        """
        Return the tracking information of a shipment.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            1 |       1 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        ...

    @sp_endpoint("/shipping/v1/tracking/{trackingId}", method="GET")
    def get_tracking_information(
        self, *args, **kwargs
    ) -> ApiResponse[GetTrackingInformationResponse]:
        """
        Return the tracking information of a shipment.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            1 |       1 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, GetTrackingInformationRequest):
            request = GetTrackingInformationRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path,
            query=query,
            body=body,
            method=method,
            _type=GetTrackingInformationResponse,
        )
