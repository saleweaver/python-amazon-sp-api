# Auto-generated tests for sp_api.api.models.shipment_invoicing.shipment_invoicing_v0.common.py
from datetime import datetime

import pytest
from sp_api.api.models.shipment_invoicing.shipment_invoicing_v0.common import (
    Address, BuyerTaxInfo, Error, GetInvoiceStatusRequest,
    GetInvoiceStatusResponse, GetRequestSerializer, GetShipmentDetailsRequest,
    GetShipmentDetailsResponse, MarketplaceTaxInfo, Money,
    PaymentMethodDetailItemList, RequestsBaseModel, SerialNumbersList,
    ShipmentDetail, ShipmentInvoiceStatusInfo, ShipmentInvoiceStatusResponse,
    ShipmentItem, SpApiBaseModel, SubmitInvoiceRequest,
    SubmitInvoiceRequestBody, SubmitInvoiceResponse, TaxClassification)


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


def test_address_instantiates():
    """Instantiate Address with dummy data"""
    kwargs = {
        "name": None,
        "address_line1": None,
        "address_line2": None,
        "address_line3": None,
        "city": None,
        "county": None,
        "district": None,
        "state_or_region": None,
        "postal_code": None,
        "country_code": None,
        "phone": None,
        "address_type": None,
    }
    obj = Address(**kwargs)
    assert isinstance(obj, Address)


def test_buyertaxinfo_instantiates():
    """Instantiate BuyerTaxInfo with dummy data"""
    kwargs = {
        "company_legal_name": None,
        "taxing_region": None,
        "tax_classifications": None,
    }
    obj = BuyerTaxInfo(**kwargs)
    assert isinstance(obj, BuyerTaxInfo)


def test_error_instantiates():
    """Instantiate Error with dummy data"""
    kwargs = {
        "code": "",
        "message": "",
        "details": None,
    }
    obj = Error(**kwargs)
    assert isinstance(obj, Error)


def test_getinvoicestatusrequest_instantiates():
    """Instantiate GetInvoiceStatusRequest with dummy data"""
    kwargs = {
        "shipment_id": "",
    }
    obj = GetInvoiceStatusRequest(**kwargs)
    assert isinstance(obj, GetInvoiceStatusRequest)


def test_shipmentinvoicestatusinfo_instantiates():
    """Instantiate ShipmentInvoiceStatusInfo with dummy data"""
    kwargs = {
        "amazon_shipment_id": None,
        "invoice_status": None,
    }
    obj = ShipmentInvoiceStatusInfo(**kwargs)
    assert isinstance(obj, ShipmentInvoiceStatusInfo)


def test_shipmentinvoicestatusresponse_instantiates():
    """Instantiate ShipmentInvoiceStatusResponse with dummy data"""
    kwargs = {
        "shipments": None,
    }
    obj = ShipmentInvoiceStatusResponse(**kwargs)
    assert isinstance(obj, ShipmentInvoiceStatusResponse)


def test_getinvoicestatusresponse_instantiates():
    """Instantiate GetInvoiceStatusResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = GetInvoiceStatusResponse(**kwargs)
    assert isinstance(obj, GetInvoiceStatusResponse)


def test_getshipmentdetailsrequest_instantiates():
    """Instantiate GetShipmentDetailsRequest with dummy data"""
    kwargs = {
        "shipment_id": "",
    }
    obj = GetShipmentDetailsRequest(**kwargs)
    assert isinstance(obj, GetShipmentDetailsRequest)


def test_marketplacetaxinfo_instantiates():
    """Instantiate MarketplaceTaxInfo with dummy data"""
    kwargs = {
        "company_legal_name": None,
        "taxing_region": None,
        "tax_classifications": None,
    }
    obj = MarketplaceTaxInfo(**kwargs)
    assert isinstance(obj, MarketplaceTaxInfo)


def test_paymentmethoddetailitemlist_instantiates():
    """Instantiate PaymentMethodDetailItemList with dummy data"""
    kwargs = {}
    obj = PaymentMethodDetailItemList(**kwargs)
    assert isinstance(obj, PaymentMethodDetailItemList)


def test_shipmentdetail_instantiates():
    """Instantiate ShipmentDetail with dummy data"""
    kwargs = {
        "warehouse_id": None,
        "amazon_order_id": None,
        "amazon_shipment_id": None,
        "purchase_date": None,
        "shipping_address": None,
        "payment_method_details": None,
        "marketplace_id": None,
        "seller_id": None,
        "buyer_name": None,
        "buyer_county": None,
        "buyer_tax_info": None,
        "marketplace_tax_info": None,
        "seller_display_name": None,
        "shipment_items": None,
    }
    obj = ShipmentDetail(**kwargs)
    assert isinstance(obj, ShipmentDetail)


def test_getshipmentdetailsresponse_instantiates():
    """Instantiate GetShipmentDetailsResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = GetShipmentDetailsResponse(**kwargs)
    assert isinstance(obj, GetShipmentDetailsResponse)


def test_money_instantiates():
    """Instantiate Money with dummy data"""
    kwargs = {
        "currency_code": None,
        "amount": None,
    }
    obj = Money(**kwargs)
    assert isinstance(obj, Money)


def test_serialnumberslist_instantiates():
    """Instantiate SerialNumbersList with dummy data"""
    kwargs = {}
    obj = SerialNumbersList(**kwargs)
    assert isinstance(obj, SerialNumbersList)


def test_shipmentitem_instantiates():
    """Instantiate ShipmentItem with dummy data"""
    kwargs = {
        "a_s_i_n": None,
        "seller_s_k_u": None,
        "order_item_id": None,
        "title": None,
        "quantity_ordered": None,
        "item_price": None,
        "shipping_price": None,
        "gift_wrap_price": None,
        "shipping_discount": None,
        "promotion_discount": None,
        "serial_numbers": None,
    }
    obj = ShipmentItem(**kwargs)
    assert isinstance(obj, ShipmentItem)


def test_submitinvoicerequestbody_instantiates():
    """Instantiate SubmitInvoiceRequestBody with dummy data"""
    kwargs = {
        "invoice_content": "",
        "marketplace_id": None,
        "content_m_d5_value": "",
    }
    obj = SubmitInvoiceRequestBody(**kwargs)
    assert isinstance(obj, SubmitInvoiceRequestBody)


def test_submitinvoicerequest_instantiates():
    """Instantiate SubmitInvoiceRequest with dummy data"""
    kwargs = {
        "shipment_id": "",
        "body": SubmitInvoiceRequestBody(
            **{"invoice_content": "", "marketplace_id": None, "content_m_d5_value": ""}
        ),
    }
    obj = SubmitInvoiceRequest(**kwargs)
    assert isinstance(obj, SubmitInvoiceRequest)


def test_submitinvoiceresponse_instantiates():
    """Instantiate SubmitInvoiceResponse with dummy data"""
    kwargs = {
        "errors": None,
    }
    obj = SubmitInvoiceResponse(**kwargs)
    assert isinstance(obj, SubmitInvoiceResponse)


def test_taxclassification_instantiates():
    """Instantiate TaxClassification with dummy data"""
    kwargs = {
        "name": None,
        "value": None,
    }
    obj = TaxClassification(**kwargs)
    assert isinstance(obj, TaxClassification)
