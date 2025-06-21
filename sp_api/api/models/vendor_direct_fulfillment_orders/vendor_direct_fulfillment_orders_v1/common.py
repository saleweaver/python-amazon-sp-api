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
AcknowledgementStatus

Status of acknowledgement.
"""


class AcknowledgementStatus(SpApiBaseModel):
    """Status of acknowledgement."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    code: Annotated[
        Optional[str],
        Field(
            None,
            description="Acknowledgement code is a unique two digit value which indicates the status of the acknowledgement. For a list of acknowledgement codes that Amazon supports, see the Vendor Direct Fulfillment APIs Use Case Guide.",
        ),
    ]

    description: Annotated[
        Optional[str], Field(None, description="Reason for the acknowledgement code.")
    ]


"""
Address

Address of the party.
"""


class Address(SpApiBaseModel):
    """Address of the party."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    name: Annotated[
        str,
        Field(
            ...,
            description="The name of the person, business or institution at that address. For Amazon label only vendors, this field will have the value `xxxxx` within the object `shipToParty`.",
        ),
    ]

    attention: Annotated[
        Optional[str],
        Field(
            None,
            description="The attention name of the person at that address. For Amazon label only vendors, this field will have the value `xxxxx` within the object `shipToParty`.",
        ),
    ]

    address_line1: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("addressLine1", "address_line1"),
            serialization_alias="addressLine1",
            description="First line of the address. For Amazon label only vendors, this field will have the value `xxxxx` within the object `shipToParty`.",
        ),
    ]

    address_line2: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("addressLine2", "address_line2"),
            serialization_alias="addressLine2",
            description="Additional address information, if required. For Amazon label only vendors, this field will have the value `xxxxx` within the object `shipToParty`.",
        ),
    ]

    address_line3: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("addressLine3", "address_line3"),
            serialization_alias="addressLine3",
            description="Additional address information, if required. For Amazon label only vendors, this field will have the value `xxxxx` within the object `shipToParty`.",
        ),
    ]

    city: Annotated[
        Optional[str],
        Field(
            None,
            description="The city where the person, business or institution is located. For Amazon label only vendors, this field will have the value `xxxxx` within the object `shipToParty`.",
        ),
    ]

    county: Annotated[
        Optional[str],
        Field(
            None,
            description="The county where person, business or institution is located. For Amazon label only vendors, this field will have the value `xxxxx` within the object `shipToParty`.",
        ),
    ]

    district: Annotated[
        Optional[str],
        Field(
            None,
            description="The district where person, business or institution is located. For Amazon label only vendors, this field will have the value `xxxxx` within the object `shipToParty`.",
        ),
    ]

    state_or_region: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("stateOrRegion", "state_or_region"),
            serialization_alias="stateOrRegion",
            description="The state or region where person, business or institution is located.",
        ),
    ]

    postal_code: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("postalCode", "postal_code"),
            serialization_alias="postalCode",
            description="The postal code of that address. It conatins a series of letters or digits or both, sometimes including spaces or punctuation.",
        ),
    ]

    country_code: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("countryCode", "country_code"),
            serialization_alias="countryCode",
            description="The two digit country code. In ISO 3166-1 alpha-2 format.",
        ),
    ]

    phone: Annotated[
        Optional[str],
        Field(
            None,
            description="The phone number of the person, business or institution located at that address. For Amazon label only vendors, this field will have the value `xxxxx` within the object `shipToParty`.",
        ),
    ]


Decimal = str
"""A decimal number with no loss of precision. Useful when precision loss is unacceptable, as with currencies. Follows RFC7159 for number representation."""


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


"""
GetOrderRequest

Request parameters for getOrder
"""


class GetOrderRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getOrder
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    purchase_order_number: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices(
                "purchaseOrderNumber", "purchase_order_number"
            ),
            serialization_alias="purchaseOrderNumber",
            description="[PATH] The order identifier for the purchase order that you want. Formatting Notes: alpha-numeric code.",
        ),
    ]


"""
GiftDetails

Gift details for the item.
"""


class GiftDetails(SpApiBaseModel):
    """Gift details for the item."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    gift_message: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("giftMessage", "gift_message"),
            serialization_alias="giftMessage",
            description="Gift message to be printed in shipment.",
        ),
    ]

    gift_wrap_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("giftWrapId", "gift_wrap_id"),
            serialization_alias="giftWrapId",
            description="Gift wrap identifier for the gift wrapping, if any.",
        ),
    ]


# Enum definitions
class UnitOfMeasureEnum(str, Enum):
    """Enum for unitOfMeasure"""

    EACH = "Each"  # Unit of measure to represent individual piece.


"""
ItemQuantity

Details of quantity ordered.
"""


class ItemQuantity(SpApiBaseModel):
    """Details of quantity ordered."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    amount: Annotated[
        Optional[int],
        Field(
            None, description="Acknowledged quantity. This value should not be zero."
        ),
    ]

    unit_of_measure: Annotated[
        Optional[UnitOfMeasureEnum],
        Field(
            None,
            validation_alias=AliasChoices("unitOfMeasure", "unit_of_measure"),
            serialization_alias="unitOfMeasure",
            description="Unit of measure for the acknowledged quantity.",
        ),
    ]


"""
Money

An amount of money, including units in the form of currency.
"""


class Money(SpApiBaseModel):
    """An amount of money, including units in the form of currency."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    currency_code: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("currencyCode", "currency_code"),
            serialization_alias="currencyCode",
            description="Three digit currency code in ISO 4217 format. String of length 3.",
        ),
    ]

    amount: Annotated[
        Optional["Decimal"],
        Field(
            None,
        ),
    ]


"""
ScheduledDeliveryShipment

Dates for the scheduled delivery shipments.
"""


class ScheduledDeliveryShipment(SpApiBaseModel):
    """Dates for the scheduled delivery shipments."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    scheduled_delivery_service_type: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "scheduledDeliveryServiceType", "scheduled_delivery_service_type"
            ),
            serialization_alias="scheduledDeliveryServiceType",
            description="Scheduled delivery service type.",
        ),
    ]

    earliest_nominated_delivery_date: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices(
                "earliestNominatedDeliveryDate", "earliest_nominated_delivery_date"
            ),
            serialization_alias="earliestNominatedDeliveryDate",
            description="Earliest nominated delivery date for the scheduled delivery.",
        ),
    ]

    latest_nominated_delivery_date: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices(
                "latestNominatedDeliveryDate", "latest_nominated_delivery_date"
            ),
            serialization_alias="latestNominatedDeliveryDate",
            description="Latest nominated delivery date for the scheduled delivery.",
        ),
    ]


"""
OrderItem

An item within an order
"""


class OrderItem(SpApiBaseModel):
    """An item within an order"""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    item_sequence_number: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("itemSequenceNumber", "item_sequence_number"),
            serialization_alias="itemSequenceNumber",
            description="Numbering of the item on the purchase order. The first item will be 1, the second 2, and so on.",
        ),
    ]

    buyer_product_identifier: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "buyerProductIdentifier", "buyer_product_identifier"
            ),
            serialization_alias="buyerProductIdentifier",
            description="Buyer's standard identification number (ASIN) of an item.",
        ),
    ]

    vendor_product_identifier: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "vendorProductIdentifier", "vendor_product_identifier"
            ),
            serialization_alias="vendorProductIdentifier",
            description="The vendor selected product identification of the item.",
        ),
    ]

    title: Annotated[Optional[str], Field(None, description="Title for the item.")]

    ordered_quantity: Annotated[
        "ItemQuantity",
        Field(
            ...,
            validation_alias=AliasChoices("orderedQuantity", "ordered_quantity"),
            serialization_alias="orderedQuantity",
            description="Item quantity ordered.",
        ),
    ]

    scheduled_delivery_shipment: Annotated[
        Optional["ScheduledDeliveryShipment"],
        Field(
            None,
            validation_alias=AliasChoices(
                "scheduledDeliveryShipment", "scheduled_delivery_shipment"
            ),
            serialization_alias="scheduledDeliveryShipment",
            description="Details for the scheduled delivery shipment.",
        ),
    ]

    gift_details: Annotated[
        Optional["GiftDetails"],
        Field(
            None,
            validation_alias=AliasChoices("giftDetails", "gift_details"),
            serialization_alias="giftDetails",
            description="Gift message and wrapId details.",
        ),
    ]

    net_price: Annotated[
        "Money",
        Field(
            ...,
            validation_alias=AliasChoices("netPrice", "net_price"),
            serialization_alias="netPrice",
            description="Net price (before tax) to vendor with currency details.",
        ),
    ]

    tax_details: Annotated[
        Optional[Dict[str, Any]],
        Field(
            None,
            validation_alias=AliasChoices("taxDetails", "tax_details"),
            serialization_alias="taxDetails",
            description="Total tax details for the line item.",
        ),
    ]

    total_price: Annotated[
        Optional["Money"],
        Field(
            None,
            validation_alias=AliasChoices("totalPrice", "total_price"),
            serialization_alias="totalPrice",
            description="The price to Amazon each (cost).",
        ),
    ]


# Enum definitions
class TaxRegistrationTypeEnum(str, Enum):
    """Enum for taxRegistrationType"""

    VAT = "VAT"  # Value-added tax.
    GST = "GST"  # Goods and Services tax.


"""
TaxRegistrationDetails

Tax registration details of the entity.
"""


class TaxRegistrationDetails(SpApiBaseModel):
    """Tax registration details of the entity."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    tax_registration_type: Annotated[
        Optional[TaxRegistrationTypeEnum],
        Field(
            None,
            validation_alias=AliasChoices(
                "taxRegistrationType", "tax_registration_type"
            ),
            serialization_alias="taxRegistrationType",
            description="Tax registration type for the entity.",
        ),
    ]

    tax_registration_number: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices(
                "taxRegistrationNumber", "tax_registration_number"
            ),
            serialization_alias="taxRegistrationNumber",
            description="Tax registration number for the party. For example, VAT ID.",
        ),
    ]

    tax_registration_address: Annotated[
        Optional["Address"],
        Field(
            None,
            validation_alias=AliasChoices(
                "taxRegistrationAddress", "tax_registration_address"
            ),
            serialization_alias="taxRegistrationAddress",
            description="Address associated with the tax registration number.",
        ),
    ]

    tax_registration_messages: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "taxRegistrationMessages", "tax_registration_messages"
            ),
            serialization_alias="taxRegistrationMessages",
            description="Tax registration message that can be used for additional tax related details.",
        ),
    ]


"""
PartyIdentification

Name, address and tax details of a party.
"""


class PartyIdentification(SpApiBaseModel):
    """Name, address and tax details of a party."""

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

    address: Annotated[
        Optional["Address"], Field(None, description="Address details of the party.")
    ]

    tax_info: Annotated[
        Optional["TaxRegistrationDetails"],
        Field(
            None,
            validation_alias=AliasChoices("taxInfo", "tax_info"),
            serialization_alias="taxInfo",
            description="Tax registration details of the entity.",
        ),
    ]


"""
ShipmentDates

Shipment dates.
"""


class ShipmentDates(SpApiBaseModel):
    """Shipment dates."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    required_ship_date: Annotated[
        datetime,
        Field(
            ...,
            validation_alias=AliasChoices("requiredShipDate", "required_ship_date"),
            serialization_alias="requiredShipDate",
            description="Time by which the vendor is required to ship the order.",
        ),
    ]

    promised_delivery_date: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices(
                "promisedDeliveryDate", "promised_delivery_date"
            ),
            serialization_alias="promisedDeliveryDate",
            description="Delivery date promised to the Amazon customer.",
        ),
    ]


"""
ShipmentDetails

Shipment details required for the shipment.
"""


class ShipmentDetails(SpApiBaseModel):
    """Shipment details required for the shipment."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    is_priority_shipment: Annotated[
        bool,
        Field(
            ...,
            validation_alias=AliasChoices("isPriorityShipment", "is_priority_shipment"),
            serialization_alias="isPriorityShipment",
            description="When true, this is a priority shipment.",
        ),
    ]

    is_scheduled_delivery_shipment: Annotated[
        Optional[bool],
        Field(
            None,
            validation_alias=AliasChoices(
                "isScheduledDeliveryShipment", "is_scheduled_delivery_shipment"
            ),
            serialization_alias="isScheduledDeliveryShipment",
            description="When true, this order is part of a scheduled delivery program.",
        ),
    ]

    is_pslip_required: Annotated[
        bool,
        Field(
            ...,
            validation_alias=AliasChoices("isPslipRequired", "is_pslip_required"),
            serialization_alias="isPslipRequired",
            description="When true, a packing slip is required to be sent to the customer.",
        ),
    ]

    is_gift: Annotated[
        Optional[bool],
        Field(
            None,
            validation_alias=AliasChoices("isGift", "is_gift"),
            serialization_alias="isGift",
            description="When true, the order contain a gift. Include the gift message and gift wrap information.",
        ),
    ]

    ship_method: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("shipMethod", "ship_method"),
            serialization_alias="shipMethod",
            description="Ship method to be used for shipping the order. Amazon defines ship method codes indicating the shipping carrier and shipment service level. To see the full list of ship methods in use, including both the code and the friendly name, search the 'Help' section on Vendor Central for 'ship methods'.",
        ),
    ]

    shipment_dates: Annotated[
        "ShipmentDates",
        Field(
            ...,
            validation_alias=AliasChoices("shipmentDates", "shipment_dates"),
            serialization_alias="shipmentDates",
        ),
    ]

    message_to_customer: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("messageToCustomer", "message_to_customer"),
            serialization_alias="messageToCustomer",
            description="Message to customer for order status.",
        ),
    ]


# Enum definitions
class OrderStatusEnum(str, Enum):
    """Enum for orderStatus"""

    NEW = "NEW"  # Status for newly created orders.
    SHIPPED = "SHIPPED"  # Status for orders that are already shipped.
    ACCEPTED = "ACCEPTED"  # Status for orders accepted by vendors.
    CANCELLED = "CANCELLED"  # Status for cancelled orders.


"""
OrderDetails

Details of an order.
"""


class OrderDetails(SpApiBaseModel):
    """Details of an order."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    customer_order_number: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices(
                "customerOrderNumber", "customer_order_number"
            ),
            serialization_alias="customerOrderNumber",
            description="The customer order number.",
        ),
    ]

    order_date: Annotated[
        datetime,
        Field(
            ...,
            validation_alias=AliasChoices("orderDate", "order_date"),
            serialization_alias="orderDate",
            description="The date the order was placed. This field is expected to be in ISO-8601 date/time format, for example:2018-07-16T23:00:00Z/ 2018-07-16T23:00:00-05:00 /2018-07-16T23:00:00-08:00. If no time zone is specified, UTC should be assumed.",
        ),
    ]

    order_status: Annotated[
        Optional[OrderStatusEnum],
        Field(
            None,
            validation_alias=AliasChoices("orderStatus", "order_status"),
            serialization_alias="orderStatus",
            description="Current status of the order.",
        ),
    ]

    shipment_details: Annotated[
        "ShipmentDetails",
        Field(
            ...,
            validation_alias=AliasChoices("shipmentDetails", "shipment_details"),
            serialization_alias="shipmentDetails",
        ),
    ]

    tax_total: Annotated[
        Optional[Dict[str, Any]],
        Field(
            None,
            validation_alias=AliasChoices("taxTotal", "tax_total"),
            serialization_alias="taxTotal",
            description="The total Tax object within shipment that relates to the order.",
        ),
    ]

    selling_party: Annotated[
        "PartyIdentification",
        Field(
            ...,
            validation_alias=AliasChoices("sellingParty", "selling_party"),
            serialization_alias="sellingParty",
            description="PartyID of vendor code.",
        ),
    ]

    ship_from_party: Annotated[
        "PartyIdentification",
        Field(
            ...,
            validation_alias=AliasChoices("shipFromParty", "ship_from_party"),
            serialization_alias="shipFromParty",
            description="PartyID of vendor's warehouse.",
        ),
    ]

    ship_to_party: Annotated[
        "Address",
        Field(
            ...,
            validation_alias=AliasChoices("shipToParty", "ship_to_party"),
            serialization_alias="shipToParty",
            description="Name/Address and tax details of the ship to party.",
        ),
    ]

    bill_to_party: Annotated[
        "PartyIdentification",
        Field(
            ...,
            validation_alias=AliasChoices("billToParty", "bill_to_party"),
            serialization_alias="billToParty",
            description="Name/Address and tax details of the bill to party.",
        ),
    ]

    items: Annotated[
        List["OrderItem"],
        Field(..., description="A list of items in this purchase order."),
    ]


"""
Order

Represents a purchase order.
"""


class Order(SpApiBaseModel):
    """Represents a purchase order."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    purchase_order_number: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices(
                "purchaseOrderNumber", "purchase_order_number"
            ),
            serialization_alias="purchaseOrderNumber",
            description="The purchase order number for this order. Formatting Notes: alpha-numeric code.",
        ),
    ]

    order_details: Annotated[
        Optional["OrderDetails"],
        Field(
            None,
            validation_alias=AliasChoices("orderDetails", "order_details"),
            serialization_alias="orderDetails",
            description="Purchase order details.",
        ),
    ]


"""
GetOrderResponse

The response schema for the getOrder operation.
"""


class GetOrderResponse(SpApiBaseModel):
    """The response schema for the getOrder operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["Order"],
        Field(None, description="The payload for the getOrder operation."),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
        ),
    ]


# Enum definitions
class StatusEnum(str, Enum):
    """Enum for status"""

    NEW = "NEW"  # Status for newly created purchase orders.
    SHIPPED = "SHIPPED"  # Status for purchase orders that are already shipped.
    ACCEPTED = "ACCEPTED"  # Status for purchase orders accepted by vendors.
    CANCELLED = "CANCELLED"  # Status for cancelled purchase orders.


class SortOrderEnum(str, Enum):
    """Enum for sortOrder"""

    ASC = "ASC"  # Sort in ascending order by order creation date.
    DESC = "DESC"  # Sort in descending order by order creation date.


"""
GetOrdersRequest

Request parameters for getOrders
"""


class GetOrdersRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getOrders
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    ship_from_party_id: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("shipFromPartyId", "ship_from_party_id"),
            serialization_alias="shipFromPartyId",
            description="[QUERY] The vendor warehouse identifier for the fulfillment warehouse. If not specified, the result will contain orders for all warehouses.",
        ),
    ]

    status: Annotated[
        Optional[StatusEnum],
        QueryParam(),
        Field(
            None,
            description="[QUERY] Returns only the purchase orders that match the specified status. If not specified, the result will contain orders that match any status.",
        ),
    ]

    limit: Annotated[
        Optional[int],
        QueryParam(),
        Field(
            None,
            description="[QUERY] The limit to the number of purchase orders returned.",
        ),
    ]

    created_after: Annotated[
        datetime,
        QueryParam(),
        Field(
            ...,
            validation_alias=AliasChoices("createdAfter", "created_after"),
            serialization_alias="createdAfter",
            description="[QUERY] Purchase orders that became available after this date and time will be included in the result. Must be in ISO-8601 date/time format.",
        ),
    ]

    created_before: Annotated[
        datetime,
        QueryParam(),
        Field(
            ...,
            validation_alias=AliasChoices("createdBefore", "created_before"),
            serialization_alias="createdBefore",
            description="[QUERY] Purchase orders that became available before this date and time will be included in the result. Must be in ISO-8601 date/time format.",
        ),
    ]

    sort_order: Annotated[
        Optional[SortOrderEnum],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("sortOrder", "sort_order"),
            serialization_alias="sortOrder",
            description="[QUERY] Sort the list in ascending or descending order by order creation date.",
        ),
    ]

    next_token: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("nextToken", "next_token"),
            serialization_alias="nextToken",
            description="[QUERY] Used for pagination when there are more orders than the specified result size limit. The token value is returned in the previous API call.",
        ),
    ]

    include_details: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("includeDetails", "include_details"),
            serialization_alias="includeDetails",
            description="[QUERY] When true, returns the complete purchase order details. Otherwise, only purchase order numbers are returned.",
        ),
    ]


"""
Pagination

The pagination elements required to retrieve the remaining data.
"""


class Pagination(SpApiBaseModel):
    """The pagination elements required to retrieve the remaining data."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    next_token: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("nextToken", "next_token"),
            serialization_alias="nextToken",
            description="A generated string used to pass information to your next request. If NextToken is returned, pass the value of NextToken to the next request. If NextToken is not returned, there are no more order items to return.",
        ),
    ]


"""
OrderList

A list of purchase orders returned as response.
"""


class OrderList(SpApiBaseModel):
    """A list of purchase orders returned as response."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    pagination: Annotated[
        Optional["Pagination"],
        Field(
            None,
            description="The pagination elements required to retrieve the remaining data.",
        ),
    ]

    orders: Annotated[
        Optional[List["Order"]],
        Field(None, description="Represents a purchase order within the OrderList."),
    ]


"""
GetOrdersResponse

The response schema for the getOrders operation.
"""


class GetOrdersResponse(SpApiBaseModel):
    """The response schema for the getOrders operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["OrderList"], Field(None, description="A list of purchase orders.")
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
        ),
    ]


"""
OrderItemAcknowledgement

Details of an individual item within the order being acknowledged.
"""


class OrderItemAcknowledgement(SpApiBaseModel):
    """Details of an individual item within the order being acknowledged."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    item_sequence_number: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("itemSequenceNumber", "item_sequence_number"),
            serialization_alias="itemSequenceNumber",
            description="Line item sequence number for the item.",
        ),
    ]

    buyer_product_identifier: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "buyerProductIdentifier", "buyer_product_identifier"
            ),
            serialization_alias="buyerProductIdentifier",
            description="Buyer's standard identification number (ASIN) of an item.",
        ),
    ]

    vendor_product_identifier: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "vendorProductIdentifier", "vendor_product_identifier"
            ),
            serialization_alias="vendorProductIdentifier",
            description="The vendor selected product identification of the item. Should be the same as was provided in the purchase order.",
        ),
    ]

    acknowledged_quantity: Annotated[
        "ItemQuantity",
        Field(
            ...,
            validation_alias=AliasChoices(
                "acknowledgedQuantity", "acknowledged_quantity"
            ),
            serialization_alias="acknowledgedQuantity",
            description="Details of quantity acknowledged with the above acknowledgement code.",
        ),
    ]


"""
OrderAcknowledgementItem

Details of an individual order being acknowledged.
"""


class OrderAcknowledgementItem(SpApiBaseModel):
    """Details of an individual order being acknowledged."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    purchase_order_number: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices(
                "purchaseOrderNumber", "purchase_order_number"
            ),
            serialization_alias="purchaseOrderNumber",
            description="The purchase order number for this order. Formatting Notes: alpha-numeric code.",
        ),
    ]

    vendor_order_number: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("vendorOrderNumber", "vendor_order_number"),
            serialization_alias="vendorOrderNumber",
            description="The vendor's order number for this order.",
        ),
    ]

    acknowledgement_date: Annotated[
        datetime,
        Field(
            ...,
            validation_alias=AliasChoices(
                "acknowledgementDate", "acknowledgement_date"
            ),
            serialization_alias="acknowledgementDate",
            description="The date and time when the order is acknowledged, in ISO-8601 date/time format. For example: 2018-07-16T23:00:00Z / 2018-07-16T23:00:00-05:00 / 2018-07-16T23:00:00-08:00.",
        ),
    ]

    acknowledgement_status: Annotated[
        "AcknowledgementStatus",
        Field(
            ...,
            validation_alias=AliasChoices(
                "acknowledgementStatus", "acknowledgement_status"
            ),
            serialization_alias="acknowledgementStatus",
            description="Status of acknowledgement.",
        ),
    ]

    selling_party: Annotated[
        "PartyIdentification",
        Field(
            ...,
            validation_alias=AliasChoices("sellingParty", "selling_party"),
            serialization_alias="sellingParty",
            description="PartyID as vendor code.",
        ),
    ]

    ship_from_party: Annotated[
        "PartyIdentification",
        Field(
            ...,
            validation_alias=AliasChoices("shipFromParty", "ship_from_party"),
            serialization_alias="shipFromParty",
            description="PartyID as the vendor's warehouseId.",
        ),
    ]

    item_acknowledgements: Annotated[
        List["OrderItemAcknowledgement"],
        Field(
            ...,
            validation_alias=AliasChoices(
                "itemAcknowledgements", "item_acknowledgements"
            ),
            serialization_alias="itemAcknowledgements",
            description="Item details including acknowledged quantity.",
        ),
    ]


"""
SubmitAcknowledgementRequestBody

The request schema for the submitAcknowledgement operation.
"""


class SubmitAcknowledgementRequestBody(SpApiBaseModel):
    """The request schema for the submitAcknowledgement operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    order_acknowledgements: Annotated[
        Optional[List["OrderAcknowledgementItem"]],
        Field(
            None,
            validation_alias=AliasChoices(
                "orderAcknowledgements", "order_acknowledgements"
            ),
            serialization_alias="orderAcknowledgements",
            description="A list of one or more purchase orders.",
        ),
    ]


"""
SubmitAcknowledgementRequest

Request parameters for submitAcknowledgement
"""


class SubmitAcknowledgementRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for submitAcknowledgement
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    body: Annotated[
        "SubmitAcknowledgementRequestBody",
        BodyParam(),
        Field(
            ...,
            description="[BODY] The request body containing the acknowledgement to an order.",
        ),
    ]


"""
TransactionId

Response containing the transaction ID.
"""


class TransactionId(SpApiBaseModel):
    """Response containing the transaction ID."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    transaction_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("transactionId", "transaction_id"),
            serialization_alias="transactionId",
            description="GUID assigned by Amazon to identify this transaction. This value can be used with the Transaction Status API to return the status of this transaction.",
        ),
    ]


"""
SubmitAcknowledgementResponse

The response schema for the submitAcknowledgement operation.
"""


class SubmitAcknowledgementResponse(SpApiBaseModel):
    """The response schema for the submitAcknowledgement operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["TransactionId"],
        Field(None, description="The payload for the submitAcknowledgement operation."),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
        ),
    ]


# Enum definitions
class TypeEnum(str, Enum):
    """Enum for type"""

    CONSUMPTION = (
        "CONSUMPTION"  # Tax levied on consumption spending on goods and services.
    )
    GST = "GST"  # Tax levied on most goods and services sold for domestic consumption.
    MW_ST_ = "MwSt."  # Mehrwertsteuer, MwSt, is German for value-added tax.
    PST = "PST"  # A provincial sales tax (PST) is imposed on consumers of goods and particular services in many Canadian provinces.
    TOTAL = "TOTAL"  # Combined total of all the applicable taxes.
    TVA = "TVA"  # Taxe sur la Valeur Ajout&#233;e (TVA) is French for value-added tax.
    VAT = "VAT"  # Value-added tax.


"""
TaxDetails

The tax details for the order. _Note:_ Amazon calculates tax on the list price (Amazon retail price).
"""


class TaxDetails(SpApiBaseModel):
    """The tax details for the order. _Note:_ Amazon calculates tax on the list price (Amazon retail price)."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    tax_rate: Annotated[
        Optional["Decimal"],
        Field(
            None,
            validation_alias=AliasChoices("taxRate", "tax_rate"),
            serialization_alias="taxRate",
        ),
    ]

    tax_amount: Annotated[
        "Money",
        Field(
            ...,
            validation_alias=AliasChoices("taxAmount", "tax_amount"),
            serialization_alias="taxAmount",
        ),
    ]

    taxable_amount: Annotated[
        Optional["Money"],
        Field(
            None,
            validation_alias=AliasChoices("taxableAmount", "taxable_amount"),
            serialization_alias="taxableAmount",
        ),
    ]

    type: Annotated[Optional[TypeEnum], Field(None, description="Tax type.")]


TaxLineItem = List["TaxDetails"]
"""A list of tax line items."""


# Rebuild models to resolve forward references
GetOrdersResponse.model_rebuild()
GetOrderResponse.model_rebuild()
OrderList.model_rebuild()
Pagination.model_rebuild()
Order.model_rebuild()
OrderDetails.model_rebuild()
PartyIdentification.model_rebuild()
TaxRegistrationDetails.model_rebuild()
Address.model_rebuild()
OrderItem.model_rebuild()
Money.model_rebuild()
SubmitAcknowledgementResponse.model_rebuild()
TransactionId.model_rebuild()
SubmitAcknowledgementRequestBody.model_rebuild()
OrderAcknowledgementItem.model_rebuild()
OrderItemAcknowledgement.model_rebuild()
ItemQuantity.model_rebuild()
TaxDetails.model_rebuild()
AcknowledgementStatus.model_rebuild()
Error.model_rebuild()
ShipmentDetails.model_rebuild()
ShipmentDates.model_rebuild()
ScheduledDeliveryShipment.model_rebuild()
GiftDetails.model_rebuild()
GetOrdersRequest.model_rebuild()
GetOrderRequest.model_rebuild()
SubmitAcknowledgementRequest.model_rebuild()
