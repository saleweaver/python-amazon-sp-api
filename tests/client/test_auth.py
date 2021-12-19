from sp_api.base import Credentials, CredentialProvider
from sp_api.base import AuthorizationError


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
