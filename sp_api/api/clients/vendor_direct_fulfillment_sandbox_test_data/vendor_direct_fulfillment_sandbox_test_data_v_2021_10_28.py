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
from sp_api.api.models.vendor_direct_fulfillment_sandbox_test_data.vendor_direct_fulfillment_sandbox_test_data_2021_10_28 import *
from sp_api.base import ApiResponse, Client, fill_query_params, sp_endpoint

T = TypeVar("T")


class VendorDirectFulfillmentSandboxTestData_V_2021_10_28(Client):
    """
    Selling Partner API for Vendor Direct Fulfillment Sandbox Test Data - 2021-10-28

    The Selling Partner API for Vendor Direct Fulfillment Sandbox Test Data provides programmatic access to vendor direct fulfillment sandbox test data.
    """

    @overload
    def generate_order_scenarios(
        self, request: GenerateOrderScenariosRequest, *args, **kwargs
    ) -> ApiResponse[TransactionReference]:
        """
        Submits a request to generate test order data for Vendor Direct Fulfillment API entities.
        """
        ...

    @sp_endpoint("/vendor/directFulfillment/sandbox/2021-10-28/orders", method="POST")
    def generate_order_scenarios(
        self, *args, **kwargs
    ) -> ApiResponse[TransactionReference]:
        """
        Submits a request to generate test order data for Vendor Direct Fulfillment API entities.
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, GenerateOrderScenariosRequest):
            request = GenerateOrderScenariosRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path, query=query, body=body, method=method, _type=TransactionReference
        )

    @overload
    def get_order_scenarios(
        self, request: GetOrderScenariosRequest, *args, **kwargs
    ) -> ApiResponse[TransactionStatus]:
        """
        Returns the status of the transaction indicated by the specified transactionId. If the transaction was successful, also returns the requested test order data.
        """
        ...

    @sp_endpoint(
        "/vendor/directFulfillment/sandbox/2021-10-28/transactions/{transactionId}",
        method="GET",
    )
    def get_order_scenarios(self, *args, **kwargs) -> ApiResponse[TransactionStatus]:
        """
        Returns the status of the transaction indicated by the specified transactionId. If the transaction was successful, also returns the requested test order data.
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, GetOrderScenariosRequest):
            request = GetOrderScenariosRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path, query=query, body=body, method=method, _type=TransactionStatus
        )
