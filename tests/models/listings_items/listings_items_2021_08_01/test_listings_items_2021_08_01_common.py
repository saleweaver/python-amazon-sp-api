# Auto-generated tests for sp_api.api.models.listings_items.listings_items_2021_08_01.common.py
from datetime import datetime

import pytest
from sp_api.api.models.listings_items.listings_items_2021_08_01.common import (
    Audience, DeleteListingsItemRequest, Error, ErrorList,
    FulfillmentAvailability, GetListingsItemRequest,
    GetListingsItemRequestIncludedDataEnum, GetRequestSerializer, Issue,
    IssueEnforcementAction, IssueEnforcements, IssueExemption,
    IssueExemptionStatusEnum, IssueSeverityEnum, Item, ItemAttributes,
    ItemIdentifiersByMarketplace, ItemImage, ItemOfferByMarketplace,
    ItemOfferByMarketplaceOfferTypeEnum, ItemProcurement,
    ItemProductTypeByMarketplace, ItemRelationship,
    ItemRelationshipsByMarketplace, ItemRelationshipTypeEnum,
    ItemSearchResults, ItemSummaryByMarketplace,
    ItemSummaryByMarketplaceConditionTypeEnum,
    ItemSummaryByMarketplaceStatusEnum, ItemVariationTheme,
    ListingsItemPatchRequestBody, ListingsItemPutRequestBody,
    ListingsItemPutRequestBodyRequirementsEnum, ListingsItemSubmissionResponse,
    ListingsItemSubmissionResponseStatusEnum, Money, Pagination,
    PatchListingsItemRequest, PatchListingsItemRequestIncludedDataEnum,
    PatchListingsItemRequestModeEnum, PatchOperation, PatchOperationOpEnum,
    Points, PutListingsItemRequest, PutListingsItemRequestIncludedDataEnum,
    PutListingsItemRequestModeEnum, RequestsBaseModel,
    SearchListingsItemsRequest, SearchListingsItemsRequestIdentifiersTypeEnum,
    SearchListingsItemsRequestIncludedDataEnum,
    SearchListingsItemsRequestSortByEnum,
    SearchListingsItemsRequestSortOrderEnum,
    SearchListingsItemsRequestWithIssueSeverityEnum,
    SearchListingsItemsRequestWithoutStatusEnum,
    SearchListingsItemsRequestWithStatusEnum, SpApiBaseModel)


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


def test_audience_instantiates():
    """Instantiate Audience with dummy data"""
    kwargs = {
        "value": None,
        "display_name": None,
    }
    obj = Audience(**kwargs)
    assert isinstance(obj, Audience)


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


def test_fulfillmentavailability_instantiates():
    """Instantiate FulfillmentAvailability with dummy data"""
    kwargs = {
        "fulfillment_channel_code": "",
        "quantity": None,
    }
    obj = FulfillmentAvailability(**kwargs)
    assert isinstance(obj, FulfillmentAvailability)


def test_getlistingsitemrequest_instantiates():
    """Instantiate GetListingsItemRequest with dummy data"""
    kwargs = {
        "seller_id": "",
        "sku": "",
        "marketplace_ids": None,
        "issue_locale": None,
        "included_data": None,
    }
    obj = GetListingsItemRequest(**kwargs)
    assert isinstance(obj, GetListingsItemRequest)


def test_issueenforcementaction_instantiates():
    """Instantiate IssueEnforcementAction with dummy data"""
    kwargs = {
        "action": "",
    }
    obj = IssueEnforcementAction(**kwargs)
    assert isinstance(obj, IssueEnforcementAction)


def test_issueexemption_instantiates():
    """Instantiate IssueExemption with dummy data"""
    kwargs = {
        "status": IssueExemptionStatusEnum.EXEMPT,
        "expiry_date": None,
    }
    obj = IssueExemption(**kwargs)
    assert isinstance(obj, IssueExemption)


def test_issueenforcements_instantiates():
    """Instantiate IssueEnforcements with dummy data"""
    kwargs = {
        "actions": [],
        "exemption": IssueExemption(
            **{"status": IssueExemptionStatusEnum.EXEMPT, "expiry_date": None}
        ),
    }
    obj = IssueEnforcements(**kwargs)
    assert isinstance(obj, IssueEnforcements)


def test_issue_instantiates():
    """Instantiate Issue with dummy data"""
    kwargs = {
        "code": "",
        "message": "",
        "severity": IssueSeverityEnum.ERROR,
        "attribute_names": None,
        "categories": [],
        "enforcements": None,
    }
    obj = Issue(**kwargs)
    assert isinstance(obj, Issue)


def test_itemattributes_instantiates():
    """Instantiate ItemAttributes with dummy data"""
    kwargs = {}
    obj = ItemAttributes(**kwargs)
    assert isinstance(obj, ItemAttributes)


def test_money_instantiates():
    """Instantiate Money with dummy data"""
    kwargs = {
        "currency_code": "",
        "amount": "",
    }
    obj = Money(**kwargs)
    assert isinstance(obj, Money)


def test_itemprocurement_instantiates():
    """Instantiate ItemProcurement with dummy data"""
    kwargs = {
        "cost_price": Money(**{"currency_code": "", "amount": ""}),
    }
    obj = ItemProcurement(**kwargs)
    assert isinstance(obj, ItemProcurement)


def test_item_instantiates():
    """Instantiate Item with dummy data"""
    kwargs = {
        "sku": "",
        "summaries": None,
        "attributes": None,
        "issues": None,
        "offers": None,
        "fulfillment_availability": None,
        "procurement": None,
        "relationships": None,
        "product_types": None,
    }
    obj = Item(**kwargs)
    assert isinstance(obj, Item)


def test_itemidentifiersbymarketplace_instantiates():
    """Instantiate ItemIdentifiersByMarketplace with dummy data"""
    kwargs = {
        "marketplace_id": None,
        "asin": None,
    }
    obj = ItemIdentifiersByMarketplace(**kwargs)
    assert isinstance(obj, ItemIdentifiersByMarketplace)


def test_itemimage_instantiates():
    """Instantiate ItemImage with dummy data"""
    kwargs = {
        "link": "",
        "height": 0,
        "width": 0,
    }
    obj = ItemImage(**kwargs)
    assert isinstance(obj, ItemImage)


def test_points_instantiates():
    """Instantiate Points with dummy data"""
    kwargs = {
        "points_number": 0,
    }
    obj = Points(**kwargs)
    assert isinstance(obj, Points)


def test_itemofferbymarketplace_instantiates():
    """Instantiate ItemOfferByMarketplace with dummy data"""
    kwargs = {
        "marketplace_id": None,
        "offer_type": ItemOfferByMarketplaceOfferTypeEnum.B2_C,
        "price": Money(**{"currency_code": "", "amount": ""}),
        "points": None,
        "audience": None,
    }
    obj = ItemOfferByMarketplace(**kwargs)
    assert isinstance(obj, ItemOfferByMarketplace)


def test_itemproducttypebymarketplace_instantiates():
    """Instantiate ItemProductTypeByMarketplace with dummy data"""
    kwargs = {
        "marketplace_id": None,
        "product_type": "",
    }
    obj = ItemProductTypeByMarketplace(**kwargs)
    assert isinstance(obj, ItemProductTypeByMarketplace)


def test_itemvariationtheme_instantiates():
    """Instantiate ItemVariationTheme with dummy data"""
    kwargs = {
        "attributes": [],
        "theme": "",
    }
    obj = ItemVariationTheme(**kwargs)
    assert isinstance(obj, ItemVariationTheme)


def test_itemrelationship_instantiates():
    """Instantiate ItemRelationship with dummy data"""
    kwargs = {
        "child_skus": None,
        "parent_skus": None,
        "variation_theme": None,
        "type": ItemRelationshipTypeEnum.VARIATION,
    }
    obj = ItemRelationship(**kwargs)
    assert isinstance(obj, ItemRelationship)


def test_itemrelationshipsbymarketplace_instantiates():
    """Instantiate ItemRelationshipsByMarketplace with dummy data"""
    kwargs = {
        "marketplace_id": None,
        "relationships": [],
    }
    obj = ItemRelationshipsByMarketplace(**kwargs)
    assert isinstance(obj, ItemRelationshipsByMarketplace)


def test_pagination_instantiates():
    """Instantiate Pagination with dummy data"""
    kwargs = {
        "next_token": None,
        "previous_token": None,
    }
    obj = Pagination(**kwargs)
    assert isinstance(obj, Pagination)


def test_itemsearchresults_instantiates():
    """Instantiate ItemSearchResults with dummy data"""
    kwargs = {
        "number_of_results": 0,
        "pagination": None,
        "items": [],
    }
    obj = ItemSearchResults(**kwargs)
    assert isinstance(obj, ItemSearchResults)


def test_itemsummarybymarketplace_instantiates():
    """Instantiate ItemSummaryByMarketplace with dummy data"""
    kwargs = {
        "marketplace_id": None,
        "asin": None,
        "product_type": "",
        "condition_type": None,
        "status": [],
        "fn_sku": None,
        "item_name": None,
        "created_date": datetime(2000, 1, 1),
        "last_updated_date": datetime(2000, 1, 1),
        "main_image": None,
    }
    obj = ItemSummaryByMarketplace(**kwargs)
    assert isinstance(obj, ItemSummaryByMarketplace)


def test_patchoperation_instantiates():
    """Instantiate PatchOperation with dummy data"""
    kwargs = {
        "op": PatchOperationOpEnum.ADD,
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
        "status": ListingsItemSubmissionResponseStatusEnum.ACCEPTED,
        "submission_id": "",
        "issues": None,
        "identifiers": None,
    }
    obj = ListingsItemSubmissionResponse(**kwargs)
    assert isinstance(obj, ListingsItemSubmissionResponse)


def test_patchlistingsitemrequest_instantiates():
    """Instantiate PatchListingsItemRequest with dummy data"""
    kwargs = {
        "seller_id": "",
        "sku": "",
        "marketplace_ids": None,
        "included_data": None,
        "mode": None,
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
        "included_data": None,
        "mode": None,
        "issue_locale": None,
        "body": ListingsItemPutRequestBody(
            **{"product_type": "", "requirements": None, "attributes": {}}
        ),
    }
    obj = PutListingsItemRequest(**kwargs)
    assert isinstance(obj, PutListingsItemRequest)


def test_searchlistingsitemsrequest_instantiates():
    """Instantiate SearchListingsItemsRequest with dummy data"""
    kwargs = {
        "seller_id": "",
        "marketplace_ids": None,
        "issue_locale": None,
        "included_data": None,
        "identifiers": None,
        "identifiers_type": None,
        "variation_parent_sku": None,
        "package_hierarchy_sku": None,
        "created_after": None,
        "created_before": None,
        "last_updated_after": None,
        "last_updated_before": None,
        "with_issue_severity": None,
        "with_status": None,
        "without_status": None,
        "sort_by": None,
        "sort_order": None,
        "page_size": None,
        "page_token": None,
    }
    obj = SearchListingsItemsRequest(**kwargs)
    assert isinstance(obj, SearchListingsItemsRequest)
