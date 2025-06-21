# Auto-generated tests for sp_api.api.models.fba_inbound_eligibility.fba_inbound_eligibility_v1.common.py
from datetime import datetime

import pytest
from sp_api.api.models.fba_inbound_eligibility.fba_inbound_eligibility_v1.common import (
    Error, GetItemEligibilityPreviewRequest, GetItemEligibilityPreviewResponse,
    GetRequestSerializer, IneligibilityReasonListEnum, ItemEligibilityPreview,
    ProgramEnum, RequestsBaseModel, SpApiBaseModel)


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
        "message": None,
        "details": None,
    }
    obj = Error(**kwargs)
    assert isinstance(obj, Error)


def test_getitemeligibilitypreviewrequest_instantiates():
    """Instantiate GetItemEligibilityPreviewRequest with dummy data"""
    kwargs = {
        "marketplace_ids": None,
        "asin": "",
        "program": ProgramEnum.INBOUND,
    }
    obj = GetItemEligibilityPreviewRequest(**kwargs)
    assert isinstance(obj, GetItemEligibilityPreviewRequest)


def test_itemeligibilitypreview_instantiates():
    """Instantiate ItemEligibilityPreview with dummy data"""
    kwargs = {
        "asin": "",
        "marketplace_id": None,
        "program": ProgramEnum.INBOUND,
        "is_eligible_for_program": False,
        "ineligibility_reason_list": None,
    }
    obj = ItemEligibilityPreview(**kwargs)
    assert isinstance(obj, ItemEligibilityPreview)


def test_getitemeligibilitypreviewresponse_instantiates():
    """Instantiate GetItemEligibilityPreviewResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = GetItemEligibilityPreviewResponse(**kwargs)
    assert isinstance(obj, GetItemEligibilityPreviewResponse)
