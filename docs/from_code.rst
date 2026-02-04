From Code
=========


You can override/set credentials from code by passing a ``dict`` to the client.

If you pass a value in credentials, other credentials from env variables or from a config file will be ignored.

.. note::
    Required fields are:

    - lwa_app_id
    - lwa_client_secret

    If you don't set the refresh_token, you have to pass it to the client.

    .. code-block:: python

        Orders(refresh_token='...')


..  code-block:: python

    credentials=dict(
            refresh_token='<refresh_token>',
            lwa_app_id='<lwa_app_id>',
            lwa_client_secret='<lwa_client_secret>'
        )



*****
Usage
*****

..  code-block:: python

    from datetime import datetime, timedelta, timezone
    Orders(credentials=credentials).get_orders(CreatedAfter=(datetime.now(timezone.utc) - timedelta(days=7)).isoformat())
