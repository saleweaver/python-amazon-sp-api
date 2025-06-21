# Auto-generated tests for sp_api.api.models.vendor_direct_fulfillment_transactions.vendor_direct_fulfillment_transactions_2021_12_28.common.py
from datetime import datetime

import pytest
from sp_api.api.models.vendor_direct_fulfillment_transactions.vendor_direct_fulfillment_transactions_2021_12_28.common import (
    Error, ErrorList, GetRequestSerializer, GetTransactionStatusRequest,
    RequestsBaseModel, SpApiBaseModel, StatusEnum, Transaction,
    TransactionStatus)


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


def test_gettransactionstatusrequest_instantiates():
    """Instantiate GetTransactionStatusRequest with dummy data"""
    kwargs = {
        "transaction_id": "",
    }
    obj = GetTransactionStatusRequest(**kwargs)
    assert isinstance(obj, GetTransactionStatusRequest)


def test_transaction_instantiates():
    """Instantiate Transaction with dummy data"""
    kwargs = {
        "transaction_id": "",
        "status": StatusEnum.FAILURE,
        "errors": None,
    }
    obj = Transaction(**kwargs)
    assert isinstance(obj, Transaction)


def test_transactionstatus_instantiates():
    """Instantiate TransactionStatus with dummy data"""
    kwargs = {
        "transaction_status": None,
    }
    obj = TransactionStatus(**kwargs)
    assert isinstance(obj, TransactionStatus)
