def test_access_token_client_success():
    from auth.access_token_client import AccessTokenClient
    from auth.credentials import Credentials
    res = AccessTokenClient().get_auth()
    print(res)
    assert hasattr(res, 'access_token')
    res = AccessTokenClient().get_auth()
    print(res)
    assert hasattr(res, 'access_token')


