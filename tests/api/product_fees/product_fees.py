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


def test_get_product_fees_estimate():
    res = ProductFees().get_product_fees_estimate([
            dict(identifier='UmaS1',id_type='ASIN',id_value="asin123", price=10, currency='USD', shipping_price=10, is_fba=False,
                points={
                    "PointsNumber": 0,
                    "PointsMonetaryValue": {
                        "CurrencyCode": "USD",
                        "Amount": 0
                    }}
                ),
            dict(identifier='UmaS2', marketplace_id=Marketplaces.MX.marketplace_id, id_type='SellerSKU', id_value="sku123", price=10, currency='MXN', shipping_price=10, is_fba=True,
                points={
                    "PointsNumber": 0,
                    "PointsMonetaryValue": {
                        "CurrencyCode": "MXN",
                        "Amount": 0
                    }}
                ),
        ])
    for fer in res.payload:
        assert fer['Status'] == 'Success'
