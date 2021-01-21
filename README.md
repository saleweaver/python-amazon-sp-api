# PYTHON-AMAZON-SP-API


![CodeQL](https://github.com/saleweaver/python-amazon-sp-api/workflows/CodeQL/badge.svg)

### Amazon Selling-Partner API

Early development status, contributions very welcome!

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

### Environment variables needed

| ENVIRONMENT VARIABLE  | DESCRIPTION | 
|---|---|
| SP_API_REFRESH_TOKEN  | The refresh token used obtained via authorization (can be passed to the client instead)  |
| LWA_APP_ID | Your login with amazon app id |
| LWA_CLIENT_SECRET | Your login with amazon client secret |
| SP_API_SECRET_KEY | AWS USER SECRET KEY |
| SP_API_ACCESS_KEY | AWS USER ACCESS KEY |
| SP_API_ROLE_ARN | The role's arn (needs permission to "Assume Role" STS) |
| SP_AWS_REGION | Defaults to 'us-east-1'. You can set it to a different region. |

---
### DISCLAIMER

We are not affiliated with Amazon
