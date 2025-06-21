# Auto-generated tests for sp_api.api.models.notifications.notifications_v1.common.py
from datetime import datetime

import pytest
from sp_api.api.models.notifications.notifications_v1.common import (
    AggregationFilter, AggregationSettings, CreateDestinationRequest,
    CreateDestinationRequestBody, CreateDestinationResponse,
    CreateSubscriptionRequest, CreateSubscriptionRequestBody,
    CreateSubscriptionResponse, DeleteDestinationRequest,
    DeleteDestinationResponse, DeleteSubscriptionByIdRequest,
    DeleteSubscriptionByIdResponse, Destination, DestinationResource,
    DestinationResourceSpecification, Error, EventBridgeResource,
    EventBridgeResourceSpecification, EventFilter, GetDestinationRequest,
    GetDestinationResponse, GetDestinationsResponse, GetRequestSerializer,
    GetSubscriptionByIdRequest, GetSubscriptionByIdResponse,
    GetSubscriptionRequest, GetSubscriptionResponse, MarketplaceFilter,
    MarketplaceIds, OrderChangeTypeFilter, ProcessingDirective,
    RequestsBaseModel, SpApiBaseModel, SqsResource, Subscription)


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


def test_aggregationsettings_instantiates():
    """Instantiate AggregationSettings with dummy data"""
    kwargs = {
        "aggregation_time_period": "",
    }
    obj = AggregationSettings(**kwargs)
    assert isinstance(obj, AggregationSettings)


def test_aggregationfilter_instantiates():
    """Instantiate AggregationFilter with dummy data"""
    kwargs = {
        "aggregation_settings": None,
    }
    obj = AggregationFilter(**kwargs)
    assert isinstance(obj, AggregationFilter)


def test_eventbridgeresourcespecification_instantiates():
    """Instantiate EventBridgeResourceSpecification with dummy data"""
    kwargs = {
        "region": "",
        "account_id": "",
    }
    obj = EventBridgeResourceSpecification(**kwargs)
    assert isinstance(obj, EventBridgeResourceSpecification)


def test_sqsresource_instantiates():
    """Instantiate SqsResource with dummy data"""
    kwargs = {
        "arn": "",
    }
    obj = SqsResource(**kwargs)
    assert isinstance(obj, SqsResource)


def test_destinationresourcespecification_instantiates():
    """Instantiate DestinationResourceSpecification with dummy data"""
    kwargs = {
        "sqs": None,
        "event_bridge": None,
    }
    obj = DestinationResourceSpecification(**kwargs)
    assert isinstance(obj, DestinationResourceSpecification)


def test_createdestinationrequestbody_instantiates():
    """Instantiate CreateDestinationRequestBody with dummy data"""
    kwargs = {
        "resource_specification": DestinationResourceSpecification(
            **{"sqs": None, "event_bridge": None}
        ),
        "name": "",
    }
    obj = CreateDestinationRequestBody(**kwargs)
    assert isinstance(obj, CreateDestinationRequestBody)


def test_createdestinationrequest_instantiates():
    """Instantiate CreateDestinationRequest with dummy data"""
    kwargs = {
        "body": CreateDestinationRequestBody(
            **{
                "resource_specification": DestinationResourceSpecification(
                    **{"sqs": None, "event_bridge": None}
                ),
                "name": "",
            }
        ),
    }
    obj = CreateDestinationRequest(**kwargs)
    assert isinstance(obj, CreateDestinationRequest)


def test_eventbridgeresource_instantiates():
    """Instantiate EventBridgeResource with dummy data"""
    kwargs = {
        "name": "",
        "region": "",
        "account_id": "",
    }
    obj = EventBridgeResource(**kwargs)
    assert isinstance(obj, EventBridgeResource)


def test_destinationresource_instantiates():
    """Instantiate DestinationResource with dummy data"""
    kwargs = {
        "sqs": None,
        "event_bridge": None,
    }
    obj = DestinationResource(**kwargs)
    assert isinstance(obj, DestinationResource)


def test_destination_instantiates():
    """Instantiate Destination with dummy data"""
    kwargs = {
        "name": "",
        "destination_id": "",
        "resource": DestinationResource(**{"sqs": None, "event_bridge": None}),
    }
    obj = Destination(**kwargs)
    assert isinstance(obj, Destination)


def test_createdestinationresponse_instantiates():
    """Instantiate CreateDestinationResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = CreateDestinationResponse(**kwargs)
    assert isinstance(obj, CreateDestinationResponse)


def test_eventfilter_instantiates():
    """Instantiate EventFilter with dummy data"""
    kwargs = {}
    obj = EventFilter(**kwargs)
    assert isinstance(obj, EventFilter)


def test_processingdirective_instantiates():
    """Instantiate ProcessingDirective with dummy data"""
    kwargs = {
        "event_filter": None,
    }
    obj = ProcessingDirective(**kwargs)
    assert isinstance(obj, ProcessingDirective)


def test_createsubscriptionrequestbody_instantiates():
    """Instantiate CreateSubscriptionRequestBody with dummy data"""
    kwargs = {
        "payload_version": "",
        "destination_id": "",
        "processing_directive": None,
    }
    obj = CreateSubscriptionRequestBody(**kwargs)
    assert isinstance(obj, CreateSubscriptionRequestBody)


def test_createsubscriptionrequest_instantiates():
    """Instantiate CreateSubscriptionRequest with dummy data"""
    kwargs = {
        "body": CreateSubscriptionRequestBody(
            **{
                "payload_version": "",
                "destination_id": "",
                "processing_directive": None,
            }
        ),
        "notification_type": "",
    }
    obj = CreateSubscriptionRequest(**kwargs)
    assert isinstance(obj, CreateSubscriptionRequest)


def test_subscription_instantiates():
    """Instantiate Subscription with dummy data"""
    kwargs = {
        "subscription_id": "",
        "payload_version": "",
        "destination_id": "",
        "processing_directive": None,
    }
    obj = Subscription(**kwargs)
    assert isinstance(obj, Subscription)


def test_createsubscriptionresponse_instantiates():
    """Instantiate CreateSubscriptionResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = CreateSubscriptionResponse(**kwargs)
    assert isinstance(obj, CreateSubscriptionResponse)


def test_deletedestinationrequest_instantiates():
    """Instantiate DeleteDestinationRequest with dummy data"""
    kwargs = {
        "destination_id": "",
    }
    obj = DeleteDestinationRequest(**kwargs)
    assert isinstance(obj, DeleteDestinationRequest)


def test_deletedestinationresponse_instantiates():
    """Instantiate DeleteDestinationResponse with dummy data"""
    kwargs = {
        "errors": None,
    }
    obj = DeleteDestinationResponse(**kwargs)
    assert isinstance(obj, DeleteDestinationResponse)


def test_deletesubscriptionbyidrequest_instantiates():
    """Instantiate DeleteSubscriptionByIdRequest with dummy data"""
    kwargs = {
        "subscription_id": "",
        "notification_type": "",
    }
    obj = DeleteSubscriptionByIdRequest(**kwargs)
    assert isinstance(obj, DeleteSubscriptionByIdRequest)


def test_deletesubscriptionbyidresponse_instantiates():
    """Instantiate DeleteSubscriptionByIdResponse with dummy data"""
    kwargs = {
        "errors": None,
    }
    obj = DeleteSubscriptionByIdResponse(**kwargs)
    assert isinstance(obj, DeleteSubscriptionByIdResponse)


def test_error_instantiates():
    """Instantiate Error with dummy data"""
    kwargs = {
        "code": "",
        "message": "",
        "details": None,
    }
    obj = Error(**kwargs)
    assert isinstance(obj, Error)


def test_getdestinationrequest_instantiates():
    """Instantiate GetDestinationRequest with dummy data"""
    kwargs = {
        "destination_id": "",
    }
    obj = GetDestinationRequest(**kwargs)
    assert isinstance(obj, GetDestinationRequest)


def test_getdestinationresponse_instantiates():
    """Instantiate GetDestinationResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = GetDestinationResponse(**kwargs)
    assert isinstance(obj, GetDestinationResponse)


def test_getdestinationsresponse_instantiates():
    """Instantiate GetDestinationsResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = GetDestinationsResponse(**kwargs)
    assert isinstance(obj, GetDestinationsResponse)


def test_getsubscriptionbyidrequest_instantiates():
    """Instantiate GetSubscriptionByIdRequest with dummy data"""
    kwargs = {
        "subscription_id": "",
        "notification_type": "",
    }
    obj = GetSubscriptionByIdRequest(**kwargs)
    assert isinstance(obj, GetSubscriptionByIdRequest)


def test_getsubscriptionbyidresponse_instantiates():
    """Instantiate GetSubscriptionByIdResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = GetSubscriptionByIdResponse(**kwargs)
    assert isinstance(obj, GetSubscriptionByIdResponse)


def test_getsubscriptionrequest_instantiates():
    """Instantiate GetSubscriptionRequest with dummy data"""
    kwargs = {
        "payload_version": None,
        "notification_type": "",
    }
    obj = GetSubscriptionRequest(**kwargs)
    assert isinstance(obj, GetSubscriptionRequest)


def test_getsubscriptionresponse_instantiates():
    """Instantiate GetSubscriptionResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = GetSubscriptionResponse(**kwargs)
    assert isinstance(obj, GetSubscriptionResponse)


def test_marketplaceids_instantiates():
    """Instantiate MarketplaceIds with dummy data"""
    kwargs = {}
    obj = MarketplaceIds(**kwargs)
    assert isinstance(obj, MarketplaceIds)


def test_marketplacefilter_instantiates():
    """Instantiate MarketplaceFilter with dummy data"""
    kwargs = {
        "marketplace_ids": None,
    }
    obj = MarketplaceFilter(**kwargs)
    assert isinstance(obj, MarketplaceFilter)


def test_orderchangetypefilter_instantiates():
    """Instantiate OrderChangeTypeFilter with dummy data"""
    kwargs = {
        "order_change_types": None,
    }
    obj = OrderChangeTypeFilter(**kwargs)
    assert isinstance(obj, OrderChangeTypeFilter)
