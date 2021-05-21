import urllib.parse

from sp_api.base import Client, sp_endpoint, fill_query_params, ApiResponse


class VendorDirectFulfillmentInventory(Client):
    """
    VendorDirectFulfillmentInventory SP-API Client
    :link: 

    The Selling Partner API for Direct Fulfillment Inventory Updates provides programmatic access to a direct fulfillment vendor's inventory updates.
    """


    @sp_endpoint('/vendor/directFulfillment/inventory/v1/warehouses/{}/items', method='POST')
    def submit_inventory_update(self, warehouseId, **kwargs) -> ApiResponse:
        """
        submit_inventory_update(self, warehouseId, **kwargs) -> ApiResponse

        Submits inventory updates for the specified warehouse for either a partial or full feed of inventory items.

**Usage Plans:**

| Plan type | Rate (requests per second) | Burst |
| ---- | ---- | ---- |
|Default| 10 | 10 |
|Selling partner specific| Variable | Variable |

The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

         Args:
        
            body: | * REQUIRED {'description': 'The request body for the submitInventoryUpdate operation.',
 'properties': {'inventory': {'$ref': '#/definitions/InventoryUpdate', 'description': 'Inventory details required to update some or all items for the requested warehouse.'}},
 'type': 'object'}
        
            warehouseId:string | * REQUIRED Identifier for the warehouse for which to update inventory.
        

         Returns:
            ApiResponse:
        """
    
        return self._request(fill_query_params(kwargs.pop('path'), warehouseId), data=kwargs)
    
