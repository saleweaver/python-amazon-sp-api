from sp_api.base.credential_provider import CredentialProvider


class BaseClient:
    scheme = 'https://'
    method = 'GET'
    content_type = 'application/x-www-form-urlencoded;charset=UTF-8'
    user_agent = 'python-sp-api'

    def __init__(self, account='default', credentials=None):
        try:
            from sp_api.base import __version__
            self.user_agent += f'-{__version__}'
        except:
            pass
        self.credentials = CredentialProvider(account, credentials).credentials
