Load All Pages Decorator
========================

..  automethod:: sp_api.util.load_all_pages

The example below will load all pages, transforming the decorated function to a generator.
The generator yields a page at a time.

Some examples:

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


.. code-block:: python

    @throttle_retry()
    @load_all_pages()
    def get_financial_events(**kwargs):
        return Finances().list_financial_events(**kwargs)

    for page in get_financial_events(PostedAfter='2021-05-10', PostedBefore='2021-05-11', MaxResultsPerPage=100):
        for event in page.payload.get('FinancialEvents').get('ShipmentEventList'):
            print(event)


.. warning::

    Amazon's endpoints don't follow naming conventions within the API. The parameter `NextToken` sometimes is called `next_token`, or differently.
    @load_all_pages accepts `next_token_param` as a parameter:

    .. code-block:: python

        @load_all_pages(next_token_param='next_token')

    Now it will look for a key named `next_token` in payload, instead of `NextToken`


