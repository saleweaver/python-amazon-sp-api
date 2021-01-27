from sp_api.api import Feeds
from sp_api.base import Marketplaces


def test_submit_feed():
    res = Feeds(marketplace=Marketplaces.DE).submit_feed('POST_PRODUCT_DATA', open('test.xml'), 'application/xml')
    print(res)

def test_get_feed():
    feed_id = ''
    print(Feeds(marketplace=Marketplaces.DE).get_feed(feed_id))


def test_get_feed_results():
    feed_doc_id = ''
    print(Feeds(marketplace=Marketplaces.DE).get_feed_result_document(feed_doc_id))

