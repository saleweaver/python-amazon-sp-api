From Code
=========


You can override/set credentials from code by passing a ``dict`` to the client.

If you pass a value in credentials, other credentials from env variables or from a config file will be ignored.

Required fields:

..  code-block:: python


    credentials=dict(
            refresh_token='<refresh_token>',
            lwa_app_id='<lwa_app_id>',
            lwa_client_secret='<lwa_client_secret>',
            aws_secret_key='<aws_secret_access_key>',
            aws_access_key='<aws_access_key_id>',
            role_arn='<role_arn>',
        )



*****
Usage
*****

..  code-block:: python

    Orders(credentials=credentials).get_orders(CreatedAfter=(datetime.utcnow() - timedelta(days=7)).isoformat())

