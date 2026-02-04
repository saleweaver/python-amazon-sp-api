import urllib

from sp_api.base import Client, Marketplaces, sp_endpoint, ApiResponse, fill_query_params
from sp_api.base.InventoryEnums import InventoryGranularity
from sp_api.util import normalize_csv_param


class Inventories(Client):
    """
    :link: https://github.com/amzn/selling-partner-api-docs/blob/main/references/fba-inventory-api/fbaInventory.md#getinventorysummaries
    """

    @sp_endpoint("/fba/inventory/v1/summaries")
    def get_inventory_summary_marketplace(self, **kwargs) -> ApiResponse:
        """
        get_inventory_summary_marketplace(self, **kwargs) -> ApiResponse
        
        Returns a list of inventory summaries. The summaries returned depend on the presence or absence of the startDateTime, sellerSkus and sellerSku parameters:
                        - All inventory summaries with available details are returned when the startDateTime, sellerSkus and sellerSku parameters are omitted.
                        - When startDateTime is provided, the operation returns inventory summaries that have had changes after the date and time specified. The sellerSkus and sellerSku parameters are ignored. Important: To avoid errors, use both startDateTime and nextToken to get the next page of inventory summaries that have changed after the date and time specified.
                        - When the sellerSkus parameter is provided, the operation returns inventory summaries for only the specified sellerSkus. The sellerSku parameter is ignored.
                        - When the sellerSku parameter is provided, the operation returns inventory summaries for only the specified sellerSku.
                        Note: The parameters associated with this operation may contain special characters that must be encoded to successfully call the API. To avoid errors with SKUs when encoding URLs, refer to [URL Encoding](https://developer-docs.amazon.com/sp-api/docs/url-encoding).
        
        Examples:
            literal blocks::
            
                Inventories().get_inventory_summary_marketplace()
        
        Args:
            **kwargs:
        
        Returns:
            ApiResponse
        """

        kwargs.update(
            {
                "granularityType": kwargs.get(
                    "granularityType", InventoryGranularity.MARKETPLACE.value
                ),
                "granularityId": kwargs.get("granularityId", self.marketplace_id),
            }
        )
        normalize_csv_param(kwargs, "sellerSkus")

        return self._request(kwargs.pop("path"), params=kwargs)


    @sp_endpoint("/fba/inventory/v1/items", method="POST")
    def create_inventory_item(self, **kwargs) -> ApiResponse:
        """
        create_inventory_item(self, **kwargs) -> ApiResponse
        
        Requests that Amazon create product-details in the Sandbox Inventory in the sandbox environment. This is a sandbox-only operation and must be directed to a sandbox endpoint. Refer to [Selling Partner API sandbox](https://developer-docs.amazon.com/sp-api/docs/the-selling-partner-api-sandbox) for more information.
        
        Examples:
            literal blocks::
            
                Inventories().create_inventory_item()
        
        Args:
            createInventoryItemRequestBody: CreateInventoryItemRequest | required CreateInventoryItem Request Body Parameter.
        
        Returns:
            ApiResponse
        """
        return self._request(kwargs.pop("path"), data=kwargs)

    @sp_endpoint("/fba/inventory/v1/items/{}", method="DELETE")
    def delete_inventory_item(self, sellerSku, **kwargs) -> ApiResponse:
        """
        delete_inventory_item(self, sellerSku, **kwargs) -> ApiResponse
        
        Requests that Amazon Deletes an item from the Sandbox Inventory in the sandbox environment. This is a sandbox-only operation and must be directed to a sandbox endpoint. Refer to [Selling Partner API sandbox](https://developer-docs.amazon.com/sp-api/docs/the-selling-partner-api-sandbox) for more information.
        
        Examples:
            literal blocks::
            
                Inventories().delete_inventory_item("value")
        
        Args:
            sellerSku: object | required A single seller SKU used for querying the specified seller SKU inventory summaries.
            key marketplaceId: object | required The marketplace ID for the marketplace for which the sellerSku is to be deleted.
        
        Returns:
            ApiResponse
        """
        return self._request(fill_query_params(kwargs.pop("path"), sellerSku), params=kwargs)

    @sp_endpoint("/fba/inventory/v1/items/inventory", method="POST")
    def add_inventory(self, **kwargs) -> ApiResponse:
        """
        add_inventory(self, **kwargs) -> ApiResponse
        
        Requests that Amazon add items to the Sandbox Inventory with desired amount of quantity in the sandbox environment. This is a sandbox-only operation and must be directed to a sandbox endpoint. Refer to [Selling Partner API sandbox](https://developer-docs.amazon.com/sp-api/docs/the-selling-partner-api-sandbox) for more information.
        
        Examples:
            literal blocks::
            
                Inventories().add_inventory()
        
        Args:
            x-amzn-idempotency-token: object | required A unique token/requestId provided with each call to ensure idempotency.
            addInventoryRequestBody: AddInventoryRequest | required List of items to add to Sandbox inventory.
        
        Returns:
            ApiResponse
        """
        return self._request(kwargs.pop("path"), data=kwargs)
