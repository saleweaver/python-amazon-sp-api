import os
from unittest import mock

from sp_api.base.credential_provider import FromCachedSecretsCredentialProvider


REFRESH_TOKEN = '<refresh_token>'
LWA_APP_ID = '<lwa_app_id>'
LWA_CLIENT_SECRET = '<lwa_client_secret>'
AWS_SECRET_KEY = '<aws_secret_access_key>'
AWS_ACCESS_KEY = '<aws_access_key_id>'
ROLE_ARN = '<role_arn>'


def test_from_cached_secrets_cp_without_secret_id_set():
    with mock.patch.dict(os.environ, {"SP_API_AWS_SECRET_ID": ""}):
        cp = FromCachedSecretsCredentialProvider()
        cp.load_credentials()

    assert cp.credentials is None


def test_from_cached_secrets_cp_without_cache_available():
    with mock.patch.dict(os.environ, {"SP_API_AWS_SECRET_ID": "test"}), \
            mock.patch.object(FromCachedSecretsCredentialProvider, "_get_secret_cache", return_value=None):
        cp = FromCachedSecretsCredentialProvider()
        cp.load_credentials()

    assert cp.credentials is None


def test_from_cached_secrets_cp_with_cache_available():
    secret_content = {
        "SP_API_REFRESH_TOKEN": REFRESH_TOKEN,
        "LWA_APP_ID": LWA_APP_ID,
        "LWA_CLIENT_SECRET": LWA_CLIENT_SECRET,
        "SP_API_ACCESS_KEY": AWS_ACCESS_KEY,
        "SP_API_SECRET_KEY": AWS_SECRET_KEY,
        "SP_API_ROLE_ARN": ROLE_ARN,
    }

    with mock.patch.dict(os.environ, {"SP_API_AWS_SECRET_ID": "test"}), \
            mock.patch.object(FromCachedSecretsCredentialProvider, "get_secret_content", return_value=secret_content):
        cp = FromCachedSecretsCredentialProvider()
        cp.load_credentials()

    assert cp.credentials == {
        "refresh_token": REFRESH_TOKEN,
        "lwa_app_id": LWA_APP_ID,
        "lwa_client_secret": LWA_CLIENT_SECRET,
        "aws_access_key": AWS_ACCESS_KEY,
        "aws_secret_key": AWS_SECRET_KEY,
        "role_arn": ROLE_ARN,
    }
