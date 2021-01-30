import json

from sp_api.api import Finances


def test_for_order():
    res = Finances().get_financial_events_for_order('485-734-5434857', MaxResultsPerPage=10)
    assert res.payload.get('NextToken') == 'Next token value'
