from datetime import datetime, timedelta, timezone

import pytz

from sp_api.api import Sales
from sp_api.base import Granularity, Marketplaces
import logging

tz = pytz.timezone('US/Central')
fmt = '%Y-%m-%dT%H:%M:%S%z'

interval = ( datetime.now(tz) - timedelta(days=185) ), ( datetime.now(tz) )


def test_sales_granularity_hour():
    s = Sales().get_order_metrics(interval, Granularity.HOUR)
    print(s)


def test_sales_granularity_day():
    s = Sales().get_order_metrics(interval, Granularity.DAY, granularityTimeZone='US/Central')
    print(s)


def test_sales_granularity_week():
    s = Sales().get_order_metrics(interval, Granularity.WEEK, granularityTimeZone='US/Central')
    print(s)


def test_sales_granularity_month():
    s = Sales().get_order_metrics(interval, Granularity.MONTH, granularityTimeZone='US/Central')
    print(s)


def test_sales_granularity_year():
    s = Sales().get_order_metrics(interval, Granularity.YEAR, granularityTimeZone='US/Central')
    print(s)
