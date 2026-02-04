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

        **Usage Plan:**

        ======================================
        Rate (requests per second)
        ======================================
        5
        ======================================

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            locationId:string | * REQUIRED The node identifier for the seller's location in smart connect for which inventory is being updated
            skuId:string | * REQUIRED The seller's identifier for the SKU for which inventory is being updated

        Returns:
            ApiResponse:
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

        **Usage Plan:**

        ======================================
        Rate (requests per second)
        ======================================
        5
        ======================================

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            locationId:string | * REQUIRED The node identifier for the seller's location in smart connect for which inventory is being updated
            skuId:string | * REQUIRED The seller's identifier for the SKU for which inventory is being updated
            quantity:integer | * REQUIRED The absolute number of items of the specified SKU available at the specified node. This value should always be a non-zero or zero positive integer
            key if_match:string | A unique number provided with each call to update the inventory. This number must be latest version of entity that exist in system. It will be equal to comparison against existing version of entity.
            key if_unmodified_since:string | Timestamp or increasing number which does greater than comparison before applying the change. This is different than version of entity and used to overwrite the latest data. It should follow data/time format of rfc2616

        Returns:
            ApiResponse:
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
