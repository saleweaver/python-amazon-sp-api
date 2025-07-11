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
DeleteListingsItemRequest

Request parameters for deleteListingsItem
"""


class DeleteListingsItemRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for deleteListingsItem
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    seller_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("sellerId", "seller_id"),
            serialization_alias="sellerId",
            description="[PATH] A selling partner identifier, such as a merchant account or vendor code.",
        ),
    ]

    sku: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            description="[PATH] A selling partner provided identifier for an Amazon listing.",
        ),
    ]

    marketplace_ids: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceIds", "marketplace_ids"),
            serialization_alias="marketplaceIds",
            description="[QUERY] A comma-delimited list of Amazon marketplace identifiers for the request.",
        ),
    ]

    issue_locale: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("issueLocale", "issue_locale"),
            serialization_alias="issueLocale",
            description="[QUERY] A locale for localization of issues. When not provided, the default language code of the first marketplace is used. Examples: 'en_US', 'fr_CA', 'fr_FR'. Localized messages default to 'en_US' when a localization is not available in the specified locale.",
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
ErrorList

A list of error responses returned when a request is unsuccessful.
"""


class ErrorList(SpApiBaseModel):
    """A list of error responses returned when a request is unsuccessful."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    errors: Annotated[
        List["Error"],
        Field(
            ...,
        ),
    ]


# Enum definitions
class IssueSeverityEnum(str, Enum):
    """Enum for severity"""

    ERROR = "ERROR"  # Indicates an issue has occurred preventing the submission from processing, such as a validation error.
    WARNING = "WARNING"  # Indicates an issue has occurred that should be reviewed, but has not prevented the submission from processing.
    INFO = "INFO"  # Indicates additional information has been provided that should be reviewed.


"""
Issue

An issue with a listings item.
"""


class Issue(SpApiBaseModel):
    """An issue with a listings item."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    code: Annotated[
        str, Field(..., description="An issue code that identifies the type of issue.")
    ]

    message: Annotated[
        str, Field(..., description="A message that describes the issue.")
    ]

    severity: Annotated[
        IssueSeverityEnum, Field(..., description="The severity of the issue.")
    ]

    attribute_name: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("attributeName", "attribute_name"),
            serialization_alias="attributeName",
            description="Name of the attribute associated with the issue, if applicable.",
        ),
    ]


# Enum definitions
class PatchOperationOpEnum(str, Enum):
    """Enum for op"""

    ADD = "add"  # The "add" operation adds or replaces the target property.
    REPLACE = "replace"  # The "replace" operation adds or replaces the target property.
    DELETE = "delete"  # The "delete" operation removes the target property. Not supported for vendors (vendors will receive an HTTP status code 400 response).


"""
PatchOperation

Individual JSON Patch operation for an HTTP PATCH request.
"""


class PatchOperation(SpApiBaseModel):
    """Individual JSON Patch operation for an HTTP PATCH request."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    op: Annotated[
        PatchOperationOpEnum,
        Field(
            ...,
            description="Type of JSON Patch operation. Supported JSON Patch operations include add, replace, and delete. See <https://tools.ietf.org/html/rfc6902>.",
        ),
    ]

    path: Annotated[
        str,
        Field(
            ...,
            description="JSON Pointer path of the element to patch. See <https://tools.ietf.org/html/rfc6902>.",
        ),
    ]

    value: Annotated[
        Optional[List[Dict[str, Any]]],
        Field(None, description="JSON value to add, replace, or delete."),
    ]


"""
ListingsItemPatchRequestBody

The request body schema for the patchListingsItem operation.
"""


class ListingsItemPatchRequestBody(SpApiBaseModel):
    """The request body schema for the patchListingsItem operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    product_type: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("productType", "product_type"),
            serialization_alias="productType",
            description="The Amazon product type of the listings item.",
        ),
    ]

    patches: Annotated[
        List["PatchOperation"],
        Field(
            ...,
            description="One or more JSON Patch operations to perform on the listings item.",
        ),
    ]


# Enum definitions
class ListingsItemPutRequestBodyRequirementsEnum(str, Enum):
    """Enum for requirements"""

    LISTING = "LISTING"  # Indicates the submitted data contains product facts and sales terms.
    LISTING_PRODUCT_ONLY = "LISTING_PRODUCT_ONLY"  # Indicates the submitted data contains product facts only.
    LISTING_OFFER_ONLY = "LISTING_OFFER_ONLY"  # Indicates the submitted data contains sales terms only. Not supported for vendors (vendors will receive an HTTP status code 400 response).


"""
ListingsItemPutRequestBody

The request body schema for the putListingsItem operation.
"""


class ListingsItemPutRequestBody(SpApiBaseModel):
    """The request body schema for the putListingsItem operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    product_type: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("productType", "product_type"),
            serialization_alias="productType",
            description="The Amazon product type of the listings item.",
        ),
    ]

    requirements: Annotated[
        Optional[ListingsItemPutRequestBodyRequirementsEnum],
        Field(
            None, description="The name of the requirements set for the provided data."
        ),
    ]

    attributes: Annotated[
        Dict[str, Any],
        Field(
            ...,
            description="JSON object containing structured listings item attribute data keyed by attribute name.",
        ),
    ]


# Enum definitions
class ListingsItemSubmissionResponseStatusEnum(str, Enum):
    """Enum for status"""

    ACCEPTED = "ACCEPTED"  # The listings submission was accepted for processing.
    INVALID = "INVALID"  # The listings submission was not valid and was not accepted for processing.


"""
ListingsItemSubmissionResponse

Response containing the results of a submission to the Selling Partner API for Listings Items.
"""


class ListingsItemSubmissionResponse(SpApiBaseModel):
    """Response containing the results of a submission to the Selling Partner API for Listings Items."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    sku: Annotated[
        str,
        Field(
            ...,
            description="A selling partner provided identifier for an Amazon listing.",
        ),
    ]

    status: Annotated[
        ListingsItemSubmissionResponseStatusEnum,
        Field(..., description="The status of the listings item submission."),
    ]

    submission_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("submissionId", "submission_id"),
            serialization_alias="submissionId",
            description="The unique identifier of the listings item submission.",
        ),
    ]

    issues: Annotated[
        Optional[List["Issue"]],
        Field(
            None,
            description="Listings item issues related to the listings item submission.",
        ),
    ]


"""
PatchListingsItemRequest

Request parameters for patchListingsItem
"""


class PatchListingsItemRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for patchListingsItem
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    seller_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("sellerId", "seller_id"),
            serialization_alias="sellerId",
            description="[PATH] A selling partner identifier, such as a merchant account or vendor code.",
        ),
    ]

    sku: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            description="[PATH] A selling partner provided identifier for an Amazon listing.",
        ),
    ]

    marketplace_ids: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceIds", "marketplace_ids"),
            serialization_alias="marketplaceIds",
            description="[QUERY] A comma-delimited list of Amazon marketplace identifiers for the request.",
        ),
    ]

    issue_locale: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("issueLocale", "issue_locale"),
            serialization_alias="issueLocale",
            description="[QUERY] A locale for localization of issues. When not provided, the default language code of the first marketplace is used. Examples: 'en_US', 'fr_CA', 'fr_FR'. Localized messages default to 'en_US' when a localization is not available in the specified locale.",
        ),
    ]

    body: Annotated[
        "ListingsItemPatchRequestBody",
        BodyParam(),
        Field(
            ...,
            description="[BODY] The request body schema for the patchListingsItem operation.",
        ),
    ]


"""
PutListingsItemRequest

Request parameters for putListingsItem
"""


class PutListingsItemRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for putListingsItem
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    seller_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("sellerId", "seller_id"),
            serialization_alias="sellerId",
            description="[PATH] A selling partner identifier, such as a merchant account or vendor code.",
        ),
    ]

    sku: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            description="[PATH] A selling partner provided identifier for an Amazon listing.",
        ),
    ]

    marketplace_ids: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceIds", "marketplace_ids"),
            serialization_alias="marketplaceIds",
            description="[QUERY] A comma-delimited list of Amazon marketplace identifiers for the request.",
        ),
    ]

    issue_locale: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("issueLocale", "issue_locale"),
            serialization_alias="issueLocale",
            description="[QUERY] A locale for localization of issues. When not provided, the default language code of the first marketplace is used. Examples: 'en_US', 'fr_CA', 'fr_FR'. Localized messages default to 'en_US' when a localization is not available in the specified locale.",
        ),
    ]

    body: Annotated[
        "ListingsItemPutRequestBody",
        BodyParam(),
        Field(
            ...,
            description="[BODY] The request body schema for the putListingsItem operation.",
        ),
    ]


# Rebuild models to resolve forward references
Error.model_rebuild()
ErrorList.model_rebuild()
Issue.model_rebuild()
PatchOperation.model_rebuild()
ListingsItemPatchRequestBody.model_rebuild()
ListingsItemPutRequestBody.model_rebuild()
ListingsItemSubmissionResponse.model_rebuild()
DeleteListingsItemRequest.model_rebuild()
PatchListingsItemRequest.model_rebuild()
PutListingsItemRequest.model_rebuild()
