from sp_api.api import CatalogItems as Catalog
from sp_api.api import CatalogItemsVersion
from sp_api.base import (ApiResponse, Marketplaces,
                         SellingApiBadRequestException)


def test_get_catalog_item():
    res = Catalog(version=CatalogItemsVersion.V_2020_12_01).get_catalog_item(
        "B098RX87V2"
    )
    assert res.errors is None
    assert isinstance(res, ApiResponse)

    # No `includedData` parameter provided - Amazon should default to
    # "summaries".
    assert "summaries" in res.payload


def test_get_catalog_item_version():
    res = Catalog(version=CatalogItemsVersion.LATEST).get_catalog_item("B098RX87V2")
    assert res.errors is None
    assert isinstance(res, ApiResponse)


def test_list_catalog_items():
    res = Catalog().search_catalog_items(keywords="test")
    assert res.errors is None

    # No `includedData` parameter provided - Amazon should default to
    # "summaries" for every returned item.
    for item in res.items:
        assert "summaries" in item


def test_get_catalog_item_foo():
    res = Catalog(version=CatalogItemsVersion.V_2020_12_01).get_catalog_item(
        "B07Z95MG3S"
    )
    assert res.errors is None
    assert isinstance(res, ApiResponse)
