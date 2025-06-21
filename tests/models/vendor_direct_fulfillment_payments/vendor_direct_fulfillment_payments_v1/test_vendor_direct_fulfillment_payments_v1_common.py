# Auto-generated tests for sp_api.api.models.vendor_direct_fulfillment_payments.vendor_direct_fulfillment_payments_v1.common.py
from datetime import datetime

import pytest
from sp_api.api.models.vendor_direct_fulfillment_payments.vendor_direct_fulfillment_payments_v1.common import (
    AdditionalDetails, Address, ChargeDetails, Error, GetRequestSerializer,
    InvoiceDetail, InvoiceItem, ItemQuantity, Money, PartyIdentification,
    RequestsBaseModel, SpApiBaseModel, SubmitInvoiceRequest,
    SubmitInvoiceRequestBody, SubmitInvoiceResponse, TaxDetail,
    TaxRegistrationDetail, TaxRegistrationTypeEnum, TaxTypeEnum,
    TransactionReference, TypeEnum)


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
        "type": TypeEnum.SUR,
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
        "city": "",
        "county": None,
        "district": None,
        "state_or_region": "",
        "postal_code": "",
        "country_code": "",
        "phone": None,
    }
    obj = Address(**kwargs)
    assert isinstance(obj, Address)


def test_money_instantiates():
    """Instantiate Money with dummy data"""
    kwargs = {
        "currency_code": "",
        "amount": "",
    }
    obj = Money(**kwargs)
    assert isinstance(obj, Money)


def test_taxdetail_instantiates():
    """Instantiate TaxDetail with dummy data"""
    kwargs = {
        "tax_type": TaxTypeEnum.CGST,
        "tax_rate": None,
        "tax_amount": Money(**{"currency_code": "", "amount": ""}),
        "taxable_amount": None,
    }
    obj = TaxDetail(**kwargs)
    assert isinstance(obj, TaxDetail)


def test_chargedetails_instantiates():
    """Instantiate ChargeDetails with dummy data"""
    kwargs = {
        "type": TypeEnum.SUR,
        "charge_amount": Money(**{"currency_code": "", "amount": ""}),
        "tax_details": None,
    }
    obj = ChargeDetails(**kwargs)
    assert isinstance(obj, ChargeDetails)


def test_error_instantiates():
    """Instantiate Error with dummy data"""
    kwargs = {
        "code": "",
        "message": "",
        "details": None,
    }
    obj = Error(**kwargs)
    assert isinstance(obj, Error)


def test_itemquantity_instantiates():
    """Instantiate ItemQuantity with dummy data"""
    kwargs = {
        "amount": 0,
        "unit_of_measure": "",
    }
    obj = ItemQuantity(**kwargs)
    assert isinstance(obj, ItemQuantity)


def test_invoiceitem_instantiates():
    """Instantiate InvoiceItem with dummy data"""
    kwargs = {
        "item_sequence_number": "",
        "buyer_product_identifier": None,
        "vendor_product_identifier": None,
        "invoiced_quantity": ItemQuantity(**{"amount": 0, "unit_of_measure": ""}),
        "net_cost": Money(**{"currency_code": "", "amount": ""}),
        "purchase_order_number": "",
        "vendor_order_number": None,
        "hsn_code": None,
        "tax_details": None,
        "charge_details": None,
    }
    obj = InvoiceItem(**kwargs)
    assert isinstance(obj, InvoiceItem)


def test_taxregistrationdetail_instantiates():
    """Instantiate TaxRegistrationDetail with dummy data"""
    kwargs = {
        "tax_registration_type": None,
        "tax_registration_number": "",
        "tax_registration_address": None,
        "tax_registration_message": None,
    }
    obj = TaxRegistrationDetail(**kwargs)
    assert isinstance(obj, TaxRegistrationDetail)


def test_partyidentification_instantiates():
    """Instantiate PartyIdentification with dummy data"""
    kwargs = {
        "party_id": "",
        "address": None,
        "tax_registration_details": None,
    }
    obj = PartyIdentification(**kwargs)
    assert isinstance(obj, PartyIdentification)


def test_invoicedetail_instantiates():
    """Instantiate InvoiceDetail with dummy data"""
    kwargs = {
        "invoice_number": "",
        "invoice_date": datetime(2000, 1, 1),
        "reference_number": None,
        "remit_to_party": PartyIdentification(
            **{"party_id": "", "address": None, "tax_registration_details": None}
        ),
        "ship_from_party": PartyIdentification(
            **{"party_id": "", "address": None, "tax_registration_details": None}
        ),
        "bill_to_party": None,
        "ship_to_country_code": None,
        "payment_terms_code": None,
        "invoice_total": Money(**{"currency_code": "", "amount": ""}),
        "tax_totals": None,
        "additional_details": None,
        "charge_details": None,
        "items": [],
    }
    obj = InvoiceDetail(**kwargs)
    assert isinstance(obj, InvoiceDetail)


def test_submitinvoicerequestbody_instantiates():
    """Instantiate SubmitInvoiceRequestBody with dummy data"""
    kwargs = {
        "invoices": None,
    }
    obj = SubmitInvoiceRequestBody(**kwargs)
    assert isinstance(obj, SubmitInvoiceRequestBody)


def test_submitinvoicerequest_instantiates():
    """Instantiate SubmitInvoiceRequest with dummy data"""
    kwargs = {
        "body": SubmitInvoiceRequestBody(**{"invoices": None}),
    }
    obj = SubmitInvoiceRequest(**kwargs)
    assert isinstance(obj, SubmitInvoiceRequest)


def test_transactionreference_instantiates():
    """Instantiate TransactionReference with dummy data"""
    kwargs = {
        "transaction_id": None,
    }
    obj = TransactionReference(**kwargs)
    assert isinstance(obj, TransactionReference)


def test_submitinvoiceresponse_instantiates():
    """Instantiate SubmitInvoiceResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = SubmitInvoiceResponse(**kwargs)
    assert isinstance(obj, SubmitInvoiceResponse)
