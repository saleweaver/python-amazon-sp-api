import urllib.parse

from sp_api.api import ProductFees
from sp_api.base import Marketplaces


def test_get_fees_for_sku():
    res = ProductFees().get_product_fees_estimate_for_sku("UmaS1", 10, currency='USD', shipping_price=10, is_fba=False,
                                                          points={
                                                              "PointsNumber": 0,
                                                              "PointsMonetaryValue": {
                                                                  "CurrencyCode": "USD",
                                                                  "Amount": 0
                                                              }
                                                          })
    assert res.payload.get('FeesEstimateResult').get('Status') == 'Success'


def test_get_fees_for_asin():
    res = ProductFees().get_product_fees_estimate_for_asin("UmaS1", 10, currency='USD', shipping_price=10, is_fba=False,
                                                           points={
                                                               "PointsNumber": 0,
                                                               "PointsMonetaryValue": {
                                                                   "CurrencyCode": "USD",
                                                                   "Amount": 0
                                                               }
                                                           })
    assert res.payload.get('FeesEstimateResult').get('Status') == 'Success'
