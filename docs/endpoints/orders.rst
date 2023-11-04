Orders
======



.. button::
   :text: View API documentation
   :link: https://sp-api-docs.saleweaver.com/redoc/ordersV0.html



..  autoclass:: sp_api.api.Orders



Restricted Data Token
=====================

To use a restricted data token to access PII data, you can pass the token obtained from the Token endpoint to the client:

..  code-block:: python

    Orders(restricted_data_token='......').get_orders(...)





