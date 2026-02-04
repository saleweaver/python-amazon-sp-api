import uuid

from sp_api.base import Client, sp_endpoint, ApiResponse, fill_query_params


class ExternalFulfillmentReturnsV20210819(Client):
    """
    External Fulfillment Returns API (version 2021-08-19).
    """

    @sp_endpoint("/externalFulfillment/returns/2021-08-19/returns", method="GET")
    def list_returns(self, **kwargs) -> ApiResponse:
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

        return self._request(kwargs.pop("path"), params=kwargs, add_marketplace=False)

    @sp_endpoint("/externalFulfillment/returns/2021-08-19/returns/{}", method="GET")
    def get_return(self, returnId, **kwargs) -> ApiResponse:
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
        return self._request(
            fill_query_params(kwargs.pop("path"), returnId),
            params=kwargs,
            add_marketplace=False,
        )

    @sp_endpoint("/externalFulfillment/returns/2021-08-19/returns/{}", method="PATCH")
    def process_return_item(self, returnId, **kwargs) -> ApiResponse:
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

        headers = self.headers.copy()
        if "x-amzn-idempotency-token" in kwargs:
            headers["x-amzn-idempotency-token"] = kwargs.pop("x-amzn-idempotency-token")
        else:
            headers["x-amzn-idempotency-token"] = str(uuid.uuid4())

        return self._request(
            fill_query_params(kwargs.pop("path"), returnId),
            data=kwargs,
            headers=headers,
            add_marketplace=False,
        )
