Quickstart
==========

.. button::
   :text: Visit Playground
   :link: https://sp-api-playground.saleweaver.com/?utm_source=documentation&utm_medium=docs&utm_term=quickstart


After setting up your credentials, you're ready to make the first call.
This quickstart uses credentials passed as a dict, if you've setup a config file or environment variables, this can be omitted.

.. code-block:: python

    credentials = dict(
        refresh_token='your_refresh_token',
        lwa_app_id='your_lwa_app_id',
        lwa_client_secret='your_lwa_client_secret',
        aws_access_key='your_aws_access_key',
        aws_secret_key='your_aws_secret_key'
    )

The default Marketplace this library uses is the US.
You can pass the marketplace when initiating a new client, or set another default as environment variable.
For example, to use the German Marketplace as the default, set `SP_API_DEFAULT_MARKETPLACE` as an environment variable:

.. code-block:: bash

    SP_API_DEFAULT_MARKETPLACE=DE

.. note::

    All endpoints have the following signature and default values:


    .. code-block:: python

        SomeClient(
            marketplace=Marketplaces.US, *,
            refresh_token=None,
            account='default',
            credentials=None,
            restricted_data_token=None
        )

Example Usage
-------------

Let's download a single order, then a list of orders.
First, create a client with your credentials and Marketplace:

.. note::

    You don't need to pass a marketplace if you want to request your default marketplace


.. note::

    You don't need to pass credentials if you've set them up as environment variables or in a config file


.. code-block:: python

    from sp_api.base import Marketplaces
    from sp_api.api import Orders

    order_client = Orders(credentials=credentials, marketplace=Marketplaces.DE)
    order = order_client.get_order('your-order-id')
    print(order) # `order` is an `ApiResponse`
    print(order.payload) # `payload` contains the original response


If you want to get a list of orders, you can make use of `load_all_pages`_, and optionally together with one of the `retry`_ decorators.
Below code will print all orders for your credentials, for the last 7 days:

.. _load_all_pages: https://sp-api-docs.saleweaver.com/utils/load_all_pages/
.. _retry: https://sp-api-docs.saleweaver.com/utils/retry/


.. code-block:: python

    from datetime import datetime, timedelta
    from sp_api.base import Marketplaces
    from sp_api.api import Orders
    from sp_api.util import throttle_retry, load_all_pages


    @throttle_retry()
    @load_all_pages()
    def load_all_orders(**kwargs):
        """
        a generator function to return all pages, obtained by NextToken
        """
        return Orders().get_orders(**kwargs)


    for page in load_all_orders(LastUpdatedAfter=(datetime.utcnow() - timedelta(days=7)).isoformat()):
        for order in page.payload.get('Orders'):
            print(order)


.. warning::

    Amazon's endpoints don't follow naming conventions within the API. The parameter `NextToken` sometimes is called `next_token`, or differently.
    @load_all_pages accepts `next_token_param` as a parameter:

    .. code-block:: python

        @load_all_pages(next_token_param='next_token')

    Now it will look for a key named `next_token` in payload, instead of `NextToken`


Creating a report is just as easy:

.. note::

    This time, `Reports` is using credentials from a config file (or environment variables), and the default marketplace

.. code-block:: python

    from datetime import datetime, timedelta
    from sp_api.api import ReportsV2
    from sp_api.base.reportTypes import ReportType, Marketplaces

    res = ReportsV2().create_report(
        reportType=ReportType.GET_FLAT_FILE_ALL_ORDERS_DATA_BY_LAST_UPDATE_GENERAL,
        # optionally, you can set a start and end time for your report
        dataStartTime=(datetime.utcnow() - timedelta(days=7)).isoformat()
        dataEndTime=(datetime.utcnow() - timedelta(days=1)).isoformat()
        )
    print(res)
    print(res.payload) # object containing a report id
