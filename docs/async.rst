Async Clients
=============

The library ships async counterparts for most API clients under ``sp_api.asyncio``.
These clients are built for ``asyncio`` and are safe to use concurrently in
event loops.

Importing async clients
-----------------------

Async clients live in ``sp_api.asyncio.api`` and share the same constructor
signature as the sync clients.

.. code-block:: python

   from sp_api.asyncio.api import Orders, Reports

Basic usage
-----------

.. code-block:: python

   import asyncio
   from datetime import datetime, timedelta, timezone

   from sp_api.asyncio.api import Orders, Reports
   from sp_api.base.reportTypes import ReportType


   async def main():
       async with Orders() as orders_client:
           res = await orders_client.get_orders(
               LastUpdatedAfter=(datetime.now(timezone.utc) - timedelta(days=1)).isoformat()
           )
           print(res.payload)

       async with Reports() as reports_client:
           report = await reports_client.create_report(
               reportType=ReportType.GET_MERCHANT_LISTINGS_ALL_DATA
           )
           print(report.payload)


   if __name__ == "__main__":
       asyncio.run(main())

Streaming a report document
---------------------------

Use ``stream=True`` with ``file=...`` to write large report files without
loading the full document into memory.

.. code-block:: python

   import asyncio
   from sp_api.asyncio.api import Reports


   async def download_report(doc_id):
       async with Reports() as reports_client:
           await reports_client.get_report_document(
               doc_id,
               file="report.txt",
               stream=True,
           )


   if __name__ == "__main__":
       asyncio.run(download_report("YOUR-REPORT-DOCUMENT-ID"))

Closing clients
---------------

If you do not use ``async with``, call ``await client.aclose()`` to close the
underlying HTTP connections.
