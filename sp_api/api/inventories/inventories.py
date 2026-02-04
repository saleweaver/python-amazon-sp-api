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
        get_inventory_summary_marketplace(self, **kwargs) -> GetInventorySummariesResponse


        Returns a list of inventory summaries. The summaries returned depend on the presence or absence of the startDateTime and sellerSkus parameters:

        - All inventory summaries with available details are returned when the startDateTime and sellerSkus parameters are omitted.
        - When startDateTime is provided, the operation returns inventory summaries that have had changes after the date and time specified. The sellerSkus parameter is ignored.
        - When the sellerSkus parameter is provided, the operation returns inventory summaries for only the specified sellerSkus.

        **Usage Plan:**

        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        2                                       2
        ======================================  ==============


        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        All inventory summaries with available details are returned when the startDateTime and sellerSkus parameters are omitted.
        When startDateTime is provided, the operation returns inventory summaries that have had changes after the date and time specified. The sellerSkus parameter is ignored.
        When the sellerSkus parameter is provided, the operation returns inventory summaries for only the specified sellerSkus.
        Usage Plan:

        Examples:
            literal blocks::

                Inventories().get_inventory_summary_marketplace(**{
                        "details": True,
                        "marketplaceIds": ["ATVPDKIKX0DER"]
                    })

        Args:
            key details: bool | true to return inventory summaries with additional summarized inventory details and quantities. Otherwise, returns inventory summaries only (default value).	boolean	"false"
            key granularityType: Granularity Type | The granularity type for the inventory aggregation level.	enum (GranularityType)	-
            key granularityId: str The granularity ID for the inventory aggregation level.	string	-
            key startDateTime: datetime | A start date and time in ISO8601 format. If specified, all inventory summaries that have changed since then are returned. You must specify a date and time that is no earlier than 18 months prior to the date and time when you call the API. Note: Changes in inboundWorkingQuantity, inboundShippedQuantity and inboundReceivingQuantity are not detected.	string (date-time)	-
            key sellerSkus: [str] | A list of seller SKUs for which to return inventory summaries. You may specify up to 50 SKUs.
            key nextToken: str | String token returned in the response of your previous request.	string	-
            key marketplaceIds: str | The marketplace ID for the marketplace for which to return inventory summaries.

        Returns:
            GetInventorySummariesResponse:

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

        Args:
            createInventoryItemRequestBody:CreateInventoryItemRequest | * REQUIRED {'description': 'An item to be created in the inventory.',
             'properties': {'marketplaceId': {'description': 'The marketplaceId.', 'type': 'string'}, 'productName': {'description': 'The name of the item.', 'type': 'string'}, 'sellerSku': {'description': 'The seller SKU of the item.', 'type': 'string'}},
             'required': ['sellerSku', 'marketplaceId', 'productName'],
             'type': 'object'}

        Returns:
            ApiResponse:
        """
        return self._request(kwargs.pop("path"), data=kwargs)

    @sp_endpoint("/fba/inventory/v1/items/{}", method="DELETE")
    def delete_inventory_item(self, sellerSku, **kwargs) -> ApiResponse:
        """
        delete_inventory_item(self, sellerSku, **kwargs) -> ApiResponse

        Requests that Amazon Deletes an item from the Sandbox Inventory in the sandbox environment. This is a sandbox-only operation and must be directed to a sandbox endpoint. Refer to [Selling Partner API sandbox](https://developer-docs.amazon.com/sp-api/docs/the-selling-partner-api-sandbox) for more information.

        Args:
            sellerSku:string | * REQUIRED A single seller SKU used for querying the specified seller SKU inventory summaries.
            key marketplaceId:string | * REQUIRED The marketplace ID for the marketplace for which the sellerSku is to be deleted.

        Returns:
            ApiResponse:
        """
        return self._request(fill_query_params(kwargs.pop("path"), sellerSku), params=kwargs)

    @sp_endpoint("/fba/inventory/v1/items/inventory", method="POST")
    def add_inventory(self, **kwargs) -> ApiResponse:
        """
        add_inventory(self, **kwargs) -> ApiResponse

        Requests that Amazon add items to the Sandbox Inventory with desired amount of quantity in the sandbox environment. This is a sandbox-only operation and must be directed to a sandbox endpoint. Refer to [Selling Partner API sandbox](https://developer-docs.amazon.com/sp-api/docs/the-selling-partner-api-sandbox) for more information.

        Args:
            x-amzn-idempotency-token:string | * REQUIRED A unique token/requestId provided with each call to ensure idempotency.
            addInventoryRequestBody:AddInventoryRequest | * REQUIRED {'description': 'The object with the list of Inventory to be added', 'properties': {'inventoryItems': {'$ref': '#/definitions/InventoryItems'}}, 'type': 'object'}

        Returns:
            ApiResponse:
        """
        return self._request(kwargs.pop("path"), data=kwargs)
