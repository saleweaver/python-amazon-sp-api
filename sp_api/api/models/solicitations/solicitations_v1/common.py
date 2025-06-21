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
CreateProductReviewAndSellerFeedbackSolicitationRequest

Request parameters for createProductReviewAndSellerFeedbackSolicitation
"""


class CreateProductReviewAndSellerFeedbackSolicitationRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for createProductReviewAndSellerFeedbackSolicitation
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    amazon_order_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("amazonOrderId", "amazon_order_id"),
            serialization_alias="amazonOrderId",
            description="[PATH] An Amazon order identifier. This specifies the order for which a solicitation is sent.",
        ),
    ]

    marketplace_ids: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceIds", "marketplace_ids"),
            serialization_alias="marketplaceIds",
            description="[QUERY] A marketplace identifier. This specifies the marketplace in which the order was placed. Only one marketplace can be specified.",
        ),
    ]


ErrorList = List["Error"]
"""A list of error responses returned when a request is unsuccessful."""


"""
CreateProductReviewAndSellerFeedbackSolicitationResponse

The response schema for the createProductReviewAndSellerFeedbackSolicitation operation.
"""


class CreateProductReviewAndSellerFeedbackSolicitationResponse(SpApiBaseModel):
    """The response schema for the createProductReviewAndSellerFeedbackSolicitation operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
        ),
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
        str, Field(..., description="A message that describes the error condition.")
    ]

    details: Annotated[
        Optional[str],
        Field(
            None,
            description="Additional details that can help the caller understand or fix the issue.",
        ),
    ]


"""
Schema

A JSON schema document describing the expected payload of the action. This object can be validated against <a href=http://json-schema.org/draft-04/schema>http://json-schema.org/draft-04/schema</a>.
"""


class Schema(SpApiBaseModel):
    """A JSON schema document describing the expected payload of the action. This object can be validated against <a href=http://json-schema.org/draft-04/schema>http://json-schema.org/draft-04/schema</a>."""

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow",
        serialize_by_alias=True,
        arbitrary_types_allowed=True,
    )


"""
GetSchemaResponse


"""


class GetSchemaResponse(SpApiBaseModel):
    """"""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    links: Annotated[
        Optional[Dict[str, Any]],
        Field(
            None,
            validation_alias=AliasChoices("_links", "links"),
            serialization_alias="_links",
        ),
    ]

    payload: Annotated[
        Optional["Schema"],
        Field(
            None,
        ),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
        ),
    ]


"""
SolicitationsAction

A simple object containing the name of the template.
"""


class SolicitationsAction(SpApiBaseModel):
    """A simple object containing the name of the template."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    name: Annotated[
        str,
        Field(
            ...,
        ),
    ]


"""
GetSolicitationActionResponse

Describes a solicitation action that can be taken for an order. Provides a JSON Hypertext Application Language (HAL) link to the JSON schema document that describes the expected input.
"""


class GetSolicitationActionResponse(SpApiBaseModel):
    """Describes a solicitation action that can be taken for an order. Provides a JSON Hypertext Application Language (HAL) link to the JSON schema document that describes the expected input."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    links: Annotated[
        Optional[Dict[str, Any]],
        Field(
            None,
            validation_alias=AliasChoices("_links", "links"),
            serialization_alias="_links",
        ),
    ]

    embedded: Annotated[
        Optional[Dict[str, Any]],
        Field(
            None,
            validation_alias=AliasChoices("_embedded", "embedded"),
            serialization_alias="_embedded",
        ),
    ]

    payload: Annotated[
        Optional["SolicitationsAction"],
        Field(
            None,
        ),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
        ),
    ]


"""
GetSolicitationActionsForOrderRequest

Request parameters for getSolicitationActionsForOrder
"""


class GetSolicitationActionsForOrderRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getSolicitationActionsForOrder
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    amazon_order_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("amazonOrderId", "amazon_order_id"),
            serialization_alias="amazonOrderId",
            description="[PATH] An Amazon order identifier. This specifies the order for which you want a list of available solicitation types.",
        ),
    ]

    marketplace_ids: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceIds", "marketplace_ids"),
            serialization_alias="marketplaceIds",
            description="[QUERY] A marketplace identifier. This specifies the marketplace in which the order was placed. Only one marketplace can be specified.",
        ),
    ]


"""
GetSolicitationActionsForOrderResponse

The response schema for the getSolicitationActionsForOrder operation.
"""


class GetSolicitationActionsForOrderResponse(SpApiBaseModel):
    """The response schema for the getSolicitationActionsForOrder operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    links: Annotated[
        Optional[Dict[str, Any]],
        Field(
            None,
            validation_alias=AliasChoices("_links", "links"),
            serialization_alias="_links",
        ),
    ]

    embedded: Annotated[
        Optional[Dict[str, Any]],
        Field(
            None,
            validation_alias=AliasChoices("_embedded", "embedded"),
            serialization_alias="_embedded",
        ),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
        ),
    ]


"""
LinkObject

A Link object.
"""


class LinkObject(SpApiBaseModel):
    """A Link object."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    href: Annotated[str, Field(..., description="A URI for this object.")]

    name: Annotated[
        Optional[str], Field(None, description="An identifier for this object.")
    ]


# Rebuild models to resolve forward references
LinkObject.model_rebuild()
SolicitationsAction.model_rebuild()
Schema.model_rebuild()
GetSolicitationActionsForOrderResponse.model_rebuild()
GetSolicitationActionResponse.model_rebuild()
GetSchemaResponse.model_rebuild()
CreateProductReviewAndSellerFeedbackSolicitationResponse.model_rebuild()
Error.model_rebuild()
GetSolicitationActionsForOrderRequest.model_rebuild()
CreateProductReviewAndSellerFeedbackSolicitationRequest.model_rebuild()
