import json

from base.helpers import fill_query_params


def test_create_path():
    query = 'foo/bar/{}/baz/{}'
    res = fill_query_params(query, 'foooo', 'baz')
    assert res == 'foo/bar/foooo/baz/baz'
