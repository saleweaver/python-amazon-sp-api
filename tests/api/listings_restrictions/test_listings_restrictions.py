from sp_api.api import ListingsRestrictions


def test_listing_restrictions():
    res = ListingsRestrictions().get_listings_restrictions(sellerId='A3F26DF64ZIPJZ', asin='B07HRD6JKK')
    assert res('restrictions') is not None
    assert isinstance(res('restrictions'), list)

