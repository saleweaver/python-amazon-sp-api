from sp_api.base import ApiResponse, sp_endpoint, fill_query_params
from sp_api.asyncio.base import AsyncBaseClient


class VehiclesV20241101(AsyncBaseClient):
    """
    Vehicles SP-API Client
    :link:

    The Selling Partner API for Automotive provides programmatic access to information needed by selling partners to provide compatibility information about their listed products.
    """

    @sp_endpoint("/catalog/2024-11-01/automotive/vehicles", method="GET")
    async def get_vehicles(self, **kwargs) -> ApiResponse:
        """
        get_vehicles(self, **kwargs) -> ApiResponse
        
        Get the latest collection of vehicles
        
        Examples:
            literal blocks::
            
                await VehiclesV20241101().get_vehicles()
        
        Args:
            key pageToken: object |  A token to fetch a certain page when there are multiple pages worth of results.
            key marketplaceId: object | required An identifier for the marketplace in which the resource operates.
            key vehicleType: object | required An identifier for vehicle type.
            key updatedAfter: object |  Date in ISO 8601 format, if provided only vehicles which are modified/added to Amazon's catalog after this date will be returned.
        
        Returns:
            ApiResponse
        """
        return await self._request(kwargs.pop("path"), params=kwargs, add_marketplace=False)
