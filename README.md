# PYTHON-AMAZON-SP-API
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


---
### DISCLAIMER

We are not affiliated with Amazon
