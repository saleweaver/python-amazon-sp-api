from sp_api.api import Notifications, Reports
from sp_api.base import SellingApiException, NotificationType, ReportType, Marketplaces


def test_create_destination():
    res = Notifications().create_destination(name='test', arn='arn:aws:sqs:us-east-2:444455556666:queue1')
    assert res.payload.get("destinationId") == "TEST_CASE_200_DESTINATION_ID"
    assert res.payload.get("resource").get('sqs').get('arn') == "arn:aws:sqs:us-east-2:444455556666:queue1"


def test_create_subscription():
    res = Notifications().create_subscription(NotificationType.MFN_ORDER_STATUS_CHANGE, destination_id='dest_id')
    assert res.payload.get('destinationId') == 'TEST_CASE_200_DESTINATION_ID'
    assert res.payload.get('subscriptionId') == 'TEST_CASE_200_SUBSCRIPTION_ID'


def test_delete_subscription():
    res = Notifications().delete_notification_subscription(NotificationType.MFN_ORDER_STATUS_CHANGE, 'subscription_id')
    assert res.errors is None


def test_get_subscriptions():
    res = Notifications().get_subscription(NotificationType.REPORT_PROCESSING_FINISHED)
    assert res.payload.get('destinationId') == 'TEST_CASE_200_DESTINATION_ID'
    assert res.payload.get('subscriptionId') == 'TEST_CASE_200_SUBSCRIPTION_ID'

