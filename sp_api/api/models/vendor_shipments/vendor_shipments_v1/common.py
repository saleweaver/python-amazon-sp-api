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
            description="The two digit country code in ISO 3166-1 alpha-2 format.",
        ),
    ]

    phone: Annotated[
        Optional[str],
        Field(
            None,
            description="The phone number of the person, business or institution located at that address.",
        ),
    ]


"""
CarrierDetails

Indicates the carrier details and their contact informations
"""


class CarrierDetails(SpApiBaseModel):
    """Indicates the carrier details and their contact informations"""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    name: Annotated[
        Optional[str],
        Field(
            None,
            description="The field is used to represent the carrier used for performing the shipment.",
        ),
    ]

    code: Annotated[
        Optional[str],
        Field(
            None,
            description="Code that identifies the carrier for the shipment. The Standard Carrier Alpha Code (SCAC) is a unique two to four letter code used to identify a carrier. Carrier SCAC codes are assigned and maintained by the NMFTA (National Motor Freight Association).",
        ),
    ]

    phone: Annotated[
        Optional[str],
        Field(
            None,
            description="The field is used to represent the Carrier contact number.",
        ),
    ]

    email: Annotated[
        Optional[str],
        Field(None, description="The field is used to represent the carrier Email id."),
    ]

    shipment_reference_number: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "shipmentReferenceNumber", "shipment_reference_number"
            ),
            serialization_alias="shipmentReferenceNumber",
            description="The field is also known as PRO number is a unique number assigned by the carrier. It is used to identify and track the shipment that goes out for delivery. This field is mandatory for US, CA, MX shipment confirmations.",
        ),
    ]


# Enum definitions
class ContainerIdentificationContainerIdentificationTypeEnum(str, Enum):
    """Enum for containerIdentificationType"""

    SSCC = "SSCC"  # 2 Digit Application Identifier (00) followed by unique 18-digit Serial Shipment Container Code (SSCC) to be included to define a pallet/carton and to identify its contents.
    AMZNCC = "AMZNCC"  # Amazon Container Code - a substitute for a SSCC that is generated by Amazon for small vendors and associated with a pallet/carton label.
    GTIN = "GTIN"  # Global Trade Identification Number (part of the standard GS1 barcoding and product identification system).
    BPS = "BPS"  # Barcode Packing Slip.
    CID = "CID"  # Container identifier for import shipments.


"""
ContainerIdentification

A list of carton identifiers.
"""


class ContainerIdentification(SpApiBaseModel):
    """A list of carton identifiers."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    container_identification_type: Annotated[
        ContainerIdentificationContainerIdentificationTypeEnum,
        Field(
            ...,
            validation_alias=AliasChoices(
                "containerIdentificationType", "container_identification_type"
            ),
            serialization_alias="containerIdentificationType",
            description="The container identification type.",
        ),
    ]

    container_identification_number: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices(
                "containerIdentificationNumber", "container_identification_number"
            ),
            serialization_alias="containerIdentificationNumber",
            description="Container identification number that adheres to the definition of the container identification type.",
        ),
    ]


# Enum definitions
class DurationDurationUnitEnum(str, Enum):
    """Enum for durationUnit"""

    DAYS = "Days"  # Days
    MONTHS = "Months"  # Months


"""
Duration

Duration after manufacturing date during which the product is valid for consumption.
"""


class Duration(SpApiBaseModel):
    """Duration after manufacturing date during which the product is valid for consumption."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    duration_unit: Annotated[
        DurationDurationUnitEnum,
        Field(
            ...,
            validation_alias=AliasChoices("durationUnit", "duration_unit"),
            serialization_alias="durationUnit",
            description="Unit for duration.",
        ),
    ]

    duration_value: Annotated[
        int,
        Field(
            ...,
            validation_alias=AliasChoices("durationValue", "duration_value"),
            serialization_alias="durationValue",
            description="Value for the duration in terms of the durationUnit.",
        ),
    ]


"""
Expiry

Expiry refers to the collection of dates required for certain items. These could be either expiryDate or mfgDate and expiryAfterDuration. These are mandatory for perishable items.
"""


class Expiry(SpApiBaseModel):
    """Expiry refers to the collection of dates required for certain items. These could be either expiryDate or mfgDate and expiryAfterDuration. These are mandatory for perishable items."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    manufacturer_date: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices("manufacturerDate", "manufacturer_date"),
            serialization_alias="manufacturerDate",
            description="Production, packaging or assembly date determined by the manufacturer. Its meaning is determined based on the trade item context.",
        ),
    ]

    expiry_date: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices("expiryDate", "expiry_date"),
            serialization_alias="expiryDate",
            description="The date that determines the limit of consumption or use of a product. Its meaning is determined based on the trade item context.",
        ),
    ]

    expiry_after_duration: Annotated[
        Optional["Duration"],
        Field(
            None,
            validation_alias=AliasChoices(
                "expiryAfterDuration", "expiry_after_duration"
            ),
            serialization_alias="expiryAfterDuration",
            description="Duration after manufacturing date during which the product is valid for consumption.",
        ),
    ]


Decimal = str
"""A decimal number with no loss of precision. Useful when precision loss is unacceptable, as with currencies. Follows RFC7159 for number representation. <br>**Pattern** : `^-?(0|([1-9]d*))(.d+)?([eE][+-]?d+)?$`."""


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
        str,
        Field(
            ...,
            validation_alias=AliasChoices("currencyCode", "currency_code"),
            serialization_alias="currencyCode",
            description="Three digit currency code in ISO 4217 format.",
        ),
    ]

    amount: Annotated[
        "Decimal",
        Field(
            ...,
        ),
    ]


# Enum definitions
class ItemDetailsHandlingCodeEnum(str, Enum):
    """Enum for handlingCode"""

    OVERSIZED = "Oversized"  # A package weighing 150 pounds or less and measuring greater than 130 inches in length and girth is classified as an oversized package.
    FRAGILE = "Fragile"  # A package containing easily breakable items.
    FOOD = "Food"  # A package containing edible items.
    HANDLE_WITH_CARE = (
        "HandleWithCare"  # A package containing fragile or dangerous items.
    )


"""
ItemDetails

Item details for be provided for every item in shipment at either the item or carton or pallet level, whichever is appropriate.
"""


class ItemDetails(SpApiBaseModel):
    """Item details for be provided for every item in shipment at either the item or carton or pallet level, whichever is appropriate."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    purchase_order_number: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "purchaseOrderNumber", "purchase_order_number"
            ),
            serialization_alias="purchaseOrderNumber",
            description="The purchase order number for the shipment being confirmed. If the items in this shipment belong to multiple purchase order numbers that are in particular carton or pallet within the shipment, then provide the purchaseOrderNumber at the appropriate carton or pallet level. Formatting Notes: 8-character alpha-numeric code.",
        ),
    ]

    lot_number: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("lotNumber", "lot_number"),
            serialization_alias="lotNumber",
            description="The batch or lot number associates an item with information the manufacturer considers relevant for traceability of the trade item to which the Element String is applied. The data may refer to the trade item itself or to items contained. This field is mandatory for all perishable items.",
        ),
    ]

    expiry: Annotated[
        Optional["Expiry"],
        Field(
            None,
            description="Expiry refers to the collection of dates required for certain items. These could be either expiryDate or mfgDate and expiryAfterDuration. These are mandatory for perishable items.",
        ),
    ]

    maximum_retail_price: Annotated[
        Optional["Money"],
        Field(
            None,
            validation_alias=AliasChoices("maximumRetailPrice", "maximum_retail_price"),
            serialization_alias="maximumRetailPrice",
            description="Maximum retail price of the item being shipped.",
        ),
    ]

    handling_code: Annotated[
        Optional[ItemDetailsHandlingCodeEnum],
        Field(
            None,
            validation_alias=AliasChoices("handlingCode", "handling_code"),
            serialization_alias="handlingCode",
            description="Identification of the instructions on how specified item/carton/pallet should be handled.",
        ),
    ]


# Enum definitions
class TotalWeightUnitOfMeasureEnum(str, Enum):
    """Enum for unitOfMeasure"""

    POUNDS = "POUNDS"  # The weight is measured in pounds.
    OUNCES = "OUNCES"  # The weight is measured in ounces.
    GRAMS = "GRAMS"  # The weight is measured in grams.
    KILOGRAMS = "KILOGRAMS"  # The weight is measured in kilograms.


"""
TotalWeight

The total weight of units that are sold by weight in a shipment.
"""


class TotalWeight(SpApiBaseModel):
    """The total weight of units that are sold by weight in a shipment."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    unit_of_measure: Annotated[
        TotalWeightUnitOfMeasureEnum,
        Field(
            ...,
            validation_alias=AliasChoices("unitOfMeasure", "unit_of_measure"),
            serialization_alias="unitOfMeasure",
            description="The unit of measure for the weight of items that are ordered by cases and support pricing by weight.",
        ),
    ]

    amount: Annotated[
        "Decimal",
        Field(
            ...,
        ),
    ]


# Enum definitions
class ItemQuantityUnitOfMeasureEnum(str, Enum):
    """Enum for unitOfMeasure"""

    CASES = "Cases"  # Packing of individual items into a case.
    EACHES = "Eaches"  # Individual items.


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
            description="Amount of units shipped for a specific item at a shipment level. If the item is present only in certain cartons or pallets within the shipment, please provide this at the appropriate carton or pallet level.",
        ),
    ]

    unit_of_measure: Annotated[
        ItemQuantityUnitOfMeasureEnum,
        Field(
            ...,
            validation_alias=AliasChoices("unitOfMeasure", "unit_of_measure"),
            serialization_alias="unitOfMeasure",
            description="Unit of measure for the shipped quantity.",
        ),
    ]

    unit_size: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices("unitSize", "unit_size"),
            serialization_alias="unitSize",
            description="The case size, in the event that we ordered using cases. Otherwise, 1.",
        ),
    ]

    total_weight: Annotated[
        Optional["TotalWeight"],
        Field(
            None,
            validation_alias=AliasChoices("totalWeight", "total_weight"),
            serialization_alias="totalWeight",
        ),
    ]


"""
ContainerItem

Carton/Pallet level details for the item.
"""


class ContainerItem(SpApiBaseModel):
    """Carton/Pallet level details for the item."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    item_reference: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("itemReference", "item_reference"),
            serialization_alias="itemReference",
            description="The reference number for the item. Please provide the itemSequenceNumber from the 'items' segment to refer to that item's details here.",
        ),
    ]

    shipped_quantity: Annotated[
        "ItemQuantity",
        Field(
            ...,
            validation_alias=AliasChoices("shippedQuantity", "shipped_quantity"),
            serialization_alias="shippedQuantity",
            description="Total item quantity shipped in this carton/pallet.",
        ),
    ]

    item_details: Annotated[
        Optional["ItemDetails"],
        Field(
            None,
            validation_alias=AliasChoices("itemDetails", "item_details"),
            serialization_alias="itemDetails",
        ),
    ]


# Enum definitions
class DimensionsUnitOfMeasureEnum(str, Enum):
    """Enum for unitOfMeasure"""

    IN = "In"  # Inches
    FT = "Ft"  # Feet
    METER = "Meter"  # Meters
    YARD = "Yard"  # Yards


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
        DimensionsUnitOfMeasureEnum,
        Field(
            ...,
            validation_alias=AliasChoices("unitOfMeasure", "unit_of_measure"),
            serialization_alias="unitOfMeasure",
            description="The unit of measure for dimensions.",
        ),
    ]


# Enum definitions
class WeightUnitOfMeasureEnum(str, Enum):
    """Enum for unitOfMeasure"""

    G = "G"  # Grams
    KG = "Kg"  # Kilograms
    OZ = "Oz"  # Ounces
    LB = "Lb"  # Pounds


"""
Weight

The weight of the shipment.
"""


class Weight(SpApiBaseModel):
    """The weight of the shipment."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    unit_of_measure: Annotated[
        WeightUnitOfMeasureEnum,
        Field(
            ...,
            validation_alias=AliasChoices("unitOfMeasure", "unit_of_measure"),
            serialization_alias="unitOfMeasure",
            description="The unit of measurement.",
        ),
    ]

    value: Annotated["Decimal", Field(..., description="The measurement value.")]


"""
Carton

Details of the carton/package being shipped.
"""


class Carton(SpApiBaseModel):
    """Details of the carton/package being shipped."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    carton_identifiers: Annotated[
        Optional[List["ContainerIdentification"]],
        Field(
            None,
            validation_alias=AliasChoices("cartonIdentifiers", "carton_identifiers"),
            serialization_alias="cartonIdentifiers",
            description="A list of carton identifiers.",
        ),
    ]

    carton_sequence_number: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices(
                "cartonSequenceNumber", "carton_sequence_number"
            ),
            serialization_alias="cartonSequenceNumber",
            description="Carton sequence number for the carton. The first carton will be 001, the second 002, and so on. This number is used as a reference to refer to this carton from the pallet level.",
        ),
    ]

    dimensions: Annotated[
        Optional["Dimensions"],
        Field(
            None,
        ),
    ]

    weight: Annotated[
        Optional["Weight"],
        Field(
            None,
        ),
    ]

    tracking_number: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("trackingNumber", "tracking_number"),
            serialization_alias="trackingNumber",
            description="This is required to be provided for every carton in the small parcel shipments.",
        ),
    ]

    items: Annotated[
        List["ContainerItem"],
        Field(..., description="A list of container item details."),
    ]


"""
CartonReferenceDetails

Carton reference details.
"""


class CartonReferenceDetails(SpApiBaseModel):
    """Carton reference details."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    carton_count: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices("cartonCount", "carton_count"),
            serialization_alias="cartonCount",
            description="Pallet level carton count is mandatory for single item pallet and optional for mixed item pallet.",
        ),
    ]

    carton_reference_numbers: Annotated[
        List["str"],
        Field(
            ...,
            validation_alias=AliasChoices(
                "cartonReferenceNumbers", "carton_reference_numbers"
            ),
            serialization_alias="cartonReferenceNumbers",
            description="Array of reference numbers for the carton that are part of this pallet/shipment. Please provide the cartonSequenceNumber from the 'cartons' segment to refer to that carton's details here.",
        ),
    ]


"""
CollectFreightPickupDetails

Transport RequestBody pickup date from Vendor Warehouse by Buyer
"""


class CollectFreightPickupDetails(SpApiBaseModel):
    """Transport RequestBody pickup date from Vendor Warehouse by Buyer"""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    requested_pick_up: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices("requestedPickUp", "requested_pick_up"),
            serialization_alias="requestedPickUp",
            description="Date on which the items can be picked up from vendor warehouse by Buyer used for WePay/Collect vendors.",
        ),
    ]

    scheduled_pick_up: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices("scheduledPickUp", "scheduled_pick_up"),
            serialization_alias="scheduledPickUp",
            description="Date on which the items are scheduled to be picked from vendor warehouse by Buyer used for WePay/Collect vendors.",
        ),
    ]

    carrier_assignment_date: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices(
                "carrierAssignmentDate", "carrier_assignment_date"
            ),
            serialization_alias="carrierAssignmentDate",
            description="Date on which the carrier is being scheduled to pickup items from vendor warehouse by Byer used for WePay/Collect vendors.",
        ),
    ]


"""
ContainerSequenceNumbers

Container sequence numbers that are involved in this shipment.
"""


class ContainerSequenceNumbers(SpApiBaseModel):
    """Container sequence numbers that are involved in this shipment."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    container_sequence_number: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "containerSequenceNumber", "container_sequence_number"
            ),
            serialization_alias="containerSequenceNumber",
            description="A list of containers shipped",
        ),
    ]


"""
InnerContainersDetails

Details of the innerContainersDetails.
"""


class InnerContainersDetails(SpApiBaseModel):
    """Details of the innerContainersDetails."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    container_count: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices("containerCount", "container_count"),
            serialization_alias="containerCount",
            description="Total containers as part of the shipment",
        ),
    ]

    container_sequence_numbers: Annotated[
        Optional[List["ContainerSequenceNumbers"]],
        Field(
            None,
            validation_alias=AliasChoices(
                "containerSequenceNumbers", "container_sequence_numbers"
            ),
            serialization_alias="containerSequenceNumbers",
            description="Container sequence numbers that are involved in this shipment.",
        ),
    ]


"""
PackageItemDetails

Item details for be provided for every item in shipment at either the item or carton or pallet level, whichever is appropriate.
"""


class PackageItemDetails(SpApiBaseModel):
    """Item details for be provided for every item in shipment at either the item or carton or pallet level, whichever is appropriate."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    purchase_order_number: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "purchaseOrderNumber", "purchase_order_number"
            ),
            serialization_alias="purchaseOrderNumber",
            description="The purchase order number for the shipment being confirmed. If the items in this shipment belong to multiple purchase order numbers that are in particular carton or pallet within the shipment, then provide the purchaseOrderNumber at the appropriate carton or pallet level. Formatting Notes: 8-character alpha-numeric code.",
        ),
    ]

    lot_number: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("lotNumber", "lot_number"),
            serialization_alias="lotNumber",
            description="The batch or lot number associates an item with information the manufacturer considers relevant for traceability of the trade item to which the Element String is applied. The data may refer to the trade item itself or to items contained. This field is mandatory for all perishable items.",
        ),
    ]

    expiry: Annotated[
        Optional["Expiry"],
        Field(
            None,
            description="Either expiryDate or mfgDate and expiryAfterDuration are mandatory for perishable items.",
        ),
    ]


"""
PackedItems

Details of the item being shipped.
"""


class PackedItems(SpApiBaseModel):
    """Details of the item being shipped."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    item_sequence_number: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices("itemSequenceNumber", "item_sequence_number"),
            serialization_alias="itemSequenceNumber",
            description="Item sequence number for the item. The first item will be 001, the second 002, and so on. This number is used as a reference to refer to this item from the carton or pallet level.",
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
            description="Buyer Standard Identification Number (ASIN) of an item.",
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
            description="The vendor selected product identification of the item. Should be the same as was sent in the purchase order.",
        ),
    ]

    packed_quantity: Annotated[
        Optional["ItemQuantity"],
        Field(
            None,
            validation_alias=AliasChoices("packedQuantity", "packed_quantity"),
            serialization_alias="packedQuantity",
            description="Total item quantity shipped in this shipment.",
        ),
    ]

    item_details: Annotated[
        Optional["PackageItemDetails"],
        Field(
            None,
            validation_alias=AliasChoices("itemDetails", "item_details"),
            serialization_alias="itemDetails",
        ),
    ]


# Enum definitions
class ContainersContainerTypeEnum(str, Enum):
    """Enum for containerType"""

    CARTON = "carton"  # A carton is a box or container usually made of liquid packaging board, paperboard and sometimes of corrugated fiberboard
    PALLET = "pallet"  # A flat transport structure which supports goods in a stable fashion while being lifted by a forklift.


"""
Containers

A list of the items in this transportation and their associated inner container details. If any of the item detail fields are common at a carton or a pallet level, provide them at the corresponding carton or pallet level.
"""


class Containers(SpApiBaseModel):
    """A list of the items in this transportation and their associated inner container details. If any of the item detail fields are common at a carton or a pallet level, provide them at the corresponding carton or pallet level."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    container_type: Annotated[
        ContainersContainerTypeEnum,
        Field(
            ...,
            validation_alias=AliasChoices("containerType", "container_type"),
            serialization_alias="containerType",
            description="The type of container.",
        ),
    ]

    container_sequence_number: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "containerSequenceNumber", "container_sequence_number"
            ),
            serialization_alias="containerSequenceNumber",
            description="An integer that must be submitted for multi-box shipments only, where one item may come in separate packages.",
        ),
    ]

    container_identifiers: Annotated[
        List["ContainerIdentification"],
        Field(
            ...,
            validation_alias=AliasChoices(
                "containerIdentifiers", "container_identifiers"
            ),
            serialization_alias="containerIdentifiers",
            description="A list of carton identifiers.",
        ),
    ]

    tracking_number: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("trackingNumber", "tracking_number"),
            serialization_alias="trackingNumber",
            description="The tracking number used for identifying the shipment.",
        ),
    ]

    dimensions: Annotated[
        Optional["Dimensions"],
        Field(
            None,
        ),
    ]

    weight: Annotated[
        Optional["Weight"],
        Field(
            None,
        ),
    ]

    tier: Annotated[
        Optional[int], Field(None, description="Number of layers per pallet.")
    ]

    block: Annotated[
        Optional[int],
        Field(None, description="Number of cartons per layer on the pallet."),
    ]

    inner_containers_details: Annotated[
        Optional["InnerContainersDetails"],
        Field(
            None,
            validation_alias=AliasChoices(
                "innerContainersDetails", "inner_containers_details"
            ),
            serialization_alias="innerContainersDetails",
        ),
    ]

    packed_items: Annotated[
        Optional[List["PackedItems"]],
        Field(
            None,
            validation_alias=AliasChoices("packedItems", "packed_items"),
            serialization_alias="packedItems",
            description="A list of packed items.",
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


ErrorList = List["Error"]
"""A list of error responses returned when a request is unsuccessful."""


# Enum definitions
class GetShipmentDetailsRequestSortOrderEnum(str, Enum):
    """Enum for sortOrder"""

    ASC = "ASC"  # Sort in ascending order by shipment creation date.
    DESC = "DESC"  # Sort in descending order by shipment creation date.


"""
GetShipmentDetailsRequest

Request parameters for GetShipmentDetails
"""


class GetShipmentDetailsRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for GetShipmentDetails
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    limit: Annotated[
        Optional[int],
        QueryParam(),
        Field(
            None,
            description="[QUERY] The limit to the number of records returned. Default value is 50 records.",
        ),
    ]

    sort_order: Annotated[
        Optional[GetShipmentDetailsRequestSortOrderEnum],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("sortOrder", "sort_order"),
            serialization_alias="sortOrder",
            description="[QUERY] Sort in ascending or descending order by purchase order creation date.",
        ),
    ]

    next_token: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("nextToken", "next_token"),
            serialization_alias="nextToken",
            description="[QUERY] Used for pagination when there are more shipments than the specified result size limit.",
        ),
    ]

    created_after: Annotated[
        Optional[datetime],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("createdAfter", "created_after"),
            serialization_alias="createdAfter",
            description="[QUERY] Get Shipment Details that became available after this timestamp will be included in the result. Must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format.",
        ),
    ]

    created_before: Annotated[
        Optional[datetime],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("createdBefore", "created_before"),
            serialization_alias="createdBefore",
            description="[QUERY] Get Shipment Details that became available before this timestamp will be included in the result. Must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format.",
        ),
    ]

    shipment_confirmed_before: Annotated[
        Optional[datetime],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices(
                "shipmentConfirmedBefore", "shipment_confirmed_before"
            ),
            serialization_alias="shipmentConfirmedBefore",
            description="[QUERY] Get Shipment Details by passing Shipment confirmed create Date Before. Must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format.",
        ),
    ]

    shipment_confirmed_after: Annotated[
        Optional[datetime],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices(
                "shipmentConfirmedAfter", "shipment_confirmed_after"
            ),
            serialization_alias="shipmentConfirmedAfter",
            description="[QUERY] Get Shipment Details by passing Shipment confirmed create Date After. Must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format.",
        ),
    ]

    package_label_created_before: Annotated[
        Optional[datetime],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices(
                "packageLabelCreatedBefore", "package_label_created_before"
            ),
            serialization_alias="packageLabelCreatedBefore",
            description="[QUERY] Get Shipment Details by passing Package label create Date by buyer. Must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format.",
        ),
    ]

    package_label_created_after: Annotated[
        Optional[datetime],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices(
                "packageLabelCreatedAfter", "package_label_created_after"
            ),
            serialization_alias="packageLabelCreatedAfter",
            description="[QUERY] Get Shipment Details by passing Package label create Date After by buyer. Must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format.",
        ),
    ]

    shipped_before: Annotated[
        Optional[datetime],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("shippedBefore", "shipped_before"),
            serialization_alias="shippedBefore",
            description="[QUERY] Get Shipment Details by passing Shipped Date Before. Must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format.",
        ),
    ]

    shipped_after: Annotated[
        Optional[datetime],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("shippedAfter", "shipped_after"),
            serialization_alias="shippedAfter",
            description="[QUERY] Get Shipment Details by passing Shipped Date After. Must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format.",
        ),
    ]

    estimated_delivery_before: Annotated[
        Optional[datetime],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices(
                "estimatedDeliveryBefore", "estimated_delivery_before"
            ),
            serialization_alias="estimatedDeliveryBefore",
            description="[QUERY] Get Shipment Details by passing Estimated Delivery Date Before. Must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format.",
        ),
    ]

    estimated_delivery_after: Annotated[
        Optional[datetime],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices(
                "estimatedDeliveryAfter", "estimated_delivery_after"
            ),
            serialization_alias="estimatedDeliveryAfter",
            description="[QUERY] Get Shipment Details by passing Estimated Delivery Date Before. Must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format.",
        ),
    ]

    shipment_delivery_before: Annotated[
        Optional[datetime],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices(
                "shipmentDeliveryBefore", "shipment_delivery_before"
            ),
            serialization_alias="shipmentDeliveryBefore",
            description="[QUERY] Get Shipment Details by passing Shipment Delivery Date Before. Must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format.",
        ),
    ]

    shipment_delivery_after: Annotated[
        Optional[datetime],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices(
                "shipmentDeliveryAfter", "shipment_delivery_after"
            ),
            serialization_alias="shipmentDeliveryAfter",
            description="[QUERY] Get Shipment Details by passing Shipment Delivery Date After. Must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format.",
        ),
    ]

    requested_pick_up_before: Annotated[
        Optional[datetime],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices(
                "requestedPickUpBefore", "requested_pick_up_before"
            ),
            serialization_alias="requestedPickUpBefore",
            description="[QUERY] Get Shipment Details by passing Before Requested pickup date. Must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format.",
        ),
    ]

    requested_pick_up_after: Annotated[
        Optional[datetime],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices(
                "requestedPickUpAfter", "requested_pick_up_after"
            ),
            serialization_alias="requestedPickUpAfter",
            description="[QUERY] Get Shipment Details by passing After Requested pickup date. Must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format.",
        ),
    ]

    scheduled_pick_up_before: Annotated[
        Optional[datetime],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices(
                "scheduledPickUpBefore", "scheduled_pick_up_before"
            ),
            serialization_alias="scheduledPickUpBefore",
            description="[QUERY] Get Shipment Details by passing Before scheduled pickup date. Must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format.",
        ),
    ]

    scheduled_pick_up_after: Annotated[
        Optional[datetime],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices(
                "scheduledPickUpAfter", "scheduled_pick_up_after"
            ),
            serialization_alias="scheduledPickUpAfter",
            description="[QUERY] Get Shipment Details by passing After Scheduled pickup date. Must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format.",
        ),
    ]

    current_shipment_status: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices(
                "currentShipmentStatus", "current_shipment_status"
            ),
            serialization_alias="currentShipmentStatus",
            description="[QUERY] Get Shipment Details by passing Current shipment status.",
        ),
    ]

    vendor_shipment_identifier: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices(
                "vendorShipmentIdentifier", "vendor_shipment_identifier"
            ),
            serialization_alias="vendorShipmentIdentifier",
            description="[QUERY] Get Shipment Details by passing Vendor Shipment ID",
        ),
    ]

    buyer_reference_number: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices(
                "buyerReferenceNumber", "buyer_reference_number"
            ),
            serialization_alias="buyerReferenceNumber",
            description="[QUERY] Get Shipment Details by passing buyer Reference ID",
        ),
    ]

    buyer_warehouse_code: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("buyerWarehouseCode", "buyer_warehouse_code"),
            serialization_alias="buyerWarehouseCode",
            description="[QUERY] Get Shipping Details based on buyer warehouse code. This value should be same as 'shipToParty.partyId' in the Shipment.",
        ),
    ]

    seller_warehouse_code: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices(
                "sellerWarehouseCode", "seller_warehouse_code"
            ),
            serialization_alias="sellerWarehouseCode",
            description="[QUERY] Get Shipping Details based on vendor warehouse code. This value should be same as 'sellingParty.partyId' in the Shipment.",
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
            description="A generated string used to pass information to your next request. If NextToken is returned, pass the value of NextToken to the next request. If NextToken is not returned, there are no more shipment items to return.",
        ),
    ]


"""
Location

Location identifier.
"""


class Location(SpApiBaseModel):
    """Location identifier."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    type: Annotated[
        Optional[str], Field(None, description="Type of location identification.")
    ]

    location_code: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("locationCode", "location_code"),
            serialization_alias="locationCode",
            description="Location code.",
        ),
    ]

    country_code: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("countryCode", "country_code"),
            serialization_alias="countryCode",
            description="The two digit country code. In ISO 3166-1 alpha-2 format.",
        ),
    ]


# Enum definitions
class StopFunctionCodeEnum(str, Enum):
    """Enum for functionCode"""

    PORT_OF_DISCHARGE = "PortOfDischarge"  # Port of Discharge is a place where a vessel discharges or unloads some or all of its shipments.
    FREIGHT_PAYABLE_AT = (
        "FreightPayableAt"  # Place where the payment for the freight is made.
    )
    PORT_OF_LOADING = "PortOfLoading"  # The port where goods are put on a ship.


"""
Stop

Contractual or operational port or point relevant to the movement of the cargo.
"""


class Stop(SpApiBaseModel):
    """Contractual or operational port or point relevant to the movement of the cargo."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    function_code: Annotated[
        StopFunctionCodeEnum,
        Field(
            ...,
            validation_alias=AliasChoices("functionCode", "function_code"),
            serialization_alias="functionCode",
            description="Provide the function code.",
        ),
    ]

    location_identification: Annotated[
        Optional["Location"],
        Field(
            None,
            validation_alias=AliasChoices(
                "locationIdentification", "location_identification"
            ),
            serialization_alias="locationIdentification",
        ),
    ]

    arrival_time: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices("arrivalTime", "arrival_time"),
            serialization_alias="arrivalTime",
            description="Date and time of the arrival of the cargo.",
        ),
    ]

    departure_time: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices("departureTime", "departure_time"),
            serialization_alias="departureTime",
            description="Date and time of the departure of the cargo.",
        ),
    ]


"""
Route

This is used only for direct import shipment confirmations.
"""


class Route(SpApiBaseModel):
    """This is used only for direct import shipment confirmations."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    stops: Annotated[
        List["Stop"],
        Field(
            ...,
            description="The port or location involved in transporting the cargo, as specified in transportation contracts or operational plans.",
        ),
    ]


# Enum definitions
class ImportDetailsMethodOfPaymentEnum(str, Enum):
    """Enum for methodOfPayment"""

    PAID_BY_BUYER = "PaidByBuyer"  # Buyer pays for shipping.
    COLLECT_ON_DELIVERY = "CollectOnDelivery"  # Buyer pays for shipping on delivery.
    DEFINED_BY_BUYER_AND_SELLER = "DefinedByBuyerAndSeller"  # Shipping costs paid as agreed upon between buyer and seller.
    FOB_PORT_OF_CALL = (
        "FOBPortOfCall"  # Seller pays for transportation incl. loading, shipping.
    )
    PREPAID_BY_SELLER = "PrepaidBySeller"  # Seller prepays for shipping.
    PAID_BY_SELLER = "PaidBySeller"  # Seller pays for shipping.


class ImportDetailsHandlingInstructionsEnum(str, Enum):
    """Enum for handlingInstructions"""

    OVERSIZED = "Oversized"  # A package weighing 150 pounds or less and measuring greater than 130 inches in length and girth is classified as an oversized package.
    FRAGILE = "Fragile"  # A package containing easily breakable items.
    FOOD = "Food"  # A package containing edible items.
    HANDLE_WITH_CARE = (
        "HandleWithCare"  # A package containing fragile or dangerous items.
    )


"""
ImportDetails

Provide these fields only if this shipment is a direct import.
"""


class ImportDetails(SpApiBaseModel):
    """Provide these fields only if this shipment is a direct import."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    method_of_payment: Annotated[
        Optional[ImportDetailsMethodOfPaymentEnum],
        Field(
            None,
            validation_alias=AliasChoices("methodOfPayment", "method_of_payment"),
            serialization_alias="methodOfPayment",
            description="This is used for import purchase orders only. If the recipient requests, this field will contain the shipment method of payment.",
        ),
    ]

    seal_number: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("sealNumber", "seal_number"),
            serialization_alias="sealNumber",
            description="The container's seal number.",
        ),
    ]

    route: Annotated[
        Optional["Route"],
        Field(None, description="The route and stop details for this shipment."),
    ]

    import_containers: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("importContainers", "import_containers"),
            serialization_alias="importContainers",
            description="Types and numbers of container(s) for import purchase orders. Can be a comma-separated list if shipment has multiple containers.",
        ),
    ]

    billable_weight: Annotated[
        Optional["Weight"],
        Field(
            None,
            validation_alias=AliasChoices("billableWeight", "billable_weight"),
            serialization_alias="billableWeight",
            description="Billable weight of the direct imports shipment.",
        ),
    ]

    estimated_ship_by_date: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices(
                "estimatedShipByDate", "estimated_ship_by_date"
            ),
            serialization_alias="estimatedShipByDate",
            description="Date on which the shipment is expected to be shipped. This value should not be in the past and not more than 60 days out in the future.",
        ),
    ]

    handling_instructions: Annotated[
        Optional[ImportDetailsHandlingInstructionsEnum],
        Field(
            None,
            validation_alias=AliasChoices(
                "handlingInstructions", "handling_instructions"
            ),
            serialization_alias="handlingInstructions",
            description="Identification of the instructions on how specified item/carton/pallet should be handled.",
        ),
    ]


# Enum definitions
class TaxRegistrationDetailsTaxRegistrationTypeEnum(str, Enum):
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
        TaxRegistrationDetailsTaxRegistrationTypeEnum,
        Field(
            ...,
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
            description="Tax registration number for the entity. For example, VAT ID.",
        ),
    ]


"""
PartyIdentification

Name/Address and tax details of the party.
"""


class PartyIdentification(SpApiBaseModel):
    """Name/Address and tax details of the party."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    address: Annotated[
        Optional["Address"],
        Field(None, description="Identification of the party by address."),
    ]

    party_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("partyId", "party_id"),
            serialization_alias="partyId",
            description="Assigned identification for the party.",
        ),
    ]

    tax_registration_details: Annotated[
        Optional[List["TaxRegistrationDetails"]],
        Field(
            None,
            validation_alias=AliasChoices(
                "taxRegistrationDetails", "tax_registration_details"
            ),
            serialization_alias="taxRegistrationDetails",
            description="Tax registration details of the entity.",
        ),
    ]


"""
PurchaseOrderItems

Details of the item being shipped.
"""


class PurchaseOrderItems(SpApiBaseModel):
    """Details of the item being shipped."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    item_sequence_number: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("itemSequenceNumber", "item_sequence_number"),
            serialization_alias="itemSequenceNumber",
            description="Item sequence number for the item. The first item will be 001, the second 002, and so on. This number is used as a reference to refer to this item from the carton or pallet level.",
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
            description="Amazon Standard Identification Number (ASIN) for a SKU",
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
            description="The vendor selected product identification of the item. Should be the same as was sent in the purchase order.",
        ),
    ]

    shipped_quantity: Annotated[
        "ItemQuantity",
        Field(
            ...,
            validation_alias=AliasChoices("shippedQuantity", "shipped_quantity"),
            serialization_alias="shippedQuantity",
            description="Total item quantity shipped in this shipment.",
        ),
    ]

    maximum_retail_price: Annotated[
        Optional["Money"],
        Field(
            None,
            validation_alias=AliasChoices("maximumRetailPrice", "maximum_retail_price"),
            serialization_alias="maximumRetailPrice",
        ),
    ]


"""
PurchaseOrders

Transport RequestBody pickup date
"""


class PurchaseOrders(SpApiBaseModel):
    """Transport RequestBody pickup date"""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    purchase_order_number: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "purchaseOrderNumber", "purchase_order_number"
            ),
            serialization_alias="purchaseOrderNumber",
            description="Purchase order numbers involved in this shipment, list all the PO that are involved as part of this shipment.",
        ),
    ]

    purchase_order_date: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices("purchaseOrderDate", "purchase_order_date"),
            serialization_alias="purchaseOrderDate",
            description="Purchase order numbers involved in this shipment, list all the PO that are involved as part of this shipment.",
        ),
    ]

    ship_window: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("shipWindow", "ship_window"),
            serialization_alias="shipWindow",
            description="Date range in which shipment is expected for these purchase orders.",
        ),
    ]

    items: Annotated[
        Optional[List["PurchaseOrderItems"]],
        Field(
            None,
            description="A list of the items that are associated to the PO in this transport and their associated details.",
        ),
    ]


# Enum definitions
class ShipmentStatusDetailsShipmentStatusEnum(str, Enum):
    """Enum for shipmentStatus"""

    CREATED = "Created"  # Shipment request was received by buyer.
    TRANSPORTATION_REQUESTED = "TransportationRequested"
    CARRIER_ASSIGNED = "CarrierAssigned"
    SHIPPED = "Shipped"  # Shipment done to buyer warehouse.


"""
ShipmentStatusDetails

Shipment Status details.
"""


class ShipmentStatusDetails(SpApiBaseModel):
    """Shipment Status details."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    shipment_status: Annotated[
        Optional[ShipmentStatusDetailsShipmentStatusEnum],
        Field(
            None,
            validation_alias=AliasChoices("shipmentStatus", "shipment_status"),
            serialization_alias="shipmentStatus",
            description="Current status of the shipment on whether it is picked up or scheduled.",
        ),
    ]

    shipment_status_date: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices("shipmentStatusDate", "shipment_status_date"),
            serialization_alias="shipmentStatusDate",
            description="Date and time on last status update received for the shipment",
        ),
    ]


# Enum definitions
class VolumeUnitOfMeasureEnum(str, Enum):
    """Enum for unitOfMeasure"""

    CU_FT = "CuFt"  # Cubic feet.
    CU_IN = "CuIn"  # Cubic inches.
    CU_M = "CuM"  # Cubic meter.
    CU_Y = "CuY"  # Cubic yard.


"""
Volume

The volume of the shipment.
"""


class Volume(SpApiBaseModel):
    """The volume of the shipment."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    unit_of_measure: Annotated[
        VolumeUnitOfMeasureEnum,
        Field(
            ...,
            validation_alias=AliasChoices("unitOfMeasure", "unit_of_measure"),
            serialization_alias="unitOfMeasure",
            description="The unit of measurement.",
        ),
    ]

    value: Annotated["Decimal", Field(..., description="The measurement value.")]


"""
TransportShipmentMeasurements

Shipment measurement details.
"""


class TransportShipmentMeasurements(SpApiBaseModel):
    """Shipment measurement details."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    total_carton_count: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices("totalCartonCount", "total_carton_count"),
            serialization_alias="totalCartonCount",
            description="Total number of cartons present in the shipment. Provide the cartonCount only for non-palletized shipments.",
        ),
    ]

    total_pallet_stackable: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices(
                "totalPalletStackable", "total_pallet_stackable"
            ),
            serialization_alias="totalPalletStackable",
            description="Total number of Stackable Pallets present in the shipment.",
        ),
    ]

    total_pallet_non_stackable: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices(
                "totalPalletNonStackable", "total_pallet_non_stackable"
            ),
            serialization_alias="totalPalletNonStackable",
            description="Total number of Non Stackable Pallets present in the shipment.",
        ),
    ]

    shipment_weight: Annotated[
        Optional["Weight"],
        Field(
            None,
            validation_alias=AliasChoices("shipmentWeight", "shipment_weight"),
            serialization_alias="shipmentWeight",
            description="Total Weight of the shipment.",
        ),
    ]

    shipment_volume: Annotated[
        Optional["Volume"],
        Field(
            None,
            validation_alias=AliasChoices("shipmentVolume", "shipment_volume"),
            serialization_alias="shipmentVolume",
            description="Total Volume of the shipment.",
        ),
    ]


# Enum definitions
class TransportationDetailsShipModeEnum(str, Enum):
    """Enum for shipMode"""

    TRUCK_LOAD = "TruckLoad"  # Truckload shipping is the movement of large amounts of homogeneous cargo, generally the amount necessary to fill an entire semi-trailer or intermodal container.
    LESS_THAN_TRUCK_LOAD = (
        "LessThanTruckLoad"  # Shipping does not fill the entire truck.
    )
    SMALL_PARCEL = "SmallParcel"  # Small parcel shipments are under 70 pounds per parcel and shipped with your own packaging or carrier supplied boxes.


class TransportationDetailsTransportationModeEnum(str, Enum):
    """Enum for transportationMode"""

    ROAD = "Road"  # The mode of transportation is by Road (on a truck).
    AIR = "Air"  # The mode of transportation is by Air (on a plane).
    OCEAN = "Ocean"  # The mode of transportation is by Ocean (on a ship).


"""
TransportationDetails

Transportation details for this shipment.
"""


class TransportationDetails(SpApiBaseModel):
    """Transportation details for this shipment."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    ship_mode: Annotated[
        Optional[TransportationDetailsShipModeEnum],
        Field(
            None,
            validation_alias=AliasChoices("shipMode", "ship_mode"),
            serialization_alias="shipMode",
            description="The type of shipment.",
        ),
    ]

    transportation_mode: Annotated[
        Optional[TransportationDetailsTransportationModeEnum],
        Field(
            None,
            validation_alias=AliasChoices("transportationMode", "transportation_mode"),
            serialization_alias="transportationMode",
            description="The mode of transportation for this shipment.",
        ),
    ]

    shipped_date: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices("shippedDate", "shipped_date"),
            serialization_alias="shippedDate",
            description="Date when shipment is performed by the Vendor to Buyer",
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
            description="Estimated Date on which shipment will be delivered from Vendor to Buyer",
        ),
    ]

    shipment_delivery_date: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices(
                "shipmentDeliveryDate", "shipment_delivery_date"
            ),
            serialization_alias="shipmentDeliveryDate",
            description="Date on which shipment will be delivered from Vendor to Buyer",
        ),
    ]

    carrier_details: Annotated[
        Optional["CarrierDetails"],
        Field(
            None,
            validation_alias=AliasChoices("carrierDetails", "carrier_details"),
            serialization_alias="carrierDetails",
            description="Indicates the carrier details and their contact informations",
        ),
    ]

    bill_of_lading_number: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "billOfLadingNumber", "bill_of_lading_number"
            ),
            serialization_alias="billOfLadingNumber",
            description="The Bill of Lading (BOL) number is a unique number assigned to each shipment of goods by the vendor or shipper during the creation of the Bill of Lading. This number must be unique for every shipment and cannot be a date/time or single character. The BOL numer is mandatory in Shipment Confirmation message for FTL and LTL shipments, and must match the paper BOL provided with the shipment. Instead of BOL, an alternative reference number (like Delivery Note Number) for the shipment can also be sent in this field.",
        ),
    ]


# Enum definitions
class ShipmentTransactionTypeEnum(str, Enum):
    """Enum for transactionType"""

    NEW = "New"  # Initial shipment Request.
    CANCEL = "Cancel"  # Cancel existing shipment RequestBody message. should be used only to cancel Shipment request


class ShipmentCurrentShipmentStatusEnum(str, Enum):
    """Enum for currentShipmentStatus"""

    CREATED = "Created"  # Shipment request was received by buyer.
    TRANSPORTATION_REQUESTED = "TransportationRequested"
    CARRIER_ASSIGNED = "CarrierAssigned"
    SHIPPED = "Shipped"  # Shipment sent to buyer warehouse.


class ShipmentShipmentFreightTermEnum(str, Enum):
    """Enum for shipmentFreightTerm"""

    COLLECT = "Collect"  # Buyer Pays / We Pay for the the transportation. Buyer pays for the shipment and provides Vendor and picks up shipment from vendor warehouse / location
    PREPAID = "Prepaid"  # Vendor pays / They Pay for the transportation. Vendor pays for the shipment and ships the goods to buyer warehouse / location


"""
Shipment

A list of one or more shipments with respective details.
"""


class Shipment(SpApiBaseModel):
    """A list of one or more shipments with respective details."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    vendor_shipment_identifier: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices(
                "vendorShipmentIdentifier", "vendor_shipment_identifier"
            ),
            serialization_alias="vendorShipmentIdentifier",
            description="Unique Transportation ID created by Vendor (Should not be used over the last 365 days).",
        ),
    ]

    transaction_type: Annotated[
        ShipmentTransactionTypeEnum,
        Field(
            ...,
            validation_alias=AliasChoices("transactionType", "transaction_type"),
            serialization_alias="transactionType",
            description="Indicates the type of transportation request (for example, `New` or `Cancel`). Each `transactionType` has a unique set of operations and there are corresponding details to be populated for each operation.",
        ),
    ]

    buyer_reference_number: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "buyerReferenceNumber", "buyer_reference_number"
            ),
            serialization_alias="buyerReferenceNumber",
            description="The buyer Reference Number is a unique identifier generated by buyer for all Collect/WePay shipments when you submit a transportation request. This field is mandatory for Collect/WePay shipments.",
        ),
    ]

    transaction_date: Annotated[
        datetime,
        Field(
            ...,
            validation_alias=AliasChoices("transactionDate", "transaction_date"),
            serialization_alias="transactionDate",
            description="Date on which the transportation request was submitted.",
        ),
    ]

    current_shipment_status: Annotated[
        Optional[ShipmentCurrentShipmentStatusEnum],
        Field(
            None,
            validation_alias=AliasChoices(
                "currentShipmentStatus", "current_shipment_status"
            ),
            serialization_alias="currentShipmentStatus",
            description="Indicates the current shipment status.",
        ),
    ]

    currentshipment_status_date: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices(
                "currentshipmentStatusDate", "currentshipment_status_date"
            ),
            serialization_alias="currentshipmentStatusDate",
            description="Date and time when the last status was updated.",
        ),
    ]

    shipment_status_details: Annotated[
        Optional[List["ShipmentStatusDetails"]],
        Field(
            None,
            validation_alias=AliasChoices(
                "shipmentStatusDetails", "shipment_status_details"
            ),
            serialization_alias="shipmentStatusDetails",
            description="Indicates the list of current shipment status details and when the last update was received from carrier this is available on shipment Details response.",
        ),
    ]

    shipment_create_date: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices("shipmentCreateDate", "shipment_create_date"),
            serialization_alias="shipmentCreateDate",
            description="The date and time of the shipment request created by vendor.",
        ),
    ]

    shipment_confirm_date: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices(
                "shipmentConfirmDate", "shipment_confirm_date"
            ),
            serialization_alias="shipmentConfirmDate",
            description="The date and time of the departure of the shipment from the vendor's location. Vendors are requested to send ASNs within 30 minutes of departure from their warehouse/distribution center or at least 6 hours prior to the appointment time at the Buyer destination warehouse, whichever is sooner. Shipped date mentioned in the shipment confirmation should not be in the future.",
        ),
    ]

    package_label_create_date: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices(
                "packageLabelCreateDate", "package_label_create_date"
            ),
            serialization_alias="packageLabelCreateDate",
            description="The date and time of the package label created for the shipment by buyer.",
        ),
    ]

    shipment_freight_term: Annotated[
        Optional[ShipmentShipmentFreightTermEnum],
        Field(
            None,
            validation_alias=AliasChoices(
                "shipmentFreightTerm", "shipment_freight_term"
            ),
            serialization_alias="shipmentFreightTerm",
            description="Specifies if payment is Collect (WePay) or Prepaid (TheyPay). Required.",
        ),
    ]

    selling_party: Annotated[
        "PartyIdentification",
        Field(
            ...,
            validation_alias=AliasChoices("sellingParty", "selling_party"),
            serialization_alias="sellingParty",
            description="Name/Address and tax details of the selling party.",
        ),
    ]

    ship_from_party: Annotated[
        "PartyIdentification",
        Field(
            ...,
            validation_alias=AliasChoices("shipFromParty", "ship_from_party"),
            serialization_alias="shipFromParty",
            description="Name/Address and tax details of the ship from party.",
        ),
    ]

    ship_to_party: Annotated[
        "PartyIdentification",
        Field(
            ...,
            validation_alias=AliasChoices("shipToParty", "ship_to_party"),
            serialization_alias="shipToParty",
            description="Name/Address of the destination warehouse where the shipment is being shipped to.",
        ),
    ]

    shipment_measurements: Annotated[
        Optional["TransportShipmentMeasurements"],
        Field(
            None,
            validation_alias=AliasChoices(
                "shipmentMeasurements", "shipment_measurements"
            ),
            serialization_alias="shipmentMeasurements",
            description="Indicates the shipment measurement details on how many cartons and pallets and the total transportation weight and volume as part of this request. This is a mandatory detail which will help determining the transportation cost, truck allocations and route determination efficiently.",
        ),
    ]

    collect_freight_pickup_details: Annotated[
        Optional["CollectFreightPickupDetails"],
        Field(
            None,
            validation_alias=AliasChoices(
                "collectFreightPickupDetails", "collect_freight_pickup_details"
            ),
            serialization_alias="collectFreightPickupDetails",
            description="Indicates the earliest pickup date for the transportation from vendor warehouse. This information is mandatory to be filled for requesting transportation from Buyer (WePay/Collect).",
        ),
    ]

    purchase_orders: Annotated[
        Optional[List["PurchaseOrders"]],
        Field(
            None,
            validation_alias=AliasChoices("purchaseOrders", "purchase_orders"),
            serialization_alias="purchaseOrders",
            description="Indicates the purchase orders involved for the transportation request. This group is an array create 1 for each PO and list their corresponding items. This information is used for deciding the route,truck allocation and storage efficiently. This is a mandatory information for Buyer performing transportation from vendor warehouse (WePay/Collect)",
        ),
    ]

    import_details: Annotated[
        Optional["ImportDetails"],
        Field(
            None,
            validation_alias=AliasChoices("importDetails", "import_details"),
            serialization_alias="importDetails",
            description="Provide these fields only if this shipment is a direct import.",
        ),
    ]

    containers: Annotated[
        Optional[List["Containers"]],
        Field(
            None,
            description="A list of the items in this transportation and their associated inner container details. If any of the item detail fields are common at a carton or a pallet level, provide them at the corresponding carton or pallet level.",
        ),
    ]

    transportation_details: Annotated[
        Optional["TransportationDetails"],
        Field(
            None,
            validation_alias=AliasChoices(
                "transportationDetails", "transportation_details"
            ),
            serialization_alias="transportationDetails",
            description="Transportation details this a mandatory information which states delivery date, shipping date and carrier details.",
        ),
    ]


"""
ShipmentDetails

The request schema for the GetShipmentDetails operation.
"""


class ShipmentDetails(SpApiBaseModel):
    """The request schema for the GetShipmentDetails operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    pagination: Annotated[
        Optional["Pagination"],
        Field(
            None,
        ),
    ]

    shipments: Annotated[
        Optional[List["Shipment"]],
        Field(
            None, description="A list of one or more shipments with underlying details."
        ),
    ]


"""
GetShipmentDetailsResponse

The response schema for the GetShipmentDetails operation.
"""


class GetShipmentDetailsResponse(SpApiBaseModel):
    """The response schema for the GetShipmentDetails operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["ShipmentDetails"],
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


# Enum definitions
class LabelDataLabelFormatEnum(str, Enum):
    """Enum for labelFormat"""

    PDF = "PDF"


"""
LabelData

Label details as part of the transport label response
"""


class LabelData(SpApiBaseModel):
    """Label details as part of the transport label response"""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    label_sequence_number: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices(
                "labelSequenceNumber", "label_sequence_number"
            ),
            serialization_alias="labelSequenceNumber",
            description="A sequential number assigned to each label within a shipment.",
        ),
    ]

    label_format: Annotated[
        Optional[LabelDataLabelFormatEnum],
        Field(
            None,
            validation_alias=AliasChoices("labelFormat", "label_format"),
            serialization_alias="labelFormat",
            description="The format of the label.",
        ),
    ]

    carrier_code: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("carrierCode", "carrier_code"),
            serialization_alias="carrierCode",
            description="Unique identification of the carrier.",
        ),
    ]

    tracking_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("trackingId", "tracking_id"),
            serialization_alias="trackingId",
            description="Tracking Id for the transportation.",
        ),
    ]

    label: Annotated[
        Optional[str],
        Field(
            None,
            description="The base-64 encoded string that represents the shipment label.",
        ),
    ]


"""
VendorDetails

Vendor Details as part of Label response.
"""


class VendorDetails(SpApiBaseModel):
    """Vendor Details as part of Label response."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    selling_party: Annotated[
        Optional["PartyIdentification"],
        Field(
            None,
            validation_alias=AliasChoices("sellingParty", "selling_party"),
            serialization_alias="sellingParty",
            description="Name/Address and tax details of the selling party.",
        ),
    ]

    vendor_shipment_identifier: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "vendorShipmentIdentifier", "vendor_shipment_identifier"
            ),
            serialization_alias="vendorShipmentIdentifier",
            description="Unique vendor shipment id which is not used in last 365 days",
        ),
    ]


# Enum definitions
class ShipmentInformationShipModeEnum(str, Enum):
    """Enum for shipMode"""

    SMALL_PARCEL = "SmallParcel"
    LTL = "LTL"


"""
ShipmentInformation

Shipment Information details for Label request.
"""


class ShipmentInformation(SpApiBaseModel):
    """Shipment Information details for Label request."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    vendor_details: Annotated[
        Optional["VendorDetails"],
        Field(
            None,
            validation_alias=AliasChoices("vendorDetails", "vendor_details"),
            serialization_alias="vendorDetails",
            description="Vendor Details requesting for Shipment Label",
        ),
    ]

    buyer_reference_number: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "buyerReferenceNumber", "buyer_reference_number"
            ),
            serialization_alias="buyerReferenceNumber",
            description="The buyer reference number is a unique identifier generated by the buyer for all Collect and WePay shipments.",
        ),
    ]

    ship_to_party: Annotated[
        Optional["PartyIdentification"],
        Field(
            None,
            validation_alias=AliasChoices("shipToParty", "ship_to_party"),
            serialization_alias="shipToParty",
            description="The name and address of the destination warehouse where the shipment is being shipped.",
        ),
    ]

    ship_from_party: Annotated[
        Optional["PartyIdentification"],
        Field(
            None,
            validation_alias=AliasChoices("shipFromParty", "ship_from_party"),
            serialization_alias="shipFromParty",
            description="Name/Address of the destination warehouse where the shipment is being shipped to.",
        ),
    ]

    warehouse_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("warehouseId", "warehouse_id"),
            serialization_alias="warehouseId",
            description="Vendor Warehouse ID from where the shipment is scheduled to be picked up by buyer / Carrier.",
        ),
    ]

    master_tracking_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("masterTrackingId", "master_tracking_id"),
            serialization_alias="masterTrackingId",
            description="Unique Id with which the shipment can be tracked for Small Parcels.",
        ),
    ]

    total_label_count: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices("totalLabelCount", "total_label_count"),
            serialization_alias="totalLabelCount",
            description="Number of Labels that are created as part of this shipment.",
        ),
    ]

    ship_mode: Annotated[
        Optional[ShipmentInformationShipModeEnum],
        Field(
            None,
            validation_alias=AliasChoices("shipMode", "ship_mode"),
            serialization_alias="shipMode",
            description="Type of shipment whether it is Small Parcel",
        ),
    ]


"""
TransportLabel

A list of one or more ShipmentLabels.
"""


class TransportLabel(SpApiBaseModel):
    """A list of one or more ShipmentLabels."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    label_create_date_time: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices(
                "labelCreateDateTime", "label_create_date_time"
            ),
            serialization_alias="labelCreateDateTime",
            description="Date on which label is created.",
        ),
    ]

    shipment_information: Annotated[
        Optional["ShipmentInformation"],
        Field(
            None,
            validation_alias=AliasChoices(
                "shipmentInformation", "shipment_information"
            ),
            serialization_alias="shipmentInformation",
            description="Indicates the shipment Information details like warehouse and business reference details like ARN, Selling Party detail and Vendor Warehouse details",
        ),
    ]

    label_data: Annotated[
        Optional[List["LabelData"]],
        Field(
            None,
            validation_alias=AliasChoices("labelData", "label_data"),
            serialization_alias="labelData",
            description="Indicates the label data,format and type associated .",
        ),
    ]


"""
TransportationLabels

The request schema for the GetShipmentLabels operation.
"""


class TransportationLabels(SpApiBaseModel):
    """The request schema for the GetShipmentLabels operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    pagination: Annotated[
        Optional["Pagination"],
        Field(
            None,
        ),
    ]

    transport_labels: Annotated[
        Optional[List["TransportLabel"]],
        Field(
            None,
            validation_alias=AliasChoices("transportLabels", "transport_labels"),
            serialization_alias="transportLabels",
            description="A list of one or more ShipmentLabels.",
        ),
    ]


"""
GetShipmentLabels

The response schema for the GetShipmentLabels operation.
"""


class GetShipmentLabels(SpApiBaseModel):
    """The response schema for the GetShipmentLabels operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["TransportationLabels"],
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


# Enum definitions
class GetShipmentLabelsRequestSortOrderEnum(str, Enum):
    """Enum for sortOrder"""

    ASC = "ASC"  # Sort the list by shipment label creation date in ascending order.
    DESC = "DESC"  # Sort the list by shipment label creation date in descending order.


"""
GetShipmentLabelsRequest

Request parameters for GetShipmentLabels
"""


class GetShipmentLabelsRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for GetShipmentLabels
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    limit: Annotated[
        Optional[int],
        QueryParam(),
        Field(
            None,
            description="[QUERY] The limit to the number of records returned. Default value is 50 records.",
        ),
    ]

    sort_order: Annotated[
        Optional[GetShipmentLabelsRequestSortOrderEnum],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("sortOrder", "sort_order"),
            serialization_alias="sortOrder",
            description="[QUERY] Sort the list by shipment label creation date in ascending or descending order.",
        ),
    ]

    next_token: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("nextToken", "next_token"),
            serialization_alias="nextToken",
            description="[QUERY] A token that you use to retrieve the next page of results. The response includes `nextToken` when the number of results exceeds the specified `pageSize` value. To get the next page of results, call the operation with this token and include the same arguments as the call that produced the token. To get a complete list, call this operation until `nextToken` is null. Note that this operation can return empty pages.",
        ),
    ]

    label_created_after: Annotated[
        Optional[datetime],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("labelCreatedAfter", "label_created_after"),
            serialization_alias="labelCreatedAfter",
            description="[QUERY] Shipment labels created after this time will be included in the result. This field must be in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) datetime format.",
        ),
    ]

    label_created_before: Annotated[
        Optional[datetime],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("labelCreatedBefore", "label_created_before"),
            serialization_alias="labelCreatedBefore",
            description="[QUERY] Shipment labels created before this time will be included in the result. This field must be in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) datetime format.",
        ),
    ]

    buyer_reference_number: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices(
                "buyerReferenceNumber", "buyer_reference_number"
            ),
            serialization_alias="buyerReferenceNumber",
            description="[QUERY] Get Shipment labels by passing buyer reference number.",
        ),
    ]

    vendor_shipment_identifier: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices(
                "vendorShipmentIdentifier", "vendor_shipment_identifier"
            ),
            serialization_alias="vendorShipmentIdentifier",
            description="[QUERY] Get Shipment labels by passing vendor shipment identifier.",
        ),
    ]

    seller_warehouse_code: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices(
                "sellerWarehouseCode", "seller_warehouse_code"
            ),
            serialization_alias="sellerWarehouseCode",
            description="[QUERY] Get Shipping labels based on vendor warehouse code. This value must be same as the `sellingParty.partyId` in the shipment.",
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
        str,
        Field(
            ...,
            validation_alias=AliasChoices("itemSequenceNumber", "item_sequence_number"),
            serialization_alias="itemSequenceNumber",
            description="Item sequence number for the item. The first item will be 001, the second 002, and so on. This number is used as a reference to refer to this item from the carton or pallet level.",
        ),
    ]

    amazon_product_identifier: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "amazonProductIdentifier", "amazon_product_identifier"
            ),
            serialization_alias="amazonProductIdentifier",
            description="Buyer Standard Identification Number (ASIN) of an item.",
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
            description="The vendor selected product identification of the item. Should be the same as was sent in the purchase order.",
        ),
    ]

    shipped_quantity: Annotated[
        "ItemQuantity",
        Field(
            ...,
            validation_alias=AliasChoices("shippedQuantity", "shipped_quantity"),
            serialization_alias="shippedQuantity",
            description="Total item quantity shipped in this shipment.",
        ),
    ]

    item_details: Annotated[
        Optional["ItemDetails"],
        Field(
            None,
            validation_alias=AliasChoices("itemDetails", "item_details"),
            serialization_alias="itemDetails",
        ),
    ]


# Enum definitions
class PackedQuantityUnitOfMeasureEnum(str, Enum):
    """Enum for unitOfMeasure"""

    CASES = "Cases"  # Packing of individual items into a case.
    EACHES = "Eaches"  # Individual items.


"""
PackedQuantity

Details of item quantity.
"""


class PackedQuantity(SpApiBaseModel):
    """Details of item quantity."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    amount: Annotated[
        int,
        Field(
            ...,
            description="Amount of units shipped for a specific item at a shipment level. If the item is present only in certain cartons or pallets within the shipment, please provide this at the appropriate carton or pallet level.",
        ),
    ]

    unit_of_measure: Annotated[
        PackedQuantityUnitOfMeasureEnum,
        Field(
            ...,
            validation_alias=AliasChoices("unitOfMeasure", "unit_of_measure"),
            serialization_alias="unitOfMeasure",
            description="Unit of measure for the shipped quantity.",
        ),
    ]

    unit_size: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices("unitSize", "unit_size"),
            serialization_alias="unitSize",
            description="The case size, in the event that we ordered using cases. Otherwise, 1.",
        ),
    ]


"""
Pallet

Details of the Pallet/Tare being shipped.
"""


class Pallet(SpApiBaseModel):
    """Details of the Pallet/Tare being shipped."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    pallet_identifiers: Annotated[
        List["ContainerIdentification"],
        Field(
            ...,
            validation_alias=AliasChoices("palletIdentifiers", "pallet_identifiers"),
            serialization_alias="palletIdentifiers",
            description="A list of pallet identifiers.",
        ),
    ]

    tier: Annotated[
        Optional[int],
        Field(
            None,
            description="Number of layers per pallet. Only applicable to container type Pallet.",
        ),
    ]

    block: Annotated[
        Optional[int],
        Field(
            None,
            description="Number of cartons per layer on the pallet. Only applicable to container type Pallet.",
        ),
    ]

    dimensions: Annotated[
        Optional["Dimensions"],
        Field(
            None,
        ),
    ]

    weight: Annotated[
        Optional["Weight"],
        Field(
            None,
        ),
    ]

    carton_reference_details: Annotated[
        Optional["CartonReferenceDetails"],
        Field(
            None,
            validation_alias=AliasChoices(
                "cartonReferenceDetails", "carton_reference_details"
            ),
            serialization_alias="cartonReferenceDetails",
            description="Carton reference details.",
        ),
    ]

    items: Annotated[
        Optional[List["ContainerItem"]],
        Field(None, description="A list of container item details."),
    ]


"""
PurchaseOrderItemDetails

Item details for be provided for every item in shipment at either the item or carton or pallet level, whichever is appropriate.
"""


class PurchaseOrderItemDetails(SpApiBaseModel):
    """Item details for be provided for every item in shipment at either the item or carton or pallet level, whichever is appropriate."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    maximum_retail_price: Annotated[
        Optional["Money"],
        Field(
            None,
            validation_alias=AliasChoices("maximumRetailPrice", "maximum_retail_price"),
            serialization_alias="maximumRetailPrice",
            description="Maximum retail price of the item being shipped.",
        ),
    ]


"""
ShipmentMeasurements

Shipment measurement details.
"""


class ShipmentMeasurements(SpApiBaseModel):
    """Shipment measurement details."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    gross_shipment_weight: Annotated[
        Optional["Weight"],
        Field(
            None,
            validation_alias=AliasChoices(
                "grossShipmentWeight", "gross_shipment_weight"
            ),
            serialization_alias="grossShipmentWeight",
            description="Gross weight of the shipment.",
        ),
    ]

    shipment_volume: Annotated[
        Optional["Volume"],
        Field(
            None,
            validation_alias=AliasChoices("shipmentVolume", "shipment_volume"),
            serialization_alias="shipmentVolume",
            description="Gross Volume of the shipment.",
        ),
    ]

    carton_count: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices("cartonCount", "carton_count"),
            serialization_alias="cartonCount",
            description="Number of cartons present in the shipment. Provide the cartonCount only for non-palletized shipments.",
        ),
    ]

    pallet_count: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices("palletCount", "pallet_count"),
            serialization_alias="palletCount",
            description="Number of pallets present in the shipment. Provide the palletCount only for palletized shipments.",
        ),
    ]


# Enum definitions
class TransportationDetailsForShipmentConfirmationTransportationModeEnum(str, Enum):
    """Enum for transportationMode"""

    ROAD = "Road"  # The mode of transportation is by Road (on a truck).
    AIR = "Air"  # The mode of transportation is by Air (on a plane).
    OCEAN = "Ocean"  # The mode of transportation is by Ocean (on a ship).


"""
TransportationDetailsForShipmentConfirmation

Transportation details for this shipment.
"""


class TransportationDetailsForShipmentConfirmation(SpApiBaseModel):
    """Transportation details for this shipment."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    carrier_scac: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("carrierScac", "carrier_scac"),
            serialization_alias="carrierScac",
            description="Code that identifies the carrier for the shipment. The Standard Carrier Alpha Code (SCAC) is a unique two to four letter code used to identify a carrier. Carrier SCAC codes are assigned and maintained by the NMFTA (National Motor Freight Association). This field is mandatory for US, CA, MX shipment confirmations.",
        ),
    ]

    carrier_shipment_reference_number: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "carrierShipmentReferenceNumber", "carrier_shipment_reference_number"
            ),
            serialization_alias="carrierShipmentReferenceNumber",
            description="The field also known as PRO number is a unique number assigned by the carrier. It is used to identify and track the shipment that goes out for delivery. This field is mandatory for UA, CA, MX shipment confirmations.",
        ),
    ]

    transportation_mode: Annotated[
        Optional[TransportationDetailsForShipmentConfirmationTransportationModeEnum],
        Field(
            None,
            validation_alias=AliasChoices("transportationMode", "transportation_mode"),
            serialization_alias="transportationMode",
            description="The mode of transportation for this shipment.",
        ),
    ]

    bill_of_lading_number: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "billOfLadingNumber", "bill_of_lading_number"
            ),
            serialization_alias="billOfLadingNumber",
            description="The Bill of Lading (BOL) number is a unique number assigned to each shipment of goods by the vendor or shipper during the creation of the Bill of Lading. This number must be unique for every shipment and cannot be a date/time or single character. The BOL numer is mandatory in Shipment Confirmation message for FTL and LTL shipments, and must match the paper BOL provided with the shipment. Instead of BOL, an alternative reference number (like Delivery Note Number) for the shipment can also be sent in this field.",
        ),
    ]


# Enum definitions
class ShipmentConfirmationShipmentConfirmationTypeEnum(str, Enum):
    """Enum for shipmentConfirmationType"""

    ORIGINAL = "Original"  # Initial shipment confirmation message.
    REPLACE = "Replace"  # Replace the original shipment confirmation message.


class ShipmentConfirmationShipmentTypeEnum(str, Enum):
    """Enum for shipmentType"""

    TRUCK_LOAD = "TruckLoad"  # Truckload shipping is the movement of large amounts of homogeneous cargo, generally the amount necessary to fill an entire semi-trailer or intermodal container.
    LESS_THAN_TRUCK_LOAD = (
        "LessThanTruckLoad"  # Shipping does not fill the entire truck.
    )
    SMALL_PARCEL = "SmallParcel"  # Small parcel shipments are under 70 pounds per and shipped in your own packaging or carrier supplied boxes.


class ShipmentConfirmationShipmentStructureEnum(str, Enum):
    """Enum for shipmentStructure"""

    PALLETIZED_ASSORTMENT_CASE = "PalletizedAssortmentCase"  # Shipment -> Order -> Pallet/Tare -> Carton/Package -> Item
    LOOSE_ASSORTMENT_CASE = (
        "LooseAssortmentCase"  # Shipment -> Order -> Carton/Package -> Item
    )
    PALLET_OF_ITEMS = "PalletOfItems"  # Shipment -> Order -> Pallet/Tare -> Item
    PALLETIZED_STANDARD_CASE = "PalletizedStandardCase"  # Shipment -> Order -> Pallet/Tare -> Item -> Carton/Package
    LOOSE_STANDARD_CASE = (
        "LooseStandardCase"  # Shipment -> Order -> Item -> Carton/Package
    )
    MASTER_PALLET = "MasterPallet"  # Shipment -> Pallet/Tare -> Order -> Item
    MASTER_CASE = "MasterCase"  # Shipment -> Carton/Package -> Order -> Item


"""
ShipmentConfirmation

A list of one or more shipment confirmations.
"""


class ShipmentConfirmation(SpApiBaseModel):
    """A list of one or more shipment confirmations."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    shipment_identifier: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("shipmentIdentifier", "shipment_identifier"),
            serialization_alias="shipmentIdentifier",
            description="Unique shipment ID (not used over the last 365 days).",
        ),
    ]

    shipment_confirmation_type: Annotated[
        ShipmentConfirmationShipmentConfirmationTypeEnum,
        Field(
            ...,
            validation_alias=AliasChoices(
                "shipmentConfirmationType", "shipment_confirmation_type"
            ),
            serialization_alias="shipmentConfirmationType",
            description="Indicates if this shipment confirmation is the initial confirmation, or intended to replace an already posted shipment confirmation. If replacing an existing shipment confirmation, be sure to provide the identical shipmentIdentifier and sellingParty information as in the previous confirmation.",
        ),
    ]

    shipment_type: Annotated[
        Optional[ShipmentConfirmationShipmentTypeEnum],
        Field(
            None,
            validation_alias=AliasChoices("shipmentType", "shipment_type"),
            serialization_alias="shipmentType",
            description="The type of shipment.",
        ),
    ]

    shipment_structure: Annotated[
        Optional[ShipmentConfirmationShipmentStructureEnum],
        Field(
            None,
            validation_alias=AliasChoices("shipmentStructure", "shipment_structure"),
            serialization_alias="shipmentStructure",
            description="Shipment hierarchical structure.",
        ),
    ]

    transportation_details: Annotated[
        Optional["TransportationDetailsForShipmentConfirmation"],
        Field(
            None,
            validation_alias=AliasChoices(
                "transportationDetails", "transportation_details"
            ),
            serialization_alias="transportationDetails",
            description="Transportation details for this shipment.",
        ),
    ]

    amazon_reference_number: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "amazonReferenceNumber", "amazon_reference_number"
            ),
            serialization_alias="amazonReferenceNumber",
            description="The Amazon Reference Number is a unique identifier generated by Amazon for all Collect/WePay shipments when you submit a routing request. This field is mandatory for Collect/WePay shipments.",
        ),
    ]

    shipment_confirmation_date: Annotated[
        datetime,
        Field(
            ...,
            validation_alias=AliasChoices(
                "shipmentConfirmationDate", "shipment_confirmation_date"
            ),
            serialization_alias="shipmentConfirmationDate",
            description="Date on which the shipment confirmation was submitted.",
        ),
    ]

    shipped_date: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices("shippedDate", "shipped_date"),
            serialization_alias="shippedDate",
            description="The date and time of the departure of the shipment from the vendor's location. Vendors are requested to send ASNs within 30 minutes of departure from their warehouse/distribution center or at least 6 hours prior to the appointment time at the buyer destination warehouse, whichever is sooner. Shipped date mentioned in the shipment confirmation should not be in the future.",
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
            description="The date and time on which the shipment is estimated to reach buyer's warehouse. It needs to be an estimate based on the average transit time between ship from location and the destination. The exact appointment time will be provided by the buyer and is potentially not known when creating the shipment confirmation.",
        ),
    ]

    selling_party: Annotated[
        "PartyIdentification",
        Field(
            ...,
            validation_alias=AliasChoices("sellingParty", "selling_party"),
            serialization_alias="sellingParty",
            description="Name/Address and tax details of the selling party.",
        ),
    ]

    ship_from_party: Annotated[
        "PartyIdentification",
        Field(
            ...,
            validation_alias=AliasChoices("shipFromParty", "ship_from_party"),
            serialization_alias="shipFromParty",
            description="Name/Address and tax details of the ship from party.",
        ),
    ]

    ship_to_party: Annotated[
        "PartyIdentification",
        Field(
            ...,
            validation_alias=AliasChoices("shipToParty", "ship_to_party"),
            serialization_alias="shipToParty",
            description="Name/Address of the destination warehouse where the shipment is being shipped to.",
        ),
    ]

    shipment_measurements: Annotated[
        Optional["ShipmentMeasurements"],
        Field(
            None,
            validation_alias=AliasChoices(
                "shipmentMeasurements", "shipment_measurements"
            ),
            serialization_alias="shipmentMeasurements",
        ),
    ]

    import_details: Annotated[
        Optional["ImportDetails"],
        Field(
            None,
            validation_alias=AliasChoices("importDetails", "import_details"),
            serialization_alias="importDetails",
            description="Provide these fields only if this shipment is a direct import.",
        ),
    ]

    shipped_items: Annotated[
        List["Item"],
        Field(
            ...,
            validation_alias=AliasChoices("shippedItems", "shipped_items"),
            serialization_alias="shippedItems",
            description="A list of the items in this shipment and their associated details. If any of the item detail fields are common at a carton or a pallet level, provide them at the corresponding carton or pallet level.",
        ),
    ]

    cartons: Annotated[
        Optional[List["Carton"]],
        Field(None, description="A list of the cartons in this shipment."),
    ]

    pallets: Annotated[
        Optional[List["Pallet"]],
        Field(None, description="A list of the pallets in this shipment."),
    ]


"""
SubmitShipmentConfirmationsRequestBody

The request schema for the SubmitShipmentConfirmations operation.
"""


class SubmitShipmentConfirmationsRequestBody(SpApiBaseModel):
    """The request schema for the SubmitShipmentConfirmations operation."""

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
            description="A list of one or more shipment confirmations.",
        ),
    ]


"""
SubmitShipmentConfirmationsRequest

Request parameters for SubmitShipmentConfirmations
"""


class SubmitShipmentConfirmationsRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for SubmitShipmentConfirmations
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    body: Annotated[
        "SubmitShipmentConfirmationsRequestBody",
        BodyParam(),
        Field(..., description="[BODY] A request to submit shipment confirmation."),
    ]


"""
TransactionReference

The response payload for the SubmitShipmentConfirmations operation.
"""


class TransactionReference(SpApiBaseModel):
    """The response payload for the SubmitShipmentConfirmations operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    transaction_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("transactionId", "transaction_id"),
            serialization_alias="transactionId",
            description="GUID assigned by Buyer to identify this transaction. This value can be used with the Transaction Status API to return the status of this transaction.",
        ),
    ]


"""
SubmitShipmentConfirmationsResponse

The response schema for the SubmitShipmentConfirmations operation.
"""


class SubmitShipmentConfirmationsResponse(SpApiBaseModel):
    """The response schema for the SubmitShipmentConfirmations operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["TransactionReference"],
        Field(
            None,
            description="The response payload for the SubmitShipmentConfirmations operation.",
        ),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
        ),
    ]


"""
SubmitShipments

The request schema for the SubmitShipments operation.
"""


class SubmitShipments(SpApiBaseModel):
    """The request schema for the SubmitShipments operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    shipments: Annotated[
        Optional[List["Shipment"]],
        Field(
            None, description="A list of one or more shipments with underlying details."
        ),
    ]


"""
SubmitShipmentsRequest

Request parameters for SubmitShipments
"""


class SubmitShipmentsRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for SubmitShipments
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    body: Annotated[
        "SubmitShipments",
        BodyParam(),
        Field(..., description="[BODY] A request to submit shipment request."),
    ]


# Rebuild models to resolve forward references
SubmitShipmentConfirmationsRequestBody.model_rebuild()
SubmitShipments.model_rebuild()
GetShipmentDetailsResponse.model_rebuild()
GetShipmentLabels.model_rebuild()
ShipmentDetails.model_rebuild()
TransportationLabels.model_rebuild()
Pagination.model_rebuild()
ShipmentConfirmation.model_rebuild()
Shipment.model_rebuild()
TransportLabel.model_rebuild()
ShipmentMeasurements.model_rebuild()
ShipmentInformation.model_rebuild()
LabelData.model_rebuild()
VendorDetails.model_rebuild()
ShipmentStatusDetails.model_rebuild()
TransportShipmentMeasurements.model_rebuild()
CollectFreightPickupDetails.model_rebuild()
PurchaseOrders.model_rebuild()
TransportationDetails.model_rebuild()
TransportationDetailsForShipmentConfirmation.model_rebuild()
CarrierDetails.model_rebuild()
ImportDetails.model_rebuild()
Containers.model_rebuild()
PackedItems.model_rebuild()
Item.model_rebuild()
PurchaseOrderItems.model_rebuild()
Carton.model_rebuild()
InnerContainersDetails.model_rebuild()
ContainerSequenceNumbers.model_rebuild()
Pallet.model_rebuild()
ItemDetails.model_rebuild()
PackageItemDetails.model_rebuild()
PurchaseOrderItemDetails.model_rebuild()
ContainerIdentification.model_rebuild()
ContainerItem.model_rebuild()
CartonReferenceDetails.model_rebuild()
PartyIdentification.model_rebuild()
TaxRegistrationDetails.model_rebuild()
Address.model_rebuild()
Route.model_rebuild()
Stop.model_rebuild()
Location.model_rebuild()
Dimensions.model_rebuild()
Volume.model_rebuild()
Weight.model_rebuild()
Money.model_rebuild()
ItemQuantity.model_rebuild()
TotalWeight.model_rebuild()
PackedQuantity.model_rebuild()
Expiry.model_rebuild()
Duration.model_rebuild()
SubmitShipmentConfirmationsResponse.model_rebuild()
TransactionReference.model_rebuild()
Error.model_rebuild()
SubmitShipmentConfirmationsRequest.model_rebuild()
SubmitShipmentsRequest.model_rebuild()
GetShipmentDetailsRequest.model_rebuild()
GetShipmentLabelsRequest.model_rebuild()
