"""
Common models generated from Swagger/OpenAPI specification.

This file was auto-generated. Do not edit manually.

"""

from datetime import date, datetime
from enum import Enum, auto
from typing import Annotated, Any, Dict, List, Optional, Union
from uuid import UUID

from pydantic import AliasChoices, BaseModel, ConfigDict, Field

from .base_models import (BodyParam, GetRequestSerializer, PathParam,
                          QueryParam, RequestsBaseModel, SpApiBaseModel)

"""
NotificationParameters

The dynamic parameters required by the notification templated specified by `templateId`.
"""


class NotificationParameters(SpApiBaseModel):
    """The dynamic parameters required by the notification templated specified by `templateId`."""

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow",
        serialize_by_alias=True,
        arbitrary_types_allowed=True,
    )


"""
CreateNotificationRequestBody

The request for the `createNotification` operation.
"""


class CreateNotificationRequestBody(SpApiBaseModel):
    """The request for the `createNotification` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    template_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("templateId", "template_id"),
            serialization_alias="templateId",
            description="The unique identifier of the notification template you used to onboard your application.",
        ),
    ]

    notification_parameters: Annotated[
        "NotificationParameters",
        Field(
            ...,
            validation_alias=AliasChoices(
                "notificationParameters", "notification_parameters"
            ),
            serialization_alias="notificationParameters",
            description="The parameters specified in the template you used to onboard your application.",
        ),
    ]

    marketplace_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="An encrypted marketplace identifier for the posted notification.",
        ),
    ]


"""
CreateNotificationRequest

Request parameters for createNotification
"""


class CreateNotificationRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for createNotification
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    body: Annotated[
        "CreateNotificationRequestBody",
        BodyParam(),
        Field(
            ...,
            description="[BODY] The request body for the `createNotification` operation.",
        ),
    ]


"""
CreateNotificationResponse

The response for the `createNotification` operation.
"""


class CreateNotificationResponse(SpApiBaseModel):
    """The response for the `createNotification` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    notification_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("notificationId", "notification_id"),
            serialization_alias="notificationId",
            description="The unique identifier assigned to each notification.",
        ),
    ]


# Enum definitions
class DeletionReasonEnum(str, Enum):
    """Enum for deletionReason"""

    INCORRECT_CONTENT = (
        "INCORRECT_CONTENT"  # The notification's content is recognized to be incorrect.
    )
    INCORRECT_RECIPIENT = (
        "INCORRECT_RECIPIENT"  # The notification was sent to incorrect seller.
    )


"""
DeleteNotificationsRequestBody

The request for the `deleteNotifications` operation.
"""


class DeleteNotificationsRequestBody(SpApiBaseModel):
    """The request for the `deleteNotifications` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    template_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("templateId", "template_id"),
            serialization_alias="templateId",
            description="The unique identifier of the notification template you used to onboard your application.",
        ),
    ]

    deletion_reason: Annotated[
        DeletionReasonEnum,
        Field(
            ...,
            validation_alias=AliasChoices("deletionReason", "deletion_reason"),
            serialization_alias="deletionReason",
            description="The unique identifier that maps each notification status to a reason code.",
        ),
    ]


"""
DeleteNotificationsRequest

Request parameters for deleteNotifications
"""


class DeleteNotificationsRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for deleteNotifications
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    body: Annotated[
        "DeleteNotificationsRequestBody",
        BodyParam(),
        Field(
            ...,
            description="[BODY] The request body for the `deleteNotifications` operation.",
        ),
    ]


"""
Error

Error response returned when the request is unsuccessful.
"""


class Error(SpApiBaseModel):
    """Error response returned when the request is unsuccessful."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    code: Annotated[
        str,
        Field(
            ...,
            description="An error code that identifies the type of error that occurred.",
        ),
    ]

    message: Annotated[
        str, Field(..., description="A message that describes the error condition.")
    ]

    details: Annotated[
        Optional[str],
        Field(
            None,
            description="Additional details that can help the caller understand or fix the issue.",
        ),
    ]


"""
ErrorList

A list of error responses returned when a request is unsuccessful.
"""


class ErrorList(SpApiBaseModel):
    """A list of error responses returned when a request is unsuccessful."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    errors: Annotated[
        List["Error"],
        Field(
            ..., description="Error response returned when the request is unsuccessful."
        ),
    ]


# Enum definitions
class FeedbackActionCodeEnum(str, Enum):
    """Enum for feedbackActionCode"""

    SELLER_ACTION_COMPLETED = "SELLER_ACTION_COMPLETED"  # The seller completed the action attached to the posted notification.


"""
RecordActionFeedbackRequestBody

The request for the `recordActionFeedback` operation.
"""


class RecordActionFeedbackRequestBody(SpApiBaseModel):
    """The request for the `recordActionFeedback` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    feedback_action_code: Annotated[
        FeedbackActionCodeEnum,
        Field(
            ...,
            validation_alias=AliasChoices("feedbackActionCode", "feedback_action_code"),
            serialization_alias="feedbackActionCode",
            description="The unique identifier for each notification status.",
        ),
    ]


"""
RecordActionFeedbackRequest

Request parameters for recordActionFeedback
"""


class RecordActionFeedbackRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for recordActionFeedback
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    notification_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("notificationId", "notification_id"),
            serialization_alias="notificationId",
            description="[PATH] A `notificationId` uniquely identifies a notification.",
        ),
    ]

    body: Annotated[
        "RecordActionFeedbackRequestBody",
        BodyParam(),
        Field(
            ...,
            description="[BODY] The request body for the `recordActionFeedback` operation.",
        ),
    ]


# Rebuild models to resolve forward references
Error.model_rebuild()
ErrorList.model_rebuild()
CreateNotificationRequestBody.model_rebuild()
NotificationParameters.model_rebuild()
CreateNotificationResponse.model_rebuild()
DeleteNotificationsRequestBody.model_rebuild()
RecordActionFeedbackRequestBody.model_rebuild()
CreateNotificationRequest.model_rebuild()
DeleteNotificationsRequest.model_rebuild()
RecordActionFeedbackRequest.model_rebuild()
