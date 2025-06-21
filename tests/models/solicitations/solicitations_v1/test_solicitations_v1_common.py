# Auto-generated tests for sp_api.api.models.solicitations.solicitations_v1.common.py
from datetime import datetime

import pytest
from sp_api.api.models.solicitations.solicitations_v1.common import (
    CreateProductReviewAndSellerFeedbackSolicitationRequest,
    CreateProductReviewAndSellerFeedbackSolicitationResponse, Error,
    GetRequestSerializer, GetSchemaResponse, GetSolicitationActionResponse,
    GetSolicitationActionsForOrderRequest,
    GetSolicitationActionsForOrderResponse, LinkObject, RequestsBaseModel,
    Schema, SolicitationsAction, SpApiBaseModel)


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


def test_createproductreviewandsellerfeedbacksolicitationrequest_instantiates():
    """Instantiate CreateProductReviewAndSellerFeedbackSolicitationRequest with dummy data"""
    kwargs = {
        "amazon_order_id": "",
        "marketplace_ids": None,
    }
    obj = CreateProductReviewAndSellerFeedbackSolicitationRequest(**kwargs)
    assert isinstance(obj, CreateProductReviewAndSellerFeedbackSolicitationRequest)


def test_createproductreviewandsellerfeedbacksolicitationresponse_instantiates():
    """Instantiate CreateProductReviewAndSellerFeedbackSolicitationResponse with dummy data"""
    kwargs = {
        "errors": None,
    }
    obj = CreateProductReviewAndSellerFeedbackSolicitationResponse(**kwargs)
    assert isinstance(obj, CreateProductReviewAndSellerFeedbackSolicitationResponse)


def test_error_instantiates():
    """Instantiate Error with dummy data"""
    kwargs = {
        "code": "",
        "message": "",
        "details": None,
    }
    obj = Error(**kwargs)
    assert isinstance(obj, Error)


def test_schema_instantiates():
    """Instantiate Schema with dummy data"""
    kwargs = {}
    obj = Schema(**kwargs)
    assert isinstance(obj, Schema)


def test_getschemaresponse_instantiates():
    """Instantiate GetSchemaResponse with dummy data"""
    kwargs = {
        "links": None,
        "payload": None,
        "errors": None,
    }
    obj = GetSchemaResponse(**kwargs)
    assert isinstance(obj, GetSchemaResponse)


def test_solicitationsaction_instantiates():
    """Instantiate SolicitationsAction with dummy data"""
    kwargs = {
        "name": "",
    }
    obj = SolicitationsAction(**kwargs)
    assert isinstance(obj, SolicitationsAction)


def test_getsolicitationactionresponse_instantiates():
    """Instantiate GetSolicitationActionResponse with dummy data"""
    kwargs = {
        "links": None,
        "embedded": None,
        "payload": None,
        "errors": None,
    }
    obj = GetSolicitationActionResponse(**kwargs)
    assert isinstance(obj, GetSolicitationActionResponse)


def test_getsolicitationactionsfororderrequest_instantiates():
    """Instantiate GetSolicitationActionsForOrderRequest with dummy data"""
    kwargs = {
        "amazon_order_id": "",
        "marketplace_ids": None,
    }
    obj = GetSolicitationActionsForOrderRequest(**kwargs)
    assert isinstance(obj, GetSolicitationActionsForOrderRequest)


def test_getsolicitationactionsfororderresponse_instantiates():
    """Instantiate GetSolicitationActionsForOrderResponse with dummy data"""
    kwargs = {
        "links": None,
        "embedded": None,
        "errors": None,
    }
    obj = GetSolicitationActionsForOrderResponse(**kwargs)
    assert isinstance(obj, GetSolicitationActionsForOrderResponse)


def test_linkobject_instantiates():
    """Instantiate LinkObject with dummy data"""
    kwargs = {
        "href": "",
        "name": None,
    }
    obj = LinkObject(**kwargs)
    assert isinstance(obj, LinkObject)
