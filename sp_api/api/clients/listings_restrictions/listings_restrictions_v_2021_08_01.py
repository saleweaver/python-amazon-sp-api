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
from sp_api.api.models.listings_restrictions.listings_restrictions_2021_08_01 import *
from sp_api.base import ApiResponse, Client, fill_query_params, sp_endpoint

T = TypeVar("T")


class ListingsRestrictions_V_2021_08_01(Client):
    """
    Selling Partner API for Listings Restrictions - 2021-08-01

    The Selling Partner API for Listings Restrictions provides programmatic access to restrictions on Amazon catalog listings.
    For more information, see the [Listings Restrictions API Use Case Guide](doc:listings-restrictions-api-v2021-08-01-use-case-guide).
    """

    @overload
    def get_listings_restrictions(
        self, request: GetListingsRestrictionsRequest, *args, **kwargs
    ) -> ApiResponse[RestrictionList]:
        """
        Returns listing restrictions for an item in the Amazon Catalog.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            5 |      10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        ...

    @sp_endpoint("/listings/2021-08-01/restrictions", method="GET")
    def get_listings_restrictions(
        self, *args, **kwargs
    ) -> ApiResponse[RestrictionList]:
        """
        Returns listing restrictions for an item in the Amazon Catalog.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            5 |      10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, GetListingsRestrictionsRequest):
            request = GetListingsRestrictionsRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path, query=query, body=body, method=method, _type=RestrictionList
        )
