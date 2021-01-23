from sp_api.api import Feeds
from sp_api.base import Marketplaces


def test_submit_feed():
    res = Feeds(marketplace=Marketplaces.DE).submit_feed('POST_FLAT_FILE_INVLOADER_DATA', open('test.tsv'))
    print(res)


def test_get_feed():
    feed_id = ''
    print(Feeds(marketplace=Marketplaces.GB).get_feed(feed_id))


def test_get_feed_results():
    feed_doc_id = ''
    print(Feeds(marketplace=Marketplaces.FR).get_feed_result_document(feed_doc_id))

