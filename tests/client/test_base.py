import os
import pytest

from sp_api.api import FulfillmentInbound
from sp_api.base import AccessTokenClient
from sp_api.base import Marketplaces, MissingCredentials, Client, SellingApiForbiddenException
from sp_api.base.credential_provider import FromCodeCredentialProvider, FromEnvironmentVariablesCredentialProvider, \
    FromSecretsCredentialProvider, FromConfigFileCredentialProvider, required_credentials
from sp_api.base.exceptions import MissingScopeException

refresh_token = '<refresh_token>'
lwa_app_id = '<lwa_app_id>'
lwa_client_secret = '<lwa_client_secret>'


class Res:
    status_code = 200
    method = 'GET'
    headers = {}
    def json(self):
        return {'foo': 'bar'}

    def __getattr__(self, item):
        return item


def test_client_request():
    try:
        Client()._request('', data=dict())
    except SellingApiForbiddenException as e:
        assert isinstance(e, SellingApiForbiddenException)


def test_client_timeout():
    client = Client(timeout=1)
    assert client.timeout == 1
    client = Client()
    assert client.timeout is None


def test_api_response_has_next_token():
    res = FulfillmentInbound().get_shipments(QueryType='SHIPMENT')
    assert res.next_token is not None


def test_marketplaces():
    assert Marketplaces.DE.region == 'eu-west-1'
    assert Marketplaces.US.marketplace_id == 'ATVPDKIKX0DER'


def test_from_code_credential_provider():
    p = FromCodeCredentialProvider(credentials=dict(
        refresh_token=refresh_token,
        lwa_app_id=lwa_app_id,
        lwa_client_secret=lwa_client_secret,
    ))
    assert p.credentials is not None
    assert isinstance(p.credentials, dict)


def test_from_code_credential_provider_no_refresh_token():
    p = FromCodeCredentialProvider(credentials=dict(
        lwa_app_id=lwa_app_id,
        lwa_client_secret=lwa_client_secret,
    ))
    assert p.credentials is not None
    assert isinstance(p.credentials, dict)
    assert p.credentials.get('refresh_token') is None


@pytest.mark.order(-2)
def test_env_vars_provider():
    os.environ['SP_API_REFRESH_TOKEN'] = 'foo'
    os.environ['LWA_APP_ID'] = 'foo'
    os.environ['LWA_CLIENT_SECRET'] = 'foo'

    p = FromEnvironmentVariablesCredentialProvider()()
    assert 'refresh_token' in p

    os.environ.pop('SP_API_REFRESH_TOKEN')
    os.environ.pop('LWA_APP_ID')
    os.environ.pop('LWA_CLIENT_SECRET')


@pytest.mark.order(-1)
def test_from_secrets():
    os.environ['SP_API_AWS_SECRET_ID'] = 'testing/sp-api-foo'
    try:
        p = FromSecretsCredentialProvider()()
        assert 'refresh_token' in p
        assert p.get('refresh_token') == 'foo'
        os.environ.pop('SP_API_AWS_SECRET_ID')
    except MissingCredentials as e:
        assert isinstance(e, MissingCredentials)


def test_from_config_file_provider():
    try:
        p = FromConfigFileCredentialProvider()()
        assert p.get('refresh_token') is not None
    except MissingCredentials as e:
        assert isinstance(e, MissingCredentials)


def test_req():
    assert len(required_credentials) == 2


def test_client():
    client = Client(marketplace=Marketplaces.UK)
    assert client.marketplace_id == Marketplaces.UK.marketplace_id
    assert client.credentials is not None
    assert client.endpoint == Marketplaces.UK.endpoint
    assert client.region == Marketplaces.UK.region
    assert client.restricted_data_token is None
    assert isinstance(client._auth, AccessTokenClient)

    assert isinstance(client._get_cache_key(), str)
    assert isinstance(client._get_cache_key('test'), str)

    assert client.headers['host'] == client.endpoint[8:]
    assert len(client.headers.keys()) == 5

    assert client.auth is not None
    try:
        x = client.grantless_auth
    except MissingScopeException as e:
        assert isinstance(e, MissingScopeException)

    try:
        client._request('', data={})
    except SellingApiForbiddenException as e:
        assert isinstance(e, SellingApiForbiddenException)
    try:
        client._request('', params={})
    except SellingApiForbiddenException as e:
        assert isinstance(e, SellingApiForbiddenException)

    check = client._check_response(Res())
    assert check.payload['foo'] == 'bar'

    r = Res()
    r.method = 'POST'
    check = client._check_response(r)
    assert check.payload['foo'] == 'bar'
    assert check('foo') == 'bar'
    assert check.foo == 'bar'
    assert check()['foo'] == 'bar'

    r.method = 'DELETE'
    check = client._check_response(r)
    assert check.payload['foo'] == 'bar'
    assert check('foo') == 'bar'
    assert check.foo == 'bar'
    assert check()['foo'] == 'bar'

    client.grantless_scope = 'sellingpartnerapi::notifications'
    assert client.grantless_auth is not None

    try:
        client._request_grantless_operation('')
    except SellingApiForbiddenException as e:
        assert isinstance(e, SellingApiForbiddenException)
