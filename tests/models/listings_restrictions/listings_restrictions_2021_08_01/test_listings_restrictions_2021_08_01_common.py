# Auto-generated tests for sp_api.api.models.listings_restrictions.listings_restrictions_2021_08_01.common.py
from datetime import datetime

import pytest
from sp_api.api.models.listings_restrictions.listings_restrictions_2021_08_01.common import (
    ConditionTypeEnum, Error, GetListingsRestrictionsRequest,
    GetRequestSerializer, Link, Reason, ReasonCodeEnum, RequestsBaseModel,
    Restriction, RestrictionList, SpApiBaseModel, VerbEnum)


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


def test_getlistingsrestrictionsrequest_instantiates():
    """Instantiate GetListingsRestrictionsRequest with dummy data"""
    kwargs = {
        "asin": "",
        "condition_type": None,
        "seller_id": "",
        "marketplace_ids": None,
        "reason_locale": None,
    }
    obj = GetListingsRestrictionsRequest(**kwargs)
    assert isinstance(obj, GetListingsRestrictionsRequest)


def test_link_instantiates():
    """Instantiate Link with dummy data"""
    kwargs = {
        "resource": "",
        "verb": VerbEnum.GET,
        "title": None,
        "type": None,
    }
    obj = Link(**kwargs)
    assert isinstance(obj, Link)


def test_reason_instantiates():
    """Instantiate Reason with dummy data"""
    kwargs = {
        "message": "",
        "reason_code": None,
        "links": None,
    }
    obj = Reason(**kwargs)
    assert isinstance(obj, Reason)


def test_restriction_instantiates():
    """Instantiate Restriction with dummy data"""
    kwargs = {
        "marketplace_id": None,
        "condition_type": None,
        "reasons": None,
    }
    obj = Restriction(**kwargs)
    assert isinstance(obj, Restriction)


def test_restrictionlist_instantiates():
    """Instantiate RestrictionList with dummy data"""
    kwargs = {
        "restrictions": [],
    }
    obj = RestrictionList(**kwargs)
    assert isinstance(obj, RestrictionList)
