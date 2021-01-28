import urllib

from sp_api.api.products.products import Products
from sp_api.base import Marketplaces


def test_pricing_for_sku():
    print(Products().get_competitive_pricing_for_asins(['']))
