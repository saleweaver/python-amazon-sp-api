from sp_api.api import Authorization


def test_get_auth_code():
    res = Authorization().get_authorization_code(mwsAuthToken='test', developerId='test', sellingPartnerId='test')
    assert res.payload['authorizationCode'] == 'ANDMxqpCmqWHJeyzdbMH'
