import urllib.parse
from io import BytesIO, StringIO
from typing import Union, BinaryIO, TextIO

from sp_api.base import Client, sp_endpoint, fill_query_params, ApiResponse


class DataKiosk(Client):
    """
    DataKiosk SP-API Client
    :link: 

    The Selling Partner API for Data Kiosk lets you submit GraphQL queries from a variety of schemas to help selling partners manage their businesses.
    """

    @sp_endpoint('/dataKiosk/2023-11-15/queries', method='GET')
    def get_queries(self, **kwargs) -> ApiResponse:
        """
        get_queries(self, **kwargs) -> ApiResponse

        Returns details for the Data Kiosk queries that match the specified filters. See the `createQuery` operation for details about query retention.

        **Usage Plan:**

        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        0.0222                                  10
        ======================================  ==============


        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:
        
            key processingStatuses:array |  A list of processing statuses used to filter queries.
        
            key pageSize:integer |  The maximum number of queries to return in a single call.
        
            key createdSince:string |  The earliest query creation date and time for queries to include in the response, in ISO 8601 date time format. The default is 90 days ago.
        
            key createdUntil:string |  The latest query creation date and time for queries to include in the response, in ISO 8601 date time format. The default is the time of the `getQueries` request.
        
            key paginationToken:string |  A token to fetch a certain page of results when there are multiple pages of results available. The value of this token is fetched from the `pagination.nextToken` field returned in the `GetQueriesResponse` object. All other parameters must be provided with the same values that were provided with the request that generated this token, with the exception of `pageSize` which can be modified between calls to `getQueries`. In the absence of this token value, `getQueries` returns the first page of results.
        

        Returns:
            ApiResponse:
        """

        return self._request(kwargs.pop('path'), params=kwargs, add_marketplace=False)

    @sp_endpoint('/dataKiosk/2023-11-15/queries', method='POST')
    def create_query(self, query, pagination_token=None, **kwargs) -> ApiResponse:
        """
        create_query(self, query, pagination_token=None, **kwargs) -> ApiResponse

        Creates a Data Kiosk query request.

        **Note:** The retention of a query varies based on the fields requested. Each field within a schema is annotated with a `@resultRetention` directive that defines how long a query containing that field will be retained. When a query contains multiple fields with different retentions, the shortest (minimum) retention is applied. The retention of a query's resulting documents always matches the retention of the query.

        **Usage Plan:**

        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        0.0167                                  15
        ======================================  ==============


        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:
        
            query:string | * REQUIRED The query to submit. The query must be a valid GraphQL query in the schema specified by the `schema` parameter.
            pagination_token:string |  A token to fetch a certain page of results when there are multiple pages of results available. The value of this token is fetched from the `pagination.nextToken` field returned in the `GetQueriesResponse` object. All other parameters must be provided with the same values that were provided with the request that generated this token, with the exception of `pageSize` which can be modified between calls to `getQueries`. In the absence of this token value, `getQueries` returns the first page of results.


        Returns:
            ApiResponse:
        """
        kwargs['query'] = query
        if pagination_token:
            kwargs['paginationToken'] = pagination_token
        return self._request(kwargs.pop('path'), data=kwargs, add_marketplace=False)

    @sp_endpoint('/dataKiosk/2023-11-15/queries/{}', method='DELETE')
    def cancel_query(self, query_id, **kwargs) -> ApiResponse:
        """
        cancel_query(self, queryId, **kwargs) -> ApiResponse

        Cancels the query specified by the `queryId` parameter. Only queries with a non-terminal `processingStatus` (`IN_QUEUE`, `IN_PROGRESS`) can be cancelled. Cancelling a query that already has a `processingStatus` of `CANCELLED` will no-op. Cancelled queries are returned in subsequent calls to the `getQuery` and `getQueries` operations.

        **Usage Plan:**

        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        0.0222                                  10
        ======================================  ==============

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:
        
            query_id:string | * REQUIRED The identifier for the query. This identifier is unique only in combination with a selling partner account ID.
        

        Returns:
            ApiResponse:
        """

        return self._request(fill_query_params(kwargs.pop('path'), query_id), data=kwargs, add_marketplace=False)

    @sp_endpoint('/dataKiosk/2023-11-15/queries/{}', method='GET')
    def get_query(self, query_id, **kwargs) -> ApiResponse:
        """
        get_query(self, queryId, **kwargs) -> ApiResponse

        Returns query details for the query specified by the `queryId` parameter. See the `createQuery` operation for details about query retention.

        **Usage Plan:**

        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        2                                       15
        ======================================  ==============

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:
        
            query_id:string | * REQUIRED The query identifier.
        

        Returns:
            ApiResponse:
        """

        return self._request(fill_query_params(kwargs.pop('path'), query_id), params=kwargs, add_marketplace=False)

    @sp_endpoint('/dataKiosk/2023-11-15/documents/{}', method='GET')
    def get_document(self, document_id, download: bool = False, file: Union[BytesIO, str, BinaryIO, TextIO] = None,
                     encoding='utf-8', **kwargs) -> ApiResponse:
        """
        get_document(self, document_id, download: bool = False, file: Union[BytesIO, str, BinaryIO, TextIO] = None, encoding='utf-8', **kwargs) -> ApiResponse

        Returns the information required for retrieving a Data Kiosk document's contents. See the `createQuery` operation for details about document retention.

        **Usage Plan:**

        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        0.0167                                  15
        ======================================  ==============

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:
        
            document_id:string | * REQUIRED The identifier for the Data Kiosk document.
            file: | * OPTIONAL The file to write the response to.
            download: | * OPTIONAL If True, the file will be downloaded and returned in the payload.
            encoding: | * OPTIONAL The encoding to use when writing the file. Defaults to utf-8, binary data is written if applicable filemode is passed.


        Returns:
            ApiResponse:
        """

        res = self._request(fill_query_params(kwargs.pop('path'), document_id), params=kwargs, add_marketplace=False)
        if download or file or ('decrypt' in kwargs and kwargs['decrypt']):
            import requests
            document_response = requests.get(
                res.payload.get('documentUrl'),
                proxies=self.proxies,
                verify=self.verify,
            )
            document = document_response.content
            if download:
                res.payload.update({
                    'document': document,
                })
            if file:
                self._handle_file(file, document, encoding=encoding)
        return res

    @staticmethod
    def _handle_file(file, document, encoding='utf-8'):
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
            if 'b' in file.mode:
                file.write(document)
            else:
                file.write(document.decode(encoding))
