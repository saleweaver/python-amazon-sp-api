Config File
===========



An example config file is provided in this repository, it supports multiple accounts.
The programm looks for a file called `credentials.yml`_

The config is parsed by `confused`_, see their docs for more in depth information.
Search paths are:

..  code-block:: bash

    macOS: ~/.config/python-sp-api
    Other Unix: ~/.config/python-sp-api
    Windows: %APPDATA%\python-sp-api where the APPDATA environment variable falls back to %HOME%\AppData\Roaming if undefined

If you're only using one account, place it under default. You can pass the account's name to the client to use any other account used in the `credentials.yml`_ file.

.. note::
    Required fields are:

    - lwa_app_id
    - lwa_client_secret
    - aws_secret_key
    - aws_access_key

    If you don't set the refresh_token, you have to pass it to the client.

    .. code-block:: python

        Orders(refresh_token='...')

.. warning::
    If you have assigned the execute-api (STS) permissions to your AWS **user**, omit `role_arn`.

    If you have assigned the permission to a role, the `role_arn` parameter is required.

..  code-block:: yaml

    version: '1.0'

    default:
      refresh_token: ''
      lwa_app_id: ''
      lwa_client_secret: ''
      aws_secret_key: ''
      aws_access_key: ''
      role_arn: ''
    another_account:
      refresh_token: ''
      lwa_app_id: ''
      lwa_client_secret: ''
      aws_secret_key: ''
      aws_access_key: ''
      role_arn: ''


**************************
Usage with default account
**************************

..  code-block:: python

    Orders().get_orders(CreatedAfter=(datetime.utcnow() - timedelta(days=7)).isoformat())


**************************
Usage with another_account
**************************

You can use every account's name from the config file for account

..  code-block:: python

    Orders(account=another_account).get_orders(CreatedAfter=(datetime.utcnow() - timedelta(days=7)).isoformat())

.. note::

    The refresh token can be passed directly to the client, too. You don't need to pass the whole credentials if all that changes is the refresh token.

    ..  code-block:: python

        Orders(account='another_account', refresh_token='<refresh_token_for_this_request>').get_orders(CreatedAfter=(datetime.utcnow() - timedelta(days=7)).isoformat())


**********
References
**********

.. target-notes::

.. _`credentials.yml`: https://github.com/saleweaver/python-amazon-sp-api/blob/master/credentials.yml
.. _`confused`: https://confuse.readthedocs.io/en/latest/usage.html#search-paths


