from sp_api.base import AccessTokenClient
from sp_api.base import Credentials, CredentialProvider
from sp_api.base import AuthorizationError
from sp_api.base.credential_provider import FromCodeCredentialProvider
refresh_token = '<refresh_token>'
lwa_app_id = '<lwa_app_id>'
lwa_client_secret = '<lwa_client_secret>'
aws_secret_key = '<aws_secret_access_key>'
aws_access_key = '<aws_access_key_id>'
role_arn = '<role_arn>'



def test_auth_exception():
    e = AuthorizationError(200, 'Foo', 999)
    assert e.status_code == 999
    assert e.error_code == 200
    assert e.message == 'Foo'


def test_credentials():
    x = CredentialProvider()
    assert x.credentials.lwa_app_id is not None
    assert x.credentials.lwa_client_secret is not None
    assert x.credentials.aws_secret_key is not None
    assert x.credentials.aws_access_key is not None


def test_auth_client():
    client = AccessTokenClient(credentials=CredentialProvider(credentials=dict(
        refresh_token=refresh_token,
        lwa_app_id=lwa_app_id,
        lwa_client_secret=lwa_client_secret,
        aws_secret_key=aws_secret_key,
        aws_access_key=aws_access_key,
        role_arn=role_arn,
    )).credentials)
    x = client._auth_code_request_body('foo')
    assert x.get('grant_type') == 'authorization_code'

    try:
        client.authorize_auth_code('foo')
    except AuthorizationError as e:
        assert isinstance(e, AuthorizationError)

    try:
        client._request('https://jsonplaceholder.typicode.com/posts/1', {}, {})
    except AuthorizationError as e:
        assert isinstance(e, AuthorizationError)
