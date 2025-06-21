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
CancelFeedRequest

Request parameters for cancelFeed
"""


class CancelFeedRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for cancelFeed
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    feed_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("feedId", "feed_id"),
            serialization_alias="feedId",
            description="[PATH] The identifier for the feed. This identifier is unique only in combination with a seller ID.",
        ),
    ]


"""
CreateFeedDocumentSpecification

Specifies the content type for the createFeedDocument operation.
"""


class CreateFeedDocumentSpecification(SpApiBaseModel):
    """Specifies the content type for the createFeedDocument operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    content_type: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("contentType", "content_type"),
            serialization_alias="contentType",
            description="The content type of the feed.",
        ),
    ]


"""
CreateFeedDocumentRequest

Request parameters for createFeedDocument
"""


class CreateFeedDocumentRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for createFeedDocument
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    body: Annotated[
        "CreateFeedDocumentSpecification",
        BodyParam(),
        Field(
            ...,
            description="[BODY] Specifies the content type for the createFeedDocument operation.",
        ),
    ]


"""
CreateFeedDocumentResponse

Information required to upload a feed document's contents.
"""


class CreateFeedDocumentResponse(SpApiBaseModel):
    """Information required to upload a feed document's contents."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    feed_document_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("feedDocumentId", "feed_document_id"),
            serialization_alias="feedDocumentId",
            description="The identifier of the feed document.",
        ),
    ]

    url: Annotated[
        str,
        Field(
            ...,
            description="The presigned URL for uploading the feed contents. This URL expires after 5 minutes.",
        ),
    ]


"""
FeedOptions

Additional options to control the feed. These vary by feed type.
"""


class FeedOptions(SpApiBaseModel):
    """Additional options to control the feed. These vary by feed type."""

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow",
        serialize_by_alias=True,
        arbitrary_types_allowed=True,
    )


"""
CreateFeedSpecification

Information required to create the feed.
"""


class CreateFeedSpecification(SpApiBaseModel):
    """Information required to create the feed."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    feed_type: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("feedType", "feed_type"),
            serialization_alias="feedType",
            description="The feed type.",
        ),
    ]

    marketplace_ids: Annotated[
        Optional[List["str"]],
        Field(
            None,
            validation_alias=AliasChoices("marketplaceIds", "marketplace_ids"),
            serialization_alias="marketplaceIds",
            description="A list of identifiers for marketplaces that you want the feed to be applied to.",
        ),
    ]

    input_feed_document_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices(
                "inputFeedDocumentId", "input_feed_document_id"
            ),
            serialization_alias="inputFeedDocumentId",
            description="The document identifier returned by the createFeedDocument operation. Upload the feed document contents before calling the createFeed operation.",
        ),
    ]

    feed_options: Annotated[
        Optional["FeedOptions"],
        Field(
            None,
            validation_alias=AliasChoices("feedOptions", "feed_options"),
            serialization_alias="feedOptions",
        ),
    ]


"""
CreateFeedRequest

Request parameters for createFeed
"""


class CreateFeedRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for createFeed
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    body: Annotated[
        "CreateFeedSpecification",
        BodyParam(),
        Field(..., description="[BODY] Information required to create the feed."),
    ]


"""
CreateFeedResponse

Response schema.
"""


class CreateFeedResponse(SpApiBaseModel):
    """Response schema."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    feed_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("feedId", "feed_id"),
            serialization_alias="feedId",
            description="The identifier for the feed. This identifier is unique only in combination with a seller ID.",
        ),
    ]


"""
Error

An error response returned when the request is unsuccessful.
"""


class Error(SpApiBaseModel):
    """An error response returned when the request is unsuccessful."""

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
            description="An error response returned when the request is unsuccessful.",
        ),
    ]


# Enum definitions
class ProcessingStatusEnum(str, Enum):
    """Enum for processingStatus"""

    CANCELLED = "CANCELLED"  # The feed was cancelled before it started processing.
    DONE = "DONE"  # The feed has completed processing. Examine the contents of the result document to determine if there were any errors during processing.
    FATAL = "FATAL"  # The feed was aborted due to a fatal error. Some, none, or all of the operations within the feed may have completed successfully.
    IN_PROGRESS = "IN_PROGRESS"  # The feed is being processed.
    IN_QUEUE = "IN_QUEUE"  # The feed has not yet started processing. It may be waiting for another IN_PROGRESS feed.


"""
Feed

Detailed information about the feed.
"""


class Feed(SpApiBaseModel):
    """Detailed information about the feed."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    feed_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("feedId", "feed_id"),
            serialization_alias="feedId",
            description="The identifier for the feed. This identifier is unique only in combination with a seller ID.",
        ),
    ]

    feed_type: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("feedType", "feed_type"),
            serialization_alias="feedType",
            description="The feed type.",
        ),
    ]

    marketplace_ids: Annotated[
        Optional[List["str"]],
        Field(
            None,
            validation_alias=AliasChoices("marketplaceIds", "marketplace_ids"),
            serialization_alias="marketplaceIds",
            description="A list of identifiers for the marketplaces that the feed is applied to.",
        ),
    ]

    created_time: Annotated[
        datetime,
        Field(
            ...,
            validation_alias=AliasChoices("createdTime", "created_time"),
            serialization_alias="createdTime",
            description="The date and time when the feed was created, in ISO 8601 date time format.",
        ),
    ]

    processing_status: Annotated[
        ProcessingStatusEnum,
        Field(
            ...,
            validation_alias=AliasChoices("processingStatus", "processing_status"),
            serialization_alias="processingStatus",
            description="The processing status of the feed.",
        ),
    ]

    processing_start_time: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices(
                "processingStartTime", "processing_start_time"
            ),
            serialization_alias="processingStartTime",
            description="The date and time when feed processing started, in ISO 8601 date time format.",
        ),
    ]

    processing_end_time: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices("processingEndTime", "processing_end_time"),
            serialization_alias="processingEndTime",
            description="The date and time when feed processing completed, in ISO 8601 date time format.",
        ),
    ]

    result_feed_document_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "resultFeedDocumentId", "result_feed_document_id"
            ),
            serialization_alias="resultFeedDocumentId",
            description="The identifier for the feed document. This identifier is unique only in combination with a seller ID.",
        ),
    ]


# Enum definitions
class CompressionAlgorithmEnum(str, Enum):
    """Enum for compressionAlgorithm"""

    GZIP = "GZIP"  # The gzip compression algorithm.


"""
FeedDocument

Information required for the feed document.
"""


class FeedDocument(SpApiBaseModel):
    """Information required for the feed document."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    feed_document_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("feedDocumentId", "feed_document_id"),
            serialization_alias="feedDocumentId",
            description="The identifier for the feed document. This identifier is unique only in combination with a seller ID.",
        ),
    ]

    url: Annotated[
        str,
        Field(
            ...,
            description="A presigned URL for the feed document. If `compressionAlgorithm` is not returned, you can download the feed directly from this URL. This URL expires after 5 minutes.",
        ),
    ]

    compression_algorithm: Annotated[
        Optional[CompressionAlgorithmEnum],
        Field(
            None,
            validation_alias=AliasChoices(
                "compressionAlgorithm", "compression_algorithm"
            ),
            serialization_alias="compressionAlgorithm",
            description="If the feed document contents have been compressed, the compression algorithm used is returned in this property and you must decompress the feed when you download. Otherwise, you can download the feed directly. Refer to [Step 7. Download the feed processing report](doc:feeds-api-v2021-06-30-use-case-guide#step-7-download-the-feed-processing-report) in the use case guide, where sample code is provided.",
        ),
    ]


FeedList = List["Feed"]
"""A list of feeds."""


"""
GetFeedDocumentRequest

Request parameters for getFeedDocument
"""


class GetFeedDocumentRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getFeedDocument
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    feed_document_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("feedDocumentId", "feed_document_id"),
            serialization_alias="feedDocumentId",
            description="[PATH] The identifier of the feed document.",
        ),
    ]


"""
GetFeedRequest

Request parameters for getFeed
"""


class GetFeedRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getFeed
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    feed_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("feedId", "feed_id"),
            serialization_alias="feedId",
            description="[PATH] The identifier for the feed. This identifier is unique only in combination with a seller ID.",
        ),
    ]


# Enum definitions
class ProcessingStatusesEnum(str, Enum):
    """Enum for processingStatuses"""

    CANCELLED = "CANCELLED"  # The feed was cancelled before it started processing.
    DONE = "DONE"  # The feed has completed processing. Examine the contents of the result document to determine if there were any errors during processing.
    FATAL = "FATAL"  # The feed was aborted due to a fatal error. Some, none, or all of the operations within the feed may have completed successfully.
    IN_PROGRESS = "IN_PROGRESS"  # The feed is being processed.
    IN_QUEUE = "IN_QUEUE"  # The feed has not yet started processing. It may be waiting for another IN_PROGRESS feed.


"""
GetFeedsRequest

Request parameters for getFeeds
"""


class GetFeedsRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getFeeds
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    feed_types: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("feedTypes", "feed_types"),
            serialization_alias="feedTypes",
            description="[QUERY] A list of feed types used to filter feeds. When feedTypes is provided, the other filter parameters (processingStatuses, marketplaceIds, createdSince, createdUntil) and pageSize may also be provided. Either feedTypes or nextToken is required.",
        ),
    ]

    marketplace_ids: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceIds", "marketplace_ids"),
            serialization_alias="marketplaceIds",
            description="[QUERY] A list of marketplace identifiers used to filter feeds. The feeds returned will match at least one of the marketplaces that you specify.",
        ),
    ]

    page_size: Annotated[
        Optional[int],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("pageSize", "page_size"),
            serialization_alias="pageSize",
            description="[QUERY] The maximum number of feeds to return in a single call.",
        ),
    ]

    processing_statuses: Annotated[
        Optional[List["ProcessingStatusesEnum"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("processingStatuses", "processing_statuses"),
            serialization_alias="processingStatuses",
            description="[QUERY] A list of processing statuses used to filter feeds.",
        ),
    ]

    created_since: Annotated[
        Optional[datetime],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("createdSince", "created_since"),
            serialization_alias="createdSince",
            description="[QUERY] The earliest feed creation date and time for feeds included in the response, in ISO 8601 format. The default is 90 days ago. Feeds are retained for a maximum of 90 days.",
        ),
    ]

    created_until: Annotated[
        Optional[datetime],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("createdUntil", "created_until"),
            serialization_alias="createdUntil",
            description="[QUERY] The latest feed creation date and time for feeds included in the response, in ISO 8601 format. The default is now.",
        ),
    ]

    next_token: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("nextToken", "next_token"),
            serialization_alias="nextToken",
            description="[QUERY] A string token returned in the response to your previous request. nextToken is returned when the number of results exceeds the specified pageSize value. To get the next page of results, call the getFeeds operation and include this token as the only parameter. Specifying nextToken with any other parameters will cause the request to fail.",
        ),
    ]


"""
GetFeedsResponse

Response schema.
"""


class GetFeedsResponse(SpApiBaseModel):
    """Response schema."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    feeds: Annotated["FeedList", Field(..., description="The feeds.")]

    next_token: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("nextToken", "next_token"),
            serialization_alias="nextToken",
            description="Returned when the number of results exceeds pageSize. To get the next page of results, call the getFeeds operation with this token as the only parameter.",
        ),
    ]


# Rebuild models to resolve forward references
Error.model_rebuild()
ErrorList.model_rebuild()
CreateFeedResponse.model_rebuild()
Feed.model_rebuild()
GetFeedsResponse.model_rebuild()
FeedDocument.model_rebuild()
FeedOptions.model_rebuild()
CreateFeedSpecification.model_rebuild()
CreateFeedDocumentSpecification.model_rebuild()
CreateFeedDocumentResponse.model_rebuild()
GetFeedsRequest.model_rebuild()
CreateFeedRequest.model_rebuild()
CancelFeedRequest.model_rebuild()
GetFeedRequest.model_rebuild()
CreateFeedDocumentRequest.model_rebuild()
GetFeedDocumentRequest.model_rebuild()
