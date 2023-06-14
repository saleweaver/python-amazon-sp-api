from sp_api.api.products.products import Products
from sp_api.base import ApiResponse, Marketplaces, SellingApiBadRequestException


def test_pricing_for_sku():
    res = Products().get_product_pricing_for_skus([], MarketplaceId="ATVPDKIKX0DER")
    assert res.payload[0].get('status') == 'Success'


def test_pricing_for_asin():
    res = Products().get_product_pricing_for_asins([], MarketplaceId="ATVPDKIKX0DER")
    assert res.payload[0].get('status') == 'Success'


def test_pricing_for_asin_expect_400():
    try:
        Products().get_product_pricing_for_asins(['TEST_CASE_400'], MarketplaceId='TEST_CASE_400')
    except SellingApiBadRequestException:
        pass


def test_competitive_pricing_for_sku():
    res = Products().get_competitive_pricing_for_skus([], MarketplaceId="ATVPDKIKX0DER")
    assert res.payload[0].get('status') == 'Success'


def test_competitive_pricing_for_asin():
    res = Products().get_competitive_pricing_for_asins([], MarketplaceId="ATVPDKIKX0DER")
    assert res.payload[0].get('status') == 'Success'


def test_get_item_offers_batch():
    res = Products().get_item_offers_batch([])
    assert res.errors is None
    assert isinstance(res, ApiResponse)


def test_get_listing_offers_batch():
    res = Products().get_listing_offers_batch([])
    assert res.errors is None
    assert isinstance(res, ApiResponse)
