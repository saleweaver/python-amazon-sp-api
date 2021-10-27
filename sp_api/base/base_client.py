from sp_api.base.credential_provider import CredentialProvider


class BaseClient:
    scheme = 'https://'
    method = 'GET'
    content_type = 'application/x-www-form-urlencoded;charset=UTF-8'
    user_agent = 'python-sp-api'

    def __init__(self, account='default', credentials=None):
        self.user_agent += '0.6.5'
        self.credentials = CredentialProvider(account, credentials).credentials
