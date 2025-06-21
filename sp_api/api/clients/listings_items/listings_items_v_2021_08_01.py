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
from sp_api.api.models.listings_items.listings_items_2021_08_01 import *
from sp_api.base import ApiResponse, Client, fill_query_params, sp_endpoint

T = TypeVar("T")


class ListingsItems_V_2021_08_01(Client):
    """
    Selling Partner API for Listings Items - 2021-08-01

    The Selling Partner API for Listings Items (Listings Items API) provides programmatic access to selling partner listings on Amazon. Use this API in collaboration with the Selling Partner API for Product Type Definitions, which you use to retrieve the information about Amazon product types needed to use the Listings Items API.
    For more information, see the [Listings Items API Use Case Guide](https://developer-docs.amazon.com/sp-api/docs/listings-items-api-v2021-08-01-use-case-guide).
    """

    @overload
    def delete_listings_item(
        self, request: DeleteListingsItemRequest, *args, **kwargs
    ) -> ApiResponse[ListingsItemSubmissionResponse]:
        """
        Delete a listings item for a selling partner.

        **Note:** The parameters associated with this operation may contain special characters that must be encoded to successfully call the API. To avoid errors with SKUs when encoding URLs, refer to [URL Encoding](https://developer-docs.amazon.com/sp-api/docs/url-encoding).

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            5 |      10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        ...

    @sp_endpoint("/listings/2021-08-01/items/{sellerId}/{sku}", method="DELETE")
    def delete_listings_item(
        self, *args, **kwargs
    ) -> ApiResponse[ListingsItemSubmissionResponse]:
        """
        Delete a listings item for a selling partner.

        **Note:** The parameters associated with this operation may contain special characters that must be encoded to successfully call the API. To avoid errors with SKUs when encoding URLs, refer to [URL Encoding](https://developer-docs.amazon.com/sp-api/docs/url-encoding).

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            5 |      10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, DeleteListingsItemRequest):
            request = DeleteListingsItemRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path,
            query=query,
            body=body,
            method=method,
            _type=ListingsItemSubmissionResponse,
        )

    @overload
    def get_listings_item(
        self, request: GetListingsItemRequest, *args, **kwargs
    ) -> ApiResponse[Item]:
        """
        Returns details about a listings item for a selling partner.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            5 |      10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput can receive higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api) in the Selling Partner API documentation.
        """
        ...

    @sp_endpoint("/listings/2021-08-01/items/{sellerId}/{sku}", method="GET")
    def get_listings_item(self, *args, **kwargs) -> ApiResponse[Item]:
        """
        Returns details about a listings item for a selling partner.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            5 |      10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput can receive higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api) in the Selling Partner API documentation.
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, GetListingsItemRequest):
            request = GetListingsItemRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(path, query=query, body=body, method=method, _type=Item)

    @overload
    def patch_listings_item(
        self, request: PatchListingsItemRequest, *args, **kwargs
    ) -> ApiResponse[ListingsItemSubmissionResponse]:
        """
        Partially update (patch) a listings item for a selling partner. Only top-level listings item attributes can be patched. Patching nested attributes is not supported.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            5 |       5 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput can receive higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api) in the Selling Partner API documentation.
        """
        ...

    @sp_endpoint("/listings/2021-08-01/items/{sellerId}/{sku}", method="PATCH")
    def patch_listings_item(
        self, *args, **kwargs
    ) -> ApiResponse[ListingsItemSubmissionResponse]:
        """
        Partially update (patch) a listings item for a selling partner. Only top-level listings item attributes can be patched. Patching nested attributes is not supported.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            5 |       5 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput can receive higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api) in the Selling Partner API documentation.
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, PatchListingsItemRequest):
            request = PatchListingsItemRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path,
            query=query,
            body=body,
            method=method,
            _type=ListingsItemSubmissionResponse,
        )

    @overload
    def put_listings_item(
        self, request: PutListingsItemRequest, *args, **kwargs
    ) -> ApiResponse[ListingsItemSubmissionResponse]:
        """
        Creates a new or fully-updates an existing listings item for a selling partner.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            5 |      10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput can receive higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api) in the Selling Partner API documentation.
        """
        ...

    @sp_endpoint("/listings/2021-08-01/items/{sellerId}/{sku}", method="PUT")
    def put_listings_item(
        self, *args, **kwargs
    ) -> ApiResponse[ListingsItemSubmissionResponse]:
        """
        Creates a new or fully-updates an existing listings item for a selling partner.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            5 |      10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput can receive higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api) in the Selling Partner API documentation.
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, PutListingsItemRequest):
            request = PutListingsItemRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path,
            query=query,
            body=body,
            method=method,
            _type=ListingsItemSubmissionResponse,
        )

    @overload
    def search_listings_items(
        self, request: SearchListingsItemsRequest, *args, **kwargs
    ) -> ApiResponse[ItemSearchResults]:
        """
        Search for and return a list of selling partner listings items and their respective details.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            5 |       5 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that are applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput might have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        ...

    @sp_endpoint("/listings/2021-08-01/items/{sellerId}", method="GET")
    def search_listings_items(self, *args, **kwargs) -> ApiResponse[ItemSearchResults]:
        """
        Search for and return a list of selling partner listings items and their respective details.

        **Usage Plan:**

        |   Rate (requests per second) |   Burst |
        |------------------------------|---------|
        |                            5 |       5 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that are applied to the requested operation, when available. The preceding table contains the default rate and burst values for this operation. Selling partners whose business demands require higher throughput might have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, SearchListingsItemsRequest):
            request = SearchListingsItemsRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path, query=query, body=body, method=method, _type=ItemSearchResults
        )
