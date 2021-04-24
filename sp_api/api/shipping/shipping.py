from sp_api.base.helpers import sp_endpoint, fill_query_params
from sp_api.base import Client, Marketplaces, deprecated, NotificationType, ApiResponse


class Shipping(Client):
    """
    :link: https://github.com/amzn/selling-partner-api-docs/blob/main/references/shipping-api/shipping.md
    """

    @sp_endpoint('/shipping/v1/purchaseShipment', method='POST')
    def purchase_shipment(self, data, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'), data=data)

    @sp_endpoint('/shipping/v1/rates', method='POST')
    def get_rates(self, data, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'), data=data)

    @sp_endpoint('/shipping/v1/account')
    def get_account(self, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop('path'), params={**kwargs})

    @sp_endpoint('/shipping/v1/tracking/{}')
    def get_tracking(self, tracking_id: str, **kwargs) -> ApiResponse:
        return self._request(fill_query_params(kwargs.pop('path'), tracking_id), params={**kwargs})
