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

Shipping address that represents the origin or destination location.
"""


class Address(SpApiBaseModel):
    """Shipping address that represents the origin or destination location."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    address_line1: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("addressLine1", "address_line1"),
            serialization_alias="addressLine1",
            description="First line of the address text.",
        ),
    ]

    address_line2: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("addressLine2", "address_line2"),
            serialization_alias="addressLine2",
            description="Optional second line of the address text.",
        ),
    ]

    address_line3: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("addressLine3", "address_line3"),
            serialization_alias="addressLine3",
            description="Optional third line of the address text.",
        ),
    ]

    city: Annotated[
        Optional[str],
        Field(None, description="Optional city where this address is located."),
    ]

    country_code: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("countryCode", "country_code"),
            serialization_alias="countryCode",
            description="Two-digit, ISO 3166-1 alpha-2 formatted country code where this address is located.",
        ),
    ]

    county: Annotated[
        Optional[str],
        Field(None, description="Optional county where this address is located."),
    ]

    district: Annotated[
        Optional[str],
        Field(None, description="Optional district where this address is located."),
    ]

    name: Annotated[
        str,
        Field(
            ...,
            description="Name of the person, business, or institution at this address.",
        ),
    ]

    phone_number: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("phoneNumber", "phone_number"),
            serialization_alias="phoneNumber",
            description="Optional E.164-formatted phone number for an available contact at this address.",
        ),
    ]

    postal_code: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("postalCode", "postal_code"),
            serialization_alias="postalCode",
            description="Optional postal code where this address is located.",
        ),
    ]

    state_or_region: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("stateOrRegion", "state_or_region"),
            serialization_alias="stateOrRegion",
            description="State or region where this address is located. Note that this is contextual to the specified country code.",
        ),
    ]


"""
CancelInboundRequest

Request parameters for cancelInbound
"""


class CancelInboundRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for cancelInbound
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    order_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("orderId", "order_id"),
            serialization_alias="orderId",
            description="[PATH] The ID of the inbound order you want to cancel.",
        ),
    ]


CarrierCodeType = str
"""Denotes the type for the carrier."""


"""
CarrierCode

Identifies the carrier that will deliver the shipment.
"""


class CarrierCode(SpApiBaseModel):
    """Identifies the carrier that will deliver the shipment."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    carrier_code_type: Annotated[
        Optional["CarrierCodeType"],
        Field(
            None,
            validation_alias=AliasChoices("carrierCodeType", "carrier_code_type"),
            serialization_alias="carrierCodeType",
            description="Denotes the carrier type.",
        ),
    ]

    carrier_code_value: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("carrierCodeValue", "carrier_code_value"),
            serialization_alias="carrierCodeValue",
            description="Value of the carrier code.",
        ),
    ]


LabelOwner = str
"""The entity that labels the products."""


PrepCategory = str
"""The preparation category for shipping an item to Amazon's fulfillment network."""


PrepOwner = str
"""The owner of the preparations, if special preparations are required."""


"""
PrepInstruction

Information pertaining to the preparation of inbound products.
"""


class PrepInstruction(SpApiBaseModel):
    """Information pertaining to the preparation of inbound products."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    prep_owner: Annotated[
        Optional["PrepOwner"],
        Field(
            None,
            validation_alias=AliasChoices("prepOwner", "prep_owner"),
            serialization_alias="prepOwner",
        ),
    ]

    prep_type: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("prepType", "prep_type"),
            serialization_alias="prepType",
            description="The type of preparation to be done. For more information about preparing items, refer to [Prep guidance](https://sellercentral.amazon.com/help/hub/reference/external/GF4G7547KSLDX2KC) on Seller Central.",
        ),
    ]


"""
PrepDetails

The preparation details for a product. This contains the prep category, prep owner, and label owner. Prep instructions are generated based on the specified category.
"""


class PrepDetails(SpApiBaseModel):
    """The preparation details for a product. This contains the prep category, prep owner, and label owner. Prep instructions are generated based on the specified category."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    label_owner: Annotated[
        Optional["LabelOwner"],
        Field(
            None,
            validation_alias=AliasChoices("labelOwner", "label_owner"),
            serialization_alias="labelOwner",
        ),
    ]

    prep_category: Annotated[
        Optional["PrepCategory"],
        Field(
            None,
            validation_alias=AliasChoices("prepCategory", "prep_category"),
            serialization_alias="prepCategory",
            description="The preparation category for shipping an item to Amazon's fulfillment network.",
        ),
    ]

    prep_instructions: Annotated[
        Optional[List["PrepInstruction"]],
        Field(
            None,
            validation_alias=AliasChoices("prepInstructions", "prep_instructions"),
            serialization_alias="prepInstructions",
            description="Contains information about the preparation of the inbound products. The system auto-generates this field with the use of the `prepCategory`, and if you attempt to pass a value for this field, the system will ignore it.",
        ),
    ]

    prep_owner: Annotated[
        Optional["PrepOwner"],
        Field(
            None,
            validation_alias=AliasChoices("prepOwner", "prep_owner"),
            serialization_alias="prepOwner",
        ),
    ]


"""
ProductAttribute

Product instance attribute that is not described at the SKU level in the catalog.
"""


class ProductAttribute(SpApiBaseModel):
    """Product instance attribute that is not described at the SKU level in the catalog."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    name: Annotated[Optional[str], Field(None, description="Product attribute name.")]

    value: Annotated[Optional[str], Field(None, description="Product attribute value.")]


"""
ProductQuantity

Represents a product with the SKU details and the corresponding quantity.
"""


class ProductQuantity(SpApiBaseModel):
    """Represents a product with the SKU details and the corresponding quantity."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    attributes: Annotated[
        Optional[List["ProductAttribute"]],
        Field(
            None,
            description="Contains attributes for this instance of the product. For example, item color, or other attributes that distinguish the product beyond the SKU. This is metadata for the product and Amazon does not process this data.",
        ),
    ]

    quantity: Annotated[int, Field(..., description="Product quantity.")]

    sku: Annotated[str, Field(..., description="The seller or merchant SKU.")]

    expiration: Annotated[
        Optional[datetime],
        Field(
            None,
            description="The expiration date for the SKU. Values are in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format.",
        ),
    ]

    prep_details: Annotated[
        Optional["PrepDetails"],
        Field(
            None,
            validation_alias=AliasChoices("prepDetails", "prep_details"),
            serialization_alias="prepDetails",
            description="Preparation details of a product which contains the prep category, prep owner and the label owner. If not passed while creating an inbound order, NO_PREP will be used on the product by-default. Prep instructions will be generated based on the category passed",
        ),
    ]


"""
DistributionPackageContents

Represents the contents inside a package, which can be products or a nested package.
"""


class DistributionPackageContents(SpApiBaseModel):
    """Represents the contents inside a package, which can be products or a nested package."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    packages: Annotated[
        Optional[List["DistributionPackageQuantity"]],
        Field(
            None,
            description="This is required only when `DistributionPackageType=PALLET`.",
        ),
    ]

    products: Annotated[
        Optional[List["ProductQuantity"]],
        Field(
            None,
            description="This is required only when `DistributionPackageType=CASE`.",
        ),
    ]


DistributionPackageType = str
"""Type of distribution packages."""


DimensionUnitOfMeasurement = str
"""Unit of measurement for package dimensions."""


"""
PackageDimensions

Dimensions of the package.
"""


class PackageDimensions(SpApiBaseModel):
    """Dimensions of the package."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    height: Annotated[float, Field(..., description="Height of the package.")]

    length: Annotated[float, Field(..., description="Length of the package.")]

    unit_of_measurement: Annotated[
        "DimensionUnitOfMeasurement",
        Field(
            ...,
            validation_alias=AliasChoices("unitOfMeasurement", "unit_of_measurement"),
            serialization_alias="unitOfMeasurement",
            description="Unit of measurement for package dimensions.",
        ),
    ]

    width: Annotated[float, Field(..., description="Width of the package.")]


VolumeUnitOfMeasurement = str
"""Unit of measurement for the package volume."""


"""
PackageVolume

Represents the volume of the package with a unit of measurement.
"""


class PackageVolume(SpApiBaseModel):
    """Represents the volume of the package with a unit of measurement."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    unit_of_measurement: Annotated[
        "VolumeUnitOfMeasurement",
        Field(
            ...,
            validation_alias=AliasChoices("unitOfMeasurement", "unit_of_measurement"),
            serialization_alias="unitOfMeasurement",
            description="Unit of measurement for the package volume.",
        ),
    ]

    volume: Annotated[float, Field(..., description="The package volume value.")]


WeightUnitOfMeasurement = str
"""Unit of measurement for the package weight."""


"""
PackageWeight

Represents the weight of the package with a unit of measurement.
"""


class PackageWeight(SpApiBaseModel):
    """Represents the weight of the package with a unit of measurement."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    unit_of_measurement: Annotated[
        "WeightUnitOfMeasurement",
        Field(
            ...,
            validation_alias=AliasChoices("unitOfMeasurement", "unit_of_measurement"),
            serialization_alias="unitOfMeasurement",
            description="Unit of measurement for the package weight.",
        ),
    ]

    weight: Annotated[float, Field(..., description="The package weight value.")]


"""
MeasurementData

Package weight and dimension.
"""


class MeasurementData(SpApiBaseModel):
    """Package weight and dimension."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    dimensions: Annotated[
        Optional["PackageDimensions"],
        Field(
            None,
            description="Dimensions of the package. Dimensions are required when creating an inbound or outbound order.",
        ),
    ]

    volume: Annotated[
        Optional["PackageVolume"], Field(None, description="Volume of the package.")
    ]

    weight: Annotated["PackageWeight", Field(..., description="Weight of the package.")]


"""
DistributionPackage

Represents an AWD distribution package.
"""


class DistributionPackage(SpApiBaseModel):
    """Represents an AWD distribution package."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    contents: Annotated[
        "DistributionPackageContents",
        Field(..., description="The contents appropriate for the type."),
    ]

    measurements: Annotated[
        "MeasurementData",
        Field(
            ...,
            description="Measurements of a package, including weight, volume, and dimensions.",
        ),
    ]

    type: Annotated[
        "DistributionPackageType",
        Field(..., description="Type of distribution package."),
    ]


"""
DistributionPackageQuantity

Represents a distribution package with its respective quantity.
"""


class DistributionPackageQuantity(SpApiBaseModel):
    """Represents a distribution package with its respective quantity."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    count: Annotated[
        int,
        Field(
            ...,
            description="Number of cases or pallets with the same package configuration.",
        ),
    ]

    distribution_package: Annotated[
        "DistributionPackage",
        Field(
            ...,
            validation_alias=AliasChoices(
                "distributionPackage", "distribution_package"
            ),
            serialization_alias="distributionPackage",
        ),
    ]


"""
InboundPackages

Represents the packages to inbound.
"""


class InboundPackages(SpApiBaseModel):
    """Represents the packages to inbound."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    packages_to_inbound: Annotated[
        List["DistributionPackageQuantity"],
        Field(
            ...,
            validation_alias=AliasChoices("packagesToInbound", "packages_to_inbound"),
            serialization_alias="packagesToInbound",
            description="List of packages to be inbounded.",
        ),
    ]


"""
CheckInboundEligibilityRequest

Request parameters for checkInboundEligibility
"""


class CheckInboundEligibilityRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for checkInboundEligibility
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    body: Annotated[
        "InboundPackages",
        BodyParam(),
        Field(..., description="[BODY] Represents the packages you want to inbound."),
    ]


"""
ConfirmInboundRequest

Request parameters for confirmInbound
"""


class ConfirmInboundRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for confirmInbound
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    order_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("orderId", "order_id"),
            serialization_alias="orderId",
            description="[PATH] The ID of the inbound order that you want to confirm.",
        ),
    ]


"""
InboundPreferences

Preferences that can be passed in context of an inbound order
"""


class InboundPreferences(SpApiBaseModel):
    """Preferences that can be passed in context of an inbound order"""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    destination_region: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("destinationRegion", "destination_region"),
            serialization_alias="destinationRegion",
            description="Pass a preferred region so that the inbound order can be shipped to an AWD warehouse located in that region. This doesn't guarantee the order to be assigned in the specified destination region as it depends on warehouse capacity availability. AWD currently supports following region IDs: [us-west, us-east, us-southcentral, us-southeast]",
        ),
    ]


"""
InboundOrderCreationData

Payload for creating an inbound order.
"""


class InboundOrderCreationData(SpApiBaseModel):
    """Payload for creating an inbound order."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    external_reference_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "externalReferenceId", "external_reference_id"
            ),
            serialization_alias="externalReferenceId",
            description="Reference ID that can be used to correlate the order with partner resources.",
        ),
    ]

    origin_address: Annotated[
        "Address",
        Field(
            ...,
            validation_alias=AliasChoices("originAddress", "origin_address"),
            serialization_alias="originAddress",
            description="Origin address from where the inbound order will be shipped.",
        ),
    ]

    packages_to_inbound: Annotated[
        List["DistributionPackageQuantity"],
        Field(
            ...,
            validation_alias=AliasChoices("packagesToInbound", "packages_to_inbound"),
            serialization_alias="packagesToInbound",
            description="List of packages to be inbounded.",
        ),
    ]

    preferences: Annotated[
        Optional["InboundPreferences"],
        Field(
            None,
        ),
    ]


"""
CreateInboundRequest

Request parameters for createInbound
"""


class CreateInboundRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for createInbound
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    body: Annotated[
        "InboundOrderCreationData",
        BodyParam(),
        Field(..., description="[BODY] Payload for creating an inbound order."),
    ]


"""
DestinationDetails

Destination details of an inbound order based on the assigned region and DC for the order.
"""


class DestinationDetails(SpApiBaseModel):
    """Destination details of an inbound order based on the assigned region and DC for the order."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    destination_address: Annotated[
        Optional["Address"],
        Field(
            None,
            validation_alias=AliasChoices("destinationAddress", "destination_address"),
            serialization_alias="destinationAddress",
            description="Destination address of the AWD facility where the shipment will be shipped to",
        ),
    ]

    destination_region: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("destinationRegion", "destination_region"),
            serialization_alias="destinationRegion",
            description="Assigned region where the order will be shipped. This can differ from what was passed as preference. AWD currently supports following region IDs: [us-west, us-east, us-southcentral, us-southeast]",
        ),
    ]

    shipment_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("shipmentId", "shipment_id"),
            serialization_alias="shipmentId",
            description="Unique ID of the confirmed shipment being shipped to the assigned destination. This will be available only after an inbound order is confirmed and can be used to track the shipment.",
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

This exception is thrown when client inputs are invalid.
"""


class ErrorList(SpApiBaseModel):
    """This exception is thrown when client inputs are invalid."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    errors: Annotated[
        List["Error"],
        Field(..., description="A list of errors describing the failures."),
    ]


"""
ExpirationDetails

The expiration details of the inventory. This object will only appear if the details parameter in the request is set to `SHOW`.
"""


class ExpirationDetails(SpApiBaseModel):
    """The expiration details of the inventory. This object will only appear if the details parameter in the request is set to `SHOW`."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    expiration: Annotated[
        Optional[datetime], Field(None, description="The expiration date of the SKU.")
    ]

    onhand_quantity: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices("onhandQuantity", "onhand_quantity"),
            serialization_alias="onhandQuantity",
            description="The quantity that is present in AWD.",
        ),
    ]


"""
GetInboundRequest

Request parameters for getInbound
"""


class GetInboundRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getInbound
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    order_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("orderId", "order_id"),
            serialization_alias="orderId",
            description="[PATH] The ID of the inbound order that you want to retrieve.",
        ),
    ]


# Enum definitions
class GetInboundShipmentLabelsRequestPageTypeEnum(str, Enum):
    """Enum for pageType"""

    THERMAL_NONPCP = "THERMAL_NONPCP"  # Use `THERMAL_NONPC` for a thermal printer. Supports non-Amazon-partnered shipments.
    PLAIN_PAPER = "PLAIN_PAPER"  # One label per sheet of US Letter paper. Only for non-Amazon-partnered shipments.
    LETTER_6 = "LETTER_6"  # Six labels per US Letter label sheet.


class GetInboundShipmentLabelsRequestFormatTypeEnum(str, Enum):
    """Enum for formatType"""

    PDF = "PDF"  # PDF format.


"""
GetInboundShipmentLabelsRequest

Request parameters for getInboundShipmentLabels
"""


class GetInboundShipmentLabelsRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getInboundShipmentLabels
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
            description="[PATH] ID for the shipment.",
        ),
    ]

    page_type: Annotated[
        Optional[GetInboundShipmentLabelsRequestPageTypeEnum],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("pageType", "page_type"),
            serialization_alias="pageType",
            description="[QUERY] Page type for the generated labels. The default is `PLAIN_PAPER`.",
        ),
    ]

    format_type: Annotated[
        Optional[GetInboundShipmentLabelsRequestFormatTypeEnum],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("formatType", "format_type"),
            serialization_alias="formatType",
            description="[QUERY] The format type of the output file that contains your labels. The default format type is `PDF`.",
        ),
    ]


# Enum definitions
class GetInboundShipmentRequestSkuQuantitiesEnum(str, Enum):
    """Enum for skuQuantities"""

    SHOW = "SHOW"  # Show the additional SKU quantity details.
    HIDE = "HIDE"  # Hide the additional SKU quantity details.


"""
GetInboundShipmentRequest

Request parameters for getInboundShipment
"""


class GetInboundShipmentRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getInboundShipment
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
            description="[PATH] ID for the shipment. A shipment contains the cases being inbounded.",
        ),
    ]

    sku_quantities: Annotated[
        Optional[GetInboundShipmentRequestSkuQuantitiesEnum],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("skuQuantities", "sku_quantities"),
            serialization_alias="skuQuantities",
            description="[QUERY] If equal to `SHOW`, the response includes the shipment SKU quantity details.  Defaults to `HIDE`, in which case the response does not contain SKU quantities",
        ),
    ]


InboundEligibilityStatus = str
"""Enum denoting the package inbound eligibility."""


"""
OrderIneligibilityReason

Represents one ineligibility reason for the order (there can be multiple reasons).
"""


class OrderIneligibilityReason(SpApiBaseModel):
    """Represents one ineligibility reason for the order (there can be multiple reasons)."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    code: Annotated[str, Field(..., description="Code for the order ineligibility.")]

    description: Annotated[
        str,
        Field(
            ...,
            description="Description detailing the ineligibility reason of the order.",
        ),
    ]


"""
SkuIneligibilityReason

Represents the ineligibility reason for one SKU.
"""


class SkuIneligibilityReason(SpApiBaseModel):
    """Represents the ineligibility reason for one SKU."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    code: Annotated[str, Field(..., description="Code for the SKU ineligibility.")]

    description: Annotated[
        str, Field(..., description="Detailed description of the SKU ineligibility.")
    ]


"""
SkuEligibility

Represents eligibility of one SKU.
"""


class SkuEligibility(SpApiBaseModel):
    """Represents eligibility of one SKU."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    ineligibility_reasons: Annotated[
        Optional[List["SkuIneligibilityReason"]],
        Field(
            None,
            validation_alias=AliasChoices(
                "ineligibilityReasons", "ineligibility_reasons"
            ),
            serialization_alias="ineligibilityReasons",
            description="If not eligible, these are list of error codes and descriptions.",
        ),
    ]

    package_quantity: Annotated[
        "DistributionPackageQuantity",
        Field(
            ...,
            validation_alias=AliasChoices("packageQuantity", "package_quantity"),
            serialization_alias="packageQuantity",
        ),
    ]

    status: Annotated[
        "InboundEligibilityStatus",
        Field(
            ...,
        ),
    ]


"""
InboundEligibility

Represents the eligibility status of the inbound packages.
"""


class InboundEligibility(SpApiBaseModel):
    """Represents the eligibility status of the inbound packages."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    ineligibility_reasons: Annotated[
        Optional[List["OrderIneligibilityReason"]],
        Field(
            None,
            validation_alias=AliasChoices(
                "ineligibilityReasons", "ineligibility_reasons"
            ),
            serialization_alias="ineligibilityReasons",
            description="If there are order level eligibility issues, then this list will contain those error codes and descriptions.",
        ),
    ]

    packages_to_inbound: Annotated[
        List["SkuEligibility"],
        Field(
            ...,
            validation_alias=AliasChoices("packagesToInbound", "packages_to_inbound"),
            serialization_alias="packagesToInbound",
            description="Details on SKU eligibility for each inbound package.",
        ),
    ]

    previewed_at: Annotated[
        datetime,
        Field(
            ...,
            validation_alias=AliasChoices("previewedAt", "previewed_at"),
            serialization_alias="previewedAt",
            description="Timestamp when the eligibility check is performed.",
        ),
    ]

    status: Annotated[
        "InboundEligibilityStatus",
        Field(
            ...,
        ),
    ]


InboundStatus = str
"""The supported statuses for an inbound order."""


"""
InboundOrder

Represents an AWD inbound order.
"""


class InboundOrder(SpApiBaseModel):
    """Represents an AWD inbound order."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    created_at: Annotated[
        datetime,
        Field(
            ...,
            validation_alias=AliasChoices("createdAt", "created_at"),
            serialization_alias="createdAt",
            description="Date when this order was created.",
        ),
    ]

    destination_details: Annotated[
        Optional["DestinationDetails"],
        Field(
            None,
            validation_alias=AliasChoices("destinationDetails", "destination_details"),
            serialization_alias="destinationDetails",
            description="Destination details of an inbound order based on the assigned region and DC for the order.",
        ),
    ]

    external_reference_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "externalReferenceId", "external_reference_id"
            ),
            serialization_alias="externalReferenceId",
            description="Reference ID that can be used to correlate the order with partner resources.",
        ),
    ]

    order_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("orderId", "order_id"),
            serialization_alias="orderId",
            description="Inbound order ID.",
        ),
    ]

    order_status: Annotated[
        "InboundStatus",
        Field(
            ...,
            validation_alias=AliasChoices("orderStatus", "order_status"),
            serialization_alias="orderStatus",
            description="Inbound order status.",
        ),
    ]

    origin_address: Annotated[
        "Address",
        Field(
            ...,
            validation_alias=AliasChoices("originAddress", "origin_address"),
            serialization_alias="originAddress",
            description="Origin address from where the inbound order will be shipped.",
        ),
    ]

    packages_to_inbound: Annotated[
        List["DistributionPackageQuantity"],
        Field(
            ...,
            validation_alias=AliasChoices("packagesToInbound", "packages_to_inbound"),
            serialization_alias="packagesToInbound",
            description="List of packages to be inbounded.",
        ),
    ]

    preferences: Annotated[
        Optional["InboundPreferences"],
        Field(
            None,
        ),
    ]

    updated_at: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices("updatedAt", "updated_at"),
            serialization_alias="updatedAt",
            description="Date when this order was last updated.",
        ),
    ]


"""
InboundOrderReference

A response that contains the reference identifiers for the newly created or updated inbound order. Consists of an order ID and version.
"""


class InboundOrderReference(SpApiBaseModel):
    """A response that contains the reference identifiers for the newly created or updated inbound order. Consists of an order ID and version."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    order_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("orderId", "order_id"),
            serialization_alias="orderId",
            description="Order ID of the inbound order.",
        ),
    ]


InboundShipmentStatus = str
"""Possible shipment statuses used by shipments."""


InventoryUnitOfMeasurement = str
"""Unit of measurement for the inventory."""


"""
InventoryQuantity

Quantity of inventory with an associated measurement unit context.
"""


class InventoryQuantity(SpApiBaseModel):
    """Quantity of inventory with an associated measurement unit context."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    quantity: Annotated[
        float, Field(..., description="Quantity of the respective inventory.")
    ]

    unit_of_measurement: Annotated[
        "InventoryUnitOfMeasurement",
        Field(
            ...,
            validation_alias=AliasChoices("unitOfMeasurement", "unit_of_measurement"),
            serialization_alias="unitOfMeasurement",
            description="Unit of measurement for the inventory.",
        ),
    ]


"""
SkuQuantity

Quantity details for a SKU as part of a shipment
"""


class SkuQuantity(SpApiBaseModel):
    """Quantity details for a SKU as part of a shipment"""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    expected_quantity: Annotated[
        "InventoryQuantity",
        Field(
            ...,
            validation_alias=AliasChoices("expectedQuantity", "expected_quantity"),
            serialization_alias="expectedQuantity",
        ),
    ]

    received_quantity: Annotated[
        Optional["InventoryQuantity"],
        Field(
            None,
            validation_alias=AliasChoices("receivedQuantity", "received_quantity"),
            serialization_alias="receivedQuantity",
        ),
    ]

    sku: Annotated[str, Field(..., description="The merchant stock keeping unit")]


"""
InboundShipment

Represents an AWD inbound shipment.
"""


class InboundShipment(SpApiBaseModel):
    """Represents an AWD inbound shipment."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    carrier_code: Annotated[
        Optional["CarrierCode"],
        Field(
            None,
            validation_alias=AliasChoices("carrierCode", "carrier_code"),
            serialization_alias="carrierCode",
            description="The shipment carrier code.",
        ),
    ]

    created_at: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices("createdAt", "created_at"),
            serialization_alias="createdAt",
            description="Timestamp when the shipment was created. The date is returned in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format.",
        ),
    ]

    destination_address: Annotated[
        "Address",
        Field(
            ...,
            validation_alias=AliasChoices("destinationAddress", "destination_address"),
            serialization_alias="destinationAddress",
            description="Destination address for this shipment.",
        ),
    ]

    external_reference_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "externalReferenceId", "external_reference_id"
            ),
            serialization_alias="externalReferenceId",
            description="Client-provided reference ID that can correlate this shipment to client resources. For example, to map this shipment to an internal bookkeeping order record.",
        ),
    ]

    order_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("orderId", "order_id"),
            serialization_alias="orderId",
            description="The AWD inbound order ID that this inbound shipment belongs to.",
        ),
    ]

    origin_address: Annotated[
        "Address",
        Field(
            ...,
            validation_alias=AliasChoices("originAddress", "origin_address"),
            serialization_alias="originAddress",
            description="Origin address for this shipment.",
        ),
    ]

    received_quantity: Annotated[
        Optional[List["InventoryQuantity"]],
        Field(
            None,
            validation_alias=AliasChoices("receivedQuantity", "received_quantity"),
            serialization_alias="receivedQuantity",
            description="Quantity received (at the receiving end) as part of this shipment.",
        ),
    ]

    ship_by: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices("shipBy", "ship_by"),
            serialization_alias="shipBy",
            description="Timestamp when the shipment will be shipped.",
        ),
    ]

    shipment_container_quantities: Annotated[
        List["DistributionPackageQuantity"],
        Field(
            ...,
            validation_alias=AliasChoices(
                "shipmentContainerQuantities", "shipment_container_quantities"
            ),
            serialization_alias="shipmentContainerQuantities",
            description="Packages that are part of this shipment.",
        ),
    ]

    shipment_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("shipmentId", "shipment_id"),
            serialization_alias="shipmentId",
            description="Unique shipment ID.",
        ),
    ]

    shipment_sku_quantities: Annotated[
        Optional[List["SkuQuantity"]],
        Field(
            None,
            validation_alias=AliasChoices(
                "shipmentSkuQuantities", "shipment_sku_quantities"
            ),
            serialization_alias="shipmentSkuQuantities",
            description="Quantity details at SKU level for the shipment. This attribute will only appear if the skuQuantities parameter in the request is set to SHOW.",
        ),
    ]

    destination_region: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("destinationRegion", "destination_region"),
            serialization_alias="destinationRegion",
            description="Assigned region where the order will be shipped. This can differ from what was passed as preference. AWD currently supports following region IDs: [us-west, us-east, us-southcentral, us-southeast]",
        ),
    ]

    shipment_status: Annotated[
        "InboundShipmentStatus",
        Field(
            ...,
            validation_alias=AliasChoices("shipmentStatus", "shipment_status"),
            serialization_alias="shipmentStatus",
            description="Current status of this shipment.",
        ),
    ]

    tracking_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("trackingId", "tracking_id"),
            serialization_alias="trackingId",
            description="Carrier-unique tracking ID for this shipment.",
        ),
    ]

    updated_at: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices("updatedAt", "updated_at"),
            serialization_alias="updatedAt",
            description="Timestamp when the shipment was updated. The date is returned in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format.",
        ),
    ]

    warehouse_reference_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "warehouseReferenceId", "warehouse_reference_id"
            ),
            serialization_alias="warehouseReferenceId",
            description="An AWD-provided reference ID that you can use to interact with the warehouse. For example, a carrier appointment booking.",
        ),
    ]


"""
InboundShipmentSummary

Summary for an AWD inbound shipment containing the shipment ID, which can be used to retrieve the actual shipment.
"""


class InboundShipmentSummary(SpApiBaseModel):
    """Summary for an AWD inbound shipment containing the shipment ID, which can be used to retrieve the actual shipment."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    created_at: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices("createdAt", "created_at"),
            serialization_alias="createdAt",
            description="Timestamp when the shipment was created.",
        ),
    ]

    external_reference_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "externalReferenceId", "external_reference_id"
            ),
            serialization_alias="externalReferenceId",
            description="Optional client-provided reference ID that can be used to correlate this shipment with client resources. For example, to map this shipment to an internal bookkeeping order record.",
        ),
    ]

    order_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("orderId", "order_id"),
            serialization_alias="orderId",
            description="The AWD inbound order ID that this inbound shipment belongs to.",
        ),
    ]

    shipment_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("shipmentId", "shipment_id"),
            serialization_alias="shipmentId",
            description="A unique shipment ID.",
        ),
    ]

    shipment_status: Annotated[
        "InboundShipmentStatus",
        Field(
            ...,
            validation_alias=AliasChoices("shipmentStatus", "shipment_status"),
            serialization_alias="shipmentStatus",
        ),
    ]

    updated_at: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices("updatedAt", "updated_at"),
            serialization_alias="updatedAt",
            description="Timestamp when the shipment was updated.",
        ),
    ]


"""
InventoryDetails

Additional inventory details. This object is only displayed if the details parameter in the request is set to `SHOW`.
"""


class InventoryDetails(SpApiBaseModel):
    """Additional inventory details. This object is only displayed if the details parameter in the request is set to `SHOW`."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    available_distributable_quantity: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices(
                "availableDistributableQuantity", "available_distributable_quantity"
            ),
            serialization_alias="availableDistributableQuantity",
            description="Quantity that is available for downstream channel replenishment.",
        ),
    ]

    replenishment_quantity: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices(
                "replenishmentQuantity", "replenishment_quantity"
            ),
            serialization_alias="replenishmentQuantity",
            description="Quantity that is in transit from AWD and has not yet been received at FBA.",
        ),
    ]

    reserved_distributable_quantity: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices(
                "reservedDistributableQuantity", "reserved_distributable_quantity"
            ),
            serialization_alias="reservedDistributableQuantity",
            description="Quantity that is reserved for a downstream channel replenishment order that is being prepared for shipment.",
        ),
    ]


"""
InventorySummary

Summary of inventory per SKU.
"""


class InventorySummary(SpApiBaseModel):
    """Summary of inventory per SKU."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    expiration_details: Annotated[
        Optional[List["ExpirationDetails"]],
        Field(
            None,
            validation_alias=AliasChoices("expirationDetails", "expiration_details"),
            serialization_alias="expirationDetails",
            description="The expiration details of the inventory. This object will only appear if the `details` parameter in the request is set to `SHOW`.",
        ),
    ]

    inventory_details: Annotated[
        Optional["InventoryDetails"],
        Field(
            None,
            validation_alias=AliasChoices("inventoryDetails", "inventory_details"),
            serialization_alias="inventoryDetails",
        ),
    ]

    sku: Annotated[str, Field(..., description="The seller or merchant SKU.")]

    total_inbound_quantity: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices(
                "totalInboundQuantity", "total_inbound_quantity"
            ),
            serialization_alias="totalInboundQuantity",
            description="Total quantity that is in-transit from the seller and has not yet been received at an AWD Distribution Center",
        ),
    ]

    total_onhand_quantity: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices(
                "totalOnhandQuantity", "total_onhand_quantity"
            ),
            serialization_alias="totalOnhandQuantity",
            description="Total quantity that is present in AWD distribution centers.",
        ),
    ]


"""
InventoryListing

AWD inventory payload.
"""


class InventoryListing(SpApiBaseModel):
    """AWD inventory payload."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    inventory: Annotated[
        List["InventorySummary"], Field(..., description="List of inventory summaries.")
    ]

    next_token: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("nextToken", "next_token"),
            serialization_alias="nextToken",
            description="A token that is used to retrieve the next page of results. The response includes `nextToken` when the number of results exceeds the specified `maxResults` value. To get the next page of results, call the operation with this token and include the same arguments as the call that produced the token. To get a complete list, call this operation until `nextToken` is null. Note that this operation can return empty pages.",
        ),
    ]


LabelStatus = str
"""The status of your label."""


# Enum definitions
class ListInboundShipmentsRequestSortByEnum(str, Enum):
    """Enum for sortBy"""

    UPDATED_AT = "UPDATED_AT"  # Sort by the time of update.
    CREATED_AT = "CREATED_AT"  # Sort by the time of creation.


class ListInboundShipmentsRequestSortOrderEnum(str, Enum):
    """Enum for sortOrder"""

    ASCENDING = "ASCENDING"  # Sorts the collection in ascending order.
    DESCENDING = "DESCENDING"  # Sorts the collection in descending order.


class ListInboundShipmentsRequestShipmentStatusEnum(str, Enum):
    """Enum for shipmentStatus"""

    CREATED = "CREATED"  # Shipment is created, but hasn't shipped.
    SHIPPED = "SHIPPED"  # Shipment was picked up by the carrier or was dropped off with the carrier.
    IN_TRANSIT = "IN_TRANSIT"  # The carrier has notified AWD that the shipment is in transit between the origin and destination nodes.
    RECEIVING = "RECEIVING"  # The shipment has been partially received.
    DELIVERED = "DELIVERED"  # The shipment has reached the destination node and has been delivered to the facility yard. The shipment `receive` process at the warehouse will start soon.
    CLOSED = "CLOSED"  # No more actions are required for the shipment. This is a final state.
    CANCELLED = "CANCELLED"  # The shipment is cancelled. This is a final state.


"""
ListInboundShipmentsRequest

Request parameters for listInboundShipments
"""


class ListInboundShipmentsRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for listInboundShipments
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    sort_by: Annotated[
        Optional[ListInboundShipmentsRequestSortByEnum],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("sortBy", "sort_by"),
            serialization_alias="sortBy",
            description="[QUERY] Field to sort results by. By default, the response will be sorted by UPDATED_AT.",
        ),
    ]

    sort_order: Annotated[
        Optional[ListInboundShipmentsRequestSortOrderEnum],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("sortOrder", "sort_order"),
            serialization_alias="sortOrder",
            description="[QUERY] Sort the response in ASCENDING or DESCENDING order. By default, the response will be sorted in DESCENDING order.",
        ),
    ]

    shipment_status: Annotated[
        Optional[ListInboundShipmentsRequestShipmentStatusEnum],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("shipmentStatus", "shipment_status"),
            serialization_alias="shipmentStatus",
            description="[QUERY] Filter by inbound shipment status.",
        ),
    ]

    updated_after: Annotated[
        Optional[datetime],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("updatedAfter", "updated_after"),
            serialization_alias="updatedAfter",
            description="[QUERY] List the inbound shipments that were updated after a certain time (inclusive). The date must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format.",
        ),
    ]

    updated_before: Annotated[
        Optional[datetime],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("updatedBefore", "updated_before"),
            serialization_alias="updatedBefore",
            description="[QUERY] List the inbound shipments that were updated before a certain time (inclusive). The date must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format.",
        ),
    ]

    max_results: Annotated[
        Optional[int],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("maxResults", "max_results"),
            serialization_alias="maxResults",
            description="[QUERY] Maximum number of results to return.",
        ),
    ]

    next_token: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("nextToken", "next_token"),
            serialization_alias="nextToken",
            description="[QUERY] A token that is used to retrieve the next page of results. The response includes `nextToken` when the number of results exceeds the specified `maxResults` value. To get the next page of results, call the operation with this token and include the same arguments as the call that produced the token. To get a complete list, call this operation until `nextToken` is null. Note that this operation can return empty pages.",
        ),
    ]


# Enum definitions
class ListInventoryRequestSortOrderEnum(str, Enum):
    """Enum for sortOrder"""

    ASCENDING = "ASCENDING"  # Sorts the collection in ascending order.
    DESCENDING = "DESCENDING"  # Sorts the collection in descending order.


class ListInventoryRequestDetailsEnum(str, Enum):
    """Enum for details"""

    SHOW = "SHOW"  # Show the additional summarized inventory details.
    HIDE = "HIDE"  # Hide the additional summarized inventory details.


"""
ListInventoryRequest

Request parameters for listInventory
"""


class ListInventoryRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for listInventory
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    sku: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None, description="[QUERY] Filter by seller or merchant SKU for the item."
        ),
    ]

    sort_order: Annotated[
        Optional[ListInventoryRequestSortOrderEnum],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("sortOrder", "sort_order"),
            serialization_alias="sortOrder",
            description="[QUERY] Sort the response in `ASCENDING` or `DESCENDING` order.",
        ),
    ]

    details: Annotated[
        Optional[ListInventoryRequestDetailsEnum],
        QueryParam(),
        Field(
            None,
            description="[QUERY] Set to `SHOW` to return summaries with additional inventory details. Defaults to `HIDE,` which returns only inventory summary totals.",
        ),
    ]

    next_token: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("nextToken", "next_token"),
            serialization_alias="nextToken",
            description="[QUERY] A token that is used to retrieve the next page of results. The response includes `nextToken` when the number of results exceeds the specified `maxResults` value. To get the next page of results, call the operation with this token and include the same arguments as the call that produced the token. To get a complete list, call this operation until `nextToken` is null. Note that this operation can return empty pages.",
        ),
    ]

    max_results: Annotated[
        Optional[int],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("maxResults", "max_results"),
            serialization_alias="maxResults",
            description="[QUERY] Maximum number of results to return.",
        ),
    ]


"""
ShipmentLabels

Shipment labels.
"""


class ShipmentLabels(SpApiBaseModel):
    """Shipment labels."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    label_download_u_r_l: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("labelDownloadURL", "label_download_u_r_l"),
            serialization_alias="labelDownloadURL",
            description="The URL to download shipment labels. The URL is active for 600 seconds from generation.",
        ),
    ]

    label_status: Annotated[
        "LabelStatus",
        Field(
            ...,
            validation_alias=AliasChoices("labelStatus", "label_status"),
            serialization_alias="labelStatus",
            description="Status of label generation.",
        ),
    ]


"""
ShipmentListing

A list of inbound shipment summaries filtered by the attributes specified in the request.
"""


class ShipmentListing(SpApiBaseModel):
    """A list of inbound shipment summaries filtered by the attributes specified in the request."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    next_token: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("nextToken", "next_token"),
            serialization_alias="nextToken",
            description="A token that is used to retrieve the next page of results. The response includes `nextToken` when the number of results exceeds the specified `maxResults` value. To get the next page of results, call the operation with this token and include the same arguments as the call that produced the token. To get a complete list, call this operation until `nextToken` is null. Note that this operation can return empty pages.",
        ),
    ]

    shipments: Annotated[
        Optional[List["InboundShipmentSummary"]],
        Field(None, description="List of inbound shipment summaries."),
    ]


"""
TrackingDetails

Tracking details for the shipment. If using SPD transportation, this can be for each case. If not using SPD transportation, this is a single tracking entry for the entire shipment.
"""


class TrackingDetails(SpApiBaseModel):
    """Tracking details for the shipment. If using SPD transportation, this can be for each case. If not using SPD transportation, this is a single tracking entry for the entire shipment."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    carrier_code: Annotated[
        Optional["CarrierCode"],
        Field(
            None,
            validation_alias=AliasChoices("carrierCode", "carrier_code"),
            serialization_alias="carrierCode",
            description="Unique or identifying code for the carrier.",
        ),
    ]

    booking_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("bookingId", "booking_id"),
            serialization_alias="bookingId",
            description="The identifier that is received from transportation to uniquely identify a booking.",
        ),
    ]


"""
TransportationDetails

Transportation details for the shipment.
"""


class TransportationDetails(SpApiBaseModel):
    """Transportation details for the shipment."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    tracking_details: Annotated[
        List["TrackingDetails"],
        Field(
            ...,
            validation_alias=AliasChoices("trackingDetails", "tracking_details"),
            serialization_alias="trackingDetails",
            description="Tracking details for the shipment. If using SPD transportation, this can be for each case. If not using SPD transportation, this is a single tracking entry for the entire shipment.",
        ),
    ]


"""
UpdateInboundRequest

Request parameters for updateInbound
"""


class UpdateInboundRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for updateInbound
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    order_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("orderId", "order_id"),
            serialization_alias="orderId",
            description="[PATH] The ID of the inbound order that you want to update.",
        ),
    ]

    body: Annotated[
        "InboundOrder",
        BodyParam(),
        Field(..., description="[BODY] Represents an AWD inbound order."),
    ]


"""
UpdateInboundShipmentTransportDetailsRequest

Request parameters for updateInboundShipmentTransportDetails
"""


class UpdateInboundShipmentTransportDetailsRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for updateInboundShipmentTransportDetails
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
            description="[PATH] The shipment ID.",
        ),
    ]

    body: Annotated[
        "TransportationDetails",
        BodyParam(),
        Field(..., description="[BODY] Transportation details for the shipment."),
    ]


# Rebuild models to resolve forward references
Address.model_rebuild()
CarrierCode.model_rebuild()
DestinationDetails.model_rebuild()
DistributionPackage.model_rebuild()
DistributionPackageContents.model_rebuild()
DistributionPackageQuantity.model_rebuild()
Error.model_rebuild()
ErrorList.model_rebuild()
InboundEligibility.model_rebuild()
InboundOrder.model_rebuild()
InboundOrderCreationData.model_rebuild()
InboundOrderReference.model_rebuild()
InboundPackages.model_rebuild()
InboundPreferences.model_rebuild()
InboundShipment.model_rebuild()
InboundShipmentSummary.model_rebuild()
ExpirationDetails.model_rebuild()
InventoryDetails.model_rebuild()
InventoryListing.model_rebuild()
InventoryQuantity.model_rebuild()
InventorySummary.model_rebuild()
MeasurementData.model_rebuild()
OrderIneligibilityReason.model_rebuild()
PackageDimensions.model_rebuild()
PackageVolume.model_rebuild()
PackageWeight.model_rebuild()
PrepDetails.model_rebuild()
PrepInstruction.model_rebuild()
ProductAttribute.model_rebuild()
ProductQuantity.model_rebuild()
ShipmentLabels.model_rebuild()
ShipmentListing.model_rebuild()
SkuEligibility.model_rebuild()
SkuIneligibilityReason.model_rebuild()
SkuQuantity.model_rebuild()
TrackingDetails.model_rebuild()
TransportationDetails.model_rebuild()
CreateInboundRequest.model_rebuild()
GetInboundRequest.model_rebuild()
UpdateInboundRequest.model_rebuild()
CancelInboundRequest.model_rebuild()
ConfirmInboundRequest.model_rebuild()
GetInboundShipmentRequest.model_rebuild()
GetInboundShipmentLabelsRequest.model_rebuild()
UpdateInboundShipmentTransportDetailsRequest.model_rebuild()
CheckInboundEligibilityRequest.model_rebuild()
ListInboundShipmentsRequest.model_rebuild()
ListInventoryRequest.model_rebuild()
