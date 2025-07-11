# Auto-generated tests for sp_api.api.models.sales.sales_v1.common.py
from datetime import datetime

import pytest
from sp_api.api.models.sales.sales_v1.common import (
    Error, GetOrderMetricsRequest, GetOrderMetricsRequestAmazonProgramEnum,
    GetOrderMetricsRequestBuyerTypeEnum,
    GetOrderMetricsRequestFirstDayOfWeekEnum,
    GetOrderMetricsRequestGranularityEnum, GetOrderMetricsResponse,
    GetRequestSerializer, Money, OrderMetricsInterval, RequestsBaseModel,
    SpApiBaseModel)


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


def test_error_instantiates():
    """Instantiate Error with dummy data"""
    kwargs = {
        "code": "",
        "message": "",
        "details": None,
    }
    obj = Error(**kwargs)
    assert isinstance(obj, Error)


def test_getordermetricsrequest_instantiates():
    """Instantiate GetOrderMetricsRequest with dummy data"""
    kwargs = {
        "marketplace_ids": None,
        "interval": "",
        "granularity_time_zone": None,
        "granularity": GetOrderMetricsRequestGranularityEnum.HOUR,
        "buyer_type": None,
        "fulfillment_network": None,
        "first_day_of_week": None,
        "asin": None,
        "sku": None,
        "amazon_program": None,
    }
    obj = GetOrderMetricsRequest(**kwargs)
    assert isinstance(obj, GetOrderMetricsRequest)


def test_getordermetricsresponse_instantiates():
    """Instantiate GetOrderMetricsResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = GetOrderMetricsResponse(**kwargs)
    assert isinstance(obj, GetOrderMetricsResponse)


def test_money_instantiates():
    """Instantiate Money with dummy data"""
    kwargs = {
        "currency_code": "",
        "amount": "",
    }
    obj = Money(**kwargs)
    assert isinstance(obj, Money)


def test_ordermetricsinterval_instantiates():
    """Instantiate OrderMetricsInterval with dummy data"""
    kwargs = {
        "interval": "",
        "unit_count": 0,
        "order_item_count": 0,
        "order_count": 0,
        "average_unit_price": Money(**{"currency_code": "", "amount": ""}),
        "total_sales": Money(**{"currency_code": "", "amount": ""}),
    }
    obj = OrderMetricsInterval(**kwargs)
    assert isinstance(obj, OrderMetricsInterval)
