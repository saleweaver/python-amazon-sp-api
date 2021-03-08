import urllib
from datetime import datetime

from sp_api.base import Client, Marketplaces, sp_endpoint, Granularity, ApiResponse
import logging


class Sales(Client):
    """
    :link: https://github.com/amzn/selling-partner-api-docs/blob/main/references/sales-api/sales.md#parameters
    """

    @sp_endpoint('/sales/v1/orderMetrics')
    def get_order_metrics(self, interval: tuple, granularity: Granularity, granularityTimeZone: str = None, **kwargs) -> ApiResponse:
        """
        get_order_metrics(self, interval: tuple, granularity: Granularity, granularityTimeZone: str = None, **kwargs) -> ApiResponse

        Returns aggregated order metrics for given interval, broken down by granularity, for given buyer type.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | .5 | 15 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Type	Name	Description	Schema	Default
        Query	marketplaceIds
        required

        A list of marketplace identifiers. Example: ATVPDKIKX0DER indicates the US marketplace.	< string > array	-

        Query	interval
        required

        A time interval used for selecting order metrics.
        This takes the form of two dates separated by two hyphens (first date is inclusive; second date is exclusive).
        Dates are in ISO8601 format and must represent absolute time (either Z notation or offset notation).
        Example: 2018-09-01T00:00:00-07:00--2018-09-04T00:00:00-07:00 requests order metrics for Sept 1st, 2nd and 3rd in the -07:00 zone.	string	-

        Query	granularityTimeZone
        optional

        An IANA-compatible time zone for determining the day boundary.
        !! Required when specifying a granularity value greater than Hour. !!
        The granularityTimeZone value must align with the offset of the specified interval value.
        For example, if the interval value uses Z notation, then granularityTimeZone must be UTC.
        If the interval value uses an offset, then granularityTimeZone must be an IANA-compatible time zone that matches the offset.
        Example: US/Pacific to compute day boundaries, accounting for daylight time savings, for US/Pacific zone.	string	-

        Query	granularity
        required

        The granularity of the grouping of order metrics, based on a unit of time.
        Specifying granularity=Hour results in a successful request only if the interval specified is less than or equal to 30 days from now.
        For all other granularities, the interval specified must be less or equal to 2 years from now.
        Specifying granularity=Total results in order metrics that are aggregated over the entire interval that you specify.
        If the interval start and end date don’t align with the specified granularity, the head and tail end of the response interval will contain partial data.
        Example: Day to get a daily breakdown of the request interval, where the day boundary is defined by the granularityTimeZone.	enum (Granularity)	-

        Query	buyerType
        optional

        Filters the results by the buyer type that you specify, B2B (business to business) or B2C (business to customer).
        Example: B2B, if you want the response to include order metrics for only B2B buyers.
        Default: enum (BuyerType)	"All"

        Query	fulfillmentNetwork
        optional

        Filters the results by the fulfillment network that you specify,
        MFN (merchant fulfillment network) or AFN (Amazon fulfillment network).
        Do not include this filter if you want the response to include order metrics for all fulfillment networks.
        Example: AFN, if you want the response to include order metrics for only Amazon fulfillment network.	string -

        Query	firstDayOfWeek
        optional

        Specifies the day that the week starts on when granularity=Week, either Monday or Sunday.
        Default: Monday.
        Example: Sunday, if you want the week to start on a Sunday.	enum (FirstDayOfWeek)	"Monday"

        Query	asin
        optional

        Filters the results by the ASIN that you specify. Specifying both ASIN and SKU returns an error.
        Do not include this filter if you want the response to include order metrics for all ASINs.
        Example: B0792R1RSN, if you want the response to include order metrics for only ASIN B0792R1RSN.	string	-

        Query	sku
        optional

        Filters the results by the SKU that you specify.
        Specifying both ASIN and SKU returns an error.
        Do not include this filter if you want the response to include order metrics for all SKUs. Example: TestSKU, if you want the response to include order metrics for only SKU TestSKU.

        :param interval:
        :param granularityTimeZone:
        :param granularity:
        :param kwargs:

        :return: ApiResponse

        """
        kwargs.update({
            'interval': '--'.join([self._create_datetime_stamp(_interval) for _interval in interval]),
            'granularity': granularity.value,
        })
        if granularityTimeZone:
            kwargs.update({'granularityTimeZone': granularityTimeZone})
        if 'sku' in kwargs:
            kwargs.update({'sku': urllib.parse.quote_plus(kwargs.pop('sku'))})
        return self._request(kwargs.pop('path'), params=kwargs)

    @staticmethod
    def _create_datetime_stamp(datetime_obj: datetime or str):
        """
        Create datetimestring

        Args:
            datetime_obj:

        Returns:

        """
        if isinstance(datetime_obj, str):
            return datetime_obj
        fmt = '%Y-%m-%dT%H:%M:%S%z'
        return datetime_obj.strftime(fmt)[:-2] + ':00'
