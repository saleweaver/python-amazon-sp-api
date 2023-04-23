from sp_api.api import Orders


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


def test_update_shipment_status():
    res = Orders().update_shipment_status(
        order_id='123-1234567-1234567',
        marketplaceId='ATVPDKIKX0DER',
        shipmentStatus='ReadyForPickup'
    )
    assert res() is not None
    assert isinstance(res(), dict)
    assert res.errors is None
    assert res.payload.get("status_code") == 204


def test_confirm_shipment():
    res = Orders().confirm_shipment(
        order_id='123-1234567-1234567',
        marketplaceId='ATVPDKIKX0DER',
        packageDetail={
            'packageReferenceId': '0001',
            'carrierCode': 'DHL',
            "shippingMethod": 'Paket',
            'trackingNumber': '1234567890',
            'shipDate': '2023-03-19T12:00:00Z',
            'orderItems': [
                {
                    'orderItemId': '123456789',
                    'quantity': 1
                },
                {
                    'orderItemId': '2345678901',
                    'quantity': 2
                },
            ]
        }
    )
    assert res() is not None
    assert isinstance(res(), dict)
    assert res.errors is None
    assert res.payload.get("status_code") is None


def test_update_shipment_status_400_error():
    from sp_api.base import SellingApiBadRequestException
    try:
        Orders().update_shipment_status(
            order_id='123-1234567-1234567',
            marketplaceId='1',
            shipmentStatus='ReadyForPickup'
        )
    except SellingApiBadRequestException as sep:
        assert sep.code == 400
        assert sep.amzn_code == 'InvalidInput'
