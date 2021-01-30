Client Usage
============






All endpoint's clients have the following signature and default values:



.. code-block:: python

    SomeClient(
        marketplace=Marketplaces.US, *,
        refresh_token=None,
        account='default',
        credentials=None
    )
