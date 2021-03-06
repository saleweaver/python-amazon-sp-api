import json
from datetime import datetime, timedelta

from sp_api.api import Finances
from sp_api.base import SellingApiBadRequestException


def test_for_order():
    res = Finances().get_financial_events_for_order('485-734-5434857', MaxResultsPerPage=10)
    assert res.payload.get('NextToken') == 'Next token value'


def test_for_order_expect_400():
    try:
        Finances().get_financial_events_for_order('BAD-ORDER', MaxResultsPerPage=10)
    except SellingApiBadRequestException as br:
        assert br.code == 400
        assert type(br) == SellingApiBadRequestException

