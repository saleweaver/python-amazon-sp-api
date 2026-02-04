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
        
        Examples:
            literal blocks::
            
                ExternalFulfillmentReturnsV20210819().list_returns()
        
        Args:
            **kwargs:
        
        Returns:
            ApiResponse
        """

        return self._request(kwargs.pop("path"), params=kwargs, add_marketplace=False)

    @sp_endpoint("/externalFulfillment/returns/2021-08-19/returns/{}", method="GET")
    def get_return(self, returnId, **kwargs) -> ApiResponse:
        """
        get_return(self, returnId, **kwargs) -> ApiResponse
        
        Get a single return item with the specified id.
        
        Examples:
            literal blocks::
            
                ExternalFulfillmentReturnsV20210819().get_return("value")
        
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

    @sp_endpoint("/externalFulfillment/returns/2021-08-19/returns/{}", method="PATCH")
    def process_return_item(self, returnId, **kwargs) -> ApiResponse:
        """
        process_return_item(self, returnId, **kwargs) -> ApiResponse
        
        Process a return by grading. Determine the item condition and update the quantities for each item condition.
        
        Examples:
            literal blocks::
            
                ExternalFulfillmentReturnsV20210819().process_return_item("value")
        
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
