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
AddressExtendedFields

The container for address extended fields (such as `street name` and `street number`). Currently only available with Brazil shipping addresses.
"""


class AddressExtendedFields(SpApiBaseModel):
    """The container for address extended fields (such as `street name` and `street number`). Currently only available with Brazil shipping addresses."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    street_name: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("StreetName", "street_name"),
            serialization_alias="StreetName",
            description="The street name.",
        ),
    ]

    street_number: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("StreetNumber", "street_number"),
            serialization_alias="StreetNumber",
            description="The house, building, or property number associated with the location's street address.",
        ),
    ]

    complement: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("Complement", "complement"),
            serialization_alias="Complement",
            description="The floor number/unit number in the building/private house number.",
        ),
    ]

    neighborhood: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("Neighborhood", "neighborhood"),
            serialization_alias="Neighborhood",
            description="The neighborhood. This value is only used in some countries (such as Brazil).",
        ),
    ]


# Enum definitions
class AddressTypeEnum(str, Enum):
    """Enum for AddressType"""

    RESIDENTIAL = "Residential"  # The shipping address is a residential address.
    COMMERCIAL = "Commercial"  # The shipping address is a commercial address.


"""
Address

The shipping address for the order.
"""


class Address(SpApiBaseModel):
    """The shipping address for the order."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    name: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("Name", "name"),
            serialization_alias="Name",
            description="The name.",
        ),
    ]

    company_name: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("CompanyName", "company_name"),
            serialization_alias="CompanyName",
            description="The company name of the recipient. **Note**: This attribute is only available for shipping address.",
        ),
    ]

    address_line1: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("AddressLine1", "address_line1"),
            serialization_alias="AddressLine1",
            description="The street address.",
        ),
    ]

    address_line2: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("AddressLine2", "address_line2"),
            serialization_alias="AddressLine2",
            description="Additional street address information, if required.",
        ),
    ]

    address_line3: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("AddressLine3", "address_line3"),
            serialization_alias="AddressLine3",
            description="Additional street address information, if required.",
        ),
    ]

    city: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("City", "city"),
            serialization_alias="City",
            description="The city.",
        ),
    ]

    county: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("County", "county"),
            serialization_alias="County",
            description="The county.",
        ),
    ]

    district: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("District", "district"),
            serialization_alias="District",
            description="The district.",
        ),
    ]

    state_or_region: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("StateOrRegion", "state_or_region"),
            serialization_alias="StateOrRegion",
            description="The state or region.",
        ),
    ]

    municipality: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("Municipality", "municipality"),
            serialization_alias="Municipality",
            description="The municipality.",
        ),
    ]

    postal_code: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("PostalCode", "postal_code"),
            serialization_alias="PostalCode",
            description="The postal code.",
        ),
    ]

    country_code: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("CountryCode", "country_code"),
            serialization_alias="CountryCode",
            description="The country code. A two-character country code, in ISO 3166-1 alpha-2 format.",
        ),
    ]

    phone: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("Phone", "phone"),
            serialization_alias="Phone",
            description="The phone number of the buyer. **Note**: 1. This attribute is only available for shipping address. 2. In some cases, the buyer phone number is suppressed: a. Phone is suppressed for all `AFN` (fulfilled by Amazon) orders. b. Phone is suppressed for the shipped `MFN` (fulfilled by seller) order when the current date is past the Latest Delivery Date.",
        ),
    ]

    extended_fields: Annotated[
        Optional["AddressExtendedFields"],
        Field(
            None,
            validation_alias=AliasChoices("ExtendedFields", "extended_fields"),
            serialization_alias="ExtendedFields",
            description="The container for address extended fields. For example, street name or street number. **Note**: This attribute is currently only available with Brazil shipping addresses.",
        ),
    ]

    address_type: Annotated[
        Optional[AddressTypeEnum],
        Field(
            None,
            validation_alias=AliasChoices("AddressType", "address_type"),
            serialization_alias="AddressType",
            description="The address type of the shipping address.",
        ),
    ]


"""
AmazonPrograms

Contains the list of programs that are associated with an item. Possible programs are: - **Subscribe and Save**: Offers recurring, scheduled deliveries to Amazon customers and Amazon Business customers for their frequently ordered products.
"""


class AmazonPrograms(SpApiBaseModel):
    """Contains the list of programs that are associated with an item. Possible programs are: - **Subscribe and Save**: Offers recurring, scheduled deliveries to Amazon customers and Amazon Business customers for their frequently ordered products."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    programs: Annotated[
        List["str"],
        Field(
            ...,
            validation_alias=AliasChoices("Programs", "programs"),
            serialization_alias="Programs",
            description="A list of the programs that are associated with the specified order item. **Possible values**: `SUBSCRIBE_AND_SAVE`",
        ),
    ]


AssociationType = str
"""The type of association an item has with an order item."""


"""
AssociatedItem

An item that is associated with an order item. For example, a tire installation service that is purchased with tires.
"""


class AssociatedItem(SpApiBaseModel):
    """An item that is associated with an order item. For example, a tire installation service that is purchased with tires."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    order_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("OrderId", "order_id"),
            serialization_alias="OrderId",
            description="The order item's order identifier, in 3-7-7 format.",
        ),
    ]

    order_item_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("OrderItemId", "order_item_id"),
            serialization_alias="OrderItemId",
            description="An Amazon-defined item identifier for the associated item.",
        ),
    ]

    association_type: Annotated[
        Optional["AssociationType"],
        Field(
            None,
            validation_alias=AliasChoices("AssociationType", "association_type"),
            serialization_alias="AssociationType",
        ),
    ]


"""
AutomatedShippingSettings

Contains information regarding the Shipping Settings Automation program, such as whether the order's shipping settings were generated automatically, and what those settings are.
"""


class AutomatedShippingSettings(SpApiBaseModel):
    """Contains information regarding the Shipping Settings Automation program, such as whether the order's shipping settings were generated automatically, and what those settings are."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    has_automated_shipping_settings: Annotated[
        Optional[bool],
        Field(
            None,
            validation_alias=AliasChoices(
                "HasAutomatedShippingSettings", "has_automated_shipping_settings"
            ),
            serialization_alias="HasAutomatedShippingSettings",
            description="When true, this order has automated shipping settings generated by Amazon. This order could be identified as an SSA order.",
        ),
    ]

    automated_carrier: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("AutomatedCarrier", "automated_carrier"),
            serialization_alias="AutomatedCarrier",
            description="Auto-generated carrier for SSA orders.",
        ),
    ]

    automated_ship_method: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "AutomatedShipMethod", "automated_ship_method"
            ),
            serialization_alias="AutomatedShipMethod",
            description="Auto-generated ship method for SSA orders.",
        ),
    ]


"""
OpenTimeInterval

The time when the business opens or closes.
"""


class OpenTimeInterval(SpApiBaseModel):
    """The time when the business opens or closes."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    hour: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices("Hour", "hour"),
            serialization_alias="Hour",
            description="The hour when the business opens or closes.",
        ),
    ]

    minute: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices("Minute", "minute"),
            serialization_alias="Minute",
            description="The minute when the business opens or closes.",
        ),
    ]


"""
OpenInterval

The time interval for which the business is open.
"""


class OpenInterval(SpApiBaseModel):
    """The time interval for which the business is open."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    start_time: Annotated[
        Optional["OpenTimeInterval"],
        Field(
            None,
            validation_alias=AliasChoices("StartTime", "start_time"),
            serialization_alias="StartTime",
            description="The time when the business opens.",
        ),
    ]

    end_time: Annotated[
        Optional["OpenTimeInterval"],
        Field(
            None,
            validation_alias=AliasChoices("EndTime", "end_time"),
            serialization_alias="EndTime",
            description="The time when the business closes.",
        ),
    ]


# Enum definitions
class DayOfWeekEnum(str, Enum):
    """Enum for DayOfWeek"""

    SUN = "SUN"  # Sunday - Day of the week.
    MON = "MON"  # Monday - Day of the week.
    TUE = "TUE"  # Tuesday - Day of the week.
    WED = "WED"  # Wednesday - Day of the week.
    THU = "THU"  # Thursday - Day of the week.
    FRI = "FRI"  # Friday - Day of the week.
    SAT = "SAT"  # Saturday - Day of the week.


"""
BusinessHours

Business days and hours when the destination is open for deliveries.
"""


class BusinessHours(SpApiBaseModel):
    """Business days and hours when the destination is open for deliveries."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    day_of_week: Annotated[
        Optional[DayOfWeekEnum],
        Field(
            None,
            validation_alias=AliasChoices("DayOfWeek", "day_of_week"),
            serialization_alias="DayOfWeek",
            description="Day of the week.",
        ),
    ]

    open_intervals: Annotated[
        Optional[List["OpenInterval"]],
        Field(
            None,
            validation_alias=AliasChoices("OpenIntervals", "open_intervals"),
            serialization_alias="OpenIntervals",
            description="Time window during the day when the business is open.",
        ),
    ]


"""
BuyerCustomizedInfoDetail

Buyer information for custom orders from the Amazon Custom program.
"""


class BuyerCustomizedInfoDetail(SpApiBaseModel):
    """Buyer information for custom orders from the Amazon Custom program."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    customized_u_r_l: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("CustomizedURL", "customized_u_r_l"),
            serialization_alias="CustomizedURL",
            description="The location of a ZIP file containing Amazon Custom data.",
        ),
    ]


"""
TaxClassification

The tax classification of the order.
"""


class TaxClassification(SpApiBaseModel):
    """The tax classification of the order."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    name: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("Name", "name"),
            serialization_alias="Name",
            description="The type of tax.",
        ),
    ]

    value: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("Value", "value"),
            serialization_alias="Value",
            description="The buyer's tax identifier.",
        ),
    ]


"""
BuyerTaxInfo

Tax information about the buyer.
"""


class BuyerTaxInfo(SpApiBaseModel):
    """Tax information about the buyer."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    company_legal_name: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("CompanyLegalName", "company_legal_name"),
            serialization_alias="CompanyLegalName",
            description="The legal name of the company.",
        ),
    ]

    taxing_region: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("TaxingRegion", "taxing_region"),
            serialization_alias="TaxingRegion",
            description="The country or region imposing the tax.",
        ),
    ]

    tax_classifications: Annotated[
        Optional[List["TaxClassification"]],
        Field(
            None,
            validation_alias=AliasChoices("TaxClassifications", "tax_classifications"),
            serialization_alias="TaxClassifications",
            description="A list of tax classifications that apply to the order.",
        ),
    ]


"""
BuyerInfo

Buyer information.
"""


class BuyerInfo(SpApiBaseModel):
    """Buyer information."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    buyer_email: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("BuyerEmail", "buyer_email"),
            serialization_alias="BuyerEmail",
            description="The anonymized email address of the buyer.",
        ),
    ]

    buyer_name: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("BuyerName", "buyer_name"),
            serialization_alias="BuyerName",
            description="The buyer name or the recipient name.",
        ),
    ]

    buyer_county: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("BuyerCounty", "buyer_county"),
            serialization_alias="BuyerCounty",
            description="The county of the buyer. **Note**: This attribute is only available in the Brazil marketplace.",
        ),
    ]

    buyer_tax_info: Annotated[
        Optional["BuyerTaxInfo"],
        Field(
            None,
            validation_alias=AliasChoices("BuyerTaxInfo", "buyer_tax_info"),
            serialization_alias="BuyerTaxInfo",
            description="Tax information about the buyer. Sellers can use this data to issue electronic invoices for business orders. **Note**: This attribute is only available for business orders in the Brazil, Mexico and India marketplaces.",
        ),
    ]

    purchase_order_number: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "PurchaseOrderNumber", "purchase_order_number"
            ),
            serialization_alias="PurchaseOrderNumber",
            description="The purchase order (PO) number entered by the buyer at checkout. Only returned for orders where the buyer entered a PO number at checkout.",
        ),
    ]


"""
BuyerRequestedCancel

Information about whether or not a buyer requested cancellation.
"""


class BuyerRequestedCancel(SpApiBaseModel):
    """Information about whether or not a buyer requested cancellation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    is_buyer_requested_cancel: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "IsBuyerRequestedCancel", "is_buyer_requested_cancel"
            ),
            serialization_alias="IsBuyerRequestedCancel",
            description="Indicate whether the buyer has requested cancellation. **Possible Values**: `true`, `false`.",
        ),
    ]

    buyer_cancel_reason: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("BuyerCancelReason", "buyer_cancel_reason"),
            serialization_alias="BuyerCancelReason",
            description="The reason that the buyer requested cancellation.",
        ),
    ]


"""
BuyerTaxInformation

Contains the business invoice tax information. Available only in the TR marketplace.
"""


class BuyerTaxInformation(SpApiBaseModel):
    """Contains the business invoice tax information. Available only in the TR marketplace."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    buyer_legal_company_name: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "BuyerLegalCompanyName", "buyer_legal_company_name"
            ),
            serialization_alias="BuyerLegalCompanyName",
            description="Business buyer's company legal name.",
        ),
    ]

    buyer_business_address: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "BuyerBusinessAddress", "buyer_business_address"
            ),
            serialization_alias="BuyerBusinessAddress",
            description="Business buyer's address.",
        ),
    ]

    buyer_tax_registration_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "BuyerTaxRegistrationId", "buyer_tax_registration_id"
            ),
            serialization_alias="BuyerTaxRegistrationId",
            description="Business buyer's tax registration ID.",
        ),
    ]

    buyer_tax_office: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("BuyerTaxOffice", "buyer_tax_office"),
            serialization_alias="BuyerTaxOffice",
            description="Business buyer's tax office.",
        ),
    ]


ErrorList = List["Error"]
"""A list of error responses returned when a request is unsuccessful."""


"""
ConfirmShipmentErrorResponse

The error response schema for the `confirmShipment` operation.
"""


class ConfirmShipmentErrorResponse(SpApiBaseModel):
    """The error response schema for the `confirmShipment` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
            description="One or more unexpected errors occurred during the `confirmShipment` operation.",
        ),
    ]


TransparencyCodeList = List["TransparencyCode"]
"""A list of order items."""


"""
ConfirmShipmentOrderItem

A single order item.
"""


class ConfirmShipmentOrderItem(SpApiBaseModel):
    """A single order item."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    order_item_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("orderItemId", "order_item_id"),
            serialization_alias="orderItemId",
            description="The order item's unique identifier.",
        ),
    ]

    quantity: Annotated[int, Field(..., description="The item's quantity.")]

    transparency_codes: Annotated[
        Optional["TransparencyCodeList"],
        Field(
            None,
            validation_alias=AliasChoices("transparencyCodes", "transparency_codes"),
            serialization_alias="transparencyCodes",
            description="The list of transparency codes.",
        ),
    ]


ConfirmShipmentOrderItemsList = List["ConfirmShipmentOrderItem"]
"""A list of order items."""


MarketplaceId = str
"""The unobfuscated marketplace identifier."""


PackageReferenceId = str
"""A seller-supplied identifier that uniquely identifies a package within the scope of an order. Only positive numeric values are supported."""


"""
PackageDetail

Properties of packages
"""


class PackageDetail(SpApiBaseModel):
    """Properties of packages"""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    package_reference_id: Annotated[
        "PackageReferenceId",
        Field(
            ...,
            validation_alias=AliasChoices("packageReferenceId", "package_reference_id"),
            serialization_alias="packageReferenceId",
        ),
    ]

    carrier_code: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("carrierCode", "carrier_code"),
            serialization_alias="carrierCode",
            description="Identifies the carrier that will deliver the package. This field is required for all marketplaces. For more information, refer to the [`CarrierCode` announcement](https://developer-docs.amazon.com/sp-api/changelog/carriercode-value-required-in-shipment-confirmations-for-br-mx-ca-sg-au-in-jp-marketplaces).",
        ),
    ]

    carrier_name: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("carrierName", "carrier_name"),
            serialization_alias="carrierName",
            description="Carrier Name that will deliver the package. Required when `carrierCode` is 'Others' ",
        ),
    ]

    shipping_method: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("shippingMethod", "shipping_method"),
            serialization_alias="shippingMethod",
            description="Ship method to be used for shipping the order.",
        ),
    ]

    tracking_number: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("trackingNumber", "tracking_number"),
            serialization_alias="trackingNumber",
            description="The tracking number used to obtain tracking and delivery information.",
        ),
    ]

    ship_date: Annotated[
        datetime,
        Field(
            ...,
            validation_alias=AliasChoices("shipDate", "ship_date"),
            serialization_alias="shipDate",
            description="The shipping date for the package. Must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> date/time format.",
        ),
    ]

    ship_from_supply_source_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "shipFromSupplySourceId", "ship_from_supply_source_id"
            ),
            serialization_alias="shipFromSupplySourceId",
            description="The unique identifier for the supply source.",
        ),
    ]

    order_items: Annotated[
        "ConfirmShipmentOrderItemsList",
        Field(
            ...,
            validation_alias=AliasChoices("orderItems", "order_items"),
            serialization_alias="orderItems",
            description="The list of order items and quantities to be updated.",
        ),
    ]


# Enum definitions
class CodCollectionMethodEnum(str, Enum):
    """Enum for codCollectionMethod"""

    DIRECT_PAYMENT = "DirectPayment"


"""
ConfirmShipmentRequestBody

The request schema for an shipment confirmation.
"""


class ConfirmShipmentRequestBody(SpApiBaseModel):
    """The request schema for an shipment confirmation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    package_detail: Annotated[
        "PackageDetail",
        Field(
            ...,
            validation_alias=AliasChoices("packageDetail", "package_detail"),
            serialization_alias="packageDetail",
        ),
    ]

    cod_collection_method: Annotated[
        Optional[CodCollectionMethodEnum],
        Field(
            None,
            validation_alias=AliasChoices(
                "codCollectionMethod", "cod_collection_method"
            ),
            serialization_alias="codCollectionMethod",
            description="The COD collection method (only supported in the JP marketplace).",
        ),
    ]

    marketplace_id: Annotated[
        Optional["MarketplaceId"],
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
        ),
    ]


"""
ConfirmShipmentRequest

Request parameters for confirmShipment
"""


class ConfirmShipmentRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for confirmShipment
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
            description="[PATH] An Amazon-defined order identifier, in 3-7-7 format.",
        ),
    ]

    payload: Annotated[
        "ConfirmShipmentRequestBody",
        BodyParam(),
        Field(..., description="[BODY] RequestBody body of `confirmShipment`."),
    ]


ConstraintType = str
"""Details the importance of the constraint present on the item"""


OtherDeliveryAttributes = str
"""Miscellaneous delivery attributes associated with the shipping address."""


"""
ExceptionDates

Dates when the business is closed or open with a different time window.
"""


class ExceptionDates(SpApiBaseModel):
    """Dates when the business is closed or open with a different time window."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    exception_date: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("ExceptionDate", "exception_date"),
            serialization_alias="ExceptionDate",
            description="Date when the business is closed, in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> date format.",
        ),
    ]

    is_open: Annotated[
        Optional[bool],
        Field(
            None,
            validation_alias=AliasChoices("IsOpen", "is_open"),
            serialization_alias="IsOpen",
            description="Boolean indicating if the business is closed or open on that date.",
        ),
    ]

    open_intervals: Annotated[
        Optional[List["OpenInterval"]],
        Field(
            None,
            validation_alias=AliasChoices("OpenIntervals", "open_intervals"),
            serialization_alias="OpenIntervals",
            description="Time window during the day when the business is open.",
        ),
    ]


"""
PreferredDeliveryTime

The time window when the delivery is preferred.
"""


class PreferredDeliveryTime(SpApiBaseModel):
    """The time window when the delivery is preferred."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    business_hours: Annotated[
        Optional[List["BusinessHours"]],
        Field(
            None,
            validation_alias=AliasChoices("BusinessHours", "business_hours"),
            serialization_alias="BusinessHours",
            description="Business hours when the business is open for deliveries.",
        ),
    ]

    exception_dates: Annotated[
        Optional[List["ExceptionDates"]],
        Field(
            None,
            validation_alias=AliasChoices("ExceptionDates", "exception_dates"),
            serialization_alias="ExceptionDates",
            description="Dates when the business is closed during the next 30 days.",
        ),
    ]


"""
DeliveryPreferences

Contains all of the delivery instructions provided by the customer for the shipping address.
"""


class DeliveryPreferences(SpApiBaseModel):
    """Contains all of the delivery instructions provided by the customer for the shipping address."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    drop_off_location: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("DropOffLocation", "drop_off_location"),
            serialization_alias="DropOffLocation",
            description="Drop-off location selected by the customer.",
        ),
    ]

    preferred_delivery_time: Annotated[
        Optional["PreferredDeliveryTime"],
        Field(
            None,
            validation_alias=AliasChoices(
                "PreferredDeliveryTime", "preferred_delivery_time"
            ),
            serialization_alias="PreferredDeliveryTime",
            description="Business hours and days when the delivery is preferred.",
        ),
    ]

    other_attributes: Annotated[
        Optional[List["OtherDeliveryAttributes"]],
        Field(
            None,
            validation_alias=AliasChoices("OtherAttributes", "other_attributes"),
            serialization_alias="OtherAttributes",
            description="Enumerated list of miscellaneous delivery attributes associated with the shipping address.",
        ),
    ]

    address_instructions: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "AddressInstructions", "address_instructions"
            ),
            serialization_alias="AddressInstructions",
            description="Building instructions, nearby landmark or navigation instructions.",
        ),
    ]


EasyShipShipmentStatus = str
"""The status of the Amazon Easy Ship order. This property is only included for Amazon Easy Ship orders."""


ElectronicInvoiceStatus = str
"""The status of the electronic invoice. Only available for Easy Ship orders and orders in the BR marketplace."""


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
Money

The monetary value of the order.
"""


class Money(SpApiBaseModel):
    """The monetary value of the order."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    currency_code: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("CurrencyCode", "currency_code"),
            serialization_alias="CurrencyCode",
            description="The three-digit currency code. In ISO 4217 format.",
        ),
    ]

    amount: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("Amount", "amount"),
            serialization_alias="Amount",
            description="The currency amount.",
        ),
    ]


"""
ExportInfo

Contains information that is related to the export of an order item.
"""


class ExportInfo(SpApiBaseModel):
    """Contains information that is related to the export of an order item."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    export_charge: Annotated[
        Optional["Money"],
        Field(
            None,
            validation_alias=AliasChoices("ExportCharge", "export_charge"),
            serialization_alias="ExportCharge",
            description="Holds the export/import charge for an order item.",
        ),
    ]

    export_charge_model: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("ExportChargeModel", "export_charge_model"),
            serialization_alias="ExportChargeModel",
            description="Holds the `ExportCharge` collection model that is associated with the specified order item.\n\n**Possible values**: `AMAZON_FACILITATED`: Import/export charge is withheld by Amazon and remitted to the customs authority by the carrier on behalf of the buyer/seller.",
        ),
    ]


"""
FulfillmentInstruction

Contains the instructions about the fulfillment, such as the location from where you want the order filled.
"""


class FulfillmentInstruction(SpApiBaseModel):
    """Contains the instructions about the fulfillment, such as the location from where you want the order filled."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    fulfillment_supply_source_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "FulfillmentSupplySourceId", "fulfillment_supply_source_id"
            ),
            serialization_alias="FulfillmentSupplySourceId",
            description="The `sourceId` of the location from where you want the order fulfilled.",
        ),
    ]


"""
GetOrderAddressRequest

Request parameters for getOrderAddress
"""


class GetOrderAddressRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getOrderAddress
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
            description="[PATH] An `orderId` is an Amazon-defined order identifier, in 3-7-7 format.",
        ),
    ]


"""
OrderAddress

The shipping address for the order.
"""


class OrderAddress(SpApiBaseModel):
    """The shipping address for the order."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    amazon_order_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("AmazonOrderId", "amazon_order_id"),
            serialization_alias="AmazonOrderId",
            description="An Amazon-defined order identifier, in 3-7-7 format.",
        ),
    ]

    buyer_company_name: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("BuyerCompanyName", "buyer_company_name"),
            serialization_alias="BuyerCompanyName",
            description="The company name of the contact buyer. For IBA orders, the buyer company must be Amazon entities.",
        ),
    ]

    shipping_address: Annotated[
        Optional["Address"],
        Field(
            None,
            validation_alias=AliasChoices("ShippingAddress", "shipping_address"),
            serialization_alias="ShippingAddress",
            description="The shipping address for the order. **Note**: `ShippingAddress` is only available for orders with the following status values: `Unshipped`, `PartiallyShipped`, `Shipped`, and `InvoiceUnconfirmed`.",
        ),
    ]

    delivery_preferences: Annotated[
        Optional["DeliveryPreferences"],
        Field(
            None,
            validation_alias=AliasChoices(
                "DeliveryPreferences", "delivery_preferences"
            ),
            serialization_alias="DeliveryPreferences",
        ),
    ]


"""
GetOrderAddressResponse

The response schema for the `getOrderAddress` operation.
"""


class GetOrderAddressResponse(SpApiBaseModel):
    """The response schema for the `getOrderAddress` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["OrderAddress"],
        Field(None, description="The payload for the `getOrderAddress` operations."),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
            description="One or more unexpected errors occurred during the `getOrderAddress` operation.",
        ),
    ]


"""
GetOrderBuyerInfoRequest

Request parameters for getOrderBuyerInfo
"""


class GetOrderBuyerInfoRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getOrderBuyerInfo
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
            description="[PATH] An `orderId` is an Amazon-defined order identifier, in 3-7-7 format.",
        ),
    ]


"""
OrderBuyerInfo

Buyer information for an order.
"""


class OrderBuyerInfo(SpApiBaseModel):
    """Buyer information for an order."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    amazon_order_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("AmazonOrderId", "amazon_order_id"),
            serialization_alias="AmazonOrderId",
            description="An Amazon-defined order identifier, in 3-7-7 format.",
        ),
    ]

    buyer_email: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("BuyerEmail", "buyer_email"),
            serialization_alias="BuyerEmail",
            description="The anonymized email address of the buyer.",
        ),
    ]

    buyer_name: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("BuyerName", "buyer_name"),
            serialization_alias="BuyerName",
            description="The buyer name or the recipient name.",
        ),
    ]

    buyer_county: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("BuyerCounty", "buyer_county"),
            serialization_alias="BuyerCounty",
            description="The county of the buyer. **Note**: This attribute is only available in the Brazil marketplace.",
        ),
    ]

    buyer_tax_info: Annotated[
        Optional["BuyerTaxInfo"],
        Field(
            None,
            validation_alias=AliasChoices("BuyerTaxInfo", "buyer_tax_info"),
            serialization_alias="BuyerTaxInfo",
            description="Tax information about the buyer. Sellers can use this data to issue electronic invoices for business orders. **Note**: This attribute is only available for business orders in the Brazil, Mexico and India marketplaces.",
        ),
    ]

    purchase_order_number: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "PurchaseOrderNumber", "purchase_order_number"
            ),
            serialization_alias="PurchaseOrderNumber",
            description="The purchase order (PO) number entered by the buyer at checkout. Only returned for orders where the buyer entered a PO number at checkout.",
        ),
    ]


"""
GetOrderBuyerInfoResponse

The response schema for the `getOrderBuyerInfo` operation.
"""


class GetOrderBuyerInfoResponse(SpApiBaseModel):
    """The response schema for the `getOrderBuyerInfo` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["OrderBuyerInfo"],
        Field(None, description="The payload for the `getOrderBuyerInfo` operation."),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
            description="One or more unexpected errors occurred during the `getOrderBuyerInfo` operation.",
        ),
    ]


"""
GetOrderItemsBuyerInfoRequest

Request parameters for getOrderItemsBuyerInfo
"""


class GetOrderItemsBuyerInfoRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getOrderItemsBuyerInfo
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
            description="[PATH] An Amazon-defined order identifier, in 3-7-7 format.",
        ),
    ]

    next_token: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("NextToken", "next_token"),
            serialization_alias="NextToken",
            description="[QUERY] A string token returned in the response of your previous request.",
        ),
    ]


OrderItemBuyerInfoList = List["OrderItemBuyerInfo"]
"""A single order item's buyer information list."""


"""
OrderItemsBuyerInfoList

A single order item's buyer information list with the order ID.
"""


class OrderItemsBuyerInfoList(SpApiBaseModel):
    """A single order item's buyer information list with the order ID."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    order_items: Annotated[
        "OrderItemBuyerInfoList",
        Field(
            ...,
            validation_alias=AliasChoices("OrderItems", "order_items"),
            serialization_alias="OrderItems",
        ),
    ]

    next_token: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("NextToken", "next_token"),
            serialization_alias="NextToken",
            description="When present and not empty, pass this string token in the next request to return the next response page.",
        ),
    ]

    amazon_order_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("AmazonOrderId", "amazon_order_id"),
            serialization_alias="AmazonOrderId",
            description="An Amazon-defined order identifier, in 3-7-7 format.",
        ),
    ]


"""
GetOrderItemsBuyerInfoResponse

The response schema for the `getOrderItemsBuyerInfo` operation.
"""


class GetOrderItemsBuyerInfoResponse(SpApiBaseModel):
    """The response schema for the `getOrderItemsBuyerInfo` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["OrderItemsBuyerInfoList"],
        Field(
            None, description="The payload for the `getOrderItemsBuyerInfo` operation."
        ),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
            description="One or more unexpected errors occurred during the `getOrderItemsBuyerInfo` operation.",
        ),
    ]


"""
GetOrderItemsRequest

Request parameters for getOrderItems
"""


class GetOrderItemsRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getOrderItems
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
            description="[PATH] An Amazon-defined order identifier, in 3-7-7 format.",
        ),
    ]

    next_token: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("NextToken", "next_token"),
            serialization_alias="NextToken",
            description="[QUERY] A string token returned in the response of your previous request.",
        ),
    ]


OrderItemList = List["OrderItem"]
"""A list of order items."""


"""
OrderItemsList

The order items list along with the order ID.
"""


class OrderItemsList(SpApiBaseModel):
    """The order items list along with the order ID."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    order_items: Annotated[
        "OrderItemList",
        Field(
            ...,
            validation_alias=AliasChoices("OrderItems", "order_items"),
            serialization_alias="OrderItems",
        ),
    ]

    next_token: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("NextToken", "next_token"),
            serialization_alias="NextToken",
            description="When present and not empty, pass this string token in the next request to return the next response page.",
        ),
    ]

    amazon_order_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("AmazonOrderId", "amazon_order_id"),
            serialization_alias="AmazonOrderId",
            description="An Amazon-defined order identifier, in 3-7-7 format.",
        ),
    ]


"""
GetOrderItemsResponse

The response schema for the `getOrderItems` operation.
"""


class GetOrderItemsResponse(SpApiBaseModel):
    """The response schema for the `getOrderItems` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["OrderItemsList"],
        Field(None, description="The payload for the `getOrderItems` operation."),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
            description="One or more unexpected errors occurred during the `getOrderItems` operation.",
        ),
    ]


"""
GetOrderRegulatedInfoRequest

Request parameters for getOrderRegulatedInfo
"""


class GetOrderRegulatedInfoRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getOrderRegulatedInfo
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
            description="[PATH] An Amazon-defined order identifier, in 3-7-7 format.",
        ),
    ]


# Enum definitions
class FieldTypeEnum(str, Enum):
    """Enum for FieldType"""

    TEXT = "Text"  # This field is a text representation of the response collected from the regulatory form.
    FILE_ATTACHMENT = "FileAttachment"  # This field contains a link to an attachment collected from the regulatory form.


"""
RegulatedInformationField

A field collected from the regulatory form.
"""


class RegulatedInformationField(SpApiBaseModel):
    """A field collected from the regulatory form."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    field_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("FieldId", "field_id"),
            serialization_alias="FieldId",
            description="The unique identifier of the field.",
        ),
    ]

    field_label: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("FieldLabel", "field_label"),
            serialization_alias="FieldLabel",
            description="The name of the field.",
        ),
    ]

    field_type: Annotated[
        FieldTypeEnum,
        Field(
            ...,
            validation_alias=AliasChoices("FieldType", "field_type"),
            serialization_alias="FieldType",
            description="The type of field.",
        ),
    ]

    field_value: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("FieldValue", "field_value"),
            serialization_alias="FieldValue",
            description="The content of the field as collected in regulatory form. Note that `FileAttachment` type fields contain a URL where you can download the attachment.",
        ),
    ]


"""
RegulatedInformation

The regulated information collected during purchase and used to verify the order.
"""


class RegulatedInformation(SpApiBaseModel):
    """The regulated information collected during purchase and used to verify the order."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    fields: Annotated[
        List["RegulatedInformationField"],
        Field(
            ...,
            validation_alias=AliasChoices("Fields", "fields"),
            serialization_alias="Fields",
            description="A list of regulated information fields as collected from the regulatory form.",
        ),
    ]


"""
RejectionReason

The reason for rejecting the order's regulated information. This is only present if the order is rejected.
"""


class RejectionReason(SpApiBaseModel):
    """The reason for rejecting the order's regulated information. This is only present if the order is rejected."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    rejection_reason_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("RejectionReasonId", "rejection_reason_id"),
            serialization_alias="RejectionReasonId",
            description="The unique identifier for the rejection reason.",
        ),
    ]

    rejection_reason_description: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices(
                "RejectionReasonDescription", "rejection_reason_description"
            ),
            serialization_alias="RejectionReasonDescription",
            description="The description of this rejection reason.",
        ),
    ]


VerificationStatus = str
"""The verification status of the order."""


"""
ValidVerificationDetail

The types of verification details that may be provided for the order and the criteria required for when the type of verification detail can be provided. The types of verification details allowed depend on the type of regulated product and will not change order to order.
"""


class ValidVerificationDetail(SpApiBaseModel):
    """The types of verification details that may be provided for the order and the criteria required for when the type of verification detail can be provided. The types of verification details allowed depend on the type of regulated product and will not change order to order."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    verification_detail_type: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices(
                "VerificationDetailType", "verification_detail_type"
            ),
            serialization_alias="VerificationDetailType",
            description="A supported type of verification detail. The type indicates which verification detail could be shared while updating the regulated order. Valid value: `prescriptionDetail`.",
        ),
    ]

    valid_verification_statuses: Annotated[
        List["VerificationStatus"],
        Field(
            ...,
            validation_alias=AliasChoices(
                "ValidVerificationStatuses", "valid_verification_statuses"
            ),
            serialization_alias="ValidVerificationStatuses",
            description="A list of valid verification statuses where the associated verification detail type may be provided. For example, if the value of this field is ['Approved'], calls to provide the associated verification detail will fail for orders with a `VerificationStatus` of `Pending`, `Rejected`, `Expired`, or `Cancelled`.",
        ),
    ]


"""
RegulatedOrderVerificationStatus

The verification status of the order, along with associated approval or rejection metadata.
"""


class RegulatedOrderVerificationStatus(SpApiBaseModel):
    """The verification status of the order, along with associated approval or rejection metadata."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    status: Annotated[
        "VerificationStatus",
        Field(
            ...,
            validation_alias=AliasChoices("Status", "status"),
            serialization_alias="Status",
            description="The verification status of the order.",
        ),
    ]

    requires_merchant_action: Annotated[
        bool,
        Field(
            ...,
            validation_alias=AliasChoices(
                "RequiresMerchantAction", "requires_merchant_action"
            ),
            serialization_alias="RequiresMerchantAction",
            description="When true, the regulated information provided in the order requires a review by the merchant.",
        ),
    ]

    valid_rejection_reasons: Annotated[
        List["RejectionReason"],
        Field(
            ...,
            validation_alias=AliasChoices(
                "ValidRejectionReasons", "valid_rejection_reasons"
            ),
            serialization_alias="ValidRejectionReasons",
            description="A list of valid rejection reasons that may be used to reject the order's regulated information.",
        ),
    ]

    rejection_reason: Annotated[
        Optional["RejectionReason"],
        Field(
            None,
            validation_alias=AliasChoices("RejectionReason", "rejection_reason"),
            serialization_alias="RejectionReason",
            description="The reason for rejecting the order's regulated information. Not present if the order isn't rejected.",
        ),
    ]

    review_date: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("ReviewDate", "review_date"),
            serialization_alias="ReviewDate",
            description="The date the order was reviewed. In [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date time format.",
        ),
    ]

    external_reviewer_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("ExternalReviewerId", "external_reviewer_id"),
            serialization_alias="ExternalReviewerId",
            description="The identifier for the order's regulated information reviewer.",
        ),
    ]

    valid_verification_details: Annotated[
        Optional[List["ValidVerificationDetail"]],
        Field(
            None,
            validation_alias=AliasChoices(
                "ValidVerificationDetails", "valid_verification_details"
            ),
            serialization_alias="ValidVerificationDetails",
            description="A list of valid verification details that may be provided and the criteria required for when the verification detail can be provided.",
        ),
    ]


"""
OrderRegulatedInfo

The order's regulated information along with its verification status.
"""


class OrderRegulatedInfo(SpApiBaseModel):
    """The order's regulated information along with its verification status."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    amazon_order_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("AmazonOrderId", "amazon_order_id"),
            serialization_alias="AmazonOrderId",
            description="An Amazon-defined order identifier, in 3-7-7 format.",
        ),
    ]

    regulated_information: Annotated[
        "RegulatedInformation",
        Field(
            ...,
            validation_alias=AliasChoices(
                "RegulatedInformation", "regulated_information"
            ),
            serialization_alias="RegulatedInformation",
            description="The regulated information collected during purchase and used to verify the order.",
        ),
    ]

    requires_dosage_label: Annotated[
        bool,
        Field(
            ...,
            validation_alias=AliasChoices(
                "RequiresDosageLabel", "requires_dosage_label"
            ),
            serialization_alias="RequiresDosageLabel",
            description="When true, the order requires attaching a dosage information label when shipped.",
        ),
    ]

    regulated_order_verification_status: Annotated[
        "RegulatedOrderVerificationStatus",
        Field(
            ...,
            validation_alias=AliasChoices(
                "RegulatedOrderVerificationStatus",
                "regulated_order_verification_status",
            ),
            serialization_alias="RegulatedOrderVerificationStatus",
            description="The order's verification status.",
        ),
    ]


"""
GetOrderRegulatedInfoResponse

The response schema for the `getOrderRegulatedInfo` operation.
"""


class GetOrderRegulatedInfoResponse(SpApiBaseModel):
    """The response schema for the `getOrderRegulatedInfo` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["OrderRegulatedInfo"],
        Field(
            None, description="The payload for the `getOrderRegulatedInfo` operation."
        ),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
            description="One or more unexpected errors occurred during the `getOrderRegulatedInfo` operation.",
        ),
    ]


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

    order_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("orderId", "order_id"),
            serialization_alias="orderId",
            description="[PATH] An Amazon-defined order identifier, in 3-7-7 format.",
        ),
    ]


"""
MarketplaceTaxInfo

Tax information about the marketplace.
"""


class MarketplaceTaxInfo(SpApiBaseModel):
    """Tax information about the marketplace."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    tax_classifications: Annotated[
        Optional[List["TaxClassification"]],
        Field(
            None,
            validation_alias=AliasChoices("TaxClassifications", "tax_classifications"),
            serialization_alias="TaxClassifications",
            description="A list of tax classifications that apply to the order.",
        ),
    ]


PaymentExecutionDetailItemList = List["PaymentExecutionDetailItem"]
"""A list of payment execution detail items."""


"""
PaymentMethodDetailItemList

A list of payment method detail items.
"""


class PaymentMethodDetailItemList(SpApiBaseModel):
    """A list of payment method detail items."""

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow",
        serialize_by_alias=True,
        arbitrary_types_allowed=True,
    )


# Enum definitions
class OrderStatusEnum(str, Enum):
    """Enum for OrderStatus"""

    PENDING = "Pending"  # The order has been placed but payment has not been authorized. The order is not ready for shipment. Note that for orders with `OrderType = Standard`, the initial order status is Pending. For orders with `OrderType = Preorder`, the initial order status is `PendingAvailability`, and the order passes into the Pending status when the payment authorization process begins.
    UNSHIPPED = "Unshipped"  # Payment has been authorized and order is ready for shipment, but no items in the order have been shipped.
    PARTIALLY_SHIPPED = "PartiallyShipped"  # One or more (but not all) items in the order have been shipped.
    SHIPPED = "Shipped"  # All items in the order have been shipped.
    CANCELED = "Canceled"  # The order was canceled.
    UNFULFILLABLE = "Unfulfillable"  # The order cannot be fulfilled. This state applies only to Amazon-fulfilled orders that were not placed on Amazon's retail web site.
    INVOICE_UNCONFIRMED = "InvoiceUnconfirmed"  # All items in the order have been shipped. The seller has not yet given confirmation to Amazon that the invoice has been shipped to the buyer.
    PENDING_AVAILABILITY = "PendingAvailability"  # This status is available for pre-orders only. The order has been placed, payment has not been authorized, and the release date for the item is in the future. The order is not ready for shipment.


class FulfillmentChannelEnum(str, Enum):
    """Enum for FulfillmentChannel"""

    MFN = "MFN"  # Fulfilled by the seller.
    AFN = "AFN"  # Fulfilled by Amazon.


class PaymentMethodEnum(str, Enum):
    """Enum for PaymentMethod"""

    COD = "COD"  # Cash on delivery.
    CVS = "CVS"  # Convenience store.
    OTHER = "Other"  # A payment method other than COD and CVS.


class OrderTypeEnum(str, Enum):
    """Enum for OrderType"""

    STANDARD_ORDER = "StandardOrder"  # An order that contains items for which the selling partner currently has inventory in stock.
    LONG_LEAD_TIME_ORDER = "LongLeadTimeOrder"  # An order that contains items that have a long lead time to ship.
    PREORDER = "Preorder"  # An order that contains items with a release date that is in the future.
    BACK_ORDER = "BackOrder"  # An order that contains items that already have been released in the market but are currently out of stock and will be available in the future.
    SOURCING_ON_DEMAND_ORDER = "SourcingOnDemandOrder"  # A Sourcing On Demand order.


class BuyerInvoicePreferenceEnum(str, Enum):
    """Enum for BuyerInvoicePreference"""

    INDIVIDUAL = "INDIVIDUAL"  # Issues an individual invoice to the buyer.
    BUSINESS = "BUSINESS"  # Issues a business invoice to the buyer. Tax information is available in `BuyerTaxInformation`.


"""
Order

Order information.
"""


class Order(SpApiBaseModel):
    """Order information."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    amazon_order_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("AmazonOrderId", "amazon_order_id"),
            serialization_alias="AmazonOrderId",
            description="An Amazon-defined order identifier, in 3-7-7 format.",
        ),
    ]

    seller_order_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("SellerOrderId", "seller_order_id"),
            serialization_alias="SellerOrderId",
            description="A seller-defined order identifier.",
        ),
    ]

    purchase_date: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("PurchaseDate", "purchase_date"),
            serialization_alias="PurchaseDate",
            description="The date when the order was created.",
        ),
    ]

    last_update_date: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("LastUpdateDate", "last_update_date"),
            serialization_alias="LastUpdateDate",
            description="The date when the order was last updated. __Note__: `LastUpdateDate` is returned with an incorrect date for orders that were last updated before 2009-04-01.",
        ),
    ]

    order_status: Annotated[
        OrderStatusEnum,
        Field(
            ...,
            validation_alias=AliasChoices("OrderStatus", "order_status"),
            serialization_alias="OrderStatus",
            description="The current order status.",
        ),
    ]

    fulfillment_channel: Annotated[
        Optional[FulfillmentChannelEnum],
        Field(
            None,
            validation_alias=AliasChoices("FulfillmentChannel", "fulfillment_channel"),
            serialization_alias="FulfillmentChannel",
            description="Whether the order was fulfilled by Amazon (`AFN`) or by the seller (`MFN`).",
        ),
    ]

    sales_channel: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("SalesChannel", "sales_channel"),
            serialization_alias="SalesChannel",
            description="The sales channel for the first item in the order.",
        ),
    ]

    order_channel: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("OrderChannel", "order_channel"),
            serialization_alias="OrderChannel",
            description="The order channel for the first item in the order.",
        ),
    ]

    ship_service_level: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("ShipServiceLevel", "ship_service_level"),
            serialization_alias="ShipServiceLevel",
            description="The order's shipment service level.",
        ),
    ]

    order_total: Annotated[
        Optional["Money"],
        Field(
            None,
            validation_alias=AliasChoices("OrderTotal", "order_total"),
            serialization_alias="OrderTotal",
            description="The total charge for this order.",
        ),
    ]

    number_of_items_shipped: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices(
                "NumberOfItemsShipped", "number_of_items_shipped"
            ),
            serialization_alias="NumberOfItemsShipped",
            description="The number of items shipped.",
        ),
    ]

    number_of_items_unshipped: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices(
                "NumberOfItemsUnshipped", "number_of_items_unshipped"
            ),
            serialization_alias="NumberOfItemsUnshipped",
            description="The number of items unshipped.",
        ),
    ]

    payment_execution_detail: Annotated[
        Optional["PaymentExecutionDetailItemList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "PaymentExecutionDetail", "payment_execution_detail"
            ),
            serialization_alias="PaymentExecutionDetail",
            description="Information about sub-payment methods for a cash-on-delivery (COD) order. __Note__: For a COD order that is paid for using one sub-payment method, one `PaymentExecutionDetailItem` object is returned, with `PaymentExecutionDetailItem`/`PaymentMethod = COD`. For a COD order that is paid for using multiple sub-payment methods, two or more `PaymentExecutionDetailItem` objects are returned.",
        ),
    ]

    payment_method: Annotated[
        Optional[PaymentMethodEnum],
        Field(
            None,
            validation_alias=AliasChoices("PaymentMethod", "payment_method"),
            serialization_alias="PaymentMethod",
            description="The payment method for the order. This property is limited to COD and CVS payment methods. Unless you need the specific COD payment information provided by the `PaymentExecutionDetailItem` object, we recommend using the `PaymentMethodDetails` property to get payment method information.",
        ),
    ]

    payment_method_details: Annotated[
        Optional["PaymentMethodDetailItemList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "PaymentMethodDetails", "payment_method_details"
            ),
            serialization_alias="PaymentMethodDetails",
            description="A list of payment methods for the order.",
        ),
    ]

    marketplace_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("MarketplaceId", "marketplace_id"),
            serialization_alias="MarketplaceId",
            description="The identifier for the marketplace where the order was placed.",
        ),
    ]

    shipment_service_level_category: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "ShipmentServiceLevelCategory", "shipment_service_level_category"
            ),
            serialization_alias="ShipmentServiceLevelCategory",
            description="The shipment service level category for the order. **Possible values**: `Expedited`, `FreeEconomy`, `NextDay`, `Priority`, `SameDay`, `SecondDay`, `Scheduled`, and `Standard`.",
        ),
    ]

    easy_ship_shipment_status: Annotated[
        Optional["EasyShipShipmentStatus"],
        Field(
            None,
            validation_alias=AliasChoices(
                "EasyShipShipmentStatus", "easy_ship_shipment_status"
            ),
            serialization_alias="EasyShipShipmentStatus",
            description="The status of the Amazon Easy Ship order. This property is only included for Amazon Easy Ship orders.",
        ),
    ]

    cba_displayable_shipping_label: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "CbaDisplayableShippingLabel", "cba_displayable_shipping_label"
            ),
            serialization_alias="CbaDisplayableShippingLabel",
            description="Custom ship label for Checkout by Amazon (CBA).",
        ),
    ]

    order_type: Annotated[
        Optional[OrderTypeEnum],
        Field(
            None,
            validation_alias=AliasChoices("OrderType", "order_type"),
            serialization_alias="OrderType",
            description="The order's type.",
        ),
    ]

    earliest_ship_date: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("EarliestShipDate", "earliest_ship_date"),
            serialization_alias="EarliestShipDate",
            description="The start of the time period within which you have committed to ship the order. In [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date time format. Only returned for seller-fulfilled orders. __Note__: `EarliestShipDate` might not be returned for orders placed before February 1, 2013.",
        ),
    ]

    latest_ship_date: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("LatestShipDate", "latest_ship_date"),
            serialization_alias="LatestShipDate",
            description="The end of the time period within which you have committed to ship the order. In [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date time format. Only returned for seller-fulfilled orders. __Note__: `LatestShipDate` might not be returned for orders placed before February 1, 2013.",
        ),
    ]

    earliest_delivery_date: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "EarliestDeliveryDate", "earliest_delivery_date"
            ),
            serialization_alias="EarliestDeliveryDate",
            description="The start of the time period within which you have committed to fulfill the order. In [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date time format. Only returned for seller-fulfilled orders.",
        ),
    ]

    latest_delivery_date: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("LatestDeliveryDate", "latest_delivery_date"),
            serialization_alias="LatestDeliveryDate",
            description="The end of the time period within which you have committed to fulfill the order. In [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date time format. Only returned for seller-fulfilled orders that do not have a `PendingAvailability`, `Pending`, or `Canceled` status.",
        ),
    ]

    is_business_order: Annotated[
        Optional[bool],
        Field(
            None,
            validation_alias=AliasChoices("IsBusinessOrder", "is_business_order"),
            serialization_alias="IsBusinessOrder",
            description="When true, the order is an Amazon Business order. An Amazon Business order is an order where the buyer is a Verified Business Buyer.",
        ),
    ]

    is_prime: Annotated[
        Optional[bool],
        Field(
            None,
            validation_alias=AliasChoices("IsPrime", "is_prime"),
            serialization_alias="IsPrime",
            description="When true, the order is a seller-fulfilled Amazon Prime order.",
        ),
    ]

    is_premium_order: Annotated[
        Optional[bool],
        Field(
            None,
            validation_alias=AliasChoices("IsPremiumOrder", "is_premium_order"),
            serialization_alias="IsPremiumOrder",
            description="When true, the order has a Premium Shipping Service Level Agreement. For more information about Premium Shipping orders, refer to 'Premium Shipping Options' in the Seller Central Help for your marketplace.",
        ),
    ]

    is_global_express_enabled: Annotated[
        Optional[bool],
        Field(
            None,
            validation_alias=AliasChoices(
                "IsGlobalExpressEnabled", "is_global_express_enabled"
            ),
            serialization_alias="IsGlobalExpressEnabled",
            description="When true, the order is a `GlobalExpress` order.",
        ),
    ]

    replaced_order_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("ReplacedOrderId", "replaced_order_id"),
            serialization_alias="ReplacedOrderId",
            description="The order ID value for the order that is being replaced. Returned only if IsReplacementOrder = true.",
        ),
    ]

    is_replacement_order: Annotated[
        Optional[bool],
        Field(
            None,
            validation_alias=AliasChoices("IsReplacementOrder", "is_replacement_order"),
            serialization_alias="IsReplacementOrder",
            description="When true, this is a replacement order.",
        ),
    ]

    promise_response_due_date: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "PromiseResponseDueDate", "promise_response_due_date"
            ),
            serialization_alias="PromiseResponseDueDate",
            description="Indicates the date by which the seller must respond to the buyer with an estimated ship date. Only returned for Sourcing on Demand orders.",
        ),
    ]

    is_estimated_ship_date_set: Annotated[
        Optional[bool],
        Field(
            None,
            validation_alias=AliasChoices(
                "IsEstimatedShipDateSet", "is_estimated_ship_date_set"
            ),
            serialization_alias="IsEstimatedShipDateSet",
            description="When true, the estimated ship date is set for the order. Only returned for Sourcing on Demand orders.",
        ),
    ]

    is_sold_by_a_b: Annotated[
        Optional[bool],
        Field(
            None,
            validation_alias=AliasChoices("IsSoldByAB", "is_sold_by_a_b"),
            serialization_alias="IsSoldByAB",
            description="When true, the item within this order was bought and re-sold by Amazon Business EU SARL (ABEU). By buying and instantly re-selling your items, ABEU becomes the seller of record, making your inventory available for sale to customers who would not otherwise purchase from a third-party seller.",
        ),
    ]

    is_i_b_a: Annotated[
        Optional[bool],
        Field(
            None,
            validation_alias=AliasChoices("IsIBA", "is_i_b_a"),
            serialization_alias="IsIBA",
            description="When true, the item within this order was bought and re-sold by Amazon Business EU SARL (ABEU). By buying and instantly re-selling your items, ABEU becomes the seller of record, making your inventory available for sale to customers who would not otherwise purchase from a third-party seller.",
        ),
    ]

    default_ship_from_location_address: Annotated[
        Optional["Address"],
        Field(
            None,
            validation_alias=AliasChoices(
                "DefaultShipFromLocationAddress", "default_ship_from_location_address"
            ),
            serialization_alias="DefaultShipFromLocationAddress",
            description="The recommended location for the seller to ship the items from. It is calculated at checkout. The seller may or may not choose to ship from this location.",
        ),
    ]

    buyer_invoice_preference: Annotated[
        Optional[BuyerInvoicePreferenceEnum],
        Field(
            None,
            validation_alias=AliasChoices(
                "BuyerInvoicePreference", "buyer_invoice_preference"
            ),
            serialization_alias="BuyerInvoicePreference",
            description="The buyer's invoicing preference. Sellers can use this data to issue electronic invoices for orders in Turkey. **Note**: This attribute is only available in the Turkey marketplace.",
        ),
    ]

    buyer_tax_information: Annotated[
        Optional["BuyerTaxInformation"],
        Field(
            None,
            validation_alias=AliasChoices(
                "BuyerTaxInformation", "buyer_tax_information"
            ),
            serialization_alias="BuyerTaxInformation",
            description="Contains the business invoice tax information. Sellers could use this data to issue electronic invoices for business orders in Turkey. **Note**: 1. This attribute is only available in the Turkey marketplace for the orders that `BuyerInvoicePreference` is BUSINESS. 2. The `BuyerTaxInformation` is a restricted data. Use the Restricted Data Token (RDT) and restricted SPDS roles to access this restricted data.",
        ),
    ]

    fulfillment_instruction: Annotated[
        Optional["FulfillmentInstruction"],
        Field(
            None,
            validation_alias=AliasChoices(
                "FulfillmentInstruction", "fulfillment_instruction"
            ),
            serialization_alias="FulfillmentInstruction",
            description="Contains the instructions about the fulfillment, such as the location from where you want the order filled.",
        ),
    ]

    is_i_s_p_u: Annotated[
        Optional[bool],
        Field(
            None,
            validation_alias=AliasChoices("IsISPU", "is_i_s_p_u"),
            serialization_alias="IsISPU",
            description="When true, this order is marked to be picked up from a store rather than delivered.",
        ),
    ]

    is_access_point_order: Annotated[
        Optional[bool],
        Field(
            None,
            validation_alias=AliasChoices(
                "IsAccessPointOrder", "is_access_point_order"
            ),
            serialization_alias="IsAccessPointOrder",
            description="When true, this order is marked to be delivered to an Access Point. The access location is chosen by the customer. Access Points include Amazon Hub Lockers, Amazon Hub Counters, and pickup points operated by carriers.",
        ),
    ]

    marketplace_tax_info: Annotated[
        Optional["MarketplaceTaxInfo"],
        Field(
            None,
            validation_alias=AliasChoices("MarketplaceTaxInfo", "marketplace_tax_info"),
            serialization_alias="MarketplaceTaxInfo",
            description="Tax information about the marketplace where the sale took place. Sellers can use this data to issue electronic invoices for orders in Brazil. **Note**: This attribute is only available in the Brazil marketplace for the orders with `Pending` or `Unshipped` status.",
        ),
    ]

    seller_display_name: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("SellerDisplayName", "seller_display_name"),
            serialization_alias="SellerDisplayName",
            description="The seller’s friendly name registered in the marketplace where the sale took place. Sellers can use this data to issue electronic invoices for orders in Brazil. **Note**: This attribute is only available in the Brazil marketplace for the orders with `Pending` or `Unshipped` status.",
        ),
    ]

    shipping_address: Annotated[
        Optional["Address"],
        Field(
            None,
            validation_alias=AliasChoices("ShippingAddress", "shipping_address"),
            serialization_alias="ShippingAddress",
            description="The shipping address for the order. **Note**: 1. `ShippingAddress` is only available for orders with the following status values: Unshipped, `PartiallyShipped`, Shipped and `InvoiceUnconfirmed`. 2. The `ShippingAddress` contains restricted data. Use the Restricted Data Token (RDT) and restricted SPDS roles to access the restricted data in `ShippingAddress`. For example, `Name`, `AddressLine1`, `AddressLine2`, `AddressLine3`, `Phone`, `AddressType`, and `ExtendedFields`.",
        ),
    ]

    buyer_info: Annotated[
        Optional["BuyerInfo"],
        Field(
            None,
            validation_alias=AliasChoices("BuyerInfo", "buyer_info"),
            serialization_alias="BuyerInfo",
            description="Buyer information. **Note**: The `BuyerInfo` contains restricted data. Use the Restricted Data Token (RDT) and restricted SPDS roles to access the restricted data in `BuyerInfo`. For example, `BuyerName`, `BuyerTaxInfo`, and `PurchaseOrderNumber`.",
        ),
    ]

    automated_shipping_settings: Annotated[
        Optional["AutomatedShippingSettings"],
        Field(
            None,
            validation_alias=AliasChoices(
                "AutomatedShippingSettings", "automated_shipping_settings"
            ),
            serialization_alias="AutomatedShippingSettings",
            description="Contains information regarding the Shipping Settings Automaton program, such as whether the order's shipping settings were generated automatically, and what those settings are.",
        ),
    ]

    has_regulated_items: Annotated[
        Optional[bool],
        Field(
            None,
            validation_alias=AliasChoices("HasRegulatedItems", "has_regulated_items"),
            serialization_alias="HasRegulatedItems",
            description="Whether the order contains regulated items which may require additional approval steps before being fulfilled.",
        ),
    ]

    electronic_invoice_status: Annotated[
        Optional["ElectronicInvoiceStatus"],
        Field(
            None,
            validation_alias=AliasChoices(
                "ElectronicInvoiceStatus", "electronic_invoice_status"
            ),
            serialization_alias="ElectronicInvoiceStatus",
            description="The status of the electronic invoice.",
        ),
    ]


"""
GetOrderResponse

The response schema for the `getOrder` operation.
"""


class GetOrderResponse(SpApiBaseModel):
    """The response schema for the `getOrder` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["Order"],
        Field(None, description="The payload for the `getOrder` operation."),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
            description="One or more unexpected errors occurred during the `getOrder` operation.",
        ),
    ]


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

    created_after: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("CreatedAfter", "created_after"),
            serialization_alias="CreatedAfter",
            description="[QUERY] Use this date to select orders created after (or at) a specified time. Only orders placed after the specified time are returned. The date must be in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) format.  **Note**: Either the `CreatedAfter` parameter or the `LastUpdatedAfter` parameter is required. Both cannot be empty. `LastUpdatedAfter` and `LastUpdatedBefore` cannot be set when `CreatedAfter` is set.",
        ),
    ]

    created_before: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("CreatedBefore", "created_before"),
            serialization_alias="CreatedBefore",
            description="[QUERY] Use this date to select orders created before (or at) a specified time. Only orders placed before the specified time are returned. The date must be in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) format.  **Note**: `CreatedBefore` is optional when `CreatedAfter` is set. If specified, `CreatedBefore` must be equal to or after the `CreatedAfter` date and at least two minutes before current time.",
        ),
    ]

    last_updated_after: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("LastUpdatedAfter", "last_updated_after"),
            serialization_alias="LastUpdatedAfter",
            description="[QUERY] Use this date to select orders that were last updated after (or at) a specified time. An update is defined as any change in order status, including the creation of a new order. Includes updates made by Amazon and by the seller. The date must be in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) format.  **Note**: Either the `CreatedAfter` parameter or the `LastUpdatedAfter` parameter is required. Both cannot be empty. `CreatedAfter` or `CreatedBefore` cannot be set when `LastUpdatedAfter` is set.",
        ),
    ]

    last_updated_before: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("LastUpdatedBefore", "last_updated_before"),
            serialization_alias="LastUpdatedBefore",
            description="[QUERY] Use this date to select orders that were last updated before (or at) a specified time. An update is defined as any change in order status, including the creation of a new order. Includes updates made by Amazon and by the seller. The date must be in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) format.  **Note**: `LastUpdatedBefore` is optional when `LastUpdatedAfter` is set. But if specified, `LastUpdatedBefore` must be equal to or after the `LastUpdatedAfter` date and at least two minutes before current time.",
        ),
    ]

    order_statuses: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("OrderStatuses", "order_statuses"),
            serialization_alias="OrderStatuses",
            description="[QUERY] A list of `OrderStatus` values used to filter the results.  **Possible values:** - `PendingAvailability` (This status is available for pre-orders only. The order has been placed, payment has not been authorized, and the release date of the item is in the future.) - `Pending` (The order has been placed but payment has not been authorized.) - `Unshipped` (Payment has been authorized and the order is ready for shipment, but no items in the order have been shipped.) - `PartiallyShipped` (One or more, but not all, items in the order have been shipped.) - `Shipped` (All items in the order have been shipped.) - `InvoiceUnconfirmed` (All items in the order have been shipped. The seller has not yet given confirmation to Amazon that the invoice has been shipped to the buyer.) - `Canceled` (The order has been canceled.) - `Unfulfillable` (The order cannot be fulfilled. This state applies only to Multi-Channel Fulfillment orders.)",
        ),
    ]

    marketplace_ids: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("MarketplaceIds", "marketplace_ids"),
            serialization_alias="MarketplaceIds",
            description="[QUERY] A list of `MarketplaceId` values. Used to select orders that were placed in the specified marketplaces.  Refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids) for a complete list of `marketplaceId` values.",
        ),
    ]

    fulfillment_channels: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices(
                "FulfillmentChannels", "fulfillment_channels"
            ),
            serialization_alias="FulfillmentChannels",
            description="[QUERY] A list that indicates how an order was fulfilled. Filters the results by fulfillment channel.   **Possible values**: `AFN` (fulfilled by Amazon), `MFN` (fulfilled by seller).",
        ),
    ]

    payment_methods: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("PaymentMethods", "payment_methods"),
            serialization_alias="PaymentMethods",
            description="[QUERY] A list of payment method values. Use this field to select orders that were paid with the specified payment methods.  **Possible values**: `COD` (cash on delivery), `CVS` (convenience store), `Other` (Any payment method other than COD or CVS).",
        ),
    ]

    buyer_email: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("BuyerEmail", "buyer_email"),
            serialization_alias="BuyerEmail",
            description="[QUERY] The email address of a buyer. Used to select orders that contain the specified email address.",
        ),
    ]

    seller_order_id: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("SellerOrderId", "seller_order_id"),
            serialization_alias="SellerOrderId",
            description="[QUERY] An order identifier that is specified by the seller. Used to select only the orders that match the order identifier. If `SellerOrderId` is specified, then `FulfillmentChannels`, `OrderStatuses`, `PaymentMethod`, `LastUpdatedAfter`, LastUpdatedBefore, and `BuyerEmail` cannot be specified.",
        ),
    ]

    max_results_per_page: Annotated[
        Optional[int],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("MaxResultsPerPage", "max_results_per_page"),
            serialization_alias="MaxResultsPerPage",
            description="[QUERY] A number that indicates the maximum number of orders that can be returned per page. Value must be 1 - 100. Default 100.",
        ),
    ]

    easy_ship_shipment_statuses: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices(
                "EasyShipShipmentStatuses", "easy_ship_shipment_statuses"
            ),
            serialization_alias="EasyShipShipmentStatuses",
            description="[QUERY] A list of `EasyShipShipmentStatus` values. Used to select Easy Ship orders with statuses that match the specified values. If `EasyShipShipmentStatus` is specified, only Amazon Easy Ship orders are returned.  **Possible values:** - `PendingSchedule` (The package is awaiting the schedule for pick-up.) - `PendingPickUp` (Amazon has not yet picked up the package from the seller.) - `PendingDropOff` (The seller will deliver the package to the carrier.) - `LabelCanceled` (The seller canceled the pickup.) - `PickedUp` (Amazon has picked up the package from the seller.) - `DroppedOff` (The package is delivered to the carrier by the seller.) - `AtOriginFC` (The packaged is at the origin fulfillment center.) - `AtDestinationFC` (The package is at the destination fulfillment center.) - `Delivered` (The package has been delivered.) - `RejectedByBuyer` (The package has been rejected by the buyer.) - `Undeliverable` (The package cannot be delivered.) - `ReturningToSeller` (The package was not delivered and is being returned to the seller.) - `ReturnedToSeller` (The package was not delivered and was returned to the seller.) - `Lost` (The package is lost.) - `OutForDelivery` (The package is out for delivery.) - `Damaged` (The package was damaged by the carrier.)",
        ),
    ]

    electronic_invoice_statuses: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices(
                "ElectronicInvoiceStatuses", "electronic_invoice_statuses"
            ),
            serialization_alias="ElectronicInvoiceStatuses",
            description="[QUERY] A list of `ElectronicInvoiceStatus` values. Used to select orders with electronic invoice statuses that match the specified values.  **Possible values:** - `NotRequired` (Electronic invoice submission is not required for this order.) - `NotFound` (The electronic invoice was not submitted for this order.) - `Processing` (The electronic invoice is being processed for this order.) - `Errored` (The last submitted electronic invoice was rejected for this order.) - `Accepted` (The last submitted electronic invoice was submitted and accepted.)",
        ),
    ]

    next_token: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("NextToken", "next_token"),
            serialization_alias="NextToken",
            description="[QUERY] A string token returned in the response of your previous request.",
        ),
    ]

    amazon_order_ids: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("AmazonOrderIds", "amazon_order_ids"),
            serialization_alias="AmazonOrderIds",
            description="[QUERY] A list of `AmazonOrderId` values. An `AmazonOrderId` is an Amazon-defined order identifier, in 3-7-7 format.",
        ),
    ]

    actual_fulfillment_supply_source_id: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices(
                "ActualFulfillmentSupplySourceId", "actual_fulfillment_supply_source_id"
            ),
            serialization_alias="ActualFulfillmentSupplySourceId",
            description="[QUERY] The `sourceId` of the location from where you want the order fulfilled.",
        ),
    ]

    is_i_s_p_u: Annotated[
        Optional[bool],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("IsISPU", "is_i_s_p_u"),
            serialization_alias="IsISPU",
            description="[QUERY] When true, this order is marked to be picked up from a store rather than delivered.",
        ),
    ]

    store_chain_store_id: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("StoreChainStoreId", "store_chain_store_id"),
            serialization_alias="StoreChainStoreId",
            description="[QUERY] The store chain store identifier. Linked to a specific store in a store chain.",
        ),
    ]

    earliest_delivery_date_before: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices(
                "EarliestDeliveryDateBefore", "earliest_delivery_date_before"
            ),
            serialization_alias="EarliestDeliveryDateBefore",
            description="[QUERY] Use this date to select orders with a earliest delivery date before (or at) a specified time. The date must be in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) format.",
        ),
    ]

    earliest_delivery_date_after: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices(
                "EarliestDeliveryDateAfter", "earliest_delivery_date_after"
            ),
            serialization_alias="EarliestDeliveryDateAfter",
            description="[QUERY] Use this date to select orders with a earliest delivery date after (or at) a specified time. The date must be in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) format.",
        ),
    ]

    latest_delivery_date_before: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices(
                "LatestDeliveryDateBefore", "latest_delivery_date_before"
            ),
            serialization_alias="LatestDeliveryDateBefore",
            description="[QUERY] Use this date to select orders with a latest delivery date before (or at) a specified time. The date must be in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) format.",
        ),
    ]

    latest_delivery_date_after: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices(
                "LatestDeliveryDateAfter", "latest_delivery_date_after"
            ),
            serialization_alias="LatestDeliveryDateAfter",
            description="[QUERY] Use this date to select orders with a latest delivery date after (or at) a specified time. The date must be in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) format.",
        ),
    ]


OrderList = List["Order"]
"""A list of orders."""


"""
OrdersList

A list of orders along with additional information to make subsequent API calls.
"""


class OrdersList(SpApiBaseModel):
    """A list of orders along with additional information to make subsequent API calls."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    orders: Annotated[
        "OrderList",
        Field(
            ...,
            validation_alias=AliasChoices("Orders", "orders"),
            serialization_alias="Orders",
        ),
    ]

    next_token: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("NextToken", "next_token"),
            serialization_alias="NextToken",
            description="When present and not empty, pass this string token in the next request to return the next response page.",
        ),
    ]

    last_updated_before: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("LastUpdatedBefore", "last_updated_before"),
            serialization_alias="LastUpdatedBefore",
            description="Use this date to select orders that were last updated before (or at) a specified time. An update is defined as any change in order status, including the creation of a new order. Includes updates made by Amazon and by the seller. All dates must be in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) format.",
        ),
    ]

    created_before: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("CreatedBefore", "created_before"),
            serialization_alias="CreatedBefore",
            description="Use this date to select orders created before (or at) a specified time. Only orders placed before the specified time are returned. The date must be in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) format.",
        ),
    ]


"""
GetOrdersResponse

The response schema for the `getOrders` operation.
"""


class GetOrdersResponse(SpApiBaseModel):
    """The response schema for the `getOrders` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["OrdersList"],
        Field(None, description="The payload for the `getOrders` operation."),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
            description="One or more unexpected errors occurred during the `getOrders` operation.",
        ),
    ]


"""
ItemBuyerInfo

A single item's buyer information.
"""


class ItemBuyerInfo(SpApiBaseModel):
    """A single item's buyer information."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    buyer_customized_info: Annotated[
        Optional["BuyerCustomizedInfoDetail"],
        Field(
            None,
            validation_alias=AliasChoices(
                "BuyerCustomizedInfo", "buyer_customized_info"
            ),
            serialization_alias="BuyerCustomizedInfo",
            description="Buyer information for custom orders from the Amazon Custom program. **Note**: This attribute is only available for MFN (fulfilled by seller) orders.",
        ),
    ]

    gift_wrap_price: Annotated[
        Optional["Money"],
        Field(
            None,
            validation_alias=AliasChoices("GiftWrapPrice", "gift_wrap_price"),
            serialization_alias="GiftWrapPrice",
            description="The gift wrap price of the item.",
        ),
    ]

    gift_wrap_tax: Annotated[
        Optional["Money"],
        Field(
            None,
            validation_alias=AliasChoices("GiftWrapTax", "gift_wrap_tax"),
            serialization_alias="GiftWrapTax",
            description="The tax on the gift wrap price.",
        ),
    ]

    gift_message_text: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("GiftMessageText", "gift_message_text"),
            serialization_alias="GiftMessageText",
            description="A gift message provided by the buyer. **Note**: This attribute is only available for MFN (fulfilled by seller) orders.",
        ),
    ]

    gift_wrap_level: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("GiftWrapLevel", "gift_wrap_level"),
            serialization_alias="GiftWrapLevel",
            description="The gift wrap level specified by the buyer.",
        ),
    ]


# Enum definitions
class UnitEnum(str, Enum):
    """Enum for Unit"""

    OUNCES = "OUNCES"  # The item is measured in ounces.
    POUNDS = "POUNDS"  # The item is measured in pounds.
    KILOGRAMS = "KILOGRAMS"  # The item is measured in kilograms.
    GRAMS = "GRAMS"  # The item is measured in grams.
    MILLIGRAMS = "MILLIGRAMS"  # The item is measured in milligrams.
    INCHES = "INCHES"  # The item is measured in inches.
    FEET = "FEET"  # The item is measured in feet.
    METERS = "METERS"  # The item is measured in meters.
    CENTIMETERS = "CENTIMETERS"  # The item is measured in centimeters.
    MILLIMETERS = "MILLIMETERS"  # The item is measured in millimeters.
    SQUARE_METERS = "SQUARE_METERS"  # The item is measured in square meters.
    SQUARE_CENTIMETERS = (
        "SQUARE_CENTIMETERS"  # The item is measured in square centimeters.
    )
    SQUARE_FEET = "SQUARE_FEET"  # The item is measured in square feet.
    SQUARE_INCHES = "SQUARE_INCHES"  # The item is measured in square inches.
    GALLONS = "GALLONS"  # The item is measured in gallons.
    PINTS = "PINTS"  # The item is measured in pints.
    QUARTS = "QUARTS"  # The item is measured in quarts.
    FLUID_OUNCES = "FLUID_OUNCES"  # The item is measured in fluid ounces.
    LITERS = "LITERS"  # The item is measured in liters.
    CUBIC_METERS = "CUBIC_METERS"  # The item is measured in cubic meters.
    CUBIC_FEET = "CUBIC_FEET"  # The item is measured in cubic feet.
    CUBIC_INCHES = "CUBIC_INCHES"  # The item is measured in cubic inches.
    CUBIC_CENTIMETERS = (
        "CUBIC_CENTIMETERS"  # The item is measured in cubic centimeters.
    )
    COUNT = "COUNT"  # The item is measured by count.


"""
Measurement

Measurement information for an order item.
"""


class Measurement(SpApiBaseModel):
    """Measurement information for an order item."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    unit: Annotated[
        UnitEnum,
        Field(
            ...,
            validation_alias=AliasChoices("Unit", "unit"),
            serialization_alias="Unit",
            description="The unit of measure.",
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


"""
PointsGrantedDetail

The number of Amazon Points offered with the purchase of an item, and their monetary value.
"""


class PointsGrantedDetail(SpApiBaseModel):
    """The number of Amazon Points offered with the purchase of an item, and their monetary value."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    points_number: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices("PointsNumber", "points_number"),
            serialization_alias="PointsNumber",
            description="The number of Amazon Points granted with the purchase of an item.",
        ),
    ]

    points_monetary_value: Annotated[
        Optional["Money"],
        Field(
            None,
            validation_alias=AliasChoices(
                "PointsMonetaryValue", "points_monetary_value"
            ),
            serialization_alias="PointsMonetaryValue",
            description="The monetary value of the Amazon Points granted.",
        ),
    ]


"""
ProductInfoDetail

Product information on the number of items.
"""


class ProductInfoDetail(SpApiBaseModel):
    """Product information on the number of items."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    number_of_items: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("NumberOfItems", "number_of_items"),
            serialization_alias="NumberOfItems",
            description="The total number of items that are included in the ASIN.",
        ),
    ]


"""
PromotionIdList

A list of promotion identifiers provided by the seller when the promotions were created.
"""


class PromotionIdList(SpApiBaseModel):
    """A list of promotion identifiers provided by the seller when the promotions were created."""

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow",
        serialize_by_alias=True,
        arbitrary_types_allowed=True,
    )


"""
ShippingConstraints

Delivery constraints applicable to this order.
"""


class ShippingConstraints(SpApiBaseModel):
    """Delivery constraints applicable to this order."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    pallet_delivery: Annotated[
        Optional["ConstraintType"],
        Field(
            None,
            validation_alias=AliasChoices("PalletDelivery", "pallet_delivery"),
            serialization_alias="PalletDelivery",
            description="Indicates if the line item needs to be delivered by pallet.",
        ),
    ]

    signature_confirmation: Annotated[
        Optional["ConstraintType"],
        Field(
            None,
            validation_alias=AliasChoices(
                "SignatureConfirmation", "signature_confirmation"
            ),
            serialization_alias="SignatureConfirmation",
            description="Indicates that the recipient of the line item must sign to confirm its delivery.",
        ),
    ]

    recipient_identity_verification: Annotated[
        Optional["ConstraintType"],
        Field(
            None,
            validation_alias=AliasChoices(
                "RecipientIdentityVerification", "recipient_identity_verification"
            ),
            serialization_alias="RecipientIdentityVerification",
            description="Indicates that the person receiving the line item must be the same as the intended recipient of the order.",
        ),
    ]

    recipient_age_verification: Annotated[
        Optional["ConstraintType"],
        Field(
            None,
            validation_alias=AliasChoices(
                "RecipientAgeVerification", "recipient_age_verification"
            ),
            serialization_alias="RecipientAgeVerification",
            description="Indicates that the carrier must confirm the recipient is of the legal age to receive the line item upon delivery.",
        ),
    ]


SubstitutionOptionList = List["SubstitutionOption"]
"""A collection of substitution options."""


# Enum definitions
class SubstitutionTypeEnum(str, Enum):
    """Enum for SubstitutionType"""

    CUSTOMER_PREFERENCE = (
        "CUSTOMER_PREFERENCE"  # Customer has provided the substitution preferences.
    )
    AMAZON_RECOMMENDED = (
        "AMAZON_RECOMMENDED"  # Amazon has provided the substitution preferences.
    )
    DO_NOT_SUBSTITUTE = (
        "DO_NOT_SUBSTITUTE"  # Do not provide a substitute if item is not found.
    )


"""
SubstitutionPreferences

Substitution preferences for an order item.
"""


class SubstitutionPreferences(SpApiBaseModel):
    """Substitution preferences for an order item."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    substitution_type: Annotated[
        SubstitutionTypeEnum,
        Field(
            ...,
            validation_alias=AliasChoices("SubstitutionType", "substitution_type"),
            serialization_alias="SubstitutionType",
            description="The type of substitution that these preferences represent.",
        ),
    ]

    substitution_options: Annotated[
        Optional["SubstitutionOptionList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "SubstitutionOptions", "substitution_options"
            ),
            serialization_alias="SubstitutionOptions",
            description="Substitution options for the order item.",
        ),
    ]


# Enum definitions
class ModelEnum(str, Enum):
    """Enum for Model"""

    MARKETPLACE_FACILITATOR = "MarketplaceFacilitator"  # Tax is withheld and remitted to the taxing authority by Amazon on behalf of the seller.


class ResponsiblePartyEnum(str, Enum):
    """Enum for ResponsibleParty"""

    AMAZON_SERVICES__INC_ = "Amazon Services, Inc."  # The `MarketplaceFacilitator` entity for the US marketplace.


"""
TaxCollection

Information about withheld taxes.
"""


class TaxCollection(SpApiBaseModel):
    """Information about withheld taxes."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    model: Annotated[
        Optional[ModelEnum],
        Field(
            None,
            validation_alias=AliasChoices("Model", "model"),
            serialization_alias="Model",
            description="The tax collection model applied to the item.",
        ),
    ]

    responsible_party: Annotated[
        Optional[ResponsiblePartyEnum],
        Field(
            None,
            validation_alias=AliasChoices("ResponsibleParty", "responsible_party"),
            serialization_alias="ResponsibleParty",
            description="The party responsible for withholding the taxes and remitting them to the taxing authority.",
        ),
    ]


# Enum definitions
class DeemedResellerCategoryEnum(str, Enum):
    """Enum for DeemedResellerCategory"""

    IOSS = "IOSS"  # Import one stop shop. The item being purchased is not held in the EU for shipment.
    UOSS = "UOSS"  # Union one stop shop. The item being purchased is held in the EU for shipment.


"""
OrderItem

A single order item.
"""


class OrderItem(SpApiBaseModel):
    """A single order item."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    a_s_i_n: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("ASIN", "a_s_i_n"),
            serialization_alias="ASIN",
            description="The item's Amazon Standard Identification Number (ASIN).",
        ),
    ]

    seller_s_k_u: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("SellerSKU", "seller_s_k_u"),
            serialization_alias="SellerSKU",
            description="The item's seller stock keeping unit (SKU).",
        ),
    ]

    order_item_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("OrderItemId", "order_item_id"),
            serialization_alias="OrderItemId",
            description="An Amazon-defined order item identifier.",
        ),
    ]

    associated_items: Annotated[
        Optional[List["AssociatedItem"]],
        Field(
            None,
            validation_alias=AliasChoices("AssociatedItems", "associated_items"),
            serialization_alias="AssociatedItems",
            description="A list of associated items that a customer has purchased with a product. For example, a tire installation service purchased with tires.",
        ),
    ]

    title: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("Title", "title"),
            serialization_alias="Title",
            description="The item's name.",
        ),
    ]

    quantity_ordered: Annotated[
        int,
        Field(
            ...,
            validation_alias=AliasChoices("QuantityOrdered", "quantity_ordered"),
            serialization_alias="QuantityOrdered",
            description="The number of items in the order. ",
        ),
    ]

    quantity_shipped: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices("QuantityShipped", "quantity_shipped"),
            serialization_alias="QuantityShipped",
            description="The number of items shipped.",
        ),
    ]

    product_info: Annotated[
        Optional["ProductInfoDetail"],
        Field(
            None,
            validation_alias=AliasChoices("ProductInfo", "product_info"),
            serialization_alias="ProductInfo",
            description="The item's product information.",
        ),
    ]

    points_granted: Annotated[
        Optional["PointsGrantedDetail"],
        Field(
            None,
            validation_alias=AliasChoices("PointsGranted", "points_granted"),
            serialization_alias="PointsGranted",
            description="The number and value of Amazon Points granted with the purchase of an item.",
        ),
    ]

    item_price: Annotated[
        Optional["Money"],
        Field(
            None,
            validation_alias=AliasChoices("ItemPrice", "item_price"),
            serialization_alias="ItemPrice",
            description="The selling price of the order item. Note that an order item is an item and a quantity. This means that the value of `ItemPrice` is equal to the selling price of the item multiplied by the quantity ordered. `ItemPrice` excludes `ShippingPrice` and GiftWrapPrice.",
        ),
    ]

    shipping_price: Annotated[
        Optional["Money"],
        Field(
            None,
            validation_alias=AliasChoices("ShippingPrice", "shipping_price"),
            serialization_alias="ShippingPrice",
            description="The item's shipping price.",
        ),
    ]

    item_tax: Annotated[
        Optional["Money"],
        Field(
            None,
            validation_alias=AliasChoices("ItemTax", "item_tax"),
            serialization_alias="ItemTax",
            description="The tax on the item price.",
        ),
    ]

    shipping_tax: Annotated[
        Optional["Money"],
        Field(
            None,
            validation_alias=AliasChoices("ShippingTax", "shipping_tax"),
            serialization_alias="ShippingTax",
            description="The tax on the shipping price.",
        ),
    ]

    shipping_discount: Annotated[
        Optional["Money"],
        Field(
            None,
            validation_alias=AliasChoices("ShippingDiscount", "shipping_discount"),
            serialization_alias="ShippingDiscount",
            description="The discount on the shipping price.",
        ),
    ]

    shipping_discount_tax: Annotated[
        Optional["Money"],
        Field(
            None,
            validation_alias=AliasChoices(
                "ShippingDiscountTax", "shipping_discount_tax"
            ),
            serialization_alias="ShippingDiscountTax",
            description="The tax on the discount on the shipping price.",
        ),
    ]

    promotion_discount: Annotated[
        Optional["Money"],
        Field(
            None,
            validation_alias=AliasChoices("PromotionDiscount", "promotion_discount"),
            serialization_alias="PromotionDiscount",
            description="The total of all promotional discounts in the offer.",
        ),
    ]

    promotion_discount_tax: Annotated[
        Optional["Money"],
        Field(
            None,
            validation_alias=AliasChoices(
                "PromotionDiscountTax", "promotion_discount_tax"
            ),
            serialization_alias="PromotionDiscountTax",
            description="The tax on the total of all promotional discounts in the offer.",
        ),
    ]

    promotion_ids: Annotated[
        Optional["PromotionIdList"],
        Field(
            None,
            validation_alias=AliasChoices("PromotionIds", "promotion_ids"),
            serialization_alias="PromotionIds",
        ),
    ]

    c_o_d_fee: Annotated[
        Optional["Money"],
        Field(
            None,
            validation_alias=AliasChoices("CODFee", "c_o_d_fee"),
            serialization_alias="CODFee",
            description="The fee charged for COD service.",
        ),
    ]

    c_o_d_fee_discount: Annotated[
        Optional["Money"],
        Field(
            None,
            validation_alias=AliasChoices("CODFeeDiscount", "c_o_d_fee_discount"),
            serialization_alias="CODFeeDiscount",
            description="The discount on the COD fee.",
        ),
    ]

    is_gift: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("IsGift", "is_gift"),
            serialization_alias="IsGift",
            description="Indicates whether the item is a gift. **Possible values**: `true` and `false`.",
        ),
    ]

    condition_note: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("ConditionNote", "condition_note"),
            serialization_alias="ConditionNote",
            description="The condition of the item, as described by the seller.",
        ),
    ]

    condition_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("ConditionId", "condition_id"),
            serialization_alias="ConditionId",
            description="The condition of the item. **Possible values**: `New`, `Used`, `Collectible`, `Refurbished`, `Preorder`, and `Club`.",
        ),
    ]

    condition_subtype_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("ConditionSubtypeId", "condition_subtype_id"),
            serialization_alias="ConditionSubtypeId",
            description="The subcondition of the item. **Possible values**: `New`, `Mint`, `Very Good`, `Good`, `Acceptable`, `Poor`, `Club`, `OEM`, `Warranty`, `Refurbished Warranty`, `Refurbished`, `Open Box`, `Any`, and `Other`.",
        ),
    ]

    scheduled_delivery_start_date: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "ScheduledDeliveryStartDate", "scheduled_delivery_start_date"
            ),
            serialization_alias="ScheduledDeliveryStartDate",
            description="The start date of the scheduled delivery window in the time zone for the order destination. In [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date time format.",
        ),
    ]

    scheduled_delivery_end_date: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "ScheduledDeliveryEndDate", "scheduled_delivery_end_date"
            ),
            serialization_alias="ScheduledDeliveryEndDate",
            description="The end date of the scheduled delivery window in the time zone for the order destination. In [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date time format.",
        ),
    ]

    price_designation: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("PriceDesignation", "price_designation"),
            serialization_alias="PriceDesignation",
            description="Indicates that the selling price is a special price that is only available for Amazon Business orders. For more information about the Amazon Business Seller Program, refer to the [Amazon Business website](https://www.amazon.com/b2b/info/amazon-business). **Possible values**: `BusinessPrice`",
        ),
    ]

    tax_collection: Annotated[
        Optional["TaxCollection"],
        Field(
            None,
            validation_alias=AliasChoices("TaxCollection", "tax_collection"),
            serialization_alias="TaxCollection",
            description="Information about withheld taxes.",
        ),
    ]

    serial_number_required: Annotated[
        Optional[bool],
        Field(
            None,
            validation_alias=AliasChoices(
                "SerialNumberRequired", "serial_number_required"
            ),
            serialization_alias="SerialNumberRequired",
            description="When true, the product type for this item has a serial number. Only returned for Amazon Easy Ship orders.",
        ),
    ]

    is_transparency: Annotated[
        Optional[bool],
        Field(
            None,
            validation_alias=AliasChoices("IsTransparency", "is_transparency"),
            serialization_alias="IsTransparency",
            description="When true, the ASIN is enrolled in Transparency. The Transparency serial number that you must submit is determined by: **1D or 2D Barcode:** This has a **T** logo. Submit either the 29-character alpha-numeric identifier beginning with **AZ** or **ZA**, or the 38-character Serialized Global Trade Item Number (SGTIN). **2D Barcode SN:** Submit the 7- to 20-character serial number barcode, which likely has the prefix **SN**. The serial number is applied to the same side of the packaging as the GTIN (UPC/EAN/ISBN) barcode. **QR code SN:** Submit the URL that the QR code generates.",
        ),
    ]

    ioss_number: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("IossNumber", "ioss_number"),
            serialization_alias="IossNumber",
            description="The IOSS number of the marketplace. Sellers shipping to the EU from outside the EU must provide this IOSS number to their carrier when Amazon has collected the VAT on the sale.",
        ),
    ]

    store_chain_store_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("StoreChainStoreId", "store_chain_store_id"),
            serialization_alias="StoreChainStoreId",
            description="The store chain store identifier. Linked to a specific store in a store chain.",
        ),
    ]

    deemed_reseller_category: Annotated[
        Optional[DeemedResellerCategoryEnum],
        Field(
            None,
            validation_alias=AliasChoices(
                "DeemedResellerCategory", "deemed_reseller_category"
            ),
            serialization_alias="DeemedResellerCategory",
            description="The category of deemed reseller. This applies to selling partners that are not based in the EU and is used to help them meet the VAT Deemed Reseller tax laws in the EU and UK.",
        ),
    ]

    buyer_info: Annotated[
        Optional["ItemBuyerInfo"],
        Field(
            None,
            validation_alias=AliasChoices("BuyerInfo", "buyer_info"),
            serialization_alias="BuyerInfo",
            description="A single item's buyer information. **Note**: The `BuyerInfo` contains restricted data. Use the Restricted Data Token (RDT) and restricted SPDS roles to access the restricted data in `BuyerInfo`. For example, `BuyerCustomizedInfo` and `GiftMessageText`.",
        ),
    ]

    buyer_requested_cancel: Annotated[
        Optional["BuyerRequestedCancel"],
        Field(
            None,
            validation_alias=AliasChoices(
                "BuyerRequestedCancel", "buyer_requested_cancel"
            ),
            serialization_alias="BuyerRequestedCancel",
            description="Information about whether or not a buyer requested cancellation.",
        ),
    ]

    serial_numbers: Annotated[
        Optional[List["str"]],
        Field(
            None,
            validation_alias=AliasChoices("SerialNumbers", "serial_numbers"),
            serialization_alias="SerialNumbers",
            description="A list of serial numbers for electronic products that are shipped to customers. Returned for FBA orders only.",
        ),
    ]

    substitution_preferences: Annotated[
        Optional["SubstitutionPreferences"],
        Field(
            None,
            validation_alias=AliasChoices(
                "SubstitutionPreferences", "substitution_preferences"
            ),
            serialization_alias="SubstitutionPreferences",
            description="Substitution preferences for the order item. This is an optional field that is only present if a seller supports substitutions, as is the case with some grocery sellers.",
        ),
    ]

    measurement: Annotated[
        Optional["Measurement"],
        Field(
            None,
            validation_alias=AliasChoices("Measurement", "measurement"),
            serialization_alias="Measurement",
            description="Measurement information for the order item.",
        ),
    ]

    shipping_constraints: Annotated[
        Optional["ShippingConstraints"],
        Field(
            None,
            validation_alias=AliasChoices(
                "ShippingConstraints", "shipping_constraints"
            ),
            serialization_alias="ShippingConstraints",
            description="Shipping constraints applicable to this order.",
        ),
    ]

    amazon_programs: Annotated[
        Optional["AmazonPrograms"],
        Field(
            None,
            validation_alias=AliasChoices("AmazonPrograms", "amazon_programs"),
            serialization_alias="AmazonPrograms",
            description="Contains the list of programs that are associated with an item.",
        ),
    ]

    export_info: Annotated[
        Optional["ExportInfo"],
        Field(
            None,
            validation_alias=AliasChoices("ExportInfo", "export_info"),
            serialization_alias="ExportInfo",
            description="Contains information that is related to the export of an order item.",
        ),
    ]


"""
OrderItemBuyerInfo

A single order item's buyer information.
"""


class OrderItemBuyerInfo(SpApiBaseModel):
    """A single order item's buyer information."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    order_item_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("OrderItemId", "order_item_id"),
            serialization_alias="OrderItemId",
            description="An Amazon-defined order item identifier.",
        ),
    ]

    buyer_customized_info: Annotated[
        Optional["BuyerCustomizedInfoDetail"],
        Field(
            None,
            validation_alias=AliasChoices(
                "BuyerCustomizedInfo", "buyer_customized_info"
            ),
            serialization_alias="BuyerCustomizedInfo",
            description="Buyer information for custom orders from the Amazon Custom program. **Note**: This attribute is only available for MFN (fulfilled by seller) orders.",
        ),
    ]

    gift_wrap_price: Annotated[
        Optional["Money"],
        Field(
            None,
            validation_alias=AliasChoices("GiftWrapPrice", "gift_wrap_price"),
            serialization_alias="GiftWrapPrice",
            description="The gift wrap price of the item.",
        ),
    ]

    gift_wrap_tax: Annotated[
        Optional["Money"],
        Field(
            None,
            validation_alias=AliasChoices("GiftWrapTax", "gift_wrap_tax"),
            serialization_alias="GiftWrapTax",
            description="The tax on the gift wrap price.",
        ),
    ]

    gift_message_text: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("GiftMessageText", "gift_message_text"),
            serialization_alias="GiftMessageText",
            description="A gift message provided by the buyer. **Note**: This attribute is only available for MFN (fulfilled by seller) orders.",
        ),
    ]

    gift_wrap_level: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("GiftWrapLevel", "gift_wrap_level"),
            serialization_alias="GiftWrapLevel",
            description="The gift wrap level specified by the buyer.",
        ),
    ]


"""
OrderItems

For partial shipment status updates, the list of order items and quantities to be updated.
"""


class OrderItems(SpApiBaseModel):
    """For partial shipment status updates, the list of order items and quantities to be updated."""

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow",
        serialize_by_alias=True,
        arbitrary_types_allowed=True,
    )


"""
PaymentExecutionDetailItem

Information about a sub-payment method used to pay for a COD order.
"""


class PaymentExecutionDetailItem(SpApiBaseModel):
    """Information about a sub-payment method used to pay for a COD order."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payment: Annotated[
        "Money",
        Field(
            ...,
            validation_alias=AliasChoices("Payment", "payment"),
            serialization_alias="Payment",
        ),
    ]

    payment_method: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("PaymentMethod", "payment_method"),
            serialization_alias="PaymentMethod",
            description="A sub-payment method for a COD order. **Possible values**: * `COD`: Cash on delivery * `GC`: Gift card * `PointsAccount`: Amazon Points * `Invoice`: Invoice",
        ),
    ]


"""
PrescriptionDetail

Information about the prescription that is used to verify a regulated product. This must be provided once per order and reflect the seller’s own records. Only approved orders can have prescriptions.
"""


class PrescriptionDetail(SpApiBaseModel):
    """Information about the prescription that is used to verify a regulated product. This must be provided once per order and reflect the seller’s own records. Only approved orders can have prescriptions."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    prescription_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("prescriptionId", "prescription_id"),
            serialization_alias="prescriptionId",
            description="The identifier for the prescription used to verify the regulated product.",
        ),
    ]

    expiration_date: Annotated[
        datetime,
        Field(
            ...,
            validation_alias=AliasChoices("expirationDate", "expiration_date"),
            serialization_alias="expirationDate",
            description="The expiration date of the prescription used to verify the regulated product, in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date time format.",
        ),
    ]

    written_quantity: Annotated[
        int,
        Field(
            ...,
            validation_alias=AliasChoices("writtenQuantity", "written_quantity"),
            serialization_alias="writtenQuantity",
            description="The number of units in each fill as provided in the prescription.",
        ),
    ]

    total_refills_authorized: Annotated[
        int,
        Field(
            ...,
            validation_alias=AliasChoices(
                "totalRefillsAuthorized", "total_refills_authorized"
            ),
            serialization_alias="totalRefillsAuthorized",
            description="The total number of refills written in the original prescription used to verify the regulated product. If a prescription originally had no refills, this value must be 0.",
        ),
    ]

    refills_remaining: Annotated[
        int,
        Field(
            ...,
            validation_alias=AliasChoices("refillsRemaining", "refills_remaining"),
            serialization_alias="refillsRemaining",
            description="The number of refills remaining for the prescription used to verify the regulated product. If a prescription originally had 10 total refills, this value must be `10` for the first order, `9` for the second order, and `0` for the eleventh order. If a prescription originally had no refills, this value must be 0.",
        ),
    ]

    clinic_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("clinicId", "clinic_id"),
            serialization_alias="clinicId",
            description="The identifier for the clinic which provided the prescription used to verify the regulated product.",
        ),
    ]

    usage_instructions: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("usageInstructions", "usage_instructions"),
            serialization_alias="usageInstructions",
            description="The instructions for the prescription as provided by the approver of the regulated product.",
        ),
    ]


ShipmentStatus = str
"""The shipment status to apply."""


"""
SubstitutionOption

Substitution options for an order item.
"""


class SubstitutionOption(SpApiBaseModel):
    """Substitution options for an order item."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    a_s_i_n: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("ASIN", "a_s_i_n"),
            serialization_alias="ASIN",
            description="The item's Amazon Standard Identification Number (ASIN).",
        ),
    ]

    quantity_ordered: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices("QuantityOrdered", "quantity_ordered"),
            serialization_alias="QuantityOrdered",
            description="The number of items to be picked for this substitution option. ",
        ),
    ]

    seller_s_k_u: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("SellerSKU", "seller_s_k_u"),
            serialization_alias="SellerSKU",
            description="The item's seller stock keeping unit (SKU).",
        ),
    ]

    title: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("Title", "title"),
            serialization_alias="Title",
            description="The item's title.",
        ),
    ]

    measurement: Annotated[
        Optional["Measurement"],
        Field(
            None,
            validation_alias=AliasChoices("Measurement", "measurement"),
            serialization_alias="Measurement",
            description="Measurement information for the substitution option.",
        ),
    ]


TransparencyCode = str
"""The transparency code associated with the item."""


"""
UpdateShipmentStatusErrorResponse

The error response schema for the `UpdateShipmentStatus` operation.
"""


class UpdateShipmentStatusErrorResponse(SpApiBaseModel):
    """The error response schema for the `UpdateShipmentStatus` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
            description="One or more unexpected errors occurred during the `UpdateShipmentStatus` operation.",
        ),
    ]


"""
UpdateShipmentStatusRequestBody

The request body for the `updateShipmentStatus` operation.
"""


class UpdateShipmentStatusRequestBody(SpApiBaseModel):
    """The request body for the `updateShipmentStatus` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    marketplace_id: Annotated[
        Optional["MarketplaceId"],
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
        ),
    ]

    shipment_status: Annotated[
        "ShipmentStatus",
        Field(
            ...,
            validation_alias=AliasChoices("shipmentStatus", "shipment_status"),
            serialization_alias="shipmentStatus",
        ),
    ]

    order_items: Annotated[
        Optional["OrderItems"],
        Field(
            None,
            validation_alias=AliasChoices("orderItems", "order_items"),
            serialization_alias="orderItems",
        ),
    ]


"""
UpdateShipmentStatusRequest

Request parameters for updateShipmentStatus
"""


class UpdateShipmentStatusRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for updateShipmentStatus
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
            description="[PATH] An Amazon-defined order identifier, in 3-7-7 format.",
        ),
    ]

    payload: Annotated[
        "UpdateShipmentStatusRequestBody",
        BodyParam(),
        Field(
            ...,
            description="[BODY] The request body for the `updateShipmentStatus` operation.",
        ),
    ]


"""
UpdateVerificationStatusErrorResponse

The error response schema for the `UpdateVerificationStatus` operation.
"""


class UpdateVerificationStatusErrorResponse(SpApiBaseModel):
    """The error response schema for the `UpdateVerificationStatus` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
            description="One or more unexpected errors occurred during the `UpdateVerificationStatus` operation.",
        ),
    ]


"""
VerificationDetails

Additional information related to the verification of a regulated order.
"""


class VerificationDetails(SpApiBaseModel):
    """Additional information related to the verification of a regulated order."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    prescription_detail: Annotated[
        Optional["PrescriptionDetail"],
        Field(
            None,
            validation_alias=AliasChoices("prescriptionDetail", "prescription_detail"),
            serialization_alias="prescriptionDetail",
            description="Information regarding the prescription tied to the order.",
        ),
    ]


"""
UpdateVerificationStatusRequestBody

The updated values of the `VerificationStatus` field.
"""


class UpdateVerificationStatusRequestBody(SpApiBaseModel):
    """The updated values of the `VerificationStatus` field."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    status: Annotated[
        Optional["VerificationStatus"],
        Field(None, description="The new verification status of the order."),
    ]

    external_reviewer_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("externalReviewerId", "external_reviewer_id"),
            serialization_alias="externalReviewerId",
            description="The identifier of the order's regulated information reviewer.",
        ),
    ]

    rejection_reason_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("rejectionReasonId", "rejection_reason_id"),
            serialization_alias="rejectionReasonId",
            description="The unique identifier of the rejection reason used for rejecting the order's regulated information. Only required if the new status is rejected.",
        ),
    ]

    verification_details: Annotated[
        Optional["VerificationDetails"],
        Field(
            None,
            validation_alias=AliasChoices(
                "verificationDetails", "verification_details"
            ),
            serialization_alias="verificationDetails",
            description="Additional information regarding the verification of the order.",
        ),
    ]


"""
UpdateVerificationStatusRequest

Request parameters for updateVerificationStatus
"""


class UpdateVerificationStatusRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for updateVerificationStatus
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
            description="[PATH] An Amazon-defined order identifier, in 3-7-7 format.",
        ),
    ]

    payload: Annotated[
        "UpdateVerificationStatusRequestBody",
        BodyParam(),
        Field(
            ...,
            description="[BODY] The request body for the `updateVerificationStatus` operation.",
        ),
    ]


# Rebuild models to resolve forward references
UpdateShipmentStatusRequestBody.model_rebuild()
UpdateVerificationStatusRequestBody.model_rebuild()
OrderItems.model_rebuild()
UpdateShipmentStatusErrorResponse.model_rebuild()
UpdateVerificationStatusErrorResponse.model_rebuild()
GetOrdersResponse.model_rebuild()
GetOrderResponse.model_rebuild()
GetOrderBuyerInfoResponse.model_rebuild()
GetOrderRegulatedInfoResponse.model_rebuild()
GetOrderAddressResponse.model_rebuild()
GetOrderItemsResponse.model_rebuild()
GetOrderItemsBuyerInfoResponse.model_rebuild()
OrdersList.model_rebuild()
Order.model_rebuild()
OrderBuyerInfo.model_rebuild()
OrderRegulatedInfo.model_rebuild()
RegulatedOrderVerificationStatus.model_rebuild()
RejectionReason.model_rebuild()
PrescriptionDetail.model_rebuild()
ValidVerificationDetail.model_rebuild()
VerificationDetails.model_rebuild()
RegulatedInformation.model_rebuild()
RegulatedInformationField.model_rebuild()
OrderAddress.model_rebuild()
Address.model_rebuild()
AddressExtendedFields.model_rebuild()
DeliveryPreferences.model_rebuild()
PreferredDeliveryTime.model_rebuild()
BusinessHours.model_rebuild()
ExceptionDates.model_rebuild()
OpenInterval.model_rebuild()
OpenTimeInterval.model_rebuild()
Money.model_rebuild()
PaymentMethodDetailItemList.model_rebuild()
PaymentExecutionDetailItem.model_rebuild()
BuyerTaxInfo.model_rebuild()
MarketplaceTaxInfo.model_rebuild()
TaxClassification.model_rebuild()
OrderItemsList.model_rebuild()
OrderItem.model_rebuild()
ExportInfo.model_rebuild()
AmazonPrograms.model_rebuild()
SubstitutionPreferences.model_rebuild()
SubstitutionOption.model_rebuild()
Measurement.model_rebuild()
AssociatedItem.model_rebuild()
OrderItemsBuyerInfoList.model_rebuild()
OrderItemBuyerInfo.model_rebuild()
PointsGrantedDetail.model_rebuild()
ProductInfoDetail.model_rebuild()
PromotionIdList.model_rebuild()
BuyerCustomizedInfoDetail.model_rebuild()
TaxCollection.model_rebuild()
BuyerTaxInformation.model_rebuild()
FulfillmentInstruction.model_rebuild()
ShippingConstraints.model_rebuild()
BuyerInfo.model_rebuild()
ItemBuyerInfo.model_rebuild()
AutomatedShippingSettings.model_rebuild()
BuyerRequestedCancel.model_rebuild()
ConfirmShipmentRequestBody.model_rebuild()
ConfirmShipmentErrorResponse.model_rebuild()
PackageDetail.model_rebuild()
ConfirmShipmentOrderItem.model_rebuild()
Error.model_rebuild()
GetOrdersRequest.model_rebuild()
GetOrderRequest.model_rebuild()
GetOrderBuyerInfoRequest.model_rebuild()
GetOrderAddressRequest.model_rebuild()
GetOrderItemsRequest.model_rebuild()
GetOrderItemsBuyerInfoRequest.model_rebuild()
UpdateShipmentStatusRequest.model_rebuild()
GetOrderRegulatedInfoRequest.model_rebuild()
UpdateVerificationStatusRequest.model_rebuild()
ConfirmShipmentRequest.model_rebuild()
