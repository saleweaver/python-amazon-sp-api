from sp_api.api import Feeds
from sp_api.base import SellingApiBadRequestException, SellingApiServerException


def test_create_feed():
    res = Feeds().create_feed('POST_PRODUCT_DATA', '3d4e42b5-1d6e-44e8-a89c-2abfca0625bb',
                              marketplaceIds=["ATVPDKIKX0DER", "A1F83G8C2ARO7P"])
    assert res.payload.get('feedId') == '3485934'


def test_get_feed():
    feed_id = 'feedId1'
    res = Feeds().get_feed(feed_id)
    assert res.payload.get('feedId') == 'FeedId1'
    assert res.payload.get('processingStatus') == 'CANCELLED'


def test_get_feed_expect_400():
    try:
        Feeds().get_feed('badFeedId1')
    except SellingApiBadRequestException as br:
        assert type(br) == SellingApiBadRequestException
        assert br.code == 400


def test_get_feed_expect_500():
    try:
        Feeds().get_feed('giberish')
    except SellingApiServerException as br:
        assert type(br) == SellingApiServerException
        assert br.code == 500

