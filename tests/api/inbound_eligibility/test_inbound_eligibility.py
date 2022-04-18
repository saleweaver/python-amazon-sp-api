from sp_api.api import FbaInboundEligibility


def test_inbound_eligibility():
    res = FbaInboundEligibility().get_item_eligibility_preview(asin='TEST_CASE_200', program="INBOUND")
    assert res.payload is not None
