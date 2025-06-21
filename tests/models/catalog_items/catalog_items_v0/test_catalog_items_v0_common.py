# Auto-generated tests for sp_api.api.models.catalog_items.catalog_items_v0.common.py
from datetime import datetime

import pytest
from sp_api.api.models.catalog_items.catalog_items_v0.common import (
    Categories, Error, GetRequestSerializer, ListCatalogCategoriesRequest,
    ListCatalogCategoriesResponse, RequestsBaseModel, SpApiBaseModel)


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


def test_categories_instantiates():
    """Instantiate Categories with dummy data"""
    kwargs = {
        "product_category_id": None,
        "product_category_name": None,
        "parent": None,
    }
    obj = Categories(**kwargs)
    assert isinstance(obj, Categories)


def test_error_instantiates():
    """Instantiate Error with dummy data"""
    kwargs = {
        "code": "",
        "message": "",
        "details": None,
    }
    obj = Error(**kwargs)
    assert isinstance(obj, Error)


def test_listcatalogcategoriesrequest_instantiates():
    """Instantiate ListCatalogCategoriesRequest with dummy data"""
    kwargs = {
        "marketplace_id": None,
        "a_s_i_n": None,
        "seller_s_k_u": None,
    }
    obj = ListCatalogCategoriesRequest(**kwargs)
    assert isinstance(obj, ListCatalogCategoriesRequest)


def test_listcatalogcategoriesresponse_instantiates():
    """Instantiate ListCatalogCategoriesResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = ListCatalogCategoriesResponse(**kwargs)
    assert isinstance(obj, ListCatalogCategoriesResponse)
