from sp_api.base import Client, Marketplaces, ApiResponse
from sp_api.base import sp_endpoint, fill_query_params


class Finances(Client):

    @sp_endpoint('/finances/v0/orders/{}/financialEvents')
    def get_financial_events_for_order(self, order_id, **kwargs) -> ApiResponse:
        """
        get_financial_events_for_order(self, order_id, **kwargs) -> ApiResponse


        Args:
            order_id:
            **kwargs:

        Returns:

        """
        return self._request(fill_query_params(kwargs.pop('path'), order_id), params={**kwargs})

