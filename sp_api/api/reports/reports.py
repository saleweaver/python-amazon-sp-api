from sp_api.api.reports.models.create_report_response import CreateReportResponse
from sp_api.base import sp_endpoint, fill_query_params
from sp_api.api.orders.models.get_order_items_response import GetOrderItemsResponse
from sp_api.api.orders.models.get_order_response import GetOrderResponse
from sp_api.api.orders.models.get_orders_response import GetOrdersResponse
from sp_api.base import Client, Marketplaces


class Reports(Client):
    def __init__(self, marketplace=Marketplaces.US, refresh_token=None):
        super().__init__(marketplace, refresh_token)

    @sp_endpoint('/reports/2020-09-04/reports', method='POST')
    def create_report(self, **kwargs):
        """
        Creates a report.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0167 | 15 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        :param kwargs:
        :return:
        """
        return CreateReportResponse(
            **self._request(kwargs.pop('path'), data={**kwargs}).json()
        )
