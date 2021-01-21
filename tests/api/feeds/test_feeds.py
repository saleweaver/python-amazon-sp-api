from sp_api.api import Feeds
from sp_api.base import Marketplaces


def test_submit_feed():
    res = Feeds(marketplace=Marketplaces.DE).submit_feed('POST_FLAT_FILE_INVLOADER_DATA', open('test.tsv'))
    print(res)


def test_get_feed():
    feed_id = '50635018648'
    print(Feeds(marketplace=Marketplaces.DE).get_feed(feed_id))


def test_get_feed_results():
    feed_doc_id = 'amzn1.tortuga.3.0afe8db9-1a27-46e5-be2f-7205c7168628.TSVW29HBP1SDR'
    print(Feeds(marketplace=Marketplaces.DE).get_feed_result_document(feed_doc_id))
