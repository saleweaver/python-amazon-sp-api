Personally identifiable information (PII)
=========================================

If your application has access to PII-Data, you can request a token with the `Token`_ client, then use the returned token to access protected resources.

.. _Token: https://sp-api-docs.saleweaver.com/endpoints/tokens/

.. code-block:: python

    token_res = Tokens().create_restricted_data_token(restrictedResources=[{
         "method": "GET",
         "path": "/orders/v0/orders",
         "dataElements": ["buyerInfo", "shippingAddress"]
        }
    ])
    orders = Orders(restricted_data_token=token_res.payload['restrictedDataToken']).get_orders(LastUpdatedAfter=(datetime.utcnow() - timedelta(days=7)).isoformat())

    # orders have buyerInfo and shippingAddress
    print(orders)

Starting with v0.9.0, you can also pass the `RestrictedResources` to the `Orders` calls:

.. code-block:: python

        orders = Orders().get_orders(
            RestrictedResources=['buyerInfo', 'shippingAddress'],
            LastUpdatedAfter=(datetime.utcnow() - timedelta(days=1)).isoformat()
        )

        order = Orders().get_order(
            'order-id',
            RestrictedResources=['buyerInfo', 'shippingAddress']
        )

        order_items = Orders().get_order_items(
            'order-id',
            RestrictedResources=['buyerInfo']
        )

