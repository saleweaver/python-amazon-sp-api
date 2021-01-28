# PYTHON-AMAZON-SP-API


![CodeQL](https://github.com/saleweaver/python-amazon-sp-api/workflows/CodeQL/badge.svg)

### Amazon Selling-Partner API

Contributions very welcome!

---

### Installation

```
pip install python-amazon-sp-api
```

---
### Usage

```
# orders API
try:
    res = Orders().get_orders(CreatedAfter=(datetime.utcnow() - timedelta(days=7)).isoformat())
    print(res.payload)  # json data
except SellingApiException as ex:
    print(ex)


# report request     
createReportResponse = Reports().create_report(reportType='GET_FLAT_FILE_OPEN_LISTINGS_DATA')

# submit feed
# feeds can be submitted like explained in Amazon's docs, or simply by calling submit_feed

Feeds().submit_feed(self, <feed_type>, <file_or_bytes_io>, content_type='text/tsv', **kwargs)
```
---

### Credential configuration

You can set the required credentials via a config file, or with environment variables.
An example config file is provided in this repository, it supports multiple accounts.
The programm looks for a file called [credentials.yml](https://github.com/saleweaver/python-amazon-sp-api/blob/master/credentials.yml)

The config is parsed by [confused](https://confuse.readthedocs.io/en/latest/usage.html#search-paths), see their docs for more in depth information. 
Search paths are:

- macOS: ~/.config/python-sp-api
- Other Unix: ~/.config/python-sp-api
- Windows: %APPDATA%\python-sp-api where the APPDATA environment variable falls back to %HOME%\AppData\Roaming if undefined

```
version: '1.0'

default:
  refresh_token: ''
  lwa_app_id: ''
  lwa_client_secret: ''
  aws_secret_key: ''
  aws_access_key: ''
  role_arn: ''

another_account:
  refresh_token: ''
  lwa_app_id: ''
  lwa_client_secret: ''
  aws_secret_key: ''
  aws_access_key: ''
  role_arn: ''

```

If no account is passed to the client, default will be used.

```
# use default
Orders().get_orders(CreatedAfter=(datetime.utcnow() - timedelta(days=7)).isoformat())
```
```
# use 'another_account'
Orders(account='another_account').get_orders(CreatedAfter=(datetime.utcnow() - timedelta(days=7)).isoformat())
```

----

#### If you prefer to set environment variables, the following have to be set:

| ENVIRONMENT VARIABLE  | DESCRIPTION | 
|---|---|
| SP_API_REFRESH_TOKEN  | The refresh token used obtained via authorization (can be passed to the client instead)  |
| LWA_APP_ID | Your login with amazon app id |
| LWA_CLIENT_SECRET | Your login with amazon client secret |
| SP_API_SECRET_KEY | AWS USER SECRET KEY |
| SP_API_ACCESS_KEY | AWS USER ACCESS KEY |
| SP_API_ROLE_ARN | The role's arn (needs permission to "Assume Role" STS) |

You can (but don't have to) suffix each of these variables with `_<account>` if you want to set multiple accounts via env variables.  

```
# use default, with or without suffix
Orders().get_orders(CreatedAfter=(datetime.utcnow() - timedelta(days=7)).isoformat())
```
```
# use 'ANOTHER_ACCOUNT', e.g. SP_API_REFRESH_TOKEN_ANOTHER_ACCOUNT
Orders(account='ANOTHER_ACCOUNT').get_orders(CreatedAfter=(datetime.utcnow() - timedelta(days=7)).isoformat())
```

#### Credentials by params:

Pass a dict like below to the client:

```
credentials=dict(
        refresh_token='<refresh_token>',
        lwa_app_id='<lwa_app_id>',
        lwa_client_secret='<lwa_client_secret>',
        aws_secret_key='<aws_secret_access_key>',
        aws_access_key='<aws_access_key_id>',
        role_arn='<role_arn>',
    )
    
Orders(credentials=credentials).get_orders(CreatedAfter=(datetime.utcnow() - timedelta(days=7)).isoformat())
```

The refresh token can be passed directly to the client, too. You don't need to pass the whole credentials if all that changes is the refresh token. 

Credentials are looked up in the following order:
1. Credential dict
2. Env variables
3. Config File

---
### DISCLAIMER

We are not affiliated with Amazon
