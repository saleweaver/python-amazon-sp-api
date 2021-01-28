import urllib

from sp_api.api.products.products import Products
from sp_api.base import Marketplaces


def test_pricing_for_sku():
    print(Products().get_product_pricing_for_skus(['abc']))
