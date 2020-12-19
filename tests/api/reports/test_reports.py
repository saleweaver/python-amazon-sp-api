from datetime import datetime, timedelta

from sp_api.api import Reports, Orders
from sp_api.api.reports.models.create_report_specification import CreateReportSpecification
from sp_api.base import Marketplaces


def test_create_report():
    print(Orders().get_orders(CreatedAfter=(datetime.now() - timedelta(days=2)).isoformat()))
    print(Reports().create_report(reportType='GET_FLAT_FILE_OPEN_LISTINGS_DATA'))
