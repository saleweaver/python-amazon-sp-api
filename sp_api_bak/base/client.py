import os
from datetime import datetime

import boto3
from cachetools import TTLCache
from requests import request

from sp_api_bak import AccessTokenClient, AccessTokenResponse
from sp_api_bak import BaseClient, Marketplaces, AWSSigV4

role_cache = TTLCache(maxsize=10, ttl=3600)
client = boto3.client('sts',
                      aws_access_key_id=os.environ.get('SP_API_ACCESS_KEY'),
                      aws_secret_access_key=os.environ.get('SP_API_SECRET_KEY')
                      )


class Client(BaseClient):
    def __init__(self,
                 marketplace: Marketplaces,
                 refresh_token=None):
        self.endpoint = marketplace.endpoint
        self.marketplace_id = marketplace.marketplace_id
        self._auth = AccessTokenClient(refresh_token)
        self.set_role()

    @staticmethod
    def set_role():
        print(os.environ.get('SP_API_ROLE_ARN'))
        role = client.assume_role(
            RoleArn=os.environ.get('SP_API_ROLE_ARN'),
            RoleSessionName='guid'
        )
        role_cache['role'] = role
        return role

    @property
    def headers(self):
        return {
            'host': self.endpoint[8:],
            'user-agent': self.user_agent,
            'x-amz-access-token': self.auth.access_token,
            'x-amz-date': datetime.utcnow().strftime('%Y%m%dT%H%M%SZ'),

        }

    @property
    def auth(self) -> AccessTokenResponse:
        return self._auth.get_auth()

    @property
    def role(self):
        try:
            role = role_cache['role']
        except KeyError:
            role = self.set_role()
        return role.get('Credentials')

    def _sign_request(self):
        role = self.role
        return AWSSigV4('execute-api',
                        aws_access_key_id=role.get('AccessKeyId'),
                        aws_secret_access_key=role.get('SecretAccessKey'),
                        region='us-east-1',
                        aws_session_token=role.get('SessionToken')
                        )

    def request(self, path: str, *, data: dict = None, params: dict = None):
        if params is None:
            params = {}
        params.update({'MarketplaceIds': self.marketplace_id})
        self.method = params.pop('method', data.pop('method'))

        return request(self.method, self.endpoint + path, params=params, data=data, headers=self.headers,
                       auth=self._sign_request())
