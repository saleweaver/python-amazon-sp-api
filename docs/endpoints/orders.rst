Orders
======




..  toctree::
    :maxdepth: 1

    orders_v0
    orders_v2026_01_01




Restricted Data Token
=====================

To use a restricted data token to access PII data, you can pass the token obtained from the Token endpoint to the client:

..  code-block:: python

    Orders(restricted_data_token='......').get_orders(...)





