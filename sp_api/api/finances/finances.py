from sp_api.api.finances.models.list_financial_events_response import ListFinancialEventsResponse
from sp_api.base import Client, Marketplaces
from sp_api.base import sp_endpoint, fill_query_params


class Finances(Client):
    def __init__(self, marketplace=Marketplaces.US, *, refresh_token=None):
        super().__init__(marketplace, refresh_token)

    @sp_endpoint('/finances/v0/orders/{}/financialEvents')
    def get_financial_events_for_order(self, order_id, **kwargs):
        return ListFinancialEventsResponse(
            **self._request(fill_query_params(kwargs.pop('path'), order_id), params={**kwargs}).json()
        )
