# PYTHON-AMAZON-SP-API

![CodeQL](https://github.com/saleweaver/python-amazon-sp-api/workflows/CodeQL/badge.svg)
![Tests](https://codebuild.eu-central-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiUXZBQ29Jd3NaNE45elZGRmdveVZMa0JCank4OGY4dnBMNDA3WGpsZXdpRXRTRHBKK1BvYmtneG00My8yYkdjdXc2S2VOeFBYcGN0VmxmVnhvZVIxZCtNPSIsIml2UGFyYW1ldGVyU3BlYyI6ImlnQUxNNlFZOVNWd0lRRlUiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=master)
![Coverage](https://img.shields.io/codeclimate/coverage/saleweaver/python-amazon-sp-api)

## Amazon Selling-Partner API

A wrapper to access **Amazon's Selling Partner API** with an easy-to-use interface.


### Q & A

If you have questions, please ask them in github discussions 

[![discussions](https://img.shields.io/badge/github-discussions-brightgreen?style=for-the-badge&logo=github)](https://github.com/saleweaver/python-amazon-sp-api/discussions)


---

### Installation
[![Badge](https://img.shields.io/pypi/v/python-amazon-sp-api?style=for-the-badge)](https://pypi.org/project/python-amazon-sp-api/)
```
pip install python-amazon-sp-api
```

---
### Usage

```
from sp_api.api import Orders
from sp_api.api import Reports
from sp_api.api import Feeds
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

[![Documentation Status](https://img.shields.io/readthedocs/python-amazon-sp-api?style=for-the-badge)](https://python-amazon-sp-api.readthedocs.io/en/latest/?badge=latest)

### DISCLAIMER

We are not affiliated with Amazon


### LICENSE

![License](https://img.shields.io/github/license/saleweaver/python-amazon-sp-api?style=for-the-badge)


---
![Maintainability](https://img.shields.io/codeclimate/maintainability/saleweaver/python-amazon-sp-api?style=for-the-badge)
![Tech](https://img.shields.io/codeclimate/tech-debt/saleweaver/python-amazon-sp-api?style=for-the-badge)
