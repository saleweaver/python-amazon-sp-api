import json
import os
import confuse
import boto3
from botocore.exceptions import ClientError
from cachetools import Cache


class MissingCredentials(Exception):
    """
    Credentials are missing, see the error output to find possible causes
    """
    pass


class CredentialProvider:
    credentials = None
    cache = Cache(maxsize=10)

    def __init__(self, account='default', credentials=None):
        self.account = account
        self.read_credentials = [
            self.from_env,
            self.from_secrets,
            self.read_config
        ]
        if credentials:
            self.credentials = self.Config(**credentials)
            missing = self.credentials.check_config()
            if len(missing):
                raise MissingCredentials(f'The following configuration parameters are missing: {missing}')
        else:
            self.load_credentials()

    def load_credentials(self):
        for read_method in self.read_credentials:
            if read_method():
                return True

    def from_secrets(self):
        if not os.environ.get('SP_API_AWS_SECRET_ID', None):
            return
        try:
            client = boto3.client('secretsmanager')
            response = client.get_secret_value(
                SecretId=os.environ.get('SP_API_AWS_SECRET_ID')
            )
            secret = json.loads(response.get('SecretString'))
            account_data = dict(
                refresh_token=secret.get('SP_API_REFRESH_TOKEN'),
                lwa_app_id=secret.get('LWA_APP_ID'),
                lwa_client_secret=secret.get('LWA_CLIENT_SECRET'),
                aws_secret_key=secret.get('SP_API_SECRET_KEY'),
                aws_access_key=secret.get('SP_API_ACCESS_KEY'),
                role_arn=secret.get('SP_API_ROLE_ARN')
            )
            self.cache['account_data'] = json.dumps(account_data)
        except ClientError as client_error:
            return
        else:
            self.credentials = self.Config(**account_data)
            return len(self.credentials.check_config()) == 0

    def from_env(self):
        try:
            account_data = json.loads(self.cache['account_data'])
        except KeyError:
            account_data = dict(
                refresh_token=self._get_env('SP_API_REFRESH_TOKEN'),
                lwa_app_id=self._get_env('LWA_APP_ID'),
                lwa_client_secret=self._get_env('LWA_CLIENT_SECRET'),
                aws_secret_key=self._get_env('SP_API_SECRET_KEY'),
                aws_access_key=self._get_env('SP_API_ACCESS_KEY'),
                role_arn=self._get_env('SP_API_ROLE_ARN')
            )
        self.credentials = self.Config(**account_data)
        return len(self.credentials.check_config()) == 0

    def _get_env(self, key):
        return os.environ.get(f'{key}_{self.account}',
                              os.environ.get(key))

    def read_config(self):
        try:
            config = confuse.Configuration('python-sp-api')
            config_filename = os.path.join(config.config_dir(), 'credentials.yml')
            config.set_file(config_filename)
            account_data = config[self.account].get()
            self.credentials = self.Config(**account_data)
            missing = self.credentials.check_config()
            if len(missing):
                raise MissingCredentials(f'The following configuration parameters are missing: {missing}')
        except confuse.exceptions.NotFoundError:
            raise MissingCredentials(f'The account {self.account} was not setup in your configuration file.')
        except confuse.exceptions.ConfigReadError:
            raise MissingCredentials(
                f'Neither environment variables nor a config file were found. '
                f'Please set the correct variables, or use a config file (credentials.yml). '
                f'See https://confuse.readthedocs.io/en/latest/usage.html#search-paths for search paths.'
            )
        else:
            return True

    class Config:
        def __init__(self,
                     refresh_token,
                     lwa_app_id,
                     lwa_client_secret,
                     aws_access_key,
                     aws_secret_key,
                     role_arn
                     ):
            self.refresh_token = refresh_token
            self.lwa_app_id = lwa_app_id
            self.lwa_client_secret = lwa_client_secret
            self.aws_access_key = aws_access_key
            self.aws_secret_key = aws_secret_key
            self.role_arn = role_arn

        def check_config(self):
            errors = []
            for k, v in self.__dict__.items():
                if not v and k != 'refresh_token':
                    errors.append(k)
            return errors
