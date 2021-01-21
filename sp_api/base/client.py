import json
import os
import re
from datetime import datetime
from pprint import pprint

import boto3
from cachetools import TTLCache
from requests import request

from sp_api.auth import AccessTokenClient, AccessTokenResponse
from .base_client import BaseClient
from .marketplaces import Marketplaces
from sp_api.base import AWSSigV4

role_cache = TTLCache(maxsize=10, ttl=3600)
client = boto3.client('sts',
                      aws_access_key_id=os.environ.get('SP_API_ACCESS_KEY'),
                      aws_secret_access_key=os.environ.get('SP_API_SECRET_KEY')
                      )


class SellingApiException(BaseException):
    pass


class Client(BaseClient):
    def __init__(self,
                 marketplace: Marketplaces,
                 refresh_token=None):
        self.endpoint = marketplace.endpoint
        self.marketplace_id = marketplace.marketplace_id
        self._auth = AccessTokenClient(refresh_token)

    @staticmethod
    def set_role():
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
            'content-type': 'application/json'
        }

    @property
    def auth(self) -> AccessTokenResponse:
        return self._auth.get_auth()

    @property
    def grantless_auth(self) -> AccessTokenResponse:
        return self._auth.get_grantless_auth()

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
                        region=os.environ.get('SP_AWS_REGION', 'us-east-1'),
                        aws_session_token=role.get('SessionToken')
                        )

    def _request(self, path: str, *, data: dict = None, params: dict = None, headers=None, add_marketplace=True):

        if params is None:
            params = {}
        if data is None:
            data = {}

        self.method = params.pop('method', data.pop('method', 'GET'))

        if self.method == 'POST':
            if add_marketplace and (not data.get('marketplaceIds', None) and not data.get('MarketplaceIds', None)):
                data.update({'marketplaceIds': [self.marketplace_id], 'MarketplaceIds': [self.marketplace_id]})
            data = json.dumps(data)
        else:
            if add_marketplace and ('MarketplaceIds' not in data and 'marketplaceIds' not in data):
                params.update({'MarketplaceId': self.marketplace_id, 'MarketplaceIds': self.marketplace_id,
                             'marketplace_ids': self.marketplace_id})

        res = request(self.method, self.endpoint + path, params=params, data=data, headers=headers or self.headers,
                      auth=self._sign_request())

        if e := res.json().get('errors', None):
            raise SellingApiException(e)
        return res

    def _request_grantless_operation(self, path: str, *, data: dict = None, params: dict = None):
        headers = {
            'host': self.endpoint[8:],
            'user-agent': self.user_agent,
            'x-amz-access-token': self.grantless_auth.access_token,
            'x-amz-date': datetime.utcnow().strftime('%Y%m%dT%H%M%SZ'),
            'content-type': 'application/json'
        }

        return self._request(path, data=data, params=params, headers=headers)
