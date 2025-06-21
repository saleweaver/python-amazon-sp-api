# Auto-generated tests for sp_api.api.models.vendor_invoices.vendor_invoices_v1.common.py
from datetime import datetime

import pytest
from sp_api.api.models.vendor_invoices.vendor_invoices_v1.common import (
    AdditionalDetails, Address, AllowanceDetails, ChargeDetails,
    CreditNoteDetails, Error, GetRequestSerializer, Invoice, InvoiceItem,
    InvoiceTypeEnum, ItemQuantity, Money, PartyIdentification, PaymentTerms,
    RequestsBaseModel, SpApiBaseModel, SubmitInvoicesRequest,
    SubmitInvoicesRequestBody, SubmitInvoicesResponse, TaxDetails,
    TaxRegistrationDetails, TaxRegistrationTypeEnum, TaxTypeEnum, TotalWeight,
    TransactionId, TypeEnum, UnitOfMeasureEnum)


def test_requestsbasemodel_instantiates():
    """Instantiate RequestsBaseModel with dummy data"""
    kwargs = {}
    obj = RequestsBaseModel(**kwargs)
    assert isinstance(obj, RequestsBaseModel)


def test_spapibasemodel_instantiates():
    """Instantiate SpApiBaseModel with dummy data"""
    kwargs = {}
    obj = SpApiBaseModel(**kwargs)
    assert isinstance(obj, SpApiBaseModel)


def test_getrequestserializer_instantiates():
    """Instantiate GetRequestSerializer with dummy data"""
    kwargs = {}
    obj = GetRequestSerializer(**kwargs)
    assert isinstance(obj, GetRequestSerializer)


def test_additionaldetails_instantiates():
    """Instantiate AdditionalDetails with dummy data"""
    kwargs = {
        "type": TypeEnum.BASIC,
        "detail": "",
        "language_code": None,
    }
    obj = AdditionalDetails(**kwargs)
    assert isinstance(obj, AdditionalDetails)


def test_address_instantiates():
    """Instantiate Address with dummy data"""
    kwargs = {
        "name": "",
        "address_line1": "",
        "address_line2": None,
        "address_line3": None,
        "city": None,
        "county": None,
        "district": None,
        "state_or_region": None,
        "postal_or_zip_code": None,
        "country_code": "",
        "phone": None,
    }
    obj = Address(**kwargs)
    assert isinstance(obj, Address)


def test_money_instantiates():
    """Instantiate Money with dummy data"""
    kwargs = {
        "currency_code": None,
        "amount": None,
    }
    obj = Money(**kwargs)
    assert isinstance(obj, Money)


def test_taxdetails_instantiates():
    """Instantiate TaxDetails with dummy data"""
    kwargs = {
        "tax_type": TaxTypeEnum.CGST,
        "tax_rate": None,
        "tax_amount": Money(**{"currency_code": None, "amount": None}),
        "taxable_amount": None,
    }
    obj = TaxDetails(**kwargs)
    assert isinstance(obj, TaxDetails)


def test_allowancedetails_instantiates():
    """Instantiate AllowanceDetails with dummy data"""
    kwargs = {
        "type": TypeEnum.BASIC,
        "description": None,
        "allowance_amount": Money(**{"currency_code": None, "amount": None}),
        "tax_details": None,
    }
    obj = AllowanceDetails(**kwargs)
    assert isinstance(obj, AllowanceDetails)


def test_chargedetails_instantiates():
    """Instantiate ChargeDetails with dummy data"""
    kwargs = {
        "type": TypeEnum.BASIC,
        "description": None,
        "charge_amount": Money(**{"currency_code": None, "amount": None}),
        "tax_details": None,
    }
    obj = ChargeDetails(**kwargs)
    assert isinstance(obj, ChargeDetails)


def test_creditnotedetails_instantiates():
    """Instantiate CreditNoteDetails with dummy data"""
    kwargs = {
        "reference_invoice_number": None,
        "debit_note_number": None,
        "returns_reference_number": None,
        "goods_return_date": None,
        "rma_id": None,
        "coop_reference_number": None,
        "consignors_reference_number": None,
    }
    obj = CreditNoteDetails(**kwargs)
    assert isinstance(obj, CreditNoteDetails)


def test_error_instantiates():
    """Instantiate Error with dummy data"""
    kwargs = {
        "code": "",
        "message": "",
        "details": None,
    }
    obj = Error(**kwargs)
    assert isinstance(obj, Error)


def test_totalweight_instantiates():
    """Instantiate TotalWeight with dummy data"""
    kwargs = {
        "unit_of_measure": UnitOfMeasureEnum.POUNDS,
        "amount": "",
    }
    obj = TotalWeight(**kwargs)
    assert isinstance(obj, TotalWeight)


def test_itemquantity_instantiates():
    """Instantiate ItemQuantity with dummy data"""
    kwargs = {
        "amount": 0,
        "unit_of_measure": UnitOfMeasureEnum.POUNDS,
        "unit_size": None,
        "total_weight": None,
    }
    obj = ItemQuantity(**kwargs)
    assert isinstance(obj, ItemQuantity)


def test_invoiceitem_instantiates():
    """Instantiate InvoiceItem with dummy data"""
    kwargs = {
        "item_sequence_number": 0,
        "amazon_product_identifier": None,
        "vendor_product_identifier": None,
        "invoiced_quantity": ItemQuantity(
            **{
                "amount": 0,
                "unit_of_measure": UnitOfMeasureEnum.POUNDS,
                "unit_size": None,
                "total_weight": None,
            }
        ),
        "net_cost": Money(**{"currency_code": None, "amount": None}),
        "net_cost_unit_of_measure": None,
        "purchase_order_number": None,
        "hsn_code": None,
        "credit_note_details": None,
        "tax_details": None,
        "charge_details": None,
        "allowance_details": None,
    }
    obj = InvoiceItem(**kwargs)
    assert isinstance(obj, InvoiceItem)


def test_taxregistrationdetails_instantiates():
    """Instantiate TaxRegistrationDetails with dummy data"""
    kwargs = {
        "tax_registration_type": TaxRegistrationTypeEnum.VAT,
        "tax_registration_number": "",
    }
    obj = TaxRegistrationDetails(**kwargs)
    assert isinstance(obj, TaxRegistrationDetails)


def test_partyidentification_instantiates():
    """Instantiate PartyIdentification with dummy data"""
    kwargs = {
        "party_id": "",
        "address": None,
        "tax_registration_details": None,
    }
    obj = PartyIdentification(**kwargs)
    assert isinstance(obj, PartyIdentification)


def test_paymentterms_instantiates():
    """Instantiate PaymentTerms with dummy data"""
    kwargs = {
        "type": None,
        "discount_percent": None,
        "discount_due_days": None,
        "net_due_days": None,
    }
    obj = PaymentTerms(**kwargs)
    assert isinstance(obj, PaymentTerms)


def test_invoice_instantiates():
    """Instantiate Invoice with dummy data"""
    kwargs = {
        "invoice_type": InvoiceTypeEnum.INVOICE,
        "id": "",
        "reference_number": None,
        "date": "",
        "remit_to_party": PartyIdentification(
            **{"party_id": "", "address": None, "tax_registration_details": None}
        ),
        "ship_to_party": None,
        "ship_from_party": None,
        "bill_to_party": None,
        "payment_terms": None,
        "invoice_total": Money(**{"currency_code": None, "amount": None}),
        "tax_details": None,
        "additional_details": None,
        "charge_details": None,
        "allowance_details": None,
        "items": None,
    }
    obj = Invoice(**kwargs)
    assert isinstance(obj, Invoice)


def test_submitinvoicesrequestbody_instantiates():
    """Instantiate SubmitInvoicesRequestBody with dummy data"""
    kwargs = {
        "invoices": None,
    }
    obj = SubmitInvoicesRequestBody(**kwargs)
    assert isinstance(obj, SubmitInvoicesRequestBody)


def test_submitinvoicesrequest_instantiates():
    """Instantiate SubmitInvoicesRequest with dummy data"""
    kwargs = {
        "body": SubmitInvoicesRequestBody(**{"invoices": None}),
    }
    obj = SubmitInvoicesRequest(**kwargs)
    assert isinstance(obj, SubmitInvoicesRequest)


def test_transactionid_instantiates():
    """Instantiate TransactionId with dummy data"""
    kwargs = {
        "transaction_id": None,
    }
    obj = TransactionId(**kwargs)
    assert isinstance(obj, TransactionId)


def test_submitinvoicesresponse_instantiates():
    """Instantiate SubmitInvoicesResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = SubmitInvoicesResponse(**kwargs)
    assert isinstance(obj, SubmitInvoicesResponse)
