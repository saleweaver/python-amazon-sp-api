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
            description="The name of the person, business or institution at that address.",
        ),
    ]

    address_line1: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("addressLine1", "address_line1"),
            serialization_alias="addressLine1",
            description="First line of the address.",
        ),
    ]

    address_line2: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("addressLine2", "address_line2"),
            serialization_alias="addressLine2",
            description="Additional street address information, if required.",
        ),
    ]

    address_line3: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("addressLine3", "address_line3"),
            serialization_alias="addressLine3",
            description="Additional street address information, if required.",
        ),
    ]

    city: Annotated[
        Optional[str],
        Field(
            None,
            description="The city where the person, business or institution is located.",
        ),
    ]

    county: Annotated[
        Optional[str],
        Field(
            None,
            description="The county where person, business or institution is located.",
        ),
    ]

    district: Annotated[
        Optional[str],
        Field(
            None,
            description="The district where person, business or institution is located.",
        ),
    ]

    state_or_region: Annotated[
        Optional[str],
        Field(
            None,
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
            description="The postal code of that address. It contains a series of letters or digits or both, sometimes including spaces or punctuation.",
        ),
    ]

    country_code: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("countryCode", "country_code"),
            serialization_alias="countryCode",
            description="The two-letter country code in [ISO 3166-1 alpha-2](https://www.iban.com/country-codes) format.",
        ),
    ]

    phone: Annotated[
        Optional[str],
        Field(
            None,
            description="The phone number of the person, business or institution located at that address.",
        ),
    ]


CarrierId = str
"""The unique carrier code for the carrier for whom container labels are requested."""


Decimal = str
"""A decimal number with no loss of precision. Useful when precision loss is unacceptable, as with currencies. Follows RFC7159 for number representation. <br>**Pattern** : `^-?(0|([1-9]d*))(.d+)?([eE][+-]?d+)?$`."""


# Enum definitions
class UnitOfMeasureEnum(str, Enum):
    """Enum for unitOfMeasure"""

    KG = "KG"  # Kilogram
    LB = "LB"  # Pounds (Libra for Latin).


"""
Dimensions

Physical dimensional measurements of a container.
"""


class Dimensions(SpApiBaseModel):
    """Physical dimensional measurements of a container."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    length: Annotated["Decimal", Field(..., description="The length of the container.")]

    width: Annotated["Decimal", Field(..., description="The width of the container.")]

    height: Annotated["Decimal", Field(..., description="The height of the container.")]

    unit_of_measure: Annotated[
        UnitOfMeasureEnum,
        Field(
            ...,
            validation_alias=AliasChoices("unitOfMeasure", "unit_of_measure"),
            serialization_alias="unitOfMeasure",
            description="The unit of measure for dimensions.",
        ),
    ]


"""
ItemQuantity

Details of item quantity.
"""


class ItemQuantity(SpApiBaseModel):
    """Details of item quantity."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    amount: Annotated[
        int,
        Field(
            ...,
            description="Quantity of units shipped for a specific item at a shipment level. If the item is present only in certain packages or pallets within the shipment, please provide this at the appropriate package or pallet level.",
        ),
    ]

    unit_of_measure: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("unitOfMeasure", "unit_of_measure"),
            serialization_alias="unitOfMeasure",
            description="Unit of measure for the shipped quantity.",
        ),
    ]


"""
PackedItem

An item that has been packed into a container for shipping.
"""


class PackedItem(SpApiBaseModel):
    """An item that has been packed into a container for shipping."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    item_sequence_number: Annotated[
        int,
        Field(
            ...,
            validation_alias=AliasChoices("itemSequenceNumber", "item_sequence_number"),
            serialization_alias="itemSequenceNumber",
            description="The sequence number of the item. The number must be the same as the order number of the item.",
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
            description="The buyer's Amazon Standard Identification Number (ASIN) of an item. Either `buyerProductIdentifier` or `vendorProductIdentifier` is required.",
        ),
    ]

    piece_number: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices("pieceNumber", "piece_number"),
            serialization_alias="pieceNumber",
            description="The piece number of the item in this container. This is required when the item is split across different containers.",
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
            description="An item's product identifier, which the vendor selects. This identifier should be the same as the identifier, such as a SKU, in the purchase order.",
        ),
    ]

    packed_quantity: Annotated[
        "ItemQuantity",
        Field(
            ...,
            validation_alias=AliasChoices("packedQuantity", "packed_quantity"),
            serialization_alias="packedQuantity",
            description="The total quantity of items that are packed in the shipment.",
        ),
    ]


# Enum definitions
class UnitOfMeasureEnum(str, Enum):
    """Enum for unitOfMeasure"""

    KG = "KG"  # Kilogram
    LB = "LB"  # Pounds (Libra for Latin).


"""
Weight

The weight.
"""


class Weight(SpApiBaseModel):
    """The weight."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    unit_of_measure: Annotated[
        UnitOfMeasureEnum,
        Field(
            ...,
            validation_alias=AliasChoices("unitOfMeasure", "unit_of_measure"),
            serialization_alias="unitOfMeasure",
            description="The unit of measurement.",
        ),
    ]

    value: Annotated["Decimal", Field(..., description="The measurement value.")]


# Enum definitions
class ContainerTypeEnum(str, Enum):
    """Enum for containerType"""

    CARTON = (
        "Carton"  # A packing container type that is typically used for drinks or food.
    )
    PALLET = "Pallet"  # A flat transport structure which supports goods in a stable fashion while being lifted by a forklift.


"""
Container

A container used for shipping and packing items.
"""


class Container(SpApiBaseModel):
    """A container used for shipping and packing items."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    container_type: Annotated[
        ContainerTypeEnum,
        Field(
            ...,
            validation_alias=AliasChoices("containerType", "container_type"),
            serialization_alias="containerType",
            description="The type of container.",
        ),
    ]

    container_identifier: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices(
                "containerIdentifier", "container_identifier"
            ),
            serialization_alias="containerIdentifier",
            description="The container identifier.",
        ),
    ]

    tracking_number: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("trackingNumber", "tracking_number"),
            serialization_alias="trackingNumber",
            description="The tracking number.",
        ),
    ]

    manifest_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("manifestId", "manifest_id"),
            serialization_alias="manifestId",
            description="The manifest identifier.",
        ),
    ]

    manifest_date: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("manifestDate", "manifest_date"),
            serialization_alias="manifestDate",
            description="The date of the manifest.",
        ),
    ]

    ship_method: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("shipMethod", "ship_method"),
            serialization_alias="shipMethod",
            description="The shipment method. This property is required when calling the `submitShipmentConfirmations` operation, and optional otherwise.",
        ),
    ]

    scac_code: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("scacCode", "scac_code"),
            serialization_alias="scacCode",
            description="SCAC code required for NA VOC vendors only.",
        ),
    ]

    carrier: Annotated[
        Optional[str],
        Field(None, description="Carrier required for EU VOC vendors only."),
    ]

    container_sequence_number: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices(
                "containerSequenceNumber", "container_sequence_number"
            ),
            serialization_alias="containerSequenceNumber",
            description="An integer that must be submitted for multi-box shipments only, where one item may come in separate packages.",
        ),
    ]

    dimensions: Annotated[
        Optional["Dimensions"],
        Field(
            None,
        ),
    ]

    weight: Annotated[
        "Weight",
        Field(
            ...,
        ),
    ]

    packed_items: Annotated[
        List["PackedItem"],
        Field(
            ...,
            validation_alias=AliasChoices("packedItems", "packed_items"),
            serialization_alias="packedItems",
            description="A list of packed items.",
        ),
    ]


ContainerLabelFormat = str
"""The format of the container label."""


"""
ContainerLabel

The details of the container label.
"""


class ContainerLabel(SpApiBaseModel):
    """The details of the container label."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    container_tracking_number: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "containerTrackingNumber", "container_tracking_number"
            ),
            serialization_alias="containerTrackingNumber",
            description="The container (pallet) tracking identifier from the shipping carrier.",
        ),
    ]

    content: Annotated[
        str,
        Field(
            ..., description="The container label content encoded into a Base64 string."
        ),
    ]

    format: Annotated[
        "ContainerLabelFormat",
        Field(..., description="The format of the container label."),
    ]


Packages = List["Package"]
"""An array of package objects in a container."""


# Enum definitions
class TaxRegistrationTypeEnum(str, Enum):
    """Enum for taxRegistrationType"""

    VAT = "VAT"  # Value-added tax.
    GST = "GST"  # Goods and Services Tax (GST).


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

The name, address, and tax details of a party.
"""


class PartyIdentification(SpApiBaseModel):
    """The name, address, and tax details of a party."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    party_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("partyId", "party_id"),
            serialization_alias="partyId",
            description="The identifier of the party.",
        ),
    ]

    address: Annotated[
        Optional["Address"], Field(None, description="The address of the party.")
    ]

    tax_registration_details: Annotated[
        Optional[List["TaxRegistrationDetails"]],
        Field(
            None,
            validation_alias=AliasChoices(
                "taxRegistrationDetails", "tax_registration_details"
            ),
            serialization_alias="taxRegistrationDetails",
            description="The tax registration details of the party.",
        ),
    ]


VendorContainerId = str
"""The unique, vendor-provided identifier for the container."""


"""
CreateContainerLabelRequestBody

The request body schema for the `createContainerLabel` operation.
"""


class CreateContainerLabelRequestBody(SpApiBaseModel):
    """The request body schema for the `createContainerLabel` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    selling_party: Annotated[
        "PartyIdentification",
        Field(
            ...,
            validation_alias=AliasChoices("sellingParty", "selling_party"),
            serialization_alias="sellingParty",
            description="The ID of the selling party or vendor.",
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

    carrier_id: Annotated[
        "CarrierId",
        Field(
            ...,
            validation_alias=AliasChoices("carrierId", "carrier_id"),
            serialization_alias="carrierId",
            description="The container (pallet) label's carrier.",
        ),
    ]

    vendor_container_id: Annotated[
        "VendorContainerId",
        Field(
            ...,
            validation_alias=AliasChoices("vendorContainerId", "vendor_container_id"),
            serialization_alias="vendorContainerId",
            description="The vendor's unique identifier for the container.",
        ),
    ]

    packages: Annotated[
        "Packages",
        Field(
            ...,
            description="An array of package objects that associate shipment packages with a container.",
        ),
    ]


"""
CreateContainerLabelRequest

Request parameters for createContainerLabel
"""


class CreateContainerLabelRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for createContainerLabel
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    body: Annotated[
        "CreateContainerLabelRequestBody",
        BodyParam(),
        Field(
            ...,
            description="[BODY] RequestBody body containing the container label data.",
        ),
    ]


"""
CreateContainerLabelResponse

The response schema for the `createContainerLabel` operation.
"""


class CreateContainerLabelResponse(SpApiBaseModel):
    """The response schema for the `createContainerLabel` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    container_label: Annotated[
        "ContainerLabel",
        Field(
            ...,
            validation_alias=AliasChoices("containerLabel", "container_label"),
            serialization_alias="containerLabel",
            description="The label data for the container label.",
        ),
    ]


"""
CreateShippingLabelsRequestBody

The request body for the createShippingLabels operation.
"""


class CreateShippingLabelsRequestBody(SpApiBaseModel):
    """The request body for the createShippingLabels operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    selling_party: Annotated[
        "PartyIdentification",
        Field(
            ...,
            validation_alias=AliasChoices("sellingParty", "selling_party"),
            serialization_alias="sellingParty",
            description="ID of the selling party or vendor.",
        ),
    ]

    ship_from_party: Annotated[
        "PartyIdentification",
        Field(
            ...,
            validation_alias=AliasChoices("shipFromParty", "ship_from_party"),
            serialization_alias="shipFromParty",
            description="Warehouse code of vendor.",
        ),
    ]

    containers: Annotated[
        Optional[List["Container"]],
        Field(None, description="A list of the packages in this shipment."),
    ]


"""
CreateShippingLabelsRequest

Request parameters for createShippingLabels
"""


class CreateShippingLabelsRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for createShippingLabels
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
            description="[PATH] The purchase order number for which you want to return the shipping labels. It should be the same number as the `purchaseOrderNumber` in the order.",
        ),
    ]

    body: Annotated[
        "CreateShippingLabelsRequestBody",
        BodyParam(),
        Field(
            ...,
            description="[BODY] The request payload that contains the parameters for creating shipping labels.",
        ),
    ]


"""
CustomerInvoice

Represents a customer invoice associated with a purchase order.
"""


class CustomerInvoice(SpApiBaseModel):
    """Represents a customer invoice associated with a purchase order."""

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
            description="The purchase order number for this order.",
        ),
    ]

    content: Annotated[str, Field(..., description="The Base64 customer invoice.")]


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
            description="Pagination occurs when a request produces a response that exceeds the `pageSize`. This means that the response is divided into individual pages. To retrieve the next page or the previous page, you must pass the `nextToken` value or the `previousToken` value as the `pageToken` parameter in the next request. There is no `nextToken` in the pagination object on the last page.",
        ),
    ]


"""
CustomerInvoiceList

Represents a list of customer invoices, potentially paginated.
"""


class CustomerInvoiceList(SpApiBaseModel):
    """Represents a list of customer invoices, potentially paginated."""

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

    customer_invoices: Annotated[
        Optional[List["CustomerInvoice"]],
        Field(
            None,
            validation_alias=AliasChoices("customerInvoices", "customer_invoices"),
            serialization_alias="customerInvoices",
            description="Represents a customer invoice within the `CustomerInvoiceList`.",
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
            description="An array of Error objects representing individual errors encountered during the request.",
        ),
    ]


"""
GetCustomerInvoiceRequest

Request parameters for getCustomerInvoice
"""


class GetCustomerInvoiceRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getCustomerInvoice
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
            description="[PATH] Purchase order number of the shipment for which to return the invoice.",
        ),
    ]


# Enum definitions
class SortOrderEnum(str, Enum):
    """Enum for sortOrder"""

    ASC = "ASC"  # Sort in ascending order by packing slip creation date.
    DESC = "DESC"  # Sort in descending order by packing slip creation date.


"""
GetCustomerInvoicesRequest

Request parameters for getCustomerInvoices
"""


class GetCustomerInvoicesRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getCustomerInvoices
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
            description="[QUERY] The vendor warehouseId for order fulfillment. If not specified, the result will contain orders for all warehouses.",
        ),
    ]

    limit: Annotated[
        Optional[int],
        QueryParam(),
        Field(None, description="[QUERY] The limit to the number of records returned"),
    ]

    created_after: Annotated[
        datetime,
        QueryParam(),
        Field(
            ...,
            validation_alias=AliasChoices("createdAfter", "created_after"),
            serialization_alias="createdAfter",
            description="[QUERY] Orders that became available after this date and time will be included in the result. Values are in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format.",
        ),
    ]

    created_before: Annotated[
        datetime,
        QueryParam(),
        Field(
            ...,
            validation_alias=AliasChoices("createdBefore", "created_before"),
            serialization_alias="createdBefore",
            description="[QUERY] Orders that became available before this date and time will be included in the result. Values are in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format.",
        ),
    ]

    sort_order: Annotated[
        Optional[SortOrderEnum],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("sortOrder", "sort_order"),
            serialization_alias="sortOrder",
            description="[QUERY] Sort ASC or DESC by order creation date.",
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


"""
GetPackingSlipRequest

Request parameters for getPackingSlip
"""


class GetPackingSlipRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getPackingSlip
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
            description="[PATH] The `purchaseOrderNumber` for the packing slip that you want.",
        ),
    ]


# Enum definitions
class SortOrderEnum(str, Enum):
    """Enum for sortOrder"""

    ASC = "ASC"  # Sort in ascending order by packing slip creation date.
    DESC = "DESC"  # Sort in descending order by packing slip creation date.


"""
GetPackingSlipsRequest

Request parameters for getPackingSlips
"""


class GetPackingSlipsRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getPackingSlips
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
            description="[QUERY] The vendor `warehouseId` for order fulfillment. If not specified, the result contains orders for all warehouses.",
        ),
    ]

    limit: Annotated[
        Optional[int],
        QueryParam(),
        Field(None, description="[QUERY] The maximum number of records to return."),
    ]

    created_after: Annotated[
        datetime,
        QueryParam(),
        Field(
            ...,
            validation_alias=AliasChoices("createdAfter", "created_after"),
            serialization_alias="createdAfter",
            description="[QUERY] Packing slips that become available after this date and time will be included in the result. Values are in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format.",
        ),
    ]

    created_before: Annotated[
        datetime,
        QueryParam(),
        Field(
            ...,
            validation_alias=AliasChoices("createdBefore", "created_before"),
            serialization_alias="createdBefore",
            description="[QUERY] Packing slips that became available before this date and time will be included in the result. Values are in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format.",
        ),
    ]

    sort_order: Annotated[
        Optional[SortOrderEnum],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("sortOrder", "sort_order"),
            serialization_alias="sortOrder",
            description="[QUERY] The packing slip creation dates, which are sorted by ascending or descending order.",
        ),
    ]

    next_token: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("nextToken", "next_token"),
            serialization_alias="nextToken",
            description="[QUERY] Used for pagination when there are more packing slips than the specified result size limit. The token value is returned in the previous API call.",
        ),
    ]


"""
GetShippingLabelRequest

Request parameters for getShippingLabel
"""


class GetShippingLabelRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getShippingLabel
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
            description="[PATH] The purchase order number for which you want to return the shipping label. It should be the same `purchaseOrderNumber` that you received in the order.",
        ),
    ]


# Enum definitions
class SortOrderEnum(str, Enum):
    """Enum for sortOrder"""

    ASC = "ASC"  # Sort in ascending order by packing slip creation date.
    DESC = "DESC"  # Sort in descending order by packing slip creation date.


"""
GetShippingLabelsRequest

Request parameters for getShippingLabels
"""


class GetShippingLabelsRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getShippingLabels
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
            description="[QUERY] The vendor `warehouseId` for order fulfillment. If not specified, the result contains orders for all warehouses.",
        ),
    ]

    limit: Annotated[
        Optional[int],
        QueryParam(),
        Field(None, description="[QUERY] The limit to the number of records returned."),
    ]

    created_after: Annotated[
        datetime,
        QueryParam(),
        Field(
            ...,
            validation_alias=AliasChoices("createdAfter", "created_after"),
            serialization_alias="createdAfter",
            description="[QUERY] Shipping labels that became available after this date and time will be included in the result. Values are in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format.",
        ),
    ]

    created_before: Annotated[
        datetime,
        QueryParam(),
        Field(
            ...,
            validation_alias=AliasChoices("createdBefore", "created_before"),
            serialization_alias="createdBefore",
            description="[QUERY] Shipping labels that became available before this date and time will be included in the result. Values are in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format.",
        ),
    ]

    sort_order: Annotated[
        Optional[SortOrderEnum],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("sortOrder", "sort_order"),
            serialization_alias="sortOrder",
            description="[QUERY] The sort order creation date. You can choose between ascending (`ASC`) or descending (`DESC`) sort order.",
        ),
    ]

    next_token: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("nextToken", "next_token"),
            serialization_alias="nextToken",
            description="[QUERY] Used for pagination when there are more ship labels than the specified result size limit. The token value is returned in the previous API call.",
        ),
    ]


"""
Item

Details of the item being shipped.
"""


class Item(SpApiBaseModel):
    """Details of the item being shipped."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    item_sequence_number: Annotated[
        int,
        Field(
            ...,
            validation_alias=AliasChoices("itemSequenceNumber", "item_sequence_number"),
            serialization_alias="itemSequenceNumber",
            description="The sequence number of the item. The number must be the same as the order number of the item.",
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
            description="The buyer's Amazon Standard Identification Number (ASIN) of an item. Either `buyerProductIdentifier` or `vendorProductIdentifier` is required.",
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
            description="An item's product identifier, which the vendor selects. This identifier should be the same as the identifier, such as a SKU, in the purchase order.",
        ),
    ]

    shipped_quantity: Annotated[
        "ItemQuantity",
        Field(
            ...,
            validation_alias=AliasChoices("shippedQuantity", "shipped_quantity"),
            serialization_alias="shippedQuantity",
            description="The total quantity of items that are in this shipment.",
        ),
    ]


"""
LabelData

Details of the shipment label.
"""


class LabelData(SpApiBaseModel):
    """Details of the shipment label."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    package_identifier: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("packageIdentifier", "package_identifier"),
            serialization_alias="packageIdentifier",
            description="Identifier for the package. The first package will be 001, the second 002, and so on. This number is used as a reference to refer to this package from the pallet level.",
        ),
    ]

    tracking_number: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("trackingNumber", "tracking_number"),
            serialization_alias="trackingNumber",
            description="Package tracking identifier from the shipping carrier.",
        ),
    ]

    ship_method: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("shipMethod", "ship_method"),
            serialization_alias="shipMethod",
            description="Ship method to be used for shipping the order. Amazon defines Ship Method Codes indicating shipping carrier and shipment service level. Ship Method Codes are case and format sensitive. The same ship method code should returned on the shipment confirmation. Note that the Ship Method Codes are vendor specific and will be provided to each vendor during the implementation.",
        ),
    ]

    ship_method_name: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("shipMethodName", "ship_method_name"),
            serialization_alias="shipMethodName",
            description="Shipping method name for internal reference.",
        ),
    ]

    content: Annotated[
        str,
        Field(
            ...,
            description="This field will contain the Base64 string of the shipment label content.",
        ),
    ]


"""
Package

The package that is associated with the container.
"""


class Package(SpApiBaseModel):
    """The package that is associated with the container."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    package_tracking_number: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices(
                "packageTrackingNumber", "package_tracking_number"
            ),
            serialization_alias="packageTrackingNumber",
            description="The tracking number on the label of shipment package, that you can fetch from the `shippingLabels` response. You can also scan the bar code on the shipping label to get the tracking number.",
        ),
    ]


# Enum definitions
class ContentTypeEnum(str, Enum):
    """Enum for contentType"""

    APPLICATION_PDF = "application/pdf"  # Portable Document Format (pdf).


"""
PackingSlip

Packing slip information.
"""


class PackingSlip(SpApiBaseModel):
    """Packing slip information."""

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
            description="Purchase order number of the shipment that the packing slip is for.",
        ),
    ]

    content: Annotated[
        str, Field(..., description="A Base64 string of the packing slip PDF.")
    ]

    content_type: Annotated[
        Optional[ContentTypeEnum],
        Field(
            None,
            validation_alias=AliasChoices("contentType", "content_type"),
            serialization_alias="contentType",
            description="The format of the file such as PDF, JPEG etc.",
        ),
    ]


"""
PackingSlipList

A list of packing slips.
"""


class PackingSlipList(SpApiBaseModel):
    """A list of packing slips."""

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

    packing_slips: Annotated[
        Optional[List["PackingSlip"]],
        Field(
            None,
            validation_alias=AliasChoices("packingSlips", "packing_slips"),
            serialization_alias="packingSlips",
            description="An array of packing slip objects.",
        ),
    ]


# Enum definitions
class ShipmentStatusEnum(str, Enum):
    """Enum for shipmentStatus"""

    SHIPPED = "SHIPPED"  # Orders that have left the warehouse have shipped status.
    FLOOR_DENIAL = "FLOOR_DENIAL"  # Status for orders rejected due to quality issues with products on the floor, or the physical and virtual inventory do not match.


"""
ShipmentDetails

Details about a shipment.
"""


class ShipmentDetails(SpApiBaseModel):
    """Details about a shipment."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    shipped_date: Annotated[
        datetime,
        Field(
            ...,
            validation_alias=AliasChoices("shippedDate", "shipped_date"),
            serialization_alias="shippedDate",
            description="The date of the shipment's departure from vendor's location. Vendors send ASNs within 30 minutes of departure from their warehouse/distribution center or six hours prior to the appointment time at the Amazon destination warehouse. The shipped date mentioned in the shipment confirmation cannot be in the future.",
        ),
    ]

    shipment_status: Annotated[
        ShipmentStatusEnum,
        Field(
            ...,
            validation_alias=AliasChoices("shipmentStatus", "shipment_status"),
            serialization_alias="shipmentStatus",
            description="The shipment status.",
        ),
    ]

    is_priority_shipment: Annotated[
        Optional[bool],
        Field(
            None,
            validation_alias=AliasChoices("isPriorityShipment", "is_priority_shipment"),
            serialization_alias="isPriorityShipment",
            description="Provide the priority of the shipment.",
        ),
    ]

    vendor_order_number: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("vendorOrderNumber", "vendor_order_number"),
            serialization_alias="vendorOrderNumber",
            description="The vendor order number is a unique identifier generated by a vendor for their reference.",
        ),
    ]

    estimated_delivery_date: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices(
                "estimatedDeliveryDate", "estimated_delivery_date"
            ),
            serialization_alias="estimatedDeliveryDate",
            description="The date on which the shipment is expected to reach the buyer's warehouse. The date is estimated based on the average transit time between the ship-from location and the destination. Usually, the exact appointment time is unknown when creating the shipment confirmation and is later provided by the buyer.",
        ),
    ]


"""
ShipmentConfirmation

Represents the confirmation details of a shipment, including the purchase order number and other shipment details.
"""


class ShipmentConfirmation(SpApiBaseModel):
    """Represents the confirmation details of a shipment, including the purchase order number and other shipment details."""

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
            description="Purchase order number corresponding to the shipment.",
        ),
    ]

    shipment_details: Annotated[
        "ShipmentDetails",
        Field(
            ...,
            validation_alias=AliasChoices("shipmentDetails", "shipment_details"),
            serialization_alias="shipmentDetails",
            description="Shipment information.",
        ),
    ]

    selling_party: Annotated[
        "PartyIdentification",
        Field(
            ...,
            validation_alias=AliasChoices("sellingParty", "selling_party"),
            serialization_alias="sellingParty",
            description="ID of the selling party or vendor.",
        ),
    ]

    ship_from_party: Annotated[
        "PartyIdentification",
        Field(
            ...,
            validation_alias=AliasChoices("shipFromParty", "ship_from_party"),
            serialization_alias="shipFromParty",
            description="Warehouse code of vendor.",
        ),
    ]

    items: Annotated[
        List["Item"],
        Field(
            ...,
            description="Provide the details of the items in this shipment. If any of the item details field is common at a package or a pallet level, then provide them at the corresponding package.",
        ),
    ]

    containers: Annotated[
        Optional[List["Container"]],
        Field(
            None,
            description="Provide the details of the items in this shipment. If any of the item details field is common at a package or a pallet level, then provide them at the corresponding package.",
        ),
    ]


"""
ShipmentSchedule

Details about the estimated delivery window.
"""


class ShipmentSchedule(SpApiBaseModel):
    """Details about the estimated delivery window."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    estimated_delivery_date_time: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices(
                "estimatedDeliveryDateTime", "estimated_delivery_date_time"
            ),
            serialization_alias="estimatedDeliveryDateTime",
            description="Date on which the shipment is expected to reach the customer delivery location. Values are in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format, with UTC time zone or UTC offset. For example, 2020-07-16T23:00:00Z or 2020-07-16T23:00:00+01:00.",
        ),
    ]

    appt_window_start_date_time: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices(
                "apptWindowStartDateTime", "appt_window_start_date_time"
            ),
            serialization_alias="apptWindowStartDateTime",
            description="The date and time at the start of the appointment window when the shipment is expected to be delivered. Values are in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format, with UTC time zone or UTC offset. For example, 2020-07-16T23:00:00Z or 2020-07-16T23:00:00+01:00.",
        ),
    ]

    appt_window_end_date_time: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices(
                "apptWindowEndDateTime", "appt_window_end_date_time"
            ),
            serialization_alias="apptWindowEndDateTime",
            description="The date and time at the end of the appointment window when the shipment is expected to be delivered. Values are in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format, with UTC time zone or UTC offset. For example, 2020-07-16T23:00:00Z or 2020-07-16T23:00:00+01:00.",
        ),
    ]


"""
StatusUpdateDetails

Details for the shipment status update given by the vendor for the specific package.
"""


class StatusUpdateDetails(SpApiBaseModel):
    """Details for the shipment status update given by the vendor for the specific package."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    tracking_number: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("trackingNumber", "tracking_number"),
            serialization_alias="trackingNumber",
            description="The shipment tracking number is required for every package and should match the `trackingNumber` sent for the shipment confirmation.",
        ),
    ]

    status_code: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("statusCode", "status_code"),
            serialization_alias="statusCode",
            description="Indicates the shipment status code of the package that provides transportation information for Amazon tracking systems and ultimately for the final customer. For more information, refer to the [Additional Fields Explanation](https://developer-docs.amazon.com/sp-api/docs/vendor-direct-fulfillment-shipping-api-use-case-guide#additional-fields-explanation).",
        ),
    ]

    reason_code: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("reasonCode", "reason_code"),
            serialization_alias="reasonCode",
            description="Provides a reason code for the status of the package that will provide additional information about the transportation status. For more information, refer to the [Additional Fields Explanation](https://developer-docs.amazon.com/sp-api/docs/vendor-direct-fulfillment-shipping-api-use-case-guide#additional-fields-explanation).",
        ),
    ]

    status_date_time: Annotated[
        datetime,
        Field(
            ...,
            validation_alias=AliasChoices("statusDateTime", "status_date_time"),
            serialization_alias="statusDateTime",
            description="The date and time when the shipment status was updated. Values are in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format, with UTC time zone or UTC offset. For example, 2020-07-16T23:00:00Z or 2020-07-16T23:00:00+01:00.",
        ),
    ]

    status_location_address: Annotated[
        "Address",
        Field(
            ...,
            validation_alias=AliasChoices(
                "statusLocationAddress", "status_location_address"
            ),
            serialization_alias="statusLocationAddress",
        ),
    ]

    shipment_schedule: Annotated[
        Optional["ShipmentSchedule"],
        Field(
            None,
            validation_alias=AliasChoices("shipmentSchedule", "shipment_schedule"),
            serialization_alias="shipmentSchedule",
        ),
    ]


"""
ShipmentStatusUpdate

Represents an update to the status of a shipment.
"""


class ShipmentStatusUpdate(SpApiBaseModel):
    """Represents an update to the status of a shipment."""

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
            description="Purchase order number of the shipment for which to update the shipment status.",
        ),
    ]

    selling_party: Annotated[
        "PartyIdentification",
        Field(
            ...,
            validation_alias=AliasChoices("sellingParty", "selling_party"),
            serialization_alias="sellingParty",
            description="ID of the selling party or vendor.",
        ),
    ]

    ship_from_party: Annotated[
        "PartyIdentification",
        Field(
            ...,
            validation_alias=AliasChoices("shipFromParty", "ship_from_party"),
            serialization_alias="shipFromParty",
            description="Warehouse code of vendor.",
        ),
    ]

    status_update_details: Annotated[
        "StatusUpdateDetails",
        Field(
            ...,
            validation_alias=AliasChoices(
                "statusUpdateDetails", "status_update_details"
            ),
            serialization_alias="statusUpdateDetails",
            description="Provide the details about the status of the shipment at that particular point of time.",
        ),
    ]


# Enum definitions
class LabelFormatEnum(str, Enum):
    """Enum for labelFormat"""

    PNG = "PNG"  # Portable Network Graphics (png) format.
    ZPL = "ZPL"  # Zebra Programming Language (zpl) format.


"""
ShippingLabel

Shipping label information for an order, including the purchase order number, selling party, ship from party, label format, and package details.
"""


class ShippingLabel(SpApiBaseModel):
    """Shipping label information for an order, including the purchase order number, selling party, ship from party, label format, and package details."""

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
            description="This field will contain the Purchase Order Number for this order.",
        ),
    ]

    selling_party: Annotated[
        "PartyIdentification",
        Field(
            ...,
            validation_alias=AliasChoices("sellingParty", "selling_party"),
            serialization_alias="sellingParty",
            description="ID of the selling party or vendor.",
        ),
    ]

    ship_from_party: Annotated[
        "PartyIdentification",
        Field(
            ...,
            validation_alias=AliasChoices("shipFromParty", "ship_from_party"),
            serialization_alias="shipFromParty",
            description="Warehouse code of vendor.",
        ),
    ]

    label_format: Annotated[
        LabelFormatEnum,
        Field(
            ...,
            validation_alias=AliasChoices("labelFormat", "label_format"),
            serialization_alias="labelFormat",
            description="Format of the label.",
        ),
    ]

    label_data: Annotated[
        List["LabelData"],
        Field(
            ...,
            validation_alias=AliasChoices("labelData", "label_data"),
            serialization_alias="labelData",
            description="Provides the details of the packages in this shipment.",
        ),
    ]


"""
ShippingLabelList

Response payload with the list of shipping labels.
"""


class ShippingLabelList(SpApiBaseModel):
    """Response payload with the list of shipping labels."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    pagination: Annotated[
        Optional["Pagination"],
        Field(
            None,
        ),
    ]

    shipping_labels: Annotated[
        Optional[List["ShippingLabel"]],
        Field(
            None,
            validation_alias=AliasChoices("shippingLabels", "shipping_labels"),
            serialization_alias="shippingLabels",
            description="An array containing the details of the generated shipping labels.",
        ),
    ]


"""
ShippingLabelRequestBody

Represents the request payload for creating a shipping label, containing the purchase order number, selling party, ship from party, and a list of containers or packages in the shipment.
"""


class ShippingLabelRequestBody(SpApiBaseModel):
    """Represents the request payload for creating a shipping label, containing the purchase order number, selling party, ship from party, and a list of containers or packages in the shipment."""

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
            description="The purchase order number of the order for which to create a shipping label.",
        ),
    ]

    selling_party: Annotated[
        "PartyIdentification",
        Field(
            ...,
            validation_alias=AliasChoices("sellingParty", "selling_party"),
            serialization_alias="sellingParty",
            description="The ID of the selling party or vendor.",
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

    containers: Annotated[
        Optional[List["Container"]],
        Field(None, description="A list of the packages in this shipment."),
    ]


"""
SubmitShipmentConfirmationsRequestBody

The request schema for the submitShipmentConfirmations operation.
"""


class SubmitShipmentConfirmationsRequestBody(SpApiBaseModel):
    """The request schema for the submitShipmentConfirmations operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    shipment_confirmations: Annotated[
        Optional[List["ShipmentConfirmation"]],
        Field(
            None,
            validation_alias=AliasChoices(
                "shipmentConfirmations", "shipment_confirmations"
            ),
            serialization_alias="shipmentConfirmations",
            description="Array of `ShipmentConfirmation` objects. Each `ShipmentConfirmation` object represents the confirmation details for a specific shipment.",
        ),
    ]


"""
SubmitShipmentConfirmationsRequest

Request parameters for submitShipmentConfirmations
"""


class SubmitShipmentConfirmationsRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for submitShipmentConfirmations
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    body: Annotated[
        "SubmitShipmentConfirmationsRequestBody",
        BodyParam(),
        Field(
            ...,
            description="[BODY] RequestBody body containing the shipment confirmations data.",
        ),
    ]


"""
SubmitShipmentStatusUpdatesRequestBody

The request schema for the `submitShipmentStatusUpdates` operation.
"""


class SubmitShipmentStatusUpdatesRequestBody(SpApiBaseModel):
    """The request schema for the `submitShipmentStatusUpdates` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    shipment_status_updates: Annotated[
        Optional[List["ShipmentStatusUpdate"]],
        Field(
            None,
            validation_alias=AliasChoices(
                "shipmentStatusUpdates", "shipment_status_updates"
            ),
            serialization_alias="shipmentStatusUpdates",
            description="Contains a list of one or more `ShipmentStatusUpdate` objects. Each `ShipmentStatusUpdate` object represents an update to the status of a specific shipment.",
        ),
    ]


"""
SubmitShipmentStatusUpdatesRequest

Request parameters for submitShipmentStatusUpdates
"""


class SubmitShipmentStatusUpdatesRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for submitShipmentStatusUpdates
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    body: Annotated[
        "SubmitShipmentStatusUpdatesRequestBody",
        BodyParam(),
        Field(
            ...,
            description="[BODY] RequestBody body containing the shipment status update data.",
        ),
    ]


"""
SubmitShippingLabelsRequestBody

The request schema for the `submitShippingLabelRequest` operation.
"""


class SubmitShippingLabelsRequestBody(SpApiBaseModel):
    """The request schema for the `submitShippingLabelRequest` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    shipping_label_requests: Annotated[
        Optional[List["ShippingLabelRequestBody"]],
        Field(
            None,
            validation_alias=AliasChoices(
                "shippingLabelRequests", "shipping_label_requests"
            ),
            serialization_alias="shippingLabelRequests",
            description="An array of shipping label requests to be processed.",
        ),
    ]


"""
SubmitShippingLabelRequestBodyRequest

Request parameters for submitShippingLabelRequestBody
"""


class SubmitShippingLabelRequestBodyRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for submitShippingLabelRequestBody
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    body: Annotated[
        "SubmitShippingLabelsRequestBody",
        BodyParam(),
        Field(
            ...,
            description="[BODY] The request body that contains the shipping labels data.",
        ),
    ]


"""
TransactionReference

Response containing the transaction ID.
"""


class TransactionReference(SpApiBaseModel):
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
            description="GUID to identify this transaction. This value can be used with the Transaction Status API to return the status of this transaction.",
        ),
    ]


# Rebuild models to resolve forward references
PackingSlip.model_rebuild()
PackingSlipList.model_rebuild()
CreateShippingLabelsRequestBody.model_rebuild()
SubmitShippingLabelsRequestBody.model_rebuild()
ShippingLabelRequestBody.model_rebuild()
Item.model_rebuild()
PackedItem.model_rebuild()
PartyIdentification.model_rebuild()
ShipmentDetails.model_rebuild()
StatusUpdateDetails.model_rebuild()
TaxRegistrationDetails.model_rebuild()
Address.model_rebuild()
ShipmentSchedule.model_rebuild()
Dimensions.model_rebuild()
Weight.model_rebuild()
ItemQuantity.model_rebuild()
ShippingLabelList.model_rebuild()
LabelData.model_rebuild()
ShippingLabel.model_rebuild()
SubmitShipmentConfirmationsRequestBody.model_rebuild()
ShipmentConfirmation.model_rebuild()
SubmitShipmentStatusUpdatesRequestBody.model_rebuild()
ShipmentStatusUpdate.model_rebuild()
CustomerInvoiceList.model_rebuild()
Pagination.model_rebuild()
CustomerInvoice.model_rebuild()
TransactionReference.model_rebuild()
ErrorList.model_rebuild()
Error.model_rebuild()
Container.model_rebuild()
CreateContainerLabelRequestBody.model_rebuild()
Package.model_rebuild()
CreateContainerLabelResponse.model_rebuild()
ContainerLabel.model_rebuild()
GetShippingLabelsRequest.model_rebuild()
SubmitShippingLabelRequestBodyRequest.model_rebuild()
GetShippingLabelRequest.model_rebuild()
CreateShippingLabelsRequest.model_rebuild()
SubmitShipmentConfirmationsRequest.model_rebuild()
SubmitShipmentStatusUpdatesRequest.model_rebuild()
GetCustomerInvoicesRequest.model_rebuild()
GetCustomerInvoiceRequest.model_rebuild()
GetPackingSlipsRequest.model_rebuild()
GetPackingSlipRequest.model_rebuild()
CreateContainerLabelRequest.model_rebuild()
