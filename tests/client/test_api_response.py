import pytest
from sp_api.base.ApiResponse import ApiResponse


def test_empty_response():
    resp = ApiResponse()
    assert isinstance(resp.payload, dict) is True
    assert resp.payload == {}
    assert resp.errors is None
    assert resp.pagination is None
    assert resp.headers is None
    assert resp.nextToken is None


def test_class_methods():
    resp = ApiResponse(payload={'foo': 'bar'})
    assert resp.foo == 'bar'
    assert resp() == {'foo': 'bar'}
    assert resp('foo') == 'bar'
    assert str(resp) == "{'errors': None,\n 'headers': None,\n 'kwargs': {},\n 'next_token': None,\n 'pagination': " \
                        "None,\n 'payload': {'foo': 'bar'},\n 'rate_limit': None}"


@pytest.fixture(params=[
    # payload, errors, pagination, headers, nextToken, **kwargs
    [None, None, None, None, 'test_token'],
    [None, None, {'nextToken': 'test_token'}, None, None],
    [{'NextToken': 'test_token'}, None, None, None, None],
    [{'pagination': {'nextToken': 'test_token'}}, None, None, None, None],
])
def next_token_api_response(request):
    return ApiResponse(*request.param)


def test_next_token(next_token_api_response):
    assert next_token_api_response.next_token == 'test_token'


def test_api_response():
    payload = {"example_key": "example_value"}
    errors = "example_error"
    pagination = "example_pagination"
    headers = {"x-amzn-RateLimit-Limit": 10}
    nextToken = "example_next_token"

    response = ApiResponse(
        payload=payload,
        errors=errors,
        pagination=pagination,
        headers=headers,
        nextToken=nextToken
    )

    assert response.payload == payload
    assert response.errors == errors
    assert response.pagination == pagination
    assert response.headers == headers
    assert response.rate_limit == 10
    assert response.next_token == nextToken
