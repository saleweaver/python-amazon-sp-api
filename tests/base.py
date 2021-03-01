from sp_api.api import FulfillmentInbound


def test_api_response_next_token():
    res = FulfillmentInbound().get_shipments(QueryType='SHIPMENT')
    assert res.next_token is not None
