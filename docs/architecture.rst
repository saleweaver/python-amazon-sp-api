Architecture
============

This page explains how PYTHON-AMAZON-SP-API is structured so you know what the
library is doing under the hood and how to extend it safely.

High-level components
---------------------

The project is organised roughly as:

* ``sp_api.base`` – core building blocks (client, response wrapper, marketplaces, exceptions, credentials)
* ``sp_api.api`` – one client class per SP-API group (Orders, Reports, Feeds, DataKiosk, ...)
* ``sp_api.util`` – utilities for retries, throttling and pagination
* ``docs`` – Sphinx documentation

Most users only touch the classes in ``sp_api.api``, but everything ultimately
flows through :class:`sp_api.base.Client`.

Client lifecycle
----------------

All endpoint clients inherit from :class:`sp_api.base.client.Client`, which
itself extends :class:`sp_api.base.base_client.BaseClient`.

When you do:

.. code-block:: python

   from sp_api.api import Orders

   client = Orders()

the following happens internally:

1. Credentials are resolved via :class:`sp_api.base.credential_provider.CredentialProvider`
   (code → env vars → config file).
2. The marketplace is chosen, either from the ``marketplace`` argument or from
   the ``SP_API_DEFAULT_MARKETPLACE`` environment variable.
3. An :class:`sp_api.auth.AccessTokenClient` is created for the account.
4. The client prepares the base endpoint URL, marketplace id and region.
5. The **request method**, path, params and body are passed to ``Client._request``.

Request flow
------------

All concrete endpoint methods eventually call :meth:`sp_api.base.client.Client._request`.

Key steps:

* The HTTP method is taken from the ``method`` parameter (if present in ``params`` or ``data``)
  or defaults to ``GET``.
* ``_add_marketplaces`` injects marketplace parameters into the request if you did not
  explicitly set them. It handles both ``MarketplaceId`` and ``MarketplaceIds`` forms.
* Request headers include:

  * ``x-amz-access-token`` – from either the account's access token or a restricted data token
  * ``x-amz-date`` – current UTC timestamp
  * ``user-agent`` – a library user agent
  * ``host`` – derived from the marketplace endpoint

* The request is sent using :func:`requests.request`.

Response handling
-----------------

Responses are normal ``requests`` responses but wrapped into
:class:`sp_api.base.ApiResponse` via ``Client._check_response``.

* On success, the JSON body is parsed into the ``payload`` attribute.
* If the top-level JSON is a list, it is either wrapped into ``{'payload': list}``
  or the first item is used (depending on the operation).
* If the response contains an ``errors`` key, an appropriate
  :class:`sp_api.base.exceptions.SellingApiException` subclass is raised
  based on the HTTP status.

The :class:`sp_api.base.ApiResponse` object gives you:

* ``payload`` – the original JSON payload
* ``errors`` – if present
* ``headers`` – HTTP headers (useful for rate limits)
* ``nextToken`` / ``pagination`` – when applicable
* ``__call__`` – shorthand for ``payload``
* ``__getattr__`` – convenience accessor to payload keys

See :doc:`responses` for details.

Credentials and marketplaces
----------------------------

Credentials are injected by :class:`sp_api.base.credential_provider.CredentialProvider`.
You generally do not need to instantiate this manually – passing ``credentials=...`` or
setting env vars / config file is enough.

Marketplaces are defined in :mod:`sp_api.base.marketplaces` and expose:

* The SP-API endpoint URL
* The marketplaceId
* The region

Client classes accept a ``marketplace`` keyword which defaults to
``Marketplaces.US`` if no override is found, or to ``SP_API_DEFAULT_MARKETPLACE``
when that environment variable is set.

Grantless operations & RDT
--------------------------

Two special cases:

* **Grantless operations**: some SP-API operations do not require seller-level
  authorization but do require a **scope**. Endpoint clients specify a
  ``grantless_scope`` and internally call ``Client._request_grantless_operation``.
* **Restricted Data Token (RDT)**: when you pass ``restricted_data_token=...`` to a client,
  the token is used instead of the normal access token (see the Quickstart and PII docs).

Retry & pagination utilities
----------------------------

The :mod:`sp_api.util` module provides decorators that work with any endpoint
methods returning an :class:`sp_api.base.ApiResponse`:

* :func:`sp_api.util.load_all_pages` – transforms a function into a generator
  that automatically follows ``NextToken`` (or another token name you configure).
* :func:`sp_api.util.throttle_retry` – retries on throttling exceptions
  (HTTP 429 / :class:`sp_api.base.SellingApiRequestThrottledException`).
* :func:`sp_api.util.sp_retry` – more general retry decorator.

These utilities are intentionally decoupled: you can apply them to your own
wrappers around endpoint calls without changing the endpoint clients themselves.

Extending with new endpoints
----------------------------

All endpoint clients in :mod:`sp_api.api` follow the same internal pattern:

* A class deriving from :class:`sp_api.base.client.Client`
* One method per SP-API operation
* A decorator (``@sp_endpoint``) capturing the path template and HTTP method

To add support for a missing SP-API model, you can use the ``make_endpoint``
helper from the repository root:

.. code-block:: bash

   make_endpoint https://raw.githubusercontent.com/amzn/selling-partner-api-models/main/models/listings-restrictions-api-model/listingsRestrictions_2021-08-01.json

This will generate a new endpoint client file that you can adjust and, ideally,
contribute back via a pull request.

When to dive deeper
-------------------

You may want to look at the internals when:

* Implementing new endpoints or tweaking existing ones
* Integrating with non-standard authentication flows
* Debugging low-level issues (signature, region, marketplace routing)
* Adapting the base client to other REST APIs

For most use cases, staying at the :mod:`sp_api.api` layer plus
:mod:`sp_api.util` is sufficient.