from sp_api.api.inventories.models.get_inventory_summaries_response import GetInventorySummariesResponse
from sp_api.base import Client, Marketplaces, sp_endpoint
from sp_api.base.InventoryEnums import InventoryGranularity


class Inventories(Client):
    def __init__(self, marketplace=Marketplaces.US, *, refresh_token=None, account='default', credentials=None):
        super().__init__(marketplace, refresh_token, account, credentials)

    @sp_endpoint('/fba/inventory/v1/summaries')
    def get_inventory_summary_marketplace(self, **kwargs):
        """
        DOC:https://github.com/amzn/selling-partner-api-docs/blob/main/references/fba-inventory-api/fbaInventory.md#getinventorysummaries

        Description
            Returns a list of inventory summaries. The summaries returned depend on the presence or absence of the startDateTime and sellerSkus parameters:

            All inventory summaries with available details are returned when the startDateTime and sellerSkus parameters are omitted.
            When startDateTime is provided, the operation returns inventory summaries that have had changes after the date and time specified. The sellerSkus parameter is ignored.
            When the sellerSkus parameter is provided, the operation returns inventory summaries for only the specified sellerSkus.
            Usage Plan:

            Parameters
            Type	Name	Description	Schema	Default
            Query	details
            optional	true to return inventory summaries with additional summarized inventory details and quantities. Otherwise, returns inventory summaries only (default value).	boolean	"false"
            Query	granularityType
            required	The granularity type for the inventory aggregation level.	enum (GranularityType)	-
            Query	granularityId
            required	The granularity ID for the inventory aggregation level.	string	-
            Query	startDateTime
            optional	A start date and time in ISO8601 format. If specified, all inventory summaries that have changed since then are returned. You must specify a date and time that is no earlier than 18 months prior to the date and time when you call the API. Note: Changes in inboundWorkingQuantity, inboundShippedQuantity and inboundReceivingQuantity are not detected.	string (date-time)	-
            Query	sellerSkus
            optional	A list of seller SKUs for which to return inventory summaries. You may specify up to 50 SKUs.
            Max count : 50	< string > array	-
            Query	nextToken
            optional	String token returned in the response of your previous request.	string	-
            Query	marketplaceIds
            required	The marketplace ID for the marketplace for which to return inventory summaries.
            Max count : 1	< string > array
        """

        kwargs.update({
            'granularityType': InventoryGranularity.MARKETPLACE.value,
            "granularityId": self.marketplace_id
        })

        return GetInventorySummariesResponse(**self._request(kwargs.pop('path'), params=kwargs).json())
