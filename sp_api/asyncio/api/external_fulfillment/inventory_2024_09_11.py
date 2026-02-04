from sp_api.base import sp_endpoint, fill_query_params, ApiResponse
from sp_api.asyncio.base import AsyncBaseClient


class ExternalFulfillmentInventoryV20240911(AsyncBaseClient):
    """
    External Fulfillment Inventory API (version 2024-09-11).
    """

    @sp_endpoint("/externalFulfillment/inventory/2024-09-11/locations/{}/skus/{}", method="GET")
    async def get_inventory(self, locationId, skuId, **kwargs) -> ApiResponse:
        """
        get_inventory(self, locationId, skuId, **kwargs) -> ApiResponse
        
        Get the current inventory for a given SKU at a given location.
        
        Examples:
            literal blocks::
            
                await ExternalFulfillmentInventoryV20240911().get_inventory("value", "value")
        
        Args:
            locationId:  | required
            skuId:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """
        headers = await self._get_headers()
        return await self._request(
            fill_query_params(kwargs.pop("path"), locationId, skuId),
            params=kwargs,
            headers=headers,
            add_marketplace=False,
        )


    @sp_endpoint("/externalFulfillment/inventory/2024-09-11/locations/{}/skus/{}", method="PUT")
    async def update_inventory(self, locationId, skuId, quantity, **kwargs) -> ApiResponse:
        """
        update_inventory(self, locationId, skuId, quantity, **kwargs) -> ApiResponse
        
        Get the current inventory for a given SKU at a given location.
        
        Examples:
            literal blocks::
            
                await ExternalFulfillmentInventoryV20240911().update_inventory("value", "value", "value")
        
        Args:
            locationId:  | required
            skuId:  | required
            quantity:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """
        kwargs["quantity"] = quantity

        headers = await self._get_headers()
        if "if_match" in kwargs:
            headers["If-Match"] = kwargs.pop("if_match")
        if "if_unmodified_since" in kwargs:
            headers["If-Unmodified-Since"] = kwargs.pop("if_unmodified_since")

        return await self._request(
            fill_query_params(kwargs.pop("path"), locationId, skuId),
            params=kwargs,
            headers=headers,
            add_marketplace=False,
        )

    @sp_endpoint("/externalFulfillment/inventory/2024-09-11/inventories", method="POST")
    async def batch_inventory(self, **kwargs) -> ApiResponse:
        """
        batch_inventory(self, **kwargs) -> ApiResponse
        
        Make up to 10 inventory requests. The response includes the set of responses that correspond to requests. The response for each successful request in the set includes the  inventory count for the provided `sku` and `locationId` pair.
        
        Examples:
            literal blocks::
            
                await ExternalFulfillmentInventoryV20240911().batch_inventory()
        
        Args:
            body: BatchInventoryRequest | required A list of inventory requests.
        
        Returns:
            ApiResponse
        """

        return await self._request(
            kwargs.pop("path"),
            data=kwargs,
            add_marketplace=False,
        )
