# Auto-generated tests for sp_api.api.models.fba_inventory.fba_inventory_v1.common.py
from datetime import datetime

import pytest
from sp_api.api.models.fba_inventory.fba_inventory_v1.common import (
    AddInventoryRequest, AddInventoryRequestBody, AddInventoryResponse,
    CreateInventoryItemRequest, CreateInventoryItemRequestBody,
    CreateInventoryItemResponse, DeleteInventoryItemRequest,
    DeleteInventoryItemResponse, Error, GetInventorySummariesRequest,
    GetInventorySummariesRequestGranularityTypeEnum,
    GetInventorySummariesResponse, GetInventorySummariesResult,
    GetRequestSerializer, Granularity, InventoryDetails, InventoryItem,
    InventorySummary, Pagination, RequestsBaseModel, ResearchingQuantity,
    ResearchingQuantityEntry, ResearchingQuantityEntryNameEnum,
    ReservedQuantity, SpApiBaseModel, UnfulfillableQuantity)


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


def test_addinventoryrequestbody_instantiates():
    """Instantiate AddInventoryRequestBody with dummy data"""
    kwargs = {
        "inventory_items": None,
    }
    obj = AddInventoryRequestBody(**kwargs)
    assert isinstance(obj, AddInventoryRequestBody)


def test_addinventoryrequest_instantiates():
    """Instantiate AddInventoryRequest with dummy data"""
    kwargs = {
        "add_inventory_request_body": AddInventoryRequestBody(
            **{"inventory_items": None}
        ),
    }
    obj = AddInventoryRequest(**kwargs)
    assert isinstance(obj, AddInventoryRequest)


def test_addinventoryresponse_instantiates():
    """Instantiate AddInventoryResponse with dummy data"""
    kwargs = {
        "errors": None,
    }
    obj = AddInventoryResponse(**kwargs)
    assert isinstance(obj, AddInventoryResponse)


def test_createinventoryitemrequestbody_instantiates():
    """Instantiate CreateInventoryItemRequestBody with dummy data"""
    kwargs = {
        "seller_sku": "",
        "marketplace_id": None,
        "product_name": "",
    }
    obj = CreateInventoryItemRequestBody(**kwargs)
    assert isinstance(obj, CreateInventoryItemRequestBody)


def test_createinventoryitemrequest_instantiates():
    """Instantiate CreateInventoryItemRequest with dummy data"""
    kwargs = {
        "create_inventory_item_request_body": CreateInventoryItemRequestBody(
            **{"seller_sku": "", "marketplace_id": None, "product_name": ""}
        ),
    }
    obj = CreateInventoryItemRequest(**kwargs)
    assert isinstance(obj, CreateInventoryItemRequest)


def test_createinventoryitemresponse_instantiates():
    """Instantiate CreateInventoryItemResponse with dummy data"""
    kwargs = {
        "errors": None,
    }
    obj = CreateInventoryItemResponse(**kwargs)
    assert isinstance(obj, CreateInventoryItemResponse)


def test_deleteinventoryitemrequest_instantiates():
    """Instantiate DeleteInventoryItemRequest with dummy data"""
    kwargs = {
        "seller_sku": "",
        "marketplace_id": None,
    }
    obj = DeleteInventoryItemRequest(**kwargs)
    assert isinstance(obj, DeleteInventoryItemRequest)


def test_deleteinventoryitemresponse_instantiates():
    """Instantiate DeleteInventoryItemResponse with dummy data"""
    kwargs = {
        "errors": None,
    }
    obj = DeleteInventoryItemResponse(**kwargs)
    assert isinstance(obj, DeleteInventoryItemResponse)


def test_error_instantiates():
    """Instantiate Error with dummy data"""
    kwargs = {
        "code": "",
        "message": None,
        "details": None,
    }
    obj = Error(**kwargs)
    assert isinstance(obj, Error)


def test_getinventorysummariesrequest_instantiates():
    """Instantiate GetInventorySummariesRequest with dummy data"""
    kwargs = {
        "details": None,
        "granularity_type": GetInventorySummariesRequestGranularityTypeEnum.MARKETPLACE,
        "granularity_id": "",
        "start_date_time": None,
        "seller_skus": None,
        "seller_sku": None,
        "next_token": None,
        "marketplace_ids": None,
    }
    obj = GetInventorySummariesRequest(**kwargs)
    assert isinstance(obj, GetInventorySummariesRequest)


def test_granularity_instantiates():
    """Instantiate Granularity with dummy data"""
    kwargs = {
        "granularity_type": None,
        "granularity_id": None,
    }
    obj = Granularity(**kwargs)
    assert isinstance(obj, Granularity)


def test_getinventorysummariesresult_instantiates():
    """Instantiate GetInventorySummariesResult with dummy data"""
    kwargs = {
        "granularity": Granularity(
            **{"granularity_type": None, "granularity_id": None}
        ),
        "inventory_summaries": [],
    }
    obj = GetInventorySummariesResult(**kwargs)
    assert isinstance(obj, GetInventorySummariesResult)


def test_pagination_instantiates():
    """Instantiate Pagination with dummy data"""
    kwargs = {
        "next_token": None,
    }
    obj = Pagination(**kwargs)
    assert isinstance(obj, Pagination)


def test_getinventorysummariesresponse_instantiates():
    """Instantiate GetInventorySummariesResponse with dummy data"""
    kwargs = {
        "payload": None,
        "pagination": None,
        "errors": None,
    }
    obj = GetInventorySummariesResponse(**kwargs)
    assert isinstance(obj, GetInventorySummariesResponse)


def test_researchingquantityentry_instantiates():
    """Instantiate ResearchingQuantityEntry with dummy data"""
    kwargs = {
        "name": ResearchingQuantityEntryNameEnum.RESEARCHING_QUANTITY_IN_SHORT_TERM,
        "quantity": 0,
    }
    obj = ResearchingQuantityEntry(**kwargs)
    assert isinstance(obj, ResearchingQuantityEntry)


def test_researchingquantity_instantiates():
    """Instantiate ResearchingQuantity with dummy data"""
    kwargs = {
        "total_researching_quantity": None,
        "researching_quantity_breakdown": None,
    }
    obj = ResearchingQuantity(**kwargs)
    assert isinstance(obj, ResearchingQuantity)


def test_reservedquantity_instantiates():
    """Instantiate ReservedQuantity with dummy data"""
    kwargs = {
        "total_reserved_quantity": None,
        "pending_customer_order_quantity": None,
        "pending_transshipment_quantity": None,
        "fc_processing_quantity": None,
    }
    obj = ReservedQuantity(**kwargs)
    assert isinstance(obj, ReservedQuantity)


def test_unfulfillablequantity_instantiates():
    """Instantiate UnfulfillableQuantity with dummy data"""
    kwargs = {
        "total_unfulfillable_quantity": None,
        "customer_damaged_quantity": None,
        "warehouse_damaged_quantity": None,
        "distributor_damaged_quantity": None,
        "carrier_damaged_quantity": None,
        "defective_quantity": None,
        "expired_quantity": None,
    }
    obj = UnfulfillableQuantity(**kwargs)
    assert isinstance(obj, UnfulfillableQuantity)


def test_inventorydetails_instantiates():
    """Instantiate InventoryDetails with dummy data"""
    kwargs = {
        "fulfillable_quantity": None,
        "inbound_working_quantity": None,
        "inbound_shipped_quantity": None,
        "inbound_receiving_quantity": None,
        "reserved_quantity": None,
        "researching_quantity": None,
        "unfulfillable_quantity": None,
    }
    obj = InventoryDetails(**kwargs)
    assert isinstance(obj, InventoryDetails)


def test_inventoryitem_instantiates():
    """Instantiate InventoryItem with dummy data"""
    kwargs = {
        "seller_sku": "",
        "marketplace_id": None,
        "quantity": 0,
    }
    obj = InventoryItem(**kwargs)
    assert isinstance(obj, InventoryItem)


def test_inventorysummary_instantiates():
    """Instantiate InventorySummary with dummy data"""
    kwargs = {
        "asin": None,
        "fn_sku": None,
        "seller_sku": None,
        "condition": None,
        "inventory_details": None,
        "last_updated_time": None,
        "product_name": None,
        "total_quantity": None,
        "stores": None,
    }
    obj = InventorySummary(**kwargs)
    assert isinstance(obj, InventorySummary)
