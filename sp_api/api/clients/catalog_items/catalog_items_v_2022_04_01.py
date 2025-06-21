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
from sp_api.api.models.catalog_items.catalog_items_2022_04_01 import *
from sp_api.base import ApiResponse, Client, fill_query_params, sp_endpoint

T = TypeVar("T")


class CatalogItems_V_2022_04_01(Client):
    """
    Selling Partner API for Catalog Items - 2022-04-01

    Use the Selling Partner API for Catalog Items to retrieve information about items in the Amazon catalog.
    For more information, refer to the [Catalog Items API Use Case Guide](https://developer-docs.amazon.com/sp-api/docs/:catalog-items-api-v2022-04-01-use-case-guide).
    """

    @overload
    def search_catalog_items(
        self, request: SearchCatalogItemsRequest, *args, **kwargs
    ) -> ApiResponse[ItemSearchResults]:
        """
        Search for a list of Amazon catalog items and item-related information. You can search by identifier or by keywords.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            5 |       5 |

        The `x-amzn-RateLimit-Limit` response header contains the usage plan rate limits for the operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput might have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        ...

    @sp_endpoint("/catalog/2022-04-01/items", method="GET")
    def search_catalog_items(self, *args, **kwargs) -> ApiResponse[ItemSearchResults]:
        """
        Search for a list of Amazon catalog items and item-related information. You can search by identifier or by keywords.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            5 |       5 |

        The `x-amzn-RateLimit-Limit` response header contains the usage plan rate limits for the operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput might have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, SearchCatalogItemsRequest):
            request = SearchCatalogItemsRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path, query=query, body=body, method=method, _type=ItemSearchResults
        )

    @overload
    def get_catalog_item(
        self, request: GetCatalogItemRequest, *args, **kwargs
    ) -> ApiResponse[Item]:
        """
        Retrieves details for an item in the Amazon catalog.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            5 |       5 |

        The `x-amzn-RateLimit-Limit` response header contains the usage plan rate limits for the operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput might have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        ...

    @sp_endpoint("/catalog/2022-04-01/items/{asin}", method="GET")
    def get_catalog_item(self, *args, **kwargs) -> ApiResponse[Item]:
        """
        Retrieves details for an item in the Amazon catalog.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            5 |       5 |

        The `x-amzn-RateLimit-Limit` response header contains the usage plan rate limits for the operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput might have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, GetCatalogItemRequest):
            request = GetCatalogItemRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(path, query=query, body=body, method=method, _type=Item)
