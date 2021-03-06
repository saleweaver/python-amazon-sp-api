from datetime import datetime, timedelta, timezone

import pytz

from sp_api.api import Sales
from sp_api.base import Granularity, Marketplaces, CredentialProvider
import logging

tz = pytz.timezone('US/Central')
fmt = '%Y-%m-%dT%H:%M:%S%z'

interval = (datetime.now(tz) - timedelta(days=185)), (datetime.now(tz))


def test_sales_granularity_total():
    res = Sales().get_order_metrics(interval, Granularity.TOTAL, granularityTimeZone='US/Central')
    assert res.payload[0].get('unitCount') == 2


def test_sales_granularity_day():
    res = Sales().get_order_metrics(interval, Granularity.DAY, granularityTimeZone='US/Central')
    assert res.payload[0].get('unitCount') == 1


def test_sales_granularity_total_by_asin():
    res = Sales().get_order_metrics(interval, Granularity.TOTAL, granularityTimeZone='US/Central', asin='B008OLKVEW')
    assert res.payload[0].get('unitCount') == 1


def test_sales_granularity_day_by_asin():
    res = Sales().get_order_metrics(interval, Granularity.DAY, granularityTimeZone='US/Central', asin='B008OLKVEW')
    assert res.payload[0].get('unitCount') == 1


