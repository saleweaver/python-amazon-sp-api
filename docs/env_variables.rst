Environment Variables
=====================


=====================    =============================================================================================================================================================================================
ENVIRONMENT VARIABLE     DESCRIPTION
=====================    =============================================================================================================================================================================================
SP_API_REFRESH_TOKEN     The refresh token used obtained via authorization (can be passed to the client instead)
LWA_APP_ID               Your login with amazon app id
LWA_CLIENT_SECRET        Your login with amazon client secret
SP_API_ACCESS_KEY        AWS USER ACCESS KEY
SP_API_SECRET_KEY        AWS USER SECRET KEY
SP_API_ROLE_ARN          The role's arn (needs permission to "Assume Role" STS)
SP_API_AWS_SECRET_ID     Secret id from AWS Secrets Manager, which includes the following keys: `SP_API_REFRESH_TOKEN`, `LWA_APP_ID`, `LWA_CLIENT_SECRET`, `SP_API_ACCESS_KEY`, `SP_API_SECRET_KEY`, `SP_API_ROLE_ARN`
=====================    =============================================================================================================================================================================================


To set environment variables under linux/mac, use

..  code-block:: bash

    export SP_API_REFRESH_TOKEN="<your token>"


You can (but don't have to) suffix each of these variables with `_<account>` if you want to set multiple accounts via env variables.

..  code-block:: bash

    export SP_API_REFRESH_TOKEN_ANOTHER_ACCOUNT="<your token>"


**************************
Usage with default account
**************************

..  code-block:: python

    Orders().get_orders(CreatedAfter=(datetime.utcnow() - timedelta(days=7)).isoformat())


**************************
Usage with another_account
**************************

You can use every account's name

..  code-block:: python

    Orders(account='ANOTHER_ACCOUNT').get_orders(CreatedAfter=(datetime.utcnow() - timedelta(days=7)).isoformat())


******************************
Usage with AWS Secrets Manager
******************************

The required credentials can be retrieved from a secret in AWS Secrets Manager, by setting the `SP_API_AWS_SECRET_ID`
environment variable.

If the `aws-secretsmanager-caching-python`_ library is installed, it will be used to temporarily cache the retrieved
secret contents, and reduce calls to AWS Secrets Manager.


****
Note
****

The refresh token can be passed directly to the client, too. You don't need to pass the whole credentials if all that changes is the refresh token.

..  code-block:: python

    Orders(account='ANOTHER_ACCOUNT', refresh_token='<refresh_token_for_this_request>').get_orders(CreatedAfter=(datetime.utcnow() - timedelta(days=7)).isoformat())


**********
References
**********

.. target-notes::

.. _`aws-secretsmanager-caching-python`: https://github.com/aws/aws-secretsmanager-caching-python
