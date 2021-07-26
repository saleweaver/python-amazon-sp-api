# PYTHON-AMAZON-SP-API

## Amazon Selling-Partner API

Fork from [Saleweaver](https://github.com/saleweaver/python-amazon-sp-api)

A wrapper to access **Amazon's Selling Partner API** with an easy-to-use interface.


### Q & A

If you have questions, please ask them in Saleweaver GitHub discussions 

[![discussions](https://img.shields.io/badge/github-discussions-brightgreen?style=for-the-badge&logo=github)](https://github.com/saleweaver/python-amazon-sp-api/discussions)


---

### Installation
```
pip install git+https://github.com/onesdata/python-amazon-sp-api
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
```
---

### Documentation

Documentation is available [here](https://python-amazon-sp-api.readthedocs.io/en/latest/index.html)

[![Documentation Status](https://img.shields.io/readthedocs/python-amazon-sp-api?style=for-the-badge)](https://python-amazon-sp-api.readthedocs.io/en/latest/?badge=latest)

### DISCLAIMER

* This is a fork from [Saleweaver](https://github.com/saleweaver/python-amazon-sp-api) 
* We are not affiliated with Amazon


### LICENSE

![License](https://img.shields.io/github/license/saleweaver/python-amazon-sp-api?style=for-the-badge)


---
![Maintainability](https://img.shields.io/codeclimate/maintainability/saleweaver/python-amazon-sp-api?style=for-the-badge)
![Tech](https://img.shields.io/codeclimate/tech-debt/saleweaver/python-amazon-sp-api?style=for-the-badge)
