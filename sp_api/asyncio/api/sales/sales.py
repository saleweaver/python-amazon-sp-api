import urllib
from datetime import datetime

from sp_api.base import Client, Marketplaces, sp_endpoint, Granularity, ApiResponse
from sp_api.asyncio.base import AsyncBaseClient
import logging
from sp_api.util import encode_kwarg


class Sales(AsyncBaseClient):
    """
    :link: https://github.com/amzn/selling-partner-api-docs/blob/main/references/sales-api/sales.md#parameters
    """

    @sp_endpoint("/sales/v1/orderMetrics")
    async def get_order_metrics(
        self,
        interval: tuple,
        granularity: Granularity,
        granularityTimeZone: str = None,
        **kwargs
    ) -> ApiResponse:
        """
        get_order_metrics(self, interval, granularity, granularityTimeZone, **kwargs) -> ApiResponse
        
        Returns aggregated order metrics for given interval, broken down by granularity, for given buyer type.
        
        Examples:
            literal blocks::
            
                await Sales().get_order_metrics("value", "value", "value")
        
        Args:
            interval:  | required
            granularity:  | required
            granularityTimeZone:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """
        kwargs.update(
            {
                "interval": "--".join(
                    [self._create_datetime_stamp(_interval) for _interval in interval]
                ),
                "granularity": granularity.value,
            }
        )
        if granularityTimeZone:
            kwargs.update({"granularityTimeZone": granularityTimeZone})
        encode_kwarg(kwargs, "sku", lambda value: urllib.parse.quote(value, safe=""))
        return await self._request(kwargs.pop("path"), params=kwargs)

    @staticmethod
    def _create_datetime_stamp(datetime_obj: datetime or str):
        """
        _create_datetime_stamp(datetime_obj) -> ApiResponse
        
        Create datetimestring
        
        Examples:
            literal blocks::
            
                Sales()._create_datetime_stamp("value")
        
        Args:
            datetime_obj:  | required
        
        Returns:
            ApiResponse
        """
        if isinstance(datetime_obj, str):
            return datetime_obj
        fmt = "%Y-%m-%dT%H:%M:%S%z"
        return datetime_obj.astimezone().isoformat(timespec="seconds")
