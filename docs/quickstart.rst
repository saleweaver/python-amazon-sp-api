Quickstart
==========

After setting up your credentials, you can make your first SP-API calls in a few lines.

This page focuses on **practical workflows** rather than listing every parameter. For full reference, see:

- :doc:`endpoints`
- :doc:`responses`
- :doc:`utils`

Prerequisites
-------------

- Python 3.8+
- An SP-API application in Seller Central
- A valid refresh token and IAM role / user configured according to Amazon's guide

Install the package:

.. code-block:: bash

   pip install python-amazon-sp-api

If you want to use AWS Secrets Manager for credential storage:

.. code-block:: bash

   pip install "python-amazon-sp-api[aws]"
   pip install "python-amazon-sp-api[aws-caching]"

Credentials
-----------

The library can read credentials in three ways (in this order):

1. From **arguments** passed in code
2. From **environment variables**
3. From a **config file**

See :doc:`credentials` for the full list of supported fields.

Example – credentials from code:

.. code-block:: python

   credentials = dict(
       refresh_token='your_refresh_token',
       lwa_app_id='your_lwa_app_id',
       lwa_client_secret='your_lwa_client_secret',
       aws_access_key='your_aws_access_key',
       aws_secret_key='your_aws_secret_key',
       role_arn='your_role_arn',
   )

   from sp_api.api import Orders
   orders = Orders(credentials=credentials)

Default marketplace
-------------------

By default, the library uses the US marketplace.

You can change this:

* Per client, by passing a :class:`sp_api.base.Marketplaces` value
* Globally, via the ``SP_API_DEFAULT_MARKETPLACE`` environment variable

.. code-block:: bash

   export SP_API_DEFAULT_MARKETPLACE=DE

.. code-block:: python

   from sp_api.base import Marketplaces
   from datetime import datetime, timedelta, timezone
   from sp_api.api import Orders

   # Explicit marketplace
   orders = Orders(marketplace=Marketplaces.DE)

   # Or rely on SP_API_DEFAULT_MARKETPLACE:
   orders = Orders()

All endpoint clients share the same signature:

.. code-block:: python

   SomeClient(
       marketplace=Marketplaces.US,
       *,
       refresh_token=None,
       account='default',
       credentials=None,
       restricted_data_token=None,
   )

First request: get a single order
---------------------------------

.. code-block:: python

   from sp_api.base import Marketplaces
   from sp_api.api import Orders

   client = Orders(marketplace=Marketplaces.DE)

   order = client.get_order('YOUR-ORDER-ID')

   # `order` is an ApiResponse
   print(order.payload)   # raw response dict
   print(order.Orders)    # helper to access payload['Orders'] when present

Fetching many orders with pagination
------------------------------------

SP-API uses ``NextToken`` for pagination. This library ships a utility decorator
that turns endpoint calls into a **generator** that automatically follows all pages.

.. code-block:: python

   from datetime import datetime, timedelta, timezone

   from sp_api.api import Orders
   from sp_api.util import throttle_retry, load_all_pages

   @throttle_retry()      # retry on throttling
   @load_all_pages()      # follow NextToken automatically
   def iter_orders(**kwargs):
       return Orders().get_orders(**kwargs)

   for page in iter_orders(
       LastUpdatedAfter=(datetime.now(timezone.utc) - timedelta(days=7)).isoformat()
   ):
       for order in page.payload.get('Orders', []):
           print(order['AmazonOrderId'], order['OrderStatus'])

Notes:

* ``@load_all_pages`` yields **one ApiResponse per page**.
* Some endpoints use a different token name (for example ``next_token``). You can pass
  ``next_token_param`` to the decorator:

  .. code-block:: python

     @load_all_pages(next_token_param='next_token')
     def iter_something(**kwargs):
         ...

Handling throttling & retries
-----------------------------

Amazon enforces strict rate limits per operation. When you hit the limit, SP-API
returns HTTP 429 and this library raises
:class:`sp_api.base.SellingApiRequestThrottledException`.

The :mod:`sp_api.util` module provides retry decorators:

* :func:`sp_api.util.retry`
* :func:`sp_api.util.sp_retry`
* :func:`sp_api.util.throttle_retry`

Example: retry a single call:

.. code-block:: python

   from sp_api.api import Orders
   from sp_api.util import throttle_retry

   @throttle_retry(tries=10, delay=5, rate=1.3)
   def get_orders(**kwargs):
       return Orders().get_orders(**kwargs)

   res = get_orders(CreatedAfter='2024-01-01T00:00:00Z')

Combining retries and auto-pagination:

.. code-block:: python

   from sp_api.util import sp_retry, load_all_pages

   @sp_retry(tries=10, delay=10, rate=1.2)
   @load_all_pages()
   def get_all_orders(**kwargs):
       return Orders().get_orders(**kwargs)

   for page in get_all_orders(CreatedAfter='2024-01-01T00:00:00Z'):
       ...

Creating reports
----------------

Creating a report with :class:`sp_api.api.ReportsV2`:

.. code-block:: python

   from datetime import datetime, timedelta, timezone

   from sp_api.api import ReportsV2
   from sp_api.base.reportTypes import ReportType

   reports = ReportsV2()

   res = reports.create_report(
       reportType=ReportType.GET_FLAT_FILE_ALL_ORDERS_DATA_BY_LAST_UPDATE_GENERAL,
       dataStartTime=(datetime.now(timezone.utc) - timedelta(days=7)).isoformat(),
       dataEndTime=(datetime.now(timezone.utc) - timedelta(days=1)).isoformat(),
   )

   print(res.payload)  # contains the report id

Submitting feeds
----------------

.. code-block:: python

   from sp_api.api import Feeds

   with open("my_feed_file.tsv", "rb") as f:
       Feeds().submit_feed(
           feed_type="POST_PRODUCT_DATA",   # use your feed type
           file=f,
           content_type="text/tsv",
       )

Working with PII (Restricted Data Token)
----------------------------------------

Some endpoints require access to **PII** (personally identifiable information), e.g.:

* Order shipping address
* Buyer info

For those, you must:

1. Use Amazon's Tokens API to request a **Restricted Data Token** (RDT)
2. Pass the token to the client via ``restricted_data_token``

.. code-block:: python

   from sp_api.api import Orders

   rdt = "YOUR_RESTRICTED_DATA_TOKEN"

   orders = Orders(restricted_data_token=rdt)

   res = orders.get_orders(
       LastUpdatedAfter="2024-01-01T00:00:00Z",
       # and any RestrictedResources required by Amazon
   )

Next steps
----------

From here, you probably want to look at:

* :doc:`responses` – details on :class:`sp_api.base.ApiResponse`
* :doc:`endpoints` – per-endpoint documentation
* :doc:`utils` – retry / pagination / key maker helpers
* :doc:`examples` – more complete examples and flows
