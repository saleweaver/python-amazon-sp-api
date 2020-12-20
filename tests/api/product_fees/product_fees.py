from sp_api.api import ProductFees


def test_get_fees_for_sku():
    print(ProductFees().get_product_fees_estimate_for_sku('2092'))
