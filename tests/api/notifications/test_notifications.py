from sp_api.api import Notifications
from sp_api.base import SellingApiException, NotificationType


def test_create_destination():
    try:
        res = Notifications().create_destination(name='test', arn='arn')
        print(res)
    except SellingApiException as e:
        print(e)


def test_create_subscription():
    res = Notifications().create_subscription(NotificationType.MFN_ORDER_STATUS_CHANGE, destination_id='dest_id')
    print(res)


def test_delete_subscription():
    res = Notifications().delete_notification_subscription(NotificationType.MFN_ORDER_STATUS_CHANGE, 'subscription_id')
    print(res)


def test_get_subscriptions():
    res = Notifications().get_subscription(NotificationType.REPORT_PROCESSING_FINISHED)
    print(res)


def test_add_subscription():
    res = Notifications().add_subscription(NotificationType.REPORT_PROCESSING_FINISHED)
    print(res)
