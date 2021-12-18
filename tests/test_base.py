from sp_api.api import FulfillmentInbound
from sp_api.base import Marketplaces


def test_api_response_has_next_token():
    res = FulfillmentInbound().get_shipments(QueryType='SHIPMENT')
    assert res.next_token is not None


def test_marketplaces():
    assert Marketplaces.DE.region == 'eu-west-1'
    assert Marketplaces.US.marketplace_id == 'ATVPDKIKX0DER'

