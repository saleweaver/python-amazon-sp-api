# Auto-generated tests for sp_api.api.models.vendor_direct_fulfillment_sandbox_test_data.vendor_direct_fulfillment_sandbox_test_data_2021_10_28.common.py
from datetime import datetime

import pytest
from sp_api.api.models.vendor_direct_fulfillment_sandbox_test_data.vendor_direct_fulfillment_sandbox_test_data_2021_10_28.common import (
    Error, ErrorList, GenerateOrderScenarioRequestBody,
    GenerateOrderScenariosRequest, GetOrderScenariosRequest,
    GetRequestSerializer, OrderScenarioRequestBody, Pagination,
    PartyIdentification, RequestsBaseModel, Scenario, SpApiBaseModel,
    TestCaseData, TestOrder, Transaction, TransactionReference,
    TransactionStatus, TransactionStatusEnum)


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


def test_partyidentification_instantiates():
    """Instantiate PartyIdentification with dummy data"""
    kwargs = {
        "party_id": "",
    }
    obj = PartyIdentification(**kwargs)
    assert isinstance(obj, PartyIdentification)


def test_orderscenariorequestbody_instantiates():
    """Instantiate OrderScenarioRequestBody with dummy data"""
    kwargs = {
        "selling_party": PartyIdentification(**{"party_id": ""}),
        "ship_from_party": PartyIdentification(**{"party_id": ""}),
    }
    obj = OrderScenarioRequestBody(**kwargs)
    assert isinstance(obj, OrderScenarioRequestBody)


def test_generateorderscenariorequestbody_instantiates():
    """Instantiate GenerateOrderScenarioRequestBody with dummy data"""
    kwargs = {
        "orders": None,
    }
    obj = GenerateOrderScenarioRequestBody(**kwargs)
    assert isinstance(obj, GenerateOrderScenarioRequestBody)


def test_generateorderscenariosrequest_instantiates():
    """Instantiate GenerateOrderScenariosRequest with dummy data"""
    kwargs = {
        "body": GenerateOrderScenarioRequestBody(**{"orders": None}),
    }
    obj = GenerateOrderScenariosRequest(**kwargs)
    assert isinstance(obj, GenerateOrderScenariosRequest)


def test_getorderscenariosrequest_instantiates():
    """Instantiate GetOrderScenariosRequest with dummy data"""
    kwargs = {
        "transaction_id": "",
    }
    obj = GetOrderScenariosRequest(**kwargs)
    assert isinstance(obj, GetOrderScenariosRequest)


def test_pagination_instantiates():
    """Instantiate Pagination with dummy data"""
    kwargs = {
        "next_token": None,
    }
    obj = Pagination(**kwargs)
    assert isinstance(obj, Pagination)


def test_testorder_instantiates():
    """Instantiate TestOrder with dummy data"""
    kwargs = {
        "order_id": "",
    }
    obj = TestOrder(**kwargs)
    assert isinstance(obj, TestOrder)


def test_scenario_instantiates():
    """Instantiate Scenario with dummy data"""
    kwargs = {
        "scenario_id": "",
        "orders": [],
    }
    obj = Scenario(**kwargs)
    assert isinstance(obj, Scenario)


def test_testcasedata_instantiates():
    """Instantiate TestCaseData with dummy data"""
    kwargs = {
        "scenarios": None,
    }
    obj = TestCaseData(**kwargs)
    assert isinstance(obj, TestCaseData)


def test_transaction_instantiates():
    """Instantiate Transaction with dummy data"""
    kwargs = {
        "transaction_id": "",
        "status": TransactionStatusEnum.FAILURE,
        "test_case_data": None,
    }
    obj = Transaction(**kwargs)
    assert isinstance(obj, Transaction)


def test_transactionreference_instantiates():
    """Instantiate TransactionReference with dummy data"""
    kwargs = {
        "transaction_id": None,
    }
    obj = TransactionReference(**kwargs)
    assert isinstance(obj, TransactionReference)


def test_transactionstatus_instantiates():
    """Instantiate TransactionStatus with dummy data"""
    kwargs = {
        "transaction_status": None,
    }
    obj = TransactionStatus(**kwargs)
    assert isinstance(obj, TransactionStatus)
