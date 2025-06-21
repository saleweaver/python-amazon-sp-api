"""
Common models generated from Swagger/OpenAPI specification.

This file was auto-generated. Do not edit manually.

"""

from datetime import date, datetime
from enum import Enum, auto
from typing import Annotated, Any, Dict, List, Optional, Union
from uuid import UUID

from pydantic import AliasChoices, BaseModel, ConfigDict, Field

from .base_models import (BodyParam, GetRequestSerializer, PathParam,
                          QueryParam, RequestsBaseModel, SpApiBaseModel)

"""
Categories


"""


class Categories(SpApiBaseModel):
    """"""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    product_category_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("ProductCategoryId", "product_category_id"),
            serialization_alias="ProductCategoryId",
            description="The identifier for the product category (or browse node).",
        ),
    ]

    product_category_name: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "ProductCategoryName", "product_category_name"
            ),
            serialization_alias="ProductCategoryName",
            description="The name of the product category (or browse node).",
        ),
    ]

    parent: Annotated[
        Optional[Dict[str, Any]],
        Field(None, description="The parent product category."),
    ]


"""
Error

Error response returned when the request is unsuccessful.
"""


class Error(SpApiBaseModel):
    """Error response returned when the request is unsuccessful."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    code: Annotated[
        str,
        Field(
            ...,
            description="An error code that identifies the type of error that occurred.",
        ),
    ]

    message: Annotated[
        str,
        Field(
            ...,
            description="A message that describes the error condition in a human-readable form.",
        ),
    ]

    details: Annotated[
        Optional[str],
        Field(
            None,
            description="Additional information that can help the caller understand or fix the issue.",
        ),
    ]


ErrorList = List["Error"]
"""A list of error responses returned when a request is unsuccessful."""


"""
ListCatalogCategoriesRequest

Request parameters for listCatalogCategories
"""


class ListCatalogCategoriesRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for listCatalogCategories
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    marketplace_id: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("MarketplaceId", "marketplace_id"),
            serialization_alias="MarketplaceId",
            description="[QUERY] A marketplace identifier. Specifies the marketplace for the item.",
        ),
    ]

    a_s_i_n: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("ASIN", "a_s_i_n"),
            serialization_alias="ASIN",
            description="[QUERY] The Amazon Standard Identification Number (ASIN) of the item.",
        ),
    ]

    seller_s_k_u: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("SellerSKU", "seller_s_k_u"),
            serialization_alias="SellerSKU",
            description="[QUERY] Used to identify items in the given marketplace. SellerSKU is qualified by the seller's SellerId, which is included with every operation that you submit.",
        ),
    ]


ListOfCategories = List["Categories"]
""""""


"""
ListCatalogCategoriesResponse


"""


class ListCatalogCategoriesResponse(SpApiBaseModel):
    """"""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["ListOfCategories"],
        Field(None, description="The payload for the listCatalogCategories operation."),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
            description="One or more unexpected errors occurred during the listCatalogCategories operation.",
        ),
    ]


# Rebuild models to resolve forward references
ListCatalogCategoriesResponse.model_rebuild()
Categories.model_rebuild()
Error.model_rebuild()
ListCatalogCategoriesRequest.model_rebuild()
