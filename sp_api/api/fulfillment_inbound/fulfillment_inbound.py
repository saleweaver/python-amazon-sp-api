from sp_api.base import Client, Marketplaces, ApiResponse
from sp_api.base import sp_endpoint, fill_query_params


class FulfillmentInbound(Client):
    @sp_endpoint('/fba/inbound/v0/shipments')
    def get_shipments(self, **kwargs) -> ApiResponse:
        return self._request(kwargs.get('path'), params=kwargs)

