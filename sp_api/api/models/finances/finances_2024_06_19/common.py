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
AmazonPayContext

Additional information related to Amazon Pay.
"""


class AmazonPayContext(SpApiBaseModel):
    """Additional information related to Amazon Pay."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    store_name: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("storeName", "store_name"),
            serialization_alias="storeName",
            description="Store name related to transaction.",
        ),
    ]

    order_type: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("orderType", "order_type"),
            serialization_alias="orderType",
            description="Order type of the transaction.",
        ),
    ]

    channel: Annotated[
        Optional[str],
        Field(None, description="Channel details of related transaction."),
    ]


BigDecimal = float
"""Fields with a schema type of BigDecimal are a signed decimal number (for example CurrencyAmount)."""


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
Breakdown

Breakdown provides details regarding the money movement under the financial transaction. Breakdowns get categorized further into breakdown types, breakdown amounts, and further breakdowns into a hierarchical structure.
"""


class Breakdown(SpApiBaseModel):
    """Breakdown provides details regarding the money movement under the financial transaction. Breakdowns get categorized further into breakdown types, breakdown amounts, and further breakdowns into a hierarchical structure."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    breakdown_type: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("breakdownType", "breakdown_type"),
            serialization_alias="breakdownType",
            description="The type of charge.",
        ),
    ]

    breakdown_amount: Annotated[
        Optional["Currency"],
        Field(
            None,
            validation_alias=AliasChoices("breakdownAmount", "breakdown_amount"),
            serialization_alias="breakdownAmount",
            description="The amount of the charge.",
        ),
    ]

    breakdowns: Annotated[
        Optional[List["Breakdown"]],
        Field(
            None,
            description="A list of breakdowns that detail how the total amount is calculated for the transaction.",
        ),
    ]


Breakdowns = List["Breakdown"]
"""A list of breakdowns that detail how the total amount is calculated for the transaction."""


# Enum definitions
class BusinessContextStoreNameEnum(str, Enum):
    """Enum for storeName"""

    AMAZON_HAUL = "AMAZON_HAUL"


"""
BusinessContext

Information about the line of business associated with a transaction.
"""


class BusinessContext(SpApiBaseModel):
    """Information about the line of business associated with a transaction."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    store_name: Annotated[
        Optional[BusinessContextStoreNameEnum],
        Field(
            None,
            validation_alias=AliasChoices("storeName", "store_name"),
            serialization_alias="storeName",
            description="The store name associated with the transaction.",
        ),
    ]


"""
Context

Additional Information about the item.
"""


class Context(SpApiBaseModel):
    """Additional Information about the item."""

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow",
        serialize_by_alias=True,
        arbitrary_types_allowed=True,
    )


Contexts = List["Context"]
"""List of additional Information about the item."""


Date = str
"""Fields with a schema type of date are in ISO 8601 date time format (for example GroupBeginDate)."""


"""
DeferredContext

Additional information related to Deferred transactions.
"""


class DeferredContext(SpApiBaseModel):
    """Additional information related to Deferred transactions."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    deferral_reason: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("deferralReason", "deferral_reason"),
            serialization_alias="deferralReason",
            description="The deferral policy applied to the transaction. **Examples:** `B2B` (invoiced orders), `DD7` (delivery date policy)",
        ),
    ]

    maturity_date: Annotated[
        Optional["Date"],
        Field(
            None,
            validation_alias=AliasChoices("maturityDate", "maturity_date"),
            serialization_alias="maturityDate",
            description="The release date of the transaction.",
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


ItemRelatedIdentifiers = List["ItemRelatedIdentifier"]
"""Related Business identifiers of the item in Transaction."""


"""
Item

Additional information about the items in Transaction.
"""


class Item(SpApiBaseModel):
    """Additional information about the items in Transaction."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    description: Annotated[
        Optional[str],
        Field(None, description="Description of items in the transaction"),
    ]

    related_identifiers: Annotated[
        Optional["ItemRelatedIdentifiers"],
        Field(
            None,
            validation_alias=AliasChoices("relatedIdentifiers", "related_identifiers"),
            serialization_alias="relatedIdentifiers",
            description="Related business identifiers of the item.",
        ),
    ]

    total_amount: Annotated[
        Optional["Currency"],
        Field(
            None,
            validation_alias=AliasChoices("totalAmount", "total_amount"),
            serialization_alias="totalAmount",
            description="The total amount of the item.",
        ),
    ]

    breakdowns: Annotated[
        Optional[List["Breakdown"]],
        Field(
            None,
            description="A list of breakdowns that detail how the total amount is calculated for the transaction.",
        ),
    ]

    contexts: Annotated[
        Optional["Contexts"],
        Field(None, description="Additional Information about the item."),
    ]


# Enum definitions
class ItemRelatedIdentifierItemRelatedIdentifierNameEnum(str, Enum):
    """Enum for itemRelatedIdentifierName"""

    ORDER_ADJUSTMENT_ITEM_ID = "ORDER_ADJUSTMENT_ITEM_ID"  # An Amazon-defined order adjustment identifier defined for refunds, guarantee claims, and chargeback events.
    COUPON_ID = "COUPON_ID"  # An identifier for Coupon applied on transaction.
    REMOVAL_SHIPMENT_ITEM_ID = (
        "REMOVAL_SHIPMENT_ITEM_ID"  # An identifier for an item in a removal shipment.
    )
    TRANSACTION_ID = "TRANSACTION_ID"  # Transaction id for the item.


"""
ItemRelatedIdentifier

Related business identifiers of the item.
"""


class ItemRelatedIdentifier(SpApiBaseModel):
    """Related business identifiers of the item."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    item_related_identifier_name: Annotated[
        Optional[ItemRelatedIdentifierItemRelatedIdentifierNameEnum],
        Field(
            None,
            validation_alias=AliasChoices(
                "itemRelatedIdentifierName", "item_related_identifier_name"
            ),
            serialization_alias="itemRelatedIdentifierName",
            description="Enumerated set of related item identifier names for the item.",
        ),
    ]

    item_related_identifier_value: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "itemRelatedIdentifierValue", "item_related_identifier_value"
            ),
            serialization_alias="itemRelatedIdentifierValue",
            description="Corresponding value of ItemRelatedIdentifierName",
        ),
    ]


Items = List["Item"]
"""List of items in the transaction"""


"""
ListTransactionsRequest

Request parameters for listTransactions
"""


class ListTransactionsRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for listTransactions
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    posted_after: Annotated[
        datetime,
        QueryParam(),
        Field(
            ...,
            validation_alias=AliasChoices("postedAfter", "posted_after"),
            serialization_alias="postedAfter",
            description="[QUERY] The response includes financial events posted on or after this date. This date must be in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format. The date-time must be more than two minutes before the time of the request.",
        ),
    ]

    posted_before: Annotated[
        Optional[datetime],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("postedBefore", "posted_before"),
            serialization_alias="postedBefore",
            description="[QUERY] A date used for selecting transactions posted before (but not at) a specified time. The date-time must be later than PostedAfter and no later than two minutes before the request was submitted, in ISO 8601 date time format. If PostedAfter and PostedBefore are more than 180 days apart, no transactions are returned. You must specify the PostedAfter parameter if you specify the PostedBefore parameter. Default: Now minus two minutes.",
        ),
    ]

    marketplace_id: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="[QUERY] The identifier of the marketplace from which you want to retrieve transactions. The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).",
        ),
    ]

    transaction_status: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("transactionStatus", "transaction_status"),
            serialization_alias="transactionStatus",
            description="[QUERY] The status of the transaction.  **Possible values:**  * `DEFERRED`: the transaction is currently deferred. * `RELEASED`: the transaction is currently released. * `DEFERRED_RELEASED`: the transaction was deferred in the past, but is now released. The status of a deferred transaction is updated to `DEFERRED_RELEASED` when the transaction is released.",
        ),
    ]

    next_token: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("nextToken", "next_token"),
            serialization_alias="nextToken",
            description="[QUERY] A string token returned in the response of your previous request.",
        ),
    ]


Transactions = List["Transaction"]
"""Contains transactions within a given time period."""


"""
TransactionsPayload

The payload for the `listTransactions` operation.
"""


class TransactionsPayload(SpApiBaseModel):
    """The payload for the `listTransactions` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    next_token: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("nextToken", "next_token"),
            serialization_alias="nextToken",
            description="When present and not empty, pass this string token in the next request to return the next response page.",
        ),
    ]

    transactions: Annotated[
        Optional["Transactions"],
        Field(
            None,
        ),
    ]


"""
ListTransactionsResponse

The response schema for the `listTransactions` operation.
"""


class ListTransactionsResponse(SpApiBaseModel):
    """The response schema for the `listTransactions` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["TransactionsPayload"],
        Field(None, description="The payload for the `listTransactions` operation."),
    ]


"""
MarketplaceDetails

Information about the marketplace where the transaction occurred.
"""


class MarketplaceDetails(SpApiBaseModel):
    """Information about the marketplace where the transaction occurred."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    marketplace_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="The identifier of the marketplace where the transaction occurred. The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).",
        ),
    ]

    marketplace_name: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("marketplaceName", "marketplace_name"),
            serialization_alias="marketplaceName",
            description="The name of the marketplace where the transaction occurred. Example: 'Amazon.com','Amazon.in'",
        ),
    ]


"""
PaymentsContext

Additional information related to Payments related transactions.
"""


class PaymentsContext(SpApiBaseModel):
    """Additional information related to Payments related transactions."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payment_type: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("paymentType", "payment_type"),
            serialization_alias="paymentType",
            description="Type of payment made.",
        ),
    ]

    payment_method: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("paymentMethod", "payment_method"),
            serialization_alias="paymentMethod",
            description="Method of payment made.",
        ),
    ]

    payment_reference: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("paymentReference", "payment_reference"),
            serialization_alias="paymentReference",
            description="Reference number of payment made.",
        ),
    ]

    payment_date: Annotated[
        Optional["Date"],
        Field(
            None,
            validation_alias=AliasChoices("paymentDate", "payment_date"),
            serialization_alias="paymentDate",
            description="Date of payment made.",
        ),
    ]


"""
ProductContext

Additional information related to the product.
"""


class ProductContext(SpApiBaseModel):
    """Additional information related to the product."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    asin: Annotated[
        Optional[str],
        Field(
            None,
            description="Amazon Standard Identification Number (ASIN) of the item.",
        ),
    ]

    sku: Annotated[
        Optional[str], Field(None, description="Stock keeping unit (SKU) of the item.")
    ]

    quantity_shipped: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices("quantityShipped", "quantity_shipped"),
            serialization_alias="quantityShipped",
            description="Quantity of the item shipped.",
        ),
    ]

    fulfillment_network: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("fulfillmentNetwork", "fulfillment_network"),
            serialization_alias="fulfillmentNetwork",
            description="Fulfillment network of the item.",
        ),
    ]


# Enum definitions
class RelatedIdentifierRelatedIdentifierNameEnum(str, Enum):
    """Enum for relatedIdentifierName"""

    ORDER_ID = "ORDER_ID"  # The `OrderId` that is associated with the transaction.
    SHIPMENT_ID = (
        "SHIPMENT_ID"  # The `ShipmentId` that is associated with the transaction.
    )
    FINANCIAL_EVENT_GROUP_ID = "FINANCIAL_EVENT_GROUP_ID"  # The identifier that is associated with the transaction's financial event group.
    REFUND_ID = "REFUND_ID"  # Associated RefundId of transaction
    INVOICE_ID = "INVOICE_ID"  # Associated InvoiceId of transaction
    DISBURSEMENT_ID = "DISBURSEMENT_ID"  # Disbursement Id for Amazon's bank transfer.
    TRANSFER_ID = "TRANSFER_ID"  # The `TransferId` associated with the transaction.
    DEFERRED_TRANSACTION_ID = "DEFERRED_TRANSACTION_ID"  # The transaction ID for the related deferred transaction
    RELEASE_TRANSACTION_ID = "RELEASE_TRANSACTION_ID"  # The transaction ID for the related released transaction
    SETTLEMENT_ID = "SETTLEMENT_ID"  # The identifier that is associated with the transaction's settlement group.


"""
RelatedIdentifier

Related business identifier of the transaction.
"""


class RelatedIdentifier(SpApiBaseModel):
    """Related business identifier of the transaction."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    related_identifier_name: Annotated[
        Optional[RelatedIdentifierRelatedIdentifierNameEnum],
        Field(
            None,
            validation_alias=AliasChoices(
                "relatedIdentifierName", "related_identifier_name"
            ),
            serialization_alias="relatedIdentifierName",
            description="Enumerated set of related business identifier names.",
        ),
    ]

    related_identifier_value: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "relatedIdentifierValue", "related_identifier_value"
            ),
            serialization_alias="relatedIdentifierValue",
            description="Corresponding value of RelatedIdentifierName",
        ),
    ]


RelatedIdentifiers = List["RelatedIdentifier"]
"""Related business identifiers of the transaction."""


"""
SellingPartnerMetadata

Metadata describing the seller.
"""


class SellingPartnerMetadata(SpApiBaseModel):
    """Metadata describing the seller."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    selling_partner_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("sellingPartnerId", "selling_partner_id"),
            serialization_alias="sellingPartnerId",
            description="Unique seller identifier.",
        ),
    ]

    account_type: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("accountType", "account_type"),
            serialization_alias="accountType",
            description="Account type of transaction.",
        ),
    ]

    marketplace_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="The identifier of the marketplace where the transaction occurred. The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).",
        ),
    ]


"""
TimeRangeContext

Additional information related to time range for transaction.
"""


class TimeRangeContext(SpApiBaseModel):
    """Additional information related to time range for transaction."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    start_time: Annotated[
        Optional["Date"],
        Field(
            None,
            validation_alias=AliasChoices("startTime", "start_time"),
            serialization_alias="startTime",
            description="Start time of the transaction.",
        ),
    ]

    end_time: Annotated[
        Optional["Date"],
        Field(
            None,
            validation_alias=AliasChoices("endTime", "end_time"),
            serialization_alias="endTime",
            description="End time of the transaction.",
        ),
    ]


"""
Transaction

Contains all information related to the transaction.
"""


class Transaction(SpApiBaseModel):
    """Contains all information related to the transaction."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    selling_partner_metadata: Annotated[
        Optional["SellingPartnerMetadata"],
        Field(
            None,
            validation_alias=AliasChoices(
                "sellingPartnerMetadata", "selling_partner_metadata"
            ),
            serialization_alias="sellingPartnerMetadata",
            description="Metadata describing the seller.",
        ),
    ]

    related_identifiers: Annotated[
        Optional["RelatedIdentifiers"],
        Field(
            None,
            validation_alias=AliasChoices("relatedIdentifiers", "related_identifiers"),
            serialization_alias="relatedIdentifiers",
            description="Related business identifiers of the transaction.",
        ),
    ]

    transaction_type: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("transactionType", "transaction_type"),
            serialization_alias="transactionType",
            description="The type of transaction. Possible values: * Shipment",
        ),
    ]

    transaction_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("transactionId", "transaction_id"),
            serialization_alias="transactionId",
            description="The unique identifier for the transaction.",
        ),
    ]

    transaction_status: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("transactionStatus", "transaction_status"),
            serialization_alias="transactionStatus",
            description="The status of the transaction. **Possible values:** * `DEFERRED`: the transaction is currently deferred. * `RELEASED`: the transaction is currently released. * `DEFERRED_RELEASED`: the transaction was deferred in the past, but is now released. The status of a deferred transaction is updated to `DEFERRED_RELEASED` when the transaction is released.",
        ),
    ]

    description: Annotated[
        Optional[str],
        Field(
            None,
            description="Describes the reasons for the transaction. Example: 'Order Payment','Refund Order'",
        ),
    ]

    posted_date: Annotated[
        Optional["Date"],
        Field(
            None,
            validation_alias=AliasChoices("postedDate", "posted_date"),
            serialization_alias="postedDate",
            description="The date and time when the transaction was posted.",
        ),
    ]

    total_amount: Annotated[
        Optional["Currency"],
        Field(
            None,
            validation_alias=AliasChoices("totalAmount", "total_amount"),
            serialization_alias="totalAmount",
            description="Total amount of transaction.",
        ),
    ]

    marketplace_details: Annotated[
        Optional["MarketplaceDetails"],
        Field(
            None,
            validation_alias=AliasChoices("marketplaceDetails", "marketplace_details"),
            serialization_alias="marketplaceDetails",
            description="Information about the marketplace where the transaction occurred.",
        ),
    ]

    items: Annotated[
        Optional["Items"],
        Field(
            None, description="Additional information about the items in Transaction."
        ),
    ]

    contexts: Annotated[
        Optional["Contexts"],
        Field(None, description="Additional Information about the transaction."),
    ]

    breakdowns: Annotated[
        Optional[List["Breakdown"]],
        Field(
            None,
            description="A list of breakdowns that detail how the total amount is calculated for the transaction.",
        ),
    ]


# Rebuild models to resolve forward references
ListTransactionsResponse.model_rebuild()
TransactionsPayload.model_rebuild()
Transaction.model_rebuild()
Currency.model_rebuild()
SellingPartnerMetadata.model_rebuild()
RelatedIdentifier.model_rebuild()
MarketplaceDetails.model_rebuild()
Item.model_rebuild()
ItemRelatedIdentifier.model_rebuild()
Breakdown.model_rebuild()
Context.model_rebuild()
ProductContext.model_rebuild()
AmazonPayContext.model_rebuild()
PaymentsContext.model_rebuild()
DeferredContext.model_rebuild()
BusinessContext.model_rebuild()
TimeRangeContext.model_rebuild()
ErrorList.model_rebuild()
Error.model_rebuild()
ListTransactionsRequest.model_rebuild()
