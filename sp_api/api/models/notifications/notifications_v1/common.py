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

AggregationTimePeriod = str
"""The supported aggregation time periods. For example, if FiveMinutes is the value chosen, and 50 price updates occur for an ASIN within 5 minutes, Amazon will send only two notifications; one for the first event, and then a subsequent notification 5 minutes later with the final end state of the data. The 48 interim events will be dropped."""


"""
AggregationSettings

A container that holds all of the necessary properties to configure the aggregation of notifications.
"""


class AggregationSettings(SpApiBaseModel):
    """A container that holds all of the necessary properties to configure the aggregation of notifications."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    aggregation_time_period: Annotated[
        "AggregationTimePeriod",
        Field(
            ...,
            validation_alias=AliasChoices(
                "aggregationTimePeriod", "aggregation_time_period"
            ),
            serialization_alias="aggregationTimePeriod",
            description="The supported time period to use to perform marketplace-ASIN level aggregation.",
        ),
    ]


"""
AggregationFilter

A filter used to select the aggregation time period at which to send notifications (for example: limit to one notification every five minutes for high frequency notifications).
"""


class AggregationFilter(SpApiBaseModel):
    """A filter used to select the aggregation time period at which to send notifications (for example: limit to one notification every five minutes for high frequency notifications)."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    aggregation_settings: Annotated[
        Optional["AggregationSettings"],
        Field(
            None,
            validation_alias=AliasChoices(
                "aggregationSettings", "aggregation_settings"
            ),
            serialization_alias="aggregationSettings",
        ),
    ]


"""
EventBridgeResourceSpecification

The information required to create an Amazon EventBridge destination.
"""


class EventBridgeResourceSpecification(SpApiBaseModel):
    """The information required to create an Amazon EventBridge destination."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    region: Annotated[
        str,
        Field(
            ...,
            description="The AWS region in which you will be receiving the notifications.",
        ),
    ]

    account_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("accountId", "account_id"),
            serialization_alias="accountId",
            description="The identifier for the AWS account that is responsible for charges related to receiving notifications.",
        ),
    ]


"""
SqsResource

The information required to create an Amazon Simple Queue Service (Amazon SQS) queue destination.
"""


class SqsResource(SpApiBaseModel):
    """The information required to create an Amazon Simple Queue Service (Amazon SQS) queue destination."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    arn: Annotated[
        str,
        Field(
            ...,
            description="The Amazon Resource Name (ARN) associated with the SQS queue.",
        ),
    ]


"""
DestinationResourceSpecification

The information required to create a destination resource. Applications should use one resource type (sqs or eventBridge) per destination.
"""


class DestinationResourceSpecification(SpApiBaseModel):
    """The information required to create a destination resource. Applications should use one resource type (sqs or eventBridge) per destination."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    sqs: Annotated[
        Optional["SqsResource"],
        Field(
            None,
            description="The information required to create an Amazon Simple Queue Service (SQS) queue destination.",
        ),
    ]

    event_bridge: Annotated[
        Optional["EventBridgeResourceSpecification"],
        Field(
            None,
            validation_alias=AliasChoices("eventBridge", "event_bridge"),
            serialization_alias="eventBridge",
            description="The information required to create an Amazon EventBridge destination.",
        ),
    ]


"""
CreateDestinationRequestBody

The request schema for the `createDestination` operation.
"""


class CreateDestinationRequestBody(SpApiBaseModel):
    """The request schema for the `createDestination` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    resource_specification: Annotated[
        "DestinationResourceSpecification",
        Field(
            ...,
            validation_alias=AliasChoices(
                "resourceSpecification", "resource_specification"
            ),
            serialization_alias="resourceSpecification",
            description="The information required to create a destination resource. Applications should use one resource type (sqs or eventBridge) per destination.",
        ),
    ]

    name: Annotated[
        str,
        Field(
            ...,
            description="A developer-defined name to help identify this destination.",
        ),
    ]


"""
CreateDestinationRequest

Request parameters for createDestination
"""


class CreateDestinationRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for createDestination
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    body: Annotated[
        "CreateDestinationRequestBody",
        BodyParam(),
        Field(..., description="[BODY] Parameter"),
    ]


"""
EventBridgeResource

The Amazon EventBridge destination.
"""


class EventBridgeResource(SpApiBaseModel):
    """The Amazon EventBridge destination."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    name: Annotated[
        str,
        Field(
            ...,
            description="The name of the partner event source associated with the destination.",
        ),
    ]

    region: Annotated[
        str,
        Field(
            ...,
            description="The AWS region in which you receive the notifications. For AWS regions that are supported in Amazon EventBridge, refer to [Amazon EventBridge endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/ev.html).",
        ),
    ]

    account_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("accountId", "account_id"),
            serialization_alias="accountId",
            description="The identifier for the AWS account that is responsible for charges related to receiving notifications.",
        ),
    ]


"""
DestinationResource

The destination resource types.
"""


class DestinationResource(SpApiBaseModel):
    """The destination resource types."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    sqs: Annotated[
        Optional["SqsResource"],
        Field(
            None, description="An Amazon Simple Queue Service (SQS) queue destination."
        ),
    ]

    event_bridge: Annotated[
        Optional["EventBridgeResource"],
        Field(
            None,
            validation_alias=AliasChoices("eventBridge", "event_bridge"),
            serialization_alias="eventBridge",
            description="An Amazon EventBridge destination.",
        ),
    ]


"""
Destination

Information about the destination created when you call the `createDestination` operation.
"""


class Destination(SpApiBaseModel):
    """Information about the destination created when you call the `createDestination` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    name: Annotated[
        str, Field(..., description="The developer-defined name for this destination.")
    ]

    destination_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("destinationId", "destination_id"),
            serialization_alias="destinationId",
            description="The destination identifier generated when you created the destination.",
        ),
    ]

    resource: Annotated[
        "DestinationResource",
        Field(
            ...,
            description="The resource that will receive notifications associated with this destination.",
        ),
    ]


ErrorList = List["Error"]
"""A list of error responses returned when a request is unsuccessful."""


"""
CreateDestinationResponse

The response schema for the createDestination operation.
"""


class CreateDestinationResponse(SpApiBaseModel):
    """The response schema for the createDestination operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["Destination"],
        Field(None, description="The payload for the `createDestination` operation."),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
            description="One or more unexpected errors occurred during the `createDestination` operation.",
        ),
    ]


"""
EventFilter

A `notificationType` specific filter. This object contains all of the currently available filters and properties that you can use to define a `notificationType` specific filter.
"""


class EventFilter(SpApiBaseModel):
    """A `notificationType` specific filter. This object contains all of the currently available filters and properties that you can use to define a `notificationType` specific filter."""

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow",
        serialize_by_alias=True,
        arbitrary_types_allowed=True,
    )


"""
ProcessingDirective

Additional information passed to the subscription to control the processing of notifications. For example, you can use an `eventFilter` to customize your subscription to send notifications for only the specified `marketplaceId`s, or select the aggregation time period at which to send notifications (for example: limit to one notification every five minutes for high frequency notifications). The specific features available vary depending on the `notificationType`. This feature is currently only supported by the `ANY_OFFER_CHANGED` and `ORDER_CHANGE` `notificationType`s.
"""


class ProcessingDirective(SpApiBaseModel):
    """Additional information passed to the subscription to control the processing of notifications. For example, you can use an `eventFilter` to customize your subscription to send notifications for only the specified `marketplaceId`s, or select the aggregation time period at which to send notifications (for example: limit to one notification every five minutes for high frequency notifications). The specific features available vary depending on the `notificationType`. This feature is currently only supported by the `ANY_OFFER_CHANGED` and `ORDER_CHANGE` `notificationType`s."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    event_filter: Annotated[
        Optional["EventFilter"],
        Field(
            None,
            validation_alias=AliasChoices("eventFilter", "event_filter"),
            serialization_alias="eventFilter",
            description="A `notificationType` specific filter.",
        ),
    ]


"""
CreateSubscriptionRequestBody

The request schema for the `createSubscription` operation.
"""


class CreateSubscriptionRequestBody(SpApiBaseModel):
    """The request schema for the `createSubscription` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload_version: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("payloadVersion", "payload_version"),
            serialization_alias="payloadVersion",
            description="The version of the payload object to be used in the notification.",
        ),
    ]

    destination_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("destinationId", "destination_id"),
            serialization_alias="destinationId",
            description="The identifier for the destination where notifications will be delivered.",
        ),
    ]

    processing_directive: Annotated[
        Optional["ProcessingDirective"],
        Field(
            None,
            validation_alias=AliasChoices(
                "processingDirective", "processing_directive"
            ),
            serialization_alias="processingDirective",
        ),
    ]


"""
CreateSubscriptionRequest

Request parameters for createSubscription
"""


class CreateSubscriptionRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for createSubscription
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    body: Annotated[
        "CreateSubscriptionRequestBody",
        BodyParam(),
        Field(..., description="[BODY] Parameter"),
    ]

    notification_type: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("notificationType", "notification_type"),
            serialization_alias="notificationType",
            description="[PATH] Path parameter: notificationType",
        ),
    ]


"""
Subscription

Information about the subscription.
"""


class Subscription(SpApiBaseModel):
    """Information about the subscription."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    subscription_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("subscriptionId", "subscription_id"),
            serialization_alias="subscriptionId",
            description="The subscription identifier generated when the subscription is created.",
        ),
    ]

    payload_version: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("payloadVersion", "payload_version"),
            serialization_alias="payloadVersion",
            description="The version of the payload object to be used in the notification.",
        ),
    ]

    destination_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("destinationId", "destination_id"),
            serialization_alias="destinationId",
            description="The identifier for the destination where notifications will be delivered.",
        ),
    ]

    processing_directive: Annotated[
        Optional["ProcessingDirective"],
        Field(
            None,
            validation_alias=AliasChoices(
                "processingDirective", "processing_directive"
            ),
            serialization_alias="processingDirective",
        ),
    ]


"""
CreateSubscriptionResponse

The response schema for the `createSubscription` operation.
"""


class CreateSubscriptionResponse(SpApiBaseModel):
    """The response schema for the `createSubscription` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["Subscription"],
        Field(None, description="The payload for the `createSubscription` operation."),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
            description="One or more unexpected errors occurred during the `createSubscription` operation.",
        ),
    ]


"""
DeleteDestinationRequest

Request parameters for deleteDestination
"""


class DeleteDestinationRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for deleteDestination
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    destination_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("destinationId", "destination_id"),
            serialization_alias="destinationId",
            description="[PATH] The identifier for the destination that you want to delete.",
        ),
    ]


"""
DeleteDestinationResponse

The response schema for the `deleteDestination` operation.
"""


class DeleteDestinationResponse(SpApiBaseModel):
    """The response schema for the `deleteDestination` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
            description="One or more unexpected errors occurred during the `deleteDestination` operation.",
        ),
    ]


"""
DeleteSubscriptionByIdRequest

Request parameters for deleteSubscriptionById
"""


class DeleteSubscriptionByIdRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for deleteSubscriptionById
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    subscription_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("subscriptionId", "subscription_id"),
            serialization_alias="subscriptionId",
            description="[PATH] The identifier for the subscription that you want to delete.",
        ),
    ]

    notification_type: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("notificationType", "notification_type"),
            serialization_alias="notificationType",
            description="[PATH] Path parameter: notificationType",
        ),
    ]


"""
DeleteSubscriptionByIdResponse

The response schema for the `deleteSubscriptionById` operation.
"""


class DeleteSubscriptionByIdResponse(SpApiBaseModel):
    """The response schema for the `deleteSubscriptionById` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
            description="An unexpected condition occurred during the `deleteSubscriptionById` operation.",
        ),
    ]


DestinationList = List["Destination"]
"""A list of destinations."""


"""
Error

An error response returned when the request is unsuccessful.
"""


class Error(SpApiBaseModel):
    """An error response returned when the request is unsuccessful."""

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
GetDestinationRequest

Request parameters for getDestination
"""


class GetDestinationRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getDestination
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    destination_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("destinationId", "destination_id"),
            serialization_alias="destinationId",
            description="[PATH] The identifier generated when you created the destination.",
        ),
    ]


"""
GetDestinationResponse

The response schema for the `getDestination` operation.
"""


class GetDestinationResponse(SpApiBaseModel):
    """The response schema for the `getDestination` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["Destination"],
        Field(None, description="The payload for the `getDestination` operation."),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
            description="One or more unexpected errors occurred during the `getDestination` operation.",
        ),
    ]


"""
GetDestinationsResponse

The response schema for the `getDestinations` operation.
"""


class GetDestinationsResponse(SpApiBaseModel):
    """The response schema for the `getDestinations` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["DestinationList"],
        Field(None, description="The payload for the `getDestinations` operation."),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
            description="One or more unexpected errors occurred during the `getDestinations` operation.",
        ),
    ]


"""
GetSubscriptionByIdRequest

Request parameters for getSubscriptionById
"""


class GetSubscriptionByIdRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getSubscriptionById
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    subscription_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("subscriptionId", "subscription_id"),
            serialization_alias="subscriptionId",
            description="[PATH] The identifier for the subscription that you want to get.",
        ),
    ]

    notification_type: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("notificationType", "notification_type"),
            serialization_alias="notificationType",
            description="[PATH] Path parameter: notificationType",
        ),
    ]


"""
GetSubscriptionByIdResponse

The response schema for the `getSubscriptionById` operation.
"""


class GetSubscriptionByIdResponse(SpApiBaseModel):
    """The response schema for the `getSubscriptionById` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["Subscription"],
        Field(None, description="The payload for the `getSubscriptionById` operation."),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
            description="An unexpected condition occurred during the `getSubscriptionById` operation.",
        ),
    ]


"""
GetSubscriptionRequest

Request parameters for getSubscription
"""


class GetSubscriptionRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getSubscription
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload_version: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("payloadVersion", "payload_version"),
            serialization_alias="payloadVersion",
            description="[QUERY] The version of the payload object to be used in the notification.",
        ),
    ]

    notification_type: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("notificationType", "notification_type"),
            serialization_alias="notificationType",
            description="[PATH] Path parameter: notificationType",
        ),
    ]


"""
GetSubscriptionResponse

The response schema for the `getSubscription` operation.
"""


class GetSubscriptionResponse(SpApiBaseModel):
    """The response schema for the `getSubscription` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["Subscription"],
        Field(None, description="The payload for the `getSubscription` operation."),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
            description="One or more unexpected errors occurred during the `getSubscription` operation.",
        ),
    ]


"""
MarketplaceIds

A list of marketplace identifiers to subscribe to (for example: ATVPDKIKX0DER). To receive notifications in every marketplace, do not provide this list.
"""


class MarketplaceIds(SpApiBaseModel):
    """A list of marketplace identifiers to subscribe to (for example: ATVPDKIKX0DER). To receive notifications in every marketplace, do not provide this list."""

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow",
        serialize_by_alias=True,
        arbitrary_types_allowed=True,
    )


"""
MarketplaceFilter

An event filter to customize your subscription to send notifications for only the specified `marketplaceId`s.
"""


class MarketplaceFilter(SpApiBaseModel):
    """An event filter to customize your subscription to send notifications for only the specified `marketplaceId`s."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    marketplace_ids: Annotated[
        Optional["MarketplaceIds"],
        Field(
            None,
            validation_alias=AliasChoices("marketplaceIds", "marketplace_ids"),
            serialization_alias="marketplaceIds",
        ),
    ]


OrderChangeTypeEnum = str
"""The supported order change type of ORDER_CHANGE notification."""


OrderChangeTypes = List["OrderChangeTypeEnum"]
"""A list of order change types to subscribe to (for example: `BuyerRequestedChange`). To receive notifications of all change types, do not provide this list."""


"""
OrderChangeTypeFilter

An event filter to customize your subscription to send notifications for only the specified `orderChangeType`.
"""


class OrderChangeTypeFilter(SpApiBaseModel):
    """An event filter to customize your subscription to send notifications for only the specified `orderChangeType`."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    order_change_types: Annotated[
        Optional["OrderChangeTypes"],
        Field(
            None,
            validation_alias=AliasChoices("orderChangeTypes", "order_change_types"),
            serialization_alias="orderChangeTypes",
        ),
    ]


# Rebuild models to resolve forward references
ProcessingDirective.model_rebuild()
EventFilter.model_rebuild()
MarketplaceFilter.model_rebuild()
MarketplaceIds.model_rebuild()
AggregationFilter.model_rebuild()
AggregationSettings.model_rebuild()
OrderChangeTypeFilter.model_rebuild()
Subscription.model_rebuild()
CreateSubscriptionResponse.model_rebuild()
CreateSubscriptionRequestBody.model_rebuild()
GetSubscriptionByIdResponse.model_rebuild()
GetSubscriptionResponse.model_rebuild()
DeleteSubscriptionByIdResponse.model_rebuild()
Destination.model_rebuild()
DestinationResource.model_rebuild()
DestinationResourceSpecification.model_rebuild()
SqsResource.model_rebuild()
EventBridgeResourceSpecification.model_rebuild()
EventBridgeResource.model_rebuild()
CreateDestinationRequestBody.model_rebuild()
CreateDestinationResponse.model_rebuild()
GetDestinationResponse.model_rebuild()
GetDestinationsResponse.model_rebuild()
DeleteDestinationResponse.model_rebuild()
Error.model_rebuild()
GetSubscriptionRequest.model_rebuild()
CreateSubscriptionRequest.model_rebuild()
GetSubscriptionByIdRequest.model_rebuild()
DeleteSubscriptionByIdRequest.model_rebuild()
CreateDestinationRequest.model_rebuild()
GetDestinationRequest.model_rebuild()
DeleteDestinationRequest.model_rebuild()
