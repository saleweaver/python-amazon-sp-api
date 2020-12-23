import urllib

from sp_api.api.products.products import Products


def test_pricing_for_sku():
    print(Products().get_product_pricing_for_skus(["Sam's Club_2.50_23", "2092"]))

