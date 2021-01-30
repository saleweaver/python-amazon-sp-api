# PYTHON-AMAZON-SP-API


![CodeQL](https://github.com/saleweaver/python-amazon-sp-api/workflows/CodeQL/badge.svg)
![Tests](https://codebuild.eu-central-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiUXZBQ29Jd3NaNE45elZGRmdveVZMa0JCank4OGY4dnBMNDA3WGpsZXdpRXRTRHBKK1BvYmtneG00My8yYkdjdXc2S2VOeFBYcGN0VmxmVnhvZVIxZCtNPSIsIml2UGFyYW1ldGVyU3BlYyI6ImlnQUxNNlFZOVNWd0lRRlUiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=master)


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

### Documentation

Documentation is available [here](https://python-amazon-sp-api.readthedocs.io/en/latest/index.html)

### DISCLAIMER

We are not affiliated with Amazon
