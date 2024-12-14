class AccessTokenResponse:
    def __init__(self, **kwargs):
        self.access_token = kwargs.get("access_token")
        self.refresh_token = kwargs.get("refresh_token")
        self.expires_in = kwargs.get("expires_in")
        self.token_type = kwargs.get("token_type")
