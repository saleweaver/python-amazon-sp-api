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


class SellingApiException(BaseException):
    pass


class Client(BaseClient):
    boto3_client = None

    def __init__(self,
                 marketplace: Marketplaces,
                 refresh_token=None,
                 account='default',
                 credentials=None
                 ):
        super().__init__(account, credentials)
        self.boto3_client = boto3.client(
            'sts',
            aws_access_key_id=self.credentials.aws_access_key,
            aws_secret_access_key=self.credentials.aws_secret_key
        )
        self.endpoint = marketplace.endpoint
        self.marketplace_id = marketplace.marketplace_id
        self.region = marketplace.region
        self._auth = AccessTokenClient(refresh_token=refresh_token, account=account, credentials=credentials)

    def set_role(self):
        role = self.boto3_client.assume_role(
            RoleArn=self.credentials.role_arn,
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
                        region=self.region,
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
            if add_marketplace and (
                    'MarketplaceIds' not in params and 'marketplaceIds' not in params and 'marketplace_ids' not in params and 'MarketplaceId' not in params):
                params.update({'MarketplaceId': self.marketplace_id, 'MarketplaceIds': self.marketplace_id,
                               'marketplace_ids': self.marketplace_id, 'marketplaceIds': self.marketplace_id})
        res = request(self.method, self.endpoint + path, params=params, data=data, headers=headers or self.headers,
                      auth=self._sign_request())

        e = res.json().get('errors', None)
        if e:
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
