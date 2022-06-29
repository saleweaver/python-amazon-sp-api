from sp_api.api import CatalogItems as Catalog, CatalogItemsVersion
from sp_api.base import Marketplaces, SellingApiBadRequestException, ApiResponse


def test_get_catalog_item():
    res = Catalog(version=CatalogItemsVersion.V_2020_12_01).get_catalog_item('B098RX87V2')
    assert res.errors is None
    assert isinstance(res, ApiResponse)


def test_get_catalog_item_version():
    res = Catalog(version=CatalogItemsVersion.LATEST).get_catalog_item('B098RX87V2')
    assert res.errors is None
    assert isinstance(res, ApiResponse)


def test_list_catalog_items():
    res = Catalog().search_catalog_items(keywords='test')
    assert res.errors is None

