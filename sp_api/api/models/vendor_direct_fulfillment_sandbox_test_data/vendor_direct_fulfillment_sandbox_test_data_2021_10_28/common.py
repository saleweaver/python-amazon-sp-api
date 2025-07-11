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
            description="An array of individual error objects containing error details.",
        ),
    ]


"""
PartyIdentification

The identification object for the party information. For example, warehouse code or vendor code. Please refer to specific party for more details.
"""


class PartyIdentification(SpApiBaseModel):
    """The identification object for the party information. For example, warehouse code or vendor code. Please refer to specific party for more details."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    party_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("partyId", "party_id"),
            serialization_alias="partyId",
            description="Assigned identification for the party. For example, warehouse code or vendor code. Please refer to specific party for more details.",
        ),
    ]


"""
OrderScenarioRequestBody

The party identifiers required to generate the test data.
"""


class OrderScenarioRequestBody(SpApiBaseModel):
    """The party identifiers required to generate the test data."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    selling_party: Annotated[
        "PartyIdentification",
        Field(
            ...,
            validation_alias=AliasChoices("sellingParty", "selling_party"),
            serialization_alias="sellingParty",
            description="The identifier of the selling party or vendor.",
        ),
    ]

    ship_from_party: Annotated[
        "PartyIdentification",
        Field(
            ...,
            validation_alias=AliasChoices("shipFromParty", "ship_from_party"),
            serialization_alias="shipFromParty",
            description="The warehouse code of the vendor.",
        ),
    ]


"""
GenerateOrderScenarioRequestBody

The request body for the generateOrderScenarios operation.
"""


class GenerateOrderScenarioRequestBody(SpApiBaseModel):
    """The request body for the generateOrderScenarios operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    orders: Annotated[
        Optional[List["OrderScenarioRequestBody"]],
        Field(
            None,
            description="The list of test orders requested as indicated by party identifiers.",
        ),
    ]


"""
GenerateOrderScenariosRequest

Request parameters for generateOrderScenarios
"""


class GenerateOrderScenariosRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for generateOrderScenarios
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    body: Annotated[
        "GenerateOrderScenarioRequestBody",
        BodyParam(),
        Field(
            ...,
            description="[BODY] The request payload containing parameters for generating test order data scenarios.",
        ),
    ]


"""
GetOrderScenariosRequest

Request parameters for getOrderScenarios
"""


class GetOrderScenariosRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getOrderScenarios
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
            description="[PATH] The transaction identifier returned in the response to the generateOrderScenarios operation.",
        ),
    ]


"""
Pagination

A generated string used to pass information to your next request. If NextToken is returned, pass the value of NextToken to the next request. If NextToken is not returned, there are no more order items to return.
"""


class Pagination(SpApiBaseModel):
    """A generated string used to pass information to your next request. If NextToken is returned, pass the value of NextToken to the next request. If NextToken is not returned, there are no more order items to return."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    next_token: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("nextToken", "next_token"),
            serialization_alias="nextToken",
            description="A generated token to be passed in the next request to retrieve the next set of results.",
        ),
    ]


"""
TestOrder

Error response returned when the request is unsuccessful.
"""


class TestOrder(SpApiBaseModel):
    """Error response returned when the request is unsuccessful."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    order_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("orderId", "order_id"),
            serialization_alias="orderId",
            description="An error code that identifies the type of error that occurred.",
        ),
    ]


"""
Scenario

A scenario test case response returned when the request is successful.
"""


class Scenario(SpApiBaseModel):
    """A scenario test case response returned when the request is successful."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    scenario_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("scenarioId", "scenario_id"),
            serialization_alias="scenarioId",
            description="An identifier that identifies the type of scenario that user can use for testing.",
        ),
    ]

    orders: Annotated[
        List["TestOrder"],
        Field(
            ...,
            description="A list of orders that can be used by the caller to test each life cycle or scenario.",
        ),
    ]


"""
TestCaseData

The set of test case data returned in response to the test data request.
"""


class TestCaseData(SpApiBaseModel):
    """The set of test case data returned in response to the test data request."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    scenarios: Annotated[
        Optional[List["Scenario"]],
        Field(
            None,
            description="Set of use cases that describes the possible test scenarios.",
        ),
    ]


# Enum definitions
class TransactionStatusEnum(str, Enum):
    """Enum for status"""

    FAILURE = "FAILURE"  # Transaction has failed.
    PROCESSING = "PROCESSING"  # Transaction is in process.
    SUCCESS = "SUCCESS"  # Transaction has completed successfully.


"""
Transaction

The transaction details including the status. If the transaction was successful, also includes the requested test order data.
"""


class Transaction(SpApiBaseModel):
    """The transaction details including the status. If the transaction was successful, also includes the requested test order data."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    transaction_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("transactionId", "transaction_id"),
            serialization_alias="transactionId",
            description="The unique identifier returned in the response to the generateOrderScenarios request.",
        ),
    ]

    status: Annotated[
        TransactionStatusEnum,
        Field(..., description="The current processing status of the transaction."),
    ]

    test_case_data: Annotated[
        Optional["TestCaseData"],
        Field(
            None,
            validation_alias=AliasChoices("testCaseData", "test_case_data"),
            serialization_alias="testCaseData",
            description="Test case data for the transaction. Only available when the transaction status is SUCCESS.",
        ),
    ]


"""
TransactionReference

A GUID assigned by Amazon to identify this transaction.
"""


class TransactionReference(SpApiBaseModel):
    """A GUID assigned by Amazon to identify this transaction."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    transaction_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("transactionId", "transaction_id"),
            serialization_alias="transactionId",
            description="A GUID (Globally Unique Identifier) assigned by Amazon to uniquely identify the transaction.",
        ),
    ]


"""
TransactionStatus

The payload for the getOrderScenarios operation.
"""


class TransactionStatus(SpApiBaseModel):
    """The payload for the getOrderScenarios operation."""

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


# Rebuild models to resolve forward references
GenerateOrderScenarioRequestBody.model_rebuild()
OrderScenarioRequestBody.model_rebuild()
PartyIdentification.model_rebuild()
Pagination.model_rebuild()
TransactionReference.model_rebuild()
TransactionStatus.model_rebuild()
Transaction.model_rebuild()
TestCaseData.model_rebuild()
Scenario.model_rebuild()
TestOrder.model_rebuild()
ErrorList.model_rebuild()
Error.model_rebuild()
GenerateOrderScenariosRequest.model_rebuild()
GetOrderScenariosRequest.model_rebuild()
