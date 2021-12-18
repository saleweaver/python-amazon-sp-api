import os
import pytest

from sp_api.api import FulfillmentInbound
from sp_api.base import Marketplaces, MissingCredentials
from sp_api.base.credential_provider import FromCodeCredentialProvider, FromEnvironmentVariablesCredentialProvider, \
    FromSecretsCredentialProvider, FromConfigFileCredentialProvider, required_credentials


refresh_token = '<refresh_token>'
lwa_app_id = '<lwa_app_id>'
lwa_client_secret = '<lwa_client_secret>'
aws_secret_key = '<aws_secret_access_key>'
aws_access_key = '<aws_access_key_id>'
role_arn = '<role_arn>'


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
        aws_secret_key=aws_secret_key,
        aws_access_key=aws_access_key,
        role_arn=role_arn,
    ))
    assert p.credentials is not None
    assert isinstance(p.credentials, dict)


def test_from_code_credential_provider_no_role():
    p = FromCodeCredentialProvider(credentials=dict(
        refresh_token=refresh_token,
        lwa_app_id=lwa_app_id,
        lwa_client_secret=lwa_client_secret,
        aws_secret_key=aws_secret_key,
        aws_access_key=aws_access_key,
    ))
    assert p.credentials is not None
    assert isinstance(p.credentials, dict)
    assert p.credentials.get('role_arn') is None


def test_from_code_credential_provider_no_role_no_refresh_token():
    p = FromCodeCredentialProvider(credentials=dict(
        lwa_app_id=lwa_app_id,
        lwa_client_secret=lwa_client_secret,
        aws_secret_key=aws_secret_key,
        aws_access_key=aws_access_key,
    ))
    assert p.credentials is not None
    assert isinstance(p.credentials, dict)
    assert p.credentials.get('role_arn') is None
    assert p.credentials.get('refresh_token') is None


@pytest.mark.order(-2)
def test_env_vars_provider():
    os.environ['SP_API_REFRESH_TOKEN'] = 'foo'
    os.environ['LWA_APP_ID'] = 'foo'
    os.environ['LWA_CLIENT_SECRET'] = 'foo'
    os.environ['SP_API_ACCESS_KEY'] = 'foo'
    os.environ['SP_API_SECRET_KEY'] = 'foo'
    os.environ['SP_API_ROLE_ARN'] = 'foo'

    p = FromEnvironmentVariablesCredentialProvider()()
    assert 'refresh_token' in p

    os.environ.pop('SP_API_REFRESH_TOKEN')
    os.environ.pop('LWA_APP_ID')
    os.environ.pop('LWA_CLIENT_SECRET')
    os.environ.pop('SP_API_ACCESS_KEY')
    os.environ.pop('SP_API_SECRET_KEY')
    os.environ.pop('SP_API_ROLE_ARN')


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
    assert len(required_credentials) == 4

