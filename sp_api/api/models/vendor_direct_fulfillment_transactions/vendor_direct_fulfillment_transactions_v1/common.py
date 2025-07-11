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


ErrorList = List["Error"]
"""A list of error responses returned when a request is unsuccessful."""


# Enum definitions
class TransactionStatusEnum(str, Enum):
    """Enum for status"""

    FAILURE = "Failure"  # Transaction has failed.
    PROCESSING = "Processing"  # Transaction is in process.
    SUCCESS = "Success"  # Transaction has completed successfully.


"""
Transaction

The transaction status details.
"""


class Transaction(SpApiBaseModel):
    """The transaction status details."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    transaction_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("transactionId", "transaction_id"),
            serialization_alias="transactionId",
            description="The unique identifier sent in the 'transactionId' field in response to the post request of a specific transaction.",
        ),
    ]

    status: Annotated[
        TransactionStatusEnum,
        Field(..., description="Current processing status of the transaction."),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
            description="Error code and message for the failed transaction. Only available when transaction status is 'Failure'.",
        ),
    ]


"""
TransactionStatus

The payload for the getTransactionStatus operation.
"""


class TransactionStatus(SpApiBaseModel):
    """The payload for the getTransactionStatus operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    transaction_status: Annotated[
        Optional["Transaction"],
        Field(
            None,
            validation_alias=AliasChoices("transactionStatus", "transaction_status"),
            serialization_alias="transactionStatus",
        ),
    ]


"""
GetTransactionResponse

The response schema for the getTransactionStatus operation.
"""


class GetTransactionResponse(SpApiBaseModel):
    """The response schema for the getTransactionStatus operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["TransactionStatus"],
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
GetTransactionStatusRequest

Request parameters for getTransactionStatus
"""


class GetTransactionStatusRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getTransactionStatus
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    transaction_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("transactionId", "transaction_id"),
            serialization_alias="transactionId",
            description="[PATH] Previously returned in the response to the POST request of a specific transaction.",
        ),
    ]


# Rebuild models to resolve forward references
GetTransactionResponse.model_rebuild()
TransactionStatus.model_rebuild()
Transaction.model_rebuild()
Error.model_rebuild()
GetTransactionStatusRequest.model_rebuild()
