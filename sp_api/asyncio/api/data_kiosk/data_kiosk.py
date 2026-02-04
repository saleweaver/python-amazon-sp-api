import urllib.parse
from io import BytesIO, StringIO
from typing import Union, BinaryIO, TextIO

from sp_api.base import ApiResponse, fill_query_params, sp_endpoint
from sp_api.asyncio.base import AsyncBaseClient


class DataKiosk(AsyncBaseClient):
    """
    DataKiosk SP-API Client
    :link:

    The Selling Partner API for Data Kiosk lets you submit GraphQL queries from a variety of schemas to help selling partners manage their businesses.
    """

    @sp_endpoint("/dataKiosk/2023-11-15/queries", method="GET")
    async def get_queries(self, **kwargs) -> ApiResponse:
        """
        get_queries(self, **kwargs) -> ApiResponse
        
        Returns details for the Data Kiosk queries that match the specified filters. See the `createQuery` operation for details about query retention.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        0.0222                                  10
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await DataKiosk().get_queries()
        
        Args:
            key processingStatuses: object |  A list of processing statuses used to filter queries.
            key pageSize: object |  The maximum number of queries to return in a single call.
            key createdSince: object |  The earliest query creation date and time for queries to include in the response, in ISO 8601 date time format. The default is 90 days ago.
            key createdUntil: object |  The latest query creation date and time for queries to include in the response, in ISO 8601 date time format. The default is the time of the `getQueries` request.
            key paginationToken: object |  A token to fetch a certain page of results when there are multiple pages of results available. The value of this token is fetched from the `pagination.nextToken` field returned in the `GetQueriesResponse` object. All other parameters must be provided with the same values that were provided with the request that generated this token, with the exception of `pageSize` which can be modified between calls to `getQueries`. In the absence of this token value, `getQueries` returns the first page of results.
        
        Returns:
            ApiResponse
        """

        return await self._request(
            kwargs.pop("path"),
            params=kwargs,
            add_marketplace=False,
        )

    @sp_endpoint("/dataKiosk/2023-11-15/queries", method="POST")
    async def create_query(self, query, pagination_token=None, **kwargs) -> ApiResponse:
        """
        create_query(self, query, pagination_token, **kwargs) -> ApiResponse
        
        Creates a Data Kiosk query request.
        
        **Note:** The retention of a query varies based on the fields requested. Each field within a schema is annotated with a `@resultRetention` directive that defines how long a query containing that field will be retained. When a query contains multiple fields with different retentions, the shortest (minimum) retention is applied. The retention of a query's resulting documents always matches the retention of the query.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        0.0167                                  15
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await DataKiosk().create_query("value", "value")
        
        Args:
            body: CreateQuerySpecification | required The body of the request.
        
        Returns:
            ApiResponse
        """
        kwargs["query"] = query
        if pagination_token:
            kwargs["paginationToken"] = pagination_token
        return await self._request(
            kwargs.pop("path"),
            data=kwargs,
            add_marketplace=False,
        )

    @sp_endpoint("/dataKiosk/2023-11-15/queries/{}", method="DELETE")
    async def cancel_query(self, query_id, **kwargs) -> ApiResponse:
        """
        cancel_query(self, query_id, **kwargs) -> ApiResponse
        
        Cancels the query specified by the `queryId` parameter. Only queries with a non-terminal `processingStatus` (`IN_QUEUE`, `IN_PROGRESS`) can be cancelled. Cancelling a query that already has a `processingStatus` of `CANCELLED` will no-op. Cancelled queries are returned in subsequent calls to the `getQuery` and `getQueries` operations.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        0.0222                                  10
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await DataKiosk().cancel_query("value")
        
        Args:
            queryId: object | required The identifier for the query. This identifier is unique only in combination with a selling partner account ID.
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), query_id),
            data=kwargs,
            add_marketplace=False,
        )

    @sp_endpoint("/dataKiosk/2023-11-15/queries/{}", method="GET")
    async def get_query(self, query_id, **kwargs) -> ApiResponse:
        """
        get_query(self, query_id, **kwargs) -> ApiResponse
        
        Returns query details for the query specified by the `queryId` parameter. See the `createQuery` operation for details about query retention.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        2.0                                     15
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await DataKiosk().get_query("value")
        
        Args:
            queryId: object | required The query identifier.
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), query_id),
            params=kwargs,
            add_marketplace=False,
        )

    @sp_endpoint("/dataKiosk/2023-11-15/documents/{}", method="GET")
    async def get_document(
        self,
        document_id,
        download: bool = False,
        file: Union[BytesIO, str, BinaryIO, TextIO] = None,
        encoding="utf-8",
        **kwargs
    ) -> ApiResponse:
        """
        get_document(self, document_id, download, file, encoding, **kwargs) -> ApiResponse
        
        Returns the information required for retrieving a Data Kiosk document's contents. See the `createQuery` operation for details about document retention.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        0.0167                                  15
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await DataKiosk().get_document("value", "value", "value", "value")
        
        Args:
            documentId: object | required The identifier for the Data Kiosk document.
        
        Returns:
            ApiResponse
        """

        res = await self._request(
            fill_query_params(kwargs.pop("path"), document_id),
            params=kwargs,
            add_marketplace=False,
        )
        if download or file or ("decrypt" in kwargs and kwargs["decrypt"]):
            document_response = await self._transport.request(
                "GET",
                res.payload.get("documentUrl"),
            )
            document = document_response.content
            if download:
                res.payload.update(
                    {
                        "document": document,
                    }
                )
            if file:
                self._handle_file(file, document, encoding=encoding)
        return res

    @staticmethod
    def _handle_file(file, document, encoding="utf-8"):
        if isinstance(file, str):
            if isinstance(document, bytes):
                with open(file, "wb+") as f:
                    f.write(document)
            else:
                with open(file, "w+") as text_file:
                    text_file.write(document)
        elif isinstance(file, BytesIO):
            file.write(document)
            file.seek(0)
        elif isinstance(file, StringIO):
            file.write(document.decode(encoding))
            file.seek(0)
        else:
            if "b" in file.mode:
                file.write(document)
            else:
                file.write(document.decode(encoding))