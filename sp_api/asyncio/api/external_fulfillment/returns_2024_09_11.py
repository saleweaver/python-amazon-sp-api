import uuid

from sp_api.base import sp_endpoint, ApiResponse, fill_query_params
from sp_api.asyncio.base import AsyncBaseClient


class ExternalFulfillmentReturnsV20240911(AsyncBaseClient):
    """
    External Fulfillment Returns API (version 2024-09-11).
    """

    @sp_endpoint("/externalFulfillment/returns/2024-09-11/returns", method="GET")
    async def list_returns(self, **kwargs) -> ApiResponse:
        """
        list_returns(self, **kwargs) -> ApiResponse

        Get a list of return items dropped for the seller in the specified node, and in the specified status. Returns can be further filtered based on their creation date/time

        **Usage Plans:**

        ======================================
        Rate (requests per second)
        ======================================
        5
        ======================================

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            key returnLocationId:string | The SmartConnect location identifier for which return items are to be retrieved
            key rmaId:string | The RMA id of the return items to be listed
            key status:string | Retrieves only those return items which are in the specified status. The most common use-case would be to fetch all new return items which would be in the CREATED status
            key reverseTrackingId:string | The reverseTrackingId of the return items to be listed
            key createdSince:string | Return items whose creation is after the specified date/time are included in the response. This field should be in the ISO8601 date/time format.
            key createdUntil:string | Return items whose creation is before the specified date/time are included in the response. This field should be in the ISO8601 date/time format.
            key lastUpdatedSince:string | Return items whose last update is after the specified date/time are included in the response. This field should be in the ISO8601 date/time format. Only to be used along with returnLocationId and status params.
            key lastUpdatedUntil:string | Return items whose last update is before the specified date/time are included in the response. This field should be in the ISO8601 date/time format. Only to be used along with returnLocationId and status params.
            key lastUpdatedAfter:string | DEPRECATED. Use createdFrom param instead for same results. Return items whose creation is after the specified date/time are included in the response. This field should be in the ISO8601 date/time format.
            key lastUpdatedBefore:string | DEPRECATED. Use createdTo param instead for same results. Return items whose creation is before the specified date/time are included in the response. This field should be in the ISO8601 date/time format.
            key maxResults:integer | Specify the number of return items to be included in the response. It will default to 10 in case not provided. Maximum limit is 100.
            key nextToken:string | A cursor representing information about the next page of returns. Use the value returned in previous calls to page through the complete list of returns.

        Returns:
            ApiResponse:
        """

        return await self._request(kwargs.pop("path"), params=kwargs, add_marketplace=False)


    @sp_endpoint("/externalFulfillment/returns/2024-09-11/returns/{}", method="GET")
    async def get_return(self, returnId, **kwargs) -> ApiResponse:
        """
        get_return(self, returnId, **kwargs) -> ApiResponse

        Get a single return item with the specified id.

        **Usage Plan:**

        ======================================
        Rate (requests per second)
        ======================================
        5
        ======================================

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            returnId:string | * REQUIRED The id of the return item to be retrieved.

        Returns:
            ApiResponse:
        """
        return await self._request(
            fill_query_params(kwargs.pop("path"), returnId),
            params=kwargs,
            add_marketplace=False,
        )

    @sp_endpoint("/externalFulfillment/returns/2024-09-11/returns/{}", method="PATCH")
    async def process_return_item(self, returnId, **kwargs) -> ApiResponse:
        """
        process_return_item(self, returnId, **kwargs) -> ApiResponse

        Process a return by grading. Determine the item condition and update the quantities for each item condition.

        **Usage Plan:**

        ======================================
        Rate (requests per second)
        ======================================
        5
        ======================================

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            returnId:string | * REQUIRED The id of the return item to be retrieved.

            body: {
              "op": "increment",
              "path": "/processedReturns",
              "value": {
                "Sellable": 0,
                "Defective": 0,
                "CustomerDamaged": 0,
                "CarrierDamaged": 0,
                "Fraud": 0,
                "WrongItem": 0
              }
            }

        Returns:
            ApiResponse:
        """

        headers = await self._get_headers()
        if "x-amzn-idempotency-token" in kwargs:
            headers["x-amzn-idempotency-token"] = kwargs.pop("x-amzn-idempotency-token")
        else:
            headers["x-amzn-idempotency-token"] = str(uuid.uuid4())

        return await self._request(
            fill_query_params(kwargs.pop("path"), returnId),
            data=kwargs,
            headers=headers,
            add_marketplace=False,
        )

    @sp_endpoint("/externalFulfillment/2024-09-11/returns", method="GET")
    async def list_returns_get(self, **kwargs) -> ApiResponse:
        """
        list_returns_get(self, **kwargs) -> ApiResponse

        Retrieve a list of return items. You can filter results by location, RMA ID, status, or time.

        Args:
            key returnLocationId:string |  The SmartConnect location ID of the location from which you want to retrieve return items.
            key rmaId:string |  The RMA ID of the return items you want to list.
            key status:string |  The status of return items you want to list. You can retrieve all new return items with the `CREATED` status.
            key reverseTrackingId:string |  The reverse tracking ID of the return items you want to list.
            key createdSince:string |  Return items created after the specified date are included in the response. In [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format.
            key createdUntil:string |  Return items created before the specified date are included in the response. In [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format.
            key lastUpdatedSince:string |  Return items updated after the specified date are included in the response. In [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format. If you supply this parameter, you must also supply `returnLocationId` and `status`.
            key lastUpdatedUntil:string |  Return items whose most recent update is before the specified date are included in the response. In [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format. If you supply this parameter, you must also supply `returnLocationId` and `status`.
            key lastUpdatedAfter:string |  DEPRECATED. Use the `createdSince` parameter.
            key lastUpdatedBefore:string |  DEPRECATED. Use the `createdUntil` parameter.
            key maxResults:integer |  The number of return items you want to include in the response.
            
            **Default:** 10
            
            **Maximum:** 100
            key nextToken:string |  A token that you use to retrieve the next page of results. The response includes `nextToken` when there are multiple pages of results. To get the next page of results, call the operation with this token and include the same arguments as the call that produced the token. To get a complete list, call this operation until `nextToken` is null. Note that this operation can return empty pages.

        Returns:
            ApiResponse:
        """
        return await self._request(kwargs.pop("path"), params=kwargs, add_marketplace=False)

    @sp_endpoint("/externalFulfillment/2024-09-11/returns/{}", method="GET")
    async def get_return_get(self, returnId, **kwargs) -> ApiResponse:
        """
        get_return_get(self, returnId, **kwargs) -> ApiResponse

        Retrieve the return item with the specified ID.

        Args:
            returnId:string | * REQUIRED The ID of the return item you want.

        Returns:
            ApiResponse:
        """
        return await self._request(fill_query_params(kwargs.pop("path"), returnId), params=kwargs, add_marketplace=False)
