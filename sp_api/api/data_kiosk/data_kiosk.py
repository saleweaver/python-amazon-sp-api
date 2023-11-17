import urllib.parse

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

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0222 | 10 |

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

        return self._request(kwargs.pop('path'), params=kwargs)

    @sp_endpoint('/dataKiosk/2023-11-15/queries', method='POST')
    def create_query(self, **kwargs) -> ApiResponse:
        """
        create_query(self, **kwargs) -> ApiResponse

        Creates a Data Kiosk query request.

        **Note:** The retention of a query varies based on the fields requested. Each field within a schema is annotated with a `@resultRetention` directive that defines how long a query containing that field will be retained. When a query contains multiple fields with different retentions, the shortest (minimum) retention is applied. The retention of a query's resulting documents always matches the retention of the query.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0167 | 15 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:
        
            body: | * REQUIRED {'description': 'Information required to create the query.',
                     'properties': {'paginationToken': {'description': 'A token to fetch a certain page of query results when there are multiple pages of query results available. The value of this token must be fetched from the `pagination.nextToken` field of the '
                                                                       '`Query` object, and the `query` field for this object must also be set to the `query` field of the same `Query` object. A `Query` object can be retrieved from either the `getQueries` or `getQuery` '
                                                                       'operation. In the absence of this token value, the first page of query results will be requested.',
                                                        'type': 'string'},
                                    'query': {'description': 'The GraphQL query to submit. A query must be at most 8000 characters after unnecessary whitespace is removed.', 'type': 'string'}},
                     'required': ['query'],
                     'type': 'object'}


        Returns:
            ApiResponse:
        """

        return self._request(kwargs.pop('path'), data=kwargs)

    @sp_endpoint('/dataKiosk/2023-11-15/queries/{}', method='DELETE')
    def cancel_query(self, queryId, **kwargs) -> ApiResponse:
        """
        cancel_query(self, queryId, **kwargs) -> ApiResponse

        Cancels the query specified by the `queryId` parameter. Only queries with a non-terminal `processingStatus` (`IN_QUEUE`, `IN_PROGRESS`) can be cancelled. Cancelling a query that already has a `processingStatus` of `CANCELLED` will no-op. Cancelled queries are returned in subsequent calls to the `getQuery` and `getQueries` operations.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0222 | 10 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:
        
            queryId:string | * REQUIRED The identifier for the query. This identifier is unique only in combination with a selling partner account ID.
        

        Returns:
            ApiResponse:
        """

        return self._request(fill_query_params(kwargs.pop('path'), queryId), data=kwargs)

    @sp_endpoint('/dataKiosk/2023-11-15/queries/{}', method='GET')
    def get_query(self, queryId, **kwargs) -> ApiResponse:
        """
        get_query(self, queryId, **kwargs) -> ApiResponse

        Returns query details for the query specified by the `queryId` parameter. See the `createQuery` operation for details about query retention.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2.0 | 15 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:
        
            queryId:string | * REQUIRED The query identifier.
        

        Returns:
            ApiResponse:
        """

        return self._request(fill_query_params(kwargs.pop('path'), queryId), params=kwargs)

    @sp_endpoint('/dataKiosk/2023-11-15/documents/{}', method='GET')
    def get_document(self, documentId, **kwargs) -> ApiResponse:
        """
        get_document(self, documentId, **kwargs) -> ApiResponse

        Returns the information required for retrieving a Data Kiosk document's contents. See the `createQuery` operation for details about document retention.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0167 | 15 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:
        
            documentId:string | * REQUIRED The identifier for the Data Kiosk document.
        

        Returns:
            ApiResponse:
        """

        return self._request(fill_query_params(kwargs.pop('path'), documentId), params=kwargs)
