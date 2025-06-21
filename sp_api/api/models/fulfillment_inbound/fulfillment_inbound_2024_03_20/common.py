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

Specific details to identify a place.
"""


class Address(SpApiBaseModel):
    """Specific details to identify a place."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    address_line1: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("addressLine1", "address_line1"),
            serialization_alias="addressLine1",
            description="Street address information.",
        ),
    ]

    address_line2: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("addressLine2", "address_line2"),
            serialization_alias="addressLine2",
            description="Additional street address information.",
        ),
    ]

    city: Annotated[str, Field(..., description="The city.")]

    company_name: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("companyName", "company_name"),
            serialization_alias="companyName",
            description="The name of the business.",
        ),
    ]

    country_code: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("countryCode", "country_code"),
            serialization_alias="countryCode",
            description="The country code in two-character ISO 3166-1 alpha-2 format.",
        ),
    ]

    email: Annotated[Optional[str], Field(None, description="The email address.")]

    name: Annotated[
        str,
        Field(
            ..., description="The name of the individual who is the primary contact."
        ),
    ]

    phone_number: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("phoneNumber", "phone_number"),
            serialization_alias="phoneNumber",
            description="The phone number.",
        ),
    ]

    postal_code: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("postalCode", "postal_code"),
            serialization_alias="postalCode",
            description="The postal code.",
        ),
    ]

    state_or_province_code: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "stateOrProvinceCode", "state_or_province_code"
            ),
            serialization_alias="stateOrProvinceCode",
            description="The state or province code.",
        ),
    ]


"""
AddressInput

Specific details to identify a place.
"""


class AddressInput(SpApiBaseModel):
    """Specific details to identify a place."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    address_line1: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("addressLine1", "address_line1"),
            serialization_alias="addressLine1",
            description="Street address information.",
        ),
    ]

    address_line2: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("addressLine2", "address_line2"),
            serialization_alias="addressLine2",
            description="Additional street address information.",
        ),
    ]

    city: Annotated[str, Field(..., description="The city.")]

    company_name: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("companyName", "company_name"),
            serialization_alias="companyName",
            description="The name of the business.",
        ),
    ]

    country_code: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("countryCode", "country_code"),
            serialization_alias="countryCode",
            description="The country code in two-character ISO 3166-1 alpha-2 format.",
        ),
    ]

    email: Annotated[Optional[str], Field(None, description="The email address.")]

    name: Annotated[
        str,
        Field(
            ..., description="The name of the individual who is the primary contact."
        ),
    ]

    phone_number: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("phoneNumber", "phone_number"),
            serialization_alias="phoneNumber",
            description="The phone number.",
        ),
    ]

    postal_code: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("postalCode", "postal_code"),
            serialization_alias="postalCode",
            description="The postal code.",
        ),
    ]

    state_or_province_code: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "stateOrProvinceCode", "state_or_province_code"
            ),
            serialization_alias="stateOrProvinceCode",
            description="The state or province code.",
        ),
    ]


AllOwnersConstraint = str
"""A constraint that applies to all owners. If no constraint is specified, defer to any individual owner constraints."""


"""
AppointmentSlotTime

An appointment slot time with start and end.
"""


class AppointmentSlotTime(SpApiBaseModel):
    """An appointment slot time with start and end."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    end_time: Annotated[
        datetime,
        Field(
            ...,
            validation_alias=AliasChoices("endTime", "end_time"),
            serialization_alias="endTime",
            description="The end timestamp of the appointment in UTC.",
        ),
    ]

    start_time: Annotated[
        datetime,
        Field(
            ...,
            validation_alias=AliasChoices("startTime", "start_time"),
            serialization_alias="startTime",
            description="The start timestamp of the appointment in UTC.",
        ),
    ]


"""
AppointmentSlot

The fulfillment center appointment slot for the transportation option.
"""


class AppointmentSlot(SpApiBaseModel):
    """The fulfillment center appointment slot for the transportation option."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    slot_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("slotId", "slot_id"),
            serialization_alias="slotId",
            description="An identifier to a self-ship appointment slot.",
        ),
    ]

    slot_time: Annotated[
        "AppointmentSlotTime",
        Field(
            ...,
            validation_alias=AliasChoices("slotTime", "slot_time"),
            serialization_alias="slotTime",
        ),
    ]


BoxContentInformationSource = str
"""Indication of how box content is meant to be provided."""


UnitOfMeasurement = str
"""Unit of linear measure."""


"""
Dimensions

Measurement of a package's dimensions.
"""


class Dimensions(SpApiBaseModel):
    """Measurement of a package's dimensions."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    height: Annotated[float, Field(..., description="The height of a package.")]

    length: Annotated[float, Field(..., description="The length of a package.")]

    unit_of_measurement: Annotated[
        "UnitOfMeasurement",
        Field(
            ...,
            validation_alias=AliasChoices("unitOfMeasurement", "unit_of_measurement"),
            serialization_alias="unitOfMeasurement",
        ),
    ]

    width: Annotated[float, Field(..., description="The width of a package.")]


"""
Currency

The type and amount of currency.
"""


class Currency(SpApiBaseModel):
    """The type and amount of currency."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    amount: Annotated[float, Field(..., description="Decimal value of the currency.")]

    code: Annotated[
        str, Field(..., description="ISO 4217 standard of a currency code.")
    ]


"""
PrepInstruction

Information pertaining to the preparation of inbound goods.
"""


class PrepInstruction(SpApiBaseModel):
    """Information pertaining to the preparation of inbound goods."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    fee: Annotated[
        Optional["Currency"],
        Field(
            None,
        ),
    ]

    prep_owner: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("prepOwner", "prep_owner"),
            serialization_alias="prepOwner",
            description="In some situations, special preparations are required for items and this field reflects the owner of the preparations. Options include `AMAZON`, `SELLER` or `NONE`.",
        ),
    ]

    prep_type: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("prepType", "prep_type"),
            serialization_alias="prepType",
            description="Type of preparation that should be done. Possible values: `ITEM_LABELING`, `ITEM_BUBBLEWRAP`, `ITEM_POLYBAGGING`, `ITEM_TAPING`, `ITEM_BLACK_SHRINKWRAP`, `ITEM_HANG_GARMENT`, `ITEM_BOXING`, `ITEM_SETCREAT`, `ITEM_RMOVHANG`, `ITEM_SUFFOSTK`, `ITEM_CAP_SEALING`, `ITEM_DEBUNDLE`, `ITEM_SETSTK`, `ITEM_SIOC`, `ITEM_NO_PREP`, `ADULT`, `BABY`, `TEXTILE`, `HANGER`, `FRAGILE`, `LIQUID`, `SHARP`, `SMALL`, `PERFORATED`, `GRANULAR`, `SET`, `FC_PROVIDED`, `UNKNOWN`, `NONE`.",
        ),
    ]


"""
Item

Information associated with a single SKU in the seller's catalog.
"""


class Item(SpApiBaseModel):
    """Information associated with a single SKU in the seller's catalog."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    asin: Annotated[
        str,
        Field(
            ...,
            description="The Amazon Standard Identification Number (ASIN) of the item.",
        ),
    ]

    expiration: Annotated[
        Optional[str],
        Field(
            None,
            description="The expiration date of the MSKU. In [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) datetime format with pattern`YYYY-MM-DD`. The same MSKU with different expiration dates cannot go into the same box.",
        ),
    ]

    fnsku: Annotated[
        str,
        Field(
            ...,
            description="A unique identifier assigned by Amazon to products stored in and fulfilled from an Amazon fulfillment center.",
        ),
    ]

    label_owner: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("labelOwner", "label_owner"),
            serialization_alias="labelOwner",
            description="Specifies who will label the items. Options include `AMAZON`, `SELLER`, and `NONE`.",
        ),
    ]

    manufacturing_lot_code: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "manufacturingLotCode", "manufacturing_lot_code"
            ),
            serialization_alias="manufacturingLotCode",
            description="The manufacturing lot code.",
        ),
    ]

    msku: Annotated[
        str,
        Field(
            ...,
            description="The merchant SKU, a merchant-supplied identifier of a specific SKU.",
        ),
    ]

    prep_instructions: Annotated[
        List["PrepInstruction"],
        Field(
            ...,
            validation_alias=AliasChoices("prepInstructions", "prep_instructions"),
            serialization_alias="prepInstructions",
            description="Special preparations that are required for an item.",
        ),
    ]

    quantity: Annotated[
        int, Field(..., description="The number of the specified MSKU.")
    ]


"""
Region

Representation of a location used within the inbounding experience.
"""


class Region(SpApiBaseModel):
    """Representation of a location used within the inbounding experience."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    country_code: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("countryCode", "country_code"),
            serialization_alias="countryCode",
            description="ISO 3166 standard alpha-2 country code.",
        ),
    ]

    state: Annotated[Optional[str], Field(None, description="State.")]

    warehouse_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("warehouseId", "warehouse_id"),
            serialization_alias="warehouseId",
            description="An identifier for a warehouse, such as a FC, IXD, upstream storage.",
        ),
    ]


UnitOfWeight = str
"""Unit of the weight being measured."""


"""
Weight

The weight of a package.
"""


class Weight(SpApiBaseModel):
    """The weight of a package."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    unit: Annotated[
        "UnitOfWeight",
        Field(
            ...,
        ),
    ]

    value: Annotated[float, Field(..., description="Value of a weight.")]


"""
Box

Contains information about a box that is used in the inbound plan. The box is a container that holds multiple items.
"""


class Box(SpApiBaseModel):
    """Contains information about a box that is used in the inbound plan. The box is a container that holds multiple items."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    box_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("boxId", "box_id"),
            serialization_alias="boxId",
            description="The ID provided by Amazon that identifies a given box. This ID is comprised of the external shipment ID (which is generated after transportation has been confirmed) and the index of the box.",
        ),
    ]

    content_information_source: Annotated[
        Optional["BoxContentInformationSource"],
        Field(
            None,
            validation_alias=AliasChoices(
                "contentInformationSource", "content_information_source"
            ),
            serialization_alias="contentInformationSource",
        ),
    ]

    destination_region: Annotated[
        Optional["Region"],
        Field(
            None,
            validation_alias=AliasChoices("destinationRegion", "destination_region"),
            serialization_alias="destinationRegion",
        ),
    ]

    dimensions: Annotated[
        Optional["Dimensions"],
        Field(
            None,
        ),
    ]

    external_container_identifier: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "externalContainerIdentifier", "external_container_identifier"
            ),
            serialization_alias="externalContainerIdentifier",
            description="The external identifier for this container / box.",
        ),
    ]

    external_container_identifier_type: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "externalContainerIdentifierType", "external_container_identifier_type"
            ),
            serialization_alias="externalContainerIdentifierType",
            description="Type of the external identifier used. Can be: `AMAZON`, `SSCC`.",
        ),
    ]

    items: Annotated[
        Optional[List["Item"]],
        Field(None, description="Items contained within the box."),
    ]

    package_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("packageId", "package_id"),
            serialization_alias="packageId",
            description="Primary key to uniquely identify a Package (Box or Pallet).",
        ),
    ]

    quantity: Annotated[
        Optional[int],
        Field(
            None,
            description="The number of containers where all other properties like weight or dimensions are identical.",
        ),
    ]

    template_name: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("templateName", "template_name"),
            serialization_alias="templateName",
            description="Template name of the box.",
        ),
    ]

    weight: Annotated[
        Optional["Weight"],
        Field(
            None,
        ),
    ]


LabelOwner = str
"""Specifies who will label the items. Options include `AMAZON`, `SELLER` or `NONE`."""


PrepOwner = str
"""The owner of the preparations, if special preparations are required."""


"""
ItemInput

Defines an item's input parameters.
"""


class ItemInput(SpApiBaseModel):
    """Defines an item's input parameters."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    expiration: Annotated[
        Optional[str],
        Field(
            None,
            description="The expiration date of the MSKU. In [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) datetime format with pattern `YYYY-MM-DD`. Items with the same MSKU but different expiration dates cannot go into the same box.",
        ),
    ]

    label_owner: Annotated[
        "LabelOwner",
        Field(
            ...,
            validation_alias=AliasChoices("labelOwner", "label_owner"),
            serialization_alias="labelOwner",
        ),
    ]

    manufacturing_lot_code: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "manufacturingLotCode", "manufacturing_lot_code"
            ),
            serialization_alias="manufacturingLotCode",
            description="The manufacturing lot code.",
        ),
    ]

    msku: Annotated[
        str,
        Field(
            ...,
            description="The merchant SKU, a merchant-supplied identifier of a specific SKU.",
        ),
    ]

    prep_owner: Annotated[
        "PrepOwner",
        Field(
            ...,
            validation_alias=AliasChoices("prepOwner", "prep_owner"),
            serialization_alias="prepOwner",
        ),
    ]

    quantity: Annotated[
        int,
        Field(
            ...,
            description="The number of units of the specified MSKU that will be shipped.",
        ),
    ]


"""
BoxInput

Input information for a given box.
"""


class BoxInput(SpApiBaseModel):
    """Input information for a given box."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    content_information_source: Annotated[
        "BoxContentInformationSource",
        Field(
            ...,
            validation_alias=AliasChoices(
                "contentInformationSource", "content_information_source"
            ),
            serialization_alias="contentInformationSource",
        ),
    ]

    dimensions: Annotated[
        "Dimensions",
        Field(
            ...,
        ),
    ]

    items: Annotated[
        Optional[List["ItemInput"]],
        Field(
            None,
            description="The items and their quantity in the box. This must be empty if the box `contentInformationSource` is `BARCODE_2D` or `MANUAL_PROCESS`.",
        ),
    ]

    quantity: Annotated[
        int,
        Field(
            ...,
            description="The number of containers where all other properties like weight or dimensions are identical.",
        ),
    ]

    weight: Annotated[
        "Weight",
        Field(
            ...,
        ),
    ]


"""
WeightRange

The range of weights that are allowed for a package.
"""


class WeightRange(SpApiBaseModel):
    """The range of weights that are allowed for a package."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    maximum: Annotated[float, Field(..., description="Maximum allowed weight.")]

    minimum: Annotated[float, Field(..., description="Minimum allowed weight.")]

    unit: Annotated[
        "UnitOfWeight",
        Field(
            ...,
        ),
    ]


"""
BoxRequirements

The requirements for a box in the packing option.
"""


class BoxRequirements(SpApiBaseModel):
    """The requirements for a box in the packing option."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    weight: Annotated[
        "WeightRange",
        Field(
            ...,
        ),
    ]


"""
BoxUpdateInput

Input information for updating a box
"""


class BoxUpdateInput(SpApiBaseModel):
    """Input information for updating a box"""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    content_information_source: Annotated[
        "BoxContentInformationSource",
        Field(
            ...,
            validation_alias=AliasChoices(
                "contentInformationSource", "content_information_source"
            ),
            serialization_alias="contentInformationSource",
        ),
    ]

    dimensions: Annotated[
        "Dimensions",
        Field(
            ...,
        ),
    ]

    items: Annotated[
        Optional[List["ItemInput"]],
        Field(
            None,
            description="The items and their quantity in the box. This must be empty if the box `contentInformationSource` is `BARCODE_2D` or `MANUAL_PROCESS`.",
        ),
    ]

    package_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("packageId", "package_id"),
            serialization_alias="packageId",
            description="Primary key to uniquely identify a Box Package. PackageId must be provided if the intent is to update an existing box. Adding a new box will not require providing this value. Any existing PackageIds not provided will be treated as to-be-removed",
        ),
    ]

    quantity: Annotated[
        int,
        Field(
            ...,
            description="The number of containers where all other properties like weight or dimensions are identical.",
        ),
    ]

    weight: Annotated[
        "Weight",
        Field(
            ...,
        ),
    ]


"""
CancelInboundPlanRequest

Request parameters for cancelInboundPlan
"""


class CancelInboundPlanRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for cancelInboundPlan
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    inbound_plan_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("inboundPlanId", "inbound_plan_id"),
            serialization_alias="inboundPlanId",
            description="[PATH] Identifier of an inbound plan.",
        ),
    ]


"""
CancelInboundPlanResponse

The `cancelInboundPlan` response.
"""


class CancelInboundPlanResponse(SpApiBaseModel):
    """The `cancelInboundPlan` response."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    operation_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("operationId", "operation_id"),
            serialization_alias="operationId",
            description="UUID for the given operation.",
        ),
    ]


ReasonComment = str
"""Reason for cancelling or rescheduling a self-ship appointment."""


"""
CancelSelfShipAppointmentRequestBody

The `cancelSelfShipAppointment` request.
"""


class CancelSelfShipAppointmentRequestBody(SpApiBaseModel):
    """The `cancelSelfShipAppointment` request."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    reason_comment: Annotated[
        Optional["ReasonComment"],
        Field(
            None,
            validation_alias=AliasChoices("reasonComment", "reason_comment"),
            serialization_alias="reasonComment",
        ),
    ]


"""
CancelSelfShipAppointmentRequest

Request parameters for cancelSelfShipAppointment
"""


class CancelSelfShipAppointmentRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for cancelSelfShipAppointment
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    inbound_plan_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("inboundPlanId", "inbound_plan_id"),
            serialization_alias="inboundPlanId",
            description="[PATH] Identifier of an inbound plan.",
        ),
    ]

    shipment_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("shipmentId", "shipment_id"),
            serialization_alias="shipmentId",
            description="[PATH] Identifier of a shipment. A shipment contains the boxes and units being inbounded.",
        ),
    ]

    body: Annotated[
        "CancelSelfShipAppointmentRequestBody",
        BodyParam(),
        Field(
            ...,
            description="[BODY] The body of the request to `cancelSelfShipAppointment`.",
        ),
    ]


"""
CancelSelfShipAppointmentResponse

The `CancelSelfShipAppointment` response.
"""


class CancelSelfShipAppointmentResponse(SpApiBaseModel):
    """The `CancelSelfShipAppointment` response."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    operation_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("operationId", "operation_id"),
            serialization_alias="operationId",
            description="UUID for the given operation.",
        ),
    ]


"""
Carrier

The carrier for the inbound shipment.
"""


class Carrier(SpApiBaseModel):
    """The carrier for the inbound shipment."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    alpha_code: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("alphaCode", "alpha_code"),
            serialization_alias="alphaCode",
            description="The carrier code. For example, USPS or DHLEX.",
        ),
    ]

    name: Annotated[Optional[str], Field(None, description="The name of the carrier.")]


"""
CarrierAppointment

Contains details for a transportation carrier appointment. This appointment is vended out by Amazon and is an indicator for when a transportation carrier is accepting shipments to be picked up.
"""


class CarrierAppointment(SpApiBaseModel):
    """Contains details for a transportation carrier appointment. This appointment is vended out by Amazon and is an indicator for when a transportation carrier is accepting shipments to be picked up."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    end_time: Annotated[
        datetime,
        Field(
            ...,
            validation_alias=AliasChoices("endTime", "end_time"),
            serialization_alias="endTime",
            description="The end timestamp of the appointment in UTC.",
        ),
    ]

    start_time: Annotated[
        datetime,
        Field(
            ...,
            validation_alias=AliasChoices("startTime", "start_time"),
            serialization_alias="startTime",
            description="The start timestamp of the appointment in UTC.",
        ),
    ]


"""
TaxRate

Contains the type and rate of tax.
"""


class TaxRate(SpApiBaseModel):
    """Contains the type and rate of tax."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    cess_rate: Annotated[
        Optional[float],
        Field(
            None,
            validation_alias=AliasChoices("cessRate", "cess_rate"),
            serialization_alias="cessRate",
            description="Rate of cess tax.",
        ),
    ]

    gst_rate: Annotated[
        Optional[float],
        Field(
            None,
            validation_alias=AliasChoices("gstRate", "gst_rate"),
            serialization_alias="gstRate",
            description="Rate of gst tax.",
        ),
    ]

    tax_type: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("taxType", "tax_type"),
            serialization_alias="taxType",
            description="Type of tax. Possible values: `CGST`, `SGST`, `IGST`, `TOTAL_TAX`.",
        ),
    ]


"""
TaxDetails

Information used to determine the tax compliance.
"""


class TaxDetails(SpApiBaseModel):
    """Information used to determine the tax compliance."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    declared_value: Annotated[
        Optional["Currency"],
        Field(
            None,
            validation_alias=AliasChoices("declaredValue", "declared_value"),
            serialization_alias="declaredValue",
        ),
    ]

    hsn_code: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("hsnCode", "hsn_code"),
            serialization_alias="hsnCode",
            description="Harmonized System of Nomenclature code.",
        ),
    ]

    tax_rates: Annotated[
        Optional[List["TaxRate"]],
        Field(
            None,
            validation_alias=AliasChoices("taxRates", "tax_rates"),
            serialization_alias="taxRates",
            description="List of tax rates.",
        ),
    ]


"""
ComplianceDetail

Contains item identifiers and related tax information.
"""


class ComplianceDetail(SpApiBaseModel):
    """Contains item identifiers and related tax information."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    asin: Annotated[
        Optional[str],
        Field(
            None,
            description="The Amazon Standard Identification Number, which identifies the detail page identifier.",
        ),
    ]

    fnsku: Annotated[
        Optional[str],
        Field(
            None,
            description="The Fulfillment Network SKU, which identifies a real fulfillable item with catalog data and condition.",
        ),
    ]

    msku: Annotated[
        Optional[str],
        Field(
            None,
            description="The merchant SKU, a merchant-supplied identifier for a specific SKU.",
        ),
    ]

    tax_details: Annotated[
        Optional["TaxDetails"],
        Field(
            None,
            validation_alias=AliasChoices("taxDetails", "tax_details"),
            serialization_alias="taxDetails",
        ),
    ]


"""
ConfirmDeliveryWindowOptionsRequest

Request parameters for confirmDeliveryWindowOptions
"""


class ConfirmDeliveryWindowOptionsRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for confirmDeliveryWindowOptions
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    inbound_plan_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("inboundPlanId", "inbound_plan_id"),
            serialization_alias="inboundPlanId",
            description="[PATH] Identifier of an inbound plan.",
        ),
    ]

    shipment_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("shipmentId", "shipment_id"),
            serialization_alias="shipmentId",
            description="[PATH] The shipment to confirm the delivery window option for.",
        ),
    ]

    delivery_window_option_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices(
                "deliveryWindowOptionId", "delivery_window_option_id"
            ),
            serialization_alias="deliveryWindowOptionId",
            description="[PATH] The id of the delivery window option to be confirmed.",
        ),
    ]


"""
ConfirmDeliveryWindowOptionsResponse

The `confirmDeliveryWindowOptions` response.
"""


class ConfirmDeliveryWindowOptionsResponse(SpApiBaseModel):
    """The `confirmDeliveryWindowOptions` response."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    operation_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("operationId", "operation_id"),
            serialization_alias="operationId",
            description="UUID for the given operation.",
        ),
    ]


"""
ConfirmPackingOptionRequest

Request parameters for confirmPackingOption
"""


class ConfirmPackingOptionRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for confirmPackingOption
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    inbound_plan_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("inboundPlanId", "inbound_plan_id"),
            serialization_alias="inboundPlanId",
            description="[PATH] Identifier of an inbound plan.",
        ),
    ]

    packing_option_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("packingOptionId", "packing_option_id"),
            serialization_alias="packingOptionId",
            description="[PATH] Identifier of a packing option.",
        ),
    ]


"""
ConfirmPackingOptionResponse

The `confirmPackingOption` response.
"""


class ConfirmPackingOptionResponse(SpApiBaseModel):
    """The `confirmPackingOption` response."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    operation_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("operationId", "operation_id"),
            serialization_alias="operationId",
            description="UUID for the given operation.",
        ),
    ]


"""
ConfirmPlacementOptionRequest

Request parameters for confirmPlacementOption
"""


class ConfirmPlacementOptionRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for confirmPlacementOption
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    inbound_plan_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("inboundPlanId", "inbound_plan_id"),
            serialization_alias="inboundPlanId",
            description="[PATH] Identifier of an inbound plan.",
        ),
    ]

    placement_option_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("placementOptionId", "placement_option_id"),
            serialization_alias="placementOptionId",
            description="[PATH] The identifier of a placement option. A placement option represents the shipment splits and destinations of SKUs.",
        ),
    ]


"""
ConfirmPlacementOptionResponse

The `confirmPlacementOption` response.
"""


class ConfirmPlacementOptionResponse(SpApiBaseModel):
    """The `confirmPlacementOption` response."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    operation_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("operationId", "operation_id"),
            serialization_alias="operationId",
            description="UUID for the given operation.",
        ),
    ]


"""
ConfirmShipmentContentUpdatePreviewRequest

Request parameters for confirmShipmentContentUpdatePreview
"""


class ConfirmShipmentContentUpdatePreviewRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for confirmShipmentContentUpdatePreview
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    inbound_plan_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("inboundPlanId", "inbound_plan_id"),
            serialization_alias="inboundPlanId",
            description="[PATH] Identifier of an inbound plan.",
        ),
    ]

    shipment_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("shipmentId", "shipment_id"),
            serialization_alias="shipmentId",
            description="[PATH] Identifier of a shipment. A shipment contains the boxes and units being inbounded.",
        ),
    ]

    content_update_preview_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices(
                "contentUpdatePreviewId", "content_update_preview_id"
            ),
            serialization_alias="contentUpdatePreviewId",
            description="[PATH] Identifier of a content update preview.",
        ),
    ]


"""
ConfirmShipmentContentUpdatePreviewResponse

The `confirmShipmentContentUpdatePreview` response.
"""


class ConfirmShipmentContentUpdatePreviewResponse(SpApiBaseModel):
    """The `confirmShipmentContentUpdatePreview` response."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    operation_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("operationId", "operation_id"),
            serialization_alias="operationId",
            description="UUID for the given operation.",
        ),
    ]


"""
ContactInformation

The seller's contact information.
"""


class ContactInformation(SpApiBaseModel):
    """The seller's contact information."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    email: Annotated[Optional[str], Field(None, description="The email address.")]

    name: Annotated[str, Field(..., description="The contact's name.")]

    phone_number: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("phoneNumber", "phone_number"),
            serialization_alias="phoneNumber",
            description="The phone number.",
        ),
    ]


"""
TransportationSelection

The transportation option selected to confirm.
"""


class TransportationSelection(SpApiBaseModel):
    """The transportation option selected to confirm."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    contact_information: Annotated[
        Optional["ContactInformation"],
        Field(
            None,
            validation_alias=AliasChoices("contactInformation", "contact_information"),
            serialization_alias="contactInformation",
        ),
    ]

    shipment_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("shipmentId", "shipment_id"),
            serialization_alias="shipmentId",
            description="Shipment ID that the transportation Option is for.",
        ),
    ]

    transportation_option_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices(
                "transportationOptionId", "transportation_option_id"
            ),
            serialization_alias="transportationOptionId",
            description="Transportation option being selected for the provided shipment.",
        ),
    ]


"""
ConfirmTransportationOptionsRequestBody

The `confirmTransportationOptions` request.
"""


class ConfirmTransportationOptionsRequestBody(SpApiBaseModel):
    """The `confirmTransportationOptions` request."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    transportation_selections: Annotated[
        List["TransportationSelection"],
        Field(
            ...,
            validation_alias=AliasChoices(
                "transportationSelections", "transportation_selections"
            ),
            serialization_alias="transportationSelections",
            description="Information needed to confirm one of the available transportation options.",
        ),
    ]


"""
ConfirmTransportationOptionsRequest

Request parameters for confirmTransportationOptions
"""


class ConfirmTransportationOptionsRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for confirmTransportationOptions
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    inbound_plan_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("inboundPlanId", "inbound_plan_id"),
            serialization_alias="inboundPlanId",
            description="[PATH] Identifier of an inbound plan.",
        ),
    ]

    body: Annotated[
        "ConfirmTransportationOptionsRequestBody",
        BodyParam(),
        Field(
            ...,
            description="[BODY] The body of the request to `confirmTransportationOptions`.",
        ),
    ]


"""
ConfirmTransportationOptionsResponse

The `confirmTransportationOptions` response.
"""


class ConfirmTransportationOptionsResponse(SpApiBaseModel):
    """The `confirmTransportationOptions` response."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    operation_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("operationId", "operation_id"),
            serialization_alias="operationId",
            description="UUID for the given operation.",
        ),
    ]


"""
RequestedUpdates

Objects that were included in the update request.
"""


class RequestedUpdates(SpApiBaseModel):
    """Objects that were included in the update request."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    boxes: Annotated[
        Optional[List["BoxUpdateInput"]],
        Field(
            None,
            description="A list of boxes that will be present in the shipment after the update.",
        ),
    ]

    items: Annotated[
        Optional[List["ItemInput"]],
        Field(
            None,
            description="A list of all items that will be present in the shipment after the update.",
        ),
    ]


"""
Quote

The estimated shipping cost associated with the transportation option.
"""


class Quote(SpApiBaseModel):
    """The estimated shipping cost associated with the transportation option."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    cost: Annotated[
        "Currency",
        Field(
            ...,
        ),
    ]

    expiration: Annotated[
        Optional[datetime],
        Field(
            None,
            description="The time at which this transportation option quote expires. In [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) datetime with pattern `yyyy-MM-ddTHH:mm:ss.sssZ`.",
        ),
    ]

    voidable_until: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices("voidableUntil", "voidable_until"),
            serialization_alias="voidableUntil",
            description="Voidable until timestamp.",
        ),
    ]


"""
TransportationOption

Contains information pertaining to a transportation option and the related carrier.
"""


class TransportationOption(SpApiBaseModel):
    """Contains information pertaining to a transportation option and the related carrier."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    carrier: Annotated[
        "Carrier",
        Field(
            ...,
        ),
    ]

    carrier_appointment: Annotated[
        Optional["CarrierAppointment"],
        Field(
            None,
            validation_alias=AliasChoices("carrierAppointment", "carrier_appointment"),
            serialization_alias="carrierAppointment",
        ),
    ]

    preconditions: Annotated[
        List["str"],
        Field(
            ...,
            description="Identifies a list of preconditions for confirming the transportation option.",
        ),
    ]

    quote: Annotated[
        Optional["Quote"],
        Field(
            None,
        ),
    ]

    shipment_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("shipmentId", "shipment_id"),
            serialization_alias="shipmentId",
            description="Identifier of a shipment. A shipment contains the boxes and units being inbounded.",
        ),
    ]

    shipping_mode: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("shippingMode", "shipping_mode"),
            serialization_alias="shippingMode",
            description="Mode of shipment transportation that this option will provide. Possible values: `GROUND_SMALL_PARCEL`, `FREIGHT_LTL`, `FREIGHT_FTL_PALLET`, `FREIGHT_FTL_NONPALLET`, `OCEAN_LCL`, `OCEAN_FCL`, `AIR_SMALL_PARCEL`, `AIR_SMALL_PARCEL_EXPRESS`.",
        ),
    ]

    shipping_solution: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("shippingSolution", "shipping_solution"),
            serialization_alias="shippingSolution",
            description="Shipping program for the option. Possible values: `AMAZON_PARTNERED_CARRIER`, `USE_YOUR_OWN_CARRIER`.",
        ),
    ]

    transportation_option_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices(
                "transportationOptionId", "transportation_option_id"
            ),
            serialization_alias="transportationOptionId",
            description="Identifier of a transportation option. A transportation option represent one option for how to send a shipment.",
        ),
    ]


"""
ContentUpdatePreview

Preview of the changes that will be applied to the shipment.
"""


class ContentUpdatePreview(SpApiBaseModel):
    """Preview of the changes that will be applied to the shipment."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    content_update_preview_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices(
                "contentUpdatePreviewId", "content_update_preview_id"
            ),
            serialization_alias="contentUpdatePreviewId",
            description="Identifier of a content update preview.",
        ),
    ]

    expiration: Annotated[
        datetime,
        Field(
            ...,
            description="The time at which the content update expires. In [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) datetime format with pattern `yyyy-MM-ddTHH:mm:ss.sssZ`.",
        ),
    ]

    requested_updates: Annotated[
        "RequestedUpdates",
        Field(
            ...,
            validation_alias=AliasChoices("requestedUpdates", "requested_updates"),
            serialization_alias="requestedUpdates",
        ),
    ]

    transportation_option: Annotated[
        "TransportationOption",
        Field(
            ...,
            validation_alias=AliasChoices(
                "transportationOption", "transportation_option"
            ),
            serialization_alias="transportationOption",
        ),
    ]


"""
CreateInboundPlanRequestBody

The `createInboundPlan` request.
"""


class CreateInboundPlanRequestBody(SpApiBaseModel):
    """The `createInboundPlan` request."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    destination_marketplaces: Annotated[
        Optional[List["str"]],
        Field(
            None,
            validation_alias=AliasChoices(
                "destinationMarketplaces", "destination_marketplaces"
            ),
            serialization_alias="destinationMarketplaces",
            description="Marketplaces where the items need to be shipped to. Currently only one marketplace can be selected in this request.",
        ),
    ]

    items: Annotated[
        List["ItemInput"], Field(..., description="Items included in this plan.")
    ]

    name: Annotated[
        Optional[str],
        Field(
            None,
            description="Name for the Inbound Plan. If one isn't provided, a default name will be provided.",
        ),
    ]

    source_address: Annotated[
        "AddressInput",
        Field(
            ...,
            validation_alias=AliasChoices("sourceAddress", "source_address"),
            serialization_alias="sourceAddress",
        ),
    ]


"""
CreateInboundPlanRequest

Request parameters for createInboundPlan
"""


class CreateInboundPlanRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for createInboundPlan
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    body: Annotated[
        "CreateInboundPlanRequestBody",
        BodyParam(),
        Field(
            ..., description="[BODY] The body of the request to `createInboundPlan`."
        ),
    ]


"""
CreateInboundPlanResponse

The `createInboundPlan` response.
"""


class CreateInboundPlanResponse(SpApiBaseModel):
    """The `createInboundPlan` response."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    inbound_plan_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("inboundPlanId", "inbound_plan_id"),
            serialization_alias="inboundPlanId",
            description="Identifier of an inbound plan.",
        ),
    ]

    operation_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("operationId", "operation_id"),
            serialization_alias="operationId",
            description="UUID for the given operation.",
        ),
    ]


ItemLabelPageType = str
"""The page type to use to print the labels. Possible values: 'A4_21', 'A4_24', 'A4_24_64x33', 'A4_24_66x35', 'A4_24_70x36', 'A4_24_70x37', 'A4_24i', 'A4_27', 'A4_40_52x29', 'A4_44_48x25', 'Letter_30'."""


LabelPrintType = str
"""Indicates the type of print type for a given label."""


"""
MskuQuantity

Represents an MSKU and the related quantity.
"""


class MskuQuantity(SpApiBaseModel):
    """Represents an MSKU and the related quantity."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    msku: Annotated[
        str,
        Field(
            ...,
            description="The merchant SKU, a merchant-supplied identifier for a specific SKU.",
        ),
    ]

    quantity: Annotated[int, Field(..., description="A positive integer.")]


"""
CreateMarketplaceItemLabelsRequestBody

The `createMarketplaceItemLabels` request.
"""


class CreateMarketplaceItemLabelsRequestBody(SpApiBaseModel):
    """The `createMarketplaceItemLabels` request."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    height: Annotated[
        Optional[float], Field(None, description="The height of the item label.")
    ]

    label_type: Annotated[
        "LabelPrintType",
        Field(
            ...,
            validation_alias=AliasChoices("labelType", "label_type"),
            serialization_alias="labelType",
        ),
    ]

    locale_code: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("localeCode", "locale_code"),
            serialization_alias="localeCode",
            description="The locale code constructed from ISO 639 language code and ISO 3166-1 alpha-2 standard of country codes separated by an underscore character.",
        ),
    ]

    marketplace_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="The Marketplace ID. For a list of possible values, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).",
        ),
    ]

    msku_quantities: Annotated[
        List["MskuQuantity"],
        Field(
            ...,
            validation_alias=AliasChoices("mskuQuantities", "msku_quantities"),
            serialization_alias="mskuQuantities",
            description="Represents the quantity of an MSKU to print item labels for.",
        ),
    ]

    page_type: Annotated[
        Optional["ItemLabelPageType"],
        Field(
            None,
            validation_alias=AliasChoices("pageType", "page_type"),
            serialization_alias="pageType",
        ),
    ]

    width: Annotated[
        Optional[float], Field(None, description="The width of the item label.")
    ]


"""
CreateMarketplaceItemLabelsRequest

Request parameters for createMarketplaceItemLabels
"""


class CreateMarketplaceItemLabelsRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for createMarketplaceItemLabels
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    body: Annotated[
        "CreateMarketplaceItemLabelsRequestBody",
        BodyParam(),
        Field(
            ...,
            description="[BODY] The body of the request to `createMarketplaceItemLabels`.",
        ),
    ]


"""
DocumentDownload

Resource to download the requested document.
"""


class DocumentDownload(SpApiBaseModel):
    """Resource to download the requested document."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    download_type: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("downloadType", "download_type"),
            serialization_alias="downloadType",
            description="The type of download. Possible values: `URL`.",
        ),
    ]

    expiration: Annotated[
        Optional[datetime],
        Field(
            None,
            description="The URI's expiration time. In [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) datetime format with pattern `yyyy-MM-ddTHH:mm:ss.sssZ`.",
        ),
    ]

    uri: Annotated[
        str,
        Field(
            ...,
            description="Uniform resource identifier to identify where the document is located.",
        ),
    ]


"""
CreateMarketplaceItemLabelsResponse

The `createMarketplaceItemLabels` response.
"""


class CreateMarketplaceItemLabelsResponse(SpApiBaseModel):
    """The `createMarketplaceItemLabels` response."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    document_downloads: Annotated[
        List["DocumentDownload"],
        Field(
            ...,
            validation_alias=AliasChoices("documentDownloads", "document_downloads"),
            serialization_alias="documentDownloads",
            description="Resources to download the requested document.",
        ),
    ]


"""
CustomPlacementInput

Provide units going to the warehouse.
"""


class CustomPlacementInput(SpApiBaseModel):
    """Provide units going to the warehouse."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    items: Annotated[
        List["ItemInput"],
        Field(..., description="Items included while creating Inbound Plan."),
    ]

    warehouse_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("warehouseId", "warehouse_id"),
            serialization_alias="warehouseId",
            description="Warehouse Id.",
        ),
    ]


"""
Window

Contains a start and end DateTime representing a time range.
"""


class Window(SpApiBaseModel):
    """Contains a start and end DateTime representing a time range."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    editable_until: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices("editableUntil", "editable_until"),
            serialization_alias="editableUntil",
            description="The timestamp at which this Window can no longer be edited.",
        ),
    ]

    end: Annotated[datetime, Field(..., description="The end timestamp of the window.")]

    start: Annotated[
        datetime, Field(..., description="The start timestamp of the window.")
    ]


"""
Dates

Specifies the date that the seller expects their shipment will be shipped.
"""


class Dates(SpApiBaseModel):
    """Specifies the date that the seller expects their shipment will be shipped."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    ready_to_ship_window: Annotated[
        Optional["Window"],
        Field(
            None,
            validation_alias=AliasChoices("readyToShipWindow", "ready_to_ship_window"),
            serialization_alias="readyToShipWindow",
        ),
    ]


"""
DeliveryWindowOption

Contains information pertaining to a delivery window option.
"""


class DeliveryWindowOption(SpApiBaseModel):
    """Contains information pertaining to a delivery window option."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    availability_type: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("availabilityType", "availability_type"),
            serialization_alias="availabilityType",
            description="Identifies type of Delivery Window Availability. Values: `AVAILABLE`, `CONGESTED`",
        ),
    ]

    delivery_window_option_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices(
                "deliveryWindowOptionId", "delivery_window_option_id"
            ),
            serialization_alias="deliveryWindowOptionId",
            description="Identifier of a delivery window option. A delivery window option represent one option for when a shipment is expected to be delivered.",
        ),
    ]

    end_date: Annotated[
        datetime,
        Field(
            ...,
            validation_alias=AliasChoices("endDate", "end_date"),
            serialization_alias="endDate",
            description="The time at which this delivery window option ends. In [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) datetime format with pattern `yyyy-MM-ddTHH:mmZ`.",
        ),
    ]

    start_date: Annotated[
        datetime,
        Field(
            ...,
            validation_alias=AliasChoices("startDate", "start_date"),
            serialization_alias="startDate",
            description="The time at which this delivery window option starts. In [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) datetime format with pattern `yyyy-MM-ddTHH:mmZ`.",
        ),
    ]

    valid_until: Annotated[
        datetime,
        Field(
            ...,
            validation_alias=AliasChoices("validUntil", "valid_until"),
            serialization_alias="validUntil",
            description="The time at which this window delivery option is no longer valid. In [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) datetime format with pattern `yyyy-MM-ddTHH:mmZ`.",
        ),
    ]


"""
Error

Error object containing information about what went wrong.
"""


class Error(SpApiBaseModel):
    """Error object containing information about what went wrong."""

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

    details: Annotated[
        Optional[str],
        Field(
            None,
            description="Additional details that can help the caller understand or fix the issue.",
        ),
    ]

    message: Annotated[
        str, Field(..., description="A message that describes the error condition.")
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

    errors: Annotated[List["Error"], Field(..., description="List of errors.")]


"""
FreightInformation

Freight information describes the skus being transported. Freight carrier options and quotes will only be returned if the freight information is provided.
"""


class FreightInformation(SpApiBaseModel):
    """Freight information describes the skus being transported. Freight carrier options and quotes will only be returned if the freight information is provided."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    declared_value: Annotated[
        Optional["Currency"],
        Field(
            None,
            validation_alias=AliasChoices("declaredValue", "declared_value"),
            serialization_alias="declaredValue",
        ),
    ]

    freight_class: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("freightClass", "freight_class"),
            serialization_alias="freightClass",
            description="Freight class. Possible values: `NONE`, `FC_50`, `FC_55`, `FC_60`, `FC_65`, `FC_70`, `FC_77_5`, `FC_85`, `FC_92_5`, `FC_100`, `FC_110`, `FC_125`, `FC_150`, `FC_175`, `FC_200`, `FC_250`, `FC_300`, `FC_400`, `FC_500`.",
        ),
    ]


"""
GenerateDeliveryWindowOptionsRequest

Request parameters for generateDeliveryWindowOptions
"""


class GenerateDeliveryWindowOptionsRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for generateDeliveryWindowOptions
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    inbound_plan_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("inboundPlanId", "inbound_plan_id"),
            serialization_alias="inboundPlanId",
            description="[PATH] Identifier of an inbound plan.",
        ),
    ]

    shipment_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("shipmentId", "shipment_id"),
            serialization_alias="shipmentId",
            description="[PATH] The shipment to generate delivery window options for.",
        ),
    ]


"""
GenerateDeliveryWindowOptionsResponse

The `generateDeliveryWindowOptions` response.
"""


class GenerateDeliveryWindowOptionsResponse(SpApiBaseModel):
    """The `generateDeliveryWindowOptions` response."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    operation_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("operationId", "operation_id"),
            serialization_alias="operationId",
            description="UUID for the given operation.",
        ),
    ]


"""
GeneratePackingOptionsRequest

Request parameters for generatePackingOptions
"""


class GeneratePackingOptionsRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for generatePackingOptions
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    inbound_plan_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("inboundPlanId", "inbound_plan_id"),
            serialization_alias="inboundPlanId",
            description="[PATH] Identifier of an inbound plan.",
        ),
    ]


"""
GeneratePackingOptionsResponse

The `generatePackingOptions` response.
"""


class GeneratePackingOptionsResponse(SpApiBaseModel):
    """The `generatePackingOptions` response."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    operation_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("operationId", "operation_id"),
            serialization_alias="operationId",
            description="UUID for the given operation.",
        ),
    ]


"""
GeneratePlacementOptionsRequestBody

The `generatePlacementOptions` request.
"""


class GeneratePlacementOptionsRequestBody(SpApiBaseModel):
    """The `generatePlacementOptions` request."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    custom_placement: Annotated[
        Optional[List["CustomPlacementInput"]],
        Field(
            None,
            validation_alias=AliasChoices("customPlacement", "custom_placement"),
            serialization_alias="customPlacement",
            description="Custom placement options you want to add to the plan. This is only used for the India (IN - A21TJRUUN4KGV) marketplace.",
        ),
    ]


"""
GeneratePlacementOptionsRequest

Request parameters for generatePlacementOptions
"""


class GeneratePlacementOptionsRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for generatePlacementOptions
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    inbound_plan_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("inboundPlanId", "inbound_plan_id"),
            serialization_alias="inboundPlanId",
            description="[PATH] Identifier of an inbound plan.",
        ),
    ]

    body: Annotated[
        "GeneratePlacementOptionsRequestBody",
        BodyParam(),
        Field(
            ...,
            description="[BODY] The body of the request to `generatePlacementOptions`.",
        ),
    ]


"""
GeneratePlacementOptionsResponse

The `generatePlacementOptions` response.
"""


class GeneratePlacementOptionsResponse(SpApiBaseModel):
    """The `generatePlacementOptions` response."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    operation_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("operationId", "operation_id"),
            serialization_alias="operationId",
            description="UUID for the given operation.",
        ),
    ]


"""
GenerateSelfShipAppointmentSlotsRequestBody

The `generateSelfShipAppointmentSlots` request.
"""


class GenerateSelfShipAppointmentSlotsRequestBody(SpApiBaseModel):
    """The `generateSelfShipAppointmentSlots` request."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    desired_end_date: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices("desiredEndDate", "desired_end_date"),
            serialization_alias="desiredEndDate",
            description="The desired end date. In [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) datetime format.",
        ),
    ]

    desired_start_date: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices("desiredStartDate", "desired_start_date"),
            serialization_alias="desiredStartDate",
            description="The desired start date. In [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) datetime format.",
        ),
    ]


"""
GenerateSelfShipAppointmentSlotsRequest

Request parameters for generateSelfShipAppointmentSlots
"""


class GenerateSelfShipAppointmentSlotsRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for generateSelfShipAppointmentSlots
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    inbound_plan_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("inboundPlanId", "inbound_plan_id"),
            serialization_alias="inboundPlanId",
            description="[PATH] Identifier of an inbound plan.",
        ),
    ]

    shipment_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("shipmentId", "shipment_id"),
            serialization_alias="shipmentId",
            description="[PATH] Identifier of a shipment. A shipment contains the boxes and units being inbounded.",
        ),
    ]

    body: Annotated[
        "GenerateSelfShipAppointmentSlotsRequestBody",
        BodyParam(),
        Field(
            ...,
            description="[BODY] The body of the request to `generateSelfShipAppointmentSlots`.",
        ),
    ]


"""
GenerateSelfShipAppointmentSlotsResponse

The `generateSelfShipAppointmentSlots` response.
"""


class GenerateSelfShipAppointmentSlotsResponse(SpApiBaseModel):
    """The `generateSelfShipAppointmentSlots` response."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    operation_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("operationId", "operation_id"),
            serialization_alias="operationId",
            description="UUID for the given operation.",
        ),
    ]


"""
GenerateShipmentContentUpdatePreviewsRequestBody

The `GenerateShipmentContentUpdatePreviews` request.
"""


class GenerateShipmentContentUpdatePreviewsRequestBody(SpApiBaseModel):
    """The `GenerateShipmentContentUpdatePreviews` request."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    boxes: Annotated[
        List["BoxUpdateInput"],
        Field(
            ...,
            description="A list of boxes that will be present in the shipment after the update.",
        ),
    ]

    items: Annotated[
        List["ItemInput"],
        Field(
            ...,
            description="A list of all items that will be present in the shipment after the update.",
        ),
    ]


"""
GenerateShipmentContentUpdatePreviewsRequest

Request parameters for generateShipmentContentUpdatePreviews
"""


class GenerateShipmentContentUpdatePreviewsRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for generateShipmentContentUpdatePreviews
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    inbound_plan_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("inboundPlanId", "inbound_plan_id"),
            serialization_alias="inboundPlanId",
            description="[PATH] Identifier of an inbound plan.",
        ),
    ]

    shipment_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("shipmentId", "shipment_id"),
            serialization_alias="shipmentId",
            description="[PATH] Identifier of a shipment. A shipment contains the boxes and units being inbounded.",
        ),
    ]

    body: Annotated[
        "GenerateShipmentContentUpdatePreviewsRequestBody",
        BodyParam(),
        Field(
            ...,
            description="[BODY] The body of the request to `generateShipmentContentUpdatePreviews`.",
        ),
    ]


"""
GenerateShipmentContentUpdatePreviewsResponse

The `GenerateShipmentContentUpdatePreviews` response.
"""


class GenerateShipmentContentUpdatePreviewsResponse(SpApiBaseModel):
    """The `GenerateShipmentContentUpdatePreviews` response."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    operation_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("operationId", "operation_id"),
            serialization_alias="operationId",
            description="UUID for the given operation.",
        ),
    ]


Stackability = str
"""Indicates whether pallets will be stacked when carrier arrives for pick-up."""


"""
PalletInput

Contains input information about a pallet to be used in the inbound plan.
"""


class PalletInput(SpApiBaseModel):
    """Contains input information about a pallet to be used in the inbound plan."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    dimensions: Annotated[
        Optional["Dimensions"],
        Field(
            None,
        ),
    ]

    quantity: Annotated[
        int,
        Field(
            ...,
            description="The number of containers where all other properties like weight or dimensions are identical.",
        ),
    ]

    stackability: Annotated[
        Optional["Stackability"],
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


"""
WindowInput

Contains only a starting DateTime.
"""


class WindowInput(SpApiBaseModel):
    """Contains only a starting DateTime."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    start: Annotated[
        datetime,
        Field(
            ...,
            description="The start date of the window. In [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) datetime format with minute precision. Supports patterns `yyyy-MM-ddTHH:mmZ`, `yyyy-MM-ddTHH:mm:ssZ`, or `yyyy-MM-ddTHH:mm:ss.sssZ`. Note that non-zero second and millisecond components are removed.",
        ),
    ]


"""
ShipmentTransportationConfiguration

Details needed to generate the transportation options.
"""


class ShipmentTransportationConfiguration(SpApiBaseModel):
    """Details needed to generate the transportation options."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    contact_information: Annotated[
        Optional["ContactInformation"],
        Field(
            None,
            validation_alias=AliasChoices("contactInformation", "contact_information"),
            serialization_alias="contactInformation",
        ),
    ]

    freight_information: Annotated[
        Optional["FreightInformation"],
        Field(
            None,
            validation_alias=AliasChoices("freightInformation", "freight_information"),
            serialization_alias="freightInformation",
        ),
    ]

    pallets: Annotated[
        Optional[List["PalletInput"]],
        Field(None, description="List of pallet configuration inputs."),
    ]

    ready_to_ship_window: Annotated[
        "WindowInput",
        Field(
            ...,
            validation_alias=AliasChoices("readyToShipWindow", "ready_to_ship_window"),
            serialization_alias="readyToShipWindow",
            description="The range of dates within which the seller intends to ship their items. This is the pick-up date or 'ready to ship' date, not an estimated delivery date.",
        ),
    ]

    shipment_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("shipmentId", "shipment_id"),
            serialization_alias="shipmentId",
            description="Identifier of a shipment. A shipment contains the boxes and units being inbounded.",
        ),
    ]


"""
GenerateTransportationOptionsRequestBody

The `generateTransportationOptions` request.
"""


class GenerateTransportationOptionsRequestBody(SpApiBaseModel):
    """The `generateTransportationOptions` request."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    placement_option_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("placementOptionId", "placement_option_id"),
            serialization_alias="placementOptionId",
            description="The placement option to generate transportation options for.",
        ),
    ]

    shipment_transportation_configurations: Annotated[
        List["ShipmentTransportationConfiguration"],
        Field(
            ...,
            validation_alias=AliasChoices(
                "shipmentTransportationConfigurations",
                "shipment_transportation_configurations",
            ),
            serialization_alias="shipmentTransportationConfigurations",
            description="List of shipment transportation configurations.",
        ),
    ]


"""
GenerateTransportationOptionsRequest

Request parameters for generateTransportationOptions
"""


class GenerateTransportationOptionsRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for generateTransportationOptions
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    inbound_plan_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("inboundPlanId", "inbound_plan_id"),
            serialization_alias="inboundPlanId",
            description="[PATH] Identifier of an inbound plan.",
        ),
    ]

    body: Annotated[
        "GenerateTransportationOptionsRequestBody",
        BodyParam(),
        Field(
            ...,
            description="[BODY] The body of the request to `generateTransportationOptions`.",
        ),
    ]


"""
GenerateTransportationOptionsResponse

The `generateTransportationOptions` response.
"""


class GenerateTransportationOptionsResponse(SpApiBaseModel):
    """The `generateTransportationOptions` response."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    operation_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("operationId", "operation_id"),
            serialization_alias="operationId",
            description="UUID for the given operation.",
        ),
    ]


"""
GetDeliveryChallanDocumentRequest

Request parameters for getDeliveryChallanDocument
"""


class GetDeliveryChallanDocumentRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getDeliveryChallanDocument
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    inbound_plan_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("inboundPlanId", "inbound_plan_id"),
            serialization_alias="inboundPlanId",
            description="[PATH] Identifier of an inbound plan.",
        ),
    ]

    shipment_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("shipmentId", "shipment_id"),
            serialization_alias="shipmentId",
            description="[PATH] Identifier of a shipment. A shipment contains the boxes and units being inbounded.",
        ),
    ]


"""
GetDeliveryChallanDocumentResponse

The `getDeliveryChallanDocumentResponse` response.
"""


class GetDeliveryChallanDocumentResponse(SpApiBaseModel):
    """The `getDeliveryChallanDocumentResponse` response."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    document_download: Annotated[
        "DocumentDownload",
        Field(
            ...,
            validation_alias=AliasChoices("documentDownload", "document_download"),
            serialization_alias="documentDownload",
        ),
    ]


"""
GetInboundOperationStatusRequest

Request parameters for getInboundOperationStatus
"""


class GetInboundOperationStatusRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getInboundOperationStatus
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    operation_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("operationId", "operation_id"),
            serialization_alias="operationId",
            description="[PATH] Identifier of an asynchronous operation.",
        ),
    ]


"""
GetInboundPlanRequest

Request parameters for getInboundPlan
"""


class GetInboundPlanRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getInboundPlan
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    inbound_plan_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("inboundPlanId", "inbound_plan_id"),
            serialization_alias="inboundPlanId",
            description="[PATH] Identifier of an inbound plan.",
        ),
    ]


"""
GetSelfShipAppointmentSlotsRequest

Request parameters for getSelfShipAppointmentSlots
"""


class GetSelfShipAppointmentSlotsRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getSelfShipAppointmentSlots
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    inbound_plan_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("inboundPlanId", "inbound_plan_id"),
            serialization_alias="inboundPlanId",
            description="[PATH] Identifier of an inbound plan.",
        ),
    ]

    shipment_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("shipmentId", "shipment_id"),
            serialization_alias="shipmentId",
            description="[PATH] Identifier of a shipment. A shipment contains the boxes and units being inbounded.",
        ),
    ]

    page_size: Annotated[
        Optional[int],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("pageSize", "page_size"),
            serialization_alias="pageSize",
            description="[QUERY] The number of self ship appointment slots to return in the response matching the given query.",
        ),
    ]

    pagination_token: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("paginationToken", "pagination_token"),
            serialization_alias="paginationToken",
            description="[QUERY] A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result.",
        ),
    ]


"""
Pagination

Contains tokens to fetch from a certain page.
"""


class Pagination(SpApiBaseModel):
    """Contains tokens to fetch from a certain page."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    next_token: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("nextToken", "next_token"),
            serialization_alias="nextToken",
            description="When present, pass this string token in the next request to return the next response page.",
        ),
    ]


"""
SelfShipAppointmentSlotsAvailability

The self ship appointment time slots availability and an expiration date for which the slots can be scheduled.
"""


class SelfShipAppointmentSlotsAvailability(SpApiBaseModel):
    """The self ship appointment time slots availability and an expiration date for which the slots can be scheduled."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    expires_at: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices("expiresAt", "expires_at"),
            serialization_alias="expiresAt",
            description="The time at which the self ship appointment slot expires. In [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) datetime format.",
        ),
    ]

    slots: Annotated[
        Optional[List["AppointmentSlot"]],
        Field(None, description="A list of appointment slots."),
    ]


"""
GetSelfShipAppointmentSlotsResponse

The `getSelfShipAppointmentSlots` response.
"""


class GetSelfShipAppointmentSlotsResponse(SpApiBaseModel):
    """The `getSelfShipAppointmentSlots` response."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    pagination: Annotated[
        Optional["Pagination"],
        Field(
            None,
        ),
    ]

    self_ship_appointment_slots_availability: Annotated[
        "SelfShipAppointmentSlotsAvailability",
        Field(
            ...,
            validation_alias=AliasChoices(
                "selfShipAppointmentSlotsAvailability",
                "self_ship_appointment_slots_availability",
            ),
            serialization_alias="selfShipAppointmentSlotsAvailability",
        ),
    ]


"""
GetShipmentContentUpdatePreviewRequest

Request parameters for getShipmentContentUpdatePreview
"""


class GetShipmentContentUpdatePreviewRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getShipmentContentUpdatePreview
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    inbound_plan_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("inboundPlanId", "inbound_plan_id"),
            serialization_alias="inboundPlanId",
            description="[PATH] Identifier of an inbound plan.",
        ),
    ]

    shipment_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("shipmentId", "shipment_id"),
            serialization_alias="shipmentId",
            description="[PATH] Identifier of a shipment. A shipment contains the boxes and units being inbounded.",
        ),
    ]

    content_update_preview_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices(
                "contentUpdatePreviewId", "content_update_preview_id"
            ),
            serialization_alias="contentUpdatePreviewId",
            description="[PATH] Identifier of a content update preview.",
        ),
    ]


"""
GetShipmentRequest

Request parameters for getShipment
"""


class GetShipmentRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getShipment
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    inbound_plan_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("inboundPlanId", "inbound_plan_id"),
            serialization_alias="inboundPlanId",
            description="[PATH] Identifier of an inbound plan.",
        ),
    ]

    shipment_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("shipmentId", "shipment_id"),
            serialization_alias="shipmentId",
            description="[PATH] Identifier of a shipment. A shipment contains the boxes and units being inbounded.",
        ),
    ]


"""
OperationProblem

A problem with additional properties persisted to an operation.
"""


class OperationProblem(SpApiBaseModel):
    """A problem with additional properties persisted to an operation."""

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

    details: Annotated[
        Optional[str],
        Field(
            None,
            description="Additional details that can help the caller understand or fix the issue.",
        ),
    ]

    message: Annotated[
        str, Field(..., description="A message that describes the error condition.")
    ]

    severity: Annotated[
        str,
        Field(
            ...,
            description="The severity of the problem. Possible values: `WARNING`, `ERROR`.",
        ),
    ]


OperationStatus = str
"""The status of an operation."""


"""
InboundOperationStatus

GetInboundOperationStatus response.
"""


class InboundOperationStatus(SpApiBaseModel):
    """GetInboundOperationStatus response."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    operation: Annotated[
        str,
        Field(
            ..., description="The name of the operation in the asynchronous API call."
        ),
    ]

    operation_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("operationId", "operation_id"),
            serialization_alias="operationId",
            description="The operation ID returned by the asynchronous API call.",
        ),
    ]

    operation_problems: Annotated[
        List["OperationProblem"],
        Field(
            ...,
            validation_alias=AliasChoices("operationProblems", "operation_problems"),
            serialization_alias="operationProblems",
            description="The problems in the processing of the asynchronous operation.",
        ),
    ]

    operation_status: Annotated[
        "OperationStatus",
        Field(
            ...,
            validation_alias=AliasChoices("operationStatus", "operation_status"),
            serialization_alias="operationStatus",
        ),
    ]


"""
PackingOptionSummary

Summary information about a packing option.
"""


class PackingOptionSummary(SpApiBaseModel):
    """Summary information about a packing option."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    packing_option_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("packingOptionId", "packing_option_id"),
            serialization_alias="packingOptionId",
            description="Identifier of a packing option.",
        ),
    ]

    status: Annotated[
        str,
        Field(
            ...,
            description="The status of a packing option. Possible values: 'OFFERED', 'ACCEPTED', 'EXPIRED'.",
        ),
    ]


"""
PlacementOptionSummary

Summary information about a placement option.
"""


class PlacementOptionSummary(SpApiBaseModel):
    """Summary information about a placement option."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    placement_option_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("placementOptionId", "placement_option_id"),
            serialization_alias="placementOptionId",
            description="The identifier of a placement option. A placement option represents the shipment splits and destinations of SKUs.",
        ),
    ]

    status: Annotated[
        str,
        Field(
            ...,
            description="The status of a placement option. Possible values: `OFFERED`, `ACCEPTED`.",
        ),
    ]


"""
ShipmentSummary

Summary information about a shipment.
"""


class ShipmentSummary(SpApiBaseModel):
    """Summary information about a shipment."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    shipment_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("shipmentId", "shipment_id"),
            serialization_alias="shipmentId",
            description="Identifier of a shipment. A shipment contains the boxes and units being inbounded.",
        ),
    ]

    status: Annotated[
        str,
        Field(
            ...,
            description="The status of a shipment. The state of the shipment will typically start as `UNCONFIRMED`, then transition to `WORKING` after a placement option has been confirmed, and then to `READY_TO_SHIP` once labels are generated. Possible values: `ABANDONED`, `CANCELLED`, `CHECKED_IN`, `CLOSED`, `DELETED`, `DELIVERED`, `IN_TRANSIT`, `MIXED`, `READY_TO_SHIP`, `RECEIVING`, `SHIPPED`, `UNCONFIRMED`, `WORKING`",
        ),
    ]


"""
InboundPlan

Inbound plan containing details of the inbound workflow.
"""


class InboundPlan(SpApiBaseModel):
    """Inbound plan containing details of the inbound workflow."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    created_at: Annotated[
        datetime,
        Field(
            ...,
            validation_alias=AliasChoices("createdAt", "created_at"),
            serialization_alias="createdAt",
            description="The time at which the inbound plan was created. In [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) datetime with pattern `yyyy-MM-ddTHH:mm:ssZ`.",
        ),
    ]

    inbound_plan_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("inboundPlanId", "inbound_plan_id"),
            serialization_alias="inboundPlanId",
            description="Identifier of an inbound plan.",
        ),
    ]

    last_updated_at: Annotated[
        datetime,
        Field(
            ...,
            validation_alias=AliasChoices("lastUpdatedAt", "last_updated_at"),
            serialization_alias="lastUpdatedAt",
            description="The time at which the inbound plan was last updated. In [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) datetime format with pattern `yyyy-MM-ddTHH:mm:ssZ`.",
        ),
    ]

    marketplace_ids: Annotated[
        Optional[List["str"]],
        Field(
            None,
            validation_alias=AliasChoices("marketplaceIds", "marketplace_ids"),
            serialization_alias="marketplaceIds",
            description="A list of marketplace IDs.",
        ),
    ]

    name: Annotated[
        str, Field(..., description="Human-readable name of the inbound plan.")
    ]

    packing_options: Annotated[
        Optional[List["PackingOptionSummary"]],
        Field(
            None,
            validation_alias=AliasChoices("packingOptions", "packing_options"),
            serialization_alias="packingOptions",
            description="Packing options for the inbound plan. This property will be populated when it has been generated via the corresponding operation. If there is a chosen placement option, only packing options for that placement option will be returned. If there are confirmed shipments, only packing options for those shipments will be returned. Query the packing option for more details.",
        ),
    ]

    placement_options: Annotated[
        Optional[List["PlacementOptionSummary"]],
        Field(
            None,
            validation_alias=AliasChoices("placementOptions", "placement_options"),
            serialization_alias="placementOptions",
            description="Placement options for the inbound plan. This property will be populated when it has been generated via the corresponding operation. If there is a chosen placement option, that will be the only returned option. Query the placement option for more details.",
        ),
    ]

    shipments: Annotated[
        Optional[List["ShipmentSummary"]],
        Field(
            None,
            description="A list of shipment IDs for the inbound plan. This property is populated when it has been generated with the `confirmPlacementOptions` operation. Only shipments from the chosen placement option are returned. Query the shipment for more details.",
        ),
    ]

    source_address: Annotated[
        "Address",
        Field(
            ...,
            validation_alias=AliasChoices("sourceAddress", "source_address"),
            serialization_alias="sourceAddress",
        ),
    ]

    status: Annotated[
        str,
        Field(
            ...,
            description="Current status of the inbound plan. Possible values: `ACTIVE`, `VOIDED`, `SHIPPED`, `ERRORED`.",
        ),
    ]


"""
InboundPlanSummary

A light-weight inbound plan.
"""


class InboundPlanSummary(SpApiBaseModel):
    """A light-weight inbound plan."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    created_at: Annotated[
        datetime,
        Field(
            ...,
            validation_alias=AliasChoices("createdAt", "created_at"),
            serialization_alias="createdAt",
            description="The time at which the inbound plan was created. In [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) datetime format with pattern `yyyy-MM-ddTHH:mm:ssZ`.",
        ),
    ]

    inbound_plan_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("inboundPlanId", "inbound_plan_id"),
            serialization_alias="inboundPlanId",
            description="Identifier of an inbound plan.",
        ),
    ]

    last_updated_at: Annotated[
        datetime,
        Field(
            ...,
            validation_alias=AliasChoices("lastUpdatedAt", "last_updated_at"),
            serialization_alias="lastUpdatedAt",
            description="The time at which the inbound plan was last updated. In [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) datetime format with pattern `yyyy-MM-ddTHH:mm:ssZ`.",
        ),
    ]

    marketplace_ids: Annotated[
        Optional[List["str"]],
        Field(
            None,
            validation_alias=AliasChoices("marketplaceIds", "marketplace_ids"),
            serialization_alias="marketplaceIds",
            description="A list of marketplace IDs.",
        ),
    ]

    name: Annotated[
        str, Field(..., description="Human-readable name of the inbound plan.")
    ]

    source_address: Annotated[
        "Address",
        Field(
            ...,
            validation_alias=AliasChoices("sourceAddress", "source_address"),
            serialization_alias="sourceAddress",
        ),
    ]

    status: Annotated[
        str,
        Field(
            ...,
            description="The current status of the inbound plan. Possible values: `ACTIVE`, `VOIDED`, `SHIPPED`, `ERRORED`.",
        ),
    ]


"""
Incentive

Contains details about cost related modifications to the placement cost.
"""


class Incentive(SpApiBaseModel):
    """Contains details about cost related modifications to the placement cost."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    description: Annotated[str, Field(..., description="Description of the incentive.")]

    target: Annotated[
        str,
        Field(
            ...,
            description="Target of the incentive. Possible values: 'Placement Services', 'Fulfillment Fee Discount'.",
        ),
    ]

    type: Annotated[
        str,
        Field(
            ..., description="Type of incentive. Possible values: `FEE`, `DISCOUNT`."
        ),
    ]

    value: Annotated[
        "Currency",
        Field(
            ...,
        ),
    ]


"""
ListDeliveryWindowOptionsRequest

Request parameters for listDeliveryWindowOptions
"""


class ListDeliveryWindowOptionsRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for listDeliveryWindowOptions
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    inbound_plan_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("inboundPlanId", "inbound_plan_id"),
            serialization_alias="inboundPlanId",
            description="[PATH] Identifier of an inbound plan.",
        ),
    ]

    shipment_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("shipmentId", "shipment_id"),
            serialization_alias="shipmentId",
            description="[PATH] The shipment to get delivery window options for.",
        ),
    ]

    page_size: Annotated[
        Optional[int],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("pageSize", "page_size"),
            serialization_alias="pageSize",
            description="[QUERY] The number of delivery window options to return in the response matching the given query.",
        ),
    ]

    pagination_token: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("paginationToken", "pagination_token"),
            serialization_alias="paginationToken",
            description="[QUERY] A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result.",
        ),
    ]


"""
ListDeliveryWindowOptionsResponse

The `listDeliveryWindowOptions` response.
"""


class ListDeliveryWindowOptionsResponse(SpApiBaseModel):
    """The `listDeliveryWindowOptions` response."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    delivery_window_options: Annotated[
        List["DeliveryWindowOption"],
        Field(
            ...,
            validation_alias=AliasChoices(
                "deliveryWindowOptions", "delivery_window_options"
            ),
            serialization_alias="deliveryWindowOptions",
            description="Delivery window options generated for the placement option.",
        ),
    ]

    pagination: Annotated[
        Optional["Pagination"],
        Field(
            None,
        ),
    ]


"""
ListInboundPlanBoxesRequest

Request parameters for listInboundPlanBoxes
"""


class ListInboundPlanBoxesRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for listInboundPlanBoxes
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    inbound_plan_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("inboundPlanId", "inbound_plan_id"),
            serialization_alias="inboundPlanId",
            description="[PATH] Identifier of an inbound plan.",
        ),
    ]

    page_size: Annotated[
        Optional[int],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("pageSize", "page_size"),
            serialization_alias="pageSize",
            description="[QUERY] The number of boxes to return in the response matching the given query.",
        ),
    ]

    pagination_token: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("paginationToken", "pagination_token"),
            serialization_alias="paginationToken",
            description="[QUERY] A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result.",
        ),
    ]


"""
ListInboundPlanBoxesResponse

The `listInboundPlanBoxes` response.
"""


class ListInboundPlanBoxesResponse(SpApiBaseModel):
    """The `listInboundPlanBoxes` response."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    boxes: Annotated[
        List["Box"], Field(..., description="A list of boxes in an inbound plan.")
    ]

    pagination: Annotated[
        Optional["Pagination"],
        Field(
            None,
        ),
    ]


"""
ListInboundPlanItemsRequest

Request parameters for listInboundPlanItems
"""


class ListInboundPlanItemsRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for listInboundPlanItems
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    inbound_plan_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("inboundPlanId", "inbound_plan_id"),
            serialization_alias="inboundPlanId",
            description="[PATH] Identifier of an inbound plan.",
        ),
    ]

    page_size: Annotated[
        Optional[int],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("pageSize", "page_size"),
            serialization_alias="pageSize",
            description="[QUERY] The number of items to return in the response matching the given query.",
        ),
    ]

    pagination_token: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("paginationToken", "pagination_token"),
            serialization_alias="paginationToken",
            description="[QUERY] A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result.",
        ),
    ]


"""
ListInboundPlanItemsResponse

The `listInboundPlanItems` response.
"""


class ListInboundPlanItemsResponse(SpApiBaseModel):
    """The `listInboundPlanItems` response."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    items: Annotated[
        List["Item"], Field(..., description="The items in an inbound plan.")
    ]

    pagination: Annotated[
        Optional["Pagination"],
        Field(
            None,
        ),
    ]


"""
ListInboundPlanPalletsRequest

Request parameters for listInboundPlanPallets
"""


class ListInboundPlanPalletsRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for listInboundPlanPallets
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    inbound_plan_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("inboundPlanId", "inbound_plan_id"),
            serialization_alias="inboundPlanId",
            description="[PATH] Identifier of an inbound plan.",
        ),
    ]

    page_size: Annotated[
        Optional[int],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("pageSize", "page_size"),
            serialization_alias="pageSize",
            description="[QUERY] The number of pallets to return in the response matching the given query.",
        ),
    ]

    pagination_token: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("paginationToken", "pagination_token"),
            serialization_alias="paginationToken",
            description="[QUERY] A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result.",
        ),
    ]


"""
Pallet

Contains information about a pallet that is used in the inbound plan. The pallet is a container that holds multiple items or boxes.
"""


class Pallet(SpApiBaseModel):
    """Contains information about a pallet that is used in the inbound plan. The pallet is a container that holds multiple items or boxes."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    dimensions: Annotated[
        Optional["Dimensions"],
        Field(
            None,
        ),
    ]

    package_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("packageId", "package_id"),
            serialization_alias="packageId",
            description="Primary key to uniquely identify a Package (Box or Pallet).",
        ),
    ]

    quantity: Annotated[
        Optional[int],
        Field(
            None,
            description="The number of containers where all other properties like weight or dimensions are identical.",
        ),
    ]

    stackability: Annotated[
        Optional["Stackability"],
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


"""
ListInboundPlanPalletsResponse

The `listInboundPlanPallets` response.
"""


class ListInboundPlanPalletsResponse(SpApiBaseModel):
    """The `listInboundPlanPallets` response."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    pagination: Annotated[
        Optional["Pagination"],
        Field(
            None,
        ),
    ]

    pallets: Annotated[
        List["Pallet"], Field(..., description="The pallets in an inbound plan.")
    ]


# Enum definitions
class StatusEnum(str, Enum):
    """Enum for status"""

    ACTIVE = "ACTIVE"  # An inbound plan that is being worked on.
    VOIDED = "VOIDED"  # An inbound plan with all shipment cancelled and can no longer be modified.
    SHIPPED = "SHIPPED"  # A completed inbound plan. Only minor modifications can be made at this time.


class SortByEnum(str, Enum):
    """Enum for sortBy"""

    LAST_UPDATED_TIME = "LAST_UPDATED_TIME"  # Last updated time of the inbound plan.
    CREATION_TIME = "CREATION_TIME"  # Inbound plan creation time.


class SortOrderEnum(str, Enum):
    """Enum for sortOrder"""

    ASC = "ASC"  # Ascending order.
    DESC = "DESC"  # Descending order.


"""
ListInboundPlansRequest

Request parameters for listInboundPlans
"""


class ListInboundPlansRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for listInboundPlans
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    page_size: Annotated[
        Optional[int],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("pageSize", "page_size"),
            serialization_alias="pageSize",
            description="[QUERY] The number of inbound plans to return in the response matching the given query.",
        ),
    ]

    pagination_token: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("paginationToken", "pagination_token"),
            serialization_alias="paginationToken",
            description="[QUERY] A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result.",
        ),
    ]

    status: Annotated[
        Optional[StatusEnum],
        QueryParam(),
        Field(None, description="[QUERY] The status of an inbound plan."),
    ]

    sort_by: Annotated[
        Optional[SortByEnum],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("sortBy", "sort_by"),
            serialization_alias="sortBy",
            description="[QUERY] Sort by field.",
        ),
    ]

    sort_order: Annotated[
        Optional[SortOrderEnum],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("sortOrder", "sort_order"),
            serialization_alias="sortOrder",
            description="[QUERY] The sort order.",
        ),
    ]


"""
ListInboundPlansResponse

The `listInboundPlans` response.
"""


class ListInboundPlansResponse(SpApiBaseModel):
    """The `listInboundPlans` response."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    inbound_plans: Annotated[
        Optional[List["InboundPlanSummary"]],
        Field(
            None,
            validation_alias=AliasChoices("inboundPlans", "inbound_plans"),
            serialization_alias="inboundPlans",
            description="A list of inbound plans with minimal information.",
        ),
    ]

    pagination: Annotated[
        Optional["Pagination"],
        Field(
            None,
        ),
    ]


"""
ListItemComplianceDetailsRequest

Request parameters for listItemComplianceDetails
"""


class ListItemComplianceDetailsRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for listItemComplianceDetails
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    mskus: Annotated[
        List["str"],
        QueryParam(),
        Field(
            ...,
            description="[QUERY] A list of merchant SKUs, a merchant-supplied identifier of a specific SKU.",
        ),
    ]

    marketplace_id: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="[QUERY] The Marketplace ID. For a list of possible values, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).",
        ),
    ]


"""
ListItemComplianceDetailsResponse

The `listItemComplianceDetails` response.
"""


class ListItemComplianceDetailsResponse(SpApiBaseModel):
    """The `listItemComplianceDetails` response."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    compliance_details: Annotated[
        Optional[List["ComplianceDetail"]],
        Field(
            None,
            validation_alias=AliasChoices("complianceDetails", "compliance_details"),
            serialization_alias="complianceDetails",
            description="List of compliance details.",
        ),
    ]


"""
ListPackingGroupBoxesRequest

Request parameters for listPackingGroupBoxes
"""


class ListPackingGroupBoxesRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for listPackingGroupBoxes
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    inbound_plan_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("inboundPlanId", "inbound_plan_id"),
            serialization_alias="inboundPlanId",
            description="[PATH] Identifier of an inbound plan.",
        ),
    ]

    packing_group_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("packingGroupId", "packing_group_id"),
            serialization_alias="packingGroupId",
            description="[PATH] Identifier of a packing group.",
        ),
    ]

    page_size: Annotated[
        Optional[int],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("pageSize", "page_size"),
            serialization_alias="pageSize",
            description="[QUERY] The number of packing group boxes to return in the response matching the given query.",
        ),
    ]

    pagination_token: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("paginationToken", "pagination_token"),
            serialization_alias="paginationToken",
            description="[QUERY] A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result.",
        ),
    ]


"""
ListPackingGroupBoxesResponse

The `listPackingGroupBoxes` response.
"""


class ListPackingGroupBoxesResponse(SpApiBaseModel):
    """The `listPackingGroupBoxes` response."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    boxes: Annotated[
        List["Box"],
        Field(
            ...,
            description="Provides the information about the list of boxes in the packing group.",
        ),
    ]

    pagination: Annotated[
        Optional["Pagination"],
        Field(
            None,
        ),
    ]


"""
ListPackingGroupItemsRequest

Request parameters for listPackingGroupItems
"""


class ListPackingGroupItemsRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for listPackingGroupItems
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    inbound_plan_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("inboundPlanId", "inbound_plan_id"),
            serialization_alias="inboundPlanId",
            description="[PATH] Identifier of an inbound plan.",
        ),
    ]

    packing_group_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("packingGroupId", "packing_group_id"),
            serialization_alias="packingGroupId",
            description="[PATH] Identifier of a packing group.",
        ),
    ]

    page_size: Annotated[
        Optional[int],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("pageSize", "page_size"),
            serialization_alias="pageSize",
            description="[QUERY] The number of packing group items to return in the response matching the given query.",
        ),
    ]

    pagination_token: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("paginationToken", "pagination_token"),
            serialization_alias="paginationToken",
            description="[QUERY] A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result.",
        ),
    ]


"""
ListPackingGroupItemsResponse

The `listPackingGroupItems` response.
"""


class ListPackingGroupItemsResponse(SpApiBaseModel):
    """The `listPackingGroupItems` response."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    items: Annotated[
        List["Item"],
        Field(
            ...,
            description="Provides the information about the list of items in the packing group.",
        ),
    ]

    pagination: Annotated[
        Optional["Pagination"],
        Field(
            None,
        ),
    ]


"""
ListPackingOptionsRequest

Request parameters for listPackingOptions
"""


class ListPackingOptionsRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for listPackingOptions
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    inbound_plan_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("inboundPlanId", "inbound_plan_id"),
            serialization_alias="inboundPlanId",
            description="[PATH] Identifier of an inbound plan.",
        ),
    ]

    page_size: Annotated[
        Optional[int],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("pageSize", "page_size"),
            serialization_alias="pageSize",
            description="[QUERY] The number of packing options to return in the response matching the given query.",
        ),
    ]

    pagination_token: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("paginationToken", "pagination_token"),
            serialization_alias="paginationToken",
            description="[QUERY] A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result.",
        ),
    ]


"""
ShippingRequirements

The possible shipping modes for the packing option for a given shipping solution or program. Available solutions are Amazon-Partnered Carrier and Use Your Own Carrier. Available modes are ground small parcel, freight less-than-truckload (LTL), freight full-truckload (FTL) palletized, freight FTL non-palletized, ocean less-than-container-load (LCL), ocean full-container load (FCL), air small parcel, and air small parcel express.
"""


class ShippingRequirements(SpApiBaseModel):
    """The possible shipping modes for the packing option for a given shipping solution or program. Available solutions are Amazon-Partnered Carrier and Use Your Own Carrier. Available modes are ground small parcel, freight less-than-truckload (LTL), freight full-truckload (FTL) palletized, freight FTL non-palletized, ocean less-than-container-load (LCL), ocean full-container load (FCL), air small parcel, and air small parcel express."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    modes: Annotated[
        List["str"],
        Field(..., description="Available shipment modes for this shipping program."),
    ]

    solution: Annotated[
        str,
        Field(
            ...,
            description="Shipping program for the option. Can be: `AMAZON_PARTNERED_CARRIER`, `USE_YOUR_OWN_CARRIER`.",
        ),
    ]


"""
PackingConfiguration

A way to configure this packing option. Some box content information sources might not be allowed. Non-standard minimum and maximum box weights might be enforced.
"""


class PackingConfiguration(SpApiBaseModel):
    """A way to configure this packing option. Some box content information sources might not be allowed. Non-standard minimum and maximum box weights might be enforced."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    box_packing_methods: Annotated[
        Optional[List["BoxContentInformationSource"]],
        Field(
            None,
            validation_alias=AliasChoices("boxPackingMethods", "box_packing_methods"),
            serialization_alias="boxPackingMethods",
            description="The box content information sources that are allowed.",
        ),
    ]

    box_requirements: Annotated[
        Optional["BoxRequirements"],
        Field(
            None,
            validation_alias=AliasChoices("boxRequirements", "box_requirements"),
            serialization_alias="boxRequirements",
        ),
    ]

    shipping_requirements: Annotated[
        Optional[List["ShippingRequirements"]],
        Field(
            None,
            validation_alias=AliasChoices(
                "shippingRequirements", "shipping_requirements"
            ),
            serialization_alias="shippingRequirements",
            description="A list of supported shipping requirements for this packing configuration.",
        ),
    ]


"""
ShippingConfiguration

The shipping configurations supported for the packing option. Available modes are ground small parcel, freight less-than-truckload (LTL), freight full-truckload (FTL) palletized, freight FTL non-palletized, ocean less-than-container-load (LCL), ocean full-container load (FCL), air small parcel, and air small parcel express.
"""


class ShippingConfiguration(SpApiBaseModel):
    """The shipping configurations supported for the packing option. Available modes are ground small parcel, freight less-than-truckload (LTL), freight full-truckload (FTL) palletized, freight FTL non-palletized, ocean less-than-container-load (LCL), ocean full-container load (FCL), air small parcel, and air small parcel express."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    shipping_mode: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("shippingMode", "shipping_mode"),
            serialization_alias="shippingMode",
            description="Mode of shipment transportation that this option will provide. Possible values: `GROUND_SMALL_PARCEL`, `FREIGHT_LTL`, `FREIGHT_FTL_PALLET`, `FREIGHT_FTL_NONPALLET`, `OCEAN_LCL`, `OCEAN_FCL`, `AIR_SMALL_PARCEL`, `AIR_SMALL_PARCEL_EXPRESS`.",
        ),
    ]

    shipping_solution: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("shippingSolution", "shipping_solution"),
            serialization_alias="shippingSolution",
            description="Shipping program for the option. Possible values: `AMAZON_PARTNERED_CARRIER`, `USE_YOUR_OWN_CARRIER`.",
        ),
    ]


"""
PackingOption

A packing option contains a set of pack groups plus additional information about the packing option, such as any discounts or fees if it's selected.
"""


class PackingOption(SpApiBaseModel):
    """A packing option contains a set of pack groups plus additional information about the packing option, such as any discounts or fees if it's selected."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    discounts: Annotated[
        List["Incentive"], Field(..., description="Discount for the offered option.")
    ]

    expiration: Annotated[
        Optional[datetime],
        Field(
            None,
            description="The time at which this packing option is no longer valid. In [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) datetime format with pattern `yyyy-MM-ddTHH:mm:ss.sssZ`.",
        ),
    ]

    fees: Annotated[
        List["Incentive"], Field(..., description="Fee for the offered option.")
    ]

    packing_groups: Annotated[
        List["str"],
        Field(
            ...,
            validation_alias=AliasChoices("packingGroups", "packing_groups"),
            serialization_alias="packingGroups",
            description="Packing group IDs.",
        ),
    ]

    packing_option_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("packingOptionId", "packing_option_id"),
            serialization_alias="packingOptionId",
            description="Identifier of a packing option.",
        ),
    ]

    status: Annotated[
        str,
        Field(
            ...,
            description="The status of the packing option. Possible values: `OFFERED`, `ACCEPTED`, `EXPIRED`.",
        ),
    ]

    supported_configurations: Annotated[
        List["PackingConfiguration"],
        Field(
            ...,
            validation_alias=AliasChoices(
                "supportedConfigurations", "supported_configurations"
            ),
            serialization_alias="supportedConfigurations",
            description="A list of possible configurations for this option.",
        ),
    ]

    supported_shipping_configurations: Annotated[
        List["ShippingConfiguration"],
        Field(
            ...,
            validation_alias=AliasChoices(
                "supportedShippingConfigurations", "supported_shipping_configurations"
            ),
            serialization_alias="supportedShippingConfigurations",
            description="**This field is deprecated**. Use the `shippingRequirements` property under `supportedConfigurations` instead. List of supported shipping modes.",
        ),
    ]


"""
ListPackingOptionsResponse

The `listPlacementOptions` response.
"""


class ListPackingOptionsResponse(SpApiBaseModel):
    """The `listPlacementOptions` response."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    packing_options: Annotated[
        List["PackingOption"],
        Field(
            ...,
            validation_alias=AliasChoices("packingOptions", "packing_options"),
            serialization_alias="packingOptions",
            description="List of packing options.",
        ),
    ]

    pagination: Annotated[
        Optional["Pagination"],
        Field(
            None,
        ),
    ]


"""
ListPlacementOptionsRequest

Request parameters for listPlacementOptions
"""


class ListPlacementOptionsRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for listPlacementOptions
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    inbound_plan_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("inboundPlanId", "inbound_plan_id"),
            serialization_alias="inboundPlanId",
            description="[PATH] Identifier of an inbound plan.",
        ),
    ]

    page_size: Annotated[
        Optional[int],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("pageSize", "page_size"),
            serialization_alias="pageSize",
            description="[QUERY] The number of placement options to return in the response matching the given query.",
        ),
    ]

    pagination_token: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("paginationToken", "pagination_token"),
            serialization_alias="paginationToken",
            description="[QUERY] A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result.",
        ),
    ]


"""
PlacementOption

Contains information pertaining to the placement of the contents of an inbound plan and the related costs.
"""


class PlacementOption(SpApiBaseModel):
    """Contains information pertaining to the placement of the contents of an inbound plan and the related costs."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    discounts: Annotated[
        List["Incentive"], Field(..., description="Discount for the offered option.")
    ]

    expiration: Annotated[
        Optional[datetime],
        Field(
            None,
            description="The expiration date of the placement option. In [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) datetime format with pattern `yyyy-MM-ddTHH:mm:ss.sssZ`.",
        ),
    ]

    fees: Annotated[
        List["Incentive"], Field(..., description="The fee for the offered option.")
    ]

    placement_option_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("placementOptionId", "placement_option_id"),
            serialization_alias="placementOptionId",
            description="The identifier of a placement option. A placement option represents the shipment splits and destinations of SKUs.",
        ),
    ]

    shipment_ids: Annotated[
        List["str"],
        Field(
            ...,
            validation_alias=AliasChoices("shipmentIds", "shipment_ids"),
            serialization_alias="shipmentIds",
            description="Shipment ids.",
        ),
    ]

    status: Annotated[
        str,
        Field(
            ...,
            description="The status of a placement option. Possible values: `OFFERED`, `ACCEPTED`, `EXPIRED`.",
        ),
    ]


"""
ListPlacementOptionsResponse

The `listPlacementOptions` response.
"""


class ListPlacementOptionsResponse(SpApiBaseModel):
    """The `listPlacementOptions` response."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    pagination: Annotated[
        Optional["Pagination"],
        Field(
            None,
        ),
    ]

    placement_options: Annotated[
        List["PlacementOption"],
        Field(
            ...,
            validation_alias=AliasChoices("placementOptions", "placement_options"),
            serialization_alias="placementOptions",
            description="Placement options generated for the inbound plan.",
        ),
    ]


"""
ListPrepDetailsRequest

Request parameters for listPrepDetails
"""


class ListPrepDetailsRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for listPrepDetails
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
            description="[QUERY] The marketplace ID. For a list of possible values, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).",
        ),
    ]

    mskus: Annotated[
        List["str"],
        QueryParam(),
        Field(
            ...,
            description="[QUERY] A list of merchant SKUs, a merchant-supplied identifier of a specific SKU.",
        ),
    ]


OwnerConstraint = str
"""A constraint that can apply to an individual owner. If no constraint is specified, both `AMAZON` and `SELLER` are acceptable."""


PrepCategory = str
"""The preparation category for shipping an item to Amazon's fulfillment network."""


PrepType = str
"""Preparation instructions for shipping an item to Amazon's fulfillment network. For more information about preparing items for shipment to Amazon's fulfillment network, refer to [Seller Central Help for your marketplace](https://developer-docs.amazon.com/sp-api/docs/seller-central-urls)."""


"""
MskuPrepDetail

An MSKU and its related prep details.
"""


class MskuPrepDetail(SpApiBaseModel):
    """An MSKU and its related prep details."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    all_owners_constraint: Annotated[
        Optional["AllOwnersConstraint"],
        Field(
            None,
            validation_alias=AliasChoices(
                "allOwnersConstraint", "all_owners_constraint"
            ),
            serialization_alias="allOwnersConstraint",
        ),
    ]

    label_owner_constraint: Annotated[
        Optional["OwnerConstraint"],
        Field(
            None,
            validation_alias=AliasChoices(
                "labelOwnerConstraint", "label_owner_constraint"
            ),
            serialization_alias="labelOwnerConstraint",
        ),
    ]

    msku: Annotated[
        str,
        Field(
            ...,
            description="The merchant SKU, a merchant-supplied identifier for a specific SKU.",
        ),
    ]

    prep_category: Annotated[
        "PrepCategory",
        Field(
            ...,
            validation_alias=AliasChoices("prepCategory", "prep_category"),
            serialization_alias="prepCategory",
        ),
    ]

    prep_owner_constraint: Annotated[
        Optional["OwnerConstraint"],
        Field(
            None,
            validation_alias=AliasChoices(
                "prepOwnerConstraint", "prep_owner_constraint"
            ),
            serialization_alias="prepOwnerConstraint",
        ),
    ]

    prep_types: Annotated[
        List["PrepType"],
        Field(
            ...,
            validation_alias=AliasChoices("prepTypes", "prep_types"),
            serialization_alias="prepTypes",
            description="A list of preparation types associated with a preparation category.",
        ),
    ]


"""
ListPrepDetailsResponse

The response to the `listPrepDetails` operation.
"""


class ListPrepDetailsResponse(SpApiBaseModel):
    """The response to the `listPrepDetails` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    msku_prep_details: Annotated[
        List["MskuPrepDetail"],
        Field(
            ...,
            validation_alias=AliasChoices("mskuPrepDetails", "msku_prep_details"),
            serialization_alias="mskuPrepDetails",
            description="A list of MSKUs and related prep details.",
        ),
    ]


"""
ListShipmentBoxesRequest

Request parameters for listShipmentBoxes
"""


class ListShipmentBoxesRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for listShipmentBoxes
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    inbound_plan_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("inboundPlanId", "inbound_plan_id"),
            serialization_alias="inboundPlanId",
            description="[PATH] Identifier of an inbound plan.",
        ),
    ]

    shipment_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("shipmentId", "shipment_id"),
            serialization_alias="shipmentId",
            description="[PATH] Identifier of a shipment. A shipment contains the boxes and units being inbounded.",
        ),
    ]

    page_size: Annotated[
        Optional[int],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("pageSize", "page_size"),
            serialization_alias="pageSize",
            description="[QUERY] The number of boxes to return in the response matching the given query.",
        ),
    ]

    pagination_token: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("paginationToken", "pagination_token"),
            serialization_alias="paginationToken",
            description="[QUERY] A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result.",
        ),
    ]


"""
ListShipmentBoxesResponse

The `listShipmentBoxes` response.
"""


class ListShipmentBoxesResponse(SpApiBaseModel):
    """The `listShipmentBoxes` response."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    boxes: Annotated[
        List["Box"], Field(..., description="A list of boxes in a shipment.")
    ]

    pagination: Annotated[
        Optional["Pagination"],
        Field(
            None,
        ),
    ]


"""
ListShipmentContentUpdatePreviewsRequest

Request parameters for listShipmentContentUpdatePreviews
"""


class ListShipmentContentUpdatePreviewsRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for listShipmentContentUpdatePreviews
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    inbound_plan_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("inboundPlanId", "inbound_plan_id"),
            serialization_alias="inboundPlanId",
            description="[PATH] Identifier of an inbound plan.",
        ),
    ]

    shipment_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("shipmentId", "shipment_id"),
            serialization_alias="shipmentId",
            description="[PATH] Identifier of a shipment. A shipment contains the boxes and units being inbounded.",
        ),
    ]

    page_size: Annotated[
        Optional[int],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("pageSize", "page_size"),
            serialization_alias="pageSize",
            description="[QUERY] The number of content update previews to return.",
        ),
    ]

    pagination_token: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("paginationToken", "pagination_token"),
            serialization_alias="paginationToken",
            description="[QUERY] A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result.",
        ),
    ]


"""
ListShipmentContentUpdatePreviewsResponse

The `ListShipmentContentUpdatePreviews` response.
"""


class ListShipmentContentUpdatePreviewsResponse(SpApiBaseModel):
    """The `ListShipmentContentUpdatePreviews` response."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    content_update_previews: Annotated[
        List["ContentUpdatePreview"],
        Field(
            ...,
            validation_alias=AliasChoices(
                "contentUpdatePreviews", "content_update_previews"
            ),
            serialization_alias="contentUpdatePreviews",
            description="A list of content update previews in a shipment.",
        ),
    ]

    pagination: Annotated[
        Optional["Pagination"],
        Field(
            None,
        ),
    ]


"""
ListShipmentItemsRequest

Request parameters for listShipmentItems
"""


class ListShipmentItemsRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for listShipmentItems
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    inbound_plan_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("inboundPlanId", "inbound_plan_id"),
            serialization_alias="inboundPlanId",
            description="[PATH] Identifier of an inbound plan.",
        ),
    ]

    shipment_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("shipmentId", "shipment_id"),
            serialization_alias="shipmentId",
            description="[PATH] Identifier of a shipment. A shipment contains the boxes and units being inbounded.",
        ),
    ]

    page_size: Annotated[
        Optional[int],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("pageSize", "page_size"),
            serialization_alias="pageSize",
            description="[QUERY] The number of items to return in the response matching the given query.",
        ),
    ]

    pagination_token: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("paginationToken", "pagination_token"),
            serialization_alias="paginationToken",
            description="[QUERY] A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result.",
        ),
    ]


"""
ListShipmentItemsResponse

The `listShipmentItems` response.
"""


class ListShipmentItemsResponse(SpApiBaseModel):
    """The `listShipmentItems` response."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    items: Annotated[List["Item"], Field(..., description="The items in a shipment.")]

    pagination: Annotated[
        Optional["Pagination"],
        Field(
            None,
        ),
    ]


"""
ListShipmentPalletsRequest

Request parameters for listShipmentPallets
"""


class ListShipmentPalletsRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for listShipmentPallets
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    inbound_plan_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("inboundPlanId", "inbound_plan_id"),
            serialization_alias="inboundPlanId",
            description="[PATH] Identifier of an inbound plan.",
        ),
    ]

    shipment_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("shipmentId", "shipment_id"),
            serialization_alias="shipmentId",
            description="[PATH] Identifier of a shipment. A shipment contains the boxes and units being inbounded.",
        ),
    ]

    page_size: Annotated[
        Optional[int],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("pageSize", "page_size"),
            serialization_alias="pageSize",
            description="[QUERY] The number of pallets to return in the response matching the given query.",
        ),
    ]

    pagination_token: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("paginationToken", "pagination_token"),
            serialization_alias="paginationToken",
            description="[QUERY] A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result.",
        ),
    ]


"""
ListShipmentPalletsResponse

The `listShipmentPallets` response.
"""


class ListShipmentPalletsResponse(SpApiBaseModel):
    """The `listShipmentPallets` response."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    pagination: Annotated[
        Optional["Pagination"],
        Field(
            None,
        ),
    ]

    pallets: Annotated[
        List["Pallet"], Field(..., description="The pallets in a shipment.")
    ]


"""
ListTransportationOptionsRequest

Request parameters for listTransportationOptions
"""


class ListTransportationOptionsRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for listTransportationOptions
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    inbound_plan_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("inboundPlanId", "inbound_plan_id"),
            serialization_alias="inboundPlanId",
            description="[PATH] Identifier of an inbound plan.",
        ),
    ]

    page_size: Annotated[
        Optional[int],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("pageSize", "page_size"),
            serialization_alias="pageSize",
            description="[QUERY] The number of transportation options to return in the response matching the given query.",
        ),
    ]

    pagination_token: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("paginationToken", "pagination_token"),
            serialization_alias="paginationToken",
            description="[QUERY] A token to fetch a certain page when there are multiple pages worth of results. The value of this token is fetched from the `pagination` returned in the API response. In the absence of the token value from the query parameter the API returns the first page of the result.",
        ),
    ]

    placement_option_id: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("placementOptionId", "placement_option_id"),
            serialization_alias="placementOptionId",
            description="[QUERY] The placement option to get transportation options for. Either `placementOptionId` or `shipmentId` must be specified.",
        ),
    ]

    shipment_id: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("shipmentId", "shipment_id"),
            serialization_alias="shipmentId",
            description="[QUERY] The shipment to get transportation options for. Either `placementOptionId` or `shipmentId` must be specified.",
        ),
    ]


"""
ListTransportationOptionsResponse

The `listTransportationOptions` response.
"""


class ListTransportationOptionsResponse(SpApiBaseModel):
    """The `listTransportationOptions` response."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    pagination: Annotated[
        Optional["Pagination"],
        Field(
            None,
        ),
    ]

    transportation_options: Annotated[
        List["TransportationOption"],
        Field(
            ...,
            validation_alias=AliasChoices(
                "transportationOptions", "transportation_options"
            ),
            serialization_alias="transportationOptions",
            description="Transportation options generated for the placement option.",
        ),
    ]


"""
LtlTrackingDetail

Contains information related to Less-Than-Truckload (LTL) shipment tracking.
"""


class LtlTrackingDetail(SpApiBaseModel):
    """Contains information related to Less-Than-Truckload (LTL) shipment tracking."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    bill_of_lading_number: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "billOfLadingNumber", "bill_of_lading_number"
            ),
            serialization_alias="billOfLadingNumber",
            description="The number of the carrier shipment acknowledgement document.",
        ),
    ]

    freight_bill_number: Annotated[
        Optional[List["str"]],
        Field(
            None,
            validation_alias=AliasChoices("freightBillNumber", "freight_bill_number"),
            serialization_alias="freightBillNumber",
            description="The number associated with the freight bill.",
        ),
    ]


"""
LtlTrackingDetailInput

Contains input information to update Less-Than-Truckload (LTL) tracking information.
"""


class LtlTrackingDetailInput(SpApiBaseModel):
    """Contains input information to update Less-Than-Truckload (LTL) tracking information."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    bill_of_lading_number: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "billOfLadingNumber", "bill_of_lading_number"
            ),
            serialization_alias="billOfLadingNumber",
            description="The number of the carrier shipment acknowledgement document.",
        ),
    ]

    freight_bill_number: Annotated[
        List["str"],
        Field(
            ...,
            validation_alias=AliasChoices("freightBillNumber", "freight_bill_number"),
            serialization_alias="freightBillNumber",
            description="Number associated with the freight bill.",
        ),
    ]


"""
MskuPrepDetailInput

An MSKU and its related prep details.
"""


class MskuPrepDetailInput(SpApiBaseModel):
    """An MSKU and its related prep details."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    msku: Annotated[
        str,
        Field(
            ...,
            description="The merchant SKU, a merchant-supplied identifier for a specific SKU.",
        ),
    ]

    prep_category: Annotated[
        "PrepCategory",
        Field(
            ...,
            validation_alias=AliasChoices("prepCategory", "prep_category"),
            serialization_alias="prepCategory",
        ),
    ]

    prep_types: Annotated[
        List["PrepType"],
        Field(
            ...,
            validation_alias=AliasChoices("prepTypes", "prep_types"),
            serialization_alias="prepTypes",
            description="A list of preparation types associated with a preparation category.",
        ),
    ]


"""
PackageGroupingInput

Packing information for the inbound plan.
"""


class PackageGroupingInput(SpApiBaseModel):
    """Packing information for the inbound plan."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    boxes: Annotated[
        List["BoxInput"],
        Field(..., description="Box level information being provided."),
    ]

    packing_group_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("packingGroupId", "packing_group_id"),
            serialization_alias="packingGroupId",
            description="The ID of the `packingGroup` that packages are grouped according to. The `PackingGroupId` can only be provided before placement confirmation, and it must belong to the confirmed `PackingOption`. One of `ShipmentId` or `PackingGroupId` must be provided with every request.",
        ),
    ]

    shipment_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("shipmentId", "shipment_id"),
            serialization_alias="shipmentId",
            description="The ID of the shipment that packages are grouped according to. The `ShipmentId` can only be provided after placement confirmation, and the shipment must belong to the confirmed placement option. One of `ShipmentId` or `PackingGroupId` must be provided with every request.",
        ),
    ]


"""
ScheduleSelfShipAppointmentRequestBody

The `scheduleSelfShipAppointment` request.
"""


class ScheduleSelfShipAppointmentRequestBody(SpApiBaseModel):
    """The `scheduleSelfShipAppointment` request."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    reason_comment: Annotated[
        Optional["ReasonComment"],
        Field(
            None,
            validation_alias=AliasChoices("reasonComment", "reason_comment"),
            serialization_alias="reasonComment",
        ),
    ]


"""
ScheduleSelfShipAppointmentRequest

Request parameters for scheduleSelfShipAppointment
"""


class ScheduleSelfShipAppointmentRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for scheduleSelfShipAppointment
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    inbound_plan_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("inboundPlanId", "inbound_plan_id"),
            serialization_alias="inboundPlanId",
            description="[PATH] Identifier of an inbound plan.",
        ),
    ]

    shipment_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("shipmentId", "shipment_id"),
            serialization_alias="shipmentId",
            description="[PATH] Identifier of a shipment. A shipment contains the boxes and units being inbounded.",
        ),
    ]

    slot_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("slotId", "slot_id"),
            serialization_alias="slotId",
            description="[PATH] An identifier to a self-ship appointment slot.",
        ),
    ]

    body: Annotated[
        "ScheduleSelfShipAppointmentRequestBody",
        BodyParam(),
        Field(
            ...,
            description="[BODY] The body of the request to `scheduleSelfShipAppointment`.",
        ),
    ]


"""
SelfShipAppointmentDetails

Appointment details for carrier pickup or fulfillment center appointments.
"""


class SelfShipAppointmentDetails(SpApiBaseModel):
    """Appointment details for carrier pickup or fulfillment center appointments."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    appointment_id: Annotated[
        Optional[float],
        Field(
            None,
            validation_alias=AliasChoices("appointmentId", "appointment_id"),
            serialization_alias="appointmentId",
            description="Identifier for appointment.",
        ),
    ]

    appointment_slot_time: Annotated[
        Optional["AppointmentSlotTime"],
        Field(
            None,
            validation_alias=AliasChoices(
                "appointmentSlotTime", "appointment_slot_time"
            ),
            serialization_alias="appointmentSlotTime",
        ),
    ]

    appointment_status: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("appointmentStatus", "appointment_status"),
            serialization_alias="appointmentStatus",
            description="Status of the appointment.",
        ),
    ]


"""
ScheduleSelfShipAppointmentResponse

The `scheduleSelfShipAppointment` response.
"""


class ScheduleSelfShipAppointmentResponse(SpApiBaseModel):
    """The `scheduleSelfShipAppointment` response."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    self_ship_appointment_details: Annotated[
        "SelfShipAppointmentDetails",
        Field(
            ...,
            validation_alias=AliasChoices(
                "selfShipAppointmentDetails", "self_ship_appointment_details"
            ),
            serialization_alias="selfShipAppointmentDetails",
        ),
    ]


"""
SelectedDeliveryWindow

Selected delivery window attributes.
"""


class SelectedDeliveryWindow(SpApiBaseModel):
    """Selected delivery window attributes."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    availability_type: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("availabilityType", "availability_type"),
            serialization_alias="availabilityType",
            description="Identifies type of Delivery Window Availability. Values: `AVAILABLE`, `CONGESTED`",
        ),
    ]

    delivery_window_option_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices(
                "deliveryWindowOptionId", "delivery_window_option_id"
            ),
            serialization_alias="deliveryWindowOptionId",
            description="Identifier of a delivery window option. A delivery window option represent one option for when a shipment is expected to be delivered.",
        ),
    ]

    editable_until: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices("editableUntil", "editable_until"),
            serialization_alias="editableUntil",
            description="The timestamp at which this Window can no longer be edited.",
        ),
    ]

    end_date: Annotated[
        datetime,
        Field(
            ...,
            validation_alias=AliasChoices("endDate", "end_date"),
            serialization_alias="endDate",
            description="The end timestamp of the window.",
        ),
    ]

    start_date: Annotated[
        datetime,
        Field(
            ...,
            validation_alias=AliasChoices("startDate", "start_date"),
            serialization_alias="startDate",
            description="The start timestamp of the window.",
        ),
    ]


"""
SetPackingInformationRequestBody

The `setPackingInformation` request.
"""


class SetPackingInformationRequestBody(SpApiBaseModel):
    """The `setPackingInformation` request."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    package_groupings: Annotated[
        List["PackageGroupingInput"],
        Field(
            ...,
            validation_alias=AliasChoices("packageGroupings", "package_groupings"),
            serialization_alias="packageGroupings",
            description="List of packing information for the inbound plan.",
        ),
    ]


"""
SetPackingInformationRequest

Request parameters for setPackingInformation
"""


class SetPackingInformationRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for setPackingInformation
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    inbound_plan_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("inboundPlanId", "inbound_plan_id"),
            serialization_alias="inboundPlanId",
            description="[PATH] Identifier of an inbound plan.",
        ),
    ]

    body: Annotated[
        "SetPackingInformationRequestBody",
        BodyParam(),
        Field(
            ...,
            description="[BODY] The body of the request to `setPackingInformation`.",
        ),
    ]


"""
SetPackingInformationResponse

The `setPackingInformation` response.
"""


class SetPackingInformationResponse(SpApiBaseModel):
    """The `setPackingInformation` response."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    operation_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("operationId", "operation_id"),
            serialization_alias="operationId",
            description="UUID for the given operation.",
        ),
    ]


"""
SetPrepDetailsRequestBody

The `setPrepDetails` request.
"""


class SetPrepDetailsRequestBody(SpApiBaseModel):
    """The `setPrepDetails` request."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    marketplace_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="The marketplace ID. For a list of possible values, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).",
        ),
    ]

    msku_prep_details: Annotated[
        List["MskuPrepDetailInput"],
        Field(
            ...,
            validation_alias=AliasChoices("mskuPrepDetails", "msku_prep_details"),
            serialization_alias="mskuPrepDetails",
            description="A list of MSKUs and related prep details.",
        ),
    ]


"""
SetPrepDetailsRequest

Request parameters for setPrepDetails
"""


class SetPrepDetailsRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for setPrepDetails
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    body: Annotated[
        "SetPrepDetailsRequestBody",
        BodyParam(),
        Field(..., description="[BODY] The body of the request to `setPrepDetails`."),
    ]


"""
SetPrepDetailsResponse

The `setPrepDetails` response.
"""


class SetPrepDetailsResponse(SpApiBaseModel):
    """The `setPrepDetails` response."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    operation_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("operationId", "operation_id"),
            serialization_alias="operationId",
            description="UUID for the given operation.",
        ),
    ]


"""
ShipmentDestination

The Amazon fulfillment center address and warehouse ID.
"""


class ShipmentDestination(SpApiBaseModel):
    """The Amazon fulfillment center address and warehouse ID."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    address: Annotated[
        Optional["Address"],
        Field(
            None,
            description="The address the shipment should be sent to. Empty if the destination type is `AMAZON_OPTIMIZED`.",
        ),
    ]

    destination_type: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("destinationType", "destination_type"),
            serialization_alias="destinationType",
            description="The type of destination for this shipment. Possible values: `AMAZON_OPTIMIZED`, `AMAZON_WAREHOUSE`.",
        ),
    ]

    warehouse_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("warehouseId", "warehouse_id"),
            serialization_alias="warehouseId",
            description="The warehouse that the shipment should be sent to. Empty if the destination type is `AMAZON_OPTIMIZED`.",
        ),
    ]


"""
ShipmentSource

Specifies the 'ship from' address for the shipment.
"""


class ShipmentSource(SpApiBaseModel):
    """Specifies the 'ship from' address for the shipment."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    address: Annotated[
        Optional["Address"],
        Field(
            None,
        ),
    ]

    source_type: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("sourceType", "source_type"),
            serialization_alias="sourceType",
            description="The type of source for this shipment. Possible values: `SELLER_FACILITY`.",
        ),
    ]


"""
SpdTrackingItem

Contains information used to track and identify a Small Parcel Delivery (SPD) item.
"""


class SpdTrackingItem(SpApiBaseModel):
    """Contains information used to track and identify a Small Parcel Delivery (SPD) item."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    box_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("boxId", "box_id"),
            serialization_alias="boxId",
            description="The ID provided by Amazon that identifies a given box. This ID is comprised of the external shipment ID (which is generated after transportation has been confirmed) and the index of the box.",
        ),
    ]

    tracking_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("trackingId", "tracking_id"),
            serialization_alias="trackingId",
            description="The tracking ID associated with each box in a non-Amazon partnered Small Parcel Delivery (SPD) shipment.",
        ),
    ]

    tracking_number_validation_status: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "trackingNumberValidationStatus", "tracking_number_validation_status"
            ),
            serialization_alias="trackingNumberValidationStatus",
            description="Whether or not Amazon has validated the tracking number. If more than 24 hours have passed and the status is not yet 'VALIDATED', please verify the number and update if necessary. Possible values: `VALIDATED`, `NOT_VALIDATED`.",
        ),
    ]


"""
SpdTrackingDetail

Contains information related to Small Parcel Delivery (SPD) shipment tracking.
"""


class SpdTrackingDetail(SpApiBaseModel):
    """Contains information related to Small Parcel Delivery (SPD) shipment tracking."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    spd_tracking_items: Annotated[
        Optional[List["SpdTrackingItem"]],
        Field(
            None,
            validation_alias=AliasChoices("spdTrackingItems", "spd_tracking_items"),
            serialization_alias="spdTrackingItems",
            description="List of Small Parcel Delivery (SPD) tracking items.",
        ),
    ]


"""
TrackingDetails

Tracking information for Less-Than-Truckload (LTL) and Small Parcel Delivery (SPD) shipments.
"""


class TrackingDetails(SpApiBaseModel):
    """Tracking information for Less-Than-Truckload (LTL) and Small Parcel Delivery (SPD) shipments."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    ltl_tracking_detail: Annotated[
        Optional["LtlTrackingDetail"],
        Field(
            None,
            validation_alias=AliasChoices("ltlTrackingDetail", "ltl_tracking_detail"),
            serialization_alias="ltlTrackingDetail",
        ),
    ]

    spd_tracking_detail: Annotated[
        Optional["SpdTrackingDetail"],
        Field(
            None,
            validation_alias=AliasChoices("spdTrackingDetail", "spd_tracking_detail"),
            serialization_alias="spdTrackingDetail",
        ),
    ]


"""
Shipment

Contains information pertaining to a shipment in an inbound plan.
"""


class Shipment(SpApiBaseModel):
    """Contains information pertaining to a shipment in an inbound plan."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    amazon_reference_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("amazonReferenceId", "amazon_reference_id"),
            serialization_alias="amazonReferenceId",
            description="A unique identifier created by Amazon that identifies this Amazon-partnered, Less Than Truckload/Full Truckload (LTL/FTL) shipment.",
        ),
    ]

    contact_information: Annotated[
        Optional["ContactInformation"],
        Field(
            None,
            validation_alias=AliasChoices("contactInformation", "contact_information"),
            serialization_alias="contactInformation",
        ),
    ]

    dates: Annotated[
        Optional["Dates"],
        Field(
            None,
        ),
    ]

    destination: Annotated[
        "ShipmentDestination",
        Field(
            ...,
        ),
    ]

    freight_information: Annotated[
        Optional["FreightInformation"],
        Field(
            None,
            validation_alias=AliasChoices("freightInformation", "freight_information"),
            serialization_alias="freightInformation",
        ),
    ]

    name: Annotated[Optional[str], Field(None, description="The name of the shipment.")]

    placement_option_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("placementOptionId", "placement_option_id"),
            serialization_alias="placementOptionId",
            description="The identifier of a placement option. A placement option represents the shipment splits and destinations of SKUs.",
        ),
    ]

    selected_delivery_window: Annotated[
        Optional["SelectedDeliveryWindow"],
        Field(
            None,
            validation_alias=AliasChoices(
                "selectedDeliveryWindow", "selected_delivery_window"
            ),
            serialization_alias="selectedDeliveryWindow",
        ),
    ]

    selected_transportation_option_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "selectedTransportationOptionId", "selected_transportation_option_id"
            ),
            serialization_alias="selectedTransportationOptionId",
            description="Identifier of a transportation option. A transportation option represent one option for how to send a shipment.",
        ),
    ]

    self_ship_appointment_details: Annotated[
        Optional[List["SelfShipAppointmentDetails"]],
        Field(
            None,
            validation_alias=AliasChoices(
                "selfShipAppointmentDetails", "self_ship_appointment_details"
            ),
            serialization_alias="selfShipAppointmentDetails",
            description="List of self ship appointment details.",
        ),
    ]

    shipment_confirmation_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "shipmentConfirmationId", "shipment_confirmation_id"
            ),
            serialization_alias="shipmentConfirmationId",
            description="The confirmed shipment ID which shows up on labels (for example, `FBA1234ABCD`).",
        ),
    ]

    shipment_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("shipmentId", "shipment_id"),
            serialization_alias="shipmentId",
            description="Identifier of a shipment. A shipment contains the boxes and units being inbounded.",
        ),
    ]

    source: Annotated[
        "ShipmentSource",
        Field(
            ...,
        ),
    ]

    status: Annotated[
        Optional[str],
        Field(
            None,
            description="The status of a shipment. The state of the shipment will typically start as `UNCONFIRMED`, then transition to `WORKING` after a placement option has been confirmed, and then to `READY_TO_SHIP` once labels are generated. Possible values: `ABANDONED`, `CANCELLED`, `CHECKED_IN`, `CLOSED`, `DELETED`, `DELIVERED`, `IN_TRANSIT`, `MIXED`, `READY_TO_SHIP`, `RECEIVING`, `SHIPPED`, `UNCONFIRMED`, `WORKING`",
        ),
    ]

    tracking_details: Annotated[
        Optional["TrackingDetails"],
        Field(
            None,
            validation_alias=AliasChoices("trackingDetails", "tracking_details"),
            serialization_alias="trackingDetails",
        ),
    ]


"""
SpdTrackingItemInput

Small Parcel Delivery (SPD) tracking items input information.
"""


class SpdTrackingItemInput(SpApiBaseModel):
    """Small Parcel Delivery (SPD) tracking items input information."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    box_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("boxId", "box_id"),
            serialization_alias="boxId",
            description="The ID provided by Amazon that identifies a given box. This ID is comprised of the external shipment ID (which is generated after transportation has been confirmed) and the index of the box.",
        ),
    ]

    tracking_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("trackingId", "tracking_id"),
            serialization_alias="trackingId",
            description="The tracking Id associated with each box in a non-Amazon partnered Small Parcel Delivery (SPD) shipment. The seller must provide this information.",
        ),
    ]


"""
SpdTrackingDetailInput

Contains input information to update Small Parcel Delivery (SPD) tracking information.
"""


class SpdTrackingDetailInput(SpApiBaseModel):
    """Contains input information to update Small Parcel Delivery (SPD) tracking information."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    spd_tracking_items: Annotated[
        List["SpdTrackingItemInput"],
        Field(
            ...,
            validation_alias=AliasChoices("spdTrackingItems", "spd_tracking_items"),
            serialization_alias="spdTrackingItems",
            description="List of Small Parcel Delivery (SPD) tracking items input.",
        ),
    ]


"""
TrackingDetailsInput

Tracking information input for Less-Than-Truckload (LTL) and Small Parcel Delivery (SPD) shipments.
"""


class TrackingDetailsInput(SpApiBaseModel):
    """Tracking information input for Less-Than-Truckload (LTL) and Small Parcel Delivery (SPD) shipments."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    ltl_tracking_detail: Annotated[
        Optional["LtlTrackingDetailInput"],
        Field(
            None,
            validation_alias=AliasChoices("ltlTrackingDetail", "ltl_tracking_detail"),
            serialization_alias="ltlTrackingDetail",
        ),
    ]

    spd_tracking_detail: Annotated[
        Optional["SpdTrackingDetailInput"],
        Field(
            None,
            validation_alias=AliasChoices("spdTrackingDetail", "spd_tracking_detail"),
            serialization_alias="spdTrackingDetail",
        ),
    ]


"""
UpdateInboundPlanNameRequestBody

The `updateInboundPlanName` request.
"""


class UpdateInboundPlanNameRequestBody(SpApiBaseModel):
    """The `updateInboundPlanName` request."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    name: Annotated[
        str,
        Field(
            ..., description="A human-readable name to update the inbound plan name to."
        ),
    ]


"""
UpdateInboundPlanNameRequest

Request parameters for updateInboundPlanName
"""


class UpdateInboundPlanNameRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for updateInboundPlanName
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    inbound_plan_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("inboundPlanId", "inbound_plan_id"),
            serialization_alias="inboundPlanId",
            description="[PATH] Identifier of an inbound plan.",
        ),
    ]

    body: Annotated[
        "UpdateInboundPlanNameRequestBody",
        BodyParam(),
        Field(
            ...,
            description="[BODY] The body of the request to `updateInboundPlanName`.",
        ),
    ]


"""
UpdateItemComplianceDetailsRequestBody

The `updateItemComplianceDetails` request.
"""


class UpdateItemComplianceDetailsRequestBody(SpApiBaseModel):
    """The `updateItemComplianceDetails` request."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    msku: Annotated[
        str,
        Field(
            ...,
            description="The merchant SKU, a merchant-supplied identifier for a specific SKU.",
        ),
    ]

    tax_details: Annotated[
        "TaxDetails",
        Field(
            ...,
            validation_alias=AliasChoices("taxDetails", "tax_details"),
            serialization_alias="taxDetails",
        ),
    ]


"""
UpdateItemComplianceDetailsRequest

Request parameters for updateItemComplianceDetails
"""


class UpdateItemComplianceDetailsRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for updateItemComplianceDetails
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
            description="[QUERY] The Marketplace ID. For a list of possible values, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).",
        ),
    ]

    body: Annotated[
        "UpdateItemComplianceDetailsRequestBody",
        BodyParam(),
        Field(
            ...,
            description="[BODY] The body of the request to `updateItemComplianceDetails`.",
        ),
    ]


"""
UpdateItemComplianceDetailsResponse

The `updateItemComplianceDetails` response.
"""


class UpdateItemComplianceDetailsResponse(SpApiBaseModel):
    """The `updateItemComplianceDetails` response."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    operation_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("operationId", "operation_id"),
            serialization_alias="operationId",
            description="UUID for the given operation.",
        ),
    ]


"""
UpdateShipmentNameRequestBody

The `updateShipmentName` request.
"""


class UpdateShipmentNameRequestBody(SpApiBaseModel):
    """The `updateShipmentName` request."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    name: Annotated[
        str,
        Field(..., description="A human-readable name to update the shipment name to."),
    ]


"""
UpdateShipmentNameRequest

Request parameters for updateShipmentName
"""


class UpdateShipmentNameRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for updateShipmentName
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    inbound_plan_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("inboundPlanId", "inbound_plan_id"),
            serialization_alias="inboundPlanId",
            description="[PATH] Identifier of an inbound plan.",
        ),
    ]

    shipment_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("shipmentId", "shipment_id"),
            serialization_alias="shipmentId",
            description="[PATH] Identifier of a shipment. A shipment contains the boxes and units being inbounded.",
        ),
    ]

    body: Annotated[
        "UpdateShipmentNameRequestBody",
        BodyParam(),
        Field(
            ..., description="[BODY] The body of the request to `updateShipmentName`."
        ),
    ]


"""
UpdateShipmentSourceAddressRequestBody

The `UpdateShipmentSourceAddress` request.
"""


class UpdateShipmentSourceAddressRequestBody(SpApiBaseModel):
    """The `UpdateShipmentSourceAddress` request."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    address: Annotated[
        "AddressInput",
        Field(
            ...,
        ),
    ]


"""
UpdateShipmentSourceAddressRequest

Request parameters for updateShipmentSourceAddress
"""


class UpdateShipmentSourceAddressRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for updateShipmentSourceAddress
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    inbound_plan_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("inboundPlanId", "inbound_plan_id"),
            serialization_alias="inboundPlanId",
            description="[PATH] Identifier of an inbound plan.",
        ),
    ]

    shipment_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("shipmentId", "shipment_id"),
            serialization_alias="shipmentId",
            description="[PATH] Identifier of a shipment. A shipment contains the boxes and units being inbounded.",
        ),
    ]

    body: Annotated[
        "UpdateShipmentSourceAddressRequestBody",
        BodyParam(),
        Field(
            ...,
            description="[BODY] The body of the request to `updateShipmentSourceAddress`.",
        ),
    ]


"""
UpdateShipmentSourceAddressResponse

The `UpdateShipmentSourceAddress` response.
"""


class UpdateShipmentSourceAddressResponse(SpApiBaseModel):
    """The `UpdateShipmentSourceAddress` response."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    operation_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("operationId", "operation_id"),
            serialization_alias="operationId",
            description="UUID for the given operation.",
        ),
    ]


"""
UpdateShipmentTrackingDetailsRequestBody

The `updateShipmentTrackingDetails` request.
"""


class UpdateShipmentTrackingDetailsRequestBody(SpApiBaseModel):
    """The `updateShipmentTrackingDetails` request."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    tracking_details: Annotated[
        "TrackingDetailsInput",
        Field(
            ...,
            validation_alias=AliasChoices("trackingDetails", "tracking_details"),
            serialization_alias="trackingDetails",
        ),
    ]


"""
UpdateShipmentTrackingDetailsRequest

Request parameters for updateShipmentTrackingDetails
"""


class UpdateShipmentTrackingDetailsRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for updateShipmentTrackingDetails
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    inbound_plan_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("inboundPlanId", "inbound_plan_id"),
            serialization_alias="inboundPlanId",
            description="[PATH] Identifier of an inbound plan.",
        ),
    ]

    shipment_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("shipmentId", "shipment_id"),
            serialization_alias="shipmentId",
            description="[PATH] Identifier of a shipment. A shipment contains the boxes and units being inbounded.",
        ),
    ]

    body: Annotated[
        "UpdateShipmentTrackingDetailsRequestBody",
        BodyParam(),
        Field(
            ...,
            description="[BODY] The body of the request to `updateShipmentTrackingDetails`.",
        ),
    ]


"""
UpdateShipmentTrackingDetailsResponse

The `updateShipmentTrackingDetails` response.
"""


class UpdateShipmentTrackingDetailsResponse(SpApiBaseModel):
    """The `updateShipmentTrackingDetails` response."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    operation_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("operationId", "operation_id"),
            serialization_alias="operationId",
            description="UUID for the given operation.",
        ),
    ]


# Rebuild models to resolve forward references
Address.model_rebuild()
AddressInput.model_rebuild()
AppointmentSlot.model_rebuild()
AppointmentSlotTime.model_rebuild()
Box.model_rebuild()
BoxInput.model_rebuild()
BoxRequirements.model_rebuild()
BoxUpdateInput.model_rebuild()
CancelInboundPlanResponse.model_rebuild()
CancelSelfShipAppointmentRequestBody.model_rebuild()
CancelSelfShipAppointmentResponse.model_rebuild()
Carrier.model_rebuild()
CarrierAppointment.model_rebuild()
ComplianceDetail.model_rebuild()
ConfirmDeliveryWindowOptionsResponse.model_rebuild()
ConfirmPackingOptionResponse.model_rebuild()
ConfirmPlacementOptionResponse.model_rebuild()
ConfirmShipmentContentUpdatePreviewResponse.model_rebuild()
ConfirmTransportationOptionsRequestBody.model_rebuild()
ConfirmTransportationOptionsResponse.model_rebuild()
ContactInformation.model_rebuild()
ContentUpdatePreview.model_rebuild()
CreateInboundPlanRequestBody.model_rebuild()
CreateInboundPlanResponse.model_rebuild()
CreateMarketplaceItemLabelsRequestBody.model_rebuild()
CreateMarketplaceItemLabelsResponse.model_rebuild()
Currency.model_rebuild()
CustomPlacementInput.model_rebuild()
Dates.model_rebuild()
DeliveryWindowOption.model_rebuild()
Dimensions.model_rebuild()
DocumentDownload.model_rebuild()
Error.model_rebuild()
ErrorList.model_rebuild()
FreightInformation.model_rebuild()
GenerateDeliveryWindowOptionsResponse.model_rebuild()
GeneratePackingOptionsResponse.model_rebuild()
GeneratePlacementOptionsRequestBody.model_rebuild()
GeneratePlacementOptionsResponse.model_rebuild()
GenerateSelfShipAppointmentSlotsRequestBody.model_rebuild()
GenerateSelfShipAppointmentSlotsResponse.model_rebuild()
GenerateShipmentContentUpdatePreviewsRequestBody.model_rebuild()
GenerateShipmentContentUpdatePreviewsResponse.model_rebuild()
GenerateTransportationOptionsRequestBody.model_rebuild()
GenerateTransportationOptionsResponse.model_rebuild()
GetDeliveryChallanDocumentResponse.model_rebuild()
GetSelfShipAppointmentSlotsResponse.model_rebuild()
InboundOperationStatus.model_rebuild()
InboundPlan.model_rebuild()
InboundPlanSummary.model_rebuild()
Incentive.model_rebuild()
Item.model_rebuild()
ItemInput.model_rebuild()
ListDeliveryWindowOptionsResponse.model_rebuild()
ListInboundPlanBoxesResponse.model_rebuild()
ListInboundPlanItemsResponse.model_rebuild()
ListInboundPlanPalletsResponse.model_rebuild()
ListInboundPlansResponse.model_rebuild()
ListItemComplianceDetailsResponse.model_rebuild()
ListPackingGroupBoxesResponse.model_rebuild()
ListPackingGroupItemsResponse.model_rebuild()
ListPackingOptionsResponse.model_rebuild()
ListPlacementOptionsResponse.model_rebuild()
ListPrepDetailsResponse.model_rebuild()
ListShipmentBoxesResponse.model_rebuild()
ListShipmentContentUpdatePreviewsResponse.model_rebuild()
ListShipmentItemsResponse.model_rebuild()
ListShipmentPalletsResponse.model_rebuild()
ListTransportationOptionsResponse.model_rebuild()
LtlTrackingDetail.model_rebuild()
LtlTrackingDetailInput.model_rebuild()
MskuPrepDetail.model_rebuild()
MskuPrepDetailInput.model_rebuild()
MskuQuantity.model_rebuild()
OperationProblem.model_rebuild()
PackageGroupingInput.model_rebuild()
PackingConfiguration.model_rebuild()
PackingOption.model_rebuild()
PackingOptionSummary.model_rebuild()
Pagination.model_rebuild()
Pallet.model_rebuild()
PalletInput.model_rebuild()
PlacementOption.model_rebuild()
PlacementOptionSummary.model_rebuild()
PrepInstruction.model_rebuild()
Quote.model_rebuild()
Region.model_rebuild()
RequestedUpdates.model_rebuild()
ScheduleSelfShipAppointmentRequestBody.model_rebuild()
ScheduleSelfShipAppointmentResponse.model_rebuild()
SelectedDeliveryWindow.model_rebuild()
SelfShipAppointmentDetails.model_rebuild()
SelfShipAppointmentSlotsAvailability.model_rebuild()
SetPackingInformationRequestBody.model_rebuild()
SetPackingInformationResponse.model_rebuild()
SetPrepDetailsRequestBody.model_rebuild()
SetPrepDetailsResponse.model_rebuild()
Shipment.model_rebuild()
ShipmentDestination.model_rebuild()
ShipmentSource.model_rebuild()
ShipmentSummary.model_rebuild()
ShipmentTransportationConfiguration.model_rebuild()
ShippingConfiguration.model_rebuild()
ShippingRequirements.model_rebuild()
SpdTrackingDetail.model_rebuild()
SpdTrackingDetailInput.model_rebuild()
SpdTrackingItem.model_rebuild()
SpdTrackingItemInput.model_rebuild()
TaxDetails.model_rebuild()
TaxRate.model_rebuild()
TrackingDetails.model_rebuild()
TrackingDetailsInput.model_rebuild()
TransportationOption.model_rebuild()
TransportationSelection.model_rebuild()
UpdateInboundPlanNameRequestBody.model_rebuild()
UpdateItemComplianceDetailsRequestBody.model_rebuild()
UpdateItemComplianceDetailsResponse.model_rebuild()
UpdateShipmentNameRequestBody.model_rebuild()
UpdateShipmentSourceAddressRequestBody.model_rebuild()
UpdateShipmentSourceAddressResponse.model_rebuild()
UpdateShipmentTrackingDetailsRequestBody.model_rebuild()
UpdateShipmentTrackingDetailsResponse.model_rebuild()
Weight.model_rebuild()
WeightRange.model_rebuild()
Window.model_rebuild()
WindowInput.model_rebuild()
ListInboundPlansRequest.model_rebuild()
CreateInboundPlanRequest.model_rebuild()
GetInboundPlanRequest.model_rebuild()
ListInboundPlanBoxesRequest.model_rebuild()
CancelInboundPlanRequest.model_rebuild()
ListInboundPlanItemsRequest.model_rebuild()
UpdateInboundPlanNameRequest.model_rebuild()
ListPackingGroupBoxesRequest.model_rebuild()
ListPackingGroupItemsRequest.model_rebuild()
SetPackingInformationRequest.model_rebuild()
ListPackingOptionsRequest.model_rebuild()
GeneratePackingOptionsRequest.model_rebuild()
ConfirmPackingOptionRequest.model_rebuild()
ListInboundPlanPalletsRequest.model_rebuild()
ListPlacementOptionsRequest.model_rebuild()
GeneratePlacementOptionsRequest.model_rebuild()
ConfirmPlacementOptionRequest.model_rebuild()
GetShipmentRequest.model_rebuild()
ListShipmentBoxesRequest.model_rebuild()
ListShipmentContentUpdatePreviewsRequest.model_rebuild()
GenerateShipmentContentUpdatePreviewsRequest.model_rebuild()
GetShipmentContentUpdatePreviewRequest.model_rebuild()
ConfirmShipmentContentUpdatePreviewRequest.model_rebuild()
GetDeliveryChallanDocumentRequest.model_rebuild()
ListDeliveryWindowOptionsRequest.model_rebuild()
GenerateDeliveryWindowOptionsRequest.model_rebuild()
ConfirmDeliveryWindowOptionsRequest.model_rebuild()
ListShipmentItemsRequest.model_rebuild()
UpdateShipmentNameRequest.model_rebuild()
ListShipmentPalletsRequest.model_rebuild()
CancelSelfShipAppointmentRequest.model_rebuild()
GetSelfShipAppointmentSlotsRequest.model_rebuild()
GenerateSelfShipAppointmentSlotsRequest.model_rebuild()
ScheduleSelfShipAppointmentRequest.model_rebuild()
UpdateShipmentSourceAddressRequest.model_rebuild()
UpdateShipmentTrackingDetailsRequest.model_rebuild()
ListTransportationOptionsRequest.model_rebuild()
GenerateTransportationOptionsRequest.model_rebuild()
ConfirmTransportationOptionsRequest.model_rebuild()
ListItemComplianceDetailsRequest.model_rebuild()
UpdateItemComplianceDetailsRequest.model_rebuild()
CreateMarketplaceItemLabelsRequest.model_rebuild()
ListPrepDetailsRequest.model_rebuild()
SetPrepDetailsRequest.model_rebuild()
GetInboundOperationStatusRequest.model_rebuild()
