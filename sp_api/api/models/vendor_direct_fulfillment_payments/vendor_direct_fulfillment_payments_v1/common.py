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


# Enum definitions
class TypeEnum(str, Enum):
    """Enum for type"""

    SUR = "SUR"  # An additional tax on something already taxed, such as a higher rate of tax on incomes above a certain level.
    OCR = "OCR"  # OCR.


"""
AdditionalDetails

A field where the selling party can provide additional information for tax-related or any other purposes.
"""


class AdditionalDetails(SpApiBaseModel):
    """A field where the selling party can provide additional information for tax-related or any other purposes."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    type: Annotated[
        TypeEnum,
        Field(
            ...,
            description="The type of the additional information provided by the selling party.",
        ),
    ]

    detail: Annotated[
        str,
        Field(
            ...,
            description="The detail of the additional information provided by the selling party.",
        ),
    ]

    language_code: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("languageCode", "language_code"),
            serialization_alias="languageCode",
            description="The language code of the additional information detail.",
        ),
    ]


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
        str,
        Field(
            ...,
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
        str,
        Field(
            ...,
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
class TaxTypeEnum(str, Enum):
    """Enum for taxType"""

    CGST = "CGST"  # Central Goods and Services Tax (CGST) is levied by the Indian government for intrastate movement of goods and services.
    SGST = "SGST"  # State Goods and Services Tax (SGST) is an indirect tax levied and collected by a State Government in India on the intra-state supplies.
    CESS = "CESS"  # A cess is a form of tax levied by the government on tax with specific purposes till the time the government gets enough money for that purpose.
    UTGST = "UTGST"  # Union Territory Goods and Services Tax in India.
    IGST = "IGST"  # Integrated Goods and Services Tax (IGST) is a tax levied on all Inter-State supplies of goods and/or services in India.
    MW_ST_ = "MwSt."  # Mehrwertsteuer, MwSt, is the German for value-added tax.
    PST = "PST"  # A provincial sales tax (PST) is imposed on consumers of goods and particular services in many Canadian provinces.
    TVA = "TVA"  # Taxe sur la Valeur Ajout&#233;e (TVA) is French for Value-added tax.
    VAT = "VAT"  # Value-added tax.
    GST = "GST"  # Tax levied on most goods and services sold for domestic consumption.
    ST = "ST"  # Sales tax.
    CONSUMPTION = (
        "Consumption"  # Tax levied on consumption spending on goods and services.
    )
    MUTUALLY_DEFINED = "MutuallyDefined"  # Tax component that was mutually agreed upon between Amazon and vendor.
    DOMESTIC_VAT = "DomesticVAT"  # Domestic Value-added tax.


"""
TaxDetail

Details of tax amount applied.
"""


class TaxDetail(SpApiBaseModel):
    """Details of tax amount applied."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    tax_type: Annotated[
        TaxTypeEnum,
        Field(
            ...,
            validation_alias=AliasChoices("taxType", "tax_type"),
            serialization_alias="taxType",
            description="Type of the tax applied.",
        ),
    ]

    tax_rate: Annotated[
        Optional["Decimal"],
        Field(
            None,
            validation_alias=AliasChoices("taxRate", "tax_rate"),
            serialization_alias="taxRate",
            description="Tax percentage applied. Percentage must be expressed in decimal.",
        ),
    ]

    tax_amount: Annotated[
        "Money",
        Field(
            ...,
            validation_alias=AliasChoices("taxAmount", "tax_amount"),
            serialization_alias="taxAmount",
            description="Total tax amount applied on invoice total or an item total.",
        ),
    ]

    taxable_amount: Annotated[
        Optional["Money"],
        Field(
            None,
            validation_alias=AliasChoices("taxableAmount", "taxable_amount"),
            serialization_alias="taxableAmount",
            description="This field will contain the invoice amount that is taxable at the rate specified in the tax rate field.",
        ),
    ]


# Enum definitions
class TypeEnum(str, Enum):
    """Enum for type"""

    SUR = "SUR"  # An additional tax on something already taxed, such as a higher rate of tax on incomes above a certain level.
    OCR = "OCR"  # OCR.


"""
ChargeDetails

Monetary and tax details of the charge.
"""


class ChargeDetails(SpApiBaseModel):
    """Monetary and tax details of the charge."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    type: Annotated[TypeEnum, Field(..., description="Type of charge applied.")]

    charge_amount: Annotated[
        "Money",
        Field(
            ...,
            validation_alias=AliasChoices("chargeAmount", "charge_amount"),
            serialization_alias="chargeAmount",
        ),
    ]

    tax_details: Annotated[
        Optional[List["TaxDetail"]],
        Field(
            None,
            validation_alias=AliasChoices("taxDetails", "tax_details"),
            serialization_alias="taxDetails",
            description="Individual tax details per line item.",
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
        int, Field(..., description="Quantity of units available for a specific item.")
    ]

    unit_of_measure: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("unitOfMeasure", "unit_of_measure"),
            serialization_alias="unitOfMeasure",
            description="Unit of measure for the available quantity.",
        ),
    ]


"""
InvoiceItem

Provides the details of the items in this invoice.
"""


class InvoiceItem(SpApiBaseModel):
    """Provides the details of the items in this invoice."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    item_sequence_number: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("itemSequenceNumber", "item_sequence_number"),
            serialization_alias="itemSequenceNumber",
            description="Numbering of the item on the purchase order. The first item will be 1, the second 2, and so on.",
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
            description="Buyer's standard identification number (ASIN) of an item.",
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
            description="The vendor selected product identification of the item.",
        ),
    ]

    invoiced_quantity: Annotated[
        "ItemQuantity",
        Field(
            ...,
            validation_alias=AliasChoices("invoicedQuantity", "invoiced_quantity"),
            serialization_alias="invoicedQuantity",
            description="Item quantity invoiced.",
        ),
    ]

    net_cost: Annotated[
        "Money",
        Field(
            ...,
            validation_alias=AliasChoices("netCost", "net_cost"),
            serialization_alias="netCost",
            description="Net price (before tax) to vendor with currency details.",
        ),
    ]

    purchase_order_number: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices(
                "purchaseOrderNumber", "purchase_order_number"
            ),
            serialization_alias="purchaseOrderNumber",
            description="The purchase order number for this order. Formatting Notes: 8-character alpha-numeric code.",
        ),
    ]

    vendor_order_number: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("vendorOrderNumber", "vendor_order_number"),
            serialization_alias="vendorOrderNumber",
            description="The vendor's order number for this order.",
        ),
    ]

    hsn_code: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("hsnCode", "hsn_code"),
            serialization_alias="hsnCode",
            description="Harmonized System of Nomenclature (HSN) tax code. The HSN number cannot contain alphabets.",
        ),
    ]

    tax_details: Annotated[
        Optional[List["TaxDetail"]],
        Field(
            None,
            validation_alias=AliasChoices("taxDetails", "tax_details"),
            serialization_alias="taxDetails",
            description="Individual tax details per line item.",
        ),
    ]

    charge_details: Annotated[
        Optional[List["ChargeDetails"]],
        Field(
            None,
            validation_alias=AliasChoices("chargeDetails", "charge_details"),
            serialization_alias="chargeDetails",
            description="Individual charge details per line item.",
        ),
    ]


# Enum definitions
class TaxRegistrationTypeEnum(str, Enum):
    """Enum for taxRegistrationType"""

    VAT = "VAT"  # Value-added tax.
    GST = "GST"  # Goods and Services tax.


"""
TaxRegistrationDetail

Tax registration details of the entity.
"""


class TaxRegistrationDetail(SpApiBaseModel):
    """Tax registration details of the entity."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    tax_registration_type: Annotated[
        Optional[TaxRegistrationTypeEnum],
        Field(
            None,
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
            description="Tax registration number for the entity. For example, VAT ID, Consumption Tax ID.",
        ),
    ]

    tax_registration_address: Annotated[
        Optional["Address"],
        Field(
            None,
            validation_alias=AliasChoices(
                "taxRegistrationAddress", "tax_registration_address"
            ),
            serialization_alias="taxRegistrationAddress",
            description="Address associated with the tax registration number.",
        ),
    ]

    tax_registration_message: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "taxRegistrationMessage", "tax_registration_message"
            ),
            serialization_alias="taxRegistrationMessage",
            description="Tax registration message that can be used for additional tax related details.",
        ),
    ]


"""
PartyIdentification

Name, address and tax details of a party.
"""


class PartyIdentification(SpApiBaseModel):
    """Name, address and tax details of a party."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    party_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("partyId", "party_id"),
            serialization_alias="partyId",
            description="Assigned Identification for the party.",
        ),
    ]

    address: Annotated[
        Optional["Address"],
        Field(None, description="Identification of the party by address."),
    ]

    tax_registration_details: Annotated[
        Optional[List["TaxRegistrationDetail"]],
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
InvoiceDetail

Represents the details of an invoice, including invoice number, date, parties involved, payment terms, totals, taxes, charges, and line items.
"""


class InvoiceDetail(SpApiBaseModel):
    """Represents the details of an invoice, including invoice number, date, parties involved, payment terms, totals, taxes, charges, and line items."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    invoice_number: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("invoiceNumber", "invoice_number"),
            serialization_alias="invoiceNumber",
            description="The unique invoice number.",
        ),
    ]

    invoice_date: Annotated[
        datetime,
        Field(
            ...,
            validation_alias=AliasChoices("invoiceDate", "invoice_date"),
            serialization_alias="invoiceDate",
            description="Invoice date.",
        ),
    ]

    reference_number: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("referenceNumber", "reference_number"),
            serialization_alias="referenceNumber",
            description="An additional unique reference number used for regulatory or other purposes.",
        ),
    ]

    remit_to_party: Annotated[
        "PartyIdentification",
        Field(
            ...,
            validation_alias=AliasChoices("remitToParty", "remit_to_party"),
            serialization_alias="remitToParty",
            description="Name, address and tax details of the party receiving the payment of this invoice.",
        ),
    ]

    ship_from_party: Annotated[
        "PartyIdentification",
        Field(
            ...,
            validation_alias=AliasChoices("shipFromParty", "ship_from_party"),
            serialization_alias="shipFromParty",
            description="Warehouse code of the vendor as in the order.",
        ),
    ]

    bill_to_party: Annotated[
        Optional["PartyIdentification"],
        Field(
            None,
            validation_alias=AliasChoices("billToParty", "bill_to_party"),
            serialization_alias="billToParty",
            description="Name, address and tax details of the party to whom this invoice is issued.",
        ),
    ]

    ship_to_country_code: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("shipToCountryCode", "ship_to_country_code"),
            serialization_alias="shipToCountryCode",
            description="Ship-to country code.",
        ),
    ]

    payment_terms_code: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("paymentTermsCode", "payment_terms_code"),
            serialization_alias="paymentTermsCode",
            description="The payment terms for the invoice.",
        ),
    ]

    invoice_total: Annotated[
        "Money",
        Field(
            ...,
            validation_alias=AliasChoices("invoiceTotal", "invoice_total"),
            serialization_alias="invoiceTotal",
            description="Total amount details of the invoice.",
        ),
    ]

    tax_totals: Annotated[
        Optional[List["TaxDetail"]],
        Field(
            None,
            validation_alias=AliasChoices("taxTotals", "tax_totals"),
            serialization_alias="taxTotals",
            description="Individual tax details per line item.",
        ),
    ]

    additional_details: Annotated[
        Optional[List["AdditionalDetails"]],
        Field(
            None,
            validation_alias=AliasChoices("additionalDetails", "additional_details"),
            serialization_alias="additionalDetails",
            description="Additional details provided by the selling party, for tax-related or other purposes.",
        ),
    ]

    charge_details: Annotated[
        Optional[List["ChargeDetails"]],
        Field(
            None,
            validation_alias=AliasChoices("chargeDetails", "charge_details"),
            serialization_alias="chargeDetails",
            description="Total charge amount details for all line items.",
        ),
    ]

    items: Annotated[
        List["InvoiceItem"],
        Field(..., description="Provides the details of the items in this invoice."),
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

    invoices: Annotated[
        Optional[List["InvoiceDetail"]],
        Field(None, description="An array of invoice details to be submitted."),
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

    body: Annotated[
        "SubmitInvoiceRequestBody",
        BodyParam(),
        Field(
            ...,
            description="[BODY] The request body containing one or more invoices for vendor orders.",
        ),
    ]


"""
TransactionReference

Response containing the transaction ID.
"""


class TransactionReference(SpApiBaseModel):
    """Response containing the transaction ID."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    transaction_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("transactionId", "transaction_id"),
            serialization_alias="transactionId",
            description="GUID to identify this transaction. This value can be used with the Transaction Status API to return the status of this transaction.",
        ),
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

    payload: Annotated[
        Optional["TransactionReference"],
        Field(
            None, description="The response payload for the submitInvoice operation."
        ),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
        ),
    ]


# Rebuild models to resolve forward references
SubmitInvoiceRequestBody.model_rebuild()
InvoiceDetail.model_rebuild()
InvoiceItem.model_rebuild()
PartyIdentification.model_rebuild()
TaxRegistrationDetail.model_rebuild()
Address.model_rebuild()
Money.model_rebuild()
TaxDetail.model_rebuild()
ChargeDetails.model_rebuild()
AdditionalDetails.model_rebuild()
ItemQuantity.model_rebuild()
SubmitInvoiceResponse.model_rebuild()
TransactionReference.model_rebuild()
Error.model_rebuild()
SubmitInvoiceRequest.model_rebuild()
