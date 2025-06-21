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
from sp_api.api.models.vendor_direct_fulfillment_transactions.vendor_direct_fulfillment_transactions_2021_12_28 import *
from sp_api.base import ApiResponse, Client, fill_query_params, sp_endpoint

T = TypeVar("T")


class VendorDirectFulfillmentTransactions_V_2021_12_28(Client):
    """
    Selling Partner API for Direct Fulfillment Transaction Status - 2021-12-28

    The Selling Partner API for Direct Fulfillment Transaction Status provides programmatic access to a direct fulfillment vendor's transaction status.
    """

    @overload
    def get_transaction_status(
        self, request: GetTransactionStatusRequest, *args, **kwargs
    ) -> ApiResponse[TransactionStatus]:
        """
        Returns the status of the transaction indicated by the specified transactionId.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                           10 |      10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        ...

    @sp_endpoint(
        "/vendor/directFulfillment/transactions/2021-12-28/transactions/{transactionId}",
        method="GET",
    )
    def get_transaction_status(self, *args, **kwargs) -> ApiResponse[TransactionStatus]:
        """
        Returns the status of the transaction indicated by the specified transactionId.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                           10 |      10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, GetTransactionStatusRequest):
            request = GetTransactionStatusRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path, query=query, body=body, method=method, _type=TransactionStatus
        )
