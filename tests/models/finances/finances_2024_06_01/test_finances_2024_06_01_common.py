# Auto-generated tests for sp_api.api.models.finances.finances_2024_06_01.common.py
from datetime import datetime

import pytest
from sp_api.api.models.finances.finances_2024_06_01.common import (
    Error, ErrorList, ExpiryDate, GetPaymentMethodsRequest,
    GetPaymentMethodsRequestPaymentMethodTypesEnum, GetPaymentMethodsResponse,
    GetRequestSerializer, InitiatePayoutRequest, InitiatePayoutRequestBody,
    InitiatePayoutResponse, PaymentMethodDetails, RequestsBaseModel,
    SpApiBaseModel)


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


def test_error_instantiates():
    """Instantiate Error with dummy data"""
    kwargs = {
        "code": "",
        "message": "",
        "details": None,
    }
    obj = Error(**kwargs)
    assert isinstance(obj, Error)


def test_errorlist_instantiates():
    """Instantiate ErrorList with dummy data"""
    kwargs = {
        "errors": [],
    }
    obj = ErrorList(**kwargs)
    assert isinstance(obj, ErrorList)


def test_expirydate_instantiates():
    """Instantiate ExpiryDate with dummy data"""
    kwargs = {
        "month": None,
        "year": None,
    }
    obj = ExpiryDate(**kwargs)
    assert isinstance(obj, ExpiryDate)


def test_getpaymentmethodsrequest_instantiates():
    """Instantiate GetPaymentMethodsRequest with dummy data"""
    kwargs = {
        "marketplace_id": None,
        "payment_method_types": None,
    }
    obj = GetPaymentMethodsRequest(**kwargs)
    assert isinstance(obj, GetPaymentMethodsRequest)


def test_getpaymentmethodsresponse_instantiates():
    """Instantiate GetPaymentMethodsResponse with dummy data"""
    kwargs = {
        "payment_methods": None,
    }
    obj = GetPaymentMethodsResponse(**kwargs)
    assert isinstance(obj, GetPaymentMethodsResponse)


def test_initiatepayoutrequestbody_instantiates():
    """Instantiate InitiatePayoutRequestBody with dummy data"""
    kwargs = {
        "marketplace_id": None,
        "account_type": "",
    }
    obj = InitiatePayoutRequestBody(**kwargs)
    assert isinstance(obj, InitiatePayoutRequestBody)


def test_initiatepayoutrequest_instantiates():
    """Instantiate InitiatePayoutRequest with dummy data"""
    kwargs = {
        "body": InitiatePayoutRequestBody(
            **{"marketplace_id": None, "account_type": ""}
        ),
    }
    obj = InitiatePayoutRequest(**kwargs)
    assert isinstance(obj, InitiatePayoutRequest)


def test_initiatepayoutresponse_instantiates():
    """Instantiate InitiatePayoutResponse with dummy data"""
    kwargs = {
        "payout_reference_id": "",
    }
    obj = InitiatePayoutResponse(**kwargs)
    assert isinstance(obj, InitiatePayoutResponse)


def test_paymentmethoddetails_instantiates():
    """Instantiate PaymentMethodDetails with dummy data"""
    kwargs = {
        "account_holder_name": None,
        "payment_method_id": None,
        "tail": None,
        "expiry_date": None,
        "country_code": None,
        "payment_method_type": None,
        "assignment_type": None,
    }
    obj = PaymentMethodDetails(**kwargs)
    assert isinstance(obj, PaymentMethodDetails)
