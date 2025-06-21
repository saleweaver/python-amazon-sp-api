# Auto-generated tests for sp_api.api.models.tokens.tokens_2021_03_01.common.py
from datetime import datetime

import pytest
from sp_api.api.models.tokens.tokens_2021_03_01.common import (
    CreateRestrictedDataTokenRequest, CreateRestrictedDataTokenRequestBody,
    CreateRestrictedDataTokenResponse, Error, ErrorList, GetRequestSerializer,
    MethodEnum, RequestsBaseModel, RestrictedResource, SpApiBaseModel)


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


def test_restrictedresource_instantiates():
    """Instantiate RestrictedResource with dummy data"""
    kwargs = {
        "method": MethodEnum.GET,
        "path": "",
        "data_elements": None,
    }
    obj = RestrictedResource(**kwargs)
    assert isinstance(obj, RestrictedResource)


def test_createrestricteddatatokenrequestbody_instantiates():
    """Instantiate CreateRestrictedDataTokenRequestBody with dummy data"""
    kwargs = {
        "target_application": None,
        "restricted_resources": [],
    }
    obj = CreateRestrictedDataTokenRequestBody(**kwargs)
    assert isinstance(obj, CreateRestrictedDataTokenRequestBody)


def test_createrestricteddatatokenrequest_instantiates():
    """Instantiate CreateRestrictedDataTokenRequest with dummy data"""
    kwargs = {
        "body": CreateRestrictedDataTokenRequestBody(
            **{"target_application": None, "restricted_resources": []}
        ),
    }
    obj = CreateRestrictedDataTokenRequest(**kwargs)
    assert isinstance(obj, CreateRestrictedDataTokenRequest)


def test_createrestricteddatatokenresponse_instantiates():
    """Instantiate CreateRestrictedDataTokenResponse with dummy data"""
    kwargs = {
        "restricted_data_token": None,
        "expires_in": None,
    }
    obj = CreateRestrictedDataTokenResponse(**kwargs)
    assert isinstance(obj, CreateRestrictedDataTokenResponse)


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
        "errors": None,
    }
    obj = ErrorList(**kwargs)
    assert isinstance(obj, ErrorList)
