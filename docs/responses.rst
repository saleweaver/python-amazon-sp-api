Responses
=========

All endpoints return `sp_api.base.ApiResponse` with the following signature. `payload` contains Amazon's response.

.. code-block:: python

    response = Orders().get_orders(CreatedAfter='TEST_CASE_200', MarketplaceIds=["ATVPDKIKX0DER"])

    print(response.payload) # original response data
    # Access one of `payload`s properties using `__getattr__`
    print(response.Orders) # Array of orders
    # Access one of `payload`s properties using `__call__`
    print(response('Orders')) # Array of orders
    # Shorthand for response.payload
    print(response()) # original response data

-----------------------------------------

..  autoclass:: sp_api.base.ApiResponse


