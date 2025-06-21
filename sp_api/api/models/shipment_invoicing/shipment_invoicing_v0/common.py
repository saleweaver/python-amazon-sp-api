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

AddressTypeEnum = str
"""The shipping address type."""


"""
Address

The shipping address details of the shipment.
"""


class Address(SpApiBaseModel):
    """The shipping address details of the shipment."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    name: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("Name", "name"),
            serialization_alias="Name",
            description="The name.",
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
            description="The country code.",
        ),
    ]

    phone: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("Phone", "phone"),
            serialization_alias="Phone",
            description="The phone number.",
        ),
    ]

    address_type: Annotated[
        Optional["AddressTypeEnum"],
        Field(
            None,
            validation_alias=AliasChoices("AddressType", "address_type"),
            serialization_alias="AddressType",
        ),
    ]


Blob = str
"""Shipment invoice document content."""


TaxClassificationList = List["TaxClassification"]
"""The list of tax classifications."""


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
        Optional["TaxClassificationList"],
        Field(
            None,
            validation_alias=AliasChoices("TaxClassifications", "tax_classifications"),
            serialization_alias="TaxClassifications",
        ),
    ]


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


ErrorList = List["Error"]
"""A list of error responses returned when a request is unsuccessful."""


"""
GetInvoiceStatusRequest

Request parameters for getInvoiceStatus
"""


class GetInvoiceStatusRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getInvoiceStatus
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
            description="[PATH] The shipment identifier for the shipment.",
        ),
    ]


ShipmentInvoiceStatus = str
"""The shipment invoice status."""


"""
ShipmentInvoiceStatusInfo

The shipment invoice status information.
"""


class ShipmentInvoiceStatusInfo(SpApiBaseModel):
    """The shipment invoice status information."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    amazon_shipment_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("AmazonShipmentId", "amazon_shipment_id"),
            serialization_alias="AmazonShipmentId",
            description="The Amazon-defined shipment identifier.",
        ),
    ]

    invoice_status: Annotated[
        Optional["ShipmentInvoiceStatus"],
        Field(
            None,
            validation_alias=AliasChoices("InvoiceStatus", "invoice_status"),
            serialization_alias="InvoiceStatus",
        ),
    ]


"""
ShipmentInvoiceStatusResponse

The shipment invoice status response.
"""


class ShipmentInvoiceStatusResponse(SpApiBaseModel):
    """The shipment invoice status response."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    shipments: Annotated[
        Optional["ShipmentInvoiceStatusInfo"],
        Field(
            None,
            validation_alias=AliasChoices("Shipments", "shipments"),
            serialization_alias="Shipments",
        ),
    ]


"""
GetInvoiceStatusResponse

The response schema for the getInvoiceStatus operation.
"""


class GetInvoiceStatusResponse(SpApiBaseModel):
    """The response schema for the getInvoiceStatus operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["ShipmentInvoiceStatusResponse"],
        Field(None, description="The payload for the getInvoiceStatus operation."),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
        ),
    ]


"""
GetShipmentDetailsRequest

Request parameters for getShipmentDetails
"""


class GetShipmentDetailsRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getShipmentDetails
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
            description="[PATH] The identifier for the shipment. Get this value from the FBAOutboundShipmentStatus notification. For information about subscribing to notifications, see the [Notifications API Use Case Guide](doc:notifications-api-v1-use-case-guide).",
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
        Optional["TaxClassificationList"],
        Field(
            None,
            validation_alias=AliasChoices("TaxClassifications", "tax_classifications"),
            serialization_alias="TaxClassifications",
        ),
    ]


"""
PaymentMethodDetailItemList

The list of payment method details.
"""


class PaymentMethodDetailItemList(SpApiBaseModel):
    """The list of payment method details."""

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow",
        serialize_by_alias=True,
        arbitrary_types_allowed=True,
    )


ShipmentItems = List["ShipmentItem"]
"""A list of shipment items."""


"""
ShipmentDetail

The information required by a selling partner to issue a shipment invoice.
"""


class ShipmentDetail(SpApiBaseModel):
    """The information required by a selling partner to issue a shipment invoice."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    warehouse_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("WarehouseId", "warehouse_id"),
            serialization_alias="WarehouseId",
            description="The Amazon-defined identifier for the warehouse.",
        ),
    ]

    amazon_order_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("AmazonOrderId", "amazon_order_id"),
            serialization_alias="AmazonOrderId",
            description="The Amazon-defined identifier for the order.",
        ),
    ]

    amazon_shipment_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("AmazonShipmentId", "amazon_shipment_id"),
            serialization_alias="AmazonShipmentId",
            description="The Amazon-defined identifier for the shipment.",
        ),
    ]

    purchase_date: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices("PurchaseDate", "purchase_date"),
            serialization_alias="PurchaseDate",
            description="The date and time when the order was created.",
        ),
    ]

    shipping_address: Annotated[
        Optional["Address"],
        Field(
            None,
            validation_alias=AliasChoices("ShippingAddress", "shipping_address"),
            serialization_alias="ShippingAddress",
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

    seller_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("SellerId", "seller_id"),
            serialization_alias="SellerId",
            description="The seller identifier.",
        ),
    ]

    buyer_name: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("BuyerName", "buyer_name"),
            serialization_alias="BuyerName",
            description="The name of the buyer.",
        ),
    ]

    buyer_county: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("BuyerCounty", "buyer_county"),
            serialization_alias="BuyerCounty",
            description="The county of the buyer.",
        ),
    ]

    buyer_tax_info: Annotated[
        Optional["BuyerTaxInfo"],
        Field(
            None,
            validation_alias=AliasChoices("BuyerTaxInfo", "buyer_tax_info"),
            serialization_alias="BuyerTaxInfo",
        ),
    ]

    marketplace_tax_info: Annotated[
        Optional["MarketplaceTaxInfo"],
        Field(
            None,
            validation_alias=AliasChoices("MarketplaceTaxInfo", "marketplace_tax_info"),
            serialization_alias="MarketplaceTaxInfo",
        ),
    ]

    seller_display_name: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("SellerDisplayName", "seller_display_name"),
            serialization_alias="SellerDisplayName",
            description="The seller’s friendly name registered in the marketplace.",
        ),
    ]

    shipment_items: Annotated[
        Optional["ShipmentItems"],
        Field(
            None,
            validation_alias=AliasChoices("ShipmentItems", "shipment_items"),
            serialization_alias="ShipmentItems",
        ),
    ]


"""
GetShipmentDetailsResponse

The response schema for the getShipmentDetails operation.
"""


class GetShipmentDetailsResponse(SpApiBaseModel):
    """The response schema for the getShipmentDetails operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["ShipmentDetail"],
        Field(None, description="The payload for the getShipmentDetails operation"),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
        ),
    ]


"""
Money

The currency type and amount.
"""


class Money(SpApiBaseModel):
    """The currency type and amount."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    currency_code: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("CurrencyCode", "currency_code"),
            serialization_alias="CurrencyCode",
            description="Three-digit currency code in ISO 4217 format.",
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
SerialNumbersList

The list of serial numbers.
"""


class SerialNumbersList(SpApiBaseModel):
    """The list of serial numbers."""

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow",
        serialize_by_alias=True,
        arbitrary_types_allowed=True,
    )


"""
ShipmentItem

The shipment item information required by a seller to issue a shipment invoice.
"""


class ShipmentItem(SpApiBaseModel):
    """The shipment item information required by a seller to issue a shipment invoice."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    a_s_i_n: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("ASIN", "a_s_i_n"),
            serialization_alias="ASIN",
            description="The Amazon Standard Identification Number (ASIN) of the item.",
        ),
    ]

    seller_s_k_u: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("SellerSKU", "seller_s_k_u"),
            serialization_alias="SellerSKU",
            description="The seller SKU of the item.",
        ),
    ]

    order_item_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("OrderItemId", "order_item_id"),
            serialization_alias="OrderItemId",
            description="The Amazon-defined identifier for the order item.",
        ),
    ]

    title: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("Title", "title"),
            serialization_alias="Title",
            description="The name of the item.",
        ),
    ]

    quantity_ordered: Annotated[
        Optional[float],
        Field(
            None,
            validation_alias=AliasChoices("QuantityOrdered", "quantity_ordered"),
            serialization_alias="QuantityOrdered",
            description="The number of items ordered.",
        ),
    ]

    item_price: Annotated[
        Optional["Money"],
        Field(
            None,
            validation_alias=AliasChoices("ItemPrice", "item_price"),
            serialization_alias="ItemPrice",
            description="The selling price of the item multiplied by the quantity ordered. Note that ItemPrice excludes ShippingPrice and GiftWrapPrice.",
        ),
    ]

    shipping_price: Annotated[
        Optional["Money"],
        Field(
            None,
            validation_alias=AliasChoices("ShippingPrice", "shipping_price"),
            serialization_alias="ShippingPrice",
            description="The shipping price of the item.",
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

    shipping_discount: Annotated[
        Optional["Money"],
        Field(
            None,
            validation_alias=AliasChoices("ShippingDiscount", "shipping_discount"),
            serialization_alias="ShippingDiscount",
            description="The discount on the shipping price.",
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

    serial_numbers: Annotated[
        Optional["SerialNumbersList"],
        Field(
            None,
            validation_alias=AliasChoices("SerialNumbers", "serial_numbers"),
            serialization_alias="SerialNumbers",
            description="The list of serial numbers.",
        ),
    ]


"""
SubmitInvoiceRequestBody

The request schema for the submitInvoice operation.
"""


class SubmitInvoiceRequestBody(SpApiBaseModel):
    """The request schema for the submitInvoice operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    invoice_content: Annotated[
        "Blob",
        Field(
            ...,
            validation_alias=AliasChoices("InvoiceContent", "invoice_content"),
            serialization_alias="InvoiceContent",
        ),
    ]

    marketplace_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("MarketplaceId", "marketplace_id"),
            serialization_alias="MarketplaceId",
            description="An Amazon marketplace identifier.",
        ),
    ]

    content_m_d5_value: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("ContentMD5Value", "content_m_d5_value"),
            serialization_alias="ContentMD5Value",
            description="MD5 sum for validating the invoice data. For more information about calculating this value, see [Working with Content-MD5 Checksums](https://docs.developer.amazonservices.com/en_US/dev_guide/DG_MD5.html).",
        ),
    ]


"""
SubmitInvoiceRequest

Request parameters for submitInvoice
"""


class SubmitInvoiceRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for submitInvoice
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
            description="[PATH] The identifier for the shipment.",
        ),
    ]

    body: Annotated[
        "SubmitInvoiceRequestBody",
        BodyParam(),
        Field(..., description="[BODY] Parameter"),
    ]


"""
SubmitInvoiceResponse

The response schema for the submitInvoice operation.
"""


class SubmitInvoiceResponse(SpApiBaseModel):
    """The response schema for the submitInvoice operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
        ),
    ]


"""
TaxClassification

The tax classification for the entity.
"""


class TaxClassification(SpApiBaseModel):
    """The tax classification for the entity."""

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
            description="The entity's tax identifier.",
        ),
    ]


# Rebuild models to resolve forward references
GetShipmentDetailsResponse.model_rebuild()
ShipmentDetail.model_rebuild()
Address.model_rebuild()
PaymentMethodDetailItemList.model_rebuild()
BuyerTaxInfo.model_rebuild()
MarketplaceTaxInfo.model_rebuild()
TaxClassification.model_rebuild()
ShipmentItem.model_rebuild()
Money.model_rebuild()
SerialNumbersList.model_rebuild()
Error.model_rebuild()
SubmitInvoiceRequestBody.model_rebuild()
SubmitInvoiceResponse.model_rebuild()
ShipmentInvoiceStatusInfo.model_rebuild()
ShipmentInvoiceStatusResponse.model_rebuild()
GetInvoiceStatusResponse.model_rebuild()
GetShipmentDetailsRequest.model_rebuild()
SubmitInvoiceRequest.model_rebuild()
GetInvoiceStatusRequest.model_rebuild()
