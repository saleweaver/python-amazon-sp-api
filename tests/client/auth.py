
def test_auth():
    from sp_api.auth import AccessTokenClient

    AccessTokenClient().authorize_auth_code('foo')
