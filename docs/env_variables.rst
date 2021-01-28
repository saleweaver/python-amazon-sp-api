Environment Variables
=====================


=====================    =========================================================================================================
ENVIRONMENT VARIABLE     DESCRIPTION
=====================    =========================================================================================================
SP_API_REFRESH_TOKEN     The refresh token used obtained via authorization (can be passed to the client instead)
LWA_APP_ID               Your login with amazon app id
LWA_CLIENT_SECRET        Your login with amazon client secret
SP_API_ACCESS_KEY        AWS USER ACCESS KEY
SP_API_SECRET_KEY        AWS USER SECRET KEY
SP_API_ROLE_ARN          The role's arn (needs permission to "Assume Role" STS)
=====================    =========================================================================================================


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

**************************
Note
**************************

The refresh token can be passed directly to the client, too. You don't need to pass the whole credentials if all that changes is the refresh token.

..  code-block:: python

    Orders(account='ANOTHER_ACCOUNT', refresh_token='<refresh_token_for_this_request>').get_orders(CreatedAfter=(datetime.utcnow() - timedelta(days=7)).isoformat())

