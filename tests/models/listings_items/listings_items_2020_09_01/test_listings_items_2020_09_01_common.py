# Auto-generated tests for sp_api.api.models.listings_items.listings_items_2020_09_01.common.py
from datetime import datetime

import pytest
from sp_api.api.models.listings_items.listings_items_2020_09_01.common import (
    DeleteListingsItemRequest, Error, ErrorList, GetRequestSerializer, Issue,
    ListingsItemPatchRequestBody, ListingsItemPutRequestBody,
    ListingsItemSubmissionResponse, OpEnum, PatchListingsItemRequest,
    PatchOperation, PutListingsItemRequest, RequestsBaseModel,
    RequirementsEnum, SeverityEnum, SpApiBaseModel, StatusEnum)


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


def test_deletelistingsitemrequest_instantiates():
    """Instantiate DeleteListingsItemRequest with dummy data"""
    kwargs = {
        "seller_id": "",
        "sku": "",
        "marketplace_ids": None,
        "issue_locale": None,
    }
    obj = DeleteListingsItemRequest(**kwargs)
    assert isinstance(obj, DeleteListingsItemRequest)


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


def test_issue_instantiates():
    """Instantiate Issue with dummy data"""
    kwargs = {
        "code": "",
        "message": "",
        "severity": SeverityEnum.ERROR,
        "attribute_name": None,
    }
    obj = Issue(**kwargs)
    assert isinstance(obj, Issue)


def test_patchoperation_instantiates():
    """Instantiate PatchOperation with dummy data"""
    kwargs = {
        "op": OpEnum.ADD,
        "path": "",
        "value": None,
    }
    obj = PatchOperation(**kwargs)
    assert isinstance(obj, PatchOperation)


def test_listingsitempatchrequestbody_instantiates():
    """Instantiate ListingsItemPatchRequestBody with dummy data"""
    kwargs = {
        "product_type": "",
        "patches": [],
    }
    obj = ListingsItemPatchRequestBody(**kwargs)
    assert isinstance(obj, ListingsItemPatchRequestBody)


def test_listingsitemputrequestbody_instantiates():
    """Instantiate ListingsItemPutRequestBody with dummy data"""
    kwargs = {
        "product_type": "",
        "requirements": None,
        "attributes": {},
    }
    obj = ListingsItemPutRequestBody(**kwargs)
    assert isinstance(obj, ListingsItemPutRequestBody)


def test_listingsitemsubmissionresponse_instantiates():
    """Instantiate ListingsItemSubmissionResponse with dummy data"""
    kwargs = {
        "sku": "",
        "status": StatusEnum.ACCEPTED,
        "submission_id": "",
        "issues": None,
    }
    obj = ListingsItemSubmissionResponse(**kwargs)
    assert isinstance(obj, ListingsItemSubmissionResponse)


def test_patchlistingsitemrequest_instantiates():
    """Instantiate PatchListingsItemRequest with dummy data"""
    kwargs = {
        "seller_id": "",
        "sku": "",
        "marketplace_ids": None,
        "issue_locale": None,
        "body": ListingsItemPatchRequestBody(**{"product_type": "", "patches": []}),
    }
    obj = PatchListingsItemRequest(**kwargs)
    assert isinstance(obj, PatchListingsItemRequest)


def test_putlistingsitemrequest_instantiates():
    """Instantiate PutListingsItemRequest with dummy data"""
    kwargs = {
        "seller_id": "",
        "sku": "",
        "marketplace_ids": None,
        "issue_locale": None,
        "body": ListingsItemPutRequestBody(
            **{"product_type": "", "requirements": None, "attributes": {}}
        ),
    }
    obj = PutListingsItemRequest(**kwargs)
    assert isinstance(obj, PutListingsItemRequest)
