# Auto-generated tests for sp_api.api.models.data_kiosk.data_kiosk_2023_11_15.common.py
from datetime import datetime

import pytest
from sp_api.api.models.data_kiosk.data_kiosk_2023_11_15.common import (
    CancelQueryRequest, CreateQueryRequest, CreateQueryResponse,
    CreateQuerySpecification, Error, ErrorList, GetDocumentRequest,
    GetDocumentResponse, GetQueriesRequest,
    GetQueriesRequestProcessingStatusesEnum, GetQueriesResponse,
    GetQueryRequest, GetRequestSerializer, Query, QueryProcessingStatusEnum,
    RequestsBaseModel, SpApiBaseModel)


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


def test_cancelqueryrequest_instantiates():
    """Instantiate CancelQueryRequest with dummy data"""
    kwargs = {
        "query_id": "",
    }
    obj = CancelQueryRequest(**kwargs)
    assert isinstance(obj, CancelQueryRequest)


def test_createqueryspecification_instantiates():
    """Instantiate CreateQuerySpecification with dummy data"""
    kwargs = {
        "query": "",
        "pagination_token": None,
    }
    obj = CreateQuerySpecification(**kwargs)
    assert isinstance(obj, CreateQuerySpecification)


def test_createqueryrequest_instantiates():
    """Instantiate CreateQueryRequest with dummy data"""
    kwargs = {
        "body": CreateQuerySpecification(**{"query": "", "pagination_token": None}),
    }
    obj = CreateQueryRequest(**kwargs)
    assert isinstance(obj, CreateQueryRequest)


def test_createqueryresponse_instantiates():
    """Instantiate CreateQueryResponse with dummy data"""
    kwargs = {
        "query_id": "",
    }
    obj = CreateQueryResponse(**kwargs)
    assert isinstance(obj, CreateQueryResponse)


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


def test_getdocumentrequest_instantiates():
    """Instantiate GetDocumentRequest with dummy data"""
    kwargs = {
        "document_id": "",
    }
    obj = GetDocumentRequest(**kwargs)
    assert isinstance(obj, GetDocumentRequest)


def test_getdocumentresponse_instantiates():
    """Instantiate GetDocumentResponse with dummy data"""
    kwargs = {
        "document_id": "",
        "document_url": "",
    }
    obj = GetDocumentResponse(**kwargs)
    assert isinstance(obj, GetDocumentResponse)


def test_getqueriesrequest_instantiates():
    """Instantiate GetQueriesRequest with dummy data"""
    kwargs = {
        "processing_statuses": None,
        "page_size": None,
        "created_since": None,
        "created_until": None,
        "pagination_token": None,
    }
    obj = GetQueriesRequest(**kwargs)
    assert isinstance(obj, GetQueriesRequest)


def test_getqueriesresponse_instantiates():
    """Instantiate GetQueriesResponse with dummy data"""
    kwargs = {
        "queries": [],
        "pagination": None,
    }
    obj = GetQueriesResponse(**kwargs)
    assert isinstance(obj, GetQueriesResponse)


def test_getqueryrequest_instantiates():
    """Instantiate GetQueryRequest with dummy data"""
    kwargs = {
        "query_id": "",
    }
    obj = GetQueryRequest(**kwargs)
    assert isinstance(obj, GetQueryRequest)


def test_query_instantiates():
    """Instantiate Query with dummy data"""
    kwargs = {
        "query_id": "",
        "query": "",
        "created_time": datetime(2000, 1, 1),
        "processing_status": QueryProcessingStatusEnum.CANCELLED,
        "processing_start_time": None,
        "processing_end_time": None,
        "data_document_id": None,
        "error_document_id": None,
        "pagination": None,
    }
    obj = Query(**kwargs)
    assert isinstance(obj, Query)
