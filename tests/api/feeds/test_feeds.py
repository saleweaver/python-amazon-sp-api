from sp_api.api import Feeds
from sp_api.base import Marketplaces


def test_submit_feed():
    res = Feeds(marketplace=Marketplaces.DE).submit_feed('POST_FLAT_FILE_INVLOADER_DATA', open('/Users/michael/dev/programs/private/python-sp-api/test.tsv'))
    print(res)


def test_get_feed():
    feed_id = '50642018648'
    print(Feeds(marketplace=Marketplaces.DE).get_feed(feed_id))


def test_get_feed_results():
    feed_doc_id = 'amzn1.tortuga.3.41f4b22c-2c06-4cc7-8cf5-88b23cbf6cbb.TQFDX97S9IQZP'
    print(Feeds(marketplace=Marketplaces.DE).get_feed_result_document(feed_doc_id))
