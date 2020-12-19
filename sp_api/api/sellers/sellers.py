from sp_api.base.helpers import sp_endpoint
from sp_api.api.sellers.models.get_marketplace_participations_response import GetMarketplaceParticipationsResponse
from sp_api.base import Client, Marketplaces


class Sellers(Client):
    def __init__(self, marketplace=Marketplaces.US, refresh_token=None):
        super().__init__(marketplace, refresh_token)

    @sp_endpoint('/sellers/v1/marketplaceParticipations')
    def get_marketplace_participation(self, **kwargs):
        return GetMarketplaceParticipationsResponse(**self._request(kwargs.pop('path')).json())
