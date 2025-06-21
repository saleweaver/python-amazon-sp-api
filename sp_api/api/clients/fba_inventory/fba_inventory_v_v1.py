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
from sp_api.api.models.fba_inventory.fba_inventory_v1 import *
from sp_api.base import ApiResponse, Client, fill_query_params, sp_endpoint

T = TypeVar("T")


class FbaInventory_V_v1(Client):
    """
    Selling Partner API for FBA Inventory - v1

    The Selling Partner API for FBA Inventory lets you programmatically retrieve information about inventory in Amazon's fulfillment network.
    """

    @overload
    def get_inventory_summaries(
        self, request: GetInventorySummariesRequest, *args, **kwargs
    ) -> ApiResponse[GetInventorySummariesResponse]:
        """
        Returns a list of inventory summaries. The summaries returned depend on the presence or absence of the startDateTime, sellerSkus and sellerSku parameters:

        - All inventory summaries with available details are returned when the startDateTime, sellerSkus and sellerSku parameters are omitted.

        - When startDateTime is provided, the operation returns inventory summaries that have had changes after the date and time specified. The sellerSkus and sellerSku parameters are ignored. Important: To avoid errors, use both startDateTime and nextToken to get the next page of inventory summaries that have changed after the date and time specified.

        - When the sellerSkus parameter is provided, the operation returns inventory summaries for only the specified sellerSkus. The sellerSku parameter is ignored.

        - When the sellerSku parameter is provided, the operation returns inventory summaries for only the specified sellerSku.

        Note: The parameters associated with this operation may contain special characters that must be encoded to successfully call the API. To avoid errors with SKUs when encoding URLs, refer to [URL Encoding](https://developer-docs.amazon.com/sp-api/docs/url-encoding).

        Usage Plan:

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            2 |       2 |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits).
        """
        ...

    @sp_endpoint("/fba/inventory/v1/summaries", method="GET")
    def get_inventory_summaries(
        self, *args, **kwargs
    ) -> ApiResponse[GetInventorySummariesResponse]:
        """
        Returns a list of inventory summaries. The summaries returned depend on the presence or absence of the startDateTime, sellerSkus and sellerSku parameters:

        - All inventory summaries with available details are returned when the startDateTime, sellerSkus and sellerSku parameters are omitted.

        - When startDateTime is provided, the operation returns inventory summaries that have had changes after the date and time specified. The sellerSkus and sellerSku parameters are ignored. Important: To avoid errors, use both startDateTime and nextToken to get the next page of inventory summaries that have changed after the date and time specified.

        - When the sellerSkus parameter is provided, the operation returns inventory summaries for only the specified sellerSkus. The sellerSku parameter is ignored.

        - When the sellerSku parameter is provided, the operation returns inventory summaries for only the specified sellerSku.

        Note: The parameters associated with this operation may contain special characters that must be encoded to successfully call the API. To avoid errors with SKUs when encoding URLs, refer to [URL Encoding](https://developer-docs.amazon.com/sp-api/docs/url-encoding).

        Usage Plan:

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            2 |       2 |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits).
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, GetInventorySummariesRequest):
            request = GetInventorySummariesRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path,
            query=query,
            body=body,
            method=method,
            _type=GetInventorySummariesResponse,
        )

    @overload
    def create_inventory_item(
        self, request: CreateInventoryItemRequest, *args, **kwargs
    ) -> ApiResponse[CreateInventoryItemResponse]:
        """
        Requests that Amazon create product-details in the Sandbox Inventory in the sandbox environment. This is a sandbox-only operation and must be directed to a sandbox endpoint. Refer to [Selling Partner API sandbox](https://developer-docs.amazon.com/sp-api/docs/the-selling-partner-api-sandbox) for more information.
        """
        ...

    @sp_endpoint("/fba/inventory/v1/items", method="POST")
    def create_inventory_item(
        self, *args, **kwargs
    ) -> ApiResponse[CreateInventoryItemResponse]:
        """
        Requests that Amazon create product-details in the Sandbox Inventory in the sandbox environment. This is a sandbox-only operation and must be directed to a sandbox endpoint. Refer to [Selling Partner API sandbox](https://developer-docs.amazon.com/sp-api/docs/the-selling-partner-api-sandbox) for more information.
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, CreateInventoryItemRequest):
            request = CreateInventoryItemRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path,
            query=query,
            body=body,
            method=method,
            _type=CreateInventoryItemResponse,
        )

    @overload
    def delete_inventory_item(
        self, request: DeleteInventoryItemRequest, *args, **kwargs
    ) -> ApiResponse[DeleteInventoryItemResponse]:
        """
        Requests that Amazon Deletes an item from the Sandbox Inventory in the sandbox environment. This is a sandbox-only operation and must be directed to a sandbox endpoint. Refer to [Selling Partner API sandbox](https://developer-docs.amazon.com/sp-api/docs/the-selling-partner-api-sandbox) for more information.
        """
        ...

    @sp_endpoint("/fba/inventory/v1/items/{sellerSku}", method="DELETE")
    def delete_inventory_item(
        self, *args, **kwargs
    ) -> ApiResponse[DeleteInventoryItemResponse]:
        """
        Requests that Amazon Deletes an item from the Sandbox Inventory in the sandbox environment. This is a sandbox-only operation and must be directed to a sandbox endpoint. Refer to [Selling Partner API sandbox](https://developer-docs.amazon.com/sp-api/docs/the-selling-partner-api-sandbox) for more information.
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, DeleteInventoryItemRequest):
            request = DeleteInventoryItemRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path,
            query=query,
            body=body,
            method=method,
            _type=DeleteInventoryItemResponse,
        )

    @overload
    def add_inventory(
        self, request: AddInventoryRequest, *args, **kwargs
    ) -> ApiResponse[AddInventoryResponse]:
        """
        Requests that Amazon add items to the Sandbox Inventory with desired amount of quantity in the sandbox environment. This is a sandbox-only operation and must be directed to a sandbox endpoint. Refer to [Selling Partner API sandbox](https://developer-docs.amazon.com/sp-api/docs/the-selling-partner-api-sandbox) for more information.
        """
        ...

    @sp_endpoint("/fba/inventory/v1/items/inventory", method="POST")
    def add_inventory(self, *args, **kwargs) -> ApiResponse[AddInventoryResponse]:
        """
        Requests that Amazon add items to the Sandbox Inventory with desired amount of quantity in the sandbox environment. This is a sandbox-only operation and must be directed to a sandbox endpoint. Refer to [Selling Partner API sandbox](https://developer-docs.amazon.com/sp-api/docs/the-selling-partner-api-sandbox) for more information.
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, AddInventoryRequest):
            request = AddInventoryRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path, query=query, body=body, method=method, _type=AddInventoryResponse
        )
