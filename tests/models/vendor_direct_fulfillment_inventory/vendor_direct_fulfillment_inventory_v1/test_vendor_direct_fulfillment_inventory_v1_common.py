# Auto-generated tests for sp_api.api.models.vendor_direct_fulfillment_inventory.vendor_direct_fulfillment_inventory_v1.common.py
from datetime import datetime

import pytest
from sp_api.api.models.vendor_direct_fulfillment_inventory.vendor_direct_fulfillment_inventory_v1.common import (
    Error, GetRequestSerializer, InventoryUpdate, ItemDetails, ItemQuantity,
    PartyIdentification, RequestsBaseModel, SpApiBaseModel,
    SubmitInventoryUpdateRequest, SubmitInventoryUpdateRequestBody,
    SubmitInventoryUpdateResponse, TransactionReference)


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


def test_itemquantity_instantiates():
    """Instantiate ItemQuantity with dummy data"""
    kwargs = {
        "amount": None,
        "unit_of_measure": "",
    }
    obj = ItemQuantity(**kwargs)
    assert isinstance(obj, ItemQuantity)


def test_itemdetails_instantiates():
    """Instantiate ItemDetails with dummy data"""
    kwargs = {
        "buyer_product_identifier": None,
        "vendor_product_identifier": None,
        "available_quantity": ItemQuantity(**{"amount": None, "unit_of_measure": ""}),
        "is_obsolete": None,
    }
    obj = ItemDetails(**kwargs)
    assert isinstance(obj, ItemDetails)


def test_partyidentification_instantiates():
    """Instantiate PartyIdentification with dummy data"""
    kwargs = {
        "party_id": "",
    }
    obj = PartyIdentification(**kwargs)
    assert isinstance(obj, PartyIdentification)


def test_inventoryupdate_instantiates():
    """Instantiate InventoryUpdate with dummy data"""
    kwargs = {
        "selling_party": PartyIdentification(**{"party_id": ""}),
        "is_full_update": False,
        "items": [],
    }
    obj = InventoryUpdate(**kwargs)
    assert isinstance(obj, InventoryUpdate)


def test_submitinventoryupdaterequestbody_instantiates():
    """Instantiate SubmitInventoryUpdateRequestBody with dummy data"""
    kwargs = {
        "inventory": None,
    }
    obj = SubmitInventoryUpdateRequestBody(**kwargs)
    assert isinstance(obj, SubmitInventoryUpdateRequestBody)


def test_submitinventoryupdaterequest_instantiates():
    """Instantiate SubmitInventoryUpdateRequest with dummy data"""
    kwargs = {
        "body": SubmitInventoryUpdateRequestBody(**{"inventory": None}),
        "warehouse_id": "",
    }
    obj = SubmitInventoryUpdateRequest(**kwargs)
    assert isinstance(obj, SubmitInventoryUpdateRequest)


def test_transactionreference_instantiates():
    """Instantiate TransactionReference with dummy data"""
    kwargs = {
        "transaction_id": None,
    }
    obj = TransactionReference(**kwargs)
    assert isinstance(obj, TransactionReference)


def test_submitinventoryupdateresponse_instantiates():
    """Instantiate SubmitInventoryUpdateResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = SubmitInventoryUpdateResponse(**kwargs)
    assert isinstance(obj, SubmitInventoryUpdateResponse)
