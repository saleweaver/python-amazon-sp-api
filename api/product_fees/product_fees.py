from api.product_fees.models.get_my_fees_estimate_response import GetMyFeesEstimateResponse
from auth.credentials import Credentials
from base.client import Client
from base.helpers import fill_query_params, sp_endpoint
from base.marketplaces import Marketplaces


class ProductFees(Client):
    def __init__(self, marketplace=Marketplaces.US, refresh_token=None):
        super().__init__(marketplace, refresh_token)

    @sp_endpoint('/products/fees/v0/listings/{}/feesEstimate')
    def get_product_fees_estimate_for_sku(self, seller_sku, **kwargs):
        return GetMyFeesEstimateResponse(**self.request(fill_query_params(kwargs.pop('path'), seller_sku)).json())
