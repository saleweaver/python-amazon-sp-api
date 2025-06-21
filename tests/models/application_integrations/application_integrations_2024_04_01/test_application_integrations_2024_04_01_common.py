# Auto-generated tests for sp_api.api.models.application_integrations.application_integrations_2024_04_01.common.py
from datetime import datetime

import pytest
from sp_api.api.models.application_integrations.application_integrations_2024_04_01.common import (
    CreateNotificationRequest, CreateNotificationRequestBody,
    CreateNotificationResponse, DeleteNotificationsRequest,
    DeleteNotificationsRequestBody, DeletionReasonEnum, Error, ErrorList,
    FeedbackActionCodeEnum, GetRequestSerializer, NotificationParameters,
    RecordActionFeedbackRequest, RecordActionFeedbackRequestBody,
    RequestsBaseModel, SpApiBaseModel)


def test_requestsbasemodel_instantiates():
    """Instantiate RequestsBaseModel with dummy data"""
    kwargs = {}
    obj = RequestsBaseModel(**kwargs)
    assert isinstance(obj, RequestsBaseModel)


def test_spapibasemodel_instantiates():
    """Instantiate SpApiBaseModel with dummy data"""
    kwargs = {}
    obj = SpApiBaseModel(**kwargs)
    assert isinstance(obj, SpApiBaseModel)


def test_getrequestserializer_instantiates():
    """Instantiate GetRequestSerializer with dummy data"""
    kwargs = {}
    obj = GetRequestSerializer(**kwargs)
    assert isinstance(obj, GetRequestSerializer)


def test_notificationparameters_instantiates():
    """Instantiate NotificationParameters with dummy data"""
    kwargs = {}
    obj = NotificationParameters(**kwargs)
    assert isinstance(obj, NotificationParameters)


def test_createnotificationrequestbody_instantiates():
    """Instantiate CreateNotificationRequestBody with dummy data"""
    kwargs = {
        "template_id": "",
        "notification_parameters": NotificationParameters(**{}),
        "marketplace_id": None,
    }
    obj = CreateNotificationRequestBody(**kwargs)
    assert isinstance(obj, CreateNotificationRequestBody)


def test_createnotificationrequest_instantiates():
    """Instantiate CreateNotificationRequest with dummy data"""
    kwargs = {
        "body": CreateNotificationRequestBody(
            **{
                "template_id": "",
                "notification_parameters": NotificationParameters(**{}),
                "marketplace_id": None,
            }
        ),
    }
    obj = CreateNotificationRequest(**kwargs)
    assert isinstance(obj, CreateNotificationRequest)


def test_createnotificationresponse_instantiates():
    """Instantiate CreateNotificationResponse with dummy data"""
    kwargs = {
        "notification_id": None,
    }
    obj = CreateNotificationResponse(**kwargs)
    assert isinstance(obj, CreateNotificationResponse)


def test_deletenotificationsrequestbody_instantiates():
    """Instantiate DeleteNotificationsRequestBody with dummy data"""
    kwargs = {
        "template_id": "",
        "deletion_reason": DeletionReasonEnum.INCORRECT_CONTENT,
    }
    obj = DeleteNotificationsRequestBody(**kwargs)
    assert isinstance(obj, DeleteNotificationsRequestBody)


def test_deletenotificationsrequest_instantiates():
    """Instantiate DeleteNotificationsRequest with dummy data"""
    kwargs = {
        "body": DeleteNotificationsRequestBody(
            **{
                "template_id": "",
                "deletion_reason": DeletionReasonEnum.INCORRECT_CONTENT,
            }
        ),
    }
    obj = DeleteNotificationsRequest(**kwargs)
    assert isinstance(obj, DeleteNotificationsRequest)


def test_error_instantiates():
    """Instantiate Error with dummy data"""
    kwargs = {
        "code": "",
        "message": "",
        "details": None,
    }
    obj = Error(**kwargs)
    assert isinstance(obj, Error)


def test_errorlist_instantiates():
    """Instantiate ErrorList with dummy data"""
    kwargs = {
        "errors": [],
    }
    obj = ErrorList(**kwargs)
    assert isinstance(obj, ErrorList)


def test_recordactionfeedbackrequestbody_instantiates():
    """Instantiate RecordActionFeedbackRequestBody with dummy data"""
    kwargs = {
        "feedback_action_code": FeedbackActionCodeEnum.SELLER_ACTION_COMPLETED,
    }
    obj = RecordActionFeedbackRequestBody(**kwargs)
    assert isinstance(obj, RecordActionFeedbackRequestBody)


def test_recordactionfeedbackrequest_instantiates():
    """Instantiate RecordActionFeedbackRequest with dummy data"""
    kwargs = {
        "notification_id": "",
        "body": RecordActionFeedbackRequestBody(
            **{"feedback_action_code": FeedbackActionCodeEnum.SELLER_ACTION_COMPLETED}
        ),
    }
    obj = RecordActionFeedbackRequest(**kwargs)
    assert isinstance(obj, RecordActionFeedbackRequest)
