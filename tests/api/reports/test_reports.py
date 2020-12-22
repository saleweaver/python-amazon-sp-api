from datetime import datetime, timedelta

from sp_api.api import Reports, Orders
from sp_api.api.reports.models.create_report_specification import CreateReportSpecification
from sp_api.base import Marketplaces, Schedules


def test_create_report():
    print(Reports().create_report(reportType='GET_REFERRAL_FEE_PREVIEW_REPORT'))


def test_get_report():
    print(Reports().get_report('595273018615'))


def test_get_report_document_w_decrypt():
    res = Reports().get_report_document('amzn1.tortuga.3.ab8cfb77-d791-4ecf-a2f5-b13cdbb9d502.T1N111ABCO06IT',
                                        decrypt=False)
    print(res)
    assert 'document' in res.payload


def test_get_report_document_n_decrypt():
    res = Reports().get_report_document('amzn1.tortuga.3.ab8cfb77-d791-4ecf-a2f5-b13cdbb9d502.T1N111ABCO06IT',
                                        decrypt=False)
    print(res)
    assert 'document' not in res.payload


def test_create_report_schedule():
    res = Reports().create_report_schedule(reportType='GET_FLAT_FILE_OPEN_LISTINGS_DATA', period=Schedules.HOURS_8.value)
    print(res)
    assert res.errors is None
    assert 'reportScheduleId' in res.payload


def test_delete_schedule_by_id():
    res = Reports().delete_report_schedule('50004018615')
    print(res)
    assert res.errors is None


def test_get_schedule_by_id_existing_schedule():
    res = Reports().get_report_schedule('50004018615')
    print(res)
    assert res.errors is None
