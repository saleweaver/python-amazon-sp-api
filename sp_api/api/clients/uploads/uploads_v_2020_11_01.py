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
from sp_api.api.models.uploads.uploads_2020_11_01 import *
from sp_api.base import ApiResponse, Client, fill_query_params, sp_endpoint

T = TypeVar("T")


class Uploads_V_2020_11_01(Client):
    """
    Selling Partner API for Uploads - 2020-11-01

    The Uploads API lets you upload files that you can programmatically access using other Selling Partner APIs, such as the A+ Content API and the Messaging API.
    """

    @overload
    def create_upload_destination_for_resource(
        self, request: CreateUploadDestinationForResourceRequest, *args, **kwargs
    ) -> ApiResponse[CreateUploadDestinationResponse]:
        """
        Creates an upload destination, returning the information required to upload a file to the destination and to programmatically access the file.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                           10 |      10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        ...

    @sp_endpoint("/uploads/2020-11-01/uploadDestinations/{resource}", method="POST")
    def create_upload_destination_for_resource(
        self, *args, **kwargs
    ) -> ApiResponse[CreateUploadDestinationResponse]:
        """
        Creates an upload destination, returning the information required to upload a file to the destination and to programmatically access the file.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                           10 |      10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, CreateUploadDestinationForResourceRequest):
            request = CreateUploadDestinationForResourceRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path,
            query=query,
            body=body,
            method=method,
            _type=CreateUploadDestinationResponse,
        )
