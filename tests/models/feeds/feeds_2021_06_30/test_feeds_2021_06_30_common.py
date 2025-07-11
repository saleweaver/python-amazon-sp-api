# Auto-generated tests for sp_api.api.models.feeds.feeds_2021_06_30.common.py
from datetime import datetime

import pytest
from sp_api.api.models.feeds.feeds_2021_06_30.common import (
    CancelFeedRequest, CreateFeedDocumentRequest, CreateFeedDocumentResponse,
    CreateFeedDocumentSpecification, CreateFeedRequest, CreateFeedResponse,
    CreateFeedSpecification, Error, ErrorList, Feed, FeedDocument,
    FeedDocumentCompressionAlgorithmEnum, FeedOptions,
    FeedProcessingStatusEnum, GetFeedDocumentRequest, GetFeedRequest,
    GetFeedsRequest, GetFeedsRequestProcessingStatusesEnum, GetFeedsResponse,
    GetRequestSerializer, RequestsBaseModel, SpApiBaseModel)


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


def test_cancelfeedrequest_instantiates():
    """Instantiate CancelFeedRequest with dummy data"""
    kwargs = {
        "feed_id": "",
    }
    obj = CancelFeedRequest(**kwargs)
    assert isinstance(obj, CancelFeedRequest)


def test_createfeeddocumentspecification_instantiates():
    """Instantiate CreateFeedDocumentSpecification with dummy data"""
    kwargs = {
        "content_type": "",
    }
    obj = CreateFeedDocumentSpecification(**kwargs)
    assert isinstance(obj, CreateFeedDocumentSpecification)


def test_createfeeddocumentrequest_instantiates():
    """Instantiate CreateFeedDocumentRequest with dummy data"""
    kwargs = {
        "body": CreateFeedDocumentSpecification(**{"content_type": ""}),
    }
    obj = CreateFeedDocumentRequest(**kwargs)
    assert isinstance(obj, CreateFeedDocumentRequest)


def test_createfeeddocumentresponse_instantiates():
    """Instantiate CreateFeedDocumentResponse with dummy data"""
    kwargs = {
        "feed_document_id": "",
        "url": "",
    }
    obj = CreateFeedDocumentResponse(**kwargs)
    assert isinstance(obj, CreateFeedDocumentResponse)


def test_feedoptions_instantiates():
    """Instantiate FeedOptions with dummy data"""
    kwargs = {}
    obj = FeedOptions(**kwargs)
    assert isinstance(obj, FeedOptions)


def test_createfeedspecification_instantiates():
    """Instantiate CreateFeedSpecification with dummy data"""
    kwargs = {
        "feed_type": "",
        "marketplace_ids": None,
        "input_feed_document_id": "",
        "feed_options": None,
    }
    obj = CreateFeedSpecification(**kwargs)
    assert isinstance(obj, CreateFeedSpecification)


def test_createfeedrequest_instantiates():
    """Instantiate CreateFeedRequest with dummy data"""
    kwargs = {
        "body": CreateFeedSpecification(
            **{
                "feed_type": "",
                "marketplace_ids": None,
                "input_feed_document_id": "",
                "feed_options": None,
            }
        ),
    }
    obj = CreateFeedRequest(**kwargs)
    assert isinstance(obj, CreateFeedRequest)


def test_createfeedresponse_instantiates():
    """Instantiate CreateFeedResponse with dummy data"""
    kwargs = {
        "feed_id": "",
    }
    obj = CreateFeedResponse(**kwargs)
    assert isinstance(obj, CreateFeedResponse)


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


def test_feed_instantiates():
    """Instantiate Feed with dummy data"""
    kwargs = {
        "feed_id": "",
        "feed_type": "",
        "marketplace_ids": None,
        "created_time": datetime(2000, 1, 1),
        "processing_status": FeedProcessingStatusEnum.CANCELLED,
        "processing_start_time": None,
        "processing_end_time": None,
        "result_feed_document_id": None,
    }
    obj = Feed(**kwargs)
    assert isinstance(obj, Feed)


def test_feeddocument_instantiates():
    """Instantiate FeedDocument with dummy data"""
    kwargs = {
        "feed_document_id": "",
        "url": "",
        "compression_algorithm": None,
    }
    obj = FeedDocument(**kwargs)
    assert isinstance(obj, FeedDocument)


def test_getfeeddocumentrequest_instantiates():
    """Instantiate GetFeedDocumentRequest with dummy data"""
    kwargs = {
        "feed_document_id": "",
    }
    obj = GetFeedDocumentRequest(**kwargs)
    assert isinstance(obj, GetFeedDocumentRequest)


def test_getfeedrequest_instantiates():
    """Instantiate GetFeedRequest with dummy data"""
    kwargs = {
        "feed_id": "",
    }
    obj = GetFeedRequest(**kwargs)
    assert isinstance(obj, GetFeedRequest)


def test_getfeedsrequest_instantiates():
    """Instantiate GetFeedsRequest with dummy data"""
    kwargs = {
        "feed_types": None,
        "marketplace_ids": None,
        "page_size": None,
        "processing_statuses": None,
        "created_since": None,
        "created_until": None,
        "next_token": None,
    }
    obj = GetFeedsRequest(**kwargs)
    assert isinstance(obj, GetFeedsRequest)


def test_getfeedsresponse_instantiates():
    """Instantiate GetFeedsResponse with dummy data"""
    kwargs = {
        "feeds": [],
        "next_token": None,
    }
    obj = GetFeedsResponse(**kwargs)
    assert isinstance(obj, GetFeedsResponse)
