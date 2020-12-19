from sp_api.api import Notifications
from sp_api.base import SellingApiException


def test_create_destination():
    try:
        res = Notifications().create_destination()
        print(res)
    except SellingApiException as e:
        print(e)
