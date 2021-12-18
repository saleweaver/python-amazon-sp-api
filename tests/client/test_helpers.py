import os

from sp_api.api import FulfillmentInbound, Orders
from sp_api.util import KeyMaker, load_all_pages, throttle_retry

key_mapping = {
    'sku': ['seller_sku', 'sellerSku'],
    'title': ['product_name']
}
test_obj = {
    'goo': {'x': {}},
    'seller_sku': 1,
    'product_name': {
        'sellerSku': [
            'seller_sku',
            3,
            {
                'sellerSku': 22,
                'product_name': {
                    'title': 'Foo',
                    'x': 'bar'
                }
            }
        ]
    }
}


def test_key_maker_from_dict():
    r = KeyMaker(key_mapping, deep=True).convert_keys(test_obj)
    assert isinstance(r, dict)
    assert r.get('sku') == 1
    assert r.get('seller_sku') is None
    assert isinstance(r.get('title'), dict)
    assert isinstance(r.get('title').get('sku'), list)


def test_key_maker_from_list():
    r = KeyMaker(key_mapping, deep=True).convert_keys([test_obj])
    assert isinstance(r, list)
    assert len(r) == 1

    assert r[0].get('sku') == 1
    assert r[0].get('seller_sku') is None
    assert isinstance(r[0].get('title'), dict)
    assert isinstance(r[0].get('title').get('sku'), list)


def test_key_maker_from_dict_not_deep():
    r = KeyMaker(key_mapping, deep=False).convert_keys(test_obj)
    assert r.get('sku') == 1
    assert r.get('seller_sku') is None
    assert isinstance(r.get('title'), dict)
    assert isinstance(r.get('title').get('sellerSku'), list)


def test_load_all_pages():
    @throttle_retry()
    @load_all_pages(extras=dict(QueryType='NEXT_TOKEN'))
    def load_shipments(**kwargs):
        return FulfillmentInbound().get_shipments(**kwargs)

    for x in load_shipments(QueryType='SHIPMENT'):
        assert x.payload is not None


def test_load_all_pages_orders():
    @throttle_retry()
    @load_all_pages()
    def load_all_orders(**kwargs):
        return Orders().get_orders(**kwargs)

    for x in load_all_orders(CreatedAfter='TEST_CASE_200', MarketplaceIds=["ATVPDKIKX0DER"]):
        assert x.payload is not None
