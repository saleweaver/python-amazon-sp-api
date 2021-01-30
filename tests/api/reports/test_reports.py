from sp_api.api import Reports
from sp_api.base import Marketplaces, Schedules


def test_create_report():
    res = Reports().create_report(
        reportType='GET_MERCHANT_LISTINGS_ALL_DATA',
        dataStartTime='2019-12-10T20:11:24.000Z',
        marketplaceIds=[
            "A1PA6795UKMFR9",
            "ATVPDKIKX0DER"
        ])
    assert res.payload.get('reportId') == 'ID323'


def test_get_report():
    res = Reports().get_report('ID323')
    assert res.payload.get('reportId') == 'ReportId1'
    assert res.payload.get('reportType') == 'FEE_DISCOUNTS_REPORT'


def test_get_report_document_n_decrypt():
    res = Reports().get_report_document('0356cf79-b8b0-4226-b4b9-0ee058ea5760', decrypt=False)
    assert res.errors is None
    assert 'document' not in res.payload


def test_create_report_schedule():
    res = Reports().create_report_schedule(reportType='FEE_DISCOUNTS_REPORT',
                                           period=Schedules.MINUTES_5.value,
                                           nextReportCreationTime="2019-12-10T20:11:24.000Z",
                                           marketplaceIds=["A1PA6795UKMFR9", "ATVPDKIKX0DER"])
    assert res.errors is None
    assert 'reportScheduleId' in res.payload


def test_delete_schedule_by_id():
    res = Reports().delete_report_schedule('ID')
    assert res.errors is None


def test_get_schedule_by_id():
    res = Reports().get_report_schedule('ID323')
    assert res.errors is None
    assert 'period' in res.payload
    assert res.payload.get('reportType') == 'FEE_DISCOUNTS_REPORT'
