import uuid

from sp_api.base import Client, sp_endpoint, ApiResponse, fill_query_params


class ExternalFulfillmentReturnsV20240911(Client):
    """
    External Fulfillment Returns API (version 2024-09-11).
    """

    @sp_endpoint("/externalFulfillment/returns/2024-09-11/returns", method="GET")
    def list_returns(self, **kwargs) -> ApiResponse:
        """
        list_returns(self, **kwargs) -> ApiResponse
        
        Get a list of return items dropped for the seller in the specified node, and in the specified status. Returns can be further filtered based on their creation date/time
        
        Examples:
            literal blocks::
            
                ExternalFulfillmentReturnsV20240911().list_returns()
        
        Args:
            **kwargs:
        
        Returns:
            ApiResponse
        """

        return self._request(kwargs.pop("path"), params=kwargs, add_marketplace=False)

    @sp_endpoint("/externalFulfillment/returns/2024-09-11/returns/{}", method="GET")
    def get_return(self, returnId, **kwargs) -> ApiResponse:
        """
        get_return(self, returnId, **kwargs) -> ApiResponse
        
        Get a single return item with the specified id.
        
        Examples:
            literal blocks::
            
                ExternalFulfillmentReturnsV20240911().get_return("value")
        
        Args:
            returnId:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """
        return self._request(
            fill_query_params(kwargs.pop("path"), returnId),
            params=kwargs,
            add_marketplace=False,
        )

    @sp_endpoint("/externalFulfillment/returns/2024-09-11/returns/{}", method="PATCH")
    def process_return_item(self, returnId, **kwargs) -> ApiResponse:
        """
        process_return_item(self, returnId, **kwargs) -> ApiResponse
        
        Process a return by grading. Determine the item condition and update the quantities for each item condition.
        
        Examples:
            literal blocks::
            
                ExternalFulfillmentReturnsV20240911().process_return_item("value")
        
        Args:
            returnId:  | required
            **kwargs:
        
        Returns:
            ApiResponse
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

    @sp_endpoint("/externalFulfillment/2024-09-11/returns", method="GET")
    def list_returns_get(self, **kwargs) -> ApiResponse:
        """
        list_returns_get(self, **kwargs) -> ApiResponse
        
        Retrieve a list of return items. You can filter results by location, RMA ID, status, or time.
        
        Examples:
            literal blocks::
            
                ExternalFulfillmentReturnsV20240911().list_returns_get()
        
        Args:
            key returnLocationId: object |  The SmartConnect location ID of the location from which you want to retrieve return items.
            key rmaId: object |  The RMA ID of the return items you want to list.
            key status: object |  The status of return items you want to list. You can retrieve all new return items with the `CREATED` status.
            key reverseTrackingId: object |  The reverse tracking ID of the return items you want to list.
            key createdSince: object |  Return items created after the specified date are included in the response. In [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format.
            key createdUntil: object |  Return items created before the specified date are included in the response. In [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format.
            key lastUpdatedSince: object |  Return items updated after the specified date are included in the response. In [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format. If you supply this parameter, you must also supply `returnLocationId` and `status`.
            key lastUpdatedUntil: object |  Return items whose most recent update is before the specified date are included in the response. In [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date-time format. If you supply this parameter, you must also supply `returnLocationId` and `status`.
            key lastUpdatedAfter: object |  DEPRECATED. Use the `createdSince` parameter.
            key lastUpdatedBefore: object |  DEPRECATED. Use the `createdUntil` parameter.
            key maxResults: object |  The number of return items you want to include in the response.
                **Default:** 10
                **Maximum:** 100
            key nextToken: object |  A token that you use to retrieve the next page of results. The response includes `nextToken` when there are multiple pages of results. To get the next page of results, call the operation with this token and include the same arguments as the call that produced the token. To get a complete list, call this operation until `nextToken` is null. Note that this operation can return empty pages.
        
        Returns:
            ApiResponse
        """
        return self._request(kwargs.pop("path"), params=kwargs, add_marketplace=False)

    @sp_endpoint("/externalFulfillment/2024-09-11/returns/{}", method="GET")
    def get_return_get(self, returnId, **kwargs) -> ApiResponse:
        """
        get_return_get(self, returnId, **kwargs) -> ApiResponse
        
        Retrieve the return item with the specified ID.
        
        Examples:
            literal blocks::
            
                ExternalFulfillmentReturnsV20240911().get_return_get("value")
        
        Args:
            returnId: object | required The ID of the return item you want.
        
        Returns:
            ApiResponse
        """
        return self._request(fill_query_params(kwargs.pop("path"), returnId), params=kwargs, add_marketplace=False)
