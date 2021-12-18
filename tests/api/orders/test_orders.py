from datetime import datetime, timedelta

from sp_api.api import Orders
from sp_api.base import Marketplaces, SellingApiForbiddenException, SellingApiException


def test_get_orders():
    res = Orders().get_orders(CreatedAfter='TEST_CASE_200', MarketplaceIds=["ATVPDKIKX0DER"])
    assert res.errors is None
    assert res.payload.get('Orders') is not None


def test_get_order_items():
    res = Orders().get_order_items('TEST_CASE_200')
    assert res.errors is None
    assert res.payload.get('AmazonOrderId') is not None


def test_get_order_address():
    res = Orders().get_order_address('TEST_CASE_200')
    assert res.errors is None
    assert res.payload.get('AmazonOrderId') is not None


def test_get_order_buyer_info():
    res = Orders().get_order_buyer_info('TEST_CASE_200')
    assert res.errors is None
    assert res.payload.get('AmazonOrderId') is not None


def test_get_order():
    res = Orders().get_order('TEST_CASE_200')
    assert res.errors is None
    assert res.payload.get('AmazonOrderId') is not None


def test_get_order_items_buyer_info():
    res = Orders().get_order_items_buyer_info('TEST_CASE_200')
    assert res.errors is None
    assert res.payload.get('AmazonOrderId') is not None


def test_get_orders_400_error():
    from sp_api.base import SellingApiBadRequestException
    try:
        Orders().get_orders(CreatedAfter='TEST_CASE_400')
    except SellingApiBadRequestException as sep:
        assert sep.code == 400
        assert sep.amzn_code == 'InvalidInput'


def test_get_order_api_response_call():
    res = Orders().get_order('TEST_CASE_200')
    print(res('DefaultShipFromLocationAddress'))
    assert res('DefaultShipFromLocationAddress') is not None
    assert res.errors is None
    assert res.payload.get('AmazonOrderId') is not None


def test_get_orders_attr():
    res = Orders().get_orders(CreatedAfter='TEST_CASE_200', MarketplaceIds=["ATVPDKIKX0DER"])
    assert res.Orders is not None
    assert res.errors is None
    assert res.payload.get('Orders') is not None


def test_get_order_api_response_call2():
    res = Orders().get_order('TEST_CASE_200')
    assert res() is not None
    assert isinstance(res(), dict)
    assert res.errors is None
    assert res.payload.get('AmazonOrderId') is not None

