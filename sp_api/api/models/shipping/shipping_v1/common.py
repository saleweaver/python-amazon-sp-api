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
Currency

The total value of all items in the container.
"""


class Currency(SpApiBaseModel):
    """The total value of all items in the container."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    value: Annotated[float, Field(..., description="The amount of currency.")]

    unit: Annotated[str, Field(..., description="A 3-character currency code.")]


ServiceType = str
"""The type of shipping service that will be used for the service offering."""


"""
TimeRange

The time range.
"""


class TimeRange(SpApiBaseModel):
    """The time range."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    start: Annotated[
        Optional[datetime],
        Field(
            None,
            description="The start date and time. This defaults to the current date and time.",
        ),
    ]

    end: Annotated[
        Optional[datetime],
        Field(
            None,
            description="The end date and time. This must come after the value of start. This defaults to the next business day from the start.",
        ),
    ]


"""
ShippingPromiseSet

The promised delivery time and pickup time.
"""


class ShippingPromiseSet(SpApiBaseModel):
    """The promised delivery time and pickup time."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    delivery_window: Annotated[
        Optional["TimeRange"],
        Field(
            None,
            validation_alias=AliasChoices("deliveryWindow", "delivery_window"),
            serialization_alias="deliveryWindow",
            description="The time window in which the shipment will be delivered.",
        ),
    ]

    receive_window: Annotated[
        Optional["TimeRange"],
        Field(
            None,
            validation_alias=AliasChoices("receiveWindow", "receive_window"),
            serialization_alias="receiveWindow",
            description="The time window in which Amazon Shipping will pick up the shipment.",
        ),
    ]


# Enum definitions
class UnitEnum(str, Enum):
    """Enum for unit"""

    G = "g"  # Grams
    KG = "kg"  # Kilograms
    OZ = "oz"  # Ounces
    LB = "lb"  # Pounds


"""
Weight

The weight.
"""


class Weight(SpApiBaseModel):
    """The weight."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    unit: Annotated[UnitEnum, Field(..., description="The unit of measurement.")]

    value: Annotated[float, Field(..., description="The measurement value.")]


"""
AcceptedRate

The specific rate purchased for the shipment, or null if unpurchased.
"""


class AcceptedRate(SpApiBaseModel):
    """The specific rate purchased for the shipment, or null if unpurchased."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    total_charge: Annotated[
        Optional["Currency"],
        Field(
            None,
            validation_alias=AliasChoices("totalCharge", "total_charge"),
            serialization_alias="totalCharge",
            description="The total charge that will be billed for the rate.",
        ),
    ]

    billed_weight: Annotated[
        Optional["Weight"],
        Field(
            None,
            validation_alias=AliasChoices("billedWeight", "billed_weight"),
            serialization_alias="billedWeight",
            description="The weight that was used to calculate the totalCharge.",
        ),
    ]

    service_type: Annotated[
        Optional["ServiceType"],
        Field(
            None,
            validation_alias=AliasChoices("serviceType", "service_type"),
            serialization_alias="serviceType",
        ),
    ]

    promise: Annotated[
        Optional["ShippingPromiseSet"],
        Field(
            None,
        ),
    ]


AccountId = str
"""This is the Amazon Shipping account id generated during the Amazon Shipping onboarding process."""


"""
Account

The account related data.
"""


class Account(SpApiBaseModel):
    """The account related data."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    account_id: Annotated[
        "AccountId",
        Field(
            ...,
            validation_alias=AliasChoices("accountId", "account_id"),
            serialization_alias="accountId",
        ),
    ]


City = str
"""The city where the person, business or institution is located."""


CountryCode = str
"""The two digit country code. In ISO 3166-1 alpha-2 format."""


PostalCode = str
"""The postal code of that address. It contains a series of letters or digits or both, sometimes including spaces or punctuation."""


StateOrRegion = str
"""The state or region where the person, business or institution is located."""


"""
Address

The address.
"""


class Address(SpApiBaseModel):
    """The address."""

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
            description="First line of that address.",
        ),
    ]

    address_line2: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("addressLine2", "address_line2"),
            serialization_alias="addressLine2",
            description="Additional address information, if required.",
        ),
    ]

    address_line3: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("addressLine3", "address_line3"),
            serialization_alias="addressLine3",
            description="Additional address information, if required.",
        ),
    ]

    state_or_region: Annotated[
        "StateOrRegion",
        Field(
            ...,
            validation_alias=AliasChoices("stateOrRegion", "state_or_region"),
            serialization_alias="stateOrRegion",
        ),
    ]

    city: Annotated[
        "City",
        Field(
            ...,
        ),
    ]

    country_code: Annotated[
        "CountryCode",
        Field(
            ...,
            validation_alias=AliasChoices("countryCode", "country_code"),
            serialization_alias="countryCode",
        ),
    ]

    postal_code: Annotated[
        "PostalCode",
        Field(
            ...,
            validation_alias=AliasChoices("postalCode", "postal_code"),
            serialization_alias="postalCode",
        ),
    ]

    email: Annotated[
        Optional[str],
        Field(
            None,
            description="The email address of the contact associated with the address.",
        ),
    ]

    copy_emails: Annotated[
        Optional[List["str"]],
        Field(
            None,
            validation_alias=AliasChoices("copyEmails", "copy_emails"),
            serialization_alias="copyEmails",
            description="The email cc addresses of the contact associated with the address.",
        ),
    ]

    phone_number: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("phoneNumber", "phone_number"),
            serialization_alias="phoneNumber",
            description="The phone number of the person, business or institution located at that address.",
        ),
    ]


"""
CancelShipmentRequest

Request parameters for cancelShipment
"""


class CancelShipmentRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for cancelShipment
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    shipment_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("shipmentId", "shipment_id"),
            serialization_alias="shipmentId",
            description="[PATH] Shipment Id to cancel a shipment",
        ),
    ]


ErrorList = List["Error"]
"""A list of error responses returned when a request is unsuccessful."""


"""
CancelShipmentResponse

The response schema for the cancelShipment operation.
"""


class CancelShipmentResponse(SpApiBaseModel):
    """The response schema for the cancelShipment operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    errors: Annotated[
        Optional["ErrorList"],
        Field(None, description="Encountered errors for the operation."),
    ]


ClientReferenceId = str
"""Client reference id."""


"""
ContainerItem

Item in the container.
"""


class ContainerItem(SpApiBaseModel):
    """Item in the container."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    quantity: Annotated[
        float,
        Field(
            ..., description="The quantity of the items of this type in the container."
        ),
    ]

    unit_price: Annotated[
        "Currency",
        Field(
            ...,
            validation_alias=AliasChoices("unitPrice", "unit_price"),
            serialization_alias="unitPrice",
            description="The unit price of an item of this type (the total value of this item type in the container is unitPrice x quantity).",
        ),
    ]

    unit_weight: Annotated[
        "Weight",
        Field(
            ...,
            validation_alias=AliasChoices("unitWeight", "unit_weight"),
            serialization_alias="unitWeight",
            description="The unit weight of an item of this type (the total weight of this item type in the container is unitWeight x quantity).",
        ),
    ]

    title: Annotated[str, Field(..., description="A descriptive title of the item.")]


ContainerReferenceId = str
"""An identifier for the container. This must be unique within all the containers in the same shipment."""


# Enum definitions
class UnitEnum(str, Enum):
    """Enum for unit"""

    G = "g"  # Grams
    KG = "kg"  # Kilograms
    OZ = "oz"  # Ounces
    LB = "lb"  # Pounds


"""
Dimensions

A set of measurements for a three-dimensional object.
"""


class Dimensions(SpApiBaseModel):
    """A set of measurements for a three-dimensional object."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    length: Annotated[float, Field(..., description="The length of the container.")]

    width: Annotated[float, Field(..., description="The width of the container.")]

    height: Annotated[float, Field(..., description="The height of the container.")]

    unit: Annotated[UnitEnum, Field(..., description="The unit of these measurements.")]


# Enum definitions
class ContainerTypeEnum(str, Enum):
    """Enum for containerType"""

    PACKAGE = "PACKAGE"  # PACKAGE


"""
Container

Container in the shipment.
"""


class Container(SpApiBaseModel):
    """Container in the shipment."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    container_type: Annotated[
        Optional[ContainerTypeEnum],
        Field(
            None,
            validation_alias=AliasChoices("containerType", "container_type"),
            serialization_alias="containerType",
            description="The type of physical container being used. (always 'PACKAGE')",
        ),
    ]

    container_reference_id: Annotated[
        "ContainerReferenceId",
        Field(
            ...,
            validation_alias=AliasChoices(
                "containerReferenceId", "container_reference_id"
            ),
            serialization_alias="containerReferenceId",
        ),
    ]

    value: Annotated[
        "Currency",
        Field(..., description="The total value of all items in the container."),
    ]

    dimensions: Annotated[
        "Dimensions",
        Field(
            ..., description="The length, width, height, and weight of the container."
        ),
    ]

    items: Annotated[
        List["ContainerItem"],
        Field(..., description="A list of the items in the container."),
    ]

    weight: Annotated["Weight", Field(..., description="The weight of the container.")]


ContainerList = List["Container"]
"""A list of container."""


"""
ContainerSpecification

Container specification for checking the service rate.
"""


class ContainerSpecification(SpApiBaseModel):
    """Container specification for checking the service rate."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    dimensions: Annotated[
        "Dimensions",
        Field(..., description="The length, width, and height of the container."),
    ]

    weight: Annotated["Weight", Field(..., description="The weight of the container.")]


ContainerSpecificationList = List["ContainerSpecification"]
"""A list of container specifications."""


"""
CreateShipmentRequestBody

The request schema for the createShipment operation.
"""


class CreateShipmentRequestBody(SpApiBaseModel):
    """The request schema for the createShipment operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    client_reference_id: Annotated[
        "ClientReferenceId",
        Field(
            ...,
            validation_alias=AliasChoices("clientReferenceId", "client_reference_id"),
            serialization_alias="clientReferenceId",
        ),
    ]

    ship_to: Annotated[
        "Address",
        Field(
            ...,
            validation_alias=AliasChoices("shipTo", "ship_to"),
            serialization_alias="shipTo",
        ),
    ]

    ship_from: Annotated[
        "Address",
        Field(
            ...,
            validation_alias=AliasChoices("shipFrom", "ship_from"),
            serialization_alias="shipFrom",
        ),
    ]

    containers: Annotated[
        "ContainerList",
        Field(
            ...,
        ),
    ]


"""
CreateShipmentRequest

Request parameters for createShipment
"""


class CreateShipmentRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for createShipment
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    body: Annotated[
        "CreateShipmentRequestBody",
        BodyParam(),
        Field(..., description="[BODY] CreateShipmentRequestBody Body"),
    ]


RateList = List["Rate"]
"""A list of all the available rates that can be used to send the shipment."""


ShipmentId = str
"""The unique shipment identifier."""


"""
CreateShipmentResult

The payload schema for the createShipment operation.
"""


class CreateShipmentResult(SpApiBaseModel):
    """The payload schema for the createShipment operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    shipment_id: Annotated[
        "ShipmentId",
        Field(
            ...,
            validation_alias=AliasChoices("shipmentId", "shipment_id"),
            serialization_alias="shipmentId",
        ),
    ]

    eligible_rates: Annotated[
        "RateList",
        Field(
            ...,
            validation_alias=AliasChoices("eligibleRates", "eligible_rates"),
            serialization_alias="eligibleRates",
        ),
    ]


"""
CreateShipmentResponse

The response schema for the createShipment operation.
"""


class CreateShipmentResponse(SpApiBaseModel):
    """The response schema for the createShipment operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["CreateShipmentResult"],
        Field(None, description="The payload for createShipment operation"),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(None, description="Encountered errors for the operation."),
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


EventCode = str
"""The event code of a shipment, such as Departed, Received, and ReadyForReceive."""


"""
Location

The location where the person, business or institution is located.
"""


class Location(SpApiBaseModel):
    """The location where the person, business or institution is located."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    state_or_region: Annotated[
        Optional["StateOrRegion"],
        Field(
            None,
            validation_alias=AliasChoices("stateOrRegion", "state_or_region"),
            serialization_alias="stateOrRegion",
        ),
    ]

    city: Annotated[
        Optional["City"],
        Field(
            None,
        ),
    ]

    country_code: Annotated[
        Optional["CountryCode"],
        Field(
            None,
            validation_alias=AliasChoices("countryCode", "country_code"),
            serialization_alias="countryCode",
        ),
    ]

    postal_code: Annotated[
        Optional["PostalCode"],
        Field(
            None,
            validation_alias=AliasChoices("postalCode", "postal_code"),
            serialization_alias="postalCode",
        ),
    ]


"""
Event

An event of a shipment
"""


class Event(SpApiBaseModel):
    """An event of a shipment"""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    event_code: Annotated[
        "EventCode",
        Field(
            ...,
            validation_alias=AliasChoices("eventCode", "event_code"),
            serialization_alias="eventCode",
        ),
    ]

    event_time: Annotated[
        datetime,
        Field(
            ...,
            validation_alias=AliasChoices("eventTime", "event_time"),
            serialization_alias="eventTime",
            description="The date and time of an event for a shipment.",
        ),
    ]

    location: Annotated[
        Optional["Location"],
        Field(
            None,
        ),
    ]


EventList = List["Event"]
"""A list of events of a shipment."""


"""
GetAccountResponse

The response schema for the getAccount operation.
"""


class GetAccountResponse(SpApiBaseModel):
    """The response schema for the getAccount operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["Account"],
        Field(None, description="The payload for getAccount operation"),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(None, description="Encountered errors for the operation."),
    ]


ServiceTypeList = List["ServiceType"]
"""A list of service types that can be used to send the shipment."""


"""
GetRatesRequestBody

The payload schema for the getRates operation.
"""


class GetRatesRequestBody(SpApiBaseModel):
    """The payload schema for the getRates operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    ship_to: Annotated[
        "Address",
        Field(
            ...,
            validation_alias=AliasChoices("shipTo", "ship_to"),
            serialization_alias="shipTo",
        ),
    ]

    ship_from: Annotated[
        "Address",
        Field(
            ...,
            validation_alias=AliasChoices("shipFrom", "ship_from"),
            serialization_alias="shipFrom",
        ),
    ]

    service_types: Annotated[
        "ServiceTypeList",
        Field(
            ...,
            validation_alias=AliasChoices("serviceTypes", "service_types"),
            serialization_alias="serviceTypes",
        ),
    ]

    ship_date: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices("shipDate", "ship_date"),
            serialization_alias="shipDate",
            description="The start date and time. This defaults to the current date and time.",
        ),
    ]

    container_specifications: Annotated[
        "ContainerSpecificationList",
        Field(
            ...,
            validation_alias=AliasChoices(
                "containerSpecifications", "container_specifications"
            ),
            serialization_alias="containerSpecifications",
        ),
    ]


"""
GetRatesRequest

Request parameters for getRates
"""


class GetRatesRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getRates
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    body: Annotated[
        "GetRatesRequestBody",
        BodyParam(),
        Field(..., description="[BODY] GetRatesRequestBody body"),
    ]


ServiceRateList = List["ServiceRate"]
"""A list of service rates."""


"""
GetRatesResult

The payload schema for the getRates operation.
"""


class GetRatesResult(SpApiBaseModel):
    """The payload schema for the getRates operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    service_rates: Annotated[
        "ServiceRateList",
        Field(
            ...,
            validation_alias=AliasChoices("serviceRates", "service_rates"),
            serialization_alias="serviceRates",
        ),
    ]


"""
GetRatesResponse

The response schema for the getRates operation.
"""


class GetRatesResponse(SpApiBaseModel):
    """The response schema for the getRates operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["GetRatesResult"],
        Field(None, description="The payload for getRates operation"),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(None, description="Encountered errors for the operation."),
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

    shipment_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("shipmentId", "shipment_id"),
            serialization_alias="shipmentId",
            description="[PATH] Shipment id to return the entire shipment object",
        ),
    ]


"""
Party

The account related with the shipment.
"""


class Party(SpApiBaseModel):
    """The account related with the shipment."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    account_id: Annotated[
        Optional["AccountId"],
        Field(
            None,
            validation_alias=AliasChoices("accountId", "account_id"),
            serialization_alias="accountId",
        ),
    ]


"""
Shipment

The shipment related data.
"""


class Shipment(SpApiBaseModel):
    """The shipment related data."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    shipment_id: Annotated[
        "ShipmentId",
        Field(
            ...,
            validation_alias=AliasChoices("shipmentId", "shipment_id"),
            serialization_alias="shipmentId",
        ),
    ]

    client_reference_id: Annotated[
        "ClientReferenceId",
        Field(
            ...,
            validation_alias=AliasChoices("clientReferenceId", "client_reference_id"),
            serialization_alias="clientReferenceId",
        ),
    ]

    ship_from: Annotated[
        "Address",
        Field(
            ...,
            validation_alias=AliasChoices("shipFrom", "ship_from"),
            serialization_alias="shipFrom",
        ),
    ]

    ship_to: Annotated[
        "Address",
        Field(
            ...,
            validation_alias=AliasChoices("shipTo", "ship_to"),
            serialization_alias="shipTo",
        ),
    ]

    accepted_rate: Annotated[
        Optional["AcceptedRate"],
        Field(
            None,
            validation_alias=AliasChoices("acceptedRate", "accepted_rate"),
            serialization_alias="acceptedRate",
        ),
    ]

    shipper: Annotated[
        Optional["Party"],
        Field(
            None,
        ),
    ]

    containers: Annotated[
        "ContainerList",
        Field(
            ...,
        ),
    ]


"""
GetShipmentResponse

The response schema for the getShipment operation.
"""


class GetShipmentResponse(SpApiBaseModel):
    """The response schema for the getShipment operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["Shipment"],
        Field(None, description="The payload for getShipment operation"),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(None, description="Encountered errors for the operation."),
    ]


"""
GetTrackingInformationRequest

Request parameters for getTrackingInformation
"""


class GetTrackingInformationRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getTrackingInformation
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    tracking_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("trackingId", "tracking_id"),
            serialization_alias="trackingId",
            description="[PATH] Tracking Id",
        ),
    ]


PromisedDeliveryDate = str
"""The promised delivery date and time of a shipment."""


TrackingId = str
"""The tracking id generated to each shipment. It contains a series of letters or digits or both."""


"""
TrackingSummary

The tracking summary.
"""


class TrackingSummary(SpApiBaseModel):
    """The tracking summary."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    status: Annotated[
        Optional[str],
        Field(
            None,
            description="The derived status based on the events in the eventHistory.",
        ),
    ]


"""
TrackingInformation

The payload schema for the getTrackingInformation operation.
"""


class TrackingInformation(SpApiBaseModel):
    """The payload schema for the getTrackingInformation operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    tracking_id: Annotated[
        "TrackingId",
        Field(
            ...,
            validation_alias=AliasChoices("trackingId", "tracking_id"),
            serialization_alias="trackingId",
        ),
    ]

    summary: Annotated[
        "TrackingSummary",
        Field(
            ...,
        ),
    ]

    promised_delivery_date: Annotated[
        "PromisedDeliveryDate",
        Field(
            ...,
            validation_alias=AliasChoices(
                "promisedDeliveryDate", "promised_delivery_date"
            ),
            serialization_alias="promisedDeliveryDate",
        ),
    ]

    event_history: Annotated[
        "EventList",
        Field(
            ...,
            validation_alias=AliasChoices("eventHistory", "event_history"),
            serialization_alias="eventHistory",
        ),
    ]


"""
GetTrackingInformationResponse

The response schema for the getTrackingInformation operation.
"""


class GetTrackingInformationResponse(SpApiBaseModel):
    """The response schema for the getTrackingInformation operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["TrackingInformation"],
        Field(None, description="The payload for getTrackingInformation operation"),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(None, description="Encountered errors for the operation."),
    ]


# Enum definitions
class LabelFormatEnum(str, Enum):
    """Enum for labelFormat"""

    PNG = "PNG"  # PNG


class LabelStockSizeEnum(str, Enum):
    """Enum for labelStockSize"""

    VALUE_4X6 = "4x6"  # 4x6


"""
LabelSpecification

The label specification info.
"""


class LabelSpecification(SpApiBaseModel):
    """The label specification info."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    label_format: Annotated[
        LabelFormatEnum,
        Field(
            ...,
            validation_alias=AliasChoices("labelFormat", "label_format"),
            serialization_alias="labelFormat",
            description="The format of the label. Enum of PNG only for now.",
        ),
    ]

    label_stock_size: Annotated[
        LabelStockSizeEnum,
        Field(
            ...,
            validation_alias=AliasChoices("labelStockSize", "label_stock_size"),
            serialization_alias="labelStockSize",
            description="The label stock size specification in length and height. Enum of 4x6 only for now.",
        ),
    ]


LabelStream = str
"""Contains binary image data encoded as a base-64 string."""


"""
Label

The label details of the container.
"""


class Label(SpApiBaseModel):
    """The label details of the container."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    label_stream: Annotated[
        Optional["LabelStream"],
        Field(
            None,
            validation_alias=AliasChoices("labelStream", "label_stream"),
            serialization_alias="labelStream",
        ),
    ]

    label_specification: Annotated[
        Optional["LabelSpecification"],
        Field(
            None,
            validation_alias=AliasChoices("labelSpecification", "label_specification"),
            serialization_alias="labelSpecification",
        ),
    ]


"""
LabelResult

Label details including label stream, format, size.
"""


class LabelResult(SpApiBaseModel):
    """Label details including label stream, format, size."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    container_reference_id: Annotated[
        Optional["ContainerReferenceId"],
        Field(
            None,
            validation_alias=AliasChoices(
                "containerReferenceId", "container_reference_id"
            ),
            serialization_alias="containerReferenceId",
        ),
    ]

    tracking_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("trackingId", "tracking_id"),
            serialization_alias="trackingId",
            description="The tracking identifier assigned to the container.",
        ),
    ]

    label: Annotated[
        Optional["Label"],
        Field(
            None,
        ),
    ]


LabelResultList = List["LabelResult"]
"""A list of label results"""


RateId = str
"""An identifier for the rating."""


"""
PurchaseLabelsRequestBody

The request schema for the purchaseLabels operation.
"""


class PurchaseLabelsRequestBody(SpApiBaseModel):
    """The request schema for the purchaseLabels operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    rate_id: Annotated[
        "RateId",
        Field(
            ...,
            validation_alias=AliasChoices("rateId", "rate_id"),
            serialization_alias="rateId",
        ),
    ]

    label_specification: Annotated[
        "LabelSpecification",
        Field(
            ...,
            validation_alias=AliasChoices("labelSpecification", "label_specification"),
            serialization_alias="labelSpecification",
        ),
    ]


"""
PurchaseLabelsRequest

Request parameters for purchaseLabels
"""


class PurchaseLabelsRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for purchaseLabels
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    shipment_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("shipmentId", "shipment_id"),
            serialization_alias="shipmentId",
            description="[PATH] Shipment id for purchase shipping label",
        ),
    ]

    body: Annotated[
        "PurchaseLabelsRequestBody",
        BodyParam(),
        Field(..., description="[BODY] PurchaseShippingLabelRequestBody body"),
    ]


"""
PurchaseLabelsResult

The payload schema for the purchaseLabels operation.
"""


class PurchaseLabelsResult(SpApiBaseModel):
    """The payload schema for the purchaseLabels operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    shipment_id: Annotated[
        "ShipmentId",
        Field(
            ...,
            validation_alias=AliasChoices("shipmentId", "shipment_id"),
            serialization_alias="shipmentId",
        ),
    ]

    client_reference_id: Annotated[
        Optional["ClientReferenceId"],
        Field(
            None,
            validation_alias=AliasChoices("clientReferenceId", "client_reference_id"),
            serialization_alias="clientReferenceId",
        ),
    ]

    accepted_rate: Annotated[
        "AcceptedRate",
        Field(
            ...,
            validation_alias=AliasChoices("acceptedRate", "accepted_rate"),
            serialization_alias="acceptedRate",
        ),
    ]

    label_results: Annotated[
        "LabelResultList",
        Field(
            ...,
            validation_alias=AliasChoices("labelResults", "label_results"),
            serialization_alias="labelResults",
        ),
    ]


"""
PurchaseLabelsResponse

The response schema for the purchaseLabels operation.
"""


class PurchaseLabelsResponse(SpApiBaseModel):
    """The response schema for the purchaseLabels operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["PurchaseLabelsResult"],
        Field(None, description="The payload for purchaseLabels operation"),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(None, description="Encountered errors for the operation."),
    ]


"""
PurchaseShipmentRequestBody

The payload schema for the purchaseShipment operation.
"""


class PurchaseShipmentRequestBody(SpApiBaseModel):
    """The payload schema for the purchaseShipment operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    client_reference_id: Annotated[
        "ClientReferenceId",
        Field(
            ...,
            validation_alias=AliasChoices("clientReferenceId", "client_reference_id"),
            serialization_alias="clientReferenceId",
        ),
    ]

    ship_to: Annotated[
        "Address",
        Field(
            ...,
            validation_alias=AliasChoices("shipTo", "ship_to"),
            serialization_alias="shipTo",
        ),
    ]

    ship_from: Annotated[
        "Address",
        Field(
            ...,
            validation_alias=AliasChoices("shipFrom", "ship_from"),
            serialization_alias="shipFrom",
        ),
    ]

    ship_date: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices("shipDate", "ship_date"),
            serialization_alias="shipDate",
            description="The start date and time. This defaults to the current date and time.",
        ),
    ]

    service_type: Annotated[
        "ServiceType",
        Field(
            ...,
            validation_alias=AliasChoices("serviceType", "service_type"),
            serialization_alias="serviceType",
        ),
    ]

    containers: Annotated[
        "ContainerList",
        Field(
            ...,
        ),
    ]

    label_specification: Annotated[
        "LabelSpecification",
        Field(
            ...,
            validation_alias=AliasChoices("labelSpecification", "label_specification"),
            serialization_alias="labelSpecification",
        ),
    ]


"""
PurchaseShipmentRequest

Request parameters for purchaseShipment
"""


class PurchaseShipmentRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for purchaseShipment
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    body: Annotated[
        "PurchaseShipmentRequestBody",
        BodyParam(),
        Field(..., description="[BODY] PurchaseShipmentRequestBody body"),
    ]


"""
ServiceRate

The specific rate for a shipping service, or null if no service available.
"""


class ServiceRate(SpApiBaseModel):
    """The specific rate for a shipping service, or null if no service available."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    total_charge: Annotated[
        "Currency",
        Field(
            ...,
            validation_alias=AliasChoices("totalCharge", "total_charge"),
            serialization_alias="totalCharge",
            description="The total charge that will be billed for the rate.",
        ),
    ]

    billable_weight: Annotated[
        "Weight",
        Field(
            ...,
            validation_alias=AliasChoices("billableWeight", "billable_weight"),
            serialization_alias="billableWeight",
            description="The weight that was used to calculate the totalCharge.",
        ),
    ]

    service_type: Annotated[
        "ServiceType",
        Field(
            ...,
            validation_alias=AliasChoices("serviceType", "service_type"),
            serialization_alias="serviceType",
        ),
    ]

    promise: Annotated[
        "ShippingPromiseSet",
        Field(
            ...,
        ),
    ]


"""
PurchaseShipmentResult

The payload schema for the purchaseShipment operation.
"""


class PurchaseShipmentResult(SpApiBaseModel):
    """The payload schema for the purchaseShipment operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    shipment_id: Annotated[
        "ShipmentId",
        Field(
            ...,
            validation_alias=AliasChoices("shipmentId", "shipment_id"),
            serialization_alias="shipmentId",
        ),
    ]

    service_rate: Annotated[
        "ServiceRate",
        Field(
            ...,
            validation_alias=AliasChoices("serviceRate", "service_rate"),
            serialization_alias="serviceRate",
        ),
    ]

    label_results: Annotated[
        "LabelResultList",
        Field(
            ...,
            validation_alias=AliasChoices("labelResults", "label_results"),
            serialization_alias="labelResults",
        ),
    ]


"""
PurchaseShipmentResponse

The response schema for the purchaseShipment operation.
"""


class PurchaseShipmentResponse(SpApiBaseModel):
    """The response schema for the purchaseShipment operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["PurchaseShipmentResult"],
        Field(None, description="The payload for purchaseShipment operation"),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(None, description="Encountered errors for the operation."),
    ]


"""
Rate

The available rate that can be used to send the shipment
"""


class Rate(SpApiBaseModel):
    """The available rate that can be used to send the shipment"""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    rate_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("rateId", "rate_id"),
            serialization_alias="rateId",
            description="An identifier for the rate.",
        ),
    ]

    total_charge: Annotated[
        Optional["Currency"],
        Field(
            None,
            validation_alias=AliasChoices("totalCharge", "total_charge"),
            serialization_alias="totalCharge",
            description="The total charge that will be billed for the rate.",
        ),
    ]

    billed_weight: Annotated[
        Optional["Weight"],
        Field(
            None,
            validation_alias=AliasChoices("billedWeight", "billed_weight"),
            serialization_alias="billedWeight",
            description="The weight that was used to calculate the totalCharge.",
        ),
    ]

    expiration_time: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices("expirationTime", "expiration_time"),
            serialization_alias="expirationTime",
            description="The time after which the offering will expire.",
        ),
    ]

    service_type: Annotated[
        Optional["ServiceType"],
        Field(
            None,
            validation_alias=AliasChoices("serviceType", "service_type"),
            serialization_alias="serviceType",
        ),
    ]

    promise: Annotated[
        Optional["ShippingPromiseSet"],
        Field(
            None,
        ),
    ]


"""
RetrieveShippingLabelRequestBody

The request schema for the retrieveShippingLabel operation.
"""


class RetrieveShippingLabelRequestBody(SpApiBaseModel):
    """The request schema for the retrieveShippingLabel operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    label_specification: Annotated[
        "LabelSpecification",
        Field(
            ...,
            validation_alias=AliasChoices("labelSpecification", "label_specification"),
            serialization_alias="labelSpecification",
        ),
    ]


"""
RetrieveShippingLabelRequest

Request parameters for retrieveShippingLabel
"""


class RetrieveShippingLabelRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for retrieveShippingLabel
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    shipment_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("shipmentId", "shipment_id"),
            serialization_alias="shipmentId",
            description="[PATH] Shipment Id to retreive label",
        ),
    ]

    tracking_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("trackingId", "tracking_id"),
            serialization_alias="trackingId",
            description="[PATH] Tracking Id",
        ),
    ]

    body: Annotated[
        "RetrieveShippingLabelRequestBody",
        BodyParam(),
        Field(..., description="[BODY] RetrieveShippingLabelRequestBody body"),
    ]


"""
RetrieveShippingLabelResult

The payload schema for the retrieveShippingLabel operation.
"""


class RetrieveShippingLabelResult(SpApiBaseModel):
    """The payload schema for the retrieveShippingLabel operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    label_stream: Annotated[
        "LabelStream",
        Field(
            ...,
            validation_alias=AliasChoices("labelStream", "label_stream"),
            serialization_alias="labelStream",
        ),
    ]

    label_specification: Annotated[
        "LabelSpecification",
        Field(
            ...,
            validation_alias=AliasChoices("labelSpecification", "label_specification"),
            serialization_alias="labelSpecification",
        ),
    ]


"""
RetrieveShippingLabelResponse

The response schema for the retrieveShippingLabel operation.
"""


class RetrieveShippingLabelResponse(SpApiBaseModel):
    """The response schema for the retrieveShippingLabel operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["RetrieveShippingLabelResult"],
        Field(None, description="The payload for retrieveShippingLabel operation"),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(None, description="Encountered errors for the operation."),
    ]


# Rebuild models to resolve forward references
Error.model_rebuild()
Location.model_rebuild()
Event.model_rebuild()
TrackingSummary.model_rebuild()
Address.model_rebuild()
TimeRange.model_rebuild()
ShippingPromiseSet.model_rebuild()
Rate.model_rebuild()
AcceptedRate.model_rebuild()
ServiceRate.model_rebuild()
Party.model_rebuild()
Currency.model_rebuild()
Dimensions.model_rebuild()
Weight.model_rebuild()
ContainerItem.model_rebuild()
Container.model_rebuild()
ContainerSpecification.model_rebuild()
Label.model_rebuild()
LabelResult.model_rebuild()
LabelSpecification.model_rebuild()
CreateShipmentRequestBody.model_rebuild()
PurchaseLabelsRequestBody.model_rebuild()
RetrieveShippingLabelRequestBody.model_rebuild()
GetRatesRequestBody.model_rebuild()
PurchaseShipmentRequestBody.model_rebuild()
CreateShipmentResult.model_rebuild()
Shipment.model_rebuild()
PurchaseLabelsResult.model_rebuild()
RetrieveShippingLabelResult.model_rebuild()
Account.model_rebuild()
GetRatesResult.model_rebuild()
PurchaseShipmentResult.model_rebuild()
TrackingInformation.model_rebuild()
CreateShipmentResponse.model_rebuild()
GetShipmentResponse.model_rebuild()
GetRatesResponse.model_rebuild()
PurchaseShipmentResponse.model_rebuild()
CancelShipmentResponse.model_rebuild()
PurchaseLabelsResponse.model_rebuild()
RetrieveShippingLabelResponse.model_rebuild()
GetAccountResponse.model_rebuild()
GetTrackingInformationResponse.model_rebuild()
CreateShipmentRequest.model_rebuild()
GetShipmentRequest.model_rebuild()
CancelShipmentRequest.model_rebuild()
PurchaseLabelsRequest.model_rebuild()
RetrieveShippingLabelRequest.model_rebuild()
PurchaseShipmentRequest.model_rebuild()
GetRatesRequest.model_rebuild()
GetTrackingInformationRequest.model_rebuild()
