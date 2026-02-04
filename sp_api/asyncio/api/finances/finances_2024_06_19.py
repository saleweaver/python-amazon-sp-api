from sp_api.base import ApiResponse
from sp_api.base import sp_endpoint, fill_query_params
from sp_api.asyncio.base import AsyncBaseClient


class FinancesV20240619(AsyncBaseClient):

    @sp_endpoint("/finances/2024-06-19/orders/{}/financialEvents")
    async def get_financial_events_for_order(self, order_id, **kwargs) -> ApiResponse:
        """
        get_financial_events_for_order(self, order_id, **kwargs) -> ApiResponse
        
         
        
        Examples:
            literal blocks::
            
                await FinancesV20240619().get_financial_events_for_order("value")
        
        Args:
            order_id:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """
        return await self._request(
            fill_query_params(kwargs.pop("path"), order_id), params={**kwargs}
        )

    @sp_endpoint("/finances/2024-06-19/financialEvents")
    async def list_financial_events(self, **kwargs) -> ApiResponse:
        """
        list_financial_events(self, **kwargs) -> ApiResponse
        
         
        
        Examples:
            literal blocks::
            
                await FinancesV20240619().list_financial_events()
        
        Args:
            **kwargs:
        
        Returns:
            ApiResponse
        """
        return await self._request(fill_query_params(kwargs.pop("path")), params={**kwargs})

    @sp_endpoint("/finances/2024-06-19/financialEventGroups/{}/financialEvents")
    async def list_financial_events_by_group_id(
        self, event_group_id, **kwargs
    ) -> ApiResponse:
        """
        list_financial_events_by_group_id(self, event_group_id, **kwargs) -> ApiResponse
        
         
        
        Examples:
            literal blocks::
            
                await FinancesV20240619().list_financial_events_by_group_id("value")
        
        Args:
            event_group_id:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """
        return await self._request(
            fill_query_params(kwargs.pop("path"), event_group_id), params={**kwargs}
        )

    @sp_endpoint("/finances/2024-06-19/financialEventGroups")
    async def list_financial_event_groups(self, **kwargs) -> ApiResponse:
        """
        list_financial_event_groups(self, **kwargs) -> ApiResponse
        
         
        
        Examples:
            literal blocks::
            
                await FinancesV20240619().list_financial_event_groups()
        
        Args:
            **kwargs:
        
        Returns:
            ApiResponse
        """
        return await self._request(kwargs.pop("path"), params={**kwargs})

    @sp_endpoint("/finances/2024-06-19/transactions")
    async def list_transactions(self, **kwargs) -> ApiResponse:
        """
        list_transactions(self, **kwargs) -> ApiResponse
        
        Returns transactions for the given parameters. Financial events might not include orders from the last 48 hours.
        
        Examples:
            literal blocks::
            
                await FinancesV20240619().list_transactions()
        
        Args:
            **kwargs:
        
        Returns:
            ApiResponse
        """

        return await self._request(kwargs.pop("path"), params={**kwargs})
