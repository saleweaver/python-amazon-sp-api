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
from sp_api.api.models.vendor_direct_fulfillment_inventory.vendor_direct_fulfillment_inventory_v1 import *
from sp_api.base import ApiResponse, Client, fill_query_params, sp_endpoint

T = TypeVar("T")


class VendorDirectFulfillmentInventory_V_v1(Client):
    """
    Selling Partner API for Direct Fulfillment Inventory Updates - v1

    The Selling Partner API for Direct Fulfillment Inventory Updates provides programmatic access to a direct fulfillment vendor's inventory updates.
    """

    @overload
    def submit_inventory_update(
        self, request: SubmitInventoryUpdateRequest, *args, **kwargs
    ) -> ApiResponse[SubmitInventoryUpdateResponse]:
        """
        Submits inventory updates for the specified warehouse for either a partial or full feed of inventory items.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                           10 |      10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        ...

    @sp_endpoint(
        "/vendor/directFulfillment/inventory/v1/warehouses/{warehouseId}/items",
        method="POST",
    )
    def submit_inventory_update(
        self, *args, **kwargs
    ) -> ApiResponse[SubmitInventoryUpdateResponse]:
        """
        Submits inventory updates for the specified warehouse for either a partial or full feed of inventory items.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                           10 |      10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, SubmitInventoryUpdateRequest):
            request = SubmitInventoryUpdateRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path,
            query=query,
            body=body,
            method=method,
            _type=SubmitInventoryUpdateResponse,
        )
