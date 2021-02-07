from sp_api.base.helpers import sp_endpoint
from sp_api.base import Client, Marketplaces, ApiResponse


class Sellers(Client):

    @sp_endpoint('/sellers/v1/marketplaceParticipations')
    def get_marketplace_participation(self, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'))
