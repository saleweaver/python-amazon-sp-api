from sp_api.base import Client, sp_endpoint, fill_query_params, ApiResponse
from sp_api.asyncio.base import AsyncBaseClient


class SupplySources(AsyncBaseClient):
    """
    SupplySources SP-API Client
    :link:

    Manage configurations and capabilities of seller supply sources.
    """

    @sp_endpoint("/supplySources/2020-07-01/supplySources", method="GET")
    async def get_supply_sources(self, **kwargs) -> ApiResponse:
        """
        get_supply_sources(self, **kwargs) -> ApiResponse
        
        The path to retrieve paginated supply sources.
        
        Examples:
            literal blocks::
            
                await SupplySources().get_supply_sources()
        
        Args:
            key nextPageToken: object |  The pagination token to retrieve a specific page of results.
            key pageSize: object |  The number of supply sources to return per paginated request.
        
        Returns:
            ApiResponse
        """

        return await self._request(kwargs.pop("path"), params=kwargs)

    @sp_endpoint("/supplySources/2020-07-01/supplySources", method="POST")
    async def create_supply_source(self, **kwargs) -> ApiResponse:
        """
        create_supply_source(self, **kwargs) -> ApiResponse
        
        Create a new supply source.
        
        Examples:
            literal blocks::
            
                await SupplySources().create_supply_source()
        
        Args:
            payload: CreateSupplySourceRequest | required A request to create a supply source.
        
        Returns:
            ApiResponse
        """

        return await self._request(kwargs.pop("path"), data=kwargs)

    @sp_endpoint("/supplySources/2020-07-01/supplySources/{}", method="GET")
    async def get_supply_source(self, supplySourceId, **kwargs) -> ApiResponse:
        """
        get_supply_source(self, supplySourceId, **kwargs) -> ApiResponse
        
        Retrieve a supply source.
        
        Examples:
            literal blocks::
            
                await SupplySources().get_supply_source("value")
        
        Args:
            supplySourceId: object | required The unique identifier of a supply source.
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), supplySourceId), params=kwargs
        )

    @sp_endpoint("/supplySources/2020-07-01/supplySources/{}", method="PUT")
    async def update_supply_source(self, supplySourceId, **kwargs) -> ApiResponse:
        """
        update_supply_source(self, supplySourceId, **kwargs) -> ApiResponse
        
        Update the configuration and capabilities of a supply source.
        
        Examples:
            literal blocks::
            
                await SupplySources().update_supply_source("value")
        
        Args:
            supplySourceId: object | required The unique identitier of a supply source.
            payload: UpdateSupplySourceRequest |
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), supplySourceId), data=kwargs
        )

    @sp_endpoint("/supplySources/2020-07-01/supplySources/{}", method="DELETE")
    async def archive_supply_source(self, supplySourceId, **kwargs) -> ApiResponse:
        """
        archive_supply_source(self, supplySourceId, **kwargs) -> ApiResponse
        
        Archive a supply source, making it inactive. Cannot be undone.
        
        Examples:
            literal blocks::
            
                await SupplySources().archive_supply_source("value")
        
        Args:
            supplySourceId: object | required The unique identifier of a supply source.
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), supplySourceId), data=kwargs
        )

    @sp_endpoint("/supplySources/2020-07-01/supplySources/{}/status", method="PUT")
    async def update_supply_source_status(self, supplySourceId, **kwargs) -> ApiResponse:
        """
        update_supply_source_status(self, supplySourceId, **kwargs) -> ApiResponse
        
        Update the status of a supply source.
        
        Examples:
            literal blocks::
            
                await SupplySources().update_supply_source_status("value")
        
        Args:
            supplySourceId: object | required The unique identifier of a supply source.
            payload: UpdateSupplySourceStatusRequest |
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), supplySourceId), data=kwargs
        )