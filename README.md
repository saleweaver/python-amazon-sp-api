# PYTHON-AMAZON-SP-API

![CodeQL](https://github.com/saleweaver/python-amazon-sp-api/workflows/CodeQL/badge.svg)
![Tests](https://codebuild.eu-central-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiUXZBQ29Jd3NaNE45elZGRmdveVZMa0JCank4OGY4dnBMNDA3WGpsZXdpRXRTRHBKK1BvYmtneG00My8yYkdjdXc2S2VOeFBYcGN0VmxmVnhvZVIxZCtNPSIsIml2UGFyYW1ldGVyU3BlYyI6ImlnQUxNNlFZOVNWd0lRRlUiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=master)

## Amazon Selling-Partner API

A wrapper to access **Amazon's Selling Partner API** with an easy-to-use interface.


### Q & A

If you have questions, please ask them in GitHub discussions 

[![discussions](https://img.shields.io/badge/github-discussions-brightgreen?style=for-the-badge&logo=github)](https://github.com/saleweaver/python-amazon-sp-api/discussions)

or

[![join on slack](https://img.shields.io/badge/slack-join%20on%20slack-orange?style=for-the-badge&logo=slack)](https://join.slack.com/t/sellingpartnerapi/shared_invite/zt-zovn6tch-810j9dBPQtJsvw7lEXSuaQ)

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
from sp_api.base import SellingApiException
from sp_api.base.reportTypes import ReportType
from datetime import datetime, timedelta

# orders API
try:
    res = Orders().get_orders(CreatedAfter=(datetime.utcnow() - timedelta(days=7)).isoformat())
    print(res.payload)  # json data
except SellingApiException as ex:
    print(ex)


# report request     
createReportResponse = Reports().create_report(reportType=ReportType.GET_MERCHANT_LISTINGS_ALL_DATA)

# submit feed
# feeds can be submitted like explained in Amazon's docs, or simply by calling submit_feed

Feeds().submit_feed(self, <feed_type>, <file_or_bytes_io>, content_type='text/tsv', **kwargs)

# PII Data

Orders(restricted_data_token='<token>').get_orders(CreatedAfter=(datetime.utcnow() - timedelta(days=7)).isoformat())

# or use the shortcut
orders = Orders().get_orders(
    RestrictedResources=['buyerInfo', 'shippingAddress'],
    LastUpdatedAfter=(datetime.utcnow() - timedelta(days=1)).isoformat()
)
```

---

### Documentation

Documentation is available [here](https://sp-api-docs.saleweaver.com/?utm_source=github&utm_medium=repo&utm_term=text)

[![Documentation Status](https://img.shields.io/readthedocs/python-amazon-sp-api?style=for-the-badge)](https://sp-api-docs.saleweaver.com/?utm_source=github&utm_medium=repo&utm_term=badge)


### DISCLAIMER

We are not affiliated with Amazon


### LICENSE

![License](https://img.shields.io/github/license/saleweaver/python-amazon-sp-api?style=for-the-badge)


---
[![Quality gate](https://sonarcloud.io/api/project_badges/quality_gate?project=saleweaver_python-amazon-sp-api)](https://sonarcloud.io/summary/new_code?id=saleweaver_python-amazon-sp-api)

[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=saleweaver_python-amazon-sp-api&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=saleweaver_python-amazon-sp-api)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=saleweaver_python-amazon-sp-api&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=saleweaver_python-amazon-sp-api)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=saleweaver_python-amazon-sp-api&metric=coverage)](https://sonarcloud.io/summary/new_code?id=saleweaver_python-amazon-sp-api)


[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=saleweaver_python-amazon-sp-api&metric=bugs)](https://sonarcloud.io/summary/new_code?id=saleweaver_python-amazon-sp-api)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=saleweaver_python-amazon-sp-api&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=saleweaver_python-amazon-sp-api)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=saleweaver_python-amazon-sp-api&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=saleweaver_python-amazon-sp-api)

[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=saleweaver_python-amazon-sp-api&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=saleweaver_python-amazon-sp-api)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=saleweaver_python-amazon-sp-api&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=saleweaver_python-amazon-sp-api)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=saleweaver_python-amazon-sp-api&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=saleweaver_python-amazon-sp-api)
