# Auto-generated tests for sp_api.api.models.uploads.uploads_2020_11_01.common.py
from datetime import datetime

import pytest
from sp_api.api.models.uploads.uploads_2020_11_01.common import (
    CreateUploadDestinationForResourceRequest, CreateUploadDestinationResponse,
    Error, GetRequestSerializer, RequestsBaseModel, SpApiBaseModel,
    UploadDestination)


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


def test_createuploaddestinationforresourcerequest_instantiates():
    """Instantiate CreateUploadDestinationForResourceRequest with dummy data"""
    kwargs = {
        "marketplace_ids": None,
        "content_m_d5": "",
        "resource": "",
        "content_type": None,
    }
    obj = CreateUploadDestinationForResourceRequest(**kwargs)
    assert isinstance(obj, CreateUploadDestinationForResourceRequest)


def test_uploaddestination_instantiates():
    """Instantiate UploadDestination with dummy data"""
    kwargs = {
        "upload_destination_id": None,
        "url": None,
        "headers": None,
    }
    obj = UploadDestination(**kwargs)
    assert isinstance(obj, UploadDestination)


def test_createuploaddestinationresponse_instantiates():
    """Instantiate CreateUploadDestinationResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = CreateUploadDestinationResponse(**kwargs)
    assert isinstance(obj, CreateUploadDestinationResponse)


def test_error_instantiates():
    """Instantiate Error with dummy data"""
    kwargs = {
        "code": "",
        "message": "",
        "details": None,
    }
    obj = Error(**kwargs)
    assert isinstance(obj, Error)
