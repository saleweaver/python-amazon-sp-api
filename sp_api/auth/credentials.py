import os


class Credentials:
    def __init__(self, refresh_token):
        self.client_id = os.environ.get('LWA_APP_ID')
        self.client_secret = os.environ.get('LWA_CLIENT_SECRET')
        self.refresh_token = refresh_token or os.environ.get('SP_API_REFRESH_TOKEN')
