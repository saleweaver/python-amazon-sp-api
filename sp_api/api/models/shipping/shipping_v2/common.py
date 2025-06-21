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

AccessPointId = str
"""Unique identifier for the access point"""


AccessPointType = str
"""The type of access point, like counter (HELIX), lockers, etc."""


"""
AccessibilityAttributes

Defines the accessibility details of the access point.
"""


class AccessibilityAttributes(SpApiBaseModel):
    """Defines the accessibility details of the access point."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    distance: Annotated[
        Optional[str],
        Field(
            None,
            description="The approximate distance of access point from input postalCode's centroid.",
        ),
    ]

    drive_time: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices("driveTime", "drive_time"),
            serialization_alias="driveTime",
            description="The approximate (static) drive time from input postal code's centroid.",
        ),
    ]


City = str
"""The city or town where the person, business or institution is located."""


CountryCode = str
"""The two digit country code. Follows ISO 3166-1 alpha-2 format."""


"""
Geocode

Defines the latitude and longitude of the access point.
"""


class Geocode(SpApiBaseModel):
    """Defines the latitude and longitude of the access point."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    latitude: Annotated[
        Optional[str], Field(None, description="The latitude of access point.")
    ]

    longitude: Annotated[
        Optional[str], Field(None, description="The longitude of access point.")
    ]


PostalCode = str
"""The postal code of that address. It contains a series of letters or digits or both, sometimes including spaces or punctuation."""


StateOrRegion = str
"""The state, county or region where the person, business or institution is located."""


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
            description="The name of the person, business or institution at the address.",
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

    company_name: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("companyName", "company_name"),
            serialization_alias="companyName",
            description="The name of the business or institution associated with the address.",
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

    phone_number: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("phoneNumber", "phone_number"),
            serialization_alias="phoneNumber",
            description="The phone number of the person, business or institution located at that address, including the country calling code.",
        ),
    ]

    geocode: Annotated[
        Optional["Geocode"],
        Field(
            None,
        ),
    ]


"""
DayOfWeekTimeMap

Map of day of the week to operating hours of that day
"""


class DayOfWeekTimeMap(SpApiBaseModel):
    """Map of day of the week to operating hours of that day"""

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow",
        serialize_by_alias=True,
        arbitrary_types_allowed=True,
    )


"""
DateRange

Date Range for query the results.
"""


class DateRange(SpApiBaseModel):
    """Date Range for query the results."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    start_date: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("startDate", "start_date"),
            serialization_alias="startDate",
            description="Start Date for query .",
        ),
    ]

    end_date: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("endDate", "end_date"),
            serialization_alias="endDate",
            description="end date for query.",
        ),
    ]


"""
TimeOfDay

Denotes time of the day, used for defining opening or closing time of access points
"""


class TimeOfDay(SpApiBaseModel):
    """Denotes time of the day, used for defining opening or closing time of access points"""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    hour_of_day: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices("hourOfDay", "hour_of_day"),
            serialization_alias="hourOfDay",
            description="Denotes hour of the day, used for defining opening or closing time of access points",
        ),
    ]

    minute_of_hour: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices("minuteOfHour", "minute_of_hour"),
            serialization_alias="minuteOfHour",
            description="Denotes minute of the hour, used for defining opening or closing time of access points",
        ),
    ]

    second_of_minute: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices("secondOfMinute", "second_of_minute"),
            serialization_alias="secondOfMinute",
            description="Denotes second of the minute, used for defining opening or closing time of access points",
        ),
    ]


"""
OperatingHours

The hours in which the access point shall remain operational
"""


class OperatingHours(SpApiBaseModel):
    """The hours in which the access point shall remain operational"""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    closing_time: Annotated[
        Optional["TimeOfDay"],
        Field(
            None,
            validation_alias=AliasChoices("closingTime", "closing_time"),
            serialization_alias="closingTime",
        ),
    ]

    opening_time: Annotated[
        Optional["TimeOfDay"],
        Field(
            None,
            validation_alias=AliasChoices("openingTime", "opening_time"),
            serialization_alias="openingTime",
        ),
    ]

    mid_day_closures: Annotated[
        Optional[List["TimeOfDay"]],
        Field(
            None,
            validation_alias=AliasChoices("midDayClosures", "mid_day_closures"),
            serialization_alias="midDayClosures",
            description="midDayClosures operating hours array",
        ),
    ]


"""
ExceptionOperatingHours

Defines exceptions to standard operating hours for certain date ranges.
"""


class ExceptionOperatingHours(SpApiBaseModel):
    """Defines exceptions to standard operating hours for certain date ranges."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    date_range: Annotated[
        Optional["DateRange"],
        Field(
            None,
            validation_alias=AliasChoices("dateRange", "date_range"),
            serialization_alias="dateRange",
        ),
    ]

    operating_hours: Annotated[
        Optional["OperatingHours"],
        Field(
            None,
            validation_alias=AliasChoices("operatingHours", "operating_hours"),
            serialization_alias="operatingHours",
        ),
    ]


# Enum definitions
class AssistanceTypeEnum(str, Enum):
    """Enum for assistanceType"""

    STAFF_ASSISTED = "STAFF_ASSISTED"
    SELF_ASSISTED = "SELF_ASSISTED"


"""
AccessPoint

Access point details
"""


class AccessPoint(SpApiBaseModel):
    """Access point details"""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    access_point_id: Annotated[
        Optional["AccessPointId"],
        Field(
            None,
            validation_alias=AliasChoices("accessPointId", "access_point_id"),
            serialization_alias="accessPointId",
        ),
    ]

    name: Annotated[
        Optional[str],
        Field(
            None,
            description="Name of entity (store/hub etc) where this access point is located",
        ),
    ]

    timezone: Annotated[
        Optional[str], Field(None, description="Timezone of access point")
    ]

    type: Annotated[
        Optional["AccessPointType"],
        Field(
            None,
        ),
    ]

    accessibility_attributes: Annotated[
        Optional["AccessibilityAttributes"],
        Field(
            None,
            validation_alias=AliasChoices(
                "accessibilityAttributes", "accessibility_attributes"
            ),
            serialization_alias="accessibilityAttributes",
        ),
    ]

    address: Annotated[
        Optional["Address"],
        Field(
            None,
        ),
    ]

    exception_operating_hours: Annotated[
        Optional[List["ExceptionOperatingHours"]],
        Field(
            None,
            validation_alias=AliasChoices(
                "exceptionOperatingHours", "exception_operating_hours"
            ),
            serialization_alias="exceptionOperatingHours",
            description="Exception operating hours for Access Point",
        ),
    ]

    assistance_type: Annotated[
        Optional[AssistanceTypeEnum],
        Field(
            None,
            validation_alias=AliasChoices("assistanceType", "assistance_type"),
            serialization_alias="assistanceType",
            description="Assistance type enum for Access point i.e. STAFF_ASSISTED or SELF_ASSISTED",
        ),
    ]

    score: Annotated[
        Optional[str],
        Field(
            None,
            description="The score of access point, based on proximity to postal code and sorting preference. This can be used to sort access point results on shipper's end.",
        ),
    ]

    standard_operating_hours: Annotated[
        Optional["DayOfWeekTimeMap"],
        Field(
            None,
            validation_alias=AliasChoices(
                "standardOperatingHours", "standard_operating_hours"
            ),
            serialization_alias="standardOperatingHours",
        ),
    ]


"""
AccessPointDetails

AccessPointDetails object
"""


class AccessPointDetails(SpApiBaseModel):
    """AccessPointDetails object"""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    access_point_id: Annotated[
        Optional["AccessPointId"],
        Field(
            None,
            validation_alias=AliasChoices("accessPointId", "access_point_id"),
            serialization_alias="accessPointId",
        ),
    ]


AccessPointList = List["AccessPoint"]
"""List of relevant Access points requested by shipper. These access points are sorted by proximity to postal code, and are limited to 40. We have internally defined a radius value to render relevant results."""


"""
AccessPointsMap

Map of type of access point to list of access points
"""


class AccessPointsMap(SpApiBaseModel):
    """Map of type of access point to list of access points"""

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow",
        serialize_by_alias=True,
        arbitrary_types_allowed=True,
    )


AccountId = str
"""Identifier for the seller's carrier account."""


AccountStatus = str
"""Account Status."""


AccountType = str
"""Shipper Account Type."""


CarrierId = str
"""The carrier identifier for the offering, provided by the carrier."""


"""
ActiveAccount

Active Account Details
"""


class ActiveAccount(SpApiBaseModel):
    """Active Account Details"""

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

    carrier_id: Annotated[
        Optional["CarrierId"],
        Field(
            None,
            validation_alias=AliasChoices("carrierId", "carrier_id"),
            serialization_alias="carrierId",
        ),
    ]


ActiveAccounts = List["ActiveAccount"]
"""A list of ActiveAccount"""


AdditionalAddressNotes = str
"""Address notes to re-attempt delivery with."""


AlternateLegTrackingId = str
"""The carrier generated reverse identifier for a returned package in a purchased shipment."""


"""
AmazonOrderDetails

Amazon order information. This is required if the shipment source channel is Amazon.
"""


class AmazonOrderDetails(SpApiBaseModel):
    """Amazon order information. This is required if the shipment source channel is Amazon."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    order_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("orderId", "order_id"),
            serialization_alias="orderId",
            description="The Amazon order ID associated with the Amazon order fulfilled by this shipment.",
        ),
    ]


"""
AmazonShipmentDetails

Amazon shipment information.
"""


class AmazonShipmentDetails(SpApiBaseModel):
    """Amazon shipment information."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    shipment_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("shipmentId", "shipment_id"),
            serialization_alias="shipmentId",
            description="This attribute is required only for a Direct Fulfillment shipment. This is the encrypted shipment ID.",
        ),
    ]


"""
Currency

The monetary value in the currency indicated, in ISO 4217 standard format.
"""


class Currency(SpApiBaseModel):
    """The monetary value in the currency indicated, in ISO 4217 standard format."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    value: Annotated[float, Field(..., description="The monetary value.")]

    unit: Annotated[
        str, Field(..., description="The ISO 4217 format 3-character currency code.")
    ]


"""
ValueAddedService

A value-added service available for purchase with a shipment service offering.
"""


class ValueAddedService(SpApiBaseModel):
    """A value-added service available for purchase with a shipment service offering."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    id: Annotated[
        str, Field(..., description="The identifier for the value-added service.")
    ]

    name: Annotated[str, Field(..., description="The name of the value-added service.")]

    cost: Annotated[
        "Currency", Field(..., description="The cost of the value-added service.")
    ]


"""
AvailableValueAddedServiceGroup

The value-added services available for purchase with a shipping service offering.
"""


class AvailableValueAddedServiceGroup(SpApiBaseModel):
    """The value-added services available for purchase with a shipping service offering."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    group_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("groupId", "group_id"),
            serialization_alias="groupId",
            description="The type of the value-added service group.",
        ),
    ]

    group_description: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("groupDescription", "group_description"),
            serialization_alias="groupDescription",
            description="The name of the value-added service group.",
        ),
    ]

    is_required: Annotated[
        bool,
        Field(
            ...,
            validation_alias=AliasChoices("isRequired", "is_required"),
            serialization_alias="isRequired",
            description="When true, one or more of the value-added services listed must be specified.",
        ),
    ]

    value_added_services: Annotated[
        Optional[List["ValueAddedService"]],
        Field(
            None,
            validation_alias=AliasChoices("valueAddedServices", "value_added_services"),
            serialization_alias="valueAddedServices",
            description="A list of optional value-added services available for purchase with a shipping service offering.",
        ),
    ]


AvailableValueAddedServiceGroupList = List["AvailableValueAddedServiceGroup"]
"""A list of value-added services available for a shipping service offering."""


ExcludedBenefits = List["ExcludedBenefit"]
"""A list of excluded benefit. Refer to the ExcludeBenefit object for further documentation"""


"""
IncludedBenefits

A list of included benefits.
"""


class IncludedBenefits(SpApiBaseModel):
    """A list of included benefits."""

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow",
        serialize_by_alias=True,
        arbitrary_types_allowed=True,
    )


"""
Benefits

Benefits that are included and excluded for each shipping offer. Benefits represents services provided by Amazon (eg. CLAIMS_PROTECTED, etc.) when sellers purchase shipping through Amazon. Benefit details will be made available for any shipment placed on or after January 1st 2024 00:00 UTC.
"""


class Benefits(SpApiBaseModel):
    """Benefits that are included and excluded for each shipping offer. Benefits represents services provided by Amazon (eg. CLAIMS_PROTECTED, etc.) when sellers purchase shipping through Amazon. Benefit details will be made available for any shipment placed on or after January 1st 2024 00:00 UTC."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    included_benefits: Annotated[
        "IncludedBenefits",
        Field(
            ...,
            validation_alias=AliasChoices("includedBenefits", "included_benefits"),
            serialization_alias="includedBenefits",
        ),
    ]

    excluded_benefits: Annotated[
        "ExcludedBenefits",
        Field(
            ...,
            validation_alias=AliasChoices("excludedBenefits", "excluded_benefits"),
            serialization_alias="excludedBenefits",
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
            description="[PATH] The shipment identifier originally returned by the purchaseShipment operation.",
        ),
    ]


"""
CancelShipmentResult

The payload for the cancelShipment operation.
"""


class CancelShipmentResult(SpApiBaseModel):
    """The payload for the cancelShipment operation."""

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow",
        serialize_by_alias=True,
        arbitrary_types_allowed=True,
    )


"""
CancelShipmentResponse

Response schema for the cancelShipment operation.
"""


class CancelShipmentResponse(SpApiBaseModel):
    """Response schema for the cancelShipment operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["CancelShipmentResult"],
        Field(
            None,
        ),
    ]


CarrierName = str
"""The carrier name for the offering."""


"""
Carrier

Carrier Related Info
"""


class Carrier(SpApiBaseModel):
    """Carrier Related Info"""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    id: Annotated[
        "CarrierId",
        Field(
            ...,
        ),
    ]

    name: Annotated[
        "CarrierName",
        Field(
            ...,
        ),
    ]


"""
CarrierAccount

Carrier Account details used to fetch rates.
"""


class CarrierAccount(SpApiBaseModel):
    """Carrier Account details used to fetch rates."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    carrier_account_id: Annotated[
        "AccountId",
        Field(
            ...,
            validation_alias=AliasChoices("carrierAccountId", "carrier_account_id"),
            serialization_alias="carrierAccountId",
        ),
    ]

    carrier_id: Annotated[
        "CarrierId",
        Field(
            ...,
            validation_alias=AliasChoices("carrierId", "carrier_id"),
            serialization_alias="carrierId",
        ),
    ]


"""
CarrierAccountAttribute

Attribute Properties required by carrier
"""


class CarrierAccountAttribute(SpApiBaseModel):
    """Attribute Properties required by carrier"""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    attribute_name: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("attributeName", "attribute_name"),
            serialization_alias="attributeName",
            description="Attribute Name .",
        ),
    ]

    property_group: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("propertyGroup", "property_group"),
            serialization_alias="propertyGroup",
            description="Property Group.",
        ),
    ]

    value: Annotated[Optional[str], Field(None, description="Value .")]


CarrierAccountAttributes = List["CarrierAccountAttribute"]
"""A list of all attributes required by the carrier in order to successfully link the merchant's account"""


InputType = str
"""Type of Input."""


ValidationMetadataList = List["ValidationMetadata"]
"""A list of ValidationMetadata"""


"""
CarrierAccountInput

Info About CarrierAccountInput
"""


class CarrierAccountInput(SpApiBaseModel):
    """Info About CarrierAccountInput"""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    description_localization_key: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "descriptionLocalizationKey", "description_localization_key"
            ),
            serialization_alias="descriptionLocalizationKey",
            description="descriptionLocalizationKey value .",
        ),
    ]

    name: Annotated[Optional[str], Field(None, description="name value .")]

    group_name: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("groupName", "group_name"),
            serialization_alias="groupName",
            description="groupName value .",
        ),
    ]

    input_type: Annotated[
        Optional["InputType"],
        Field(
            None,
            validation_alias=AliasChoices("inputType", "input_type"),
            serialization_alias="inputType",
        ),
    ]

    is_mandatory: Annotated[
        Optional[bool],
        Field(
            None,
            validation_alias=AliasChoices("isMandatory", "is_mandatory"),
            serialization_alias="isMandatory",
            description="mandatory or not value .",
        ),
    ]

    is_confidential: Annotated[
        Optional[bool],
        Field(
            None,
            validation_alias=AliasChoices("isConfidential", "is_confidential"),
            serialization_alias="isConfidential",
            description="is value is Confidential .",
        ),
    ]

    is_hidden: Annotated[
        Optional[bool],
        Field(
            None,
            validation_alias=AliasChoices("isHidden", "is_hidden"),
            serialization_alias="isHidden",
            description="is value is hidden .",
        ),
    ]

    validation_metadata: Annotated[
        Optional["ValidationMetadataList"],
        Field(
            None,
            validation_alias=AliasChoices("validationMetadata", "validation_metadata"),
            serialization_alias="validationMetadata",
        ),
    ]


CarrierAccountInputsList = List["CarrierAccountInput"]
"""A list of CarrierAccountInput"""


CarrierAccountType = str
"""CarrierAccountType associated with account."""


CarrierAccounts = List["CarrierAccount"]
"""A list of CarrierAccounts"""


ChannelType = str
"""The shipment source channel type."""


"""
ChannelDetails

Shipment source channel related information.
"""


class ChannelDetails(SpApiBaseModel):
    """Shipment source channel related information."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    channel_type: Annotated[
        "ChannelType",
        Field(
            ...,
            validation_alias=AliasChoices("channelType", "channel_type"),
            serialization_alias="channelType",
        ),
    ]

    amazon_order_details: Annotated[
        Optional["AmazonOrderDetails"],
        Field(
            None,
            validation_alias=AliasChoices("amazonOrderDetails", "amazon_order_details"),
            serialization_alias="amazonOrderDetails",
        ),
    ]

    amazon_shipment_details: Annotated[
        Optional["AmazonShipmentDetails"],
        Field(
            None,
            validation_alias=AliasChoices(
                "amazonShipmentDetails", "amazon_shipment_details"
            ),
            serialization_alias="amazonShipmentDetails",
        ),
    ]


# Enum definitions
class ChargeTypeEnum(str, Enum):
    """Enum for chargeType"""

    TAX = "TAX"  # A tax imposed on a package.
    DISCOUNT = "DISCOUNT"  # A discount deducted from the cost of a package.


"""
ChargeComponent

The type and amount of a charge applied on a package.
"""


class ChargeComponent(SpApiBaseModel):
    """The type and amount of a charge applied on a package."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    amount: Annotated[
        Optional["Currency"],
        Field(
            None,
        ),
    ]

    charge_type: Annotated[
        Optional[ChargeTypeEnum],
        Field(
            None,
            validation_alias=AliasChoices("chargeType", "charge_type"),
            serialization_alias="chargeType",
            description="The type of charge.",
        ),
    ]


ChargeList = List["ChargeComponent"]
"""A list of charges based on the shipping service charges applied on a package."""


ClaimId = str
"""The claim identifier originally returned by the createClaim operation."""


"""
ClaimProofURLs

A list of proof URLs for a claim. Basic URL validation will happen for each URLs present in the list
"""


class ClaimProofURLs(SpApiBaseModel):
    """A list of proof URLs for a claim. Basic URL validation will happen for each URLs present in the list"""

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow",
        serialize_by_alias=True,
        arbitrary_types_allowed=True,
    )


ClaimReason = str
"""The reason for which shipper is filing the claim for a particular shipment."""


# Enum definitions
class ClientReferenceTypeEnum(str, Enum):
    """Enum for clientReferenceType"""

    INTEGRATOR_SHIPPER_ID = "IntegratorShipperId"  # The unique identifier assigned to a 3P seller by the shipping integrator.
    INTEGRATOR_MERCHANT_ID = "IntegratorMerchantId"  # The unique identifier assigned to a 3P shipping integrator by Amazon.


"""
ClientReferenceDetail

Client Reference Details
"""


class ClientReferenceDetail(SpApiBaseModel):
    """Client Reference Details"""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    client_reference_type: Annotated[
        ClientReferenceTypeEnum,
        Field(
            ...,
            validation_alias=AliasChoices(
                "clientReferenceType", "client_reference_type"
            ),
            serialization_alias="clientReferenceType",
            description="Client Reference type.",
        ),
    ]

    client_reference_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("clientReferenceId", "client_reference_id"),
            serialization_alias="clientReferenceId",
            description="The Client Reference Id.",
        ),
    ]


ClientReferenceDetails = List["ClientReferenceDetail"]
"""Object to pass additional information about the MCI Integrator shipperType: List of ClientReferenceDetail"""


"""
CollectOnDelivery

The amount to collect on delivery.
"""


class CollectOnDelivery(SpApiBaseModel):
    """The amount to collect on delivery."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    amount: Annotated[
        "Currency",
        Field(
            ...,
        ),
    ]


CollectionFormId = str
"""Collection Form Id for Reprint ."""


GenerationStatus = str
"""Generation Status."""


"""
CollectionFormsHistoryRecord

Active Account Details
"""


class CollectionFormsHistoryRecord(SpApiBaseModel):
    """Active Account Details"""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    carrier_name: Annotated[
        Optional["CarrierName"],
        Field(
            None,
            validation_alias=AliasChoices("carrierName", "carrier_name"),
            serialization_alias="carrierName",
        ),
    ]

    creation_date: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("creationDate", "creation_date"),
            serialization_alias="creationDate",
            description="Creation Time for this account.",
        ),
    ]

    generation_status: Annotated[
        Optional["GenerationStatus"],
        Field(
            None,
            validation_alias=AliasChoices("generationStatus", "generation_status"),
            serialization_alias="generationStatus",
        ),
    ]

    collection_form_id: Annotated[
        Optional["CollectionFormId"],
        Field(
            None,
            validation_alias=AliasChoices("collectionFormId", "collection_form_id"),
            serialization_alias="collectionFormId",
        ),
    ]

    ship_from_address: Annotated[
        Optional["Address"],
        Field(
            None,
            validation_alias=AliasChoices("shipFromAddress", "ship_from_address"),
            serialization_alias="shipFromAddress",
        ),
    ]


CollectionFormsHistoryRecordList = List["CollectionFormsHistoryRecord"]
"""A list of CollectionFormsHistoryRecord"""


"""
CollectionsFormDocument

Collection Form Document Details
"""


class CollectionsFormDocument(SpApiBaseModel):
    """Collection Form Document Details"""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    base64_encoded_content: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "base64EncodedContent", "base64_encoded_content"
            ),
            serialization_alias="base64EncodedContent",
            description="Base64 document Value of Collection.",
        ),
    ]

    document_format: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("documentFormat", "document_format"),
            serialization_alias="documentFormat",
            description="Collection Document format is PDF.",
        ),
    ]


Contents = str
"""A Base64 encoded string of the file contents."""


SettlementType = str
"""Type of settlement the shipper wants to receive for a particular shipment."""


TrackingId = str
"""The carrier generated identifier for a package in a purchased shipment."""


"""
CreateClaimRequestBody

The request schema for the CreateClaim operation
"""


class CreateClaimRequestBody(SpApiBaseModel):
    """The request schema for the CreateClaim operation"""

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

    declared_value: Annotated[
        Optional["Currency"],
        Field(
            None,
            validation_alias=AliasChoices("declaredValue", "declared_value"),
            serialization_alias="declaredValue",
            description="This is required for off-Amazon shipments to determine value of shipments",
        ),
    ]

    claim_reason: Annotated[
        "ClaimReason",
        Field(
            ...,
            validation_alias=AliasChoices("claimReason", "claim_reason"),
            serialization_alias="claimReason",
        ),
    ]

    is_replacement_package_sent: Annotated[
        Optional[bool],
        Field(
            None,
            validation_alias=AliasChoices(
                "isReplacementPackageSent", "is_replacement_package_sent"
            ),
            serialization_alias="isReplacementPackageSent",
            description="Applicable for only On Amazon shipments to identify if replacement was sent",
        ),
    ]

    proofs: Annotated[
        Optional["ClaimProofURLs"],
        Field(
            None,
        ),
    ]

    settlement_type: Annotated[
        "SettlementType",
        Field(
            ...,
            validation_alias=AliasChoices("settlementType", "settlement_type"),
            serialization_alias="settlementType",
        ),
    ]


"""
CreateClaimRequest

Request parameters for createClaim
"""


class CreateClaimRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for createClaim
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    body: Annotated[
        "CreateClaimRequestBody",
        BodyParam(),
        Field(..., description="[BODY] RequestBody body for the createClaim operation"),
    ]


"""
CreateClaimResponse

The response schema for the createClaim operation.
"""


class CreateClaimResponse(SpApiBaseModel):
    """The response schema for the createClaim operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    claim_id: Annotated[
        Optional["ClaimId"],
        Field(
            None,
            validation_alias=AliasChoices("claimId", "claim_id"),
            serialization_alias="claimId",
        ),
    ]


# Enum definitions
class PackingGroupEnum(str, Enum):
    """Enum for packingGroup"""

    I = "I"  # Packing group I indicates great danger.
    II = "II"  # Packing group II indicates medium danger.
    III = "III"  # Packing group III indicates minor danger.


class PackingInstructionEnum(str, Enum):
    """Enum for packingInstruction"""

    PI965_SECTION_IA = "PI965_SECTION_IA"  # Ion PI965 Section IA (LiBa)
    PI965_SECTION_IB = "PI965_SECTION_IB"  # Ion PI965 Section IB (LiBa)
    PI965_SECTION_II = "PI965_SECTION_II"  # Ion PI965 Section II (LiBa)
    PI966_SECTION_I = "PI966_SECTION_I"  # Ion PI966 Section I (LiBa with equipment)
    PI966_SECTION_II = "PI966_SECTION_II"  # Ion PI966 Section II (LiBa with equipment)
    PI967_SECTION_I = "PI967_SECTION_I"  # Ion PI967 Section I (LiBa in equipment)
    PI967_SECTION_II = "PI967_SECTION_II"  # Ion PI967 Section II (LiBa in equipment)
    PI968_SECTION_IA = "PI968_SECTION_IA"  # Metal PI968 Section IA (LiBa)
    PI968_SECTION_IB = "PI968_SECTION_IB"  # Metal PI968 Section IB (LiBa)
    PI969_SECTION_I = "PI969_SECTION_I"  # Metal PI969 Section I (LiBa with equipment)
    PI969_SECTION_II = (
        "PI969_SECTION_II"  # Metal PI969 Section II (LiBa with equipment)
    )
    PI970_SECTION_I = "PI970_SECTION_I"  # Metal PI970 Section I (LiBa in equipment)
    PI970_SECTION_II = "PI970_SECTION_II"  # Metal PI970 Section II (LiBa in equipment)


"""
DangerousGoodsDetails

Details related to any dangerous goods/items that are being shipped.
"""


class DangerousGoodsDetails(SpApiBaseModel):
    """Details related to any dangerous goods/items that are being shipped."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    united_nations_regulatory_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "unitedNationsRegulatoryId", "united_nations_regulatory_id"
            ),
            serialization_alias="unitedNationsRegulatoryId",
            description="The specific UNID of the item being shipped.",
        ),
    ]

    transportation_regulatory_class: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "transportationRegulatoryClass", "transportation_regulatory_class"
            ),
            serialization_alias="transportationRegulatoryClass",
            description="The specific regulatory class of the item being shipped.",
        ),
    ]

    packing_group: Annotated[
        Optional[PackingGroupEnum],
        Field(
            None,
            validation_alias=AliasChoices("packingGroup", "packing_group"),
            serialization_alias="packingGroup",
            description="The specific packaging group of the item being shipped.",
        ),
    ]

    packing_instruction: Annotated[
        Optional[PackingInstructionEnum],
        Field(
            None,
            validation_alias=AliasChoices("packingInstruction", "packing_instruction"),
            serialization_alias="packingInstruction",
            description="The specific packing instruction of the item being shipped.",
        ),
    ]


DetailCodes = str
"""A list of codes used to provide additional shipment information."""


# Enum definitions
class UnitEnum(str, Enum):
    """Enum for unit"""

    INCH = "INCH"  # The imperial unit of length equal to one twelfth of a foot.
    CENTIMETER = (
        "CENTIMETER"  # A metric unit of length, equal to one hundredth of a meter.
    )


"""
Dimensions

A set of measurements for a three-dimensional object.
"""


class Dimensions(SpApiBaseModel):
    """A set of measurements for a three-dimensional object."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    length: Annotated[float, Field(..., description="The length of the package.")]

    width: Annotated[float, Field(..., description="The width of the package.")]

    height: Annotated[float, Field(..., description="The height of the package.")]

    unit: Annotated[UnitEnum, Field(..., description="The unit of measurement.")]


"""
DirectFulfillmentItemIdentifiers

Item identifiers for an item in a direct fulfillment shipment.
"""


class DirectFulfillmentItemIdentifiers(SpApiBaseModel):
    """Item identifiers for an item in a direct fulfillment shipment."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    line_item_i_d: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("lineItemID", "line_item_i_d"),
            serialization_alias="lineItemID",
            description="A unique identifier for an item provided by the client for a direct fulfillment shipment. This is only populated for direct fulfillment multi-piece shipments. It is required if a vendor wants to change the configuration of the packages in which the purchase order is shipped.",
        ),
    ]

    piece_number: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("pieceNumber", "piece_number"),
            serialization_alias="pieceNumber",
            description="A unique identifier for an item provided by the client for a direct fulfillment shipment. This is only populated if a single line item has multiple pieces. Defaults to 1.",
        ),
    ]


PackageList = List["Package"]
"""A list of packages to be shipped through a shipping service offering."""


DocumentFormat = str
"""The file format of the document."""


# Enum definitions
class UnitEnum(str, Enum):
    """Enum for unit"""

    INCH = "INCH"  # The imperial unit of length equal to one twelfth of a foot.
    CENTIMETER = (
        "CENTIMETER"  # A metric unit of length, equal to one hundredth of a meter.
    )


"""
DocumentSize

The size dimensions of the label.
"""


class DocumentSize(SpApiBaseModel):
    """The size dimensions of the label."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    width: Annotated[
        float,
        Field(
            ...,
            description="The width of the document measured in the units specified.",
        ),
    ]

    length: Annotated[
        float,
        Field(
            ...,
            description="The length of the document measured in the units specified.",
        ),
    ]

    unit: Annotated[UnitEnum, Field(..., description="The unit of measurement.")]


DocumentType = str
"""The type of shipping document."""


Dpi = int
"""The dots per inch (DPI) value used in printing. This value represents a measure of the resolution of the document."""


NeedFileJoining = bool
"""When true, files should be stitched together. Otherwise, files should be returned separately. Defaults to false."""


PageLayout = str
"""Indicates the position of the label on the paper. Should be the same value as returned in getRates response."""


RequestAttributes = List["LabelAttribute"]
"""Specify the type of attributes to be added on a label."""


"""
RequestedLabelCustomization

Object contains customised data requested by a shipper to be printed on a shipping label.
"""


class RequestedLabelCustomization(SpApiBaseModel):
    """Object contains customised data requested by a shipper to be printed on a shipping label."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    request_attributes: Annotated[
        Optional["RequestAttributes"],
        Field(
            None,
            validation_alias=AliasChoices("requestAttributes", "request_attributes"),
            serialization_alias="requestAttributes",
        ),
    ]


"""
RequestedDocumentSpecification

The document specifications requested. For calls to the purchaseShipment operation, the shipment purchase fails if the specified document specifications are not among those returned in the response to the getRates operation.
"""


class RequestedDocumentSpecification(SpApiBaseModel):
    """The document specifications requested. For calls to the purchaseShipment operation, the shipment purchase fails if the specified document specifications are not among those returned in the response to the getRates operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    format: Annotated[
        "DocumentFormat",
        Field(
            ...,
        ),
    ]

    size: Annotated[
        "DocumentSize",
        Field(
            ...,
        ),
    ]

    dpi: Annotated[
        Optional["Dpi"],
        Field(
            None,
        ),
    ]

    page_layout: Annotated[
        Optional["PageLayout"],
        Field(
            None,
            validation_alias=AliasChoices("pageLayout", "page_layout"),
            serialization_alias="pageLayout",
        ),
    ]

    need_file_joining: Annotated[
        "NeedFileJoining",
        Field(
            ...,
            validation_alias=AliasChoices("needFileJoining", "need_file_joining"),
            serialization_alias="needFileJoining",
        ),
    ]

    requested_document_types: Annotated[
        List["DocumentType"],
        Field(
            ...,
            validation_alias=AliasChoices(
                "requestedDocumentTypes", "requested_document_types"
            ),
            serialization_alias="requestedDocumentTypes",
            description="A list of the document types requested.",
        ),
    ]

    requested_label_customization: Annotated[
        Optional["RequestedLabelCustomization"],
        Field(
            None,
            validation_alias=AliasChoices(
                "requestedLabelCustomization", "requested_label_customization"
            ),
            serialization_alias="requestedLabelCustomization",
        ),
    ]


"""
DirectPurchaseRequestBody

The request schema for the directPurchaseShipment operation. When the channel type is Amazon, the shipTo address is not required and will be ignored.
"""


class DirectPurchaseRequestBody(SpApiBaseModel):
    """The request schema for the directPurchaseShipment operation. When the channel type is Amazon, the shipTo address is not required and will be ignored."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    ship_to: Annotated[
        Optional["Address"],
        Field(
            None,
            validation_alias=AliasChoices("shipTo", "ship_to"),
            serialization_alias="shipTo",
            description="The address where the shipment will be delivered. For vendor orders, shipTo information is pulled directly from the Amazon order.",
        ),
    ]

    ship_from: Annotated[
        Optional["Address"],
        Field(
            None,
            validation_alias=AliasChoices("shipFrom", "ship_from"),
            serialization_alias="shipFrom",
            description="The address where the package will be picked up.",
        ),
    ]

    return_to: Annotated[
        Optional["Address"],
        Field(
            None,
            validation_alias=AliasChoices("returnTo", "return_to"),
            serialization_alias="returnTo",
            description="The address where the package will be returned if it cannot be delivered.",
        ),
    ]

    packages: Annotated[
        Optional["PackageList"],
        Field(
            None,
        ),
    ]

    channel_details: Annotated[
        "ChannelDetails",
        Field(
            ...,
            validation_alias=AliasChoices("channelDetails", "channel_details"),
            serialization_alias="channelDetails",
        ),
    ]

    label_specifications: Annotated[
        Optional["RequestedDocumentSpecification"],
        Field(
            None,
            validation_alias=AliasChoices(
                "labelSpecifications", "label_specifications"
            ),
            serialization_alias="labelSpecifications",
            description="The document (label) specifications requested. The default label returned is PNG DPI 203 4x6 if no label specification is provided. Requesting an invalid file format results in a failure.",
        ),
    ]


PackageDocumentDetailList = List["PackageDocumentDetail"]
"""A list of post-purchase details about a package that will be shipped using a shipping service."""


ShipmentId = str
"""The unique shipment identifier provided by a shipping service."""


"""
DirectPurchaseResult

The payload for the directPurchaseShipment operation.
"""


class DirectPurchaseResult(SpApiBaseModel):
    """The payload for the directPurchaseShipment operation."""

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

    package_document_detail_list: Annotated[
        Optional["PackageDocumentDetailList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "packageDocumentDetailList", "package_document_detail_list"
            ),
            serialization_alias="packageDocumentDetailList",
        ),
    ]


"""
DirectPurchaseResponse

The response schema for the directPurchaseShipment operation.
"""


class DirectPurchaseResponse(SpApiBaseModel):
    """The response schema for the directPurchaseShipment operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["DirectPurchaseResult"],
        Field(
            None,
        ),
    ]


"""
DirectPurchaseShipmentRequest

Request parameters for directPurchaseShipment
"""


class DirectPurchaseShipmentRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for directPurchaseShipment
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    body: Annotated[
        "DirectPurchaseRequestBody",
        BodyParam(),
        Field(..., description="[BODY] DirectPurchaseRequestBody body"),
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

    errors: Annotated[List["Error"], Field(..., description="Array of Errors")]


EventCode = str
"""The tracking event type."""


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


ShipmentType = str
"""Shipment type."""


"""
Event

A tracking event.
"""


class Event(SpApiBaseModel):
    """A tracking event."""

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

    location: Annotated[
        Optional["Location"],
        Field(
            None,
        ),
    ]

    event_time: Annotated[
        datetime,
        Field(
            ...,
            validation_alias=AliasChoices("eventTime", "event_time"),
            serialization_alias="eventTime",
            description="The ISO 8601 formatted timestamp of the event.",
        ),
    ]

    shipment_type: Annotated[
        Optional["ShipmentType"],
        Field(
            None,
            validation_alias=AliasChoices("shipmentType", "shipment_type"),
            serialization_alias="shipmentType",
        ),
    ]


"""
ExcludedBenefitReasonCodes

List of reasons (eg. LATE_DELIVERY_RISK, etc.) indicating why a benefit is excluded for a shipping offer.
"""


class ExcludedBenefitReasonCodes(SpApiBaseModel):
    """List of reasons (eg. LATE_DELIVERY_RISK, etc.) indicating why a benefit is excluded for a shipping offer."""

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow",
        serialize_by_alias=True,
        arbitrary_types_allowed=True,
    )


"""
ExcludedBenefit

Object representing a benefit that is excluded for a shipping offer or rate.
"""


class ExcludedBenefit(SpApiBaseModel):
    """Object representing a benefit that is excluded for a shipping offer or rate."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    benefit: Annotated[str, Field(..., description="benefit")]

    reason_codes: Annotated[
        Optional["ExcludedBenefitReasonCodes"],
        Field(
            None,
            validation_alias=AliasChoices("reasonCodes", "reason_codes"),
            serialization_alias="reasonCodes",
        ),
    ]


"""
GenerateCollectionFormRequestBody

The request schema Call to generate the collection form.
"""


class GenerateCollectionFormRequestBody(SpApiBaseModel):
    """The request schema Call to generate the collection form."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    client_reference_details: Annotated[
        Optional["ClientReferenceDetails"],
        Field(
            None,
            validation_alias=AliasChoices(
                "clientReferenceDetails", "client_reference_details"
            ),
            serialization_alias="clientReferenceDetails",
        ),
    ]

    carrier_id: Annotated[
        "CarrierId",
        Field(
            ...,
            validation_alias=AliasChoices("carrierId", "carrier_id"),
            serialization_alias="carrierId",
        ),
    ]

    ship_from_address: Annotated[
        Optional["Address"],
        Field(
            None,
            validation_alias=AliasChoices("shipFromAddress", "ship_from_address"),
            serialization_alias="shipFromAddress",
        ),
    ]


"""
GenerateCollectionFormRequest

Request parameters for generateCollectionForm
"""


class GenerateCollectionFormRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for generateCollectionForm
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    body: Annotated[
        "GenerateCollectionFormRequestBody",
        BodyParam(),
        Field(..., description="[BODY] GenerateCollectionFormRequestBody body"),
    ]


"""
GenerateCollectionFormResponse

The Response for the GenerateCollectionFormResponse operation.
"""


class GenerateCollectionFormResponse(SpApiBaseModel):
    """The Response for the GenerateCollectionFormResponse operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    collections_form_document: Annotated[
        Optional["CollectionsFormDocument"],
        Field(
            None,
            validation_alias=AliasChoices(
                "collectionsFormDocument", "collections_form_document"
            ),
            serialization_alias="collectionsFormDocument",
        ),
    ]


# Enum definitions
class AccessPointTypesEnum(str, Enum):
    """Enum for accessPointTypes"""

    HELIX = "HELIX"
    CAMPUS_LOCKER = "CAMPUS_LOCKER"
    OMNI_LOCKER = "OMNI_LOCKER"
    ODIN_LOCKER = "ODIN_LOCKER"
    DOBBY_LOCKER = "DOBBY_LOCKER"
    CORE_LOCKER = "CORE_LOCKER"
    VALUE_3_P = "3P"
    CAMPUS_ROOM = "CAMPUS_ROOM"


"""
GetAccessPointsRequest

Request parameters for getAccessPoints
"""


class GetAccessPointsRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getAccessPoints
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    access_point_types: Annotated[
        List["AccessPointTypesEnum"],
        QueryParam(),
        Field(
            ...,
            validation_alias=AliasChoices("accessPointTypes", "access_point_types"),
            serialization_alias="accessPointTypes",
            description="[QUERY] Access point types",
        ),
    ]

    country_code: Annotated[
        str,
        QueryParam(),
        Field(
            ...,
            validation_alias=AliasChoices("countryCode", "country_code"),
            serialization_alias="countryCode",
            description="[QUERY] Country code for access point",
        ),
    ]

    postal_code: Annotated[
        str,
        QueryParam(),
        Field(
            ...,
            validation_alias=AliasChoices("postalCode", "postal_code"),
            serialization_alias="postalCode",
            description="[QUERY] postal code for access point",
        ),
    ]


"""
GetAccessPointsResult

The payload for the GetAccessPoints API.
"""


class GetAccessPointsResult(SpApiBaseModel):
    """The payload for the GetAccessPoints API."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    access_points_map: Annotated[
        "AccessPointsMap",
        Field(
            ...,
            validation_alias=AliasChoices("accessPointsMap", "access_points_map"),
            serialization_alias="accessPointsMap",
        ),
    ]


"""
GetAccessPointsResponse

The response schema for the GetAccessPoints operation.
"""


class GetAccessPointsResponse(SpApiBaseModel):
    """The response schema for the GetAccessPoints operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["GetAccessPointsResult"],
        Field(
            None,
        ),
    ]


"""
GetAdditionalInputsRequest

Request parameters for getAdditionalInputs
"""


class GetAdditionalInputsRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getAdditionalInputs
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    request_token: Annotated[
        str,
        QueryParam(),
        Field(
            ...,
            validation_alias=AliasChoices("requestToken", "request_token"),
            serialization_alias="requestToken",
            description="[QUERY] The request token returned in the response to the getRates operation.",
        ),
    ]

    rate_id: Annotated[
        str,
        QueryParam(),
        Field(
            ...,
            validation_alias=AliasChoices("rateId", "rate_id"),
            serialization_alias="rateId",
            description="[QUERY] The rate identifier for the shipping offering (rate) returned in the response to the getRates operation.",
        ),
    ]


"""
GetAdditionalInputsResult

The JSON schema to use to provide additional inputs when required to purchase a shipping offering.
"""


class GetAdditionalInputsResult(SpApiBaseModel):
    """The JSON schema to use to provide additional inputs when required to purchase a shipping offering."""

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow",
        serialize_by_alias=True,
        arbitrary_types_allowed=True,
    )


"""
GetAdditionalInputsResponse

The response schema for the getAdditionalInputs operation.
"""


class GetAdditionalInputsResponse(SpApiBaseModel):
    """The response schema for the getAdditionalInputs operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["GetAdditionalInputsResult"],
        Field(
            None,
        ),
    ]


LinkableCarriersList = List["LinkableCarrier"]
"""A list of LinkableCarrier"""


"""
GetCarrierAccountFormInputsResponse

The Response for the GetCarrierAccountFormInputsResponse operation.
"""


class GetCarrierAccountFormInputsResponse(SpApiBaseModel):
    """The Response for the GetCarrierAccountFormInputsResponse operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    linkable_carriers_list: Annotated[
        Optional["LinkableCarriersList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "linkableCarriersList", "linkable_carriers_list"
            ),
            serialization_alias="linkableCarriersList",
        ),
    ]


"""
GetCarrierAccountsRequestBody

The request schema for the GetCarrierAccounts operation.
"""


class GetCarrierAccountsRequestBody(SpApiBaseModel):
    """The request schema for the GetCarrierAccounts operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    client_reference_details: Annotated[
        Optional["ClientReferenceDetails"],
        Field(
            None,
            validation_alias=AliasChoices(
                "clientReferenceDetails", "client_reference_details"
            ),
            serialization_alias="clientReferenceDetails",
        ),
    ]


"""
GetCarrierAccountsRequest

Request parameters for getCarrierAccounts
"""


class GetCarrierAccountsRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getCarrierAccounts
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    body: Annotated[
        "GetCarrierAccountsRequestBody",
        BodyParam(),
        Field(..., description="[BODY] GetCarrierAccountsRequestBody body"),
    ]


"""
GetCarrierAccountsResponse

The Response for the GetCarrierAccountsResponse operation.
"""


class GetCarrierAccountsResponse(SpApiBaseModel):
    """The Response for the GetCarrierAccountsResponse operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    active_accounts: Annotated[
        "ActiveAccounts",
        Field(
            ...,
            validation_alias=AliasChoices("activeAccounts", "active_accounts"),
            serialization_alias="activeAccounts",
        ),
    ]


"""
GetCollectionFormHistoryRequestBody

The request schema to get query collections form history API .
"""


class GetCollectionFormHistoryRequestBody(SpApiBaseModel):
    """The request schema to get query collections form history API ."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    client_reference_details: Annotated[
        Optional["ClientReferenceDetails"],
        Field(
            None,
            validation_alias=AliasChoices(
                "clientReferenceDetails", "client_reference_details"
            ),
            serialization_alias="clientReferenceDetails",
        ),
    ]

    max_results: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices("maxResults", "max_results"),
            serialization_alias="maxResults",
            description="max Number of Results for query .",
        ),
    ]

    carrier_id: Annotated[
        Optional["CarrierId"],
        Field(
            None,
            validation_alias=AliasChoices("carrierId", "carrier_id"),
            serialization_alias="carrierId",
        ),
    ]

    ship_from_address: Annotated[
        Optional["Address"],
        Field(
            None,
            validation_alias=AliasChoices("shipFromAddress", "ship_from_address"),
            serialization_alias="shipFromAddress",
        ),
    ]

    date_range: Annotated[
        Optional["DateRange"],
        Field(
            None,
            validation_alias=AliasChoices("dateRange", "date_range"),
            serialization_alias="dateRange",
        ),
    ]


"""
GetCollectionFormHistoryRequest

Request parameters for getCollectionFormHistory
"""


class GetCollectionFormHistoryRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getCollectionFormHistory
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    body: Annotated[
        "GetCollectionFormHistoryRequestBody",
        BodyParam(),
        Field(..., description="[BODY] GetCollectionFormHistoryRequestBody body"),
    ]


"""
GetCollectionFormHistoryResponse

The Response for the GetCollectionFormHistoryResponse operation.
"""


class GetCollectionFormHistoryResponse(SpApiBaseModel):
    """The Response for the GetCollectionFormHistoryResponse operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    collection_forms_history_record_list: Annotated[
        Optional["CollectionFormsHistoryRecordList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "collectionFormsHistoryRecordList",
                "collection_forms_history_record_list",
            ),
            serialization_alias="collectionFormsHistoryRecordList",
        ),
    ]

    last_refreshed_date: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("lastRefreshedDate", "last_refreshed_date"),
            serialization_alias="lastRefreshedDate",
            description="Last Refereshed Date of collection",
        ),
    ]


"""
GetCollectionFormRequest

Request parameters for getCollectionForm
"""


class GetCollectionFormRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getCollectionForm
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    collection_form_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("collectionFormId", "collection_form_id"),
            serialization_alias="collectionFormId",
            description="[PATH] collection form Id to reprint a collection.",
        ),
    ]


"""
GetCollectionFormResponse

The Response for the GetCollectionFormResponse operation.
"""


class GetCollectionFormResponse(SpApiBaseModel):
    """The Response for the GetCollectionFormResponse operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    collections_form_document: Annotated[
        Optional["CollectionsFormDocument"],
        Field(
            None,
            validation_alias=AliasChoices(
                "collectionsFormDocument", "collections_form_document"
            ),
            serialization_alias="collectionsFormDocument",
        ),
    ]


"""
ShipperInstruction

The shipper instruction.
"""


class ShipperInstruction(SpApiBaseModel):
    """The shipper instruction."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    delivery_notes: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("deliveryNotes", "delivery_notes"),
            serialization_alias="deliveryNotes",
            description="The delivery notes for the shipment",
        ),
    ]


TaxDetailList = List["TaxDetail"]
"""A list of tax detail information."""


"""
ValueAddedServiceDetails

A collection of supported value-added services.
"""


class ValueAddedServiceDetails(SpApiBaseModel):
    """A collection of supported value-added services."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    collect_on_delivery: Annotated[
        Optional["CollectOnDelivery"],
        Field(
            None,
            validation_alias=AliasChoices("collectOnDelivery", "collect_on_delivery"),
            serialization_alias="collectOnDelivery",
        ),
    ]


"""
GetRatesRequestBody

The request schema for the getRates operation. When the channelType is Amazon, the shipTo address is not required and will be ignored.
"""


class GetRatesRequestBody(SpApiBaseModel):
    """The request schema for the getRates operation. When the channelType is Amazon, the shipTo address is not required and will be ignored."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    ship_to: Annotated[
        Optional["Address"],
        Field(
            None,
            validation_alias=AliasChoices("shipTo", "ship_to"),
            serialization_alias="shipTo",
            description="The ship to address.",
        ),
    ]

    ship_from: Annotated[
        "Address",
        Field(
            ...,
            validation_alias=AliasChoices("shipFrom", "ship_from"),
            serialization_alias="shipFrom",
            description="The ship from address.",
        ),
    ]

    return_to: Annotated[
        Optional["Address"],
        Field(
            None,
            validation_alias=AliasChoices("returnTo", "return_to"),
            serialization_alias="returnTo",
            description="The return to address.",
        ),
    ]

    ship_date: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices("shipDate", "ship_date"),
            serialization_alias="shipDate",
            description="The ship date and time (the requested pickup). This defaults to the current date and time.",
        ),
    ]

    shipper_instruction: Annotated[
        Optional["ShipperInstruction"],
        Field(
            None,
            validation_alias=AliasChoices("shipperInstruction", "shipper_instruction"),
            serialization_alias="shipperInstruction",
            description="This field describe shipper instruction.",
        ),
    ]

    packages: Annotated[
        "PackageList",
        Field(
            ...,
        ),
    ]

    value_added_services: Annotated[
        Optional["ValueAddedServiceDetails"],
        Field(
            None,
            validation_alias=AliasChoices("valueAddedServices", "value_added_services"),
            serialization_alias="valueAddedServices",
        ),
    ]

    tax_details: Annotated[
        Optional["TaxDetailList"],
        Field(
            None,
            validation_alias=AliasChoices("taxDetails", "tax_details"),
            serialization_alias="taxDetails",
        ),
    ]

    channel_details: Annotated[
        "ChannelDetails",
        Field(
            ...,
            validation_alias=AliasChoices("channelDetails", "channel_details"),
            serialization_alias="channelDetails",
        ),
    ]

    client_reference_details: Annotated[
        Optional["ClientReferenceDetails"],
        Field(
            None,
            validation_alias=AliasChoices(
                "clientReferenceDetails", "client_reference_details"
            ),
            serialization_alias="clientReferenceDetails",
        ),
    ]

    shipment_type: Annotated[
        Optional["ShipmentType"],
        Field(
            None,
            validation_alias=AliasChoices("shipmentType", "shipment_type"),
            serialization_alias="shipmentType",
        ),
    ]

    destination_access_point_details: Annotated[
        Optional["AccessPointDetails"],
        Field(
            None,
            validation_alias=AliasChoices(
                "destinationAccessPointDetails", "destination_access_point_details"
            ),
            serialization_alias="destinationAccessPointDetails",
        ),
    ]

    carrier_accounts: Annotated[
        Optional["CarrierAccounts"],
        Field(
            None,
            validation_alias=AliasChoices("carrierAccounts", "carrier_accounts"),
            serialization_alias="carrierAccounts",
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


IneligibleRateList = List["IneligibleRate"]
"""A list of ineligible shipping service offerings."""


RateList = List["Rate"]
"""A list of eligible shipping service offerings."""


RequestToken = str
"""A unique token generated to identify a getRates operation."""


"""
GetRatesResult

The payload for the getRates operation.
"""


class GetRatesResult(SpApiBaseModel):
    """The payload for the getRates operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    request_token: Annotated[
        "RequestToken",
        Field(
            ...,
            validation_alias=AliasChoices("requestToken", "request_token"),
            serialization_alias="requestToken",
        ),
    ]

    rates: Annotated[
        "RateList",
        Field(
            ...,
        ),
    ]

    ineligible_rates: Annotated[
        Optional["IneligibleRateList"],
        Field(
            None,
            validation_alias=AliasChoices("ineligibleRates", "ineligible_rates"),
            serialization_alias="ineligibleRates",
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
        Field(
            None,
        ),
    ]


"""
GetShipmentDocumentsRequest

Request parameters for getShipmentDocuments
"""


class GetShipmentDocumentsRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getShipmentDocuments
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
            description="[PATH] The shipment identifier originally returned by the purchaseShipment operation.",
        ),
    ]

    package_client_reference_id: Annotated[
        str,
        QueryParam(),
        Field(
            ...,
            validation_alias=AliasChoices(
                "packageClientReferenceId", "package_client_reference_id"
            ),
            serialization_alias="packageClientReferenceId",
            description="[QUERY] The package client reference identifier originally provided in the request body parameter for the getRates operation.",
        ),
    ]

    format: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            description="[QUERY] The file format of the document. Must be one of the supported formats returned by the getRates operation.",
        ),
    ]

    dpi: Annotated[
        Optional[float],
        QueryParam(),
        Field(
            None,
            description="[QUERY] The resolution of the document (for example, 300 means 300 dots per inch). Must be one of the supported resolutions returned in the response to the getRates operation.",
        ),
    ]


PackageClientReferenceId = str
"""A client provided unique identifier for a package being shipped. This value should be saved by the client to pass as a parameter to the getShipmentDocuments operation."""


PackageDocumentList = List["PackageDocument"]
"""A list of documents related to a package."""


"""
PackageDocumentDetail

The post-purchase details of a package that will be shipped using a shipping service.
"""


class PackageDocumentDetail(SpApiBaseModel):
    """The post-purchase details of a package that will be shipped using a shipping service."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    package_client_reference_id: Annotated[
        "PackageClientReferenceId",
        Field(
            ...,
            validation_alias=AliasChoices(
                "packageClientReferenceId", "package_client_reference_id"
            ),
            serialization_alias="packageClientReferenceId",
        ),
    ]

    package_documents: Annotated[
        "PackageDocumentList",
        Field(
            ...,
            validation_alias=AliasChoices("packageDocuments", "package_documents"),
            serialization_alias="packageDocuments",
        ),
    ]

    tracking_id: Annotated[
        Optional["TrackingId"],
        Field(
            None,
            validation_alias=AliasChoices("trackingId", "tracking_id"),
            serialization_alias="trackingId",
        ),
    ]


"""
GetShipmentDocumentsResult

The payload for the getShipmentDocuments operation.
"""


class GetShipmentDocumentsResult(SpApiBaseModel):
    """The payload for the getShipmentDocuments operation."""

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

    package_document_detail: Annotated[
        "PackageDocumentDetail",
        Field(
            ...,
            validation_alias=AliasChoices(
                "packageDocumentDetail", "package_document_detail"
            ),
            serialization_alias="packageDocumentDetail",
        ),
    ]

    benefits: Annotated[
        Optional["Benefits"],
        Field(
            None,
        ),
    ]


"""
GetShipmentDocumentsResponse

The response schema for the the getShipmentDocuments operation.
"""


class GetShipmentDocumentsResponse(SpApiBaseModel):
    """The response schema for the the getShipmentDocuments operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["GetShipmentDocumentsResult"],
        Field(
            None,
        ),
    ]


"""
GetTrackingRequest

Request parameters for getTracking
"""


class GetTrackingRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getTracking
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    tracking_id: Annotated[
        str,
        QueryParam(),
        Field(
            ...,
            validation_alias=AliasChoices("trackingId", "tracking_id"),
            serialization_alias="trackingId",
            description="[QUERY] A carrier-generated tracking identifier originally returned by the purchaseShipment operation.",
        ),
    ]

    carrier_id: Annotated[
        str,
        QueryParam(),
        Field(
            ...,
            validation_alias=AliasChoices("carrierId", "carrier_id"),
            serialization_alias="carrierId",
            description="[QUERY] A carrier identifier originally returned by the getRates operation for the selected rate.",
        ),
    ]


Status = str
"""The status of the package being shipped."""


"""
TrackingDetailCodes

Contains detail codes that provide additional details related to the forward and return leg of the shipment.
"""


class TrackingDetailCodes(SpApiBaseModel):
    """Contains detail codes that provide additional details related to the forward and return leg of the shipment."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    forward: Annotated[
        List["DetailCodes"],
        Field(
            ...,
            description="Contains detail codes that provide additional details related to the forward leg of the shipment.",
        ),
    ]

    returns: Annotated[
        List["DetailCodes"],
        Field(
            ...,
            description="Contains detail codes that provide additional details related to the return leg of the shipment.",
        ),
    ]


"""
TrackingSummary

A package status summary.
"""


class TrackingSummary(SpApiBaseModel):
    """A package status summary."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    status: Annotated[
        Optional["Status"],
        Field(
            None,
        ),
    ]

    tracking_detail_codes: Annotated[
        Optional["TrackingDetailCodes"],
        Field(
            None,
            validation_alias=AliasChoices(
                "trackingDetailCodes", "tracking_detail_codes"
            ),
            serialization_alias="trackingDetailCodes",
        ),
    ]


"""
GetTrackingResult

The payload for the getTracking operation.
"""


class GetTrackingResult(SpApiBaseModel):
    """The payload for the getTracking operation."""

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

    alternate_leg_tracking_id: Annotated[
        "AlternateLegTrackingId",
        Field(
            ...,
            validation_alias=AliasChoices(
                "alternateLegTrackingId", "alternate_leg_tracking_id"
            ),
            serialization_alias="alternateLegTrackingId",
        ),
    ]

    event_history: Annotated[
        List["Event"],
        Field(
            ...,
            validation_alias=AliasChoices("eventHistory", "event_history"),
            serialization_alias="eventHistory",
            description="A list of tracking events.",
        ),
    ]

    promised_delivery_date: Annotated[
        datetime,
        Field(
            ...,
            validation_alias=AliasChoices(
                "promisedDeliveryDate", "promised_delivery_date"
            ),
            serialization_alias="promisedDeliveryDate",
            description="The date and time by which the shipment is promised to be delivered.",
        ),
    ]

    summary: Annotated[
        "TrackingSummary",
        Field(
            ...,
        ),
    ]


"""
GetTrackingResponse

The response schema for the getTracking operation.
"""


class GetTrackingResponse(SpApiBaseModel):
    """The response schema for the getTracking operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["GetTrackingResult"],
        Field(
            None,
        ),
    ]


"""
GetUnmanifestedShipmentsRequestBody

The request schema for the GetUnmanifestedShipmentsRequestBody operation.
"""


class GetUnmanifestedShipmentsRequestBody(SpApiBaseModel):
    """The request schema for the GetUnmanifestedShipmentsRequestBody operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    client_reference_details: Annotated[
        Optional["ClientReferenceDetails"],
        Field(
            None,
            validation_alias=AliasChoices(
                "clientReferenceDetails", "client_reference_details"
            ),
            serialization_alias="clientReferenceDetails",
        ),
    ]


"""
GetUnmanifestedShipmentsRequest

Request parameters for getUnmanifestedShipments
"""


class GetUnmanifestedShipmentsRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getUnmanifestedShipments
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    body: Annotated[
        "GetUnmanifestedShipmentsRequestBody",
        BodyParam(),
        Field(..., description="[BODY] GetUmanifestedShipmentsRequestBody body"),
    ]


UnmanifestedCarrierInformationList = List["UnmanifestedCarrierInformation"]
"""A list of UnmanifestedCarrierInformation"""


"""
GetUnmanifestedShipmentsResponse

The Response for the GetUnmanifestedShipmentsResponse operation.
"""


class GetUnmanifestedShipmentsResponse(SpApiBaseModel):
    """The Response for the GetUnmanifestedShipmentsResponse operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    unmanifested_carrier_information_list: Annotated[
        Optional["UnmanifestedCarrierInformationList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "unmanifestedCarrierInformationList",
                "unmanifested_carrier_information_list",
            ),
            serialization_alias="unmanifestedCarrierInformationList",
        ),
    ]


MerchantId = str
"""merchant Id of provided merchant """


"""
GoodsOwner

The seller owning the goods before handing them over to the carrier
"""


class GoodsOwner(SpApiBaseModel):
    """The seller owning the goods before handing them over to the carrier"""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    merchant_id: Annotated[
        "MerchantId",
        Field(
            ...,
            validation_alias=AliasChoices("merchantId", "merchant_id"),
            serialization_alias="merchantId",
            description="The Amazon Merchant Identifier (merchantId) of the seller owning the goods before handing them over to the carrier",
        ),
    ]


IneligibilityReasonCode = str
"""Reasons that make a shipment service offering ineligible."""


"""
IneligibilityReason

The reason why a shipping service offering is ineligible.
"""


class IneligibilityReason(SpApiBaseModel):
    """The reason why a shipping service offering is ineligible."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    code: Annotated[
        "IneligibilityReasonCode",
        Field(
            ...,
        ),
    ]

    message: Annotated[str, Field(..., description="The ineligibility reason.")]


ServiceId = str
"""An identifier for the shipping service."""


ServiceName = str
"""The name of the shipping service."""


"""
IneligibleRate

Detailed information for an ineligible shipping service offering.
"""


class IneligibleRate(SpApiBaseModel):
    """Detailed information for an ineligible shipping service offering."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    service_id: Annotated[
        "ServiceId",
        Field(
            ...,
            validation_alias=AliasChoices("serviceId", "service_id"),
            serialization_alias="serviceId",
        ),
    ]

    service_name: Annotated[
        "ServiceName",
        Field(
            ...,
            validation_alias=AliasChoices("serviceName", "service_name"),
            serialization_alias="serviceName",
        ),
    ]

    carrier_name: Annotated[
        "CarrierName",
        Field(
            ...,
            validation_alias=AliasChoices("carrierName", "carrier_name"),
            serialization_alias="carrierName",
        ),
    ]

    carrier_id: Annotated[
        "CarrierId",
        Field(
            ...,
            validation_alias=AliasChoices("carrierId", "carrier_id"),
            serialization_alias="carrierId",
        ),
    ]

    ineligibility_reasons: Annotated[
        List["IneligibilityReason"],
        Field(
            ...,
            validation_alias=AliasChoices(
                "ineligibilityReasons", "ineligibility_reasons"
            ),
            serialization_alias="ineligibilityReasons",
            description="A list of reasons why a shipping service offering is ineligible.",
        ),
    ]


"""
InvoiceDetails

The invoice details for charges associated with the goods in the package. Only applies to certain regions.
"""


class InvoiceDetails(SpApiBaseModel):
    """The invoice details for charges associated with the goods in the package. Only applies to certain regions."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    invoice_number: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("invoiceNumber", "invoice_number"),
            serialization_alias="invoiceNumber",
            description="The invoice number of the item.",
        ),
    ]

    invoice_date: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices("invoiceDate", "invoice_date"),
            serialization_alias="invoiceDate",
            description="The invoice date of the item in ISO 8061 format.",
        ),
    ]


# Enum definitions
class UnitEnum(str, Enum):
    """Enum for unit"""

    INCH = "INCH"  # The imperial unit of length equal to one twelfth of a foot.
    CENTIMETER = (
        "CENTIMETER"  # A metric unit of length, equal to one hundredth of a meter.
    )


"""
LiquidVolume

Liquid Volume.
"""


class LiquidVolume(SpApiBaseModel):
    """Liquid Volume."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    unit: Annotated[UnitEnum, Field(..., description="The unit of measurement.")]

    value: Annotated[float, Field(..., description="The measurement value.")]


# Enum definitions
class UnitEnum(str, Enum):
    """Enum for unit"""

    INCH = "INCH"  # The imperial unit of length equal to one twelfth of a foot.
    CENTIMETER = (
        "CENTIMETER"  # A metric unit of length, equal to one hundredth of a meter.
    )


"""
Weight

The weight in the units indicated.
"""


class Weight(SpApiBaseModel):
    """The weight in the units indicated."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    unit: Annotated[UnitEnum, Field(..., description="The unit of measurement.")]

    value: Annotated[float, Field(..., description="The measurement value.")]


"""
Item

An item in a package.
"""


class Item(SpApiBaseModel):
    """An item in a package."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    item_value: Annotated[
        Optional["Currency"],
        Field(
            None,
            validation_alias=AliasChoices("itemValue", "item_value"),
            serialization_alias="itemValue",
        ),
    ]

    description: Annotated[
        Optional[str], Field(None, description="The product description of the item.")
    ]

    item_identifier: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("itemIdentifier", "item_identifier"),
            serialization_alias="itemIdentifier",
            description="A unique identifier for an item provided by the client.",
        ),
    ]

    quantity: Annotated[
        int, Field(..., description="The number of units. This value is required.")
    ]

    weight: Annotated[
        Optional["Weight"],
        Field(
            None,
        ),
    ]

    liquid_volume: Annotated[
        Optional["LiquidVolume"],
        Field(
            None,
            validation_alias=AliasChoices("liquidVolume", "liquid_volume"),
            serialization_alias="liquidVolume",
        ),
    ]

    is_hazmat: Annotated[
        Optional[bool],
        Field(
            None,
            validation_alias=AliasChoices("isHazmat", "is_hazmat"),
            serialization_alias="isHazmat",
            description="When true, the item qualifies as hazardous materials (hazmat). Defaults to false.",
        ),
    ]

    dangerous_goods_details: Annotated[
        Optional["DangerousGoodsDetails"],
        Field(
            None,
            validation_alias=AliasChoices(
                "dangerousGoodsDetails", "dangerous_goods_details"
            ),
            serialization_alias="dangerousGoodsDetails",
        ),
    ]

    product_type: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("productType", "product_type"),
            serialization_alias="productType",
            description="The product type of the item.",
        ),
    ]

    invoice_details: Annotated[
        Optional["InvoiceDetails"],
        Field(
            None,
            validation_alias=AliasChoices("invoiceDetails", "invoice_details"),
            serialization_alias="invoiceDetails",
        ),
    ]

    serial_numbers: Annotated[
        Optional[List["str"]],
        Field(
            None,
            validation_alias=AliasChoices("serialNumbers", "serial_numbers"),
            serialization_alias="serialNumbers",
            description="A list of unique serial numbers in an Amazon package that can be used to guarantee non-fraudulent items. The number of serial numbers in the list must be less than or equal to the quantity of items being shipped. Only applicable when channel source is Amazon.",
        ),
    ]

    direct_fulfillment_item_identifiers: Annotated[
        Optional["DirectFulfillmentItemIdentifiers"],
        Field(
            None,
            validation_alias=AliasChoices(
                "directFulfillmentItemIdentifiers",
                "direct_fulfillment_item_identifiers",
            ),
            serialization_alias="directFulfillmentItemIdentifiers",
        ),
    ]


ItemList = List["Item"]
"""A list of items."""


LabelAttribute = str
"""Enumerates the attributes supported to be printed on a shipping label. The values for these attributes are retrieved from GetRates/OneClickShipment request"""


"""
LinkCarrierAccountRequestBody

The request schema for verify and add the merchant's account with a certain carrier.
"""


class LinkCarrierAccountRequestBody(SpApiBaseModel):
    """The request schema for verify and add the merchant's account with a certain carrier."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    client_reference_details: Annotated[
        Optional["ClientReferenceDetails"],
        Field(
            None,
            validation_alias=AliasChoices(
                "clientReferenceDetails", "client_reference_details"
            ),
            serialization_alias="clientReferenceDetails",
        ),
    ]

    carrier_account_type: Annotated[
        "CarrierAccountType",
        Field(
            ...,
            validation_alias=AliasChoices("carrierAccountType", "carrier_account_type"),
            serialization_alias="carrierAccountType",
        ),
    ]

    carrier_account_attributes: Annotated[
        "CarrierAccountAttributes",
        Field(
            ...,
            validation_alias=AliasChoices(
                "carrierAccountAttributes", "carrier_account_attributes"
            ),
            serialization_alias="carrierAccountAttributes",
        ),
    ]

    encrypted_carrier_account_attributes: Annotated[
        Optional["CarrierAccountAttributes"],
        Field(
            None,
            validation_alias=AliasChoices(
                "encryptedCarrierAccountAttributes",
                "encrypted_carrier_account_attributes",
            ),
            serialization_alias="encryptedCarrierAccountAttributes",
        ),
    ]


"""
LinkCarrierAccountRequest

Request parameters for linkCarrierAccount
"""


class LinkCarrierAccountRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for linkCarrierAccount
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    carrier_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("carrierId", "carrier_id"),
            serialization_alias="carrierId",
            description="[PATH] An identifier for the carrier with which the seller's account is being linked.",
        ),
    ]

    body: Annotated[
        "LinkCarrierAccountRequestBody",
        BodyParam(),
        Field(..., description="[BODY] LinkCarrierAccountRequestBody body"),
    ]


"""
LinkCarrierAccountResponse

The Response for the LinkCarrierAccount operation.
"""


class LinkCarrierAccountResponse(SpApiBaseModel):
    """The Response for the LinkCarrierAccount operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    registration_status: Annotated[
        Optional["AccountStatus"],
        Field(
            None,
            validation_alias=AliasChoices("registrationStatus", "registration_status"),
            serialization_alias="registrationStatus",
        ),
    ]

    account_id: Annotated[
        Optional["AccountId"],
        Field(
            None,
            validation_alias=AliasChoices("accountId", "account_id"),
            serialization_alias="accountId",
        ),
    ]


"""
LinkableAccountType

Info About Linkable Account Type
"""


class LinkableAccountType(SpApiBaseModel):
    """Info About Linkable Account Type"""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    account_type: Annotated[
        Optional["AccountType"],
        Field(
            None,
            validation_alias=AliasChoices("accountType", "account_type"),
            serialization_alias="accountType",
        ),
    ]

    carrier_account_inputs: Annotated[
        Optional["CarrierAccountInputsList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "carrierAccountInputs", "carrier_account_inputs"
            ),
            serialization_alias="carrierAccountInputs",
        ),
    ]


LinkableAccountTypeList = List["LinkableAccountType"]
"""A list of LinkableAccountType"""


"""
LinkableCarrier

Info About Linkable Carrier
"""


class LinkableCarrier(SpApiBaseModel):
    """Info About Linkable Carrier"""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    carrier_id: Annotated[
        Optional["CarrierId"],
        Field(
            None,
            validation_alias=AliasChoices("carrierId", "carrier_id"),
            serialization_alias="carrierId",
        ),
    ]

    linkable_account_types: Annotated[
        Optional["LinkableAccountTypeList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "linkableAccountTypes", "linkable_account_types"
            ),
            serialization_alias="linkableAccountTypes",
        ),
    ]


NdrAction = str
"""The type of NDR action shipper wants to take for a particular shipment."""


"""
NdrRequestData

Additional information required for the NDR action that has been filed. If the NDR Action is RESCHEDULE, rescheduleDate is a required field. Otherwise, if the NDR Action is REATTEMPT, additionalAddressNotes is a required field. 
"""


class NdrRequestData(SpApiBaseModel):
    """Additional information required for the NDR action that has been filed. If the NDR Action is RESCHEDULE, rescheduleDate is a required field. Otherwise, if the NDR Action is REATTEMPT, additionalAddressNotes is a required field."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    reschedule_date: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices("rescheduleDate", "reschedule_date"),
            serialization_alias="rescheduleDate",
            description="The date on which the Seller wants to reschedule shipment delivery, in ISO-8601 date/time format",
        ),
    ]

    additional_address_notes: Annotated[
        Optional["AdditionalAddressNotes"],
        Field(
            None,
            validation_alias=AliasChoices(
                "additionalAddressNotes", "additional_address_notes"
            ),
            serialization_alias="additionalAddressNotes",
        ),
    ]


OneClickShipmentValueAddedServiceDetails = List["OneClickShipmentValueAddedService"]
"""The value-added services to be added to a shipping service purchase."""


"""
ServiceIds

A list of ServiceId.
"""


class ServiceIds(SpApiBaseModel):
    """A list of ServiceId."""

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow",
        serialize_by_alias=True,
        arbitrary_types_allowed=True,
    )


"""
ServiceSelection

Service Selection Criteria.
"""


class ServiceSelection(SpApiBaseModel):
    """Service Selection Criteria."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    service_id: Annotated[
        "ServiceIds",
        Field(
            ...,
            validation_alias=AliasChoices("serviceId", "service_id"),
            serialization_alias="serviceId",
        ),
    ]


"""
OneClickShipmentRequestBody

The request schema for the OneClickShipment operation. When the channelType is not Amazon, shipTo is required and when channelType is Amazon shipTo is ignored.
"""


class OneClickShipmentRequestBody(SpApiBaseModel):
    """The request schema for the OneClickShipment operation. When the channelType is not Amazon, shipTo is required and when channelType is Amazon shipTo is ignored."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    ship_to: Annotated[
        Optional["Address"],
        Field(
            None,
            validation_alias=AliasChoices("shipTo", "ship_to"),
            serialization_alias="shipTo",
            description="The ship to address.",
        ),
    ]

    ship_from: Annotated[
        "Address",
        Field(
            ...,
            validation_alias=AliasChoices("shipFrom", "ship_from"),
            serialization_alias="shipFrom",
            description="The ship from address.",
        ),
    ]

    return_to: Annotated[
        Optional["Address"],
        Field(
            None,
            validation_alias=AliasChoices("returnTo", "return_to"),
            serialization_alias="returnTo",
            description="The return to address.",
        ),
    ]

    ship_date: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices("shipDate", "ship_date"),
            serialization_alias="shipDate",
            description="The ship date and time (the requested pickup). This defaults to the current date and time.",
        ),
    ]

    goods_owner: Annotated[
        Optional["GoodsOwner"],
        Field(
            None,
            validation_alias=AliasChoices("goodsOwner", "goods_owner"),
            serialization_alias="goodsOwner",
            description="The seller owning the goods before handing them over to the carrier",
        ),
    ]

    packages: Annotated[
        "PackageList",
        Field(
            ...,
        ),
    ]

    value_added_services_details: Annotated[
        Optional["OneClickShipmentValueAddedServiceDetails"],
        Field(
            None,
            validation_alias=AliasChoices(
                "valueAddedServicesDetails", "value_added_services_details"
            ),
            serialization_alias="valueAddedServicesDetails",
        ),
    ]

    tax_details: Annotated[
        Optional["TaxDetailList"],
        Field(
            None,
            validation_alias=AliasChoices("taxDetails", "tax_details"),
            serialization_alias="taxDetails",
        ),
    ]

    channel_details: Annotated[
        "ChannelDetails",
        Field(
            ...,
            validation_alias=AliasChoices("channelDetails", "channel_details"),
            serialization_alias="channelDetails",
        ),
    ]

    label_specifications: Annotated[
        "RequestedDocumentSpecification",
        Field(
            ...,
            validation_alias=AliasChoices(
                "labelSpecifications", "label_specifications"
            ),
            serialization_alias="labelSpecifications",
        ),
    ]

    service_selection: Annotated[
        "ServiceSelection",
        Field(
            ...,
            validation_alias=AliasChoices("serviceSelection", "service_selection"),
            serialization_alias="serviceSelection",
        ),
    ]

    shipper_instruction: Annotated[
        Optional["ShipperInstruction"],
        Field(
            None,
            validation_alias=AliasChoices("shipperInstruction", "shipper_instruction"),
            serialization_alias="shipperInstruction",
            description="Optional field for shipper instruction.",
        ),
    ]

    destination_access_point_details: Annotated[
        Optional["AccessPointDetails"],
        Field(
            None,
            validation_alias=AliasChoices(
                "destinationAccessPointDetails", "destination_access_point_details"
            ),
            serialization_alias="destinationAccessPointDetails",
        ),
    ]


"""
OneClickShipmentRequest

Request parameters for oneClickShipment
"""


class OneClickShipmentRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for oneClickShipment
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    body: Annotated[
        "OneClickShipmentRequestBody",
        BodyParam(),
        Field(..., description="[BODY] OneClickShipmentRequestBody body"),
    ]


"""
TimeWindow

The start and end time that specifies the time interval of an event.
"""


class TimeWindow(SpApiBaseModel):
    """The start and end time that specifies the time interval of an event."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    start: Annotated[
        Optional[datetime],
        Field(None, description="The start time of the time window."),
    ]

    end: Annotated[
        Optional[datetime], Field(None, description="The end time of the time window.")
    ]


"""
Promise

The time windows promised for pickup and delivery events.
"""


class Promise(SpApiBaseModel):
    """The time windows promised for pickup and delivery events."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    delivery_window: Annotated[
        Optional["TimeWindow"],
        Field(
            None,
            validation_alias=AliasChoices("deliveryWindow", "delivery_window"),
            serialization_alias="deliveryWindow",
        ),
    ]

    pickup_window: Annotated[
        Optional["TimeWindow"],
        Field(
            None,
            validation_alias=AliasChoices("pickupWindow", "pickup_window"),
            serialization_alias="pickupWindow",
        ),
    ]


"""
Service

Service Related Info
"""


class Service(SpApiBaseModel):
    """Service Related Info"""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    id: Annotated[
        "ServiceId",
        Field(
            ...,
        ),
    ]

    name: Annotated[
        "ServiceName",
        Field(
            ...,
        ),
    ]


"""
OneClickShipmentResult

The payload for the OneClickShipment API.
"""


class OneClickShipmentResult(SpApiBaseModel):
    """The payload for the OneClickShipment API."""

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

    package_document_details: Annotated[
        "PackageDocumentDetailList",
        Field(
            ...,
            validation_alias=AliasChoices(
                "packageDocumentDetails", "package_document_details"
            ),
            serialization_alias="packageDocumentDetails",
        ),
    ]

    promise: Annotated[
        "Promise",
        Field(
            ...,
        ),
    ]

    carrier: Annotated[
        "Carrier",
        Field(
            ...,
        ),
    ]

    service: Annotated[
        "Service",
        Field(
            ...,
        ),
    ]

    total_charge: Annotated[
        "Currency",
        Field(
            ...,
            validation_alias=AliasChoices("totalCharge", "total_charge"),
            serialization_alias="totalCharge",
        ),
    ]


"""
OneClickShipmentResponse

The response schema for the OneClickShipment operation.
"""


class OneClickShipmentResponse(SpApiBaseModel):
    """The response schema for the OneClickShipment operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["OneClickShipmentResult"],
        Field(
            None,
        ),
    ]


"""
OneClickShipmentValueAddedService

A value-added service to be applied to a shipping service purchase.
"""


class OneClickShipmentValueAddedService(SpApiBaseModel):
    """A value-added service to be applied to a shipping service purchase."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    id: Annotated[
        str,
        Field(..., description="The identifier of the selected value-added service."),
    ]

    amount: Annotated[
        Optional["Currency"],
        Field(
            None,
        ),
    ]


"""
Package

A package to be shipped through a shipping service offering.
"""


class Package(SpApiBaseModel):
    """A package to be shipped through a shipping service offering."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    dimensions: Annotated[
        "Dimensions",
        Field(
            ...,
        ),
    ]

    weight: Annotated[
        "Weight",
        Field(
            ...,
        ),
    ]

    insured_value: Annotated[
        "Currency",
        Field(
            ...,
            validation_alias=AliasChoices("insuredValue", "insured_value"),
            serialization_alias="insuredValue",
        ),
    ]

    is_hazmat: Annotated[
        Optional[bool],
        Field(
            None,
            validation_alias=AliasChoices("isHazmat", "is_hazmat"),
            serialization_alias="isHazmat",
            description="When true, the package contains hazardous materials. Defaults to false.",
        ),
    ]

    seller_display_name: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("sellerDisplayName", "seller_display_name"),
            serialization_alias="sellerDisplayName",
            description="The seller name displayed on the label.",
        ),
    ]

    charges: Annotated[
        Optional["ChargeList"],
        Field(
            None,
        ),
    ]

    package_client_reference_id: Annotated[
        "PackageClientReferenceId",
        Field(
            ...,
            validation_alias=AliasChoices(
                "packageClientReferenceId", "package_client_reference_id"
            ),
            serialization_alias="packageClientReferenceId",
        ),
    ]

    items: Annotated[
        "ItemList",
        Field(
            ...,
        ),
    ]


"""
PackageDocument

A document related to a package.
"""


class PackageDocument(SpApiBaseModel):
    """A document related to a package."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    type: Annotated[
        "DocumentType",
        Field(
            ...,
        ),
    ]

    format: Annotated[
        "DocumentFormat",
        Field(
            ...,
        ),
    ]

    contents: Annotated[
        "Contents",
        Field(
            ...,
        ),
    ]


PaymentType = str
"""Payment type of the purchase."""


"""
SupportedDocumentDetail

The supported document types for a service offering.
"""


class SupportedDocumentDetail(SpApiBaseModel):
    """The supported document types for a service offering."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    name: Annotated[
        "DocumentType",
        Field(
            ...,
        ),
    ]

    is_mandatory: Annotated[
        bool,
        Field(
            ...,
            validation_alias=AliasChoices("isMandatory", "is_mandatory"),
            serialization_alias="isMandatory",
            description="When true, the supported document type is required.",
        ),
    ]


"""
PrintOption

The format options available for a label.
"""


class PrintOption(SpApiBaseModel):
    """The format options available for a label."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    supported_d_p_is: Annotated[
        Optional[List["Dpi"]],
        Field(
            None,
            validation_alias=AliasChoices("supportedDPIs", "supported_d_p_is"),
            serialization_alias="supportedDPIs",
            description="A list of the supported DPI options for a document.",
        ),
    ]

    supported_page_layouts: Annotated[
        List["PageLayout"],
        Field(
            ...,
            validation_alias=AliasChoices(
                "supportedPageLayouts", "supported_page_layouts"
            ),
            serialization_alias="supportedPageLayouts",
            description="A list of the supported page layout options for a document.",
        ),
    ]

    supported_file_joining_options: Annotated[
        List["NeedFileJoining"],
        Field(
            ...,
            validation_alias=AliasChoices(
                "supportedFileJoiningOptions", "supported_file_joining_options"
            ),
            serialization_alias="supportedFileJoiningOptions",
            description="A list of the supported needFileJoining boolean values for a document.",
        ),
    ]

    supported_document_details: Annotated[
        List["SupportedDocumentDetail"],
        Field(
            ...,
            validation_alias=AliasChoices(
                "supportedDocumentDetails", "supported_document_details"
            ),
            serialization_alias="supportedDocumentDetails",
            description="A list of the supported documented details.",
        ),
    ]


PrintOptionList = List["PrintOption"]
"""A list of the format options for a label."""


RateId = str
"""An identifier for the rate (shipment offering) provided by a shipping service provider."""


RequestedValueAddedServiceList = List["RequestedValueAddedService"]
"""The value-added services to be added to a shipping service purchase."""


"""
PurchaseShipmentRequestBody

The request schema for the purchaseShipment operation.
"""


class PurchaseShipmentRequestBody(SpApiBaseModel):
    """The request schema for the purchaseShipment operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    request_token: Annotated[
        "RequestToken",
        Field(
            ...,
            validation_alias=AliasChoices("requestToken", "request_token"),
            serialization_alias="requestToken",
        ),
    ]

    rate_id: Annotated[
        "RateId",
        Field(
            ...,
            validation_alias=AliasChoices("rateId", "rate_id"),
            serialization_alias="rateId",
        ),
    ]

    requested_document_specification: Annotated[
        "RequestedDocumentSpecification",
        Field(
            ...,
            validation_alias=AliasChoices(
                "requestedDocumentSpecification", "requested_document_specification"
            ),
            serialization_alias="requestedDocumentSpecification",
        ),
    ]

    requested_value_added_services: Annotated[
        Optional["RequestedValueAddedServiceList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "requestedValueAddedServices", "requested_value_added_services"
            ),
            serialization_alias="requestedValueAddedServices",
        ),
    ]

    additional_inputs: Annotated[
        Optional[Dict[str, Any]],
        Field(
            None,
            validation_alias=AliasChoices("additionalInputs", "additional_inputs"),
            serialization_alias="additionalInputs",
            description="The additional inputs required to purchase a shipping offering, in JSON format. The JSON provided here must adhere to the JSON schema that is returned in the response to the getAdditionalInputs operation. Additional inputs are only required when indicated by the requiresAdditionalInputs property in the response to the getRates operation.",
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
PurchaseShipmentResult

The payload for the purchaseShipment operation.
"""


class PurchaseShipmentResult(SpApiBaseModel):
    """The payload for the purchaseShipment operation."""

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

    package_document_details: Annotated[
        "PackageDocumentDetailList",
        Field(
            ...,
            validation_alias=AliasChoices(
                "packageDocumentDetails", "package_document_details"
            ),
            serialization_alias="packageDocumentDetails",
        ),
    ]

    promise: Annotated[
        "Promise",
        Field(
            ...,
        ),
    ]

    benefits: Annotated[
        Optional["Benefits"],
        Field(
            None,
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
        Field(
            None,
        ),
    ]


RateItemList = List["RateItem"]
"""A list of RateItem"""


SupportedDocumentSpecificationList = List["SupportedDocumentSpecification"]
"""A list of the document specifications supported for a shipment service offering."""


"""
Rate

The details of a shipping service offering.
"""


class Rate(SpApiBaseModel):
    """The details of a shipping service offering."""

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

    carrier_id: Annotated[
        "CarrierId",
        Field(
            ...,
            validation_alias=AliasChoices("carrierId", "carrier_id"),
            serialization_alias="carrierId",
        ),
    ]

    carrier_name: Annotated[
        "CarrierName",
        Field(
            ...,
            validation_alias=AliasChoices("carrierName", "carrier_name"),
            serialization_alias="carrierName",
        ),
    ]

    service_id: Annotated[
        "ServiceId",
        Field(
            ...,
            validation_alias=AliasChoices("serviceId", "service_id"),
            serialization_alias="serviceId",
        ),
    ]

    service_name: Annotated[
        "ServiceName",
        Field(
            ...,
            validation_alias=AliasChoices("serviceName", "service_name"),
            serialization_alias="serviceName",
        ),
    ]

    billed_weight: Annotated[
        Optional["Weight"],
        Field(
            None,
            validation_alias=AliasChoices("billedWeight", "billed_weight"),
            serialization_alias="billedWeight",
        ),
    ]

    total_charge: Annotated[
        "Currency",
        Field(
            ...,
            validation_alias=AliasChoices("totalCharge", "total_charge"),
            serialization_alias="totalCharge",
        ),
    ]

    promise: Annotated[
        "Promise",
        Field(
            ...,
        ),
    ]

    supported_document_specifications: Annotated[
        "SupportedDocumentSpecificationList",
        Field(
            ...,
            validation_alias=AliasChoices(
                "supportedDocumentSpecifications", "supported_document_specifications"
            ),
            serialization_alias="supportedDocumentSpecifications",
        ),
    ]

    available_value_added_service_groups: Annotated[
        Optional["AvailableValueAddedServiceGroupList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "availableValueAddedServiceGroups",
                "available_value_added_service_groups",
            ),
            serialization_alias="availableValueAddedServiceGroups",
        ),
    ]

    requires_additional_inputs: Annotated[
        bool,
        Field(
            ...,
            validation_alias=AliasChoices(
                "requiresAdditionalInputs", "requires_additional_inputs"
            ),
            serialization_alias="requiresAdditionalInputs",
            description="When true, indicates that additional inputs are required to purchase this shipment service. You must then call the getAdditionalInputs operation to return the JSON schema to use when providing the additional inputs to the purchaseShipment operation.",
        ),
    ]

    rate_item_list: Annotated[
        Optional["RateItemList"],
        Field(
            None,
            validation_alias=AliasChoices("rateItemList", "rate_item_list"),
            serialization_alias="rateItemList",
        ),
    ]

    payment_type: Annotated[
        Optional["PaymentType"],
        Field(
            None,
            validation_alias=AliasChoices("paymentType", "payment_type"),
            serialization_alias="paymentType",
        ),
    ]

    benefits: Annotated[
        Optional["Benefits"],
        Field(
            None,
        ),
    ]


RateItemID = str
"""Unique ID for the rateItem."""


RateItemType = str
"""Type of the rateItem."""


"""
RateItem

Rate Item for shipping (base cost, transaction fee, confirmation, insurance, etc.) Data source definition: 
"""


class RateItem(SpApiBaseModel):
    """Rate Item for shipping (base cost, transaction fee, confirmation, insurance, etc.) Data source definition:"""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    rate_item_i_d: Annotated[
        Optional["RateItemID"],
        Field(
            None,
            validation_alias=AliasChoices("rateItemID", "rate_item_i_d"),
            serialization_alias="rateItemID",
        ),
    ]

    rate_item_type: Annotated[
        Optional["RateItemType"],
        Field(
            None,
            validation_alias=AliasChoices("rateItemType", "rate_item_type"),
            serialization_alias="rateItemType",
        ),
    ]

    rate_item_charge: Annotated[
        Optional["Currency"],
        Field(
            None,
            validation_alias=AliasChoices("rateItemCharge", "rate_item_charge"),
            serialization_alias="rateItemCharge",
        ),
    ]

    rate_item_name_localization: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "rateItemNameLocalization", "rate_item_name_localization"
            ),
            serialization_alias="rateItemNameLocalization",
            description="Used for the localization.",
        ),
    ]


"""
RequestedValueAddedService

A value-added service to be applied to a shipping service purchase.
"""


class RequestedValueAddedService(SpApiBaseModel):
    """A value-added service to be applied to a shipping service purchase."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    id: Annotated[
        str,
        Field(
            ...,
            description="The identifier of the selected value-added service. Must be among those returned in the response to the getRates operation.",
        ),
    ]


"""
SubmitNdrFeedbackRequestBody

The request schema for the NdrFeedback operation
"""


class SubmitNdrFeedbackRequestBody(SpApiBaseModel):
    """The request schema for the NdrFeedback operation"""

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

    ndr_action: Annotated[
        "NdrAction",
        Field(
            ...,
            validation_alias=AliasChoices("ndrAction", "ndr_action"),
            serialization_alias="ndrAction",
        ),
    ]

    ndr_request_data: Annotated[
        Optional["NdrRequestData"],
        Field(
            None,
            validation_alias=AliasChoices("ndrRequestData", "ndr_request_data"),
            serialization_alias="ndrRequestData",
        ),
    ]


"""
SubmitNdrFeedbackRequest

Request parameters for submitNdrFeedback
"""


class SubmitNdrFeedbackRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for submitNdrFeedback
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    body: Annotated[
        "SubmitNdrFeedbackRequestBody",
        BodyParam(),
        Field(..., description="[BODY] RequestBody body for ndrFeedback operation"),
    ]


"""
SupportedDocumentSpecification

Document specification that is supported for a service offering.
"""


class SupportedDocumentSpecification(SpApiBaseModel):
    """Document specification that is supported for a service offering."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    format: Annotated[
        "DocumentFormat",
        Field(
            ...,
        ),
    ]

    size: Annotated[
        "DocumentSize",
        Field(
            ...,
        ),
    ]

    print_options: Annotated[
        "PrintOptionList",
        Field(
            ...,
            validation_alias=AliasChoices("printOptions", "print_options"),
            serialization_alias="printOptions",
        ),
    ]


TaxType = str
"""Indicates the type of tax."""


"""
TaxDetail

Indicates the tax specifications associated with the shipment for customs compliance purposes in certain regions.
"""


class TaxDetail(SpApiBaseModel):
    """Indicates the tax specifications associated with the shipment for customs compliance purposes in certain regions."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    tax_type: Annotated[
        "TaxType",
        Field(
            ...,
            validation_alias=AliasChoices("taxType", "tax_type"),
            serialization_alias="taxType",
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
            description="The shipper's tax registration number associated with the shipment for customs compliance purposes in certain regions.",
        ),
    ]


"""
UnlinkCarrierAccountRequestBody

The request schema for remove the Carrier Account associated with the provided merchant.
"""


class UnlinkCarrierAccountRequestBody(SpApiBaseModel):
    """The request schema for remove the Carrier Account associated with the provided merchant."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    client_reference_details: Annotated[
        Optional["ClientReferenceDetails"],
        Field(
            None,
            validation_alias=AliasChoices(
                "clientReferenceDetails", "client_reference_details"
            ),
            serialization_alias="clientReferenceDetails",
        ),
    ]

    account_id: Annotated[
        Optional["AccountId"],
        Field(
            None,
            validation_alias=AliasChoices("accountId", "account_id"),
            serialization_alias="accountId",
        ),
    ]


"""
UnlinkCarrierAccountRequest

Request parameters for unlinkCarrierAccount
"""


class UnlinkCarrierAccountRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for unlinkCarrierAccount
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    carrier_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("carrierId", "carrier_id"),
            serialization_alias="carrierId",
            description="[PATH] carrier Id to unlink with merchant.",
        ),
    ]

    body: Annotated[
        "UnlinkCarrierAccountRequestBody",
        BodyParam(),
        Field(..., description="[BODY] UnlinkCarrierAccountRequestBody body"),
    ]


"""
UnlinkCarrierAccountResponse

The Response for the UnlinkCarrierAccountResponse operation.
"""


class UnlinkCarrierAccountResponse(SpApiBaseModel):
    """The Response for the UnlinkCarrierAccountResponse operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    is_unlinked: Annotated[
        Optional[bool],
        Field(
            None,
            validation_alias=AliasChoices("isUnlinked", "is_unlinked"),
            serialization_alias="isUnlinked",
            description="Is Carrier unlinked from Merchant",
        ),
    ]


UnmanifestedShipmentLocationList = List["UnmanifestedShipmentLocation"]
"""A list of UnmanifestedShipmentLocation"""


"""
UnmanifestedCarrierInformation

UnmanifestedCarrierInformation like carrierId CarrierName and Location
"""


class UnmanifestedCarrierInformation(SpApiBaseModel):
    """UnmanifestedCarrierInformation like carrierId CarrierName and Location"""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    carrier_id: Annotated[
        Optional["CarrierId"],
        Field(
            None,
            validation_alias=AliasChoices("carrierId", "carrier_id"),
            serialization_alias="carrierId",
        ),
    ]

    carrier_name: Annotated[
        Optional["CarrierName"],
        Field(
            None,
            validation_alias=AliasChoices("carrierName", "carrier_name"),
            serialization_alias="carrierName",
        ),
    ]

    unmanifested_shipment_location_list: Annotated[
        Optional["UnmanifestedShipmentLocationList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "unmanifestedShipmentLocationList",
                "unmanifested_shipment_location_list",
            ),
            serialization_alias="unmanifestedShipmentLocationList",
        ),
    ]


"""
UnmanifestedShipmentLocation

UnmanifestedShipmentLocation info 
"""


class UnmanifestedShipmentLocation(SpApiBaseModel):
    """UnmanifestedShipmentLocation info"""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    address: Annotated[
        Optional["Address"],
        Field(
            None,
        ),
    ]

    last_manifest_date: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("lastManifestDate", "last_manifest_date"),
            serialization_alias="lastManifestDate",
            description="Its Last Manifest Date.",
        ),
    ]


"""
ValidationMetadata

ValidationMetadata Details
"""


class ValidationMetadata(SpApiBaseModel):
    """ValidationMetadata Details"""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    error_message: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("errorMessage", "error_message"),
            serialization_alias="errorMessage",
            description="errorMessage for the error.",
        ),
    ]

    validation_strategy: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("validationStrategy", "validation_strategy"),
            serialization_alias="validationStrategy",
            description="validationStrategy for the error.",
        ),
    ]

    value: Annotated[Optional[str], Field(None, description="Value.")]


# Rebuild models to resolve forward references
Error.model_rebuild()
ErrorList.model_rebuild()
Weight.model_rebuild()
LiquidVolume.model_rebuild()
InvoiceDetails.model_rebuild()
ChargeComponent.model_rebuild()
Currency.model_rebuild()
Dimensions.model_rebuild()
TrackingDetailCodes.model_rebuild()
ShipperInstruction.model_rebuild()
Address.model_rebuild()
Geocode.model_rebuild()
Location.model_rebuild()
RequestedLabelCustomization.model_rebuild()
PackageDocument.model_rebuild()
PrintOption.model_rebuild()
DocumentSize.model_rebuild()
SupportedDocumentDetail.model_rebuild()
RequestedDocumentSpecification.model_rebuild()
SupportedDocumentSpecification.model_rebuild()
Item.model_rebuild()
Package.model_rebuild()
DirectFulfillmentItemIdentifiers.model_rebuild()
PackageDocumentDetail.model_rebuild()
TimeWindow.model_rebuild()
Promise.model_rebuild()
RequestedValueAddedService.model_rebuild()
AvailableValueAddedServiceGroup.model_rebuild()
ValueAddedService.model_rebuild()
CollectOnDelivery.model_rebuild()
ValueAddedServiceDetails.model_rebuild()
DangerousGoodsDetails.model_rebuild()
TaxDetail.model_rebuild()
GoodsOwner.model_rebuild()
Event.model_rebuild()
TrackingSummary.model_rebuild()
AmazonOrderDetails.model_rebuild()
AmazonShipmentDetails.model_rebuild()
ChannelDetails.model_rebuild()
Rate.model_rebuild()
IneligibilityReason.model_rebuild()
IneligibleRate.model_rebuild()
CancelShipmentResult.model_rebuild()
CancelShipmentResponse.model_rebuild()
GetRatesRequestBody.model_rebuild()
AccessPointDetails.model_rebuild()
NdrRequestData.model_rebuild()
ClaimProofURLs.model_rebuild()
GetRatesResult.model_rebuild()
GetRatesResponse.model_rebuild()
DirectPurchaseRequestBody.model_rebuild()
DirectPurchaseResult.model_rebuild()
DirectPurchaseResponse.model_rebuild()
GetShipmentDocumentsResult.model_rebuild()
GetShipmentDocumentsResponse.model_rebuild()
GetTrackingResult.model_rebuild()
SubmitNdrFeedbackRequestBody.model_rebuild()
CreateClaimRequestBody.model_rebuild()
GetTrackingResponse.model_rebuild()
CreateClaimResponse.model_rebuild()
PurchaseShipmentRequestBody.model_rebuild()
PurchaseShipmentResult.model_rebuild()
PurchaseShipmentResponse.model_rebuild()
OneClickShipmentRequestBody.model_rebuild()
OneClickShipmentResponse.model_rebuild()
OneClickShipmentResult.model_rebuild()
GetAccessPointsResponse.model_rebuild()
GetAccessPointsResult.model_rebuild()
AccessPointsMap.model_rebuild()
AccessPoint.model_rebuild()
AccessibilityAttributes.model_rebuild()
OperatingHours.model_rebuild()
TimeOfDay.model_rebuild()
DayOfWeekTimeMap.model_rebuild()
ExceptionOperatingHours.model_rebuild()
GetAdditionalInputsResult.model_rebuild()
GetAdditionalInputsResponse.model_rebuild()
GetCarrierAccountsRequestBody.model_rebuild()
LinkCarrierAccountRequestBody.model_rebuild()
UnlinkCarrierAccountRequestBody.model_rebuild()
GenerateCollectionFormRequestBody.model_rebuild()
GetCollectionFormHistoryRequestBody.model_rebuild()
GetUnmanifestedShipmentsRequestBody.model_rebuild()
GetCarrierAccountFormInputsResponse.model_rebuild()
GetCarrierAccountsResponse.model_rebuild()
LinkCarrierAccountResponse.model_rebuild()
UnlinkCarrierAccountResponse.model_rebuild()
GenerateCollectionFormResponse.model_rebuild()
GetCollectionFormHistoryResponse.model_rebuild()
GetUnmanifestedShipmentsResponse.model_rebuild()
GetCollectionFormResponse.model_rebuild()
ClientReferenceDetail.model_rebuild()
CarrierAccount.model_rebuild()
ActiveAccount.model_rebuild()
DateRange.model_rebuild()
CarrierAccountAttribute.model_rebuild()
CollectionsFormDocument.model_rebuild()
CollectionFormsHistoryRecord.model_rebuild()
UnmanifestedCarrierInformation.model_rebuild()
UnmanifestedShipmentLocation.model_rebuild()
LinkableCarrier.model_rebuild()
LinkableAccountType.model_rebuild()
CarrierAccountInput.model_rebuild()
ValidationMetadata.model_rebuild()
RateItem.model_rebuild()
Benefits.model_rebuild()
IncludedBenefits.model_rebuild()
ExcludedBenefit.model_rebuild()
ExcludedBenefitReasonCodes.model_rebuild()
ServiceSelection.model_rebuild()
ServiceIds.model_rebuild()
OneClickShipmentValueAddedService.model_rebuild()
Service.model_rebuild()
Carrier.model_rebuild()
GetRatesRequest.model_rebuild()
DirectPurchaseShipmentRequest.model_rebuild()
PurchaseShipmentRequest.model_rebuild()
OneClickShipmentRequest.model_rebuild()
GetTrackingRequest.model_rebuild()
GetShipmentDocumentsRequest.model_rebuild()
CancelShipmentRequest.model_rebuild()
GetAdditionalInputsRequest.model_rebuild()
GetCarrierAccountsRequest.model_rebuild()
LinkCarrierAccountRequest.model_rebuild()
UnlinkCarrierAccountRequest.model_rebuild()
GenerateCollectionFormRequest.model_rebuild()
GetCollectionFormHistoryRequest.model_rebuild()
GetUnmanifestedShipmentsRequest.model_rebuild()
GetCollectionFormRequest.model_rebuild()
GetAccessPointsRequest.model_rebuild()
SubmitNdrFeedbackRequest.model_rebuild()
CreateClaimRequest.model_rebuild()
