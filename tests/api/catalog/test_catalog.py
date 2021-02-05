from sp_api.api import Catalog
from sp_api.base import Marketplaces


def test_get_catalog_item():
    res = Catalog().get_item('ASIN_200', MarketplaceId='TEST_CASE_200')
    assert res.errors is None


def test_list_catalog_items():
    res = Catalog().list_items(MarketplaceId='TEST_CASE_200', SellerSKU='SKU_200')
    assert res.errors is None
