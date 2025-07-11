# Auto-generated tests for sp_api.api.models.catalog_items.catalog_items_2022_04_01.common.py
from datetime import datetime

import pytest
from sp_api.api.models.catalog_items.catalog_items_2022_04_01.common import (
    BrandRefinement, ClassificationRefinement, Dimension, Dimensions, Error,
    ErrorList, GetCatalogItemRequest, GetCatalogItemRequestIncludedDataEnum,
    GetRequestSerializer, Item, ItemAttributes, ItemBrowseClassification,
    ItemBrowseClassificationsByMarketplace, ItemClassificationSalesRank,
    ItemContributor, ItemContributorRole, ItemDimensionsByMarketplace,
    ItemDisplayGroupSalesRank, ItemIdentifier, ItemIdentifiersByMarketplace,
    ItemImage, ItemImagesByMarketplace, ItemImageVariantEnum,
    ItemProductTypeByMarketplace, ItemRelationship,
    ItemRelationshipsByMarketplace, ItemRelationshipTypeEnum,
    ItemSalesRanksByMarketplace, ItemSearchResults, ItemSummaryByMarketplace,
    ItemSummaryByMarketplaceItemClassificationEnum, ItemVariationTheme,
    ItemVendorDetailsByMarketplace,
    ItemVendorDetailsByMarketplaceReplenishmentCategoryEnum,
    ItemVendorDetailsCategory, Pagination, Refinements, RequestsBaseModel,
    SearchCatalogItemsRequest, SearchCatalogItemsRequestIdentifiersTypeEnum,
    SearchCatalogItemsRequestIncludedDataEnum, SpApiBaseModel)


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


def test_dimension_instantiates():
    """Instantiate Dimension with dummy data"""
    kwargs = {
        "unit": None,
        "value": None,
    }
    obj = Dimension(**kwargs)
    assert isinstance(obj, Dimension)


def test_dimensions_instantiates():
    """Instantiate Dimensions with dummy data"""
    kwargs = {
        "height": None,
        "length": None,
        "weight": None,
        "width": None,
    }
    obj = Dimensions(**kwargs)
    assert isinstance(obj, Dimensions)


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
        "classifications": None,
        "dimensions": None,
        "identifiers": None,
        "images": None,
        "product_types": None,
        "relationships": None,
        "sales_ranks": None,
        "summaries": None,
        "vendor_details": None,
    }
    obj = Item(**kwargs)
    assert isinstance(obj, Item)


def test_itembrowseclassification_instantiates():
    """Instantiate ItemBrowseClassification with dummy data"""
    kwargs = {
        "display_name": "",
        "classification_id": "",
        "parent": None,
    }
    obj = ItemBrowseClassification(**kwargs)
    assert isinstance(obj, ItemBrowseClassification)


def test_itembrowseclassificationsbymarketplace_instantiates():
    """Instantiate ItemBrowseClassificationsByMarketplace with dummy data"""
    kwargs = {
        "marketplace_id": None,
        "classifications": None,
    }
    obj = ItemBrowseClassificationsByMarketplace(**kwargs)
    assert isinstance(obj, ItemBrowseClassificationsByMarketplace)


def test_itemclassificationsalesrank_instantiates():
    """Instantiate ItemClassificationSalesRank with dummy data"""
    kwargs = {
        "classification_id": "",
        "title": "",
        "link": None,
        "rank": 0,
    }
    obj = ItemClassificationSalesRank(**kwargs)
    assert isinstance(obj, ItemClassificationSalesRank)


def test_itemcontributorrole_instantiates():
    """Instantiate ItemContributorRole with dummy data"""
    kwargs = {
        "display_name": None,
        "value": "",
    }
    obj = ItemContributorRole(**kwargs)
    assert isinstance(obj, ItemContributorRole)


def test_itemcontributor_instantiates():
    """Instantiate ItemContributor with dummy data"""
    kwargs = {
        "role": ItemContributorRole(**{"display_name": None, "value": ""}),
        "value": "",
    }
    obj = ItemContributor(**kwargs)
    assert isinstance(obj, ItemContributor)


def test_itemdimensionsbymarketplace_instantiates():
    """Instantiate ItemDimensionsByMarketplace with dummy data"""
    kwargs = {
        "marketplace_id": None,
        "item": None,
        "package": None,
    }
    obj = ItemDimensionsByMarketplace(**kwargs)
    assert isinstance(obj, ItemDimensionsByMarketplace)


def test_itemdisplaygroupsalesrank_instantiates():
    """Instantiate ItemDisplayGroupSalesRank with dummy data"""
    kwargs = {
        "website_display_group": "",
        "title": "",
        "link": None,
        "rank": 0,
    }
    obj = ItemDisplayGroupSalesRank(**kwargs)
    assert isinstance(obj, ItemDisplayGroupSalesRank)


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
        "variant": ItemImageVariantEnum.MAIN,
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


def test_itemvariationtheme_instantiates():
    """Instantiate ItemVariationTheme with dummy data"""
    kwargs = {
        "attributes": None,
        "theme": None,
    }
    obj = ItemVariationTheme(**kwargs)
    assert isinstance(obj, ItemVariationTheme)


def test_itemrelationship_instantiates():
    """Instantiate ItemRelationship with dummy data"""
    kwargs = {
        "child_asins": None,
        "parent_asins": None,
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


def test_itemsalesranksbymarketplace_instantiates():
    """Instantiate ItemSalesRanksByMarketplace with dummy data"""
    kwargs = {
        "marketplace_id": None,
        "classification_ranks": None,
        "display_group_ranks": None,
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
        "adult_product": None,
        "autographed": None,
        "brand": None,
        "browse_classification": None,
        "color": None,
        "contributors": None,
        "item_classification": None,
        "item_name": None,
        "manufacturer": None,
        "memorabilia": None,
        "model_number": None,
        "package_quantity": None,
        "part_number": None,
        "release_date": None,
        "size": None,
        "style": None,
        "trade_in_eligible": None,
        "website_display_group": None,
        "website_display_group_name": None,
    }
    obj = ItemSummaryByMarketplace(**kwargs)
    assert isinstance(obj, ItemSummaryByMarketplace)


def test_itemvendordetailscategory_instantiates():
    """Instantiate ItemVendorDetailsCategory with dummy data"""
    kwargs = {
        "display_name": None,
        "value": None,
    }
    obj = ItemVendorDetailsCategory(**kwargs)
    assert isinstance(obj, ItemVendorDetailsCategory)


def test_itemvendordetailsbymarketplace_instantiates():
    """Instantiate ItemVendorDetailsByMarketplace with dummy data"""
    kwargs = {
        "marketplace_id": None,
        "brand_code": None,
        "manufacturer_code": None,
        "manufacturer_code_parent": None,
        "product_category": None,
        "product_group": None,
        "product_subcategory": None,
        "replenishment_category": None,
    }
    obj = ItemVendorDetailsByMarketplace(**kwargs)
    assert isinstance(obj, ItemVendorDetailsByMarketplace)


def test_searchcatalogitemsrequest_instantiates():
    """Instantiate SearchCatalogItemsRequest with dummy data"""
    kwargs = {
        "identifiers": None,
        "identifiers_type": None,
        "marketplace_ids": None,
        "included_data": None,
        "locale": None,
        "seller_id": None,
        "keywords": None,
        "brand_names": None,
        "classification_ids": None,
        "page_size": None,
        "page_token": None,
        "keywords_locale": None,
    }
    obj = SearchCatalogItemsRequest(**kwargs)
    assert isinstance(obj, SearchCatalogItemsRequest)
