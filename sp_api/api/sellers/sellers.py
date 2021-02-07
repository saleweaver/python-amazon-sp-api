from sp_api.base.helpers import sp_endpoint
from sp_api.api.sellers.models.get_marketplace_participations_response import GetMarketplaceParticipationsResponse
from sp_api.base import Client, Marketplaces


class Sellers(Client):

    @sp_endpoint('/sellers/v1/marketplaceParticipations')
    def get_marketplace_participation(self, **kwargs):
        return GetMarketplaceParticipationsResponse(**self._request(kwargs.pop('path')).json())
