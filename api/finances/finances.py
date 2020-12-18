from api.finances.models.list_financial_events_response import ListFinancialEventsResponse
from base.client import Client
from base.helpers import fill_query_params, sp_endpoint
from base.marketplaces import Marketplaces


class Finances(Client):
    def __init__(self, marketplace=Marketplaces.US, *, refresh_token=None):
        super().__init__(marketplace, refresh_token)

    @sp_endpoint('/finances/v0/orders/{}/financialEvents')
    def get_financial_events_for_order(self, order_id, **kwargs):
        return ListFinancialEventsResponse(
            **self.request(fill_query_params(kwargs.pop('path'), order_id), params={**kwargs}).json())
