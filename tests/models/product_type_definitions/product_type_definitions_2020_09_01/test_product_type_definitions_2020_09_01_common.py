# Auto-generated tests for sp_api.api.models.product_type_definitions.product_type_definitions_2020_09_01.common.py
from datetime import datetime

import pytest
from sp_api.api.models.product_type_definitions.product_type_definitions_2020_09_01.common import (
    Error, ErrorList, GetDefinitionsProductTypeRequest, GetRequestSerializer,
    LocaleEnum, ProductType, ProductTypeDefinition, ProductTypeList,
    ProductTypeVersion, PropertyGroup, RequestsBaseModel,
    RequirementsEnforcedEnum, RequirementsEnum, SchemaLink,
    SearchDefinitionsProductTypesRequest, SpApiBaseModel)


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


def test_getdefinitionsproducttyperequest_instantiates():
    """Instantiate GetDefinitionsProductTypeRequest with dummy data"""
    kwargs = {
        "product_type": "",
        "seller_id": None,
        "marketplace_ids": None,
        "product_type_version": None,
        "requirements": None,
        "requirements_enforced": None,
        "locale": None,
    }
    obj = GetDefinitionsProductTypeRequest(**kwargs)
    assert isinstance(obj, GetDefinitionsProductTypeRequest)


def test_producttype_instantiates():
    """Instantiate ProductType with dummy data"""
    kwargs = {
        "name": "",
        "display_name": "",
        "marketplace_ids": None,
    }
    obj = ProductType(**kwargs)
    assert isinstance(obj, ProductType)


def test_producttypeversion_instantiates():
    """Instantiate ProductTypeVersion with dummy data"""
    kwargs = {
        "version": "",
        "latest": False,
        "release_candidate": None,
    }
    obj = ProductTypeVersion(**kwargs)
    assert isinstance(obj, ProductTypeVersion)


def test_schemalink_instantiates():
    """Instantiate SchemaLink with dummy data"""
    kwargs = {
        "link": {},
        "checksum": "",
    }
    obj = SchemaLink(**kwargs)
    assert isinstance(obj, SchemaLink)


def test_producttypedefinition_instantiates():
    """Instantiate ProductTypeDefinition with dummy data"""
    kwargs = {
        "meta_schema": None,
        "schema": SchemaLink(**{"link": {}, "checksum": ""}),
        "requirements": RequirementsEnum.LISTING,
        "requirements_enforced": RequirementsEnforcedEnum.ENFORCED,
        "property_groups": {},
        "locale": "",
        "marketplace_ids": None,
        "product_type": "",
        "display_name": "",
        "product_type_version": ProductTypeVersion(
            **{"version": "", "latest": False, "release_candidate": None}
        ),
    }
    obj = ProductTypeDefinition(**kwargs)
    assert isinstance(obj, ProductTypeDefinition)


def test_producttypelist_instantiates():
    """Instantiate ProductTypeList with dummy data"""
    kwargs = {
        "product_types": [],
        "product_type_version": "",
    }
    obj = ProductTypeList(**kwargs)
    assert isinstance(obj, ProductTypeList)


def test_propertygroup_instantiates():
    """Instantiate PropertyGroup with dummy data"""
    kwargs = {
        "title": None,
        "description": None,
        "property_names": None,
    }
    obj = PropertyGroup(**kwargs)
    assert isinstance(obj, PropertyGroup)


def test_searchdefinitionsproducttypesrequest_instantiates():
    """Instantiate SearchDefinitionsProductTypesRequest with dummy data"""
    kwargs = {
        "keywords": None,
        "marketplace_ids": None,
        "item_name": None,
        "locale": None,
        "search_locale": None,
    }
    obj = SearchDefinitionsProductTypesRequest(**kwargs)
    assert isinstance(obj, SearchDefinitionsProductTypesRequest)
