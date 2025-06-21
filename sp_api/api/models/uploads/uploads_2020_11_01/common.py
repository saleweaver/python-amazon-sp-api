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
CreateUploadDestinationForResourceRequest

Request parameters for createUploadDestinationForResource
"""


class CreateUploadDestinationForResourceRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for createUploadDestinationForResource
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    marketplace_ids: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceIds", "marketplace_ids"),
            serialization_alias="marketplaceIds",
            description="[QUERY] The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).",
        ),
    ]

    content_m_d5: Annotated[
        str,
        QueryParam(),
        Field(
            ...,
            validation_alias=AliasChoices("contentMD5", "content_m_d5"),
            serialization_alias="contentMD5",
            description="[QUERY] An MD5 hash of the content to be submitted to the upload destination. This value is used to determine if the data has been corrupted or tampered with during transit.",
        ),
    ]

    resource: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            description="[PATH] The upload destination for your resource. For example, if you create an upload destination for the `createLegalDisclosure` operation of the Messaging API, the `{resource}` would be `/messaging/v1/orders/{amazonOrderId}/messages/legalDisclosure`, and the entire path would be `/uploads/2020-11-01/uploadDestinations/messaging/v1/orders/{amazonOrderId}/messages/legalDisclosure`. If you create an upload destination for an Aplus content document, the `{resource}` would be `aplus/2020-11-01/contentDocuments` and the path would be `/uploads/2020-11-01/uploadDestinations/aplus/2020-11-01/contentDocuments`.",
        ),
    ]

    content_type: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("contentType", "content_type"),
            serialization_alias="contentType",
            description="[QUERY] The content type of the file you upload.",
        ),
    ]


ErrorList = List["Error"]
"""A list of error responses returned when a request is unsuccessful."""


"""
UploadDestination

Information about an upload destination.
"""


class UploadDestination(SpApiBaseModel):
    """Information about an upload destination."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    upload_destination_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "uploadDestinationId", "upload_destination_id"
            ),
            serialization_alias="uploadDestinationId",
            description="The unique identifier for the upload destination.",
        ),
    ]

    url: Annotated[
        Optional[str], Field(None, description="The URL for the upload destination.")
    ]

    headers: Annotated[
        Optional[Dict[str, Any]],
        Field(None, description="The headers to include in the upload request."),
    ]


"""
CreateUploadDestinationResponse

The response schema for the createUploadDestination operation.
"""


class CreateUploadDestinationResponse(SpApiBaseModel):
    """The response schema for the createUploadDestination operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["UploadDestination"],
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
            description="Additional details that can help the caller understand or fix the issue.",
        ),
    ]


# Rebuild models to resolve forward references
CreateUploadDestinationResponse.model_rebuild()
UploadDestination.model_rebuild()
Error.model_rebuild()
CreateUploadDestinationForResourceRequest.model_rebuild()
