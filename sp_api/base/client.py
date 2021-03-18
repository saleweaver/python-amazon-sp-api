import json
from datetime import datetime
import logging

import boto3
from cachetools import TTLCache
from requests import request

from sp_api.auth import AccessTokenClient, AccessTokenResponse
from .ApiResponse import ApiResponse
from .base_client import BaseClient
from .exceptions import get_exception_for_code, SellingApiBadRequestException
from .marketplaces import Marketplaces
from sp_api.base import AWSSigV4

log = logging.getLogger(__name__)

role_cache = TTLCache(maxsize=10, ttl=3600)


class Client(BaseClient):
    boto3_client = None

    def __init__(
            self,
            marketplace: Marketplaces = Marketplaces.US,
            *,
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

    def _request(self, path: str, *, data: dict = None, params: dict = None, headers=None,
                 add_marketplace=True) -> ApiResponse:
        if params is None:
            params = {}
        if data is None:
            data = {}

        self.method = params.pop('method', data.pop('method', 'GET'))

        if add_marketplace:
            self._add_marketplaces(data if self.method in ('POST', 'PUT') else params)

        res = request(self.method, self.endpoint + path, params=params,
                      data=json.dumps(data) if data and self.method in ('POST', 'PUT') else None, headers=headers or self.headers,
                      auth=self._sign_request())

        return self._check_response(res)

    @staticmethod
    def _check_response(res) -> ApiResponse:
        error = res.json().get('errors', None)
        if error:
            exception = get_exception_for_code(res.status_code)
            raise exception(error)
        return ApiResponse(**res.json(), headers=res.headers)

    def _add_marketplaces(self, data):
        POST = ['marketplaceIds', 'MarketplaceIds']
        GET = ['MarketplaceId', 'MarketplaceIds', 'marketplace_ids', 'marketplaceIds']

        if self.method == 'POST':
            if any(x in data.keys() for x in POST):
                return
            return data.update({k: self.marketplace_id if not k.endswith('s') else [self.marketplace_id] for k in POST})
        if any(x in data.keys() for x in GET):
            return
        return data.update({k: self.marketplace_id if not k.endswith('s') else [self.marketplace_id] for k in GET})

    def _request_grantless_operation(self, path: str, *, data: dict = None, params: dict = None):
        headers = {
            'host': self.endpoint[8:],
            'user-agent': self.user_agent,
            'x-amz-access-token': self.grantless_auth.access_token,
            'x-amz-date': datetime.utcnow().strftime('%Y%m%dT%H%M%SZ'),
            'content-type': 'application/json'
        }

        return self._request(path, data=data, params=params, headers=headers)
