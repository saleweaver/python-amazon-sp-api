from sp_api.base import Client, sp_endpoint, fill_query_params, ApiResponse


class ExternalFulfillmentInventoryV20210106(Client):
    """
    External Fulfillment Inventory API (version 2021-01-06).
    """

    @sp_endpoint("/externalFulfillment/inventory/2021-01-06/locations/{}/skus/{}", method="GET")
    def get_inventory(self, locationId, skuId, **kwargs) -> ApiResponse:
        """
        get_inventory(self, locationId, skuId, **kwargs) -> ApiResponse
        
        Get the current inventory for a given SKU at a given location.
        
        Examples:
            literal blocks::
            
                ExternalFulfillmentInventoryV20210106().get_inventory("value", "value")
        
        Args:
            locationId:  | required
            skuId:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """
        return self._request(
            fill_query_params(kwargs.pop("path"), locationId, skuId),
            params=kwargs,
            headers=headers,
            add_marketplace=False,
        )

    @sp_endpoint("/externalFulfillment/inventory/2021-01-06/locations/{}/skus/{}", method="PUT")
    def update_inventory(self, locationId, skuId, quantity, **kwargs) -> ApiResponse:
        """
        update_inventory(self, locationId, skuId, quantity, **kwargs) -> ApiResponse
        
        Get the current inventory for a given SKU at a given location.
        
        Examples:
            literal blocks::
            
                ExternalFulfillmentInventoryV20210106().update_inventory("value", "value", "value")
        
        Args:
            locationId:  | required
            skuId:  | required
            quantity:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """
        kwargs["quantity"] = quantity

        headers = self.headers.copy()
        if "if_match" in kwargs:
            headers["If-Match"] = kwargs.pop("if_match")
        if "if_unmodified_since" in kwargs:
            headers["If-Unmodified-Since"] = kwargs.pop("if_unmodified_since")

        return self._request(
            fill_query_params(kwargs.pop("path"), locationId, skuId),
            params=kwargs,
            add_marketplace=False,
        )
