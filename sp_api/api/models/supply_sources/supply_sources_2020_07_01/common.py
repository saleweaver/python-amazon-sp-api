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

A physical address.
"""


class Address(SpApiBaseModel):
    """A physical address."""

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
            description="The first line of the address.",
        ),
    ]

    address_line2: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("addressLine2", "address_line2"),
            serialization_alias="addressLine2",
            description="The additional address information, if required.",
        ),
    ]

    address_line3: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("addressLine3", "address_line3"),
            serialization_alias="addressLine3",
            description="The additional address information, if required.",
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
            description="The phone number of the person, business or institution located at that address.",
        ),
    ]


"""
ContactDetails

The contact details
"""


class ContactDetails(SpApiBaseModel):
    """The contact details"""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    primary: Annotated[
        Optional[Dict[str, Any]],
        Field(
            None,
        ),
    ]


"""
AddressWithContact

The address and contact details.
"""


class AddressWithContact(SpApiBaseModel):
    """The address and contact details."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    contact_details: Annotated[
        Optional["ContactDetails"],
        Field(
            None,
            validation_alias=AliasChoices("contactDetails", "contact_details"),
            serialization_alias="contactDetails",
        ),
    ]

    address: Annotated[
        Optional["Address"],
        Field(
            None,
        ),
    ]


"""
ArchiveSupplySourceRequest

Request parameters for archiveSupplySource
"""


class ArchiveSupplySourceRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for archiveSupplySource
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    supply_source_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("supplySourceId", "supply_source_id"),
            serialization_alias="supplySourceId",
            description="[PATH] The unique identifier of a supply source.",
        ),
    ]


SupplySourceAlias = str
"""The custom alias for this supply source"""


SupplySourceCode = str
"""The seller-provided unique supply source code."""


"""
CreateSupplySourceRequestBody

A request to create a supply source.
"""


class CreateSupplySourceRequestBody(SpApiBaseModel):
    """A request to create a supply source."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    supply_source_code: Annotated[
        "SupplySourceCode",
        Field(
            ...,
            validation_alias=AliasChoices("supplySourceCode", "supply_source_code"),
            serialization_alias="supplySourceCode",
        ),
    ]

    alias: Annotated[
        "SupplySourceAlias",
        Field(
            ...,
        ),
    ]

    address: Annotated[
        "Address",
        Field(
            ...,
        ),
    ]


"""
CreateSupplySourceRequest

Request parameters for createSupplySource
"""


class CreateSupplySourceRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for createSupplySource
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        "CreateSupplySourceRequestBody",
        BodyParam(),
        Field(..., description="[BODY] A request to create a supply source."),
    ]


SupplySourceId = str
"""An Amazon generated unique supply source ID."""


"""
CreateSupplySourceResponse

The result of creating a new supply source.
"""


class CreateSupplySourceResponse(SpApiBaseModel):
    """The result of creating a new supply source."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    supply_source_id: Annotated[
        "SupplySourceId",
        Field(
            ...,
            validation_alias=AliasChoices("supplySourceId", "supply_source_id"),
            serialization_alias="supplySourceId",
        ),
    ]

    supply_source_code: Annotated[
        "SupplySourceCode",
        Field(
            ...,
            validation_alias=AliasChoices("supplySourceCode", "supply_source_code"),
            serialization_alias="supplySourceCode",
        ),
    ]


NonNegativeInteger = int
"""An unsigned integer that can be only positive or zero."""


TimeUnit = str
"""The time unit"""


"""
Duration

The duration of time.
"""


class Duration(SpApiBaseModel):
    """The duration of time."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    value: Annotated[
        Optional["NonNegativeInteger"],
        Field(
            None,
        ),
    ]

    time_unit: Annotated[
        Optional["TimeUnit"],
        Field(
            None,
            validation_alias=AliasChoices("timeUnit", "time_unit"),
            serialization_alias="timeUnit",
        ),
    ]


OperatingHours = List["OperatingHour"]
"""A list of Operating Hours."""


"""
OperatingHoursByDay

The operating hours per day
"""


class OperatingHoursByDay(SpApiBaseModel):
    """The operating hours per day"""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    monday: Annotated[
        Optional["OperatingHours"],
        Field(
            None,
        ),
    ]

    tuesday: Annotated[
        Optional["OperatingHours"],
        Field(
            None,
        ),
    ]

    wednesday: Annotated[
        Optional["OperatingHours"],
        Field(
            None,
        ),
    ]

    thursday: Annotated[
        Optional["OperatingHours"],
        Field(
            None,
        ),
    ]

    friday: Annotated[
        Optional["OperatingHours"],
        Field(
            None,
        ),
    ]

    saturday: Annotated[
        Optional["OperatingHours"],
        Field(
            None,
        ),
    ]

    sunday: Annotated[
        Optional["OperatingHours"],
        Field(
            None,
        ),
    ]


"""
ThroughputCap

The throughput capacity
"""


class ThroughputCap(SpApiBaseModel):
    """The throughput capacity"""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    value: Annotated[
        Optional["NonNegativeInteger"],
        Field(
            None,
        ),
    ]

    time_unit: Annotated[
        Optional["TimeUnit"],
        Field(
            None,
            validation_alias=AliasChoices("timeUnit", "time_unit"),
            serialization_alias="timeUnit",
        ),
    ]


ThroughputUnit = str
"""The throughput unit"""


"""
ThroughputConfig

The throughput configuration.
"""


class ThroughputConfig(SpApiBaseModel):
    """The throughput configuration."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    throughput_cap: Annotated[
        Optional["ThroughputCap"],
        Field(
            None,
            validation_alias=AliasChoices("throughputCap", "throughput_cap"),
            serialization_alias="throughputCap",
        ),
    ]

    throughput_unit: Annotated[
        "ThroughputUnit",
        Field(
            ...,
            validation_alias=AliasChoices("throughputUnit", "throughput_unit"),
            serialization_alias="throughputUnit",
        ),
    ]


"""
OperationalConfiguration

The operational configuration of `supplySources`.
"""


class OperationalConfiguration(SpApiBaseModel):
    """The operational configuration of `supplySources`."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    contact_details: Annotated[
        Optional["ContactDetails"],
        Field(
            None,
            validation_alias=AliasChoices("contactDetails", "contact_details"),
            serialization_alias="contactDetails",
        ),
    ]

    throughput_config: Annotated[
        Optional["ThroughputConfig"],
        Field(
            None,
            validation_alias=AliasChoices("throughputConfig", "throughput_config"),
            serialization_alias="throughputConfig",
        ),
    ]

    operating_hours_by_day: Annotated[
        Optional["OperatingHoursByDay"],
        Field(
            None,
            validation_alias=AliasChoices(
                "operatingHoursByDay", "operating_hours_by_day"
            ),
            serialization_alias="operatingHoursByDay",
        ),
    ]

    handling_time: Annotated[
        Optional["Duration"],
        Field(
            None,
            validation_alias=AliasChoices("handlingTime", "handling_time"),
            serialization_alias="handlingTime",
        ),
    ]


"""
ParkingWithAddressConfiguration

The parking configuration with the address.
"""


class ParkingWithAddressConfiguration(SpApiBaseModel):
    """The parking configuration with the address."""

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow",
        serialize_by_alias=True,
        arbitrary_types_allowed=True,
    )


"""
CurbsidePickupConfiguration

The curbside pickup configuration of a supply source.
"""


class CurbsidePickupConfiguration(SpApiBaseModel):
    """The curbside pickup configuration of a supply source."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    is_supported: Annotated[
        Optional[bool],
        Field(
            None,
            validation_alias=AliasChoices("isSupported", "is_supported"),
            serialization_alias="isSupported",
            description="When true, curbside pickup is supported by the supply source.",
        ),
    ]

    operational_configuration: Annotated[
        Optional["OperationalConfiguration"],
        Field(
            None,
            validation_alias=AliasChoices(
                "operationalConfiguration", "operational_configuration"
            ),
            serialization_alias="operationalConfiguration",
            description="The operational configuration for the curbside pickup configuration.",
        ),
    ]

    parking_with_address_configuration: Annotated[
        Optional["ParkingWithAddressConfiguration"],
        Field(
            None,
            validation_alias=AliasChoices(
                "parkingWithAddressConfiguration", "parking_with_address_configuration"
            ),
            serialization_alias="parkingWithAddressConfiguration",
            description="The parking configuration for curbside pickup with address for customers to use.",
        ),
    ]


DateTime = str
"""A date and time in the rfc3339 format."""


"""
DeliveryChannel

The delivery channel of a supply source.
"""


class DeliveryChannel(SpApiBaseModel):
    """The delivery channel of a supply source."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    is_supported: Annotated[
        Optional[bool],
        Field(
            None,
            validation_alias=AliasChoices("isSupported", "is_supported"),
            serialization_alias="isSupported",
        ),
    ]

    operational_configuration: Annotated[
        Optional["OperationalConfiguration"],
        Field(
            None,
            validation_alias=AliasChoices(
                "operationalConfiguration", "operational_configuration"
            ),
            serialization_alias="operationalConfiguration",
        ),
    ]


EmailAddress = str
"""The email address to which email messages are delivered."""


"""
Error

An error response returned when the request is unsuccessful.
"""


class Error(SpApiBaseModel):
    """An error response returned when the request is unsuccessful."""

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
            description="A list of error responses returned when a request is unsuccessful.",
        ),
    ]


"""
GetSupplySourceRequest

Request parameters for getSupplySource
"""


class GetSupplySourceRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getSupplySource
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    supply_source_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("supplySourceId", "supply_source_id"),
            serialization_alias="supplySourceId",
            description="[PATH] The unique identifier of a supply source.",
        ),
    ]


"""
GetSupplySourcesRequest

Request parameters for getSupplySources
"""


class GetSupplySourcesRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getSupplySources
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    next_page_token: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("nextPageToken", "next_page_token"),
            serialization_alias="nextPageToken",
            description="[QUERY] The pagination token to retrieve a specific page of results.",
        ),
    ]

    page_size: Annotated[
        Optional[float],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("pageSize", "page_size"),
            serialization_alias="pageSize",
            description="[QUERY] The number of supply sources to return per paginated request.",
        ),
    ]


"""
SupplySourceList

The list of `SupplySource`s.
"""


class SupplySourceList(SpApiBaseModel):
    """The list of `SupplySource`s."""

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow",
        serialize_by_alias=True,
        arbitrary_types_allowed=True,
    )


"""
GetSupplySourcesResponse

The paginated list of supply sources.
"""


class GetSupplySourcesResponse(SpApiBaseModel):
    """The paginated list of supply sources."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    supply_sources: Annotated[
        Optional["SupplySourceList"],
        Field(
            None,
            validation_alias=AliasChoices("supplySources", "supply_sources"),
            serialization_alias="supplySources",
        ),
    ]

    next_page_token: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("nextPageToken", "next_page_token"),
            serialization_alias="nextPageToken",
            description="If present, use this pagination token to retrieve the next page of supply sources.",
        ),
    ]


ParkingCostType = str
"""The parking cost type."""


ParkingSpotIdentificationType = str
"""The type of parking spot identification."""


"""
ParkingConfiguration

The parking configuration.
"""


class ParkingConfiguration(SpApiBaseModel):
    """The parking configuration."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    parking_cost_type: Annotated[
        Optional["ParkingCostType"],
        Field(
            None,
            validation_alias=AliasChoices("parkingCostType", "parking_cost_type"),
            serialization_alias="parkingCostType",
            description="The type of cost at parking location.",
        ),
    ]

    parking_spot_identification_type: Annotated[
        Optional["ParkingSpotIdentificationType"],
        Field(
            None,
            validation_alias=AliasChoices(
                "parkingSpotIdentificationType", "parking_spot_identification_type"
            ),
            serialization_alias="parkingSpotIdentificationType",
            description="The type of parking spot identification used at parking location.",
        ),
    ]

    number_of_parking_spots: Annotated[
        Optional["NonNegativeInteger"],
        Field(
            None,
            validation_alias=AliasChoices(
                "numberOfParkingSpots", "number_of_parking_spots"
            ),
            serialization_alias="numberOfParkingSpots",
            description="The number of parking spots.",
        ),
    ]


"""
InStorePickupConfiguration

The in-store pickup configuration of a supply source.
"""


class InStorePickupConfiguration(SpApiBaseModel):
    """The in-store pickup configuration of a supply source."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    is_supported: Annotated[
        Optional[bool],
        Field(
            None,
            validation_alias=AliasChoices("isSupported", "is_supported"),
            serialization_alias="isSupported",
            description="When true, in-store pickup is supported by the supply source (default: `isSupported` value in `PickupChannel`).",
        ),
    ]

    parking_configuration: Annotated[
        Optional["ParkingConfiguration"],
        Field(
            None,
            validation_alias=AliasChoices(
                "parkingConfiguration", "parking_configuration"
            ),
            serialization_alias="parkingConfiguration",
            description="The parking configuration for in-store pickup.",
        ),
    ]


"""
OperatingHour

The operating hour schema
"""


class OperatingHour(SpApiBaseModel):
    """The operating hour schema"""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    start_time: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("startTime", "start_time"),
            serialization_alias="startTime",
            description="The opening time, ISO 8601 formatted timestamp without date, HH:mm.",
        ),
    ]

    end_time: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("endTime", "end_time"),
            serialization_alias="endTime",
            description="The closing time, ISO 8601 formatted timestamp without date, HH:mm.",
        ),
    ]


"""
PickupChannel

The pick up channel of a supply source.
"""


class PickupChannel(SpApiBaseModel):
    """The pick up channel of a supply source."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    inventory_hold_period: Annotated[
        Optional["Duration"],
        Field(
            None,
            validation_alias=AliasChoices(
                "inventoryHoldPeriod", "inventory_hold_period"
            ),
            serialization_alias="inventoryHoldPeriod",
        ),
    ]

    is_supported: Annotated[
        Optional[bool],
        Field(
            None,
            validation_alias=AliasChoices("isSupported", "is_supported"),
            serialization_alias="isSupported",
        ),
    ]

    operational_configuration: Annotated[
        Optional["OperationalConfiguration"],
        Field(
            None,
            validation_alias=AliasChoices(
                "operationalConfiguration", "operational_configuration"
            ),
            serialization_alias="operationalConfiguration",
        ),
    ]

    in_store_pickup_configuration: Annotated[
        Optional["InStorePickupConfiguration"],
        Field(
            None,
            validation_alias=AliasChoices(
                "inStorePickupConfiguration", "in_store_pickup_configuration"
            ),
            serialization_alias="inStorePickupConfiguration",
            description="The configuration for supporting in-store pickup.",
        ),
    ]

    curbside_pickup_configuration: Annotated[
        Optional["CurbsidePickupConfiguration"],
        Field(
            None,
            validation_alias=AliasChoices(
                "curbsidePickupConfiguration", "curbside_pickup_configuration"
            ),
            serialization_alias="curbsidePickupConfiguration",
            description="The configuration for supporting curbside pickup.",
        ),
    ]


"""
ReturnLocation

The address or reference to another `supplySourceId` to act as a return location.
"""


class ReturnLocation(SpApiBaseModel):
    """The address or reference to another `supplySourceId` to act as a return location."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    supply_source_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("supplySourceId", "supply_source_id"),
            serialization_alias="supplySourceId",
            description="The Amazon provided `supplySourceId` where orders can be returned to.",
        ),
    ]

    address_with_contact: Annotated[
        Optional["AddressWithContact"],
        Field(
            None,
            validation_alias=AliasChoices("addressWithContact", "address_with_contact"),
            serialization_alias="addressWithContact",
        ),
    ]


"""
OutboundCapability

The outbound capability of a supply source.
"""


class OutboundCapability(SpApiBaseModel):
    """The outbound capability of a supply source."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    is_supported: Annotated[
        Optional[bool],
        Field(
            None,
            validation_alias=AliasChoices("isSupported", "is_supported"),
            serialization_alias="isSupported",
        ),
    ]

    operational_configuration: Annotated[
        Optional["OperationalConfiguration"],
        Field(
            None,
            validation_alias=AliasChoices(
                "operationalConfiguration", "operational_configuration"
            ),
            serialization_alias="operationalConfiguration",
        ),
    ]

    return_location: Annotated[
        Optional["ReturnLocation"],
        Field(
            None,
            validation_alias=AliasChoices("returnLocation", "return_location"),
            serialization_alias="returnLocation",
        ),
    ]

    delivery_channel: Annotated[
        Optional["DeliveryChannel"],
        Field(
            None,
            validation_alias=AliasChoices("deliveryChannel", "delivery_channel"),
            serialization_alias="deliveryChannel",
        ),
    ]

    pickup_channel: Annotated[
        Optional["PickupChannel"],
        Field(
            None,
            validation_alias=AliasChoices("pickupChannel", "pickup_channel"),
            serialization_alias="pickupChannel",
        ),
    ]


"""
ServicesCapability

The services capability of a supply source.
"""


class ServicesCapability(SpApiBaseModel):
    """The services capability of a supply source."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    is_supported: Annotated[
        Optional[bool],
        Field(
            None,
            validation_alias=AliasChoices("isSupported", "is_supported"),
            serialization_alias="isSupported",
            description="When true, `SupplySource` supports the Service capability.",
        ),
    ]

    operational_configuration: Annotated[
        Optional["OperationalConfiguration"],
        Field(
            None,
            validation_alias=AliasChoices(
                "operationalConfiguration", "operational_configuration"
            ),
            serialization_alias="operationalConfiguration",
        ),
    ]


"""
SupplySourceCapabilities

The capabilities of a supply source.
"""


class SupplySourceCapabilities(SpApiBaseModel):
    """The capabilities of a supply source."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    outbound: Annotated[
        Optional["OutboundCapability"],
        Field(
            None,
        ),
    ]

    services: Annotated[
        Optional["ServicesCapability"],
        Field(
            None,
        ),
    ]


"""
SupplySourceConfiguration

Includes configuration and timezone of a supply source.
"""


class SupplySourceConfiguration(SpApiBaseModel):
    """Includes configuration and timezone of a supply source."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    operational_configuration: Annotated[
        Optional["OperationalConfiguration"],
        Field(
            None,
            validation_alias=AliasChoices(
                "operationalConfiguration", "operational_configuration"
            ),
            serialization_alias="operationalConfiguration",
        ),
    ]

    timezone: Annotated[
        Optional[str],
        Field(
            None,
            description="Please see RFC 6557, should be a canonical time zone ID as listed here: https://www.joda.org/joda-time/timezones.html.",
        ),
    ]


SupplySourceStatusReadOnly = str
"""The `SupplySource` status."""


"""
SupplySource

The supply source details, including configurations and capabilities.
"""


class SupplySource(SpApiBaseModel):
    """The supply source details, including configurations and capabilities."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    supply_source_id: Annotated[
        Optional["SupplySourceId"],
        Field(
            None,
            validation_alias=AliasChoices("supplySourceId", "supply_source_id"),
            serialization_alias="supplySourceId",
        ),
    ]

    supply_source_code: Annotated[
        Optional["SupplySourceCode"],
        Field(
            None,
            validation_alias=AliasChoices("supplySourceCode", "supply_source_code"),
            serialization_alias="supplySourceCode",
        ),
    ]

    alias: Annotated[
        Optional["SupplySourceAlias"],
        Field(
            None,
        ),
    ]

    status: Annotated[
        Optional["SupplySourceStatusReadOnly"],
        Field(
            None,
        ),
    ]

    address: Annotated[
        Optional["Address"],
        Field(
            None,
        ),
    ]

    configuration: Annotated[
        Optional["SupplySourceConfiguration"],
        Field(
            None,
        ),
    ]

    capabilities: Annotated[
        Optional["SupplySourceCapabilities"],
        Field(
            None,
        ),
    ]

    created_at: Annotated[
        Optional["DateTime"],
        Field(
            None,
            validation_alias=AliasChoices("createdAt", "created_at"),
            serialization_alias="createdAt",
        ),
    ]

    updated_at: Annotated[
        Optional["DateTime"],
        Field(
            None,
            validation_alias=AliasChoices("updatedAt", "updated_at"),
            serialization_alias="updatedAt",
        ),
    ]


SupplySourceStatus = str
"""The `SupplySource` status"""


"""
UpdateSupplySourceRequestBody

A request to update the configuration and capabilities of a supply source.
"""


class UpdateSupplySourceRequestBody(SpApiBaseModel):
    """A request to update the configuration and capabilities of a supply source."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    alias: Annotated[
        Optional["SupplySourceAlias"],
        Field(
            None,
        ),
    ]

    configuration: Annotated[
        Optional["SupplySourceConfiguration"],
        Field(
            None,
        ),
    ]

    capabilities: Annotated[
        Optional["SupplySourceCapabilities"],
        Field(
            None,
        ),
    ]


"""
UpdateSupplySourceRequest

Request parameters for updateSupplySource
"""


class UpdateSupplySourceRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for updateSupplySource
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    supply_source_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("supplySourceId", "supply_source_id"),
            serialization_alias="supplySourceId",
            description="[PATH] The unique identitier of a supply source.",
        ),
    ]

    payload: Annotated[
        Optional["UpdateSupplySourceRequestBody"],
        BodyParam(),
        Field(None, description="[BODY] Parameter"),
    ]


"""
UpdateSupplySourceStatusRequestBody

A request to update the status of a supply source.
"""


class UpdateSupplySourceStatusRequestBody(SpApiBaseModel):
    """A request to update the status of a supply source."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    status: Annotated[
        Optional["SupplySourceStatus"],
        Field(
            None,
        ),
    ]


"""
UpdateSupplySourceStatusRequest

Request parameters for updateSupplySourceStatus
"""


class UpdateSupplySourceStatusRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for updateSupplySourceStatus
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    supply_source_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("supplySourceId", "supply_source_id"),
            serialization_alias="supplySourceId",
            description="[PATH] The unique identifier of a supply source.",
        ),
    ]

    payload: Annotated[
        Optional["UpdateSupplySourceStatusRequestBody"],
        BodyParam(),
        Field(None, description="[BODY] Parameter"),
    ]


# Rebuild models to resolve forward references
Error.model_rebuild()
ErrorList.model_rebuild()
GetSupplySourcesResponse.model_rebuild()
UpdateSupplySourceStatusRequestBody.model_rebuild()
CreateSupplySourceRequestBody.model_rebuild()
CreateSupplySourceResponse.model_rebuild()
UpdateSupplySourceRequestBody.model_rebuild()
SupplySource.model_rebuild()
SupplySourceConfiguration.model_rebuild()
SupplySourceCapabilities.model_rebuild()
SupplySourceList.model_rebuild()
OutboundCapability.model_rebuild()
ServicesCapability.model_rebuild()
PickupChannel.model_rebuild()
ParkingConfiguration.model_rebuild()
InStorePickupConfiguration.model_rebuild()
CurbsidePickupConfiguration.model_rebuild()
ParkingWithAddressConfiguration.model_rebuild()
DeliveryChannel.model_rebuild()
OperationalConfiguration.model_rebuild()
Duration.model_rebuild()
ThroughputConfig.model_rebuild()
ReturnLocation.model_rebuild()
AddressWithContact.model_rebuild()
ContactDetails.model_rebuild()
ThroughputCap.model_rebuild()
OperatingHour.model_rebuild()
OperatingHoursByDay.model_rebuild()
Address.model_rebuild()
GetSupplySourcesRequest.model_rebuild()
CreateSupplySourceRequest.model_rebuild()
GetSupplySourceRequest.model_rebuild()
UpdateSupplySourceRequest.model_rebuild()
ArchiveSupplySourceRequest.model_rebuild()
UpdateSupplySourceStatusRequest.model_rebuild()
