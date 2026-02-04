import urllib.parse

from sp_api.base import Client, sp_endpoint, fill_query_params, ApiResponse


class VendorDirectFulfillmentInventory(Client):
    """
    VendorDirectFulfillmentInventory SP-API Client
    :link:

    The Selling Partner API for Direct Fulfillment Inventory Updates provides programmatic access to a direct fulfillment vendor's inventory updates.
    """

    @sp_endpoint(
        "/vendor/directFulfillment/inventory/v1/warehouses/{}/items", method="POST"
    )
    def submit_inventory_update(self, warehouseId, **kwargs) -> ApiResponse:
        """
        submit_inventory_update(self, warehouseId, **kwargs) -> ApiResponse
        
        Submits inventory updates for the specified warehouse for either a partial or full feed of inventory items.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        10                                      10
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                VendorDirectFulfillmentInventory().submit_inventory_update("value")
        
        Args:
            body: SubmitInventoryUpdateRequest | required The request body containing the inventory update data to submit.
            warehouseId: object | required Identifier for the warehouse for which to update inventory.
        
        Returns:
            ApiResponse
        """

        return self._request(
            fill_query_params(kwargs.pop("path"), warehouseId),
            data=kwargs,
            add_marketplace=False,
        )
