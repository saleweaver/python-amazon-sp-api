from sp_api.base import ApiResponse
from sp_api.base import sp_endpoint, fill_query_params
from sp_api.asyncio.base import AsyncBaseClient


class FinancesV0(AsyncBaseClient):

    @sp_endpoint("/finances/v0/orders/{}/financialEvents")
    async def get_financial_events_for_order(self, order_id, **kwargs) -> ApiResponse:
        """
        get_financial_events_for_order(self, order_id, **kwargs) -> ApiResponse
        
        Returns all financial events for the specified order. Orders from the last 48 hours might not be included in financial events.
        
        Examples:
            literal blocks::
            
                await FinancesV0().get_financial_events_for_order("value")
        
        Args:
            order_id:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """
        return await self._request(
            fill_query_params(kwargs.pop("path"), order_id), params={**kwargs}
        )

    @sp_endpoint("/finances/v0/financialEvents")
    async def list_financial_events(self, **kwargs) -> ApiResponse:
        """
        list_financial_events(self, **kwargs) -> ApiResponse
        
        Returns financial events for the specified data range. Orders from the last 48 hours might not be included in financial events.
                        **Note:** in `ListFinancialEvents`, deferred events don't show up in responses until they are released.
        
        Examples:
            literal blocks::
            
                await FinancesV0().list_financial_events()
        
        Args:
            **kwargs:
        
        Returns:
            ApiResponse
        """
        return await self._request(fill_query_params(kwargs.pop("path")), params={**kwargs})

    @sp_endpoint("/finances/v0/financialEventGroups/{}/financialEvents")
    async def list_financial_events_by_group_id(
        self, event_group_id, **kwargs
    ) -> ApiResponse:
        """
        list_financial_events_by_group_id(self, event_group_id, **kwargs) -> ApiResponse
        
        Returns all financial events for the specified financial event group. Orders from the last 48 hours might not be included in financial events.
                        **Note:** This operation only retrieves a group's data for the past two years. A request for data spanning more than two years produces an empty response.
        
        Examples:
            literal blocks::
            
                await FinancesV0().list_financial_events_by_group_id("value")
        
        Args:
            event_group_id:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """
        return await self._request(
            fill_query_params(kwargs.pop("path"), event_group_id), params={**kwargs}
        )

    @sp_endpoint("/finances/v0/financialEventGroups")
    async def list_financial_event_groups(self, **kwargs) -> ApiResponse:
        """
        list_financial_event_groups(self, **kwargs) -> ApiResponse
        
        Returns financial event groups for a given date range. Orders from the last 48 hours might not be included in financial events.
        
        Examples:
            literal blocks::
            
                await FinancesV0().list_financial_event_groups()
        
        Args:
            **kwargs:
        
        Returns:
            ApiResponse
        """
        return await self._request(kwargs.pop("path"), params={**kwargs})

    @sp_endpoint("/finances/v0/transactions")
    async def list_transactions(self, **kwargs) -> ApiResponse:
        """
        list_transactions(self, **kwargs) -> ApiResponse
        
         
        
        Examples:
            literal blocks::
            
                await FinancesV0().list_transactions()
        
        Args:
            **kwargs:
        
        Returns:
            ApiResponse
        """

        return await self._request(kwargs.pop("path"), params={**kwargs})
