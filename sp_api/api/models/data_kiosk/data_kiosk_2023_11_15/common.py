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
CancelQueryRequest

Request parameters for cancelQuery
"""


class CancelQueryRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for cancelQuery
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    query_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("queryId", "query_id"),
            serialization_alias="queryId",
            description="[PATH] The identifier for the query. This identifier is unique only in combination with a selling partner account ID.",
        ),
    ]


"""
CreateQuerySpecification

Information required to create the query.
"""


class CreateQuerySpecification(SpApiBaseModel):
    """Information required to create the query."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    query: Annotated[
        str,
        Field(
            ...,
            description="The GraphQL query to submit. A query must be at most 8000 characters after unnecessary whitespace is removed.",
        ),
    ]

    pagination_token: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("paginationToken", "pagination_token"),
            serialization_alias="paginationToken",
            description="A token to fetch a certain page of query results when there are multiple pages of query results available. The value of this token must be fetched from the `pagination.nextToken` field of the `Query` object, and the `query` field for this object must also be set to the `query` field of the same `Query` object. A `Query` object can be retrieved from either the `getQueries` or `getQuery` operation. In the absence of this token value, the first page of query results will be requested.",
        ),
    ]


"""
CreateQueryRequest

Request parameters for createQuery
"""


class CreateQueryRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for createQuery
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    body: Annotated[
        "CreateQuerySpecification",
        BodyParam(),
        Field(..., description="[BODY] The body of the request."),
    ]


"""
CreateQueryResponse

The response for the `createQuery` operation.
"""


class CreateQueryResponse(SpApiBaseModel):
    """The response for the `createQuery` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    query_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("queryId", "query_id"),
            serialization_alias="queryId",
            description="The identifier for the query. This identifier is unique only in combination with a selling partner account ID.",
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
            ..., description="Error response returned when the request is unsuccessful."
        ),
    ]


"""
GetDocumentRequest

Request parameters for getDocument
"""


class GetDocumentRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getDocument
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    document_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("documentId", "document_id"),
            serialization_alias="documentId",
            description="[PATH] The identifier for the Data Kiosk document.",
        ),
    ]


"""
GetDocumentResponse

The response for the `getDocument` operation.
"""


class GetDocumentResponse(SpApiBaseModel):
    """The response for the `getDocument` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    document_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("documentId", "document_id"),
            serialization_alias="documentId",
            description="The identifier for the Data Kiosk document. This identifier is unique only in combination with a selling partner account ID.",
        ),
    ]

    document_url: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("documentUrl", "document_url"),
            serialization_alias="documentUrl",
            description="A presigned URL that can be used to retrieve the Data Kiosk document. This URL expires after 5 minutes. If the Data Kiosk document is compressed, the `Content-Encoding` header will indicate the compression algorithm. **Note:** Most HTTP clients are capable of automatically decompressing downloaded files based on the `Content-Encoding` header.",
        ),
    ]


# Enum definitions
class ProcessingStatusesEnum(str, Enum):
    """Enum for processingStatuses"""

    CANCELLED = "CANCELLED"  # The query was cancelled before it began processing.
    DONE = "DONE"  # The query has completed processing.
    FATAL = "FATAL"  # The query was aborted due to a fatal error.
    IN_PROGRESS = "IN_PROGRESS"  # The query is being processed.
    IN_QUEUE = "IN_QUEUE"  # The query has not yet started processing. It may be waiting for another `IN_PROGRESS` query.


"""
GetQueriesRequest

Request parameters for getQueries
"""


class GetQueriesRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getQueries
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    processing_statuses: Annotated[
        Optional[List["ProcessingStatusesEnum"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("processingStatuses", "processing_statuses"),
            serialization_alias="processingStatuses",
            description="[QUERY] A list of processing statuses used to filter queries.",
        ),
    ]

    page_size: Annotated[
        Optional[int],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("pageSize", "page_size"),
            serialization_alias="pageSize",
            description="[QUERY] The maximum number of queries to return in a single call.",
        ),
    ]

    created_since: Annotated[
        Optional[datetime],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("createdSince", "created_since"),
            serialization_alias="createdSince",
            description="[QUERY] The earliest query creation date and time for queries to include in the response, in ISO 8601 date time format. The default is 90 days ago.",
        ),
    ]

    created_until: Annotated[
        Optional[datetime],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("createdUntil", "created_until"),
            serialization_alias="createdUntil",
            description="[QUERY] The latest query creation date and time for queries to include in the response, in ISO 8601 date time format. The default is the time of the `getQueries` request.",
        ),
    ]

    pagination_token: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("paginationToken", "pagination_token"),
            serialization_alias="paginationToken",
            description="[QUERY] A token to fetch a certain page of results when there are multiple pages of results available. The value of this token is fetched from the `pagination.nextToken` field returned in the `GetQueriesResponse` object. All other parameters must be provided with the same values that were provided with the request that generated this token, with the exception of `pageSize` which can be modified between calls to `getQueries`. In the absence of this token value, `getQueries` returns the first page of results.",
        ),
    ]


QueryList = List["Query"]
"""A list of queries."""


"""
GetQueriesResponse

The response for the `getQueries` operation.
"""


class GetQueriesResponse(SpApiBaseModel):
    """The response for the `getQueries` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    queries: Annotated["QueryList", Field(..., description="The Data Kiosk queries.")]

    pagination: Annotated[
        Optional[Dict[str, Any]],
        Field(
            None,
            description="When a request has results that are not included in this response, pagination occurs. This means the results are divided into pages. To retrieve the next page, you must pass the `nextToken` as the `paginationToken` query parameter in the subsequent `getQueries` request. All other parameters must be provided with the same values that were provided with the request that generated this token, with the exception of `pageSize` which can be modified between calls to `getQueries`. When there are no more pages to fetch, the `nextToken` field will be absent.",
        ),
    ]


"""
GetQueryRequest

Request parameters for getQuery
"""


class GetQueryRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getQuery
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    query_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("queryId", "query_id"),
            serialization_alias="queryId",
            description="[PATH] The query identifier.",
        ),
    ]


# Enum definitions
class ProcessingStatusEnum(str, Enum):
    """Enum for processingStatus"""

    CANCELLED = "CANCELLED"  # The query was cancelled before it began processing.
    DONE = "DONE"  # The query has completed processing.
    FATAL = "FATAL"  # The query was aborted due to a fatal error.
    IN_PROGRESS = "IN_PROGRESS"  # The query is being processed.
    IN_QUEUE = "IN_QUEUE"  # The query has not yet started processing. It may be waiting for another `IN_PROGRESS` query.


"""
Query

Detailed information about the query.
"""


class Query(SpApiBaseModel):
    """Detailed information about the query."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    query_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("queryId", "query_id"),
            serialization_alias="queryId",
            description="The query identifier. This identifier is unique only in combination with a selling partner account ID.",
        ),
    ]

    query: Annotated[str, Field(..., description="The submitted query.")]

    created_time: Annotated[
        datetime,
        Field(
            ...,
            validation_alias=AliasChoices("createdTime", "created_time"),
            serialization_alias="createdTime",
            description="The date and time when the query was created, in ISO 8601 date time format.",
        ),
    ]

    processing_status: Annotated[
        ProcessingStatusEnum,
        Field(
            ...,
            validation_alias=AliasChoices("processingStatus", "processing_status"),
            serialization_alias="processingStatus",
            description="The processing status of the query.",
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
            description="The date and time when the query processing started, in ISO 8601 date time format.",
        ),
    ]

    processing_end_time: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices("processingEndTime", "processing_end_time"),
            serialization_alias="processingEndTime",
            description="The date and time when the query processing completed, in ISO 8601 date time format.",
        ),
    ]

    data_document_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("dataDocumentId", "data_document_id"),
            serialization_alias="dataDocumentId",
            description="The data document identifier. This identifier is only present when there is data available as a result of the query. This identifier is unique only in combination with a selling partner account ID. Pass this identifier into the `getDocument` operation to get the information required to retrieve the data document's contents.",
        ),
    ]

    error_document_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("errorDocumentId", "error_document_id"),
            serialization_alias="errorDocumentId",
            description="The error document identifier. This identifier is only present when an error occurs during query processing. This identifier is unique only in combination with a selling partner account ID. Pass this identifier into the `getDocument` operation to get the information required to retrieve the error document's contents.",
        ),
    ]

    pagination: Annotated[
        Optional[Dict[str, Any]],
        Field(
            None,
            description="When a query produces results that are not included in the data document, pagination occurs. This means the results are divided into pages. To retrieve the next page, you must pass a `CreateQuerySpecification` object with `paginationToken` set to this object's `nextToken` and with `query` set to this object's `query` in the subsequent `createQuery` request. When there are no more pages to fetch, the `nextToken` field will be absent.",
        ),
    ]


# Rebuild models to resolve forward references
ErrorList.model_rebuild()
Error.model_rebuild()
Query.model_rebuild()
CreateQuerySpecification.model_rebuild()
CreateQueryResponse.model_rebuild()
GetQueriesResponse.model_rebuild()
GetDocumentResponse.model_rebuild()
GetQueriesRequest.model_rebuild()
CreateQueryRequest.model_rebuild()
CancelQueryRequest.model_rebuild()
GetQueryRequest.model_rebuild()
GetDocumentRequest.model_rebuild()
