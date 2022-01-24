from __version__ import __version__ as version


class BaseClient:
    scheme = 'https://'
    method = 'GET'
    content_type = 'application/x-www-form-urlencoded;charset=UTF-8'
    user_agent = f'python-sp-api-{version}'
