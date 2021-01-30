from sp_api.api import Feeds


def test_create_feed():
    res = Feeds().create_feed('POST_PRODUCT_DATA', '3d4e42b5-1d6e-44e8-a89c-2abfca0625bb',
                              marketplaceIds=["ATVPDKIKX0DER", "A1F83G8C2ARO7P"])
    assert res.payload.get('feedId') == '3485934'


def test_get_feed():
    feed_id = 'feedId1'
    res = Feeds().get_feed(feed_id)
    assert res.payload.get('feedId') == 'FeedId1'
    assert res.payload.get('processingStatus') == 'CANCELLED'

