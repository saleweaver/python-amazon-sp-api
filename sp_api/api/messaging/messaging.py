import urllib.parse

from sp_api.base import Client, sp_endpoint, fill_query_params, ApiResponse


class Messaging(Client):
    """
    """

    @sp_endpoint('/messaging/v1/orders/{}')
    def get_messaging_actions_for_order(self, order_id: str, **kwargs) -> ApiResponse:
        """
        get_messaging_actions_for_order(self, order_id: str, **kwargs) -> ApiResponse
        Returns a specified item and its attributes.


        Args:
            order_id:
            key marketplaceIds: str
            **kwargs:

        Returns:
            ApiResponse:
        """
        kwargs.update({'marketplaceIds': kwargs.get('marketplaceIds', None) or self.marketplace_id})
        return self._request(fill_query_params(kwargs.pop('path'), order_id), params=kwargs)

    @sp_endpoint('/messaging/v1/orders/{}/messages/legalDisclosure', method='POST')
    def create_legal_disclosure_message(self, order_id, **kwargs):
        return self._request(fill_query_params(kwargs.pop('path'), order_id), data=kwargs)

