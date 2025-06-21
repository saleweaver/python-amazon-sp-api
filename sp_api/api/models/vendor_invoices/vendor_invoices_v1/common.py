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

    BASIC = "Basic"  # Payment term that buyer and seller have agreed to.
    END_OF_MONTH = "EndOfMonth"  # Payment term where seller gets paid end of month.
    FIXED_DATE = "FixedDate"  # Payment term where seller gets paid on a fixed date as agreed with buyer.
    PROXIMO = "Proximo"  # Payment term where seller gets paid end of following month.
    PAYMENT_DUE_UPON_RECEIPT_OF_INVOICE = "PaymentDueUponReceiptOfInvoice"  # Payment term where seller gets paid upon receipt of the invoice by the buyer.
    LETTEROF_CREDIT = "LetterofCredit"  # A payment undertaking given by a bank to the seller and is issued on behalf of the applicant i.e. the buyer.


"""
AdditionalDetails

Additional information provided by the selling party for tax-related or any other purpose.
"""


class AdditionalDetails(SpApiBaseModel):
    """Additional information provided by the selling party for tax-related or any other purpose."""

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
            description="First line of street address.",
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
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("stateOrRegion", "state_or_region"),
            serialization_alias="stateOrRegion",
            description="The state or region where person, business or institution is located.",
        ),
    ]

    postal_or_zip_code: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("postalOrZipCode", "postal_or_zip_code"),
            serialization_alias="postalOrZipCode",
            description="The postal or zip code of that address. It contains a series of letters or digits or both, sometimes including spaces or punctuation.",
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
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("currencyCode", "currency_code"),
            serialization_alias="currencyCode",
            description="Three-digit currency code in ISO 4217 format.",
        ),
    ]

    amount: Annotated[
        Optional["Decimal"],
        Field(
            None,
        ),
    ]


# Enum definitions
class TaxTypeEnum(str, Enum):
    """Enum for taxType"""

    CGST = "CGST"  # Central Goods and Services Tax (CGST) is levied by the Indian government for intrastate movement of goods and services.
    SGST = "SGST"  # State Goods and Services Tax (SGST) is an indirect tax levied and collected by a State Government in India on the intra-state supplies.
    CESS = "CESS"  # A CESS is a form of tax levied by the government on tax with specific purposes till the time the government gets enough money for that purpose.
    UTGST = "UTGST"  # Union Territory Goods and Services Tax in India.
    IGST = "IGST"  # Integrated Goods and Services Tax (IGST) is a tax levied on all Inter-State supplies of goods and/or services in India.
    MW_ST_ = "MwSt."  # Mehrwertsteuer, MwSt, is German for value-added tax.
    PST = "PST"  # A provincial sales tax (PST) is imposed on consumers of goods and particular services in many Canadian provinces.
    TVA = "TVA"  # Taxe sur la Valeur Ajout&#233;e (TVA) is French for value-added tax.
    VAT = "VAT"  # Value-added tax.
    GST = "GST"  # Tax levied on most goods and services sold for domestic consumption.
    ST = "ST"  # Sales tax.
    CONSUMPTION = (
        "Consumption"  # Tax levied on consumption spending on goods and services.
    )
    MUTUALLY_DEFINED = "MutuallyDefined"  # Tax component that was mutually agreed upon between Amazon and vendor.
    DOMESTIC_VAT = "DomesticVAT"  # Domestic value-added tax.


"""
TaxDetails

Details of tax amount applied.
"""


class TaxDetails(SpApiBaseModel):
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
            description="The invoice amount that is taxable at the rate specified in the tax rate field.",
        ),
    ]


# Enum definitions
class TypeEnum(str, Enum):
    """Enum for type"""

    BASIC = "Basic"  # Payment term that buyer and seller have agreed to.
    END_OF_MONTH = "EndOfMonth"  # Payment term where seller gets paid end of month.
    FIXED_DATE = "FixedDate"  # Payment term where seller gets paid on a fixed date as agreed with buyer.
    PROXIMO = "Proximo"  # Payment term where seller gets paid end of following month.
    PAYMENT_DUE_UPON_RECEIPT_OF_INVOICE = "PaymentDueUponReceiptOfInvoice"  # Payment term where seller gets paid upon receipt of the invoice by the buyer.
    LETTEROF_CREDIT = "LetterofCredit"  # A payment undertaking given by a bank to the seller and is issued on behalf of the applicant i.e. the buyer.


"""
AllowanceDetails

Monetary and tax details of the allowance.
"""


class AllowanceDetails(SpApiBaseModel):
    """Monetary and tax details of the allowance."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    type: Annotated[TypeEnum, Field(..., description="Type of the allowance applied.")]

    description: Annotated[
        Optional[str], Field(None, description="Description of the allowance.")
    ]

    allowance_amount: Annotated[
        "Money",
        Field(
            ...,
            validation_alias=AliasChoices("allowanceAmount", "allowance_amount"),
            serialization_alias="allowanceAmount",
            description="Total monetary amount related to this allowance.",
        ),
    ]

    tax_details: Annotated[
        Optional[List["TaxDetails"]],
        Field(
            None,
            validation_alias=AliasChoices("taxDetails", "tax_details"),
            serialization_alias="taxDetails",
            description="Tax amount details applied on this allowance.",
        ),
    ]


# Enum definitions
class TypeEnum(str, Enum):
    """Enum for type"""

    BASIC = "Basic"  # Payment term that buyer and seller have agreed to.
    END_OF_MONTH = "EndOfMonth"  # Payment term where seller gets paid end of month.
    FIXED_DATE = "FixedDate"  # Payment term where seller gets paid on a fixed date as agreed with buyer.
    PROXIMO = "Proximo"  # Payment term where seller gets paid end of following month.
    PAYMENT_DUE_UPON_RECEIPT_OF_INVOICE = "PaymentDueUponReceiptOfInvoice"  # Payment term where seller gets paid upon receipt of the invoice by the buyer.
    LETTEROF_CREDIT = "LetterofCredit"  # A payment undertaking given by a bank to the seller and is issued on behalf of the applicant i.e. the buyer.


"""
ChargeDetails

Monetary and tax details of the charge.
"""


class ChargeDetails(SpApiBaseModel):
    """Monetary and tax details of the charge."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    type: Annotated[TypeEnum, Field(..., description="Type of the charge applied.")]

    description: Annotated[
        Optional[str], Field(None, description="Description of the charge.")
    ]

    charge_amount: Annotated[
        "Money",
        Field(
            ...,
            validation_alias=AliasChoices("chargeAmount", "charge_amount"),
            serialization_alias="chargeAmount",
            description="Total monetary amount related to this charge.",
        ),
    ]

    tax_details: Annotated[
        Optional[List["TaxDetails"]],
        Field(
            None,
            validation_alias=AliasChoices("taxDetails", "tax_details"),
            serialization_alias="taxDetails",
            description="Tax amount details applied on this charge.",
        ),
    ]


DateTime = str
"""Defines a date and time according to ISO8601."""


"""
CreditNoteDetails

References required in order to process a credit note. This information is required only if InvoiceType is CreditNote.
"""


class CreditNoteDetails(SpApiBaseModel):
    """References required in order to process a credit note. This information is required only if InvoiceType is CreditNote."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    reference_invoice_number: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "referenceInvoiceNumber", "reference_invoice_number"
            ),
            serialization_alias="referenceInvoiceNumber",
            description="Original Invoice Number when sending a credit note relating to an existing invoice. One Invoice only to be processed per Credit Note. This is mandatory for AP Credit Notes.",
        ),
    ]

    debit_note_number: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("debitNoteNumber", "debit_note_number"),
            serialization_alias="debitNoteNumber",
            description="Debit Note Number as generated by Amazon. Recommended for Returns and COOP Credit Notes.",
        ),
    ]

    returns_reference_number: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "returnsReferenceNumber", "returns_reference_number"
            ),
            serialization_alias="returnsReferenceNumber",
            description="Identifies the Returns Notice Number. Mandatory for all Returns Credit Notes.",
        ),
    ]

    goods_return_date: Annotated[
        Optional["DateTime"],
        Field(
            None,
            validation_alias=AliasChoices("goodsReturnDate", "goods_return_date"),
            serialization_alias="goodsReturnDate",
            description="Date that a return is received by the vendor. It is mandatory for Returns Credit Note.",
        ),
    ]

    rma_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("rmaId", "rma_id"),
            serialization_alias="rmaId",
            description="Identifies the Returned Merchandise Authorization ID, if generated.",
        ),
    ]

    coop_reference_number: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "coopReferenceNumber", "coop_reference_number"
            ),
            serialization_alias="coopReferenceNumber",
            description="Identifies the COOP reference used for COOP agreement. Failure to provide the COOP reference number or the Debit Note number may lead to a rejection of the Credit Note.",
        ),
    ]

    consignors_reference_number: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "consignorsReferenceNumber", "consignors_reference_number"
            ),
            serialization_alias="consignorsReferenceNumber",
            description="Identifies the consignor reference number (VRET number), if generated by Amazon.",
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


# Enum definitions
class UnitOfMeasureEnum(str, Enum):
    """Enum for unitOfMeasure"""

    POUNDS = "POUNDS"  # Weight in Pound.
    OUNCES = "OUNCES"  # Weight in Ounce.
    GRAMS = "GRAMS"  # Weight in Gram.
    KILOGRAMS = "KILOGRAMS"  # Weight in Kilogram.


"""
TotalWeight

The aggregate weight of this item being invoiced. This information will be available for items sold by weight.
"""


class TotalWeight(SpApiBaseModel):
    """The aggregate weight of this item being invoiced. This information will be available for items sold by weight."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    unit_of_measure: Annotated[
        UnitOfMeasureEnum,
        Field(
            ...,
            validation_alias=AliasChoices("unitOfMeasure", "unit_of_measure"),
            serialization_alias="unitOfMeasure",
            description="The unit of measure for items sold by weight.",
        ),
    ]

    amount: Annotated[
        "Decimal",
        Field(
            ...,
        ),
    ]


# Enum definitions
class UnitOfMeasureEnum(str, Enum):
    """Enum for unitOfMeasure"""

    POUNDS = "POUNDS"  # Weight in Pound.
    OUNCES = "OUNCES"  # Weight in Ounce.
    GRAMS = "GRAMS"  # Weight in Gram.
    KILOGRAMS = "KILOGRAMS"  # Weight in Kilogram.


"""
ItemQuantity

Details of quantity.
"""


class ItemQuantity(SpApiBaseModel):
    """Details of quantity."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    amount: Annotated[
        int,
        Field(..., description="Quantity of an item. This value should not be zero."),
    ]

    unit_of_measure: Annotated[
        UnitOfMeasureEnum,
        Field(
            ...,
            validation_alias=AliasChoices("unitOfMeasure", "unit_of_measure"),
            serialization_alias="unitOfMeasure",
            description="Unit of measure for the quantity.",
        ),
    ]

    unit_size: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices("unitSize", "unit_size"),
            serialization_alias="unitSize",
            description="The case size, if the unit of measure value is Cases.",
        ),
    ]

    total_weight: Annotated[
        Optional["TotalWeight"],
        Field(
            None,
            validation_alias=AliasChoices("totalWeight", "total_weight"),
            serialization_alias="totalWeight",
        ),
    ]


NetCostUnitOfMeasure = str
"""This field represents weight unit of measure of items that are ordered by cases and supporting priced by weight."""


"""
InvoiceItem

Details of the item being invoiced.
"""


class InvoiceItem(SpApiBaseModel):
    """Details of the item being invoiced."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    item_sequence_number: Annotated[
        int,
        Field(
            ...,
            validation_alias=AliasChoices("itemSequenceNumber", "item_sequence_number"),
            serialization_alias="itemSequenceNumber",
            description="Unique number related to this line item.",
        ),
    ]

    amazon_product_identifier: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "amazonProductIdentifier", "amazon_product_identifier"
            ),
            serialization_alias="amazonProductIdentifier",
            description="Amazon Standard Identification Number (ASIN) of an item.",
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
            description="The vendor selected product identifier of the item. Should be the same as was provided in the purchase order.",
        ),
    ]

    invoiced_quantity: Annotated[
        "ItemQuantity",
        Field(
            ...,
            validation_alias=AliasChoices("invoicedQuantity", "invoiced_quantity"),
            serialization_alias="invoicedQuantity",
            description="Invoiced quantity of this item. Quantity must be greater than zero.",
        ),
    ]

    net_cost: Annotated[
        "Money",
        Field(
            ...,
            validation_alias=AliasChoices("netCost", "net_cost"),
            serialization_alias="netCost",
            description="The item cost to Amazon, which should match the cost on the order. Price information should not be zero or negative. It indicates net unit price. Net cost means VAT is not included in cost. If items are priced by weight, this cost need to be considered in conjunction with netCostUnitOfMeasure. E.g.: $5/LB",
        ),
    ]

    net_cost_unit_of_measure: Annotated[
        Optional["NetCostUnitOfMeasure"],
        Field(
            None,
            validation_alias=AliasChoices(
                "netCostUnitOfMeasure", "net_cost_unit_of_measure"
            ),
            serialization_alias="netCostUnitOfMeasure",
            description="This field represents weight unit of measure of items that are ordered by cases and supporting priced by weight.",
        ),
    ]

    purchase_order_number: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "purchaseOrderNumber", "purchase_order_number"
            ),
            serialization_alias="purchaseOrderNumber",
            description="The Amazon purchase order number for this invoiced line item. Formatting Notes: 8-character alpha-numeric code. This value is mandatory only when invoiceType is Invoice, and is not required when invoiceType is CreditNote.",
        ),
    ]

    hsn_code: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("hsnCode", "hsn_code"),
            serialization_alias="hsnCode",
            description="HSN Tax code. The HSN number cannot contain alphabets.",
        ),
    ]

    credit_note_details: Annotated[
        Optional["CreditNoteDetails"],
        Field(
            None,
            validation_alias=AliasChoices("creditNoteDetails", "credit_note_details"),
            serialization_alias="creditNoteDetails",
            description="Details required in order to process a credit note. This information is required only if invoiceType is CreditNote.",
        ),
    ]

    tax_details: Annotated[
        Optional[List["TaxDetails"]],
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

    allowance_details: Annotated[
        Optional[List["AllowanceDetails"]],
        Field(
            None,
            validation_alias=AliasChoices("allowanceDetails", "allowance_details"),
            serialization_alias="allowanceDetails",
            description="Individual allowance details per line item.",
        ),
    ]


# Enum definitions
class TaxRegistrationTypeEnum(str, Enum):
    """Enum for taxRegistrationType"""

    VAT = "VAT"  # Value-added tax.
    GST = "GST"  # Goods and services tax.


"""
TaxRegistrationDetails

Tax registration details of the entity.
"""


class TaxRegistrationDetails(SpApiBaseModel):
    """Tax registration details of the entity."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    tax_registration_type: Annotated[
        TaxRegistrationTypeEnum,
        Field(
            ...,
            validation_alias=AliasChoices(
                "taxRegistrationType", "tax_registration_type"
            ),
            serialization_alias="taxRegistrationType",
            description="The tax registration type for the entity.",
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
            description="The tax registration number for the entity. For example, VAT ID, Consumption Tax ID.",
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
            description="Assigned identification for the party.",
        ),
    ]

    address: Annotated[
        Optional["Address"],
        Field(None, description="Identification of the party by address."),
    ]

    tax_registration_details: Annotated[
        Optional[List["TaxRegistrationDetails"]],
        Field(
            None,
            validation_alias=AliasChoices(
                "taxRegistrationDetails", "tax_registration_details"
            ),
            serialization_alias="taxRegistrationDetails",
            description="Tax registration details of the party.",
        ),
    ]


# Enum definitions
class TypeEnum(str, Enum):
    """Enum for type"""

    BASIC = "Basic"  # Payment term that buyer and seller have agreed to.
    END_OF_MONTH = "EndOfMonth"  # Payment term where seller gets paid end of month.
    FIXED_DATE = "FixedDate"  # Payment term where seller gets paid on a fixed date as agreed with buyer.
    PROXIMO = "Proximo"  # Payment term where seller gets paid end of following month.
    PAYMENT_DUE_UPON_RECEIPT_OF_INVOICE = "PaymentDueUponReceiptOfInvoice"  # Payment term where seller gets paid upon receipt of the invoice by the buyer.
    LETTEROF_CREDIT = "LetterofCredit"  # A payment undertaking given by a bank to the seller and is issued on behalf of the applicant i.e. the buyer.


"""
PaymentTerms

Terms of the payment for the invoice. The basis of the payment terms is the invoice date.
"""


class PaymentTerms(SpApiBaseModel):
    """Terms of the payment for the invoice. The basis of the payment terms is the invoice date."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    type: Annotated[
        Optional[TypeEnum],
        Field(None, description="The payment term type for the invoice."),
    ]

    discount_percent: Annotated[
        Optional["Decimal"],
        Field(
            None,
            validation_alias=AliasChoices("discountPercent", "discount_percent"),
            serialization_alias="discountPercent",
            description="The discount percent value, which is good until the discount due date.",
        ),
    ]

    discount_due_days: Annotated[
        Optional[float],
        Field(
            None,
            validation_alias=AliasChoices("discountDueDays", "discount_due_days"),
            serialization_alias="discountDueDays",
            description="The number of calendar days from the Base date (Invoice date) until the discount is no longer valid.",
        ),
    ]

    net_due_days: Annotated[
        Optional[float],
        Field(
            None,
            validation_alias=AliasChoices("netDueDays", "net_due_days"),
            serialization_alias="netDueDays",
            description="The number of calendar days from the base date (invoice date) until the total amount on the invoice is due.",
        ),
    ]


# Enum definitions
class InvoiceTypeEnum(str, Enum):
    """Enum for invoiceType"""

    INVOICE = "Invoice"  # A commercial document issued by a seller to a buyer, relating to a sale transaction and indicating the products, quantities, and agreed prices for products or services the seller had provided the buyer.
    CREDIT_NOTE = "CreditNote"  # A commercial document issued by a seller to a buyer. It is evidence of the reduction in sales.


"""
Invoice

Represents an invoice or credit note document with details about the transaction, parties involved, and line items.
"""


class Invoice(SpApiBaseModel):
    """Represents an invoice or credit note document with details about the transaction, parties involved, and line items."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    invoice_type: Annotated[
        InvoiceTypeEnum,
        Field(
            ...,
            validation_alias=AliasChoices("invoiceType", "invoice_type"),
            serialization_alias="invoiceType",
            description="Identifies the type of invoice.",
        ),
    ]

    id: Annotated[
        str,
        Field(
            ...,
            description="Unique number relating to the charges defined in this document. This will be invoice number if the document type is Invoice or CreditNote number if the document type is Credit Note. Failure to provide this reference will result in a rejection.",
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

    date: Annotated[
        "DateTime",
        Field(
            ...,
            description="Date when the invoice/credit note information was generated in the origin's accounting system. The invoice date should be on or after the purchase order creation date.",
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

    ship_to_party: Annotated[
        Optional["PartyIdentification"],
        Field(
            None,
            validation_alias=AliasChoices("shipToParty", "ship_to_party"),
            serialization_alias="shipToParty",
            description="Name, address and tax details of the party receiving a shipment of products.",
        ),
    ]

    ship_from_party: Annotated[
        Optional["PartyIdentification"],
        Field(
            None,
            validation_alias=AliasChoices("shipFromParty", "ship_from_party"),
            serialization_alias="shipFromParty",
            description="Name, address and tax details of the party sending a shipment of products.",
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

    payment_terms: Annotated[
        Optional["PaymentTerms"],
        Field(
            None,
            validation_alias=AliasChoices("paymentTerms", "payment_terms"),
            serialization_alias="paymentTerms",
            description="The payment terms for the invoice.",
        ),
    ]

    invoice_total: Annotated[
        "Money",
        Field(
            ...,
            validation_alias=AliasChoices("invoiceTotal", "invoice_total"),
            serialization_alias="invoiceTotal",
            description="Total monetary amount charged in the invoice or full value of credit note to be paid including all relevant taxes. It is the total amount of invoice (including charges, less allowances) before terms discount (if discount is applicable).",
        ),
    ]

    tax_details: Annotated[
        Optional[List["TaxDetails"]],
        Field(
            None,
            validation_alias=AliasChoices("taxDetails", "tax_details"),
            serialization_alias="taxDetails",
            description="Total tax amount details for all line items.",
        ),
    ]

    additional_details: Annotated[
        Optional[List["AdditionalDetails"]],
        Field(
            None,
            validation_alias=AliasChoices("additionalDetails", "additional_details"),
            serialization_alias="additionalDetails",
            description="Additional details provided by the selling party, for tax related or other purposes.",
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

    allowance_details: Annotated[
        Optional[List["AllowanceDetails"]],
        Field(
            None,
            validation_alias=AliasChoices("allowanceDetails", "allowance_details"),
            serialization_alias="allowanceDetails",
            description="Total allowance amount details for all line items.",
        ),
    ]

    items: Annotated[
        Optional[List["InvoiceItem"]],
        Field(None, description="The list of invoice items."),
    ]


"""
SubmitInvoicesRequestBody

The request schema for the submitInvoices operation.
"""


class SubmitInvoicesRequestBody(SpApiBaseModel):
    """The request schema for the submitInvoices operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    invoices: Annotated[
        Optional[List["Invoice"]],
        Field(
            None,
            description="An array of Invoice objects representing the invoices or credit notes to be submitted.",
        ),
    ]


"""
SubmitInvoicesRequest

Request parameters for submitInvoices
"""


class SubmitInvoicesRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for submitInvoices
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    body: Annotated[
        "SubmitInvoicesRequestBody",
        BodyParam(),
        Field(
            ...,
            description="[BODY] The request body containing the invoice data to submit.",
        ),
    ]


"""
TransactionId

Response containing the transaction ID.
"""


class TransactionId(SpApiBaseModel):
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
SubmitInvoicesResponse

The response schema for the submitInvoices operation.
"""


class SubmitInvoicesResponse(SpApiBaseModel):
    """The response schema for the submitInvoices operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["TransactionId"],
        Field(
            None, description="The response payload for the submitInvoices operation."
        ),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
        ),
    ]


# Rebuild models to resolve forward references
SubmitInvoicesResponse.model_rebuild()
TransactionId.model_rebuild()
Error.model_rebuild()
SubmitInvoicesRequestBody.model_rebuild()
Invoice.model_rebuild()
PartyIdentification.model_rebuild()
TaxRegistrationDetails.model_rebuild()
Address.model_rebuild()
InvoiceItem.model_rebuild()
TaxDetails.model_rebuild()
Money.model_rebuild()
AdditionalDetails.model_rebuild()
ChargeDetails.model_rebuild()
AllowanceDetails.model_rebuild()
PaymentTerms.model_rebuild()
CreditNoteDetails.model_rebuild()
ItemQuantity.model_rebuild()
TotalWeight.model_rebuild()
SubmitInvoicesRequest.model_rebuild()
