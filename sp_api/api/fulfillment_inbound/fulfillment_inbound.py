from sp_api.base import Client, Marketplaces, ApiResponse
from sp_api.base import sp_endpoint, fill_query_params

class FulfillmentInbound(Client):
    @sp_endpoint("/fba/inbound/v0/itemsGuidance")
    def item_guidance(self, **kwargs):
        return self._request(kwargs.pop('path'), params=kwargs)

    @sp_endpoint("/fba/inbound/v0/plans", method='POST')
    def plans(self, data, **kwargs):
        return self._request(kwargs.pop('path'), data={**data, **kwargs})

    @sp_endpoint("/fba/inbound/v0/shipments/{}", method='POST')
    def create_shipment(self, shipment_id, data, **kwargs):
        return self._request(fill_query_params(kwargs.pop('path'), shipment_id), data={**data, **kwargs})

    @sp_endpoint("/fba/inbound/v0/shipments/{}", method='PUT')
    def update_shipment(self, shipment_id, data, **kwargs):
        return self._request(fill_query_params(kwargs.pop('path'), shipment_id), data={**data, **kwargs})

    @sp_endpoint("/fba/inbound/v0/shipments/{}/preorder")
    def preorder(self, shipment_id, **kwargs):
        return self._request(fill_query_params(kwargs.pop('path'), shipment_id), params=kwargs)

    @sp_endpoint("/fba/inbound/v0/shipments/{}/preorder/confirm", method='PUT')
    def confirm_preorder(self, shipment_id, **kwargs):
        return self._request(fill_query_params(kwargs.pop('path'), shipment_id), params=kwargs)

    @sp_endpoint("/fba/inbound/v0/prepInstructions")
    def prep_instruction(self, data, **kwargs):
        return self._request(kwargs.pop('path'), params={**data, **kwargs})

    @sp_endpoint("/fba/inbound/v0/shipments/{}/transport")
    def get_transport_information(self, shipment_id, **kwargs):
        return self._request(fill_query_params(kwargs.pop('path'), shipment_id), params=kwargs)

    @sp_endpoint("/fba/inbound/v0/shipments/{}/transport", method='PUT')
    def update_transport_information(self, shipment_id, **kwargs):
        return self._request(fill_query_params(kwargs.pop('path'), shipment_id), data=kwargs)

    @sp_endpoint("/fba/inbound/v0/shipments/{}/transport/void", method='POST')
    def void_transport(self, shipment_id, **kwargs):
        return self._request(fill_query_params(kwargs.pop('path'), shipment_id), data=kwargs, add_marketplace=False)

    @sp_endpoint("/fba/inbound/v0/shipments/{}/transport/estimate", method='POST')
    def estimate_transport(self, shipment_id, **kwargs):
        return self._request(fill_query_params(kwargs.pop('path'), shipment_id), data=kwargs, add_marketplace=False)

    @sp_endpoint("/fba/inbound/v0/shipments/{}/transport/confirm", method='POST')
    def confirm_transport(self, shipment_id, **kwargs):
        return self._request(fill_query_params(kwargs.pop('path'), shipment_id), data=kwargs, add_marketplace=False)

    @sp_endpoint("/fba/inbound/v0/shipments/{}/labels")
    def get_labels(self, shipment_id, **kwargs):
        return self._request(fill_query_params(kwargs.pop('path'), shipment_id), params=kwargs, add_marketplace=False)

    @sp_endpoint("/fba/inbound/v0/shipments/{}/billOfLading")
    def bill_of_lading(self, shipment_id, **kwargs):
        return self._request(fill_query_params(kwargs.pop('path'), shipment_id), params=kwargs)

    @sp_endpoint("/fba/inbound/v0/shipments")
    def get_shipments(self, **kwargs):
        return self._request(kwargs.pop('path'), params=kwargs)

    @sp_endpoint("/fba/inbound/v0/shipments/{}/items")
    def shipment_items_by_shipment(self, shipment_id, **kwargs):
        return self._request(fill_query_params(kwargs.pop('path'), shipment_id), params=kwargs)

    @sp_endpoint("/fba/inbound/v0/shipmentItems")
    def shipment_items(self, **kwargs):
        return self._request(kwargs.pop('path'), params=kwargs)

