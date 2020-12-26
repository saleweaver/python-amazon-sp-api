import urllib.parse

from sp_api.api import ProductFees
from sp_api.base import Marketplaces


def test_get_fees_for_sku():
    print(ProductFees().get_product_fees_estimate_for_sku("Foo's Club", 39.32, is_fba=False))
