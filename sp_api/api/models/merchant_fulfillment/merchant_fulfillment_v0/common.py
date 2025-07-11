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

AddressLine1 = str
"""The street address information."""


AddressLine2 = str
"""Additional street address information."""


AddressLine3 = str
"""Additional street address information."""


AddressName = str
"""The name of the addressee, or business name."""


City = str
"""The city."""


CountryCode = str
"""The two-letter country code in [ISO 3166-1 alpha-2](https://www.iban.com/country-codes) format."""


DistrictOrCounty = str
"""The district or county."""


EmailAddress = str
"""The email address."""


PhoneNumber = str
"""The phone number."""


PostalCode = str
"""The zip code or postal code."""


StateOrProvinceCode = str
"""The state or province code. This is a required field in Canada, US, and UK marketplaces, and for shipments that originate in China."""


"""
Address

The postal address information.
"""


class Address(SpApiBaseModel):
    """The postal address information."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    name: Annotated[
        "AddressName",
        Field(
            ...,
            validation_alias=AliasChoices("Name", "name"),
            serialization_alias="Name",
        ),
    ]

    address_line1: Annotated[
        "AddressLine1",
        Field(
            ...,
            validation_alias=AliasChoices("AddressLine1", "address_line1"),
            serialization_alias="AddressLine1",
        ),
    ]

    address_line2: Annotated[
        Optional["AddressLine2"],
        Field(
            None,
            validation_alias=AliasChoices("AddressLine2", "address_line2"),
            serialization_alias="AddressLine2",
        ),
    ]

    address_line3: Annotated[
        Optional["AddressLine3"],
        Field(
            None,
            validation_alias=AliasChoices("AddressLine3", "address_line3"),
            serialization_alias="AddressLine3",
        ),
    ]

    district_or_county: Annotated[
        Optional["DistrictOrCounty"],
        Field(
            None,
            validation_alias=AliasChoices("DistrictOrCounty", "district_or_county"),
            serialization_alias="DistrictOrCounty",
        ),
    ]

    email: Annotated[
        "EmailAddress",
        Field(
            ...,
            validation_alias=AliasChoices("Email", "email"),
            serialization_alias="Email",
        ),
    ]

    city: Annotated[
        "City",
        Field(
            ...,
            validation_alias=AliasChoices("City", "city"),
            serialization_alias="City",
        ),
    ]

    state_or_province_code: Annotated[
        Optional["StateOrProvinceCode"],
        Field(
            None,
            validation_alias=AliasChoices(
                "StateOrProvinceCode", "state_or_province_code"
            ),
            serialization_alias="StateOrProvinceCode",
        ),
    ]

    postal_code: Annotated[
        "PostalCode",
        Field(
            ...,
            validation_alias=AliasChoices("PostalCode", "postal_code"),
            serialization_alias="PostalCode",
        ),
    ]

    country_code: Annotated[
        "CountryCode",
        Field(
            ...,
            validation_alias=AliasChoices("CountryCode", "country_code"),
            serialization_alias="CountryCode",
        ),
    ]

    phone: Annotated[
        "PhoneNumber",
        Field(
            ...,
            validation_alias=AliasChoices("Phone", "phone"),
            serialization_alias="Phone",
        ),
    ]


"""
CurrencyAmount

Currency type and amount.
"""


class CurrencyAmount(SpApiBaseModel):
    """Currency type and amount."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    currency_code: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("CurrencyCode", "currency_code"),
            serialization_alias="CurrencyCode",
            description="Three-digit currency code in ISO 4217 format.",
        ),
    ]

    amount: Annotated[
        float,
        Field(
            ...,
            validation_alias=AliasChoices("Amount", "amount"),
            serialization_alias="Amount",
            description="The currency amount.",
        ),
    ]


UnitOfLength = str
"""The unit of length."""


"""
Length

The length.
"""


class Length(SpApiBaseModel):
    """The length."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    value: Annotated[Optional[float], Field(None, description="The value in units.")]

    unit: Annotated[
        Optional["UnitOfLength"],
        Field(
            None,
        ),
    ]


Timestamp = str
"""Date-time formatted timestamp."""


UnitOfWeight = str
"""The unit of weight."""


WeightValue = float
"""The weight value."""


"""
Weight

The weight.
"""


class Weight(SpApiBaseModel):
    """The weight."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    value: Annotated[
        "WeightValue",
        Field(
            ...,
            validation_alias=AliasChoices("Value", "value"),
            serialization_alias="Value",
        ),
    ]

    unit: Annotated[
        "UnitOfWeight",
        Field(
            ...,
            validation_alias=AliasChoices("Unit", "unit"),
            serialization_alias="Unit",
        ),
    ]


"""
AdditionalSellerInput

Additional information required to purchase shipping.
"""


class AdditionalSellerInput(SpApiBaseModel):
    """Additional information required to purchase shipping."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    data_type: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("DataType", "data_type"),
            serialization_alias="DataType",
            description="The data type of the additional information.",
        ),
    ]

    value_as_string: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("ValueAsString", "value_as_string"),
            serialization_alias="ValueAsString",
            description="The value when the data type is string.",
        ),
    ]

    value_as_boolean: Annotated[
        Optional[bool],
        Field(
            None,
            validation_alias=AliasChoices("ValueAsBoolean", "value_as_boolean"),
            serialization_alias="ValueAsBoolean",
            description="The value when the data type is boolean.",
        ),
    ]

    value_as_integer: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices("ValueAsInteger", "value_as_integer"),
            serialization_alias="ValueAsInteger",
            description="The value when the data type is integer.",
        ),
    ]

    value_as_timestamp: Annotated[
        Optional["Timestamp"],
        Field(
            None,
            validation_alias=AliasChoices("ValueAsTimestamp", "value_as_timestamp"),
            serialization_alias="ValueAsTimestamp",
            description="The value when the data type is a date-time formatted string.",
        ),
    ]

    value_as_address: Annotated[
        Optional["Address"],
        Field(
            None,
            validation_alias=AliasChoices("ValueAsAddress", "value_as_address"),
            serialization_alias="ValueAsAddress",
        ),
    ]

    value_as_weight: Annotated[
        Optional["Weight"],
        Field(
            None,
            validation_alias=AliasChoices("ValueAsWeight", "value_as_weight"),
            serialization_alias="ValueAsWeight",
        ),
    ]

    value_as_dimension: Annotated[
        Optional["Length"],
        Field(
            None,
            validation_alias=AliasChoices("ValueAsDimension", "value_as_dimension"),
            serialization_alias="ValueAsDimension",
        ),
    ]

    value_as_currency: Annotated[
        Optional["CurrencyAmount"],
        Field(
            None,
            validation_alias=AliasChoices("ValueAsCurrency", "value_as_currency"),
            serialization_alias="ValueAsCurrency",
        ),
    ]


Constraints = List["Constraint"]
"""List of constraints."""


InputTargetType = str
"""Indicates whether the additional seller input is at the item or shipment level."""


"""
RestrictedSetValues

The set of fixed values in an additional seller input.
"""


class RestrictedSetValues(SpApiBaseModel):
    """The set of fixed values in an additional seller input."""

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow",
        serialize_by_alias=True,
        arbitrary_types_allowed=True,
    )


"""
SellerInputDefinition

Specifies characteristics that apply to a seller input.
"""


class SellerInputDefinition(SpApiBaseModel):
    """Specifies characteristics that apply to a seller input."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    is_required: Annotated[
        bool,
        Field(
            ...,
            validation_alias=AliasChoices("IsRequired", "is_required"),
            serialization_alias="IsRequired",
            description="When true, the additional input field is required.",
        ),
    ]

    data_type: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("DataType", "data_type"),
            serialization_alias="DataType",
            description="The data type of the additional input field.",
        ),
    ]

    constraints: Annotated[
        "Constraints",
        Field(
            ...,
            validation_alias=AliasChoices("Constraints", "constraints"),
            serialization_alias="Constraints",
        ),
    ]

    input_display_text: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("InputDisplayText", "input_display_text"),
            serialization_alias="InputDisplayText",
            description="The display text for the additional input field.",
        ),
    ]

    input_target: Annotated[
        Optional["InputTargetType"],
        Field(
            None,
            validation_alias=AliasChoices("InputTarget", "input_target"),
            serialization_alias="InputTarget",
            description="Whether the seller input applies to the item or the shipment.",
        ),
    ]

    stored_value: Annotated[
        "AdditionalSellerInput",
        Field(
            ...,
            validation_alias=AliasChoices("StoredValue", "stored_value"),
            serialization_alias="StoredValue",
        ),
    ]

    restricted_set_values: Annotated[
        Optional["RestrictedSetValues"],
        Field(
            None,
            validation_alias=AliasChoices(
                "RestrictedSetValues", "restricted_set_values"
            ),
            serialization_alias="RestrictedSetValues",
        ),
    ]


"""
AdditionalInputs

Maps the additional seller input to the definition. The key to the map is the field name.
"""


class AdditionalInputs(SpApiBaseModel):
    """Maps the additional seller input to the definition. The key to the map is the field name."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    additional_input_field_name: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "AdditionalInputFieldName", "additional_input_field_name"
            ),
            serialization_alias="AdditionalInputFieldName",
            description="The field name.",
        ),
    ]

    seller_input_definition: Annotated[
        Optional["SellerInputDefinition"],
        Field(
            None,
            validation_alias=AliasChoices(
                "SellerInputDefinition", "seller_input_definition"
            ),
            serialization_alias="SellerInputDefinition",
        ),
    ]


AdditionalInputsList = List["AdditionalInputs"]
"""A list of additional inputs."""


"""
AdditionalSellerInputs

An additional set of seller inputs required to purchase shipping.
"""


class AdditionalSellerInputs(SpApiBaseModel):
    """An additional set of seller inputs required to purchase shipping."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    additional_input_field_name: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices(
                "AdditionalInputFieldName", "additional_input_field_name"
            ),
            serialization_alias="AdditionalInputFieldName",
            description="The name of the additional input field.",
        ),
    ]

    additional_seller_input: Annotated[
        "AdditionalSellerInput",
        Field(
            ...,
            validation_alias=AliasChoices(
                "AdditionalSellerInput", "additional_seller_input"
            ),
            serialization_alias="AdditionalSellerInput",
        ),
    ]


AdditionalSellerInputsList = List["AdditionalSellerInputs"]
"""A list of additional seller input pairs required to purchase shipping."""


AmazonOrderId = str
"""An Amazon-defined order identifier, in 3-7-7 format."""


CarrierWillPickUpOption = str
"""Carrier will pick up option."""


"""
AvailableCarrierWillPickUpOption

Indicates whether the carrier will pick up the package, and what fee is charged, if any.
"""


class AvailableCarrierWillPickUpOption(SpApiBaseModel):
    """Indicates whether the carrier will pick up the package, and what fee is charged, if any."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    carrier_will_pick_up_option: Annotated[
        "CarrierWillPickUpOption",
        Field(
            ...,
            validation_alias=AliasChoices(
                "CarrierWillPickUpOption", "carrier_will_pick_up_option"
            ),
            serialization_alias="CarrierWillPickUpOption",
        ),
    ]

    charge: Annotated[
        "CurrencyAmount",
        Field(
            ...,
            validation_alias=AliasChoices("Charge", "charge"),
            serialization_alias="Charge",
            description="The fee charged.",
        ),
    ]


AvailableCarrierWillPickUpOptionsList = List["AvailableCarrierWillPickUpOption"]
"""List of available carrier pickup options."""


DeliveryExperienceOption = str
"""The delivery confirmation level."""


"""
AvailableDeliveryExperienceOption

The available delivery confirmation options, and the fee charged, if any.
"""


class AvailableDeliveryExperienceOption(SpApiBaseModel):
    """The available delivery confirmation options, and the fee charged, if any."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    delivery_experience_option: Annotated[
        "DeliveryExperienceOption",
        Field(
            ...,
            validation_alias=AliasChoices(
                "DeliveryExperienceOption", "delivery_experience_option"
            ),
            serialization_alias="DeliveryExperienceOption",
        ),
    ]

    charge: Annotated[
        "CurrencyAmount",
        Field(
            ...,
            validation_alias=AliasChoices("Charge", "charge"),
            serialization_alias="Charge",
        ),
    ]


AvailableDeliveryExperienceOptionsList = List["AvailableDeliveryExperienceOption"]
"""List of available delivery experience options."""


AvailableFormatOptionsForLabel = List["LabelFormatOption"]
"""The available label formats."""


AvailableFormatOptionsForLabelList = List["LabelFormatOption"]
"""The available label formats."""


"""
AvailableShippingServiceOptions

The available shipping service options.
"""


class AvailableShippingServiceOptions(SpApiBaseModel):
    """The available shipping service options."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    available_carrier_will_pick_up_options: Annotated[
        "AvailableCarrierWillPickUpOptionsList",
        Field(
            ...,
            validation_alias=AliasChoices(
                "AvailableCarrierWillPickUpOptions",
                "available_carrier_will_pick_up_options",
            ),
            serialization_alias="AvailableCarrierWillPickUpOptions",
        ),
    ]

    available_delivery_experience_options: Annotated[
        "AvailableDeliveryExperienceOptionsList",
        Field(
            ...,
            validation_alias=AliasChoices(
                "AvailableDeliveryExperienceOptions",
                "available_delivery_experience_options",
            ),
            serialization_alias="AvailableDeliveryExperienceOptions",
        ),
    ]


ExcludedBenefits = List["ExcludedBenefit"]
"""A list of excluded benefits. Refer to the `ExcludeBenefit` object for further documentation."""


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

Benefits that are included and excluded for each shipping offer. Benefits represents services provided by Amazon (for example, `CLAIMS_PROTECTED`) when sellers purchase shipping through Amazon. Benefit details are made available for any shipment placed on or after January 1st 2024 00:00 UTC.
"""


class Benefits(SpApiBaseModel):
    """Benefits that are included and excluded for each shipping offer. Benefits represents services provided by Amazon (for example, `CLAIMS_PROTECTED`) when sellers purchase shipping through Amazon. Benefit details are made available for any shipment placed on or after January 1st 2024 00:00 UTC."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    included_benefits: Annotated[
        Optional["IncludedBenefits"],
        Field(
            None,
            validation_alias=AliasChoices("IncludedBenefits", "included_benefits"),
            serialization_alias="IncludedBenefits",
        ),
    ]

    excluded_benefits: Annotated[
        Optional["ExcludedBenefits"],
        Field(
            None,
            validation_alias=AliasChoices("ExcludedBenefits", "excluded_benefits"),
            serialization_alias="ExcludedBenefits",
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
            description="[PATH] The Amazon-defined shipment identifier for the shipment to cancel.",
        ),
    ]


ErrorList = List["Error"]
"""A list of error responses returned when a request is unsuccessful."""


ItemList = List["Item"]
"""The list of items you want to include in a shipment."""


CustomTextForLabel = str
"""Custom text to print on the label. Note: Custom text is only included on labels that are in ZPL format (ZPL203). FedEx does not support `CustomTextForLabel`."""


FileType = str
"""The file type for a label."""


"""
FileContents

The document data and checksum.
"""


class FileContents(SpApiBaseModel):
    """The document data and checksum."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    contents: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("Contents", "contents"),
            serialization_alias="Contents",
            description="Data for printing labels encoded into a Base64, GZip-compressed string.",
        ),
    ]

    file_type: Annotated[
        "FileType",
        Field(
            ...,
            validation_alias=AliasChoices("FileType", "file_type"),
            serialization_alias="FileType",
        ),
    ]

    checksum: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("Checksum", "checksum"),
            serialization_alias="Checksum",
            description="An MD5 hash to validate the PDF document data, in the form of a Base64 string.",
        ),
    ]


LabelDimension = float
"""A label dimension."""


"""
LabelDimensions

Dimensions for printing a shipping label.
"""


class LabelDimensions(SpApiBaseModel):
    """Dimensions for printing a shipping label."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    length: Annotated[
        "LabelDimension",
        Field(
            ...,
            validation_alias=AliasChoices("Length", "length"),
            serialization_alias="Length",
            description="The length dimension.",
        ),
    ]

    width: Annotated[
        "LabelDimension",
        Field(
            ...,
            validation_alias=AliasChoices("Width", "width"),
            serialization_alias="Width",
            description="The width dimension.",
        ),
    ]

    unit: Annotated[
        "UnitOfLength",
        Field(
            ...,
            validation_alias=AliasChoices("Unit", "unit"),
            serialization_alias="Unit",
            description="The unit of measurement.",
        ),
    ]


LabelFormat = str
"""The label format."""


StandardIdForLabel = str
"""The type of standard identifier to print on the label."""


"""
Label

Data for creating a shipping label and dimensions for printing the label.
"""


class Label(SpApiBaseModel):
    """Data for creating a shipping label and dimensions for printing the label."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    custom_text_for_label: Annotated[
        Optional["CustomTextForLabel"],
        Field(
            None,
            validation_alias=AliasChoices(
                "CustomTextForLabel", "custom_text_for_label"
            ),
            serialization_alias="CustomTextForLabel",
        ),
    ]

    dimensions: Annotated[
        "LabelDimensions",
        Field(
            ...,
            validation_alias=AliasChoices("Dimensions", "dimensions"),
            serialization_alias="Dimensions",
        ),
    ]

    file_contents: Annotated[
        "FileContents",
        Field(
            ...,
            validation_alias=AliasChoices("FileContents", "file_contents"),
            serialization_alias="FileContents",
        ),
    ]

    label_format: Annotated[
        Optional["LabelFormat"],
        Field(
            None,
            validation_alias=AliasChoices("LabelFormat", "label_format"),
            serialization_alias="LabelFormat",
        ),
    ]

    standard_id_for_label: Annotated[
        Optional["StandardIdForLabel"],
        Field(
            None,
            validation_alias=AliasChoices(
                "StandardIdForLabel", "standard_id_for_label"
            ),
            serialization_alias="StandardIdForLabel",
        ),
    ]


PackageDimension = float
"""A number that represents the given package dimension."""


PredefinedPackageDimensions = str
"""An enumeration of predefined parcel tokens. If you specify a `PredefinedPackageDimensions` token, you are not obligated to use a branded package from a carrier. For example, if you specify the `FedEx_Box_10kg` token, you do not have to use that particular package from FedEx. You are only obligated to use a box that matches the dimensions specified by the token. Note: Carriers can have restrictions on the type of package allowed for certain ship methods. Check the carrier website for details. Example: Flat rate pricing is available when materials are sent by USPS in a USPS-produced Flat Rate envelope or box."""


"""
PackageDimensions

The dimensions of a package contained in a shipment.
"""


class PackageDimensions(SpApiBaseModel):
    """The dimensions of a package contained in a shipment."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    length: Annotated[
        Optional["PackageDimension"],
        Field(
            None,
            validation_alias=AliasChoices("Length", "length"),
            serialization_alias="Length",
            description="The length dimension. If you don't specify `PredefinedPackageDimensions`, you must specify the length.",
        ),
    ]

    width: Annotated[
        Optional["PackageDimension"],
        Field(
            None,
            validation_alias=AliasChoices("Width", "width"),
            serialization_alias="Width",
            description="The width dimension. If you don't specify `PredefinedPackageDimensions`, you must specify the width.",
        ),
    ]

    height: Annotated[
        Optional["PackageDimension"],
        Field(
            None,
            validation_alias=AliasChoices("Height", "height"),
            serialization_alias="Height",
            description="The height dimension. If you don't specify `PredefinedPackageDimensions`, you must specify the height.",
        ),
    ]

    unit: Annotated[
        Optional["UnitOfLength"],
        Field(
            None,
            validation_alias=AliasChoices("Unit", "unit"),
            serialization_alias="Unit",
            description="The unit of measurement. If you don't specify `PredefinedPackageDimensions`, you must specify the unit.",
        ),
    ]

    predefined_package_dimensions: Annotated[
        Optional["PredefinedPackageDimensions"],
        Field(
            None,
            validation_alias=AliasChoices(
                "PredefinedPackageDimensions", "predefined_package_dimensions"
            ),
            serialization_alias="PredefinedPackageDimensions",
        ),
    ]


SellerOrderId = str
"""A seller-defined order identifier."""


ShipmentId = str
"""An Amazon-defined shipment identifier."""


ShipmentStatus = str
"""The shipment status."""


LabelFormatList = List["LabelFormat"]
"""List of label formats."""


ShippingServiceIdentifier = str
"""An Amazon-defined shipping service identifier."""


DeliveryExperienceType = str
"""The delivery confirmation level."""


"""
ShippingServiceOptions

Extra services provided by a carrier.
"""


class ShippingServiceOptions(SpApiBaseModel):
    """Extra services provided by a carrier."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    delivery_experience: Annotated[
        "DeliveryExperienceType",
        Field(
            ...,
            validation_alias=AliasChoices("DeliveryExperience", "delivery_experience"),
            serialization_alias="DeliveryExperience",
            description="The delivery confirmation level.",
        ),
    ]

    declared_value: Annotated[
        Optional["CurrencyAmount"],
        Field(
            None,
            validation_alias=AliasChoices("DeclaredValue", "declared_value"),
            serialization_alias="DeclaredValue",
            description="The declared value of the shipment. The carrier uses this value to determine the amount to use to insure the shipment. If `DeclaredValue` is greater than the carrier's minimum insurance amount, the seller is charged for the additional insurance, as determined by the carrier. For information about optional insurance coverage, refer to Seller Central Help: [UK](https://sellercentral.amazon.co.uk/gp/help/200204080), [US](https://sellercentral.amazon.com/gp/help/200204080).",
        ),
    ]

    carrier_will_pick_up: Annotated[
        bool,
        Field(
            ...,
            validation_alias=AliasChoices("CarrierWillPickUp", "carrier_will_pick_up"),
            serialization_alias="CarrierWillPickUp",
            description="When true, the carrier will pick up the package. Note: Scheduled carrier pickup is available only using Dynamex (US), DPD (UK), and Royal Mail (UK).",
        ),
    ]

    carrier_will_pick_up_option: Annotated[
        Optional["CarrierWillPickUpOption"],
        Field(
            None,
            validation_alias=AliasChoices(
                "CarrierWillPickUpOption", "carrier_will_pick_up_option"
            ),
            serialization_alias="CarrierWillPickUpOption",
        ),
    ]

    label_format: Annotated[
        Optional["LabelFormat"],
        Field(
            None,
            validation_alias=AliasChoices("LabelFormat", "label_format"),
            serialization_alias="LabelFormat",
            description="The seller's preferred label format.",
        ),
    ]


"""
ShippingService

A shipping service offer made by a carrier.
"""


class ShippingService(SpApiBaseModel):
    """A shipping service offer made by a carrier."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    shipping_service_name: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices(
                "ShippingServiceName", "shipping_service_name"
            ),
            serialization_alias="ShippingServiceName",
            description="A plain text representation of a carrier's shipping service. For example, 'UPS Ground' or 'FedEx Standard Overnight'. ",
        ),
    ]

    carrier_name: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("CarrierName", "carrier_name"),
            serialization_alias="CarrierName",
            description="The name of the carrier.",
        ),
    ]

    shipping_service_id: Annotated[
        "ShippingServiceIdentifier",
        Field(
            ...,
            validation_alias=AliasChoices("ShippingServiceId", "shipping_service_id"),
            serialization_alias="ShippingServiceId",
        ),
    ]

    shipping_service_offer_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices(
                "ShippingServiceOfferId", "shipping_service_offer_id"
            ),
            serialization_alias="ShippingServiceOfferId",
            description="An Amazon-defined shipping service offer identifier.",
        ),
    ]

    ship_date: Annotated[
        "Timestamp",
        Field(
            ...,
            validation_alias=AliasChoices("ShipDate", "ship_date"),
            serialization_alias="ShipDate",
            description="The date that the carrier will ship the package.",
        ),
    ]

    earliest_estimated_delivery_date: Annotated[
        Optional["Timestamp"],
        Field(
            None,
            validation_alias=AliasChoices(
                "EarliestEstimatedDeliveryDate", "earliest_estimated_delivery_date"
            ),
            serialization_alias="EarliestEstimatedDeliveryDate",
            description="The earliest date by which the shipment will be delivered.",
        ),
    ]

    latest_estimated_delivery_date: Annotated[
        Optional["Timestamp"],
        Field(
            None,
            validation_alias=AliasChoices(
                "LatestEstimatedDeliveryDate", "latest_estimated_delivery_date"
            ),
            serialization_alias="LatestEstimatedDeliveryDate",
            description="The latest date by which the shipment will be delivered.",
        ),
    ]

    rate: Annotated[
        "CurrencyAmount",
        Field(
            ...,
            validation_alias=AliasChoices("Rate", "rate"),
            serialization_alias="Rate",
            description="The amount that the carrier will charge for the shipment.",
        ),
    ]

    shipping_service_options: Annotated[
        "ShippingServiceOptions",
        Field(
            ...,
            validation_alias=AliasChoices(
                "ShippingServiceOptions", "shipping_service_options"
            ),
            serialization_alias="ShippingServiceOptions",
            description="Extra services offered by the carrier.",
        ),
    ]

    available_shipping_service_options: Annotated[
        Optional["AvailableShippingServiceOptions"],
        Field(
            None,
            validation_alias=AliasChoices(
                "AvailableShippingServiceOptions", "available_shipping_service_options"
            ),
            serialization_alias="AvailableShippingServiceOptions",
        ),
    ]

    available_label_formats: Annotated[
        Optional["LabelFormatList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "AvailableLabelFormats", "available_label_formats"
            ),
            serialization_alias="AvailableLabelFormats",
        ),
    ]

    available_format_options_for_label: Annotated[
        Optional["AvailableFormatOptionsForLabelList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "AvailableFormatOptionsForLabel", "available_format_options_for_label"
            ),
            serialization_alias="AvailableFormatOptionsForLabel",
        ),
    ]

    requires_additional_seller_inputs: Annotated[
        bool,
        Field(
            ...,
            validation_alias=AliasChoices(
                "RequiresAdditionalSellerInputs", "requires_additional_seller_inputs"
            ),
            serialization_alias="RequiresAdditionalSellerInputs",
            description="When true, additional seller inputs are required.",
        ),
    ]

    benefits: Annotated[
        Optional["Benefits"],
        Field(
            None,
            validation_alias=AliasChoices("Benefits", "benefits"),
            serialization_alias="Benefits",
        ),
    ]


TrackingId = str
"""The shipment tracking identifier provided by the carrier."""


"""
Shipment

The details of a shipment. Includes the shipment status.
"""


class Shipment(SpApiBaseModel):
    """The details of a shipment. Includes the shipment status."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    shipment_id: Annotated[
        "ShipmentId",
        Field(
            ...,
            validation_alias=AliasChoices("ShipmentId", "shipment_id"),
            serialization_alias="ShipmentId",
        ),
    ]

    amazon_order_id: Annotated[
        "AmazonOrderId",
        Field(
            ...,
            validation_alias=AliasChoices("AmazonOrderId", "amazon_order_id"),
            serialization_alias="AmazonOrderId",
        ),
    ]

    seller_order_id: Annotated[
        Optional["SellerOrderId"],
        Field(
            None,
            validation_alias=AliasChoices("SellerOrderId", "seller_order_id"),
            serialization_alias="SellerOrderId",
        ),
    ]

    item_list: Annotated[
        "ItemList",
        Field(
            ...,
            validation_alias=AliasChoices("ItemList", "item_list"),
            serialization_alias="ItemList",
        ),
    ]

    ship_from_address: Annotated[
        "Address",
        Field(
            ...,
            validation_alias=AliasChoices("ShipFromAddress", "ship_from_address"),
            serialization_alias="ShipFromAddress",
            description="The address of the sender.",
        ),
    ]

    ship_to_address: Annotated[
        "Address",
        Field(
            ...,
            validation_alias=AliasChoices("ShipToAddress", "ship_to_address"),
            serialization_alias="ShipToAddress",
            description="The destination address for the shipment.",
        ),
    ]

    package_dimensions: Annotated[
        "PackageDimensions",
        Field(
            ...,
            validation_alias=AliasChoices("PackageDimensions", "package_dimensions"),
            serialization_alias="PackageDimensions",
        ),
    ]

    weight: Annotated[
        "Weight",
        Field(
            ...,
            validation_alias=AliasChoices("Weight", "weight"),
            serialization_alias="Weight",
            description="The package weight.",
        ),
    ]

    insurance: Annotated[
        "CurrencyAmount",
        Field(
            ...,
            validation_alias=AliasChoices("Insurance", "insurance"),
            serialization_alias="Insurance",
            description="If you specify `DeclaredValue` in a previous call to the `createShipment` operation, then `Insurance` indicates the shipment insurance amount that the carrier uses. If `DeclaredValue` isn't with a previous call to the `createShipment` operation, then the shipment is insured for the carrier's minimum insurance amount, or the combined sale prices that the items are listed for in the shipment.",
        ),
    ]

    shipping_service: Annotated[
        "ShippingService",
        Field(
            ...,
            validation_alias=AliasChoices("ShippingService", "shipping_service"),
            serialization_alias="ShippingService",
        ),
    ]

    label: Annotated[
        "Label",
        Field(
            ...,
            validation_alias=AliasChoices("Label", "label"),
            serialization_alias="Label",
            description="Data for creating a shipping label and dimensions for printing the label. If the shipment is canceled, an empty label is returned.",
        ),
    ]

    status: Annotated[
        "ShipmentStatus",
        Field(
            ...,
            validation_alias=AliasChoices("Status", "status"),
            serialization_alias="Status",
            description="The shipment status.",
        ),
    ]

    tracking_id: Annotated[
        Optional["TrackingId"],
        Field(
            None,
            validation_alias=AliasChoices("TrackingId", "tracking_id"),
            serialization_alias="TrackingId",
        ),
    ]

    created_date: Annotated[
        "Timestamp",
        Field(
            ...,
            validation_alias=AliasChoices("CreatedDate", "created_date"),
            serialization_alias="CreatedDate",
            description="The date and time the shipment is created.",
        ),
    ]

    last_updated_date: Annotated[
        Optional["Timestamp"],
        Field(
            None,
            validation_alias=AliasChoices("LastUpdatedDate", "last_updated_date"),
            serialization_alias="LastUpdatedDate",
            description="The date and time of the last update.",
        ),
    ]


"""
CancelShipmentResponse

Response schema.
"""


class CancelShipmentResponse(SpApiBaseModel):
    """Response schema."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["Shipment"],
        Field(None, description="The payload for the `cancelShipment` operation."),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
            description="One or more unexpected errors occurred during the `cancelShipment` operation.",
        ),
    ]


"""
Constraint

A validation constraint.
"""


class Constraint(SpApiBaseModel):
    """A validation constraint."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    validation_reg_ex: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("ValidationRegEx", "validation_reg_ex"),
            serialization_alias="ValidationRegEx",
            description="A regular expression.",
        ),
    ]

    validation_string: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("ValidationString", "validation_string"),
            serialization_alias="ValidationString",
            description="A validation string.",
        ),
    ]


HazmatType = str
"""Hazardous materials options for a package. Consult the terms and conditions for each carrier for more information on hazardous materials."""


"""
LabelFormatOptionRequestBody

Whether to include a packing slip.
"""


class LabelFormatOptionRequestBody(SpApiBaseModel):
    """Whether to include a packing slip."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    include_packing_slip_with_label: Annotated[
        Optional[bool],
        Field(
            None,
            validation_alias=AliasChoices(
                "IncludePackingSlipWithLabel", "include_packing_slip_with_label"
            ),
            serialization_alias="IncludePackingSlipWithLabel",
            description="When true, include a packing slip with the label.",
        ),
    ]


"""
LabelCustomization

Custom text for shipping labels.
"""


class LabelCustomization(SpApiBaseModel):
    """Custom text for shipping labels."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    custom_text_for_label: Annotated[
        Optional["CustomTextForLabel"],
        Field(
            None,
            validation_alias=AliasChoices(
                "CustomTextForLabel", "custom_text_for_label"
            ),
            serialization_alias="CustomTextForLabel",
        ),
    ]

    standard_id_for_label: Annotated[
        Optional["StandardIdForLabel"],
        Field(
            None,
            validation_alias=AliasChoices(
                "StandardIdForLabel", "standard_id_for_label"
            ),
            serialization_alias="StandardIdForLabel",
        ),
    ]


"""
ShipmentRequestDetails

Shipment information required for requesting shipping service offers or for creating a shipment.
"""


class ShipmentRequestDetails(SpApiBaseModel):
    """Shipment information required for requesting shipping service offers or for creating a shipment."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    amazon_order_id: Annotated[
        "AmazonOrderId",
        Field(
            ...,
            validation_alias=AliasChoices("AmazonOrderId", "amazon_order_id"),
            serialization_alias="AmazonOrderId",
            description="An Amazon-defined order identifier in 3-7-7 format.",
        ),
    ]

    seller_order_id: Annotated[
        Optional["SellerOrderId"],
        Field(
            None,
            validation_alias=AliasChoices("SellerOrderId", "seller_order_id"),
            serialization_alias="SellerOrderId",
            description="A seller-defined order identifier.",
        ),
    ]

    item_list: Annotated[
        "ItemList",
        Field(
            ...,
            validation_alias=AliasChoices("ItemList", "item_list"),
            serialization_alias="ItemList",
        ),
    ]

    ship_from_address: Annotated[
        "Address",
        Field(
            ...,
            validation_alias=AliasChoices("ShipFromAddress", "ship_from_address"),
            serialization_alias="ShipFromAddress",
            description="The address of the sender.",
        ),
    ]

    package_dimensions: Annotated[
        "PackageDimensions",
        Field(
            ...,
            validation_alias=AliasChoices("PackageDimensions", "package_dimensions"),
            serialization_alias="PackageDimensions",
            description="The package dimensions.",
        ),
    ]

    weight: Annotated[
        "Weight",
        Field(
            ...,
            validation_alias=AliasChoices("Weight", "weight"),
            serialization_alias="Weight",
            description="The package weight.",
        ),
    ]

    must_arrive_by_date: Annotated[
        Optional["Timestamp"],
        Field(
            None,
            validation_alias=AliasChoices("MustArriveByDate", "must_arrive_by_date"),
            serialization_alias="MustArriveByDate",
            description="The date by which the package must arrive to keep the promise to the customer, in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format. If `MustArriveByDate` is specified, only shipping service offers that can be delivered by that date are returned.",
        ),
    ]

    ship_date: Annotated[
        Optional["Timestamp"],
        Field(
            None,
            validation_alias=AliasChoices("ShipDate", "ship_date"),
            serialization_alias="ShipDate",
            description="When used in a request, this is the date and time that the seller wants to ship the package. When used in a response, this is the date and time that the package can be shipped by the indicated method.",
        ),
    ]

    shipping_service_options: Annotated[
        "ShippingServiceOptions",
        Field(
            ...,
            validation_alias=AliasChoices(
                "ShippingServiceOptions", "shipping_service_options"
            ),
            serialization_alias="ShippingServiceOptions",
            description="Extra services offered by the carrier.",
        ),
    ]

    label_customization: Annotated[
        Optional["LabelCustomization"],
        Field(
            None,
            validation_alias=AliasChoices("LabelCustomization", "label_customization"),
            serialization_alias="LabelCustomization",
            description="Label customization options.",
        ),
    ]


"""
CreateShipmentRequestBody

RequestBody schema.
"""


class CreateShipmentRequestBody(SpApiBaseModel):
    """RequestBody schema."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    shipment_request_details: Annotated[
        "ShipmentRequestDetails",
        Field(
            ...,
            validation_alias=AliasChoices(
                "ShipmentRequestDetails", "shipment_request_details"
            ),
            serialization_alias="ShipmentRequestDetails",
            description="Shipment information required to create a shipment.",
        ),
    ]

    shipping_service_id: Annotated[
        "ShippingServiceIdentifier",
        Field(
            ...,
            validation_alias=AliasChoices("ShippingServiceId", "shipping_service_id"),
            serialization_alias="ShippingServiceId",
        ),
    ]

    shipping_service_offer_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "ShippingServiceOfferId", "shipping_service_offer_id"
            ),
            serialization_alias="ShippingServiceOfferId",
            description="Identifies a shipping service order made by a carrier.",
        ),
    ]

    hazmat_type: Annotated[
        Optional["HazmatType"],
        Field(
            None,
            validation_alias=AliasChoices("HazmatType", "hazmat_type"),
            serialization_alias="HazmatType",
            description="Hazardous materials options for a package. Consult the terms and conditions for each carrier for more information about hazardous materials.",
        ),
    ]

    label_format_option: Annotated[
        Optional["LabelFormatOptionRequestBody"],
        Field(
            None,
            validation_alias=AliasChoices("LabelFormatOption", "label_format_option"),
            serialization_alias="LabelFormatOption",
        ),
    ]

    shipment_level_seller_inputs_list: Annotated[
        Optional["AdditionalSellerInputsList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "ShipmentLevelSellerInputsList", "shipment_level_seller_inputs_list"
            ),
            serialization_alias="ShipmentLevelSellerInputsList",
            description="A list of additional seller inputs required to ship this shipment.",
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
        Field(
            ...,
            description="[BODY] The request schema for the `CreateShipment` operation.",
        ),
    ]


"""
CreateShipmentResponse

Response schema.
"""


class CreateShipmentResponse(SpApiBaseModel):
    """Response schema."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["Shipment"], Field(None, description="Shipment information.")
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
            description="One or more unexpected errors occurred during the `createShipment` operation.",
        ),
    ]


# Enum definitions
class DangerousGoodsDetailsPackingGroupEnum(str, Enum):
    """Enum for PackingGroup"""

    I = "I"  # Packing group I indicates great danger.
    II = "II"  # Packing group II indicates medium danger.
    III = "III"  # Packing group III indicates minor danger.


class DangerousGoodsDetailsPackingInstructionEnum(str, Enum):
    """Enum for PackingInstruction"""

    PI965_SECTION_IA = "PI965_SECTION_IA"  # Ion PI965 Section IA (LiBa).
    PI965_SECTION_IB = "PI965_SECTION_IB"  # Ion PI965 Section IB (LiBa).
    PI965_SECTION_II = "PI965_SECTION_II"  # Ion PI965 Section II (LiBa).
    PI966_SECTION_I = "PI966_SECTION_I"  # Ion PI966 Section I (LiBa with equipment).
    PI966_SECTION_II = "PI966_SECTION_II"  # Ion PI966 Section II (LiBa with equipment).
    PI967_SECTION_I = "PI967_SECTION_I"  # Ion PI967 Section I (LiBa in equipment).
    PI967_SECTION_II = "PI967_SECTION_II"  # Ion PI967 Section II (LiBa in equipment).
    PI968_SECTION_IA = "PI968_SECTION_IA"  # Metal PI968 Section IA (LiBa).
    PI968_SECTION_IB = "PI968_SECTION_IB"  # Metal PI968 Section IB (LiBa).
    PI969_SECTION_I = "PI969_SECTION_I"  # Metal PI969 Section I (LiBa with equipment).
    PI969_SECTION_II = (
        "PI969_SECTION_II"  # Metal PI969 Section II (LiBa with equipment).
    )
    PI970_SECTION_I = "PI970_SECTION_I"  # Metal PI970 Section I (LiBa in equipment).
    PI970_SECTION_II = "PI970_SECTION_II"  # Metal PI970 Section II (LiBa in equipment).


"""
DangerousGoodsDetails

Details related to any dangerous goods or items that are shipped.
"""


class DangerousGoodsDetails(SpApiBaseModel):
    """Details related to any dangerous goods or items that are shipped."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    united_nations_regulatory_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "UnitedNationsRegulatoryId", "united_nations_regulatory_id"
            ),
            serialization_alias="UnitedNationsRegulatoryId",
            description="The specific UNID of the item being shipped.",
        ),
    ]

    transportation_regulatory_class: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "TransportationRegulatoryClass", "transportation_regulatory_class"
            ),
            serialization_alias="TransportationRegulatoryClass",
            description="The specific regulatory class of the shipped item.",
        ),
    ]

    packing_group: Annotated[
        Optional[DangerousGoodsDetailsPackingGroupEnum],
        Field(
            None,
            validation_alias=AliasChoices("PackingGroup", "packing_group"),
            serialization_alias="PackingGroup",
            description="The specific packaging group of the item being shipped.",
        ),
    ]

    packing_instruction: Annotated[
        Optional[DangerousGoodsDetailsPackingInstructionEnum],
        Field(
            None,
            validation_alias=AliasChoices("PackingInstruction", "packing_instruction"),
            serialization_alias="PackingInstruction",
            description="The specific packing instruction of the item being shipped.",
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
        str,
        Field(
            ...,
            description="A message that describes the error condition in a human-readable form.",
        ),
    ]

    details: Annotated[
        Optional[str],
        Field(
            None,
            description="Additional details that can help the caller understand or fix the issue.",
        ),
    ]


"""
ExcludedBenefitReasonCodes

List of reasons why a benefit is excluded for a shipping offer (for example, `LATE_DELIVERY_RISK`).
"""


class ExcludedBenefitReasonCodes(SpApiBaseModel):
    """List of reasons why a benefit is excluded for a shipping offer (for example, `LATE_DELIVERY_RISK`)."""

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow",
        serialize_by_alias=True,
        arbitrary_types_allowed=True,
    )


"""
ExcludedBenefit

An object representing an excluded benefit that is excluded for a shipping offer or rate.
"""


class ExcludedBenefit(SpApiBaseModel):
    """An object representing an excluded benefit that is excluded for a shipping offer or rate."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    benefit: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("Benefit", "benefit"),
            serialization_alias="Benefit",
            description="A benefit that is being excluded from a shipment.",
        ),
    ]

    reason_codes: Annotated[
        Optional["ExcludedBenefitReasonCodes"],
        Field(
            None,
            validation_alias=AliasChoices("ReasonCodes", "reason_codes"),
            serialization_alias="ReasonCodes",
        ),
    ]


"""
GetAdditionalSellerInputsRequestBody

RequestBody schema.
"""


class GetAdditionalSellerInputsRequestBody(SpApiBaseModel):
    """RequestBody schema."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    shipping_service_id: Annotated[
        "ShippingServiceIdentifier",
        Field(
            ...,
            validation_alias=AliasChoices("ShippingServiceId", "shipping_service_id"),
            serialization_alias="ShippingServiceId",
        ),
    ]

    ship_from_address: Annotated[
        "Address",
        Field(
            ...,
            validation_alias=AliasChoices("ShipFromAddress", "ship_from_address"),
            serialization_alias="ShipFromAddress",
            description="The address from which to ship.",
        ),
    ]

    order_id: Annotated[
        "AmazonOrderId",
        Field(
            ...,
            validation_alias=AliasChoices("OrderId", "order_id"),
            serialization_alias="OrderId",
            description="An Amazon defined order identifier",
        ),
    ]


"""
GetAdditionalSellerInputsRequest

Request parameters for getAdditionalSellerInputs
"""


class GetAdditionalSellerInputsRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getAdditionalSellerInputs
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    body: Annotated[
        "GetAdditionalSellerInputsRequestBody",
        BodyParam(),
        Field(
            ...,
            description="[BODY] The request schema for the `GetAdditionalSellerInputs` operation.",
        ),
    ]


ItemLevelFieldsList = List["ItemLevelFields"]
"""A list of item level fields."""


"""
GetAdditionalSellerInputsResult

The payload for the `getAdditionalSellerInputs` operation.
"""


class GetAdditionalSellerInputsResult(SpApiBaseModel):
    """The payload for the `getAdditionalSellerInputs` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    shipment_level_fields: Annotated[
        Optional["AdditionalInputsList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "ShipmentLevelFields", "shipment_level_fields"
            ),
            serialization_alias="ShipmentLevelFields",
        ),
    ]

    item_level_fields_list: Annotated[
        Optional["ItemLevelFieldsList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "ItemLevelFieldsList", "item_level_fields_list"
            ),
            serialization_alias="ItemLevelFieldsList",
        ),
    ]


"""
GetAdditionalSellerInputsResponse

Response schema.
"""


class GetAdditionalSellerInputsResponse(SpApiBaseModel):
    """Response schema."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["GetAdditionalSellerInputsResult"],
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


"""
ShippingOfferingFilter

Filter for use when requesting eligible shipping services.
"""


class ShippingOfferingFilter(SpApiBaseModel):
    """Filter for use when requesting eligible shipping services."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    include_packing_slip_with_label: Annotated[
        Optional[bool],
        Field(
            None,
            validation_alias=AliasChoices(
                "IncludePackingSlipWithLabel", "include_packing_slip_with_label"
            ),
            serialization_alias="IncludePackingSlipWithLabel",
            description="When true, include a packing slip with the label.",
        ),
    ]

    include_complex_shipping_options: Annotated[
        Optional[bool],
        Field(
            None,
            validation_alias=AliasChoices(
                "IncludeComplexShippingOptions", "include_complex_shipping_options"
            ),
            serialization_alias="IncludeComplexShippingOptions",
            description="When true, include complex shipping options.",
        ),
    ]

    carrier_will_pick_up: Annotated[
        Optional["CarrierWillPickUpOption"],
        Field(
            None,
            validation_alias=AliasChoices("CarrierWillPickUp", "carrier_will_pick_up"),
            serialization_alias="CarrierWillPickUp",
        ),
    ]

    delivery_experience: Annotated[
        Optional["DeliveryExperienceOption"],
        Field(
            None,
            validation_alias=AliasChoices("DeliveryExperience", "delivery_experience"),
            serialization_alias="DeliveryExperience",
        ),
    ]


"""
GetEligibleShipmentServicesRequestBody

RequestBody schema.
"""


class GetEligibleShipmentServicesRequestBody(SpApiBaseModel):
    """RequestBody schema."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    shipment_request_details: Annotated[
        "ShipmentRequestDetails",
        Field(
            ...,
            validation_alias=AliasChoices(
                "ShipmentRequestDetails", "shipment_request_details"
            ),
            serialization_alias="ShipmentRequestDetails",
            description="Shipment information required for requesting shipping service offers.",
        ),
    ]

    shipping_offering_filter: Annotated[
        Optional["ShippingOfferingFilter"],
        Field(
            None,
            validation_alias=AliasChoices(
                "ShippingOfferingFilter", "shipping_offering_filter"
            ),
            serialization_alias="ShippingOfferingFilter",
        ),
    ]


"""
GetEligibleShipmentServicesRequest

Request parameters for getEligibleShipmentServices
"""


class GetEligibleShipmentServicesRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getEligibleShipmentServices
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    body: Annotated[
        "GetEligibleShipmentServicesRequestBody",
        BodyParam(),
        Field(
            ...,
            description="[BODY] The request schema for the `GetEligibleShipmentServices` operation.",
        ),
    ]


RejectedShippingServiceList = List["RejectedShippingService"]
"""List of services that are for some reason unavailable for this request"""


ShippingServiceList = List["ShippingService"]
"""A list of shipping services offers."""


TemporarilyUnavailableCarrierList = List["TemporarilyUnavailableCarrier"]
"""A list of temporarily unavailable carriers."""


TermsAndConditionsNotAcceptedCarrierList = List["TermsAndConditionsNotAcceptedCarrier"]
"""List of carriers whose terms and conditions were not accepted by the seller."""


"""
GetEligibleShipmentServicesResult

The payload for the `getEligibleShipmentServices` operation.
"""


class GetEligibleShipmentServicesResult(SpApiBaseModel):
    """The payload for the `getEligibleShipmentServices` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    shipping_service_list: Annotated[
        "ShippingServiceList",
        Field(
            ...,
            validation_alias=AliasChoices(
                "ShippingServiceList", "shipping_service_list"
            ),
            serialization_alias="ShippingServiceList",
            description="A list of shipping services offers.",
        ),
    ]

    rejected_shipping_service_list: Annotated[
        Optional["RejectedShippingServiceList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "RejectedShippingServiceList", "rejected_shipping_service_list"
            ),
            serialization_alias="RejectedShippingServiceList",
        ),
    ]

    temporarily_unavailable_carrier_list: Annotated[
        Optional["TemporarilyUnavailableCarrierList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "TemporarilyUnavailableCarrierList",
                "temporarily_unavailable_carrier_list",
            ),
            serialization_alias="TemporarilyUnavailableCarrierList",
        ),
    ]

    terms_and_conditions_not_accepted_carrier_list: Annotated[
        Optional["TermsAndConditionsNotAcceptedCarrierList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "TermsAndConditionsNotAcceptedCarrierList",
                "terms_and_conditions_not_accepted_carrier_list",
            ),
            serialization_alias="TermsAndConditionsNotAcceptedCarrierList",
        ),
    ]


"""
GetEligibleShipmentServicesResponse

Response schema.
"""


class GetEligibleShipmentServicesResponse(SpApiBaseModel):
    """Response schema."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["GetEligibleShipmentServicesResult"],
        Field(
            None,
        ),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
            description="One or more unexpected errors occurred during this operation.",
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

    shipment_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("shipmentId", "shipment_id"),
            serialization_alias="shipmentId",
            description="[PATH] The Amazon-defined shipment identifier for the shipment.",
        ),
    ]


"""
GetShipmentResponse

Response schema.
"""


class GetShipmentResponse(SpApiBaseModel):
    """Response schema."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["Shipment"],
        Field(None, description="The payload for the `getShipment` operation."),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
            description="One or more unexpected errors occurred during this operation.",
        ),
    ]


ItemDescription = str
"""The description of the item."""


ItemQuantity = int
"""The number of items."""


# Enum definitions
class LiquidVolumeUnitEnum(str, Enum):
    """Enum for Unit"""

    ML = "ML"  # Milliliter - Metric unit of volume.
    L = "L"  # Liter - Metric unit of volume.
    FL_OZ = "FL_OZ"  # Fluid ounce - Imperial unit of volume.
    GAL = "GAL"  # Gallon - Imperial unit of volume.
    PT = "PT"  # Pint - Imperial unit of volume.
    QT = "QT"  # Quart - Imperial unit of volume.
    C = "C"  # Cup - Imperial unit of volume.


"""
LiquidVolume

Liquid volume.
"""


class LiquidVolume(SpApiBaseModel):
    """Liquid volume."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    unit: Annotated[
        LiquidVolumeUnitEnum,
        Field(
            ...,
            validation_alias=AliasChoices("Unit", "unit"),
            serialization_alias="Unit",
            description="The unit of measurement.",
        ),
    ]

    value: Annotated[
        float,
        Field(
            ...,
            validation_alias=AliasChoices("Value", "value"),
            serialization_alias="Value",
            description="The measurement value.",
        ),
    ]


OrderItemId = str
"""An Amazon-defined identifier for an individual item in an order."""


TransparencyCodeList = List["TransparencyCode"]
"""A list of transparency codes."""


"""
Item

An Amazon order item identifier and a quantity.
"""


class Item(SpApiBaseModel):
    """An Amazon order item identifier and a quantity."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    order_item_id: Annotated[
        "OrderItemId",
        Field(
            ...,
            validation_alias=AliasChoices("OrderItemId", "order_item_id"),
            serialization_alias="OrderItemId",
        ),
    ]

    quantity: Annotated[
        "ItemQuantity",
        Field(
            ...,
            validation_alias=AliasChoices("Quantity", "quantity"),
            serialization_alias="Quantity",
        ),
    ]

    item_weight: Annotated[
        Optional["Weight"],
        Field(
            None,
            validation_alias=AliasChoices("ItemWeight", "item_weight"),
            serialization_alias="ItemWeight",
        ),
    ]

    item_description: Annotated[
        Optional["ItemDescription"],
        Field(
            None,
            validation_alias=AliasChoices("ItemDescription", "item_description"),
            serialization_alias="ItemDescription",
        ),
    ]

    transparency_code_list: Annotated[
        Optional["TransparencyCodeList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "TransparencyCodeList", "transparency_code_list"
            ),
            serialization_alias="TransparencyCodeList",
        ),
    ]

    item_level_seller_inputs_list: Annotated[
        Optional["AdditionalSellerInputsList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "ItemLevelSellerInputsList", "item_level_seller_inputs_list"
            ),
            serialization_alias="ItemLevelSellerInputsList",
            description="A list of additional seller inputs required to ship this item using the chosen shipping service.",
        ),
    ]

    liquid_volume: Annotated[
        Optional["LiquidVolume"],
        Field(
            None,
            validation_alias=AliasChoices("LiquidVolume", "liquid_volume"),
            serialization_alias="LiquidVolume",
        ),
    ]

    is_hazmat: Annotated[
        Optional[bool],
        Field(
            None,
            validation_alias=AliasChoices("IsHazmat", "is_hazmat"),
            serialization_alias="IsHazmat",
            description="When true, the item qualifies as hazardous materials (hazmat). Defaults to false.",
        ),
    ]

    dangerous_goods_details: Annotated[
        Optional["DangerousGoodsDetails"],
        Field(
            None,
            validation_alias=AliasChoices(
                "DangerousGoodsDetails", "dangerous_goods_details"
            ),
            serialization_alias="DangerousGoodsDetails",
        ),
    ]


"""
ItemLevelFields

A list of item level fields.
"""


class ItemLevelFields(SpApiBaseModel):
    """A list of item level fields."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    asin: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("Asin", "asin"),
            serialization_alias="Asin",
            description="The Amazon Standard Identification Number (ASIN) of the item.",
        ),
    ]

    additional_inputs: Annotated[
        "AdditionalInputsList",
        Field(
            ...,
            validation_alias=AliasChoices("AdditionalInputs", "additional_inputs"),
            serialization_alias="AdditionalInputs",
        ),
    ]


"""
LabelFormatOption

The label format details and whether to include a packing slip.
"""


class LabelFormatOption(SpApiBaseModel):
    """The label format details and whether to include a packing slip."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    include_packing_slip_with_label: Annotated[
        Optional[bool],
        Field(
            None,
            validation_alias=AliasChoices(
                "IncludePackingSlipWithLabel", "include_packing_slip_with_label"
            ),
            serialization_alias="IncludePackingSlipWithLabel",
            description="When true, include a packing slip with the label.",
        ),
    ]

    label_format: Annotated[
        Optional["LabelFormat"],
        Field(
            None,
            validation_alias=AliasChoices("LabelFormat", "label_format"),
            serialization_alias="LabelFormat",
        ),
    ]


"""
RejectedShippingService

Information about a rejected shipping service
"""


class RejectedShippingService(SpApiBaseModel):
    """Information about a rejected shipping service"""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    carrier_name: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("CarrierName", "carrier_name"),
            serialization_alias="CarrierName",
            description="The rejected shipping carrier name. For example, USPS.",
        ),
    ]

    shipping_service_name: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices(
                "ShippingServiceName", "shipping_service_name"
            ),
            serialization_alias="ShippingServiceName",
            description="The rejected shipping service localized name. For example, FedEx Standard Overnight.",
        ),
    ]

    shipping_service_id: Annotated[
        "ShippingServiceIdentifier",
        Field(
            ...,
            validation_alias=AliasChoices("ShippingServiceId", "shipping_service_id"),
            serialization_alias="ShippingServiceId",
            description="The rejected shipping service identifier. For example, `FEDEX_PTP_STANDARD_OVERNIGHT`.",
        ),
    ]

    rejection_reason_code: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices(
                "RejectionReasonCode", "rejection_reason_code"
            ),
            serialization_alias="RejectionReasonCode",
            description="A reason code meant to be consumed programatically. For example, `CARRIER_CANNOT_SHIP_TO_POBOX`.",
        ),
    ]

    rejection_reason_message: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "RejectionReasonMessage", "rejection_reason_message"
            ),
            serialization_alias="RejectionReasonMessage",
            description="A localized human readable description of the rejected reason.",
        ),
    ]


"""
TemporarilyUnavailableCarrier

A carrier who is temporarily unavailable, most likely due to a service outage experienced by the carrier.
"""


class TemporarilyUnavailableCarrier(SpApiBaseModel):
    """A carrier who is temporarily unavailable, most likely due to a service outage experienced by the carrier."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    carrier_name: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("CarrierName", "carrier_name"),
            serialization_alias="CarrierName",
            description="The name of the carrier.",
        ),
    ]


"""
TermsAndConditionsNotAcceptedCarrier

A carrier whose terms and conditions have not been accepted by the seller.
"""


class TermsAndConditionsNotAcceptedCarrier(SpApiBaseModel):
    """A carrier whose terms and conditions have not been accepted by the seller."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    carrier_name: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("CarrierName", "carrier_name"),
            serialization_alias="CarrierName",
            description="The name of the carrier.",
        ),
    ]


TransparencyCode = str
"""The transparency code associated with the item. Determine the transparency serial number with: **1D or 2D barcode:** This has a **T** logo. Submit either the 29-character alpha-numeric identifier beginning with **AZ** or **ZA**, or the 38-character Serialized Global Trade Item Number (SGTIN). **2D barcode SN:** Submit the 7- to 20-character serial number barcode, that likely has the prefix **SN**. The serial number is applied to the same side of the packaging as the GTIN (UPC/EAN/ISBN) barcode. **QR code SN:** Submit the URL that the QR code generates."""


# Rebuild models to resolve forward references
Error.model_rebuild()
LabelFormatOptionRequestBody.model_rebuild()
LabelFormatOption.model_rebuild()
AvailableCarrierWillPickUpOption.model_rebuild()
AvailableDeliveryExperienceOption.model_rebuild()
AvailableShippingServiceOptions.model_rebuild()
Constraint.model_rebuild()
AdditionalInputs.model_rebuild()
SellerInputDefinition.model_rebuild()
AdditionalSellerInput.model_rebuild()
AdditionalSellerInputs.model_rebuild()
Address.model_rebuild()
Benefits.model_rebuild()
IncludedBenefits.model_rebuild()
ExcludedBenefit.model_rebuild()
ExcludedBenefitReasonCodes.model_rebuild()
CancelShipmentResponse.model_rebuild()
CreateShipmentRequestBody.model_rebuild()
CreateShipmentResponse.model_rebuild()
ItemLevelFields.model_rebuild()
GetAdditionalSellerInputsRequestBody.model_rebuild()
GetAdditionalSellerInputsResult.model_rebuild()
GetAdditionalSellerInputsResponse.model_rebuild()
CurrencyAmount.model_rebuild()
FileContents.model_rebuild()
GetEligibleShipmentServicesRequestBody.model_rebuild()
GetEligibleShipmentServicesResponse.model_rebuild()
GetEligibleShipmentServicesResult.model_rebuild()
GetShipmentResponse.model_rebuild()
Item.model_rebuild()
Label.model_rebuild()
LabelCustomization.model_rebuild()
LabelDimensions.model_rebuild()
Length.model_rebuild()
PackageDimensions.model_rebuild()
RestrictedSetValues.model_rebuild()
Shipment.model_rebuild()
ShipmentRequestDetails.model_rebuild()
ShippingOfferingFilter.model_rebuild()
ShippingService.model_rebuild()
ShippingServiceOptions.model_rebuild()
RejectedShippingService.model_rebuild()
TemporarilyUnavailableCarrier.model_rebuild()
TermsAndConditionsNotAcceptedCarrier.model_rebuild()
Weight.model_rebuild()
LiquidVolume.model_rebuild()
DangerousGoodsDetails.model_rebuild()
GetEligibleShipmentServicesRequest.model_rebuild()
GetShipmentRequest.model_rebuild()
CancelShipmentRequest.model_rebuild()
CreateShipmentRequest.model_rebuild()
GetAdditionalSellerInputsRequest.model_rebuild()
