from sp_api.base.helpers import sp_endpoint, fill_query_params
from sp_api.base import Client, Marketplaces


class ProductFees(Client):
    def __init__(self, marketplace=Marketplaces.US, refresh_token=None):
        super().__init__(marketplace, refresh_token)

    @sp_endpoint('/products/fees/v0/listings/{}/feesEstimate')
    def get_product_fees_estimate_for_sku(self, seller_sku, **kwargs):
        return self._request(fill_query_params(kwargs.pop('path'), seller_sku)).json()
