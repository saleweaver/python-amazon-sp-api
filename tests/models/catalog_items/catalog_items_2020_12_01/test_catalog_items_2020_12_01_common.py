# Auto-generated tests for sp_api.api.models.catalog_items.catalog_items_2020_12_01.common.py
from datetime import datetime

import pytest
from sp_api.api.models.catalog_items.catalog_items_2020_12_01.common import (
    BrandRefinement, ClassificationRefinement, Error, ErrorList,
    GetCatalogItemRequest, GetRequestSerializer, IncludedDataEnum, Item,
    ItemAttributes, ItemIdentifier, ItemIdentifiersByMarketplace, ItemImage,
    ItemImagesByMarketplace, ItemProductTypeByMarketplace, ItemSalesRank,
    ItemSalesRanksByMarketplace, ItemSearchResults, ItemSummaryByMarketplace,
    ItemVariationsByMarketplace, ItemVendorDetailsByMarketplace, Pagination,
    Refinements, ReplenishmentCategoryEnum, RequestsBaseModel,
    SearchCatalogItemsRequest, SpApiBaseModel, VariantEnum, VariationTypeEnum)


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


def test_brandrefinement_instantiates():
    """Instantiate BrandRefinement with dummy data"""
    kwargs = {
        "number_of_results": 0,
        "brand_name": "",
    }
    obj = BrandRefinement(**kwargs)
    assert isinstance(obj, BrandRefinement)


def test_classificationrefinement_instantiates():
    """Instantiate ClassificationRefinement with dummy data"""
    kwargs = {
        "number_of_results": 0,
        "display_name": "",
        "classification_id": "",
    }
    obj = ClassificationRefinement(**kwargs)
    assert isinstance(obj, ClassificationRefinement)


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


def test_getcatalogitemrequest_instantiates():
    """Instantiate GetCatalogItemRequest with dummy data"""
    kwargs = {
        "asin": "",
        "marketplace_ids": None,
        "included_data": None,
        "locale": None,
    }
    obj = GetCatalogItemRequest(**kwargs)
    assert isinstance(obj, GetCatalogItemRequest)


def test_itemattributes_instantiates():
    """Instantiate ItemAttributes with dummy data"""
    kwargs = {}
    obj = ItemAttributes(**kwargs)
    assert isinstance(obj, ItemAttributes)


def test_item_instantiates():
    """Instantiate Item with dummy data"""
    kwargs = {
        "asin": "",
        "attributes": None,
        "identifiers": None,
        "images": None,
        "product_types": None,
        "sales_ranks": None,
        "summaries": None,
        "variations": None,
        "vendor_details": None,
    }
    obj = Item(**kwargs)
    assert isinstance(obj, Item)


def test_itemidentifier_instantiates():
    """Instantiate ItemIdentifier with dummy data"""
    kwargs = {
        "identifier_type": "",
        "identifier": "",
    }
    obj = ItemIdentifier(**kwargs)
    assert isinstance(obj, ItemIdentifier)


def test_itemidentifiersbymarketplace_instantiates():
    """Instantiate ItemIdentifiersByMarketplace with dummy data"""
    kwargs = {
        "marketplace_id": None,
        "identifiers": [],
    }
    obj = ItemIdentifiersByMarketplace(**kwargs)
    assert isinstance(obj, ItemIdentifiersByMarketplace)


def test_itemimage_instantiates():
    """Instantiate ItemImage with dummy data"""
    kwargs = {
        "variant": VariantEnum.MAIN,
        "link": "",
        "height": 0,
        "width": 0,
    }
    obj = ItemImage(**kwargs)
    assert isinstance(obj, ItemImage)


def test_itemimagesbymarketplace_instantiates():
    """Instantiate ItemImagesByMarketplace with dummy data"""
    kwargs = {
        "marketplace_id": None,
        "images": [],
    }
    obj = ItemImagesByMarketplace(**kwargs)
    assert isinstance(obj, ItemImagesByMarketplace)


def test_itemproducttypebymarketplace_instantiates():
    """Instantiate ItemProductTypeByMarketplace with dummy data"""
    kwargs = {
        "marketplace_id": None,
        "product_type": None,
    }
    obj = ItemProductTypeByMarketplace(**kwargs)
    assert isinstance(obj, ItemProductTypeByMarketplace)


def test_itemsalesrank_instantiates():
    """Instantiate ItemSalesRank with dummy data"""
    kwargs = {
        "title": "",
        "link": None,
        "rank": 0,
    }
    obj = ItemSalesRank(**kwargs)
    assert isinstance(obj, ItemSalesRank)


def test_itemsalesranksbymarketplace_instantiates():
    """Instantiate ItemSalesRanksByMarketplace with dummy data"""
    kwargs = {
        "marketplace_id": None,
        "ranks": [],
    }
    obj = ItemSalesRanksByMarketplace(**kwargs)
    assert isinstance(obj, ItemSalesRanksByMarketplace)


def test_pagination_instantiates():
    """Instantiate Pagination with dummy data"""
    kwargs = {
        "next_token": None,
        "previous_token": None,
    }
    obj = Pagination(**kwargs)
    assert isinstance(obj, Pagination)


def test_refinements_instantiates():
    """Instantiate Refinements with dummy data"""
    kwargs = {
        "brands": [],
        "classifications": [],
    }
    obj = Refinements(**kwargs)
    assert isinstance(obj, Refinements)


def test_itemsearchresults_instantiates():
    """Instantiate ItemSearchResults with dummy data"""
    kwargs = {
        "number_of_results": 0,
        "pagination": Pagination(**{"next_token": None, "previous_token": None}),
        "refinements": Refinements(**{"brands": [], "classifications": []}),
        "items": [],
    }
    obj = ItemSearchResults(**kwargs)
    assert isinstance(obj, ItemSearchResults)


def test_itemsummarybymarketplace_instantiates():
    """Instantiate ItemSummaryByMarketplace with dummy data"""
    kwargs = {
        "marketplace_id": None,
        "brand_name": None,
        "browse_node": None,
        "color_name": None,
        "item_name": None,
        "manufacturer": None,
        "model_number": None,
        "size_name": None,
        "style_name": None,
    }
    obj = ItemSummaryByMarketplace(**kwargs)
    assert isinstance(obj, ItemSummaryByMarketplace)


def test_itemvariationsbymarketplace_instantiates():
    """Instantiate ItemVariationsByMarketplace with dummy data"""
    kwargs = {
        "marketplace_id": None,
        "asins": [],
        "variation_type": VariationTypeEnum.PARENT,
    }
    obj = ItemVariationsByMarketplace(**kwargs)
    assert isinstance(obj, ItemVariationsByMarketplace)


def test_itemvendordetailsbymarketplace_instantiates():
    """Instantiate ItemVendorDetailsByMarketplace with dummy data"""
    kwargs = {
        "marketplace_id": None,
        "brand_code": None,
        "category_code": None,
        "manufacturer_code": None,
        "manufacturer_code_parent": None,
        "product_group": None,
        "replenishment_category": None,
        "subcategory_code": None,
    }
    obj = ItemVendorDetailsByMarketplace(**kwargs)
    assert isinstance(obj, ItemVendorDetailsByMarketplace)


def test_searchcatalogitemsrequest_instantiates():
    """Instantiate SearchCatalogItemsRequest with dummy data"""
    kwargs = {
        "keywords": [],
        "marketplace_ids": None,
        "included_data": None,
        "brand_names": None,
        "classification_ids": None,
        "page_size": None,
        "page_token": None,
        "keywords_locale": None,
        "locale": None,
    }
    obj = SearchCatalogItemsRequest(**kwargs)
    assert isinstance(obj, SearchCatalogItemsRequest)
