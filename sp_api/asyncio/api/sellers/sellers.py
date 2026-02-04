from sp_api.base.helpers import sp_endpoint
from sp_api.base import Client, Marketplaces, ApiResponse
from sp_api.asyncio.base import AsyncBaseClient


class Sellers(AsyncBaseClient):
    """
    :link: https://github.com/amzn/selling-partner-api-docs/blob/main/references/sellers-api/sellers.md

    """

    @sp_endpoint("/sellers/v1/marketplaceParticipations")
    async def get_marketplace_participation(self, **kwargs) -> ApiResponse:
        """
        get_marketplace_participation(self, **kwargs) -> ApiResponse
        
        Returns a list of marketplaces where the seller can list items and information about the seller's participation in those marketplaces.
        
        Examples:
            literal blocks::
            
                await Sellers().get_marketplace_participation()
        
        Args:
            **kwargs:
        
        Returns:
            ApiResponse
        """
        return await self._request(kwargs.pop("path"), add_marketplace=False)

    @sp_endpoint("/sellers/v1/account")
    async def get_account(self, **kwargs) -> ApiResponse:
        """
        get_account(self, **kwargs) -> ApiResponse
        
        Returns information about a seller account and its marketplaces.
        
        Examples:
            literal blocks::
            
                await Sellers().get_account()
        
        Args:
            **kwargs:
        
        Returns:
            ApiResponse
        """
        return await self._request(kwargs.pop("path"), add_marketplace=False)
