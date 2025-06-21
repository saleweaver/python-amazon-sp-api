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
from sp_api.api.models.merchant_fulfillment.merchant_fulfillment_v0 import *
from sp_api.base import ApiResponse, Client, fill_query_params, sp_endpoint

T = TypeVar("T")


class MerchantFulfillment_V_v0(Client):
    """
    Selling Partner API for Merchant Fulfillment - v0

    With the Selling Partner API for Merchant Fulfillment, you can build applications that sellers can use to purchase shipping for non-Prime and Prime orders using Amazon's Buy Shipping Services.
    """

    @overload
    def get_eligible_shipment_services(
        self, request: GetEligibleShipmentServicesRequest, *args, **kwargs
    ) -> ApiResponse[GetEligibleShipmentServicesResponse]:
        """
        Returns a list of shipping service offers that satisfy the specified shipment request details.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            6 |      12 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that are applied to the requested operation when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the SP-API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        ...

    @sp_endpoint("/mfn/v0/eligibleShippingServices", method="POST")
    def get_eligible_shipment_services(
        self, *args, **kwargs
    ) -> ApiResponse[GetEligibleShipmentServicesResponse]:
        """
        Returns a list of shipping service offers that satisfy the specified shipment request details.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            6 |      12 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that are applied to the requested operation when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the SP-API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, GetEligibleShipmentServicesRequest):
            request = GetEligibleShipmentServicesRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path,
            query=query,
            body=body,
            method=method,
            _type=GetEligibleShipmentServicesResponse,
        )

    @overload
    def get_shipment(
        self, request: GetShipmentRequest, *args, **kwargs
    ) -> ApiResponse[GetShipmentResponse]:
        """
        Returns the shipment information for an existing shipment.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            1 |       1 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that are applied to the requested operation when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the SP-API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        ...

    @sp_endpoint("/mfn/v0/shipments/{shipmentId}", method="GET")
    def get_shipment(self, *args, **kwargs) -> ApiResponse[GetShipmentResponse]:
        """
        Returns the shipment information for an existing shipment.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            1 |       1 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that are applied to the requested operation when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the SP-API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
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
        Cancel the shipment indicated by the specified shipment identifier.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            1 |       1 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that are applied to the requested operation when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the SP-API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        ...

    @sp_endpoint("/mfn/v0/shipments/{shipmentId}", method="DELETE")
    def cancel_shipment(self, *args, **kwargs) -> ApiResponse[CancelShipmentResponse]:
        """
        Cancel the shipment indicated by the specified shipment identifier.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            1 |       1 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that are applied to the requested operation when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the SP-API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
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
    def create_shipment(
        self, request: CreateShipmentRequest, *args, **kwargs
    ) -> ApiResponse[CreateShipmentResponse]:
        """
        Create a shipment with the information provided.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            2 |       2 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that are applied to the requested operation when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the SP-API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        ...

    @sp_endpoint("/mfn/v0/shipments", method="POST")
    def create_shipment(self, *args, **kwargs) -> ApiResponse[CreateShipmentResponse]:
        """
        Create a shipment with the information provided.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            2 |       2 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that are applied to the requested operation when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the SP-API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
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
    def get_additional_seller_inputs(
        self, request: GetAdditionalSellerInputsRequest, *args, **kwargs
    ) -> ApiResponse[GetAdditionalSellerInputsResponse]:
        """
        Gets a list of additional seller inputs required for a ship method. This is generally used for international shipping.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            1 |       1 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that are applied to the requested operation when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the SP-API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        ...

    @sp_endpoint("/mfn/v0/additionalSellerInputs", method="POST")
    def get_additional_seller_inputs(
        self, *args, **kwargs
    ) -> ApiResponse[GetAdditionalSellerInputsResponse]:
        """
        Gets a list of additional seller inputs required for a ship method. This is generally used for international shipping.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            1 |       1 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that are applied to the requested operation when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the SP-API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, GetAdditionalSellerInputsRequest):
            request = GetAdditionalSellerInputsRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path,
            query=query,
            body=body,
            method=method,
            _type=GetAdditionalSellerInputsResponse,
        )
