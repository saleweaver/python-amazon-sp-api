from datetime import datetime, timedelta

from sp_api.api import Orders
from sp_api.base import SellingApiException


def test_get_orders():
    try:
        res = Orders().get_orders(CreatedAfter=(datetime.utcnow() - timedelta(days=7)).isoformat())
        print(res.payload)  # json data
    except SellingApiException as ex:
        print(ex)
