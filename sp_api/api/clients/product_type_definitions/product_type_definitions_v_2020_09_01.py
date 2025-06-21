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
from sp_api.api.models.product_type_definitions.product_type_definitions_2020_09_01 import *
from sp_api.base import ApiResponse, Client, fill_query_params, sp_endpoint

T = TypeVar("T")


class ProductTypeDefinitions_V_2020_09_01(Client):
    """
    Selling Partner API for Product Type Definitions - 2020-09-01

    The Selling Partner API for Product Type Definitions provides programmatic access to attribute and data requirements for product types in the Amazon catalog. Use this API to return the JSON Schema for a product type that you can then use with other Selling Partner APIs, such as the Selling Partner API for Listings Items, the Selling Partner API for Catalog Items, and the Selling Partner API for Feeds (for JSON-based listing feeds).
    For more information, see the [Product Type Definitions API Use Case Guide](doc:product-type-api-use-case-guide).
    """

    @overload
    def search_definitions_product_types(
        self, request: SearchDefinitionsProductTypesRequest, *args, **kwargs
    ) -> ApiResponse[ProductTypeList]:
        """
        Search for and return a list of Amazon product types that have definitions available.

        **Usage Plans:**

        | Plan type                | Rate (requests per second)   | Burst    |
        |--------------------------|------------------------------|----------|
        | Default                  | 5                            | 10       |
        | Selling partner specific | Variable                     | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        ...

    @sp_endpoint("/definitions/2020-09-01/productTypes", method="GET")
    def search_definitions_product_types(
        self, *args, **kwargs
    ) -> ApiResponse[ProductTypeList]:
        """
        Search for and return a list of Amazon product types that have definitions available.

        **Usage Plans:**

        | Plan type                | Rate (requests per second)   | Burst    |
        |--------------------------|------------------------------|----------|
        | Default                  | 5                            | 10       |
        | Selling partner specific | Variable                     | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, SearchDefinitionsProductTypesRequest):
            request = SearchDefinitionsProductTypesRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path, query=query, body=body, method=method, _type=ProductTypeList
        )

    @overload
    def get_definitions_product_type(
        self, request: GetDefinitionsProductTypeRequest, *args, **kwargs
    ) -> ApiResponse[ProductTypeDefinition]:
        """
        Retrieve an Amazon product type definition.

        **Usage Plans:**

        | Plan type                | Rate (requests per second)   | Burst    |
        |--------------------------|------------------------------|----------|
        | Default                  | 5                            | 10       |
        | Selling partner specific | Variable                     | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        ...

    @sp_endpoint("/definitions/2020-09-01/productTypes/{productType}", method="GET")
    def get_definitions_product_type(
        self, *args, **kwargs
    ) -> ApiResponse[ProductTypeDefinition]:
        """
        Retrieve an Amazon product type definition.

        **Usage Plans:**

        | Plan type                | Rate (requests per second)   | Burst    |
        |--------------------------|------------------------------|----------|
        | Default                  | 5                            | 10       |
        | Selling partner specific | Variable                     | Variable |

        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](doc:usage-plans-and-rate-limits-in-the-sp-api).
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, GetDefinitionsProductTypeRequest):
            request = GetDefinitionsProductTypeRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path, query=query, body=body, method=method, _type=ProductTypeDefinition
        )
