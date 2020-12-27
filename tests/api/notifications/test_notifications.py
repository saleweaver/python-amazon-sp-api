from sp_api.api import Notifications
from sp_api.base import SellingApiException


def test_create_destination():
    try:
        res = Notifications().create_destination(name='test', arn='arn:aws:sqs:us-east-1:112278907045:sellingapi')
        print(res)
    except SellingApiException as e:
        print(e)
