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

AssignmentType = str
"""The default payment method type."""


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

    errors: Annotated[List["Error"], Field(..., description="array of errors")]


"""
ExpiryDate

The expiration date of the card used for payment. If the payment method is not `card`, the expiration date is `null`.
"""


class ExpiryDate(SpApiBaseModel):
    """The expiration date of the card used for payment. If the payment method is not `card`, the expiration date is `null`."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    month: Annotated[
        Optional[str],
        Field(
            None,
            description="The month the card expires expressed as a number from `1` to `12`.",
        ),
    ]

    year: Annotated[Optional[str], Field(None, description="Year")]


# Enum definitions
class GetPaymentMethodsRequestPaymentMethodTypesEnum(str, Enum):
    """Enum for paymentMethodTypes"""

    BANK_ACCOUNT = "BANK_ACCOUNT"  # The payment is from a bank account.
    CARD = "CARD"  # The payment is from a card.
    SELLER_WALLET = "SELLER_WALLET"  # The payment is from a [Seller Wallet](https://sell.amazon.com/tools/seller-wallet) virtual bank account.


"""
GetPaymentMethodsRequest

Request parameters for getPaymentMethods
"""


class GetPaymentMethodsRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getPaymentMethods
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    marketplace_id: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="[QUERY] The identifier of the marketplace from which you want to retrieve payment methods. For the list of possible marketplace identifiers, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).",
        ),
    ]

    payment_method_types: Annotated[
        Optional[List["GetPaymentMethodsRequestPaymentMethodTypesEnum"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("paymentMethodTypes", "payment_method_types"),
            serialization_alias="paymentMethodTypes",
            description="[QUERY] A comma-separated list of the payment method types you want to include in the response.",
        ),
    ]


PaymentMethodList = List["PaymentMethodDetails"]
"""The list of payment methods with payment method details."""


"""
GetPaymentMethodsResponse

The response schema for the `getPaymentMethods` operation.
"""


class GetPaymentMethodsResponse(SpApiBaseModel):
    """The response schema for the `getPaymentMethods` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payment_methods: Annotated[
        Optional["PaymentMethodList"],
        Field(
            None,
            validation_alias=AliasChoices("paymentMethods", "payment_methods"),
            serialization_alias="paymentMethods",
        ),
    ]


MarketplaceId = str
"""The identifier of the Amazon marketplace. For the list of all marketplace IDs, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids)."""


"""
InitiatePayoutRequestBody

The request schema for the `initiatePayout` operation.
"""


class InitiatePayoutRequestBody(SpApiBaseModel):
    """The request schema for the `initiatePayout` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    marketplace_id: Annotated[
        Optional["MarketplaceId"],
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="The identifier of the Amazon marketplace. This API supports the following marketplaces: DE, FR, IT, ES, SE, NL, PL, and BE. For a list of possible marketplace IDs, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).",
        ),
    ]

    account_type: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("accountType", "account_type"),
            serialization_alias="accountType",
            description="The account type in the selected marketplace for which a payout must be initiated. For supported EU marketplaces, the only account type is `Standard Orders`.",
        ),
    ]


"""
InitiatePayoutRequest

Request parameters for initiatePayout
"""


class InitiatePayoutRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for initiatePayout
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    body: Annotated[
        "InitiatePayoutRequestBody",
        BodyParam(),
        Field(
            ...,
            description="[BODY] The request body for the `initiatePayout` operation.",
        ),
    ]


"""
InitiatePayoutResponse

The response schema for the `initiatePayout` operation.
"""


class InitiatePayoutResponse(SpApiBaseModel):
    """The response schema for the `initiatePayout` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payout_reference_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("payoutReferenceId", "payout_reference_id"),
            serialization_alias="payoutReferenceId",
            description="The financial event group ID for a successfully initiated payout. You can use this ID to track payout information.",
        ),
    ]


PaymentMethodType = str
"""The type of payment method."""


"""
PaymentMethodDetails

The details of a payment method.
"""


class PaymentMethodDetails(SpApiBaseModel):
    """The details of a payment method."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    account_holder_name: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("accountHolderName", "account_holder_name"),
            serialization_alias="accountHolderName",
            description="The name of the account holder who is registered for the payment method.",
        ),
    ]

    payment_method_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("paymentMethodId", "payment_method_id"),
            serialization_alias="paymentMethodId",
            description="The payment method identifier.",
        ),
    ]

    tail: Annotated[
        Optional[str],
        Field(None, description="The last three or four digits of the payment method."),
    ]

    expiry_date: Annotated[
        Optional["ExpiryDate"],
        Field(
            None,
            validation_alias=AliasChoices("expiryDate", "expiry_date"),
            serialization_alias="expiryDate",
            description="The expiration date of the card used for payment.",
        ),
    ]

    country_code: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("countryCode", "country_code"),
            serialization_alias="countryCode",
            description="The two-letter country code in ISO 3166-1 alpha-2 format. For payment methods in the `card` category, the code is for the country where the card was issued. For payment methods in the `bank account` category, the code is for the country where the account is located.",
        ),
    ]

    payment_method_type: Annotated[
        Optional["PaymentMethodType"],
        Field(
            None,
            validation_alias=AliasChoices("paymentMethodType", "payment_method_type"),
            serialization_alias="paymentMethodType",
            description="The payment method type.",
        ),
    ]

    assignment_type: Annotated[
        Optional["AssignmentType"],
        Field(
            None,
            validation_alias=AliasChoices("assignmentType", "assignment_type"),
            serialization_alias="assignmentType",
            description="The payment method assignment type, whether it is assigned as default to the given marketplace or not.",
        ),
    ]


PaymentMethodTypeList = List["PaymentMethodType"]
"""The list of payment method types that are present."""


# Rebuild models to resolve forward references
InitiatePayoutRequestBody.model_rebuild()
InitiatePayoutResponse.model_rebuild()
GetPaymentMethodsResponse.model_rebuild()
PaymentMethodDetails.model_rebuild()
ExpiryDate.model_rebuild()
ErrorList.model_rebuild()
Error.model_rebuild()
InitiatePayoutRequest.model_rebuild()
GetPaymentMethodsRequest.model_rebuild()
