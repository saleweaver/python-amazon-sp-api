Load All Pages Decorator
========================

..  automethod:: sp_api.util.load_all_pages

The example below will load all pages, transforming the decorated function to a generator:

.. code-block:: python

    @load_all_pages()
    def get_orders(**kwargs):
        return Orders().get_orders(**kwargs)
