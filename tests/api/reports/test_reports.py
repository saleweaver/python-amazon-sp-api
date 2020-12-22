from datetime import datetime, timedelta

from sp_api.api import Reports, Orders
from sp_api.api.reports.models.create_report_specification import CreateReportSpecification
from sp_api.base import Marketplaces, Schedules


def test_create_report():
    print(Reports().create_report(reportType='GET_FBA_ESTIMATED_FBA_FEES_TXT_DATA'))


def test_get_report():
    print(Reports().get_report('597294018618'))


def test_get_report_document_w_decrypt():
    res = Reports().get_report_document('as',
                                        decrypt=True)
    print(res)
    assert 'document' in res.payload


def test_get_report_document_n_decrypt():
    res = Reports().get_report_document('as',
                                        decrypt=False)
    print(res)
    assert 'document' not in res.payload


def test_create_report_schedule():
    res = Reports().create_report_schedule(reportType='GET_FLAT_FILE_OPEN_LISTINGS_DATA', period=Schedules.HOURS_8.value)
    print(res)
    assert res.errors is None
    assert 'reportScheduleId' in res.payload


def test_delete_schedule_by_id():
    res = Reports().delete_report_schedule('5000d4018615')
    print(res)
    assert res.errors is None


def test_get_schedule_by_id_existing_schedule():
    res = Reports().get_report_schedule('5000401d8615')
    print(res)
    assert res.errors is None
