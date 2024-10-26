import enum
import urllib.parse

from sp_api.base import Client, sp_endpoint, fill_query_params, ApiResponse


class AmazonWarehousingAndDistributionVersion(str, enum.Enum):
    V_2024_05_09 = "2024-05-09"
    LATEST = "2024-05-09"


class AmazonWarehousingAndDistribution(Client):
    """
    AmazonWarehousingAndDistribu SP-API Client
    :link: 

    The Selling Partner API for Amazon Warehousing and Distribution (AWD).
    """

    version: AmazonWarehousingAndDistributionVersion = AmazonWarehousingAndDistributionVersion.V_2024_05_09

    def __init__(self, *args, **kwargs):
        if 'version' in kwargs:
            self.version = kwargs.get('version', AmazonWarehousingAndDistributionVersion.V_2024_05_09)
        super().__init__(*args, **{**kwargs, 'version': self.version})

    @sp_endpoint('/awd/<version>/inboundShipments/{}', method='GET')
    def get_inbound_shipment(self, shipmentId, **kwargs) -> ApiResponse:
        """
        get_inbound_shipment(self, shipmentId, **kwargs) -> ApiResponse

        Retrieves an AWD inbound shipment.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 2 | 2 |

The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api)

        Args:
        
            shipmentId:string | * REQUIRED ID for the shipment. A shipment contains the cases being inbounded.
        

        Returns:
            ApiResponse:
        """

        return self._request(fill_query_params(kwargs.pop('path'), shipmentId), params=kwargs)

    @sp_endpoint('/awd/<version>/inboundShipments', method='GET')
    def list_inbound_shipments(self, **kwargs) -> ApiResponse:
        """
        list_inbound_shipments(self, **kwargs) -> ApiResponse

        Retrieves a summary for all the inbound AWD shipments associated with a merchant, with the ability to apply optional filters.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 1 | 1 |

The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:
        
            key sortBy:string |  Field to sort results by. Required if `sortOrder` is provided.
        
            key sortOrder:string |  Sort the response in `ASCENDING` or `DESCENDING` order.
        
            key shipmentStatus:string |  Filter by inbound shipment status.
        
            key updatedAfter:string |  List the inbound shipments that were updated after a certain time (inclusive). The date must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format.
        
            key updatedBefore:string |  List the inbound shipments that were updated before a certain time (inclusive). The date must be in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> format.
        
            key maxResults:integer |  Maximum number of results to return.
        
            key nextToken:string |  Token to retrieve the next set of paginated results.
        

        Returns:
            ApiResponse:
        """

        return self._request(kwargs.pop('path'), params=kwargs)

    @sp_endpoint('/awd/<version>/inventory', method='GET')
    def list_inventory(self, **kwargs) -> ApiResponse:
        """
        list_inventory(self, **kwargs) -> ApiResponse

        Lists AWD inventory associated with a merchant with the ability to apply optional filters.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 2 | 2 |

The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:
        
            key sku:string |  Filter by seller or merchant SKU for the item.
        
            key sortOrder:string |  Sort the response in `ASCENDING` or `DESCENDING` order.
        
            key details:string |  Set to `SHOW` to return summaries with additional inventory details. Defaults to `HIDE,` which returns only inventory summary totals.
        
            key nextToken:string |  Token to retrieve the next set of paginated results.
        
            key maxResults:integer |  Maximum number of results to return.
        

        Returns:
            ApiResponse:
        """

        return self._request(kwargs.pop('path'), params=kwargs)
