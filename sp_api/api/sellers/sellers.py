from sp_api.base.helpers import sp_endpoint
from sp_api.base import Client, Marketplaces, ApiResponse


class Sellers(Client):
    """
    :link: https://github.com/amzn/selling-partner-api-docs/blob/main/references/sellers-api/sellers.md

    """

    @sp_endpoint("/sellers/v1/marketplaceParticipations")
    def get_marketplace_participation(self, **kwargs) -> ApiResponse:
        """
        get_marketplace_participation(self, **kwargs) -> ApiResponse
        
        Returns a list of marketplaces where the seller can list items and information about the seller's participation in those marketplaces.
        
        Examples:
            literal blocks::
            
                Sellers().get_marketplace_participation()
        
        Args:
            **kwargs:
        
        Returns:
            ApiResponse
        """
        return self._request(kwargs.pop("path"), add_marketplace=False)

    @sp_endpoint("/sellers/v1/account")
    def get_account(self, **kwargs) -> ApiResponse:
        """
        get_account(self, **kwargs) -> ApiResponse
        
        Returns information about a seller account and its marketplaces.
        
        Examples:
            literal blocks::
            
                Sellers().get_account()
        
        Args:
            **kwargs:
        
        Returns:
            ApiResponse
        """
        return self._request(kwargs.pop("path"), add_marketplace=False)
