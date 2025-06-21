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

AdditionalLocationInfo = str
"""Additional location information."""


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

    city: Annotated[
        Optional[str],
        Field(
            None,
            description="The city where the person, business, or institution is located. This property is required in all countries except Japan. It should not be used in Japan.",
        ),
    ]

    district_or_county: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("districtOrCounty", "district_or_county"),
            serialization_alias="districtOrCounty",
            description="The district or county where the person, business, or institution is located.",
        ),
    ]

    state_or_region: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("stateOrRegion", "state_or_region"),
            serialization_alias="stateOrRegion",
            description="The state or region where the person, business or institution is located.",
        ),
    ]

    postal_code: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("postalCode", "postal_code"),
            serialization_alias="postalCode",
            description="The postal code of the address.",
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
            description="The phone number of the person, business, or institution located at the address.",
        ),
    ]


Decimal = str
"""A decimal number with no loss of precision. Useful when precision loss is unacceptable, as with currencies. Follows RFC7159 for number representation."""


# Enum definitions
class UnitOfMeasureEnum(str, Enum):
    """Enum for unitOfMeasure"""

    EACHES = "Eaches"  # Specifies an integer count of units.


"""
Amount

A quantity based on unit of measure.
"""


class Amount(SpApiBaseModel):
    """A quantity based on unit of measure."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    unit_of_measure: Annotated[
        UnitOfMeasureEnum,
        Field(
            ...,
            validation_alias=AliasChoices("unitOfMeasure", "unit_of_measure"),
            serialization_alias="unitOfMeasure",
            description="The unit of measure for the amount.",
        ),
    ]

    value: Annotated[
        "Decimal",
        Field(
            ...,
            description="The amount of a product in the associated unit of measure.",
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
        str,
        Field(
            ...,
            validation_alias=AliasChoices("currencyCode", "currency_code"),
            serialization_alias="currencyCode",
            description="Three digit currency code in ISO 4217 format.",
        ),
    ]

    value: Annotated[
        "Decimal",
        Field(
            ...,
        ),
    ]


"""
CODSettings

The COD (Cash On Delivery) charges that you associate with a COD fulfillment order.
"""


class CODSettings(SpApiBaseModel):
    """The COD (Cash On Delivery) charges that you associate with a COD fulfillment order."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    is_cod_required: Annotated[
        bool,
        Field(
            ...,
            validation_alias=AliasChoices("isCodRequired", "is_cod_required"),
            serialization_alias="isCodRequired",
            description="When true, this fulfillment order requires a COD (Cash On Delivery) payment.",
        ),
    ]

    cod_charge: Annotated[
        Optional["Money"],
        Field(
            None,
            validation_alias=AliasChoices("codCharge", "cod_charge"),
            serialization_alias="codCharge",
            description="The amount of the COD charge to be collected from the recipient for a COD order.",
        ),
    ]

    cod_charge_tax: Annotated[
        Optional["Money"],
        Field(
            None,
            validation_alias=AliasChoices("codChargeTax", "cod_charge_tax"),
            serialization_alias="codChargeTax",
            description="The amount of the tax on the COD charge to be collected from the recipient for a COD order.",
        ),
    ]

    shipping_charge: Annotated[
        Optional["Money"],
        Field(
            None,
            validation_alias=AliasChoices("shippingCharge", "shipping_charge"),
            serialization_alias="shippingCharge",
            description="The amount of the tax on the COD charge to be collected from the recipient for a COD order.",
        ),
    ]

    shipping_charge_tax: Annotated[
        Optional["Money"],
        Field(
            None,
            validation_alias=AliasChoices("shippingChargeTax", "shipping_charge_tax"),
            serialization_alias="shippingChargeTax",
            description="The amount of the tax on the shipping charge to be collected from the recipient for a COD order.",
        ),
    ]


"""
CancelFulfillmentOrderRequest

Request parameters for cancelFulfillmentOrder
"""


class CancelFulfillmentOrderRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for cancelFulfillmentOrder
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    seller_fulfillment_order_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices(
                "sellerFulfillmentOrderId", "seller_fulfillment_order_id"
            ),
            serialization_alias="sellerFulfillmentOrderId",
            description="[PATH] The identifier assigned to the item by the seller when the fulfillment order was created.",
        ),
    ]


ErrorList = List["Error"]
"""A list of error responses returned when a request is unsuccessful."""


"""
CancelFulfillmentOrderResponse

The response schema for the `cancelFulfillmentOrder` operation.
"""


class CancelFulfillmentOrderResponse(SpApiBaseModel):
    """The response schema for the `cancelFulfillmentOrder` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
            description="One or more unexpected errors occurred during the `cancelFulfillmentOrder` operation.",
        ),
    ]


Quantity = int
"""The item quantity."""


"""
CreateFulfillmentOrderItem

Item information for creating a fulfillment order.
"""


class CreateFulfillmentOrderItem(SpApiBaseModel):
    """Item information for creating a fulfillment order."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    seller_sku: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("sellerSku", "seller_sku"),
            serialization_alias="sellerSku",
            description="The seller SKU of the item.",
        ),
    ]

    seller_fulfillment_order_item_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices(
                "sellerFulfillmentOrderItemId", "seller_fulfillment_order_item_id"
            ),
            serialization_alias="sellerFulfillmentOrderItemId",
            description="A fulfillment order item identifier that the seller creates to track fulfillment order items. Used to disambiguate multiple fulfillment items that have the same `SellerSKU`. For example, the seller might assign different `SellerFulfillmentOrderItemId` values to two items in a fulfillment order that share the same `SellerSKU` but have different `GiftMessage` values.",
        ),
    ]

    quantity: Annotated[
        "Quantity",
        Field(
            ...,
        ),
    ]

    gift_message: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("giftMessage", "gift_message"),
            serialization_alias="giftMessage",
            description="A message to the gift recipient, if applicable.",
        ),
    ]

    displayable_comment: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("displayableComment", "displayable_comment"),
            serialization_alias="displayableComment",
            description="Item-specific text that displays in recipient-facing materials such as the outbound shipment packing slip.",
        ),
    ]

    fulfillment_network_sku: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "fulfillmentNetworkSku", "fulfillment_network_sku"
            ),
            serialization_alias="fulfillmentNetworkSku",
            description="Amazon's fulfillment network SKU of the item.",
        ),
    ]

    per_unit_declared_value: Annotated[
        Optional["Money"],
        Field(
            None,
            validation_alias=AliasChoices(
                "perUnitDeclaredValue", "per_unit_declared_value"
            ),
            serialization_alias="perUnitDeclaredValue",
            description="The monetary value assigned by the seller to this item. This is a required field for India MCF orders.",
        ),
    ]

    per_unit_price: Annotated[
        Optional["Money"],
        Field(
            None,
            validation_alias=AliasChoices("perUnitPrice", "per_unit_price"),
            serialization_alias="perUnitPrice",
            description="The amount to be collected from the recipient for this item in a COD (Cash On Delivery) order.",
        ),
    ]

    per_unit_tax: Annotated[
        Optional["Money"],
        Field(
            None,
            validation_alias=AliasChoices("perUnitTax", "per_unit_tax"),
            serialization_alias="perUnitTax",
            description="The tax on the amount to be collected from the recipient for this item in a COD (Cash On Delivery) order.",
        ),
    ]


CreateFulfillmentOrderItemList = List["CreateFulfillmentOrderItem"]
"""An array of item information for creating a fulfillment order."""


# Enum definitions
class TypeEnum(str, Enum):
    """Enum for type"""

    FRONT_DOOR = "FRONT_DOOR"  # Indicates delivery preferred to front door.
    DELIVERY_BOX = "DELIVERY_BOX"  # Indicates delivery preferred to a delivery box.
    GAS_METER_BOX = "GAS_METER_BOX"  # Indicates delivery preferred to a gas meter box.
    BICYCLE_BASKET = (
        "BICYCLE_BASKET"  # Indicates delivery preferred to a bicycle basket.
    )
    GARAGE = "GARAGE"  # Indicates delivery preferred to a garage.
    RECEPTIONIST = "RECEPTIONIST"  # Indicates delivery preferred with a receptionist.
    FALLBACK_NEIGHBOR_DELIVERY = "FALLBACK_NEIGHBOR_DELIVERY"  # Indicates delivery preferred with a designated neighbor if the recipient is not available at the destination address.
    DO_NOT_LEAVE_UNATTENDED = (
        "DO_NOT_LEAVE_UNATTENDED"  # Indicates delivery preferred as attended.
    )


"""
DropOffLocation

The preferred location to leave packages at the destination address.
"""


class DropOffLocation(SpApiBaseModel):
    """The preferred location to leave packages at the destination address."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    type: Annotated[
        TypeEnum,
        Field(
            ...,
            description="Specifies the preferred location to leave the package at the destination address.",
        ),
    ]

    attributes: Annotated[
        Optional[Dict[str, Any]],
        Field(
            None,
            description="Additional information about the drop-off location that can vary depending on the type of drop-off location specified in the `type` field. If the `type` is set to `FALLBACK_NEIGHBOR_DELIVERY`, the `attributes` object should include the exact keys `neighborName` and `houseNumber` to provide the name and house number of the designated neighbor.",
        ),
    ]


"""
DeliveryPreferences

The delivery preferences applied to the destination address. These preferences are applied when possible and are best effort. This feature is currently supported only in the JP marketplace and not applicable for other marketplaces. For eligible orders, the default delivery preference will be to deliver the package unattended at the front door, unless you specify otherwise.
"""


class DeliveryPreferences(SpApiBaseModel):
    """The delivery preferences applied to the destination address. These preferences are applied when possible and are best effort. This feature is currently supported only in the JP marketplace and not applicable for other marketplaces. For eligible orders, the default delivery preference will be to deliver the package unattended at the front door, unless you specify otherwise."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    delivery_instructions: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "deliveryInstructions", "delivery_instructions"
            ),
            serialization_alias="deliveryInstructions",
            description="Additional delivery instructions. For example, this could be instructions on how to enter a building, nearby landmark or navigation instructions, 'Beware of dogs', etc.",
        ),
    ]

    drop_off_location: Annotated[
        Optional["DropOffLocation"],
        Field(
            None,
            validation_alias=AliasChoices("dropOffLocation", "drop_off_location"),
            serialization_alias="dropOffLocation",
            description="The preferred location to leave packages at the destination address.",
        ),
    ]


Timestamp = str
"""Date timestamp"""


"""
DeliveryWindow

The time range within which a Scheduled Delivery fulfillment order should be delivered. This is only available in the JP marketplace.
"""


class DeliveryWindow(SpApiBaseModel):
    """The time range within which a Scheduled Delivery fulfillment order should be delivered. This is only available in the JP marketplace."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    start_date: Annotated[
        "Timestamp",
        Field(
            ...,
            validation_alias=AliasChoices("startDate", "start_date"),
            serialization_alias="startDate",
            description="The date and time of the start of the Scheduled Delivery window. Must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format.",
        ),
    ]

    end_date: Annotated[
        "Timestamp",
        Field(
            ...,
            validation_alias=AliasChoices("endDate", "end_date"),
            serialization_alias="endDate",
            description="The date and time of the end of the Scheduled Delivery window. Must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format.",
        ),
    ]


# Enum definitions
class FeatureFulfillmentPolicyEnum(str, Enum):
    """Enum for featureFulfillmentPolicy"""

    REQUIRED = "Required"  # If the offer can't be shipped with the selected feature, reject the order.
    NOT_REQUIRED = "NotRequired"  # The feature is not required for shipping.


"""
FeatureSettings

`FeatureSettings` allows users to apply fulfillment features to an order. To block an order from being shipped using Amazon Logistics (AMZL) and an AMZL tracking number, use `featureName` as `BLOCK_AMZL` and `featureFulfillmentPolicy` as `Required`. Blocking AMZL will incur an additional fee surcharge on your MCF orders and increase the risk of some of your orders being unfulfilled or delivered late if there are no alternative carriers available. Using `BLOCK_AMZL` in an order request will take precedence over your Seller Central account setting. To ship in non-Amazon branded packaging (blank boxes), use featureName `BLANK_BOX`.
"""


class FeatureSettings(SpApiBaseModel):
    """`FeatureSettings` allows users to apply fulfillment features to an order. To block an order from being shipped using Amazon Logistics (AMZL) and an AMZL tracking number, use `featureName` as `BLOCK_AMZL` and `featureFulfillmentPolicy` as `Required`. Blocking AMZL will incur an additional fee surcharge on your MCF orders and increase the risk of some of your orders being unfulfilled or delivered late if there are no alternative carriers available. Using `BLOCK_AMZL` in an order request will take precedence over your Seller Central account setting. To ship in non-Amazon branded packaging (blank boxes), use featureName `BLANK_BOX`."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    feature_name: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("featureName", "feature_name"),
            serialization_alias="featureName",
            description="The name of the feature.",
        ),
    ]

    feature_fulfillment_policy: Annotated[
        Optional[FeatureFulfillmentPolicyEnum],
        Field(
            None,
            validation_alias=AliasChoices(
                "featureFulfillmentPolicy", "feature_fulfillment_policy"
            ),
            serialization_alias="featureFulfillmentPolicy",
            description="Specifies the policy to use when fulfilling an order.",
        ),
    ]


FulfillmentAction = str
"""Specifies whether the fulfillment order should ship now or have an order hold put on it."""


FulfillmentPolicy = str
"""The `FulfillmentPolicy` value specified when you submitted the `createFulfillmentOrder` operation."""


"""
NotificationEmailList

A list of email addresses that the seller provides that are used by Amazon to send ship-complete notifications to recipients on behalf of the seller.
"""


class NotificationEmailList(SpApiBaseModel):
    """A list of email addresses that the seller provides that are used by Amazon to send ship-complete notifications to recipients on behalf of the seller."""

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow",
        serialize_by_alias=True,
        arbitrary_types_allowed=True,
    )


PaymentInformationList = List["PaymentInformation"]
"""An array of various payment attributes related to this fulfillment order."""


ShippingSpeedCategory = str
"""The shipping method used for the fulfillment order. When this value is `ScheduledDelivery`, choose `Ship` for the `fulfillmentAction`. `Hold` is not a valid `fulfillmentAction` value when the `shippingSpeedCategory` value is `ScheduledDelivery`. Note: Shipping method service level agreements vary by marketplace. Sellers should refer to the [Seller Central](https://developer-docs.amazon.com/sp-api/docs/seller-central-urls) website in their marketplace for shipping method service level agreements and fulfillment fees."""


"""
CreateFulfillmentOrderRequestBody

The request body schema for the `createFulfillmentOrder` operation.
"""


class CreateFulfillmentOrderRequestBody(SpApiBaseModel):
    """The request body schema for the `createFulfillmentOrder` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    marketplace_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="The marketplace the fulfillment order is placed against.",
        ),
    ]

    seller_fulfillment_order_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices(
                "sellerFulfillmentOrderId", "seller_fulfillment_order_id"
            ),
            serialization_alias="sellerFulfillmentOrderId",
            description="A fulfillment order identifier that the seller creates to track their fulfillment order. The `SellerFulfillmentOrderId` must be unique for each fulfillment order that a seller creates. If the seller's system already creates unique order identifiers, then these might be good values for them to use.",
        ),
    ]

    displayable_order_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("displayableOrderId", "displayable_order_id"),
            serialization_alias="displayableOrderId",
            description="A fulfillment order identifier that the seller creates. This value displays as the order identifier in recipient-facing materials such as the outbound shipment packing slip. The value of `DisplayableOrderId` should match the order identifier that the seller provides to the recipient. The seller can use the `SellerFulfillmentOrderId` for this value or they can specify an alternate value if they want the recipient to reference an alternate order identifier. The value must be an alpha-numeric or ISO 8859-1 compliant string from one to 40 characters in length. Cannot contain two spaces in a row. Leading and trailing white space is removed.",
        ),
    ]

    displayable_order_date: Annotated[
        "Timestamp",
        Field(
            ...,
            validation_alias=AliasChoices(
                "displayableOrderDate", "displayable_order_date"
            ),
            serialization_alias="displayableOrderDate",
            description="The date and time of the fulfillment order. Displays as the order date in recipient-facing materials such as the outbound shipment packing slip.",
        ),
    ]

    displayable_order_comment: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices(
                "displayableOrderComment", "displayable_order_comment"
            ),
            serialization_alias="displayableOrderComment",
            description="Order-specific text that appears in recipient-facing materials such as the outbound shipment packing slip.",
        ),
    ]

    shipping_speed_category: Annotated[
        "ShippingSpeedCategory",
        Field(
            ...,
            validation_alias=AliasChoices(
                "shippingSpeedCategory", "shipping_speed_category"
            ),
            serialization_alias="shippingSpeedCategory",
            description="The shipping method for the fulfillment order. When this value is `ScheduledDelivery`, choose Ship for the `fulfillmentAction`. Hold is not a valid `fulfillmentAction` value when the `shippingSpeedCategory` value is `ScheduledDelivery`. Note: Shipping method service level agreements vary by marketplace. Sellers can refer to [Seller Central]( https://developer-docs.amazon.com/sp-api/docs/seller-central-urls) for shipping method service-level agreements and multi-channel fulfillment fees.",
        ),
    ]

    delivery_window: Annotated[
        Optional["DeliveryWindow"],
        Field(
            None,
            validation_alias=AliasChoices("deliveryWindow", "delivery_window"),
            serialization_alias="deliveryWindow",
        ),
    ]

    destination_address: Annotated[
        "Address",
        Field(
            ...,
            validation_alias=AliasChoices("destinationAddress", "destination_address"),
            serialization_alias="destinationAddress",
            description="The destination address for the fulfillment order.",
        ),
    ]

    delivery_preferences: Annotated[
        Optional["DeliveryPreferences"],
        Field(
            None,
            validation_alias=AliasChoices(
                "deliveryPreferences", "delivery_preferences"
            ),
            serialization_alias="deliveryPreferences",
            description="The delivery preferences applied to the destination address. These preferences are applied when possible and are best effort. For eligible orders, the default delivery preference is to leave the package unattended at the front door. This feature is currently supported only in the JP marketplace and not applicable for other marketplaces. For eligible orders, the default delivery preference will be to deliver the package unattended at the front door, unless you specify otherwise.",
        ),
    ]

    fulfillment_action: Annotated[
        Optional["FulfillmentAction"],
        Field(
            None,
            validation_alias=AliasChoices("fulfillmentAction", "fulfillment_action"),
            serialization_alias="fulfillmentAction",
        ),
    ]

    fulfillment_policy: Annotated[
        Optional["FulfillmentPolicy"],
        Field(
            None,
            validation_alias=AliasChoices("fulfillmentPolicy", "fulfillment_policy"),
            serialization_alias="fulfillmentPolicy",
        ),
    ]

    cod_settings: Annotated[
        Optional["CODSettings"],
        Field(
            None,
            validation_alias=AliasChoices("codSettings", "cod_settings"),
            serialization_alias="codSettings",
        ),
    ]

    ship_from_country_code: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "shipFromCountryCode", "ship_from_country_code"
            ),
            serialization_alias="shipFromCountryCode",
            description="The two-character country code for the country from which the fulfillment order ships. Must be in ISO 3166-1 alpha-2 format.",
        ),
    ]

    notification_emails: Annotated[
        Optional["NotificationEmailList"],
        Field(
            None,
            validation_alias=AliasChoices("notificationEmails", "notification_emails"),
            serialization_alias="notificationEmails",
        ),
    ]

    feature_constraints: Annotated[
        Optional[List["FeatureSettings"]],
        Field(
            None,
            validation_alias=AliasChoices("featureConstraints", "feature_constraints"),
            serialization_alias="featureConstraints",
            description="A list of features and their fulfillment policies to apply to the order.",
        ),
    ]

    items: Annotated[
        "CreateFulfillmentOrderItemList",
        Field(
            ...,
            description="A list of items to include in the fulfillment order preview, including quantity. Maximum of 100 line items with a maximum of 250 units per order.",
        ),
    ]

    payment_information: Annotated[
        Optional["PaymentInformationList"],
        Field(
            None,
            validation_alias=AliasChoices("paymentInformation", "payment_information"),
            serialization_alias="paymentInformation",
            description="An array of various payment attributes related to this fulfillment order. This property is required if the order is placed against the India marketplace.",
        ),
    ]


"""
CreateFulfillmentOrderRequest

Request parameters for createFulfillmentOrder
"""


class CreateFulfillmentOrderRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for createFulfillmentOrder
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    body: Annotated[
        "CreateFulfillmentOrderRequestBody",
        BodyParam(),
        Field(..., description="[BODY] CreateFulfillmentOrderRequestBody parameter"),
    ]


"""
CreateFulfillmentOrderResponse

The response schema for the `createFulfillmentOrder` operation.
"""


class CreateFulfillmentOrderResponse(SpApiBaseModel):
    """The response schema for the `createFulfillmentOrder` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
            description="One or more unexpected errors occurred during the `createFulfillmentOrder` operation.",
        ),
    ]


CreateReturnItemList = List["CreateReturnItem"]
"""An array of items to be returned."""


"""
CreateFulfillmentReturnRequestBody

The `createFulfillmentReturn` operation creates a fulfillment return for items that were fulfilled using the `createFulfillmentOrder` operation. For calls to `createFulfillmentReturn`, you must include `ReturnReasonCode` values returned by a previous call to the `listReturnReasonCodes` operation.
"""


class CreateFulfillmentReturnRequestBody(SpApiBaseModel):
    """The `createFulfillmentReturn` operation creates a fulfillment return for items that were fulfilled using the `createFulfillmentOrder` operation. For calls to `createFulfillmentReturn`, you must include `ReturnReasonCode` values returned by a previous call to the `listReturnReasonCodes` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    items: Annotated[
        "CreateReturnItemList",
        Field(
            ...,
        ),
    ]


"""
CreateFulfillmentReturnRequest

Request parameters for createFulfillmentReturn
"""


class CreateFulfillmentReturnRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for createFulfillmentReturn
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    body: Annotated[
        "CreateFulfillmentReturnRequestBody",
        BodyParam(),
        Field(..., description="[BODY] CreateFulfillmentReturnRequestBody parameter"),
    ]

    seller_fulfillment_order_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices(
                "sellerFulfillmentOrderId", "seller_fulfillment_order_id"
            ),
            serialization_alias="sellerFulfillmentOrderId",
            description="[PATH] An identifier assigned by the seller to the fulfillment order at the time it was created. The seller uses their own records to find the correct `SellerFulfillmentOrderId` value based on the buyer's request to return items.",
        ),
    ]


InvalidReturnItemList = List["InvalidReturnItem"]
"""An array of invalid return item information."""


ReturnAuthorizationList = List["ReturnAuthorization"]
"""An array of return authorization information."""


ReturnItemList = List["ReturnItem"]
"""An array of items that Amazon accepted for return. Returns empty if no items were accepted for return."""


"""
CreateFulfillmentReturnResult

The result for the createFulfillmentReturn operation.
"""


class CreateFulfillmentReturnResult(SpApiBaseModel):
    """The result for the createFulfillmentReturn operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    return_items: Annotated[
        Optional["ReturnItemList"],
        Field(
            None,
            validation_alias=AliasChoices("returnItems", "return_items"),
            serialization_alias="returnItems",
        ),
    ]

    invalid_return_items: Annotated[
        Optional["InvalidReturnItemList"],
        Field(
            None,
            validation_alias=AliasChoices("invalidReturnItems", "invalid_return_items"),
            serialization_alias="invalidReturnItems",
        ),
    ]

    return_authorizations: Annotated[
        Optional["ReturnAuthorizationList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "returnAuthorizations", "return_authorizations"
            ),
            serialization_alias="returnAuthorizations",
        ),
    ]


"""
CreateFulfillmentReturnResponse

The response schema for the `createFulfillmentReturn` operation.
"""


class CreateFulfillmentReturnResponse(SpApiBaseModel):
    """The response schema for the `createFulfillmentReturn` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["CreateFulfillmentReturnResult"],
        Field(
            None, description="The payload for the `createFulfillmentReturn` operation."
        ),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
            description="One or more unexpected errors occurred during the `createFulfillmentReturn` operation.",
        ),
    ]


"""
CreateReturnItem

An item that Amazon accepted for return.
"""


class CreateReturnItem(SpApiBaseModel):
    """An item that Amazon accepted for return."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    seller_return_item_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices(
                "sellerReturnItemId", "seller_return_item_id"
            ),
            serialization_alias="sellerReturnItemId",
            description="An identifier assigned by the seller to the return item.",
        ),
    ]

    seller_fulfillment_order_item_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices(
                "sellerFulfillmentOrderItemId", "seller_fulfillment_order_item_id"
            ),
            serialization_alias="sellerFulfillmentOrderItemId",
            description="The identifier assigned to the item by the seller when the fulfillment order was created.",
        ),
    ]

    amazon_shipment_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("amazonShipmentId", "amazon_shipment_id"),
            serialization_alias="amazonShipmentId",
            description="The identifier for the shipment that is associated with the return item.",
        ),
    ]

    return_reason_code: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("returnReasonCode", "return_reason_code"),
            serialization_alias="returnReasonCode",
            description="The return reason code assigned to the return item by the seller.",
        ),
    ]

    return_comment: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("returnComment", "return_comment"),
            serialization_alias="returnComment",
            description="An optional comment about the return item.",
        ),
    ]


CurrentStatus = str
"""The current delivery status of the package."""


"""
DateRange

The time range within which something (for example, a delivery) will occur.
"""


class DateRange(SpApiBaseModel):
    """The time range within which something (for example, a delivery) will occur."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    earliest: Annotated[
        "Timestamp", Field(..., description="The earliest point in a date range.")
    ]

    latest: Annotated[
        "Timestamp", Field(..., description="The latest point in a date range.")
    ]


"""
DeliveryDocument

A delivery document for a package.
"""


class DeliveryDocument(SpApiBaseModel):
    """A delivery document for a package."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    document_type: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("documentType", "document_type"),
            serialization_alias="documentType",
            description="The delivery document type. Values are `SIGNATURE` and `DELIVERY_IMAGE`.",
        ),
    ]

    url: Annotated[
        Optional[str],
        Field(
            None,
            description="A URL that you can use to download the document. This URL has a `Content-Type` header. Note that the URL expires after one hour. To get a new URL, you must call the API again.",
        ),
    ]


DeliveryDocumentList = List["DeliveryDocument"]
"""A list of delivery documents for a package."""


"""
DeliveryInformation

The delivery information for the package. This information is available after the package is delivered.
"""


class DeliveryInformation(SpApiBaseModel):
    """The delivery information for the package. This information is available after the package is delivered."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    delivery_document_list: Annotated[
        Optional["DeliveryDocumentList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "deliveryDocumentList", "delivery_document_list"
            ),
            serialization_alias="deliveryDocumentList",
            description="All of the delivery documents for a package.",
        ),
    ]

    drop_off_location: Annotated[
        Optional["DropOffLocation"],
        Field(
            None,
            validation_alias=AliasChoices("dropOffLocation", "drop_off_location"),
            serialization_alias="dropOffLocation",
            description="The drop off location for a package.",
        ),
    ]


"""
DeliveryMessage

Localized messaging for a delivery offering.
"""


class DeliveryMessage(SpApiBaseModel):
    """Localized messaging for a delivery offering."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    text: Annotated[
        Optional[str],
        Field(None, description="The message content for a delivery offering."),
    ]

    locale: Annotated[
        Optional[str],
        Field(None, description="The locale for the message (for example, en_US)."),
    ]


"""
DeliveryPolicy

The policy for a delivery offering.
"""


class DeliveryPolicy(SpApiBaseModel):
    """The policy for a delivery offering."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    message: Annotated[
        Optional["DeliveryMessage"],
        Field(None, description="Localized messaging for a delivery offering."),
    ]


"""
DeliveryOffer

An available offer for delivery of a product.
"""


class DeliveryOffer(SpApiBaseModel):
    """An available offer for delivery of a product."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    expires_at: Annotated[
        Optional["Timestamp"],
        Field(
            None,
            validation_alias=AliasChoices("expiresAt", "expires_at"),
            serialization_alias="expiresAt",
            description="The timestamp at which a delivery offer expires.",
        ),
    ]

    date_range: Annotated[
        Optional["DateRange"],
        Field(
            None,
            validation_alias=AliasChoices("dateRange", "date_range"),
            serialization_alias="dateRange",
            description="The range between which delivery is expected.",
        ),
    ]

    policy: Annotated[
        Optional["DeliveryPolicy"],
        Field(
            None,
            description="The policy for a delivery offer, including localized messaging.",
        ),
    ]


DeliveryOffersList = List["DeliveryOffer"]
"""An array of delivery offer information."""


"""
ProductIdentifier

Product identifier input that locates a product for MCF.
"""


class ProductIdentifier(SpApiBaseModel):
    """Product identifier input that locates a product for MCF."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    merchant_sku: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("merchantSku", "merchant_sku"),
            serialization_alias="merchantSku",
            description="The merchant SKU for the product.",
        ),
    ]


"""
GetDeliveryOffersProduct

The product details for the delivery offer.
"""


class GetDeliveryOffersProduct(SpApiBaseModel):
    """The product details for the delivery offer."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    product_identifier: Annotated[
        "ProductIdentifier",
        Field(
            ...,
            validation_alias=AliasChoices("productIdentifier", "product_identifier"),
            serialization_alias="productIdentifier",
            description="Product identifier input that locates a product for MCF.",
        ),
    ]

    amount: Annotated[
        Optional["Amount"],
        Field(None, description="The amount of the requested product."),
    ]


IpAddress = str
"""An IP Address."""


"""
VariablePrecisionAddress

A physical address with varying degrees of precision. A more precise address can provide more accurate results than country code and postal code alone.
"""


class VariablePrecisionAddress(SpApiBaseModel):
    """A physical address with varying degrees of precision. A more precise address can provide more accurate results than country code and postal code alone."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    address_line1: Annotated[
        Optional[str],
        Field(
            None,
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

    city: Annotated[
        Optional[str],
        Field(
            None,
            description="The city where the person, business, or institution is located. This property should not be used in Japan.",
        ),
    ]

    district_or_county: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("districtOrCounty", "district_or_county"),
            serialization_alias="districtOrCounty",
            description="The district or county where the person, business, or institution is located.",
        ),
    ]

    state_or_region: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("stateOrRegion", "state_or_region"),
            serialization_alias="stateOrRegion",
            description="The state or region where the person, business or institution is located.",
        ),
    ]

    postal_code: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("postalCode", "postal_code"),
            serialization_alias="postalCode",
            description="The postal code of the address.",
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


"""
Destination

The destination for the delivery offer.
"""


class Destination(SpApiBaseModel):
    """The destination for the delivery offer."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    delivery_address: Annotated[
        Optional["VariablePrecisionAddress"],
        Field(
            None,
            validation_alias=AliasChoices("deliveryAddress", "delivery_address"),
            serialization_alias="deliveryAddress",
        ),
    ]

    ip_address: Annotated[
        Optional["IpAddress"],
        Field(
            None,
            validation_alias=AliasChoices("ipAddress", "ip_address"),
            serialization_alias="ipAddress",
            description="The IP address of the customer.",
        ),
    ]


"""
Origin

The origin for the delivery offer.
"""


class Origin(SpApiBaseModel):
    """The origin for the delivery offer."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    country_code: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("countryCode", "country_code"),
            serialization_alias="countryCode",
            description="The two digit country code the items should ship from. In ISO 3166-1 alpha-2 format.",
        ),
    ]


"""
GetDeliveryOffersTerms

The delivery terms for the delivery offer.
"""


class GetDeliveryOffersTerms(SpApiBaseModel):
    """The delivery terms for the delivery offer."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    origin: Annotated[
        "Origin", Field(..., description="The origin for the delivery offer.")
    ]

    destination: Annotated[
        "Destination", Field(..., description="The destination for the delivery offer.")
    ]


"""
GetDeliveryOffersRequestBody

The request body schema for the getDeliveryOffers operation.
"""


class GetDeliveryOffersRequestBody(SpApiBaseModel):
    """The request body schema for the getDeliveryOffers operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    product: Annotated[
        "GetDeliveryOffersProduct",
        Field(..., description="The product details for the delivery offer."),
    ]

    terms: Annotated[
        "GetDeliveryOffersTerms",
        Field(..., description="The terms for the delivery offer."),
    ]


"""
DeliveryOffersRequest

Request parameters for deliveryOffers
"""


class DeliveryOffersRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for deliveryOffers
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    body: Annotated[
        "GetDeliveryOffersRequestBody",
        BodyParam(),
        Field(..., description="[BODY] GetDeliveryOffersRequestBody parameter"),
    ]


DeliveryWindowList = List["DeliveryWindow"]
"""An array of delivery windows."""


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
"""The event code for the delivery event."""


"""
Feature

A Multi-Channel Fulfillment feature.
"""


class Feature(SpApiBaseModel):
    """A Multi-Channel Fulfillment feature."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    feature_name: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("featureName", "feature_name"),
            serialization_alias="featureName",
            description="The feature name.",
        ),
    ]

    feature_description: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("featureDescription", "feature_description"),
            serialization_alias="featureDescription",
            description="The feature description.",
        ),
    ]

    seller_eligible: Annotated[
        Optional[bool],
        Field(
            None,
            validation_alias=AliasChoices("sellerEligible", "seller_eligible"),
            serialization_alias="sellerEligible",
            description="When true, indicates that the seller is eligible to use the feature.",
        ),
    ]


"""
FeatureSku

Information about an SKU, including the count available, identifiers, and a list of overlapping SKUs that share the same inventory pool.
"""


class FeatureSku(SpApiBaseModel):
    """Information about an SKU, including the count available, identifiers, and a list of overlapping SKUs that share the same inventory pool."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    seller_sku: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("sellerSku", "seller_sku"),
            serialization_alias="sellerSku",
            description="Used to identify an item in the given marketplace. `SellerSKU` is qualified by the seller's SellerId, which is included with every operation that you submit.",
        ),
    ]

    fn_sku: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("fnSku", "fn_sku"),
            serialization_alias="fnSku",
            description="The unique SKU used by Amazon's fulfillment network.",
        ),
    ]

    asin: Annotated[
        Optional[str],
        Field(
            None,
            description="The Amazon Standard Identification Number (ASIN) of the item.",
        ),
    ]

    sku_count: Annotated[
        Optional[float],
        Field(
            None,
            validation_alias=AliasChoices("skuCount", "sku_count"),
            serialization_alias="skuCount",
            description="The number of SKUs available for this service.",
        ),
    ]

    overlapping_skus: Annotated[
        Optional[List["str"]],
        Field(
            None,
            validation_alias=AliasChoices("overlappingSkus", "overlapping_skus"),
            serialization_alias="overlappingSkus",
            description="Other seller SKUs that are shared across the same inventory.",
        ),
    ]


Features = List["Feature"]
"""An array of features."""


# Enum definitions
class NameEnum(str, Enum):
    """Enum for name"""

    FBA_PER_UNIT_FULFILLMENT_FEE = "FBAPerUnitFulfillmentFee"  # Estimated fee for each unit in the fulfillment order.
    FBA_PER_ORDER_FULFILLMENT_FEE = (
        "FBAPerOrderFulfillmentFee"  # Estimated order-level fee.
    )
    FBA_TRANSPORTATION_FEE = "FBATransportationFee"  # Estimated shipping fee.
    FBA_FULFILLMENT_COD_FEE = "FBAFulfillmentCODFee"  # Estimated COD (Cash On Delivery) fee. This fee applies only to fulfillment order previews for COD.


"""
Fee

Fee type and cost.
"""


class Fee(SpApiBaseModel):
    """Fee type and cost."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    name: Annotated[NameEnum, Field(..., description="The type of fee.")]

    amount: Annotated["Money", Field(..., description="The amount of the fee.")]


FeeList = List["Fee"]
"""An array of fee type and cost pairs."""


FulfillmentOrderStatus = str
"""The current status of the fulfillment order."""


"""
FulfillmentOrder

General information about a fulfillment order, including its status.
"""


class FulfillmentOrder(SpApiBaseModel):
    """General information about a fulfillment order, including its status."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    seller_fulfillment_order_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices(
                "sellerFulfillmentOrderId", "seller_fulfillment_order_id"
            ),
            serialization_alias="sellerFulfillmentOrderId",
            description="The fulfillment order identifier submitted with the `createFulfillmentOrder` operation.",
        ),
    ]

    marketplace_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="The identifier for the marketplace the fulfillment order is placed against.",
        ),
    ]

    displayable_order_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("displayableOrderId", "displayable_order_id"),
            serialization_alias="displayableOrderId",
            description="A fulfillment order identifier submitted with the `createFulfillmentOrder` operation. Displays as the order identifier in recipient-facing materials such as the packing slip.",
        ),
    ]

    displayable_order_date: Annotated[
        "Timestamp",
        Field(
            ...,
            validation_alias=AliasChoices(
                "displayableOrderDate", "displayable_order_date"
            ),
            serialization_alias="displayableOrderDate",
            description="A date and time submitted with the `createFulfillmentOrder` operation. Displays as the order date in recipient-facing materials such as the packing slip.",
        ),
    ]

    displayable_order_comment: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices(
                "displayableOrderComment", "displayable_order_comment"
            ),
            serialization_alias="displayableOrderComment",
            description="A text block submitted with the `createFulfillmentOrder` operation. Displays in recipient-facing materials such as the packing slip.",
        ),
    ]

    shipping_speed_category: Annotated[
        "ShippingSpeedCategory",
        Field(
            ...,
            validation_alias=AliasChoices(
                "shippingSpeedCategory", "shipping_speed_category"
            ),
            serialization_alias="shippingSpeedCategory",
        ),
    ]

    delivery_window: Annotated[
        Optional["DeliveryWindow"],
        Field(
            None,
            validation_alias=AliasChoices("deliveryWindow", "delivery_window"),
            serialization_alias="deliveryWindow",
        ),
    ]

    destination_address: Annotated[
        "Address",
        Field(
            ...,
            validation_alias=AliasChoices("destinationAddress", "destination_address"),
            serialization_alias="destinationAddress",
            description="The destination address submitted with the `createFulfillmentOrder` operation.",
        ),
    ]

    fulfillment_action: Annotated[
        Optional["FulfillmentAction"],
        Field(
            None,
            validation_alias=AliasChoices("fulfillmentAction", "fulfillment_action"),
            serialization_alias="fulfillmentAction",
        ),
    ]

    fulfillment_policy: Annotated[
        Optional["FulfillmentPolicy"],
        Field(
            None,
            validation_alias=AliasChoices("fulfillmentPolicy", "fulfillment_policy"),
            serialization_alias="fulfillmentPolicy",
        ),
    ]

    cod_settings: Annotated[
        Optional["CODSettings"],
        Field(
            None,
            validation_alias=AliasChoices("codSettings", "cod_settings"),
            serialization_alias="codSettings",
        ),
    ]

    received_date: Annotated[
        "Timestamp",
        Field(
            ...,
            validation_alias=AliasChoices("receivedDate", "received_date"),
            serialization_alias="receivedDate",
            description="The date and time that the fulfillment order was received by an Amazon fulfillment center.",
        ),
    ]

    fulfillment_order_status: Annotated[
        "FulfillmentOrderStatus",
        Field(
            ...,
            validation_alias=AliasChoices(
                "fulfillmentOrderStatus", "fulfillment_order_status"
            ),
            serialization_alias="fulfillmentOrderStatus",
        ),
    ]

    status_updated_date: Annotated[
        "Timestamp",
        Field(
            ...,
            validation_alias=AliasChoices("statusUpdatedDate", "status_updated_date"),
            serialization_alias="statusUpdatedDate",
            description="The date and time that the status of the fulfillment order last changed. Must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format.",
        ),
    ]

    notification_emails: Annotated[
        Optional["NotificationEmailList"],
        Field(
            None,
            validation_alias=AliasChoices("notificationEmails", "notification_emails"),
            serialization_alias="notificationEmails",
        ),
    ]

    feature_constraints: Annotated[
        Optional[List["FeatureSettings"]],
        Field(
            None,
            validation_alias=AliasChoices("featureConstraints", "feature_constraints"),
            serialization_alias="featureConstraints",
            description="A list of features and their fulfillment policies to apply to the order.",
        ),
    ]


"""
FulfillmentOrderItem

Item information for a fulfillment order.
"""


class FulfillmentOrderItem(SpApiBaseModel):
    """Item information for a fulfillment order."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    seller_sku: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("sellerSku", "seller_sku"),
            serialization_alias="sellerSku",
            description="The seller SKU of the item.",
        ),
    ]

    seller_fulfillment_order_item_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices(
                "sellerFulfillmentOrderItemId", "seller_fulfillment_order_item_id"
            ),
            serialization_alias="sellerFulfillmentOrderItemId",
            description="A fulfillment order item identifier submitted with a call to the `createFulfillmentOrder` operation.",
        ),
    ]

    quantity: Annotated[
        "Quantity",
        Field(
            ...,
        ),
    ]

    gift_message: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("giftMessage", "gift_message"),
            serialization_alias="giftMessage",
            description="A message to the gift recipient, if applicable.",
        ),
    ]

    displayable_comment: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("displayableComment", "displayable_comment"),
            serialization_alias="displayableComment",
            description="Item-specific text that displays in recipient-facing materials such as the outbound shipment packing slip.",
        ),
    ]

    fulfillment_network_sku: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "fulfillmentNetworkSku", "fulfillment_network_sku"
            ),
            serialization_alias="fulfillmentNetworkSku",
            description="Amazon's fulfillment network SKU of the item.",
        ),
    ]

    order_item_disposition: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "orderItemDisposition", "order_item_disposition"
            ),
            serialization_alias="orderItemDisposition",
            description="Indicates whether the item is sellable or unsellable.",
        ),
    ]

    cancelled_quantity: Annotated[
        "Quantity",
        Field(
            ...,
            validation_alias=AliasChoices("cancelledQuantity", "cancelled_quantity"),
            serialization_alias="cancelledQuantity",
            description="The item quantity that was cancelled by the seller.",
        ),
    ]

    unfulfillable_quantity: Annotated[
        "Quantity",
        Field(
            ...,
            validation_alias=AliasChoices(
                "unfulfillableQuantity", "unfulfillable_quantity"
            ),
            serialization_alias="unfulfillableQuantity",
            description="The item quantity that is unfulfillable.",
        ),
    ]

    estimated_ship_date: Annotated[
        Optional["Timestamp"],
        Field(
            None,
            validation_alias=AliasChoices("estimatedShipDate", "estimated_ship_date"),
            serialization_alias="estimatedShipDate",
            description="The estimated date and time that the item quantity is scheduled to ship from the fulfillment center. Note that this value can change over time. If the shipment that contains the item quantity has been cancelled, `estimatedShipDate` is not returned.",
        ),
    ]

    estimated_arrival_date: Annotated[
        Optional["Timestamp"],
        Field(
            None,
            validation_alias=AliasChoices(
                "estimatedArrivalDate", "estimated_arrival_date"
            ),
            serialization_alias="estimatedArrivalDate",
            description="The estimated arrival date and time of the item quantity. Note that this value can change over time. If the shipment that contains the item quantity has been cancelled, `estimatedArrivalDate` is not returned.",
        ),
    ]

    per_unit_price: Annotated[
        Optional["Money"],
        Field(
            None,
            validation_alias=AliasChoices("perUnitPrice", "per_unit_price"),
            serialization_alias="perUnitPrice",
            description="The amount to be collected from the recipient for this item in a COD (Cash On Delivery) order.",
        ),
    ]

    per_unit_tax: Annotated[
        Optional["Money"],
        Field(
            None,
            validation_alias=AliasChoices("perUnitTax", "per_unit_tax"),
            serialization_alias="perUnitTax",
            description="The tax on the amount to be collected from the recipient for this item in a COD (Cash On Delivery) order.",
        ),
    ]

    per_unit_declared_value: Annotated[
        Optional["Money"],
        Field(
            None,
            validation_alias=AliasChoices(
                "perUnitDeclaredValue", "per_unit_declared_value"
            ),
            serialization_alias="perUnitDeclaredValue",
            description="The monetary value assigned by the seller to this item. This is a required field for India MCF orders.",
        ),
    ]


FulfillmentOrderItemList = List["FulfillmentOrderItem"]
"""An array of fulfillment order item information."""


FulfillmentPreviewShipmentList = List["FulfillmentPreviewShipment"]
"""An array of fulfillment preview shipment information."""


"""
ScheduledDeliveryInfo

Delivery information for a scheduled delivery. This is only available in the JP marketplace.
"""


class ScheduledDeliveryInfo(SpApiBaseModel):
    """Delivery information for a scheduled delivery. This is only available in the JP marketplace."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    delivery_time_zone: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("deliveryTimeZone", "delivery_time_zone"),
            serialization_alias="deliveryTimeZone",
            description="The time zone of the destination address for the fulfillment order preview. Must be an IANA time zone name. Example: Asia/Tokyo.",
        ),
    ]

    delivery_windows: Annotated[
        "DeliveryWindowList",
        Field(
            ...,
            validation_alias=AliasChoices("deliveryWindows", "delivery_windows"),
            serialization_alias="deliveryWindows",
            description="An array of time ranges that are available for scheduled delivery.",
        ),
    ]


"""
StringList

String list
"""


class StringList(SpApiBaseModel):
    """String list"""

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow",
        serialize_by_alias=True,
        arbitrary_types_allowed=True,
    )


UnfulfillablePreviewItemList = List["UnfulfillablePreviewItem"]
"""An array of unfulfillable preview item information."""


# Enum definitions
class UnitEnum(str, Enum):
    """Enum for unit"""

    KG = "KG"  # Kilograms.
    KILOGRAMS = "KILOGRAMS"  # Kilograms.
    LB = "LB"  # Pounds.
    POUNDS = "POUNDS"  # Pounds.


"""
Weight

The weight.
"""


class Weight(SpApiBaseModel):
    """The weight."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    unit: Annotated[UnitEnum, Field(..., description="The unit of weight.")]

    value: Annotated[str, Field(..., description="The weight value.")]


"""
FulfillmentPreview

Information about a fulfillment order preview, including delivery and fee information based on shipping method.
"""


class FulfillmentPreview(SpApiBaseModel):
    """Information about a fulfillment order preview, including delivery and fee information based on shipping method."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    shipping_speed_category: Annotated[
        "ShippingSpeedCategory",
        Field(
            ...,
            validation_alias=AliasChoices(
                "shippingSpeedCategory", "shipping_speed_category"
            ),
            serialization_alias="shippingSpeedCategory",
        ),
    ]

    scheduled_delivery_info: Annotated[
        Optional["ScheduledDeliveryInfo"],
        Field(
            None,
            validation_alias=AliasChoices(
                "scheduledDeliveryInfo", "scheduled_delivery_info"
            ),
            serialization_alias="scheduledDeliveryInfo",
        ),
    ]

    is_fulfillable: Annotated[
        bool,
        Field(
            ...,
            validation_alias=AliasChoices("isFulfillable", "is_fulfillable"),
            serialization_alias="isFulfillable",
            description="When true, this fulfillment order preview is fulfillable.",
        ),
    ]

    is_c_o_d_capable: Annotated[
        bool,
        Field(
            ...,
            validation_alias=AliasChoices("isCODCapable", "is_c_o_d_capable"),
            serialization_alias="isCODCapable",
            description="When true, this fulfillment order preview is for COD (Cash On Delivery).",
        ),
    ]

    estimated_shipping_weight: Annotated[
        Optional["Weight"],
        Field(
            None,
            validation_alias=AliasChoices(
                "estimatedShippingWeight", "estimated_shipping_weight"
            ),
            serialization_alias="estimatedShippingWeight",
            description="Estimated shipping weight for this fulfillment order preview.",
        ),
    ]

    estimated_fees: Annotated[
        Optional["FeeList"],
        Field(
            None,
            validation_alias=AliasChoices("estimatedFees", "estimated_fees"),
            serialization_alias="estimatedFees",
            description="The estimated fulfillment fees for this fulfillment order preview, if applicable. The fees data will not be available for IN marketplace orders.",
        ),
    ]

    fulfillment_preview_shipments: Annotated[
        Optional["FulfillmentPreviewShipmentList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "fulfillmentPreviewShipments", "fulfillment_preview_shipments"
            ),
            serialization_alias="fulfillmentPreviewShipments",
        ),
    ]

    unfulfillable_preview_items: Annotated[
        Optional["UnfulfillablePreviewItemList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "unfulfillablePreviewItems", "unfulfillable_preview_items"
            ),
            serialization_alias="unfulfillablePreviewItems",
        ),
    ]

    order_unfulfillable_reasons: Annotated[
        Optional["StringList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "orderUnfulfillableReasons", "order_unfulfillable_reasons"
            ),
            serialization_alias="orderUnfulfillableReasons",
            description="Error codes associated with the fulfillment order preview that indicate why the order is not fulfillable. Error code examples: `DeliverySLAUnavailable` `InvalidDestinationAddress`",
        ),
    ]

    marketplace_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="The marketplace the fulfillment order is placed against.",
        ),
    ]

    feature_constraints: Annotated[
        Optional[List["FeatureSettings"]],
        Field(
            None,
            validation_alias=AliasChoices("featureConstraints", "feature_constraints"),
            serialization_alias="featureConstraints",
            description="A list of features and their fulfillment policies to apply to the order.",
        ),
    ]


# Enum definitions
class ShippingWeightCalculationMethodEnum(str, Enum):
    """Enum for shippingWeightCalculationMethod"""

    PACKAGE = "Package"  # Based on the actual weight of the items.
    DIMENSIONAL = "Dimensional"  # Based on the cubic space that the items occupy.


"""
FulfillmentPreviewItem

Item information for a shipment in a fulfillment order preview.
"""


class FulfillmentPreviewItem(SpApiBaseModel):
    """Item information for a shipment in a fulfillment order preview."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    seller_sku: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("sellerSku", "seller_sku"),
            serialization_alias="sellerSku",
            description="The seller SKU of the item.",
        ),
    ]

    quantity: Annotated["Quantity", Field(..., description="The item quantity.")]

    seller_fulfillment_order_item_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices(
                "sellerFulfillmentOrderItemId", "seller_fulfillment_order_item_id"
            ),
            serialization_alias="sellerFulfillmentOrderItemId",
            description="A fulfillment order item identifier that the seller created with a call to the `createFulfillmentOrder` operation.",
        ),
    ]

    estimated_shipping_weight: Annotated[
        Optional["Weight"],
        Field(
            None,
            validation_alias=AliasChoices(
                "estimatedShippingWeight", "estimated_shipping_weight"
            ),
            serialization_alias="estimatedShippingWeight",
            description="The estimated shipping weight of the item quantity for a single item, as identified by `sellerSku`, in a shipment.",
        ),
    ]

    shipping_weight_calculation_method: Annotated[
        Optional[ShippingWeightCalculationMethodEnum],
        Field(
            None,
            validation_alias=AliasChoices(
                "shippingWeightCalculationMethod", "shipping_weight_calculation_method"
            ),
            serialization_alias="shippingWeightCalculationMethod",
            description="The method used to calculate the estimated shipping weight.",
        ),
    ]


FulfillmentPreviewItemList = List["FulfillmentPreviewItem"]
"""An array of fulfillment preview item information."""


FulfillmentPreviewList = List["FulfillmentPreview"]
"""An array of fulfillment preview information."""


"""
FulfillmentPreviewShipment

Delivery and item information for a shipment in a fulfillment order preview.
"""


class FulfillmentPreviewShipment(SpApiBaseModel):
    """Delivery and item information for a shipment in a fulfillment order preview."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    earliest_ship_date: Annotated[
        Optional["Timestamp"],
        Field(
            None,
            validation_alias=AliasChoices("earliestShipDate", "earliest_ship_date"),
            serialization_alias="earliestShipDate",
            description="The earliest date that the shipment is expected to be sent from the fulfillment center. Must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format.",
        ),
    ]

    latest_ship_date: Annotated[
        Optional["Timestamp"],
        Field(
            None,
            validation_alias=AliasChoices("latestShipDate", "latest_ship_date"),
            serialization_alias="latestShipDate",
            description="The latest date that the shipment is expected to be sent from the fulfillment center. Must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format.",
        ),
    ]

    earliest_arrival_date: Annotated[
        Optional["Timestamp"],
        Field(
            None,
            validation_alias=AliasChoices(
                "earliestArrivalDate", "earliest_arrival_date"
            ),
            serialization_alias="earliestArrivalDate",
            description="The earliest date that the shipment is expected to arrive at its destination.",
        ),
    ]

    latest_arrival_date: Annotated[
        Optional["Timestamp"],
        Field(
            None,
            validation_alias=AliasChoices("latestArrivalDate", "latest_arrival_date"),
            serialization_alias="latestArrivalDate",
            description="The latest date that the shipment is expected to arrive at its destination. Must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format.",
        ),
    ]

    shipping_notes: Annotated[
        Optional[List["str"]],
        Field(
            None,
            validation_alias=AliasChoices("shippingNotes", "shipping_notes"),
            serialization_alias="shippingNotes",
            description="Provides additional insight into the shipment timeline when exact delivery dates are not able to be precomputed.",
        ),
    ]

    fulfillment_preview_items: Annotated[
        "FulfillmentPreviewItemList",
        Field(
            ...,
            validation_alias=AliasChoices(
                "fulfillmentPreviewItems", "fulfillment_preview_items"
            ),
            serialization_alias="fulfillmentPreviewItems",
            description="Information about the items in the shipment.",
        ),
    ]


FulfillmentReturnItemStatus = str
"""Indicates if the return item has been processed by a fulfillment center."""


FulfillmentShipmentItemList = List["FulfillmentShipmentItem"]
"""An array of fulfillment shipment item information."""


FulfillmentShipmentPackageList = List["FulfillmentShipmentPackage"]
"""An array of fulfillment shipment package information."""


# Enum definitions
class FulfillmentShipmentStatusEnum(str, Enum):
    """Enum for fulfillmentShipmentStatus"""

    PENDING = "PENDING"  # The process of picking units from inventory has begun.
    SHIPPED = (
        "SHIPPED"  # All packages in the shipment have left the fulfillment center.
    )
    CANCELLED_BY_FULFILLER = "CANCELLED_BY_FULFILLER"  # The Amazon fulfillment center could not fulfill the shipment as planned. This might be because the inventory was not at the expected location in the fulfillment center. After cancelling the fulfillment order, Amazon immediately creates a new fulfillment shipment and again attempts to fulfill the order.
    CANCELLED_BY_SELLER = "CANCELLED_BY_SELLER"  # The shipment was cancelled using the `CancelFulfillmentOrder` request.


"""
FulfillmentShipment

Delivery and item information for a shipment in a fulfillment order.
"""


class FulfillmentShipment(SpApiBaseModel):
    """Delivery and item information for a shipment in a fulfillment order."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    amazon_shipment_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("amazonShipmentId", "amazon_shipment_id"),
            serialization_alias="amazonShipmentId",
            description="A shipment identifier assigned by Amazon.",
        ),
    ]

    fulfillment_center_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices(
                "fulfillmentCenterId", "fulfillment_center_id"
            ),
            serialization_alias="fulfillmentCenterId",
            description="An identifier for the fulfillment center that the shipment will be sent from.",
        ),
    ]

    fulfillment_shipment_status: Annotated[
        FulfillmentShipmentStatusEnum,
        Field(
            ...,
            validation_alias=AliasChoices(
                "fulfillmentShipmentStatus", "fulfillment_shipment_status"
            ),
            serialization_alias="fulfillmentShipmentStatus",
            description="The current status of the shipment.",
        ),
    ]

    shipping_date: Annotated[
        Optional["Timestamp"],
        Field(
            None,
            validation_alias=AliasChoices("shippingDate", "shipping_date"),
            serialization_alias="shippingDate",
            description="The meaning of the `shippingDate` value depends on the current status of the shipment. If the current value of `FulfillmentShipmentStatus` is: * Pending - `shippingDate` represents the estimated time that the shipment will leave the Amazon fulfillment center. * Shipped - `shippingDate` represents the date that the shipment left the Amazon fulfillment center. If a shipment includes more than one package, `shippingDate` applies to all of the packages in the shipment. If the value of `FulfillmentShipmentStatus` is `CancelledByFulfiller` or `CancelledBySeller`, `shippingDate` is not returned. The value must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format.",
        ),
    ]

    estimated_arrival_date: Annotated[
        Optional["Timestamp"],
        Field(
            None,
            validation_alias=AliasChoices(
                "estimatedArrivalDate", "estimated_arrival_date"
            ),
            serialization_alias="estimatedArrivalDate",
            description="The estimated arrival date and time of the shipment. Must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format. Note that this value can change over time. If a shipment includes more than one package, `estimatedArrivalDate` applies to all of the packages in the shipment. If the shipment has been cancelled, `estimatedArrivalDate` is not returned.",
        ),
    ]

    shipping_notes: Annotated[
        Optional[List["str"]],
        Field(
            None,
            validation_alias=AliasChoices("shippingNotes", "shipping_notes"),
            serialization_alias="shippingNotes",
            description="Provides additional insight into shipment timeline. Primairly used to communicate that actual delivery dates aren't available.",
        ),
    ]

    fulfillment_shipment_item: Annotated[
        "FulfillmentShipmentItemList",
        Field(
            ...,
            validation_alias=AliasChoices(
                "fulfillmentShipmentItem", "fulfillment_shipment_item"
            ),
            serialization_alias="fulfillmentShipmentItem",
        ),
    ]

    fulfillment_shipment_package: Annotated[
        Optional["FulfillmentShipmentPackageList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "fulfillmentShipmentPackage", "fulfillment_shipment_package"
            ),
            serialization_alias="fulfillmentShipmentPackage",
        ),
    ]


"""
FulfillmentShipmentItem

Item information for a shipment in a fulfillment order.
"""


class FulfillmentShipmentItem(SpApiBaseModel):
    """Item information for a shipment in a fulfillment order."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    seller_sku: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("sellerSku", "seller_sku"),
            serialization_alias="sellerSku",
            description="The seller SKU of the item.",
        ),
    ]

    seller_fulfillment_order_item_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices(
                "sellerFulfillmentOrderItemId", "seller_fulfillment_order_item_id"
            ),
            serialization_alias="sellerFulfillmentOrderItemId",
            description="The fulfillment order item identifier that the seller created and submitted with a call to the `createFulfillmentOrder` operation.",
        ),
    ]

    quantity: Annotated[
        "Quantity",
        Field(
            ...,
        ),
    ]

    package_number: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices("packageNumber", "package_number"),
            serialization_alias="packageNumber",
            description="An identifier for the package that contains the item quantity.",
        ),
    ]

    serial_number: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("serialNumber", "serial_number"),
            serialization_alias="serialNumber",
            description="The serial number of the shipped item.",
        ),
    ]

    manufacturer_lot_codes: Annotated[
        Optional["StringList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "manufacturerLotCodes", "manufacturer_lot_codes"
            ),
            serialization_alias="manufacturerLotCodes",
            description="The manufacturer lot codes of the shipped items.",
        ),
    ]


FulfillmentShipmentList = List["FulfillmentShipment"]
"""An array of fulfillment shipment information."""


"""
LockerDetails

The locker details, which you can use to access the locker delivery box.
"""


class LockerDetails(SpApiBaseModel):
    """The locker details, which you can use to access the locker delivery box."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    locker_number: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("lockerNumber", "locker_number"),
            serialization_alias="lockerNumber",
            description="Indicates the locker number",
        ),
    ]

    locker_access_code: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("lockerAccessCode", "locker_access_code"),
            serialization_alias="lockerAccessCode",
            description="Indicates the locker access code",
        ),
    ]


"""
FulfillmentShipmentPackage

Package information for a shipment in a fulfillment order.
"""


class FulfillmentShipmentPackage(SpApiBaseModel):
    """Package information for a shipment in a fulfillment order."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    package_number: Annotated[
        int,
        Field(
            ...,
            validation_alias=AliasChoices("packageNumber", "package_number"),
            serialization_alias="packageNumber",
            description="Identifies a package in a shipment.",
        ),
    ]

    carrier_code: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("carrierCode", "carrier_code"),
            serialization_alias="carrierCode",
            description="Identifies the carrier who will deliver the shipment to the recipient.",
        ),
    ]

    tracking_number: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("trackingNumber", "tracking_number"),
            serialization_alias="trackingNumber",
            description="The tracking number, if provided, can be used to obtain tracking and delivery information.",
        ),
    ]

    estimated_arrival_date: Annotated[
        Optional["Timestamp"],
        Field(
            None,
            validation_alias=AliasChoices(
                "estimatedArrivalDate", "estimated_arrival_date"
            ),
            serialization_alias="estimatedArrivalDate",
            description="The estimated arrival date and time of the package. Must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format.",
        ),
    ]

    locker_details: Annotated[
        Optional["LockerDetails"],
        Field(
            None,
            validation_alias=AliasChoices("lockerDetails", "locker_details"),
            serialization_alias="lockerDetails",
            description="The locker details, if provided can be used to access locker delivery box.",
        ),
    ]

    delivery_information: Annotated[
        Optional["DeliveryInformation"],
        Field(
            None,
            validation_alias=AliasChoices(
                "deliveryInformation", "delivery_information"
            ),
            serialization_alias="deliveryInformation",
            description="The delivery information for the package. This information is available after the package is delivered.",
        ),
    ]


"""
GetDeliveryOffersResult

A list of delivery offers, including offer expiration, earliest and latest date and time range, and the delivery offer policy.
"""


class GetDeliveryOffersResult(SpApiBaseModel):
    """A list of delivery offers, including offer expiration, earliest and latest date and time range, and the delivery offer policy."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    delivery_offers: Annotated[
        Optional["DeliveryOffersList"],
        Field(
            None,
            validation_alias=AliasChoices("deliveryOffers", "delivery_offers"),
            serialization_alias="deliveryOffers",
            description="An array of delivery offers.",
        ),
    ]


"""
GetDeliveryOffersResponse

The response schema for the getDeliveryOffers operation.
"""


class GetDeliveryOffersResponse(SpApiBaseModel):
    """The response schema for the getDeliveryOffers operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["GetDeliveryOffersResult"],
        Field(
            None,
            description="The response payload for the getDeliveryOffers operation.",
        ),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
            description="One or more unexpected errors occurred during the getDeliveryOffers operation.",
        ),
    ]


"""
GetFeatureInventoryRequest

Request parameters for getFeatureInventory
"""


class GetFeatureInventoryRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getFeatureInventory
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
            description="[QUERY] The marketplace for which to return a list of the inventory that is eligible for the specified feature.",
        ),
    ]

    feature_name: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("featureName", "feature_name"),
            serialization_alias="featureName",
            description="[PATH] The name of the feature for which to return a list of eligible inventory.",
        ),
    ]

    next_token: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("nextToken", "next_token"),
            serialization_alias="nextToken",
            description="[QUERY] A string token returned in the response to your previous request that is used to return the next response page. A value of null will return the first page.",
        ),
    ]

    query_start_date: Annotated[
        Optional[datetime],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("queryStartDate", "query_start_date"),
            serialization_alias="queryStartDate",
            description="[QUERY] A date that you can use to select inventory that has been updated since a specified date. An update is defined as any change in feature-enabled inventory availability. The date must be in the format yyyy-MM-ddTHH:mm:ss.sssZ",
        ),
    ]


"""
GetFeatureInventoryResult

The payload for the `getEligibileInventory` operation.
"""


class GetFeatureInventoryResult(SpApiBaseModel):
    """The payload for the `getEligibileInventory` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    marketplace_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="The requested marketplace.",
        ),
    ]

    feature_name: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("featureName", "feature_name"),
            serialization_alias="featureName",
            description="The name of the feature.",
        ),
    ]

    next_token: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("nextToken", "next_token"),
            serialization_alias="nextToken",
            description="When present and not empty, pass this string token in the next request to return the next response page.",
        ),
    ]

    feature_skus: Annotated[
        Optional[List["FeatureSku"]],
        Field(
            None,
            validation_alias=AliasChoices("featureSkus", "feature_skus"),
            serialization_alias="featureSkus",
            description="An array of SKUs eligible for this feature and the quantity available.",
        ),
    ]


"""
GetFeatureInventoryResponse

The breakdown of eligibility inventory by feature.
"""


class GetFeatureInventoryResponse(SpApiBaseModel):
    """The breakdown of eligibility inventory by feature."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["GetFeatureInventoryResult"],
        Field(
            None,
        ),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
            description="One or more unexpected errors occurred during the `getFeatureInventory` operation.",
        ),
    ]


"""
GetFeatureSKURequest

Request parameters for getFeatureSKU
"""


class GetFeatureSKURequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getFeatureSKU
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
            description="[QUERY] The marketplace for which to return the count.",
        ),
    ]

    feature_name: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("featureName", "feature_name"),
            serialization_alias="featureName",
            description="[PATH] The name of the feature.",
        ),
    ]

    seller_sku: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("sellerSku", "seller_sku"),
            serialization_alias="sellerSku",
            description="[PATH] Used to identify an item in the given marketplace. `SellerSKU` is qualified by the seller's `SellerId`, which is included with every operation that you submit.",
        ),
    ]


"""
GetFeatureSkuResult

The payload for the `getFeatureSKU` operation.
"""


class GetFeatureSkuResult(SpApiBaseModel):
    """The payload for the `getFeatureSKU` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    marketplace_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="The requested marketplace.",
        ),
    ]

    feature_name: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("featureName", "feature_name"),
            serialization_alias="featureName",
            description="The name of the feature.",
        ),
    ]

    is_eligible: Annotated[
        bool,
        Field(
            ...,
            validation_alias=AliasChoices("isEligible", "is_eligible"),
            serialization_alias="isEligible",
            description="When true, the seller SKU is eligible for the requested feature.",
        ),
    ]

    ineligible_reasons: Annotated[
        Optional[List["str"]],
        Field(
            None,
            validation_alias=AliasChoices("ineligibleReasons", "ineligible_reasons"),
            serialization_alias="ineligibleReasons",
            description="A list of one or more reasons that the seller SKU is ineligibile for the feature. Possible values: * `MERCHANT_NOT_ENROLLED` - The merchant isn't enrolled for the feature. * `SKU_NOT_ELIGIBLE` - The SKU doesn't reside in a warehouse that supports the feature. * `INVALID_SKU` - There is an issue with the SKU provided.",
        ),
    ]

    sku_info: Annotated[
        Optional["FeatureSku"],
        Field(
            None,
            validation_alias=AliasChoices("skuInfo", "sku_info"),
            serialization_alias="skuInfo",
            description="Information about the SKU, including the count available, identifiers, and a list of overlapping SKUs that share the same inventory pool.",
        ),
    ]


"""
GetFeatureSkuResponse

The response schema for the `getFeatureSKU` operation.
"""


class GetFeatureSkuResponse(SpApiBaseModel):
    """The response schema for the `getFeatureSKU` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["GetFeatureSkuResult"],
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
GetFeaturesRequest

Request parameters for getFeatures
"""


class GetFeaturesRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getFeatures
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
            description="[QUERY] The marketplace for which to return the list of features.",
        ),
    ]


"""
GetFeaturesResult

The payload for the `getFeatures` operation.
"""


class GetFeaturesResult(SpApiBaseModel):
    """The payload for the `getFeatures` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    features: Annotated[
        "Features",
        Field(
            ...,
        ),
    ]


"""
GetFeaturesResponse

The response schema for the `getFeatures` operation.
"""


class GetFeaturesResponse(SpApiBaseModel):
    """The response schema for the `getFeatures` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["GetFeaturesResult"],
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
GetFulfillmentOrderRequest

Request parameters for getFulfillmentOrder
"""


class GetFulfillmentOrderRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getFulfillmentOrder
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    seller_fulfillment_order_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices(
                "sellerFulfillmentOrderId", "seller_fulfillment_order_id"
            ),
            serialization_alias="sellerFulfillmentOrderId",
            description="[PATH] The identifier assigned to the item by the seller when the fulfillment order was created.",
        ),
    ]


"""
GetFulfillmentOrderResult

The request for the getFulfillmentOrder operation.
"""


class GetFulfillmentOrderResult(SpApiBaseModel):
    """The request for the getFulfillmentOrder operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    fulfillment_order: Annotated[
        "FulfillmentOrder",
        Field(
            ...,
            validation_alias=AliasChoices("fulfillmentOrder", "fulfillment_order"),
            serialization_alias="fulfillmentOrder",
        ),
    ]

    fulfillment_order_items: Annotated[
        "FulfillmentOrderItemList",
        Field(
            ...,
            validation_alias=AliasChoices(
                "fulfillmentOrderItems", "fulfillment_order_items"
            ),
            serialization_alias="fulfillmentOrderItems",
        ),
    ]

    fulfillment_shipments: Annotated[
        Optional["FulfillmentShipmentList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "fulfillmentShipments", "fulfillment_shipments"
            ),
            serialization_alias="fulfillmentShipments",
        ),
    ]

    return_items: Annotated[
        "ReturnItemList",
        Field(
            ...,
            validation_alias=AliasChoices("returnItems", "return_items"),
            serialization_alias="returnItems",
        ),
    ]

    return_authorizations: Annotated[
        "ReturnAuthorizationList",
        Field(
            ...,
            validation_alias=AliasChoices(
                "returnAuthorizations", "return_authorizations"
            ),
            serialization_alias="returnAuthorizations",
        ),
    ]

    payment_information: Annotated[
        Optional["PaymentInformationList"],
        Field(
            None,
            validation_alias=AliasChoices("paymentInformation", "payment_information"),
            serialization_alias="paymentInformation",
        ),
    ]


"""
GetFulfillmentOrderResponse

The response schema for the `getFulfillmentOrder` operation.
"""


class GetFulfillmentOrderResponse(SpApiBaseModel):
    """The response schema for the `getFulfillmentOrder` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["GetFulfillmentOrderResult"],
        Field(None, description="The payload for the `getFulfillmentOrder` operation."),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
            description="One or more unexpected errors occurred during the `getFulfillmentOrder` operation.",
        ),
    ]


"""
GetFulfillmentPreviewItem

Item information for a fulfillment order preview.
"""


class GetFulfillmentPreviewItem(SpApiBaseModel):
    """Item information for a fulfillment order preview."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    seller_sku: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("sellerSku", "seller_sku"),
            serialization_alias="sellerSku",
            description="The seller SKU of the item.",
        ),
    ]

    quantity: Annotated[
        "Quantity",
        Field(
            ...,
        ),
    ]

    per_unit_declared_value: Annotated[
        Optional["Money"],
        Field(
            None,
            validation_alias=AliasChoices(
                "perUnitDeclaredValue", "per_unit_declared_value"
            ),
            serialization_alias="perUnitDeclaredValue",
            description="The monetary value assigned by the seller to this item. This is a required field if this order is an export order or an India MCF order.",
        ),
    ]

    seller_fulfillment_order_item_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices(
                "sellerFulfillmentOrderItemId", "seller_fulfillment_order_item_id"
            ),
            serialization_alias="sellerFulfillmentOrderItemId",
            description="A fulfillment order item identifier that the seller creates to track items in the fulfillment preview.",
        ),
    ]


GetFulfillmentPreviewItemList = List["GetFulfillmentPreviewItem"]
"""An array of fulfillment preview item information."""


ShippingSpeedCategoryList = List["ShippingSpeedCategory"]
"""ShippingSpeedCategory List"""


"""
GetFulfillmentPreviewRequestBody

The request body schema for the `getFulfillmentPreview` operation.
"""


class GetFulfillmentPreviewRequestBody(SpApiBaseModel):
    """The request body schema for the `getFulfillmentPreview` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    marketplace_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="The marketplace the fulfillment order is placed against.",
        ),
    ]

    address: Annotated[
        "Address",
        Field(
            ...,
            description="The destination address for the fulfillment order preview.",
        ),
    ]

    items: Annotated[
        "GetFulfillmentPreviewItemList",
        Field(
            ...,
            description="Identifying information and quantity information for the items in the fulfillment order preview. Maximum of 100 line items with a maximum of 250 units per order. ",
        ),
    ]

    shipping_speed_categories: Annotated[
        Optional["ShippingSpeedCategoryList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "shippingSpeedCategories", "shipping_speed_categories"
            ),
            serialization_alias="shippingSpeedCategories",
            description="A list of shipping methods used for creating fulfillment order previews. Possible values: * `Standard` - Standard shipping method. * `Expedited` - Expedited shipping method. * `Priority` - Priority shipping method. * `ScheduledDelivery` - Scheduled Delivery shipping method. Note: Shipping method service level agreements vary by marketplace. Sellers should refer to the Seller Central website in their marketplace for shipping method service level agreements and fulfillment fees.",
        ),
    ]

    include_c_o_d_fulfillment_preview: Annotated[
        Optional[bool],
        Field(
            None,
            validation_alias=AliasChoices(
                "includeCODFulfillmentPreview", "include_c_o_d_fulfillment_preview"
            ),
            serialization_alias="includeCODFulfillmentPreview",
            description="When true, returns all fulfillment order previews both for COD and not for COD. Otherwise, returns only fulfillment order previews that are not for COD.",
        ),
    ]

    include_delivery_windows: Annotated[
        Optional[bool],
        Field(
            None,
            validation_alias=AliasChoices(
                "includeDeliveryWindows", "include_delivery_windows"
            ),
            serialization_alias="includeDeliveryWindows",
            description="When true, returns the `ScheduledDeliveryInfo` response object, which contains the available delivery windows for a Scheduled Delivery. The `ScheduledDeliveryInfo` response object can only be returned for fulfillment order previews with `ShippingSpeedCategories` = `ScheduledDelivery`.",
        ),
    ]

    feature_constraints: Annotated[
        Optional[List["FeatureSettings"]],
        Field(
            None,
            validation_alias=AliasChoices("featureConstraints", "feature_constraints"),
            serialization_alias="featureConstraints",
            description="A list of features and their fulfillment policies to apply to the order.",
        ),
    ]


"""
GetFulfillmentPreviewRequest

Request parameters for getFulfillmentPreview
"""


class GetFulfillmentPreviewRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getFulfillmentPreview
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    body: Annotated[
        "GetFulfillmentPreviewRequestBody",
        BodyParam(),
        Field(..., description="[BODY] GetFulfillmentPreviewRequestBody parameter"),
    ]


"""
GetFulfillmentPreviewResult

A list of fulfillment order previews, including estimated shipping weights, estimated shipping fees, and estimated ship dates and arrival dates.
"""


class GetFulfillmentPreviewResult(SpApiBaseModel):
    """A list of fulfillment order previews, including estimated shipping weights, estimated shipping fees, and estimated ship dates and arrival dates."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    fulfillment_previews: Annotated[
        Optional["FulfillmentPreviewList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "fulfillmentPreviews", "fulfillment_previews"
            ),
            serialization_alias="fulfillmentPreviews",
        ),
    ]


"""
GetFulfillmentPreviewResponse

The response schema for the `getFulfillmentPreview` operation.
"""


class GetFulfillmentPreviewResponse(SpApiBaseModel):
    """The response schema for the `getFulfillmentPreview` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["GetFulfillmentPreviewResult"],
        Field(
            None,
            description="The response payload for the `getFulfillmentPreview` operation.",
        ),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
            description="One or more unexpected errors occurred during the `getFulfillmentPreview` operation.",
        ),
    ]


"""
GetPackageTrackingDetailsRequest

Request parameters for getPackageTrackingDetails
"""


class GetPackageTrackingDetailsRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getPackageTrackingDetails
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    package_number: Annotated[
        int,
        QueryParam(),
        Field(
            ...,
            validation_alias=AliasChoices("packageNumber", "package_number"),
            serialization_alias="packageNumber",
            description="[QUERY] The unencrypted package identifier returned by the `getFulfillmentOrder` operation.",
        ),
    ]


"""
TrackingAddress

Address information for tracking the package.
"""


class TrackingAddress(SpApiBaseModel):
    """Address information for tracking the package."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    city: Annotated[str, Field(..., description="The city.")]

    state: Annotated[str, Field(..., description="The state.")]

    country: Annotated[str, Field(..., description="The country.")]


TrackingEventList = List["TrackingEvent"]
"""An array of tracking event information."""


"""
PackageTrackingDetails

Tracking details of package
"""


class PackageTrackingDetails(SpApiBaseModel):
    """Tracking details of package"""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    package_number: Annotated[
        int,
        Field(
            ...,
            validation_alias=AliasChoices("packageNumber", "package_number"),
            serialization_alias="packageNumber",
            description="The package identifier.",
        ),
    ]

    tracking_number: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("trackingNumber", "tracking_number"),
            serialization_alias="trackingNumber",
            description="The tracking number for the package.",
        ),
    ]

    customer_tracking_link: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "customerTrackingLink", "customer_tracking_link"
            ),
            serialization_alias="customerTrackingLink",
            description="Link on swiship.com that allows customers to track the package.",
        ),
    ]

    carrier_code: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("carrierCode", "carrier_code"),
            serialization_alias="carrierCode",
            description="The name of the carrier.",
        ),
    ]

    carrier_phone_number: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("carrierPhoneNumber", "carrier_phone_number"),
            serialization_alias="carrierPhoneNumber",
            description="The phone number of the carrier.",
        ),
    ]

    carrier_u_r_l: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("carrierURL", "carrier_u_r_l"),
            serialization_alias="carrierURL",
            description="The URL of the carrier's website.",
        ),
    ]

    ship_date: Annotated[
        Optional["Timestamp"],
        Field(
            None,
            validation_alias=AliasChoices("shipDate", "ship_date"),
            serialization_alias="shipDate",
            description="The shipping date for the package.",
        ),
    ]

    estimated_arrival_date: Annotated[
        Optional["Timestamp"],
        Field(
            None,
            validation_alias=AliasChoices(
                "estimatedArrivalDate", "estimated_arrival_date"
            ),
            serialization_alias="estimatedArrivalDate",
            description="The estimated arrival date.",
        ),
    ]

    ship_to_address: Annotated[
        Optional["TrackingAddress"],
        Field(
            None,
            validation_alias=AliasChoices("shipToAddress", "ship_to_address"),
            serialization_alias="shipToAddress",
            description="The destination city for the package.",
        ),
    ]

    current_status: Annotated[
        Optional["CurrentStatus"],
        Field(
            None,
            validation_alias=AliasChoices("currentStatus", "current_status"),
            serialization_alias="currentStatus",
        ),
    ]

    current_status_description: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "currentStatusDescription", "current_status_description"
            ),
            serialization_alias="currentStatusDescription",
            description="Description corresponding to the CurrentStatus value.",
        ),
    ]

    delivery_window: Annotated[
        Optional["DateRange"],
        Field(
            None,
            validation_alias=AliasChoices("deliveryWindow", "delivery_window"),
            serialization_alias="deliveryWindow",
            description="The delivery window for the package. This is available after the package reaches its destination delivery station.",
        ),
    ]

    signed_for_by: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("signedForBy", "signed_for_by"),
            serialization_alias="signedForBy",
            description="The name of the person who signed for the package.",
        ),
    ]

    additional_location_info: Annotated[
        Optional["AdditionalLocationInfo"],
        Field(
            None,
            validation_alias=AliasChoices(
                "additionalLocationInfo", "additional_location_info"
            ),
            serialization_alias="additionalLocationInfo",
        ),
    ]

    tracking_events: Annotated[
        Optional["TrackingEventList"],
        Field(
            None,
            validation_alias=AliasChoices("trackingEvents", "tracking_events"),
            serialization_alias="trackingEvents",
        ),
    ]


"""
GetPackageTrackingDetailsResponse

The response schema for the `getPackageTrackingDetails` operation.
"""


class GetPackageTrackingDetailsResponse(SpApiBaseModel):
    """The response schema for the `getPackageTrackingDetails` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["PackageTrackingDetails"],
        Field(
            None,
            description="The payload for the `getPackageTrackingDetails` operation.",
        ),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
            description="One or more unexpected errors occurred during the `getPackageTrackingDetails` operation.",
        ),
    ]


InvalidItemReasonCode = str
"""A code for why the item is invalid for return."""


"""
InvalidItemReason

The reason that the item is invalid for return.
"""


class InvalidItemReason(SpApiBaseModel):
    """The reason that the item is invalid for return."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    invalid_item_reason_code: Annotated[
        "InvalidItemReasonCode",
        Field(
            ...,
            validation_alias=AliasChoices(
                "invalidItemReasonCode", "invalid_item_reason_code"
            ),
            serialization_alias="invalidItemReasonCode",
        ),
    ]

    description: Annotated[
        str,
        Field(
            ...,
            description="A human readable description of the invalid item reason code.",
        ),
    ]


"""
InvalidReturnItem

An item that is invalid for return.
"""


class InvalidReturnItem(SpApiBaseModel):
    """An item that is invalid for return."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    seller_return_item_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices(
                "sellerReturnItemId", "seller_return_item_id"
            ),
            serialization_alias="sellerReturnItemId",
            description="An identifier assigned by the seller to the return item.",
        ),
    ]

    seller_fulfillment_order_item_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices(
                "sellerFulfillmentOrderItemId", "seller_fulfillment_order_item_id"
            ),
            serialization_alias="sellerFulfillmentOrderItemId",
            description="The identifier assigned to the item by the seller when the fulfillment order was created.",
        ),
    ]

    invalid_item_reason: Annotated[
        "InvalidItemReason",
        Field(
            ...,
            validation_alias=AliasChoices("invalidItemReason", "invalid_item_reason"),
            serialization_alias="invalidItemReason",
        ),
    ]


"""
ListAllFulfillmentOrdersRequest

Request parameters for listAllFulfillmentOrders
"""


class ListAllFulfillmentOrdersRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for listAllFulfillmentOrders
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    query_start_date: Annotated[
        Optional[datetime],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("queryStartDate", "query_start_date"),
            serialization_alias="queryStartDate",
            description="[QUERY] A date used to select fulfillment orders that were last updated after (or at) a specified time. An update is defined as any change in fulfillment order status, including the creation of a new fulfillment order.",
        ),
    ]

    next_token: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("nextToken", "next_token"),
            serialization_alias="nextToken",
            description="[QUERY] A string token returned in the response to your previous request.",
        ),
    ]


"""
ListAllFulfillmentOrdersResult

The request for the listAllFulfillmentOrders operation.
"""


class ListAllFulfillmentOrdersResult(SpApiBaseModel):
    """The request for the listAllFulfillmentOrders operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    next_token: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("nextToken", "next_token"),
            serialization_alias="nextToken",
            description="When present and not empty, pass this string token in the next request to return the next response page.",
        ),
    ]

    fulfillment_orders: Annotated[
        Optional[List["FulfillmentOrder"]],
        Field(
            None,
            validation_alias=AliasChoices("fulfillmentOrders", "fulfillment_orders"),
            serialization_alias="fulfillmentOrders",
            description="An array of fulfillment order information.",
        ),
    ]


"""
ListAllFulfillmentOrdersResponse

The response schema for the `listAllFulfillmentOrders` operation.
"""


class ListAllFulfillmentOrdersResponse(SpApiBaseModel):
    """The response schema for the `listAllFulfillmentOrders` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["ListAllFulfillmentOrdersResult"],
        Field(
            None,
            description="The payload for the `listAllFulfillmentOrders` operation.",
        ),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
            description="One or more unexpected errors occurred during the `listAllFulfillmentOrders` operation.",
        ),
    ]


"""
ListReturnReasonCodesRequest

Request parameters for listReturnReasonCodes
"""


class ListReturnReasonCodesRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for listReturnReasonCodes
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    seller_sku: Annotated[
        str,
        QueryParam(),
        Field(
            ...,
            validation_alias=AliasChoices("sellerSku", "seller_sku"),
            serialization_alias="sellerSku",
            description="[QUERY] The seller SKU for which return reason codes are required.",
        ),
    ]

    marketplace_id: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="[QUERY] The marketplace for which the seller wants return reason codes.",
        ),
    ]

    seller_fulfillment_order_id: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices(
                "sellerFulfillmentOrderId", "seller_fulfillment_order_id"
            ),
            serialization_alias="sellerFulfillmentOrderId",
            description="[QUERY] The identifier assigned to the item by the seller when the fulfillment order was created. The service uses this value to determine the marketplace for which the seller wants return reason codes.",
        ),
    ]

    language: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            description="[QUERY] The language that the `TranslatedDescription` property of the `ReasonCodeDetails` response object should be translated into.",
        ),
    ]


ReasonCodeDetailsList = List["ReasonCodeDetails"]
"""An array of return reason code details."""


"""
ListReturnReasonCodesResult

The request for the listReturnReasonCodes operation.
"""


class ListReturnReasonCodesResult(SpApiBaseModel):
    """The request for the listReturnReasonCodes operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    reason_code_details: Annotated[
        Optional["ReasonCodeDetailsList"],
        Field(
            None,
            validation_alias=AliasChoices("reasonCodeDetails", "reason_code_details"),
            serialization_alias="reasonCodeDetails",
        ),
    ]


"""
ListReturnReasonCodesResponse

The response schema for the `listReturnReasonCodes` operation.
"""


class ListReturnReasonCodesResponse(SpApiBaseModel):
    """The response schema for the `listReturnReasonCodes` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["ListReturnReasonCodesResult"],
        Field(
            None, description="The payload for the `listReturnReasonCodes` operation."
        ),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
            description="One or more unexpected errors occurred during the `listReturnReasonCodes` operation.",
        ),
    ]


"""
PaymentInformation

The attributes related to the payment made from customer to seller for this order.
"""


class PaymentInformation(SpApiBaseModel):
    """The attributes related to the payment made from customer to seller for this order."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payment_transaction_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices(
                "paymentTransactionId", "payment_transaction_id"
            ),
            serialization_alias="paymentTransactionId",
            description="The transaction identifier of this payment.",
        ),
    ]

    payment_mode: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("paymentMode", "payment_mode"),
            serialization_alias="paymentMode",
            description="The transaction mode of this payment.",
        ),
    ]

    payment_date: Annotated[
        "Timestamp",
        Field(
            ...,
            validation_alias=AliasChoices("paymentDate", "payment_date"),
            serialization_alias="paymentDate",
            description="The transaction date of this payment.",
        ),
    ]


"""
ReasonCodeDetails

A return reason code, a description, and an optional description translation.
"""


class ReasonCodeDetails(SpApiBaseModel):
    """A return reason code, a description, and an optional description translation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    return_reason_code: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("returnReasonCode", "return_reason_code"),
            serialization_alias="returnReasonCode",
            description="A code that indicates a valid return reason.",
        ),
    ]

    description: Annotated[
        str,
        Field(
            ..., description="A human readable description of the return reason code."
        ),
    ]

    translated_description: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "translatedDescription", "translated_description"
            ),
            serialization_alias="translatedDescription",
            description="A translation of the description. The translation is in the language specified in the Language request parameter.",
        ),
    ]


"""
ReturnAuthorization

Return authorization information for items accepted for return.
"""


class ReturnAuthorization(SpApiBaseModel):
    """Return authorization information for items accepted for return."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    return_authorization_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices(
                "returnAuthorizationId", "return_authorization_id"
            ),
            serialization_alias="returnAuthorizationId",
            description="An identifier for the return authorization. This identifier associates return items with the return authorization used to return them.",
        ),
    ]

    fulfillment_center_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices(
                "fulfillmentCenterId", "fulfillment_center_id"
            ),
            serialization_alias="fulfillmentCenterId",
            description="An identifier for the Amazon fulfillment center that the return items should be sent to.",
        ),
    ]

    return_to_address: Annotated[
        "Address",
        Field(
            ...,
            validation_alias=AliasChoices("returnToAddress", "return_to_address"),
            serialization_alias="returnToAddress",
            description="The address of the Amazon fulfillment center that the return items should be sent to.",
        ),
    ]

    amazon_rma_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("amazonRmaId", "amazon_rma_id"),
            serialization_alias="amazonRmaId",
            description="The return merchandise authorization (RMA) that Amazon needs to process the return.",
        ),
    ]

    rma_page_u_r_l: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("rmaPageURL", "rma_page_u_r_l"),
            serialization_alias="rmaPageURL",
            description="A URL for a web page that contains the return authorization barcode and the mailing label. This does not include pre-paid shipping.",
        ),
    ]


ReturnItemDisposition = str
"""The condition of the return item when received by an Amazon fulfillment center."""


"""
ReturnItem

An item that Amazon accepted for return.
"""


class ReturnItem(SpApiBaseModel):
    """An item that Amazon accepted for return."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    seller_return_item_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices(
                "sellerReturnItemId", "seller_return_item_id"
            ),
            serialization_alias="sellerReturnItemId",
            description="An identifier assigned by the seller to the return item.",
        ),
    ]

    seller_fulfillment_order_item_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices(
                "sellerFulfillmentOrderItemId", "seller_fulfillment_order_item_id"
            ),
            serialization_alias="sellerFulfillmentOrderItemId",
            description="The identifier assigned to the item by the seller when the fulfillment order was created.",
        ),
    ]

    amazon_shipment_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("amazonShipmentId", "amazon_shipment_id"),
            serialization_alias="amazonShipmentId",
            description="The identifier for the shipment that is associated with the return item.",
        ),
    ]

    seller_return_reason_code: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices(
                "sellerReturnReasonCode", "seller_return_reason_code"
            ),
            serialization_alias="sellerReturnReasonCode",
            description="The return reason code assigned to the return item by the seller.",
        ),
    ]

    return_comment: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("returnComment", "return_comment"),
            serialization_alias="returnComment",
            description="An optional comment about the return item.",
        ),
    ]

    amazon_return_reason_code: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "amazonReturnReasonCode", "amazon_return_reason_code"
            ),
            serialization_alias="amazonReturnReasonCode",
            description="The return reason code that the Amazon fulfillment center assigned to the return item.",
        ),
    ]

    status: Annotated[
        "FulfillmentReturnItemStatus",
        Field(
            ...,
            description="Indicates if the return item has been processed by an Amazon fulfillment center.",
        ),
    ]

    status_changed_date: Annotated[
        "Timestamp",
        Field(
            ...,
            validation_alias=AliasChoices("statusChangedDate", "status_changed_date"),
            serialization_alias="statusChangedDate",
            description="Indicates when the status last changed.",
        ),
    ]

    return_authorization_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "returnAuthorizationId", "return_authorization_id"
            ),
            serialization_alias="returnAuthorizationId",
            description="Identifies the return authorization used to return this item. Refer to `ReturnAuthorization`.",
        ),
    ]

    return_received_condition: Annotated[
        Optional["ReturnItemDisposition"],
        Field(
            None,
            validation_alias=AliasChoices(
                "returnReceivedCondition", "return_received_condition"
            ),
            serialization_alias="returnReceivedCondition",
        ),
    ]

    fulfillment_center_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "fulfillmentCenterId", "fulfillment_center_id"
            ),
            serialization_alias="fulfillmentCenterId",
            description="The identifier for the Amazon fulfillment center that processed the return item.",
        ),
    ]


"""
SubmitFulfillmentOrderStatusUpdateRequestBody

The request body schema for the `submitFulfillmentOrderStatusUpdate` operation.
"""


class SubmitFulfillmentOrderStatusUpdateRequestBody(SpApiBaseModel):
    """The request body schema for the `submitFulfillmentOrderStatusUpdate` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    fulfillment_order_status: Annotated[
        Optional["FulfillmentOrderStatus"],
        Field(
            None,
            validation_alias=AliasChoices(
                "fulfillmentOrderStatus", "fulfillment_order_status"
            ),
            serialization_alias="fulfillmentOrderStatus",
        ),
    ]


"""
SubmitFulfillmentOrderStatusUpdateRequest

Request parameters for submitFulfillmentOrderStatusUpdate
"""


class SubmitFulfillmentOrderStatusUpdateRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for submitFulfillmentOrderStatusUpdate
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    seller_fulfillment_order_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices(
                "sellerFulfillmentOrderId", "seller_fulfillment_order_id"
            ),
            serialization_alias="sellerFulfillmentOrderId",
            description="[PATH] The identifier assigned to the item by the seller when the fulfillment order was created.",
        ),
    ]

    body: Annotated[
        "SubmitFulfillmentOrderStatusUpdateRequestBody",
        BodyParam(),
        Field(
            ...,
            description="[BODY] The identifier assigned to the item by the seller when the fulfillment order was created.",
        ),
    ]


"""
SubmitFulfillmentOrderStatusUpdateResponse

The response schema for the `SubmitFulfillmentOrderStatusUpdate` operation.
"""


class SubmitFulfillmentOrderStatusUpdateResponse(SpApiBaseModel):
    """The response schema for the `SubmitFulfillmentOrderStatusUpdate` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
            description="One or more unexpected errors occurred during the `SubmitFulfillmentOrderStatusUpdate` operation.",
        ),
    ]


"""
TrackingEvent

Information for tracking package deliveries.
"""


class TrackingEvent(SpApiBaseModel):
    """Information for tracking package deliveries."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    event_date: Annotated[
        "Timestamp",
        Field(
            ...,
            validation_alias=AliasChoices("eventDate", "event_date"),
            serialization_alias="eventDate",
            description="The date and time that the delivery event took place. Must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format.",
        ),
    ]

    event_address: Annotated[
        "TrackingAddress",
        Field(
            ...,
            validation_alias=AliasChoices("eventAddress", "event_address"),
            serialization_alias="eventAddress",
            description="The city where the delivery event took place.",
        ),
    ]

    event_code: Annotated[
        "EventCode",
        Field(
            ...,
            validation_alias=AliasChoices("eventCode", "event_code"),
            serialization_alias="eventCode",
            description="The event code for the delivery event.",
        ),
    ]

    event_description: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("eventDescription", "event_description"),
            serialization_alias="eventDescription",
            description="A description for the corresponding event code.",
        ),
    ]


"""
UnfulfillablePreviewItem

Information about unfulfillable items in a fulfillment order preview.
"""


class UnfulfillablePreviewItem(SpApiBaseModel):
    """Information about unfulfillable items in a fulfillment order preview."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    seller_sku: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("sellerSku", "seller_sku"),
            serialization_alias="sellerSku",
            description="The seller SKU of the item.",
        ),
    ]

    quantity: Annotated[
        "Quantity",
        Field(
            ...,
        ),
    ]

    seller_fulfillment_order_item_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices(
                "sellerFulfillmentOrderItemId", "seller_fulfillment_order_item_id"
            ),
            serialization_alias="sellerFulfillmentOrderItemId",
            description="A fulfillment order item identifier created with a call to the `getFulfillmentPreview` operation.",
        ),
    ]

    item_unfulfillable_reasons: Annotated[
        Optional["StringList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "itemUnfulfillableReasons", "item_unfulfillable_reasons"
            ),
            serialization_alias="itemUnfulfillableReasons",
            description="Error codes associated with the fulfillment order preview that indicate why the item is unfulfillable.",
        ),
    ]


"""
UpdateFulfillmentOrderItem

Item information for updating a fulfillment order.
"""


class UpdateFulfillmentOrderItem(SpApiBaseModel):
    """Item information for updating a fulfillment order."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    seller_sku: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("sellerSku", "seller_sku"),
            serialization_alias="sellerSku",
            description="The seller SKU of the item.",
        ),
    ]

    seller_fulfillment_order_item_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices(
                "sellerFulfillmentOrderItemId", "seller_fulfillment_order_item_id"
            ),
            serialization_alias="sellerFulfillmentOrderItemId",
            description="Identifies the fulfillment order item to update. Created with a previous call to the createFulfillmentOrder operation.",
        ),
    ]

    quantity: Annotated[
        "Quantity",
        Field(
            ...,
        ),
    ]

    gift_message: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("giftMessage", "gift_message"),
            serialization_alias="giftMessage",
            description="A message to the gift recipient, if applicable.",
        ),
    ]

    displayable_comment: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("displayableComment", "displayable_comment"),
            serialization_alias="displayableComment",
            description="Item-specific text that displays in recipient-facing materials such as the outbound shipment packing slip.",
        ),
    ]

    fulfillment_network_sku: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "fulfillmentNetworkSku", "fulfillment_network_sku"
            ),
            serialization_alias="fulfillmentNetworkSku",
            description="Amazon's fulfillment network SKU of the item.",
        ),
    ]

    order_item_disposition: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "orderItemDisposition", "order_item_disposition"
            ),
            serialization_alias="orderItemDisposition",
            description="Indicates whether the item is sellable or unsellable.",
        ),
    ]

    per_unit_declared_value: Annotated[
        Optional["Money"],
        Field(
            None,
            validation_alias=AliasChoices(
                "perUnitDeclaredValue", "per_unit_declared_value"
            ),
            serialization_alias="perUnitDeclaredValue",
            description="The monetary value assigned by the seller to this item. This is a required field for India MCF orders.",
        ),
    ]

    per_unit_price: Annotated[
        Optional["Money"],
        Field(
            None,
            validation_alias=AliasChoices("perUnitPrice", "per_unit_price"),
            serialization_alias="perUnitPrice",
            description="The amount to be collected from the recipient for this item in a COD (Cash On Delivery) order.",
        ),
    ]

    per_unit_tax: Annotated[
        Optional["Money"],
        Field(
            None,
            validation_alias=AliasChoices("perUnitTax", "per_unit_tax"),
            serialization_alias="perUnitTax",
            description="The tax on the amount to be collected from the recipient for this item in a COD (Cash On Delivery) order.",
        ),
    ]


UpdateFulfillmentOrderItemList = List["UpdateFulfillmentOrderItem"]
"""An array of fulfillment order item information for updating a fulfillment order."""


"""
UpdateFulfillmentOrderRequestBody

The request body schema for the `updateFulfillmentOrder` operation.
"""


class UpdateFulfillmentOrderRequestBody(SpApiBaseModel):
    """The request body schema for the `updateFulfillmentOrder` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    marketplace_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="The marketplace the fulfillment order is placed against.",
        ),
    ]

    displayable_order_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("displayableOrderId", "displayable_order_id"),
            serialization_alias="displayableOrderId",
            description="A fulfillment order identifier that the seller creates. This value displays as the order identifier in recipient-facing materials such as the outbound shipment packing slip. The value of `DisplayableOrderId` should match the order identifier that the seller provides to the recipient. The seller can use the `SellerFulfillmentOrderId` for this value or they can specify an alternate value if they want the recipient to reference an alternate order identifier.",
        ),
    ]

    displayable_order_date: Annotated[
        Optional["Timestamp"],
        Field(
            None,
            validation_alias=AliasChoices(
                "displayableOrderDate", "displayable_order_date"
            ),
            serialization_alias="displayableOrderDate",
            description="The date and time of the fulfillment order. Displays as the order date in recipient-facing materials such as the outbound shipment packing slip.",
        ),
    ]

    displayable_order_comment: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "displayableOrderComment", "displayable_order_comment"
            ),
            serialization_alias="displayableOrderComment",
            description="Order-specific text that appears in recipient-facing materials such as the outbound shipment packing slip.",
        ),
    ]

    shipping_speed_category: Annotated[
        Optional["ShippingSpeedCategory"],
        Field(
            None,
            validation_alias=AliasChoices(
                "shippingSpeedCategory", "shipping_speed_category"
            ),
            serialization_alias="shippingSpeedCategory",
        ),
    ]

    destination_address: Annotated[
        Optional["Address"],
        Field(
            None,
            validation_alias=AliasChoices("destinationAddress", "destination_address"),
            serialization_alias="destinationAddress",
            description="The destination address for the fulfillment order.",
        ),
    ]

    fulfillment_action: Annotated[
        Optional["FulfillmentAction"],
        Field(
            None,
            validation_alias=AliasChoices("fulfillmentAction", "fulfillment_action"),
            serialization_alias="fulfillmentAction",
        ),
    ]

    fulfillment_policy: Annotated[
        Optional["FulfillmentPolicy"],
        Field(
            None,
            validation_alias=AliasChoices("fulfillmentPolicy", "fulfillment_policy"),
            serialization_alias="fulfillmentPolicy",
        ),
    ]

    ship_from_country_code: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "shipFromCountryCode", "ship_from_country_code"
            ),
            serialization_alias="shipFromCountryCode",
            description="The two-character country code for the country from which the fulfillment order ships. Must be in ISO 3166-1 alpha-2 format.",
        ),
    ]

    notification_emails: Annotated[
        Optional["NotificationEmailList"],
        Field(
            None,
            validation_alias=AliasChoices("notificationEmails", "notification_emails"),
            serialization_alias="notificationEmails",
        ),
    ]

    feature_constraints: Annotated[
        Optional[List["FeatureSettings"]],
        Field(
            None,
            validation_alias=AliasChoices("featureConstraints", "feature_constraints"),
            serialization_alias="featureConstraints",
            description="A list of features and their fulfillment policies to apply to the order.",
        ),
    ]

    items: Annotated[
        Optional["UpdateFulfillmentOrderItemList"],
        Field(
            None,
            description="A list of items to include in the fulfillment order preview, including quantity.",
        ),
    ]


"""
UpdateFulfillmentOrderRequest

Request parameters for updateFulfillmentOrder
"""


class UpdateFulfillmentOrderRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for updateFulfillmentOrder
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    body: Annotated[
        "UpdateFulfillmentOrderRequestBody",
        BodyParam(),
        Field(..., description="[BODY] UpdateFulfillmentOrderRequestBody parameter"),
    ]

    seller_fulfillment_order_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices(
                "sellerFulfillmentOrderId", "seller_fulfillment_order_id"
            ),
            serialization_alias="sellerFulfillmentOrderId",
            description="[PATH] The identifier assigned to the item by the seller when the fulfillment order was created.",
        ),
    ]


"""
UpdateFulfillmentOrderResponse

The response schema for the `updateFulfillmentOrder` operation.
"""


class UpdateFulfillmentOrderResponse(SpApiBaseModel):
    """The response schema for the `updateFulfillmentOrder` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
            description="One or more unexpected errors occurred during the `updateFulfillmentOrder` operation.",
        ),
    ]


# Rebuild models to resolve forward references
Error.model_rebuild()
Address.model_rebuild()
CODSettings.model_rebuild()
CreateFulfillmentOrderItem.model_rebuild()
CreateFulfillmentOrderRequestBody.model_rebuild()
CreateFulfillmentReturnRequestBody.model_rebuild()
CreateFulfillmentReturnResult.model_rebuild()
CreateFulfillmentReturnResponse.model_rebuild()
CreateReturnItem.model_rebuild()
Money.model_rebuild()
DeliveryWindow.model_rebuild()
DeliveryPreferences.model_rebuild()
DropOffLocation.model_rebuild()
Fee.model_rebuild()
FulfillmentOrder.model_rebuild()
FulfillmentOrderItem.model_rebuild()
FulfillmentPreview.model_rebuild()
FulfillmentPreviewItem.model_rebuild()
FulfillmentPreviewShipment.model_rebuild()
FulfillmentShipment.model_rebuild()
FulfillmentShipmentItem.model_rebuild()
FulfillmentShipmentPackage.model_rebuild()
GetFulfillmentOrderResult.model_rebuild()
GetFulfillmentOrderResponse.model_rebuild()
GetFulfillmentPreviewItem.model_rebuild()
GetFulfillmentPreviewRequestBody.model_rebuild()
GetFulfillmentPreviewResult.model_rebuild()
GetFulfillmentPreviewResponse.model_rebuild()
GetDeliveryOffersRequestBody.model_rebuild()
GetDeliveryOffersResponse.model_rebuild()
GetDeliveryOffersResult.model_rebuild()
DeliveryOffer.model_rebuild()
GetDeliveryOffersProduct.model_rebuild()
Amount.model_rebuild()
GetDeliveryOffersTerms.model_rebuild()
Destination.model_rebuild()
ProductIdentifier.model_rebuild()
Origin.model_rebuild()
VariablePrecisionAddress.model_rebuild()
DateRange.model_rebuild()
DeliveryPolicy.model_rebuild()
DeliveryMessage.model_rebuild()
InvalidItemReason.model_rebuild()
InvalidReturnItem.model_rebuild()
ListAllFulfillmentOrdersResult.model_rebuild()
ListAllFulfillmentOrdersResponse.model_rebuild()
ListReturnReasonCodesResult.model_rebuild()
ListReturnReasonCodesResponse.model_rebuild()
LockerDetails.model_rebuild()
DeliveryInformation.model_rebuild()
DeliveryDocument.model_rebuild()
NotificationEmailList.model_rebuild()
PackageTrackingDetails.model_rebuild()
GetPackageTrackingDetailsResponse.model_rebuild()
ReasonCodeDetails.model_rebuild()
PaymentInformation.model_rebuild()
ReturnAuthorization.model_rebuild()
ReturnItem.model_rebuild()
ScheduledDeliveryInfo.model_rebuild()
StringList.model_rebuild()
TrackingAddress.model_rebuild()
TrackingEvent.model_rebuild()
UnfulfillablePreviewItem.model_rebuild()
UpdateFulfillmentOrderItem.model_rebuild()
UpdateFulfillmentOrderRequestBody.model_rebuild()
UpdateFulfillmentOrderResponse.model_rebuild()
CreateFulfillmentOrderResponse.model_rebuild()
CancelFulfillmentOrderResponse.model_rebuild()
Weight.model_rebuild()
GetFeatureInventoryResponse.model_rebuild()
GetFeatureInventoryResult.model_rebuild()
FeatureSku.model_rebuild()
GetFeaturesResponse.model_rebuild()
GetFeaturesResult.model_rebuild()
Feature.model_rebuild()
GetFeatureSkuResponse.model_rebuild()
GetFeatureSkuResult.model_rebuild()
FeatureSettings.model_rebuild()
SubmitFulfillmentOrderStatusUpdateRequestBody.model_rebuild()
SubmitFulfillmentOrderStatusUpdateResponse.model_rebuild()
GetFulfillmentPreviewRequest.model_rebuild()
DeliveryOffersRequest.model_rebuild()
ListAllFulfillmentOrdersRequest.model_rebuild()
CreateFulfillmentOrderRequest.model_rebuild()
GetPackageTrackingDetailsRequest.model_rebuild()
ListReturnReasonCodesRequest.model_rebuild()
CreateFulfillmentReturnRequest.model_rebuild()
GetFulfillmentOrderRequest.model_rebuild()
UpdateFulfillmentOrderRequest.model_rebuild()
CancelFulfillmentOrderRequest.model_rebuild()
SubmitFulfillmentOrderStatusUpdateRequest.model_rebuild()
GetFeaturesRequest.model_rebuild()
GetFeatureInventoryRequest.model_rebuild()
GetFeatureSKURequest.model_rebuild()
