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
AccountHolderAddress

The Address used to verify the bank account of the payee. This can be a person or business mailing address.
"""


class AccountHolderAddress(SpApiBaseModel):
    """The Address used to verify the bank account of the payee. This can be a person or business mailing address."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    address_line1: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("addressLine1", "address_line1"),
            serialization_alias="addressLine1",
            description="Address Line 1 of the public address.",
        ),
    ]

    address_line2: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("addressLine2", "address_line2"),
            serialization_alias="addressLine2",
            description="Address Line 2 of the public address.",
        ),
    ]

    city: Annotated[str, Field(..., description="City name of the public address.")]

    state: Annotated[
        str,
        Field(
            ...,
            description="State name of the public address. This will be state or region for CN (China) based addresses.",
        ),
    ]

    postal_code: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("postalCode", "postal_code"),
            serialization_alias="postalCode",
            description="Postal code of the public address.",
        ),
    ]

    country: Annotated[
        Optional[str], Field(None, description="Country name of the public address.")
    ]

    country_code: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("countryCode", "country_code"),
            serialization_alias="countryCode",
            description="The two digit country code, in ISO 3166 format.",
        ),
    ]


BalanceType = str
"""The type of bank account balance."""


BigDecimal = float
"""A decimal number, such as an amount or FX rate."""


"""
Balance

The balance amount in the Amazon Seller Wallet bank account.
"""


class Balance(SpApiBaseModel):
    """The balance amount in the Amazon Seller Wallet bank account."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    account_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("accountId", "account_id"),
            serialization_alias="accountId",
            description="The unique identifier provided by Amazon to identify the account.",
        ),
    ]

    balance_type: Annotated[
        Optional["BalanceType"],
        Field(
            None,
            validation_alias=AliasChoices("balanceType", "balance_type"),
            serialization_alias="balanceType",
            description="The type of balance.",
        ),
    ]

    balance_amount: Annotated[
        "BigDecimal",
        Field(
            ...,
            validation_alias=AliasChoices("balanceAmount", "balance_amount"),
            serialization_alias="balanceAmount",
            description="The balance amount in number format.",
        ),
    ]

    balance_currency: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("balanceCurrency", "balance_currency"),
            serialization_alias="balanceCurrency",
            description="The Amazon Seller Wallet bank account currency code in ISO 4217 format.",
        ),
    ]

    last_update_date: Annotated[
        datetime,
        Field(
            ...,
            validation_alias=AliasChoices("lastUpdateDate", "last_update_date"),
            serialization_alias="lastUpdateDate",
            description="The date of the most recent account balance update.",
        ),
    ]


"""
BalanceListing

A list of balances in the seller account.
"""


class BalanceListing(SpApiBaseModel):
    """A list of balances in the seller account."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    balances: Annotated[
        Optional[List["Balance"]],
        Field(None, description="A list of balances in the seller account."),
    ]


BankAccountHolderStatus = str
"""The status of the Amazon Seller Wallet account holder."""


BankAccountNumberFormat = str
"""The bank account's format type."""


BankAccountOwnershipType = str
"""The destination bank account's ownership type."""


BankNumberFormat = str
"""The format of the bank number. Also known as the routing number type."""


"""
BankAccount

Details of an Amazon Seller Wallet bank account. This account is used to hold the money that a Seller Wallet customer earns by selling items.
"""


class BankAccount(SpApiBaseModel):
    """Details of an Amazon Seller Wallet bank account. This account is used to hold the money that a Seller Wallet customer earns by selling items."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    account_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("accountId", "account_id"),
            serialization_alias="accountId",
            description="The unique identifier provided by Amazon to identify the account.",
        ),
    ]

    account_holder_name: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("accountHolderName", "account_holder_name"),
            serialization_alias="accountHolderName",
            description="The bank account holder's name (expected to be an Amazon customer).",
        ),
    ]

    bank_account_number_format: Annotated[
        "BankAccountNumberFormat",
        Field(
            ...,
            validation_alias=AliasChoices(
                "bankAccountNumberFormat", "bank_account_number_format"
            ),
            serialization_alias="bankAccountNumberFormat",
            description="The format in which the bank account number is provided.",
        ),
    ]

    bank_name: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("bankName", "bank_name"),
            serialization_alias="bankName",
            description="The name of the bank. This value is Amazon Seller Wallet for Amazon Seller Wallet accounts.",
        ),
    ]

    bank_account_ownership_type: Annotated[
        "BankAccountOwnershipType",
        Field(
            ...,
            validation_alias=AliasChoices(
                "bankAccountOwnershipType", "bank_account_ownership_type"
            ),
            serialization_alias="bankAccountOwnershipType",
            description="Type of ownership of the bank account. This value is SELF for Amazon Seller Wallet accounts.",
        ),
    ]

    routing_number: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("routingNumber", "routing_number"),
            serialization_alias="routingNumber",
            description="Routing number for automated clearing house transfers. This value is nine consecutive zeros for Amazon Seller Wallet accounts.",
        ),
    ]

    bank_number_format: Annotated[
        "BankNumberFormat",
        Field(
            ...,
            validation_alias=AliasChoices("bankNumberFormat", "bank_number_format"),
            serialization_alias="bankNumberFormat",
            description="Bank number format or routing number type.",
        ),
    ]

    account_country_code: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("accountCountryCode", "account_country_code"),
            serialization_alias="accountCountryCode",
            description="The two-digit country code in ISO 3166 format.",
        ),
    ]

    account_currency: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("accountCurrency", "account_currency"),
            serialization_alias="accountCurrency",
            description="Bank account currency code in ISO 4217 format.",
        ),
    ]

    bank_account_number_tail: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices(
                "bankAccountNumberTail", "bank_account_number_tail"
            ),
            serialization_alias="bankAccountNumberTail",
            description="The last 3 digit of the bank account number. This value is three consecutive zeros for Amazon Seller Wallet accounts.",
        ),
    ]

    bank_account_holder_status: Annotated[
        Optional["BankAccountHolderStatus"],
        Field(
            None,
            validation_alias=AliasChoices(
                "bankAccountHolderStatus", "bank_account_holder_status"
            ),
            serialization_alias="bankAccountHolderStatus",
            description="The compliance status of the bank account holder.",
        ),
    ]


"""
BankAccountListing

A list of bank accounts.
"""


class BankAccountListing(SpApiBaseModel):
    """A list of bank accounts."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    accounts: Annotated[
        List["BankAccount"], Field(..., description="A list of bank accounts.")
    ]


"""
Currency

A currency type and amount.
"""


class Currency(SpApiBaseModel):
    """A currency type and amount."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    currency_code: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("currencyCode", "currency_code"),
            serialization_alias="currencyCode",
            description="The three-digit currency code in ISO 4217 format.",
        ),
    ]

    currency_amount: Annotated[
        Optional["BigDecimal"],
        Field(
            None,
            validation_alias=AliasChoices("currencyAmount", "currency_amount"),
            serialization_alias="currencyAmount",
            description="The monetary value.",
        ),
    ]


"""
TransactionInstrumentDetails

Details of the destination bank account in the transaction request.
"""


class TransactionInstrumentDetails(SpApiBaseModel):
    """Details of the destination bank account in the transaction request."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    bank_account: Annotated[
        "BankAccount",
        Field(
            ...,
            validation_alias=AliasChoices("bankAccount", "bank_account"),
            serialization_alias="bankAccount",
            description="Details of the destination bank account.",
        ),
    ]

    bank_account_number: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("bankAccountNumber", "bank_account_number"),
            serialization_alias="bankAccountNumber",
            description="The bank account number of the destination payment method. **Note:** This field is encrypted before Amazon receives it, so should not be used to generate `destAccountDigitalSignature`, and should not be included in the request signature.",
        ),
    ]


FeeType = str
"""The type of fee on the transaction."""


"""
Fee

Details of the fee.
"""


class Fee(SpApiBaseModel):
    """Details of the fee."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    fee_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("feeId", "fee_id"),
            serialization_alias="feeId",
            description="The unique identifier assigned to the fee.",
        ),
    ]

    fee_type: Annotated[
        "FeeType",
        Field(
            ...,
            validation_alias=AliasChoices("feeType", "fee_type"),
            serialization_alias="feeType",
            description="The type of the fee.",
        ),
    ]

    fee_rate_value: Annotated[
        "BigDecimal",
        Field(
            ...,
            validation_alias=AliasChoices("feeRateValue", "fee_rate_value"),
            serialization_alias="feeRateValue",
            description="The value of the fee in percentage format.",
        ),
    ]

    fee_amount: Annotated[
        "Currency",
        Field(
            ...,
            validation_alias=AliasChoices("feeAmount", "fee_amount"),
            serialization_alias="feeAmount",
            description="The actual value of the fee in numeric format.",
        ),
    ]


RateDirection = str
"""Whether the customer is buying or selling the source currency."""


"""
FxRateDetails

Foreign exchange rate details.
"""


class FxRateDetails(SpApiBaseModel):
    """Foreign exchange rate details."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    fx_rate_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("fxRateId", "fx_rate_id"),
            serialization_alias="fxRateId",
            description="The unique identifier assigned to the fees / foreign exchange rate of a transaction.",
        ),
    ]

    base_rate: Annotated[
        "BigDecimal",
        Field(
            ...,
            validation_alias=AliasChoices("baseRate", "base_rate"),
            serialization_alias="baseRate",
            description="The market foreign exchange rate.",
        ),
    ]

    effective_fx_rate: Annotated[
        "BigDecimal",
        Field(
            ...,
            validation_alias=AliasChoices("effectiveFxRate", "effective_fx_rate"),
            serialization_alias="effectiveFxRate",
            description="The total rate applied to the money transfer. This includes all exchange rates, markups, and fees.",
        ),
    ]

    rate_direction: Annotated[
        "RateDirection",
        Field(
            ...,
            validation_alias=AliasChoices("rateDirection", "rate_direction"),
            serialization_alias="rateDirection",
            description="Whether the customer is buying or selling the source currency.",
        ),
    ]


"""
TransferRatePreview

The fees and foreign exchange rates applied to the transaction. If the fees are in terms of the `baseAmount` (source account) currency, then the effective rate is equal to **1 - (fees * `baseRate` / `baseAmount`)**. If the fees are in terms of the `transferAmount` (destination account) currency, then the effective rate is equal to **`baseRate` - (fees / `baseAmount`)**. In the preceding expressions, **fees** is equal to the sum of all `feeAmount.currencyAmount` values in the `fees` array.
"""


class TransferRatePreview(SpApiBaseModel):
    """The fees and foreign exchange rates applied to the transaction. If the fees are in terms of the `baseAmount` (source account) currency, then the effective rate is equal to **1 - (fees * `baseRate` / `baseAmount`)**. If the fees are in terms of the `transferAmount` (destination account) currency, then the effective rate is equal to **`baseRate` - (fees / `baseAmount`)**. In the preceding expressions, **fees** is equal to the sum of all `feeAmount.currencyAmount` values in the `fees` array."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    base_amount: Annotated[
        "Currency",
        Field(
            ...,
            validation_alias=AliasChoices("baseAmount", "base_amount"),
            serialization_alias="baseAmount",
            description="The base amount of the transaction.",
        ),
    ]

    fx_rate_details: Annotated[
        "FxRateDetails",
        Field(
            ...,
            validation_alias=AliasChoices("fxRateDetails", "fx_rate_details"),
            serialization_alias="fxRateDetails",
            description="The foreign exchange rate value of the transaction.",
        ),
    ]

    transfer_amount: Annotated[
        "Currency",
        Field(
            ...,
            validation_alias=AliasChoices("transferAmount", "transfer_amount"),
            serialization_alias="transferAmount",
            description="The final amount transferred, which includes both the fee deduction and currency conversion rate.",
        ),
    ]

    fees: Annotated[List["Fee"], Field(..., description="A list of fees.")]


"""
TransactionInitiationRequestBody

RequestBody body to initiate a transaction from a Seller Wallet bank account to another customer-defined bank account.
"""


class TransactionInitiationRequestBody(SpApiBaseModel):
    """RequestBody body to initiate a transaction from a Seller Wallet bank account to another customer-defined bank account."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    source_account_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("sourceAccountId", "source_account_id"),
            serialization_alias="sourceAccountId",
            description="The unique identifier of the source Amazon Seller Wallet bank account from which the money is debited.",
        ),
    ]

    destination_account_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "destinationAccountId", "destination_account_id"
            ),
            serialization_alias="destinationAccountId",
            description="The unique identifier of the destination bank account where the money is deposited.",
        ),
    ]

    description: Annotated[
        str, Field(..., description="A description of the transaction.")
    ]

    destination_transaction_instrument: Annotated[
        "TransactionInstrumentDetails",
        Field(
            ...,
            validation_alias=AliasChoices(
                "destinationTransactionInstrument", "destination_transaction_instrument"
            ),
            serialization_alias="destinationTransactionInstrument",
            description="Details of the destination bank account in the transaction request.",
        ),
    ]

    destination_account_holder_address: Annotated[
        Optional["AccountHolderAddress"],
        Field(
            None,
            validation_alias=AliasChoices(
                "destinationAccountHolderAddress", "destination_account_holder_address"
            ),
            serialization_alias="destinationAccountHolderAddress",
            description="The address used to verify the bank account of the payee. This can be a person or business mailing address.",
        ),
    ]

    source_amount: Annotated[
        "Currency",
        Field(
            ...,
            validation_alias=AliasChoices("sourceAmount", "source_amount"),
            serialization_alias="sourceAmount",
            description="The transaction amount in the source account's currency format. Requests that use a currency other than source bank account currency will fail.",
        ),
    ]

    transfer_rate_details: Annotated[
        Optional["TransferRatePreview"],
        Field(
            None,
            validation_alias=AliasChoices(
                "transferRateDetails", "transfer_rate_details"
            ),
            serialization_alias="transferRateDetails",
            description="The fees and foreign exchange rates applied to the transaction. Transfer Rate Preview is currently optional. This field is required when the third party honors the fees and rates of the Seller Wallet transaction.",
        ),
    ]

    request_time: Annotated[
        datetime,
        Field(
            ...,
            validation_alias=AliasChoices("requestTime", "request_time"),
            serialization_alias="requestTime",
            description="The time at which the transaction was initiated in [ISO 8601 date time format](https://developer-docs.amazon.com/sp-api/docs/iso-8601).",
        ),
    ]


"""
CreateTransactionRequest

Request parameters for createTransaction
"""


class CreateTransactionRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for createTransaction
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    body: Annotated[
        "TransactionInitiationRequestBody",
        BodyParam(),
        Field(..., description="[BODY] The payload of the request"),
    ]


PaymentPreferencePaymentType = str
"""The type of payment preference."""


"""
PaymentPreference

The type of payment preference in which the transfer is being scheduled.
"""


class PaymentPreference(SpApiBaseModel):
    """The type of payment preference in which the transfer is being scheduled."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payment_preference_payment_type: Annotated[
        "PaymentPreferencePaymentType",
        Field(
            ...,
            validation_alias=AliasChoices(
                "paymentPreferencePaymentType", "payment_preference_payment_type"
            ),
            serialization_alias="paymentPreferencePaymentType",
            description="The preferred payment type for the scheduled transaction. Can be `PERCENTAGE` or `AMOUNT`.",
        ),
    ]

    value: Annotated[
        "BigDecimal", Field(..., description="The value of the payment preference.")
    ]


TransactionType = str
"""The type of transaction."""


RecurringFrequency = str
"""The frequency at which the transaction is repeated."""


ScheduleExpressionType = str
"""The type of scheduled transfer expression."""


"""
ScheduleExpression

The configuration of the schedule.
"""


class ScheduleExpression(SpApiBaseModel):
    """The configuration of the schedule."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    schedule_expression_type: Annotated[
        "ScheduleExpressionType",
        Field(
            ...,
            validation_alias=AliasChoices(
                "scheduleExpressionType", "schedule_expression_type"
            ),
            serialization_alias="scheduleExpressionType",
            description="The type of the scheduled transfer.",
        ),
    ]

    recurring_frequency: Annotated[
        Optional["RecurringFrequency"],
        Field(
            None,
            validation_alias=AliasChoices("recurringFrequency", "recurring_frequency"),
            serialization_alias="recurringFrequency",
            description="How often the scheduled transfer happens. This field is required if `scheduleExpressionType` is `RECURRING`; otherwise it should be empty.",
        ),
    ]


ScheduleTransferType = str
"""The type of schedule the transfer is on. Schedules based on time patterns use EventBridge."""


"""
TransferScheduleInformation

Mandatory information for initiating a schedule transfer.
"""


class TransferScheduleInformation(SpApiBaseModel):
    """Mandatory information for initiating a schedule transfer."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    schedule_start_date: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices("scheduleStartDate", "schedule_start_date"),
            serialization_alias="scheduleStartDate",
            description="The start date of the scheduled transfer.",
        ),
    ]

    schedule_end_date: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices("scheduleEndDate", "schedule_end_date"),
            serialization_alias="scheduleEndDate",
            description="The end date of the scheduled transfer.",
        ),
    ]

    schedule_expression: Annotated[
        Optional["ScheduleExpression"],
        Field(
            None,
            validation_alias=AliasChoices("scheduleExpression", "schedule_expression"),
            serialization_alias="scheduleExpression",
            description="How often the scheduled transfer repeats.",
        ),
    ]

    schedule_type: Annotated[
        Optional["ScheduleTransferType"],
        Field(
            None,
            validation_alias=AliasChoices("scheduleType", "schedule_type"),
            serialization_alias="scheduleType",
            description="The type of schedule.",
        ),
    ]


TransferScheduleStatus = str
"""The schedule status of the transfer."""


"""
TransferScheduleRequestBody

RequestBody body to initiate a scheduled transfer from a Seller Wallet bank account to another customer-defined bank account.
"""


class TransferScheduleRequestBody(SpApiBaseModel):
    """RequestBody body to initiate a scheduled transfer from a Seller Wallet bank account to another customer-defined bank account."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    source_account_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("sourceAccountId", "source_account_id"),
            serialization_alias="sourceAccountId",
            description="The unique identifier of the source Amazon Seller Wallet bank account from which money is debited.",
        ),
    ]

    source_currency_code: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("sourceCurrencyCode", "source_currency_code"),
            serialization_alias="sourceCurrencyCode",
            description="The three-letter currency code of the source payment method country, in ISO 4217 format.",
        ),
    ]

    destination_account_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices(
                "destinationAccountId", "destination_account_id"
            ),
            serialization_alias="destinationAccountId",
            description="The unique identifier of the destination bank account where the money is deposited.",
        ),
    ]

    destination_transaction_instrument: Annotated[
        "TransactionInstrumentDetails",
        Field(
            ...,
            validation_alias=AliasChoices(
                "destinationTransactionInstrument", "destination_transaction_instrument"
            ),
            serialization_alias="destinationTransactionInstrument",
            description="Details of the destination bank account in the transaction request.",
        ),
    ]

    transaction_type: Annotated[
        "TransactionType",
        Field(
            ...,
            validation_alias=AliasChoices("transactionType", "transaction_type"),
            serialization_alias="transactionType",
            description="The type of the scheduled transaction.",
        ),
    ]

    transfer_schedule_information: Annotated[
        "TransferScheduleInformation",
        Field(
            ...,
            validation_alias=AliasChoices(
                "transferScheduleInformation", "transfer_schedule_information"
            ),
            serialization_alias="transferScheduleInformation",
            description="The configuration of the scheduled transfer.",
        ),
    ]

    payment_preference: Annotated[
        "PaymentPreference",
        Field(
            ...,
            validation_alias=AliasChoices("paymentPreference", "payment_preference"),
            serialization_alias="paymentPreference",
            description="The payment preference of the scheduled transfer.",
        ),
    ]

    transfer_schedule_status: Annotated[
        Optional["TransferScheduleStatus"],
        Field(
            None,
            validation_alias=AliasChoices(
                "transferScheduleStatus", "transfer_schedule_status"
            ),
            serialization_alias="transferScheduleStatus",
            description="The type of transaction schedule. This field is required when you update a transfer schedule.",
        ),
    ]


"""
CreateTransferScheduleRequest

Request parameters for createTransferSchedule
"""


class CreateTransferScheduleRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for createTransferSchedule
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    body: Annotated[
        "TransferScheduleRequestBody",
        BodyParam(),
        Field(..., description="[BODY] The payload of the request."),
    ]


"""
DeleteScheduleTransactionRequest

Request parameters for deleteScheduleTransaction
"""


class DeleteScheduleTransactionRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for deleteScheduleTransaction
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    transfer_schedule_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("transferScheduleId", "transfer_schedule_id"),
            serialization_alias="transferScheduleId",
            description="[PATH] A unique reference ID for a scheduled transfer.",
        ),
    ]


"""
DeleteTransferSchedule

The response returned when the schedule transfer's delete request is successful.
"""


class DeleteTransferSchedule(SpApiBaseModel):
    """The response returned when the schedule transfer's delete request is successful."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    code: Annotated[
        str,
        Field(
            ...,
            description="A success code that specifies that the delete operation was successful. For example, HTTP 200.",
        ),
    ]

    message: Annotated[
        str,
        Field(
            ...,
            description="A message that describes the success condition of the delete schedule transaction.",
        ),
    ]

    details: Annotated[
        Optional[str],
        Field(
            None,
            description="Additional details that can help the caller understand the operation execution.",
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

    errors: Annotated[List["Error"], Field(..., description="List of errors")]


"""
GetAccountRequest

Request parameters for getAccount
"""


class GetAccountRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getAccount
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    account_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("accountId", "account_id"),
            serialization_alias="accountId",
            description="[PATH] The ID of the Amazon Seller Wallet account.",
        ),
    ]


"""
GetTransactionRequest

Request parameters for getTransaction
"""


class GetTransactionRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getTransaction
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
            description="[PATH] The ID of the Amazon Seller Wallet transaction.",
        ),
    ]


"""
GetTransferPreviewRequest

Request parameters for getTransferPreview
"""


class GetTransferPreviewRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getTransferPreview
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    source_country_code: Annotated[
        str,
        QueryParam(),
        Field(
            ...,
            validation_alias=AliasChoices("sourceCountryCode", "source_country_code"),
            serialization_alias="sourceCountryCode",
            description="[QUERY] Country code of the source transaction account in ISO 3166 format.",
        ),
    ]

    source_currency_code: Annotated[
        str,
        QueryParam(),
        Field(
            ...,
            validation_alias=AliasChoices("sourceCurrencyCode", "source_currency_code"),
            serialization_alias="sourceCurrencyCode",
            description="[QUERY] Currency code of the source transaction country in ISO 4217 format.",
        ),
    ]

    destination_country_code: Annotated[
        str,
        QueryParam(),
        Field(
            ...,
            validation_alias=AliasChoices(
                "destinationCountryCode", "destination_country_code"
            ),
            serialization_alias="destinationCountryCode",
            description="[QUERY] Country code of the destination transaction account in ISO 3166 format.",
        ),
    ]

    destination_currency_code: Annotated[
        str,
        QueryParam(),
        Field(
            ...,
            validation_alias=AliasChoices(
                "destinationCurrencyCode", "destination_currency_code"
            ),
            serialization_alias="destinationCurrencyCode",
            description="[QUERY] Currency code of the destination transaction country in ISO 4217 format.",
        ),
    ]

    base_amount: Annotated[
        float,
        QueryParam(),
        Field(
            ...,
            validation_alias=AliasChoices("baseAmount", "base_amount"),
            serialization_alias="baseAmount",
            description="[QUERY] The base transaction amount without any markup fees.",
        ),
    ]


"""
GetTransferScheduleRequest

Request parameters for getTransferSchedule
"""


class GetTransferScheduleRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getTransferSchedule
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    transfer_schedule_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("transferScheduleId", "transfer_schedule_id"),
            serialization_alias="transferScheduleId",
            description="[PATH] The schedule ID of the Amazon Seller Wallet transfer.",
        ),
    ]


"""
ListAccountBalancesRequest

Request parameters for listAccountBalances
"""


class ListAccountBalancesRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for listAccountBalances
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    account_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("accountId", "account_id"),
            serialization_alias="accountId",
            description="[PATH] The ID of the Amazon Seller Wallet account.",
        ),
    ]


"""
ListAccountTransactionsRequest

Request parameters for listAccountTransactions
"""


class ListAccountTransactionsRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for listAccountTransactions
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    account_id: Annotated[
        str,
        QueryParam(),
        Field(
            ...,
            validation_alias=AliasChoices("accountId", "account_id"),
            serialization_alias="accountId",
            description="[QUERY] The ID of the Amazon Seller Wallet account.",
        ),
    ]

    next_page_token: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("nextPageToken", "next_page_token"),
            serialization_alias="nextPageToken",
            description="[QUERY] A token that you use to retrieve the next page of results. The response includes `nextPageToken` when the number of results exceeds 100. To get the next page of results, call the operation with this token and include the same arguments as the call that produced the token. To get a complete list, call this operation until `nextPageToken` is null. Note that this operation can return empty pages.",
        ),
    ]


"""
ListAccountsRequest

Request parameters for listAccounts
"""


class ListAccountsRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for listAccounts
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
            description="[QUERY] The marketplace for which items are returned. The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).",
        ),
    ]


"""
ListTransferSchedulesRequest

Request parameters for listTransferSchedules
"""


class ListTransferSchedulesRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for listTransferSchedules
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    account_id: Annotated[
        str,
        QueryParam(),
        Field(
            ...,
            validation_alias=AliasChoices("accountId", "account_id"),
            serialization_alias="accountId",
            description="[QUERY] The ID of the Amazon Seller Wallet account.",
        ),
    ]

    next_page_token: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("nextPageToken", "next_page_token"),
            serialization_alias="nextPageToken",
            description="[QUERY] A token that you use to retrieve the next page of results. The response includes `nextPageToken` when the number of results exceeds the specified `pageSize` value. To get the next page of results, call the operation with this token and include the same arguments as the call that produced the token. To get a complete list, call this operation until `nextPageToken` is null. Note that this operation can return empty pages.",
        ),
    ]


"""
TransactionAccount

Details of the bank account involved in transaction.
"""


class TransactionAccount(SpApiBaseModel):
    """Details of the bank account involved in transaction."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    account_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("accountId", "account_id"),
            serialization_alias="accountId",
            description="The unique identifier provided by Amazon to identify the account.",
        ),
    ]

    bank_account_holder_name: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices(
                "bankAccountHolderName", "bank_account_holder_name"
            ),
            serialization_alias="bankAccountHolderName",
            description="The account holder's name.",
        ),
    ]

    bank_name: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("bankName", "bank_name"),
            serialization_alias="bankName",
            description="The name of the bank.",
        ),
    ]

    bank_account_number_format: Annotated[
        "BankAccountNumberFormat",
        Field(
            ...,
            validation_alias=AliasChoices(
                "bankAccountNumberFormat", "bank_account_number_format"
            ),
            serialization_alias="bankAccountNumberFormat",
            description="The format for the bank account number.",
        ),
    ]

    bank_account_number_tail: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "bankAccountNumberTail", "bank_account_number_tail"
            ),
            serialization_alias="bankAccountNumberTail",
            description="The last three digits of the bank account number.",
        ),
    ]

    bank_account_country_code: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "bankAccountCountryCode", "bank_account_country_code"
            ),
            serialization_alias="bankAccountCountryCode",
            description="The two-digit country code, in ISO 3166 format. This field is optional for `transactionSourceAccount`, but is mandatory for `transactionDestinationAccount`.",
        ),
    ]

    bank_account_currency: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices(
                "bankAccountCurrency", "bank_account_currency"
            ),
            serialization_alias="bankAccountCurrency",
            description="The currency code in ISO 4217 format.",
        ),
    ]


TransactionStatus = str
"""The current status of the transaction."""


"""
Transaction

The current transaction status and historical details related to it.
"""


class Transaction(SpApiBaseModel):
    """The current transaction status and historical details related to it."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    transaction_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("transactionId", "transaction_id"),
            serialization_alias="transactionId",
            description="The unique identifier provided by Amazon to the transaction.",
        ),
    ]

    transaction_type: Annotated[
        "TransactionType",
        Field(
            ...,
            validation_alias=AliasChoices("transactionType", "transaction_type"),
            serialization_alias="transactionType",
            description="The type of the transaction.",
        ),
    ]

    transaction_status: Annotated[
        "TransactionStatus",
        Field(
            ...,
            validation_alias=AliasChoices("transactionStatus", "transaction_status"),
            serialization_alias="transactionStatus",
            description="The status of the transaction.",
        ),
    ]

    transaction_request_date: Annotated[
        datetime,
        Field(
            ...,
            validation_alias=AliasChoices(
                "transactionRequestDate", "transaction_request_date"
            ),
            serialization_alias="transactionRequestDate",
            description="The date on which the transaction was initiated.",
        ),
    ]

    expected_completion_date: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices(
                "expectedCompletionDate", "expected_completion_date"
            ),
            serialization_alias="expectedCompletionDate",
            description="The expected completion date of the transaction.",
        ),
    ]

    transaction_actual_completion_date: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices(
                "transactionActualCompletionDate", "transaction_actual_completion_date"
            ),
            serialization_alias="transactionActualCompletionDate",
            description="The transaction's completion date.",
        ),
    ]

    last_update_date: Annotated[
        datetime,
        Field(
            ...,
            validation_alias=AliasChoices("lastUpdateDate", "last_update_date"),
            serialization_alias="lastUpdateDate",
            description="The date of the most recent account balance update.",
        ),
    ]

    requester_name: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("requesterName", "requester_name"),
            serialization_alias="requesterName",
            description="The Amazon Seller Wallet customer who requested the transaction.",
        ),
    ]

    transaction_requester_source: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices(
                "transactionRequesterSource", "transaction_requester_source"
            ),
            serialization_alias="transactionRequesterSource",
            description="The transaction initiation source. This value could be the Amazon portal or PISP name that the customer used to start the transaction.",
        ),
    ]

    transaction_description: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices(
                "transactionDescription", "transaction_description"
            ),
            serialization_alias="transactionDescription",
            description="The description provided by the requester in the transaction request at time of transaction initiation.",
        ),
    ]

    transaction_source_account: Annotated[
        "TransactionAccount",
        Field(
            ...,
            validation_alias=AliasChoices(
                "transactionSourceAccount", "transaction_source_account"
            ),
            serialization_alias="transactionSourceAccount",
            description="The source bank account details in the transaction.",
        ),
    ]

    transaction_destination_account: Annotated[
        "TransactionAccount",
        Field(
            ...,
            validation_alias=AliasChoices(
                "transactionDestinationAccount", "transaction_destination_account"
            ),
            serialization_alias="transactionDestinationAccount",
            description="The destination bank account details in the transaction.",
        ),
    ]

    transaction_request_amount: Annotated[
        "Currency",
        Field(
            ...,
            validation_alias=AliasChoices(
                "transactionRequestAmount", "transaction_request_amount"
            ),
            serialization_alias="transactionRequestAmount",
            description="The amount for which the transfer was initiated.",
        ),
    ]

    transfer_rate_details: Annotated[
        "TransferRatePreview",
        Field(
            ...,
            validation_alias=AliasChoices(
                "transferRateDetails", "transfer_rate_details"
            ),
            serialization_alias="transferRateDetails",
            description="The fees and rates applied on the transaction, as applicable.",
        ),
    ]

    transaction_final_amount: Annotated[
        Optional["Currency"],
        Field(
            None,
            validation_alias=AliasChoices(
                "transactionFinalAmount", "transaction_final_amount"
            ),
            serialization_alias="transactionFinalAmount",
            description="The amount of completed transaction in the destination account currency. This value is only populated for international transactions",
        ),
    ]

    transaction_failure_reason: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "transactionFailureReason", "transaction_failure_reason"
            ),
            serialization_alias="transactionFailureReason",
            description="The reason the transaction failed, if applicable.",
        ),
    ]


"""
TransactionListing

A list of transactions.
"""


class TransactionListing(SpApiBaseModel):
    """A list of transactions."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    next_page_token: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("nextPageToken", "next_page_token"),
            serialization_alias="nextPageToken",
            description="A token that you use to retrieve the next page of results. The response includes `nextPageToken` when the number of results exceeds 100. To get the next page of results, call the operation with this token and include the same arguments as the call that produced the token. To get a complete list, call this operation until `nextPageToken` is null. Note that this operation can return empty pages.",
        ),
    ]

    transactions: Annotated[
        List["Transaction"], Field(..., description="A list of transactions.")
    ]


"""
TransferScheduleFailures

The time of and reason for the transfer schedule failure.
"""


class TransferScheduleFailures(SpApiBaseModel):
    """The time of and reason for the transfer schedule failure."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    transfer_schedule_failure_date: Annotated[
        datetime,
        Field(
            ...,
            validation_alias=AliasChoices(
                "transferScheduleFailureDate", "transfer_schedule_failure_date"
            ),
            serialization_alias="transferScheduleFailureDate",
            description="The transfer schedule failure date.",
        ),
    ]

    transfer_schedule_failure_reason: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices(
                "transferScheduleFailureReason", "transfer_schedule_failure_reason"
            ),
            serialization_alias="transferScheduleFailureReason",
            description="The reason listed for the failure of the transfer schedule.",
        ),
    ]


"""
TransferSchedule

Transfer schedule details and historical details related to it.
"""


class TransferSchedule(SpApiBaseModel):
    """Transfer schedule details and historical details related to it."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    transfer_schedule_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("transferScheduleId", "transfer_schedule_id"),
            serialization_alias="transferScheduleId",
            description="The unique identifier provided by Amazon to the scheduled transfer.",
        ),
    ]

    transaction_type: Annotated[
        "TransactionType",
        Field(
            ...,
            validation_alias=AliasChoices("transactionType", "transaction_type"),
            serialization_alias="transactionType",
            description="The type of transfer.",
        ),
    ]

    transaction_source_account: Annotated[
        Optional["TransactionAccount"],
        Field(
            None,
            validation_alias=AliasChoices(
                "transactionSourceAccount", "transaction_source_account"
            ),
            serialization_alias="transactionSourceAccount",
            description="Details of the source bank account in the scheduled transfer.",
        ),
    ]

    transaction_destination_account: Annotated[
        "TransactionAccount",
        Field(
            ...,
            validation_alias=AliasChoices(
                "transactionDestinationAccount", "transaction_destination_account"
            ),
            serialization_alias="transactionDestinationAccount",
            description="Details of the destination bank account in the scheduled transfer. Here `bankAccountCountryCode` is a required field.",
        ),
    ]

    transfer_schedule_status: Annotated[
        "TransferScheduleStatus",
        Field(
            ...,
            validation_alias=AliasChoices(
                "transferScheduleStatus", "transfer_schedule_status"
            ),
            serialization_alias="transferScheduleStatus",
            description="The type of transfer schedule. This information can be modified when you update a transfer schedule.",
        ),
    ]

    transfer_schedule_information: Annotated[
        "TransferScheduleInformation",
        Field(
            ...,
            validation_alias=AliasChoices(
                "transferScheduleInformation", "transfer_schedule_information"
            ),
            serialization_alias="transferScheduleInformation",
            description="The fields required for the scheduled transfer. This information can be modified when you update a transfer schedule.",
        ),
    ]

    payment_preference: Annotated[
        Optional["PaymentPreference"],
        Field(
            None,
            validation_alias=AliasChoices("paymentPreference", "payment_preference"),
            serialization_alias="paymentPreference",
            description="The payment preference of the scheduled transfer. This information can be modified when you update a transfer schedule.",
        ),
    ]

    transfer_schedule_failures: Annotated[
        List["TransferScheduleFailures"],
        Field(
            ...,
            validation_alias=AliasChoices(
                "transferScheduleFailures", "transfer_schedule_failures"
            ),
            serialization_alias="transferScheduleFailures",
            description="A list of transfer schedule failures.",
        ),
    ]


"""
TransferScheduleListing

A list of transfer schedules.
"""


class TransferScheduleListing(SpApiBaseModel):
    """A list of transfer schedules."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    next_page_token: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("nextPageToken", "next_page_token"),
            serialization_alias="nextPageToken",
            description="A token that you use to retrieve the next page of results. The response includes `nextPageToken` when the number of results exceeds 100. To get the next page of results, call the operation with this token and include the same arguments as the call that produced the token. To get a complete list, call this operation until `nextPageToken` is null. Note that this operation can return empty pages.",
        ),
    ]

    transfer_schedules: Annotated[
        List["TransferSchedule"],
        Field(
            ...,
            validation_alias=AliasChoices("transferSchedules", "transfer_schedules"),
            serialization_alias="transferSchedules",
            description="A list of transfer schedules.",
        ),
    ]


"""
UpdateTransferScheduleRequest

Request parameters for updateTransferSchedule
"""


class UpdateTransferScheduleRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for updateTransferSchedule
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    body: Annotated[
        "TransferSchedule",
        BodyParam(),
        Field(
            ...,
            description="[BODY] The payload of the scheduled transfer request that is to be updated.",
        ),
    ]


# Rebuild models to resolve forward references
AccountHolderAddress.model_rebuild()
BankAccount.model_rebuild()
BankAccountListing.model_rebuild()
Balance.model_rebuild()
BalanceListing.model_rebuild()
Currency.model_rebuild()
DeleteTransferSchedule.model_rebuild()
Error.model_rebuild()
ErrorList.model_rebuild()
FxRateDetails.model_rebuild()
Fee.model_rebuild()
PaymentPreference.model_rebuild()
TransferScheduleInformation.model_rebuild()
ScheduleExpression.model_rebuild()
TransactionInitiationRequestBody.model_rebuild()
TransactionInstrumentDetails.model_rebuild()
Transaction.model_rebuild()
TransactionAccount.model_rebuild()
TransactionListing.model_rebuild()
TransferRatePreview.model_rebuild()
TransferSchedule.model_rebuild()
TransferScheduleFailures.model_rebuild()
TransferScheduleListing.model_rebuild()
TransferScheduleRequestBody.model_rebuild()
ListAccountsRequest.model_rebuild()
GetAccountRequest.model_rebuild()
ListAccountBalancesRequest.model_rebuild()
GetTransferPreviewRequest.model_rebuild()
ListAccountTransactionsRequest.model_rebuild()
CreateTransactionRequest.model_rebuild()
GetTransactionRequest.model_rebuild()
ListTransferSchedulesRequest.model_rebuild()
CreateTransferScheduleRequest.model_rebuild()
UpdateTransferScheduleRequest.model_rebuild()
GetTransferScheduleRequest.model_rebuild()
DeleteScheduleTransactionRequest.model_rebuild()
