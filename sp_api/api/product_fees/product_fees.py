import json

from sp_api.api.product_fees.models.get_my_fees_estimate_response import GetMyFeesEstimateResponse
from sp_api.base.helpers import sp_endpoint, fill_query_params
from sp_api.base import Client, Marketplaces


class ProductFees(Client):
    def __init__(self, marketplace=Marketplaces.US, refresh_token=None):
        super().__init__(marketplace, refresh_token)

    @sp_endpoint('/products/fees/v0/listings/{}/feesEstimate', method='POST')
    def get_product_fees_estimate_for_sku(self, seller_sku, price: float, currency='USD', **kwargs):
        kwargs.update({
            'FeesEstimateRequest': {
                'Identifier': price,
                'PriceToEstimateFees': {
                    'ListingPrice': {
                        'Amount': price,
                        'CurrencyCode': currency
                    }
                },
                'MarketplaceId': self.marketplace_id
            }
        })
        return GetMyFeesEstimateResponse(
            **self._request(fill_query_params(kwargs.pop('path'), seller_sku), data=kwargs).json())

    @sp_endpoint('/products/fees/v0/items/{}/feesEstimate', method='POST')
    def get_product_fees_estimate_for_asin(self, asin, price: float, currency='USD', **kwargs):
        kwargs.update({
            'FeesEstimateRequest': {
                'Identifier': price,
                'PriceToEstimateFees': {
                    'ListingPrice': {
                        'Amount': price,
                        'CurrencyCode': currency
                    }
                },
                'MarketplaceId': self.marketplace_id
            }
        })
        return GetMyFeesEstimateResponse(
            **self._request(fill_query_params(kwargs.pop('path'), asin), data=kwargs).json())
