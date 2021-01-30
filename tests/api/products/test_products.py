import urllib

from sp_api.api.products.products import Products
from sp_api.base import Marketplaces


def test_pricing_for_sku():
    res = Products().get_product_pricing_for_skus([])
    assert res.payload[0].get('status') == 'Success'


def test_pricing_for_asin():
    res = Products().get_product_pricing_for_asins([])
    assert res.payload[0].get('status') == 'Success'


# def test_competitive_pricing_for_sku():
#     res = Products().get_competitive_pricing_for_skus([])
#     assert res.payload[0].get('status') == 'Success'
#
#
# def test_competitive_pricing_for_asin():
#     res = Products().get_competitive_pricing_for_asins([])
#     assert res.payload[0].get('status') == 'Success'
