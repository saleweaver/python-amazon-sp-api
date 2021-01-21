from sp_api.api import Reports
from sp_api.base import Marketplaces, Schedules


def test_create_report():
    print(Reports(marketplace=Marketplaces.DE).create_report(reportType='GET_MERCHANT_LISTINGS_ALL_DATA'))


def test_get_report():
    print(Reports(marketplace=Marketplaces.DE).get_report('50632018648'))


def test_get_report_document_w_decrypt():
    res = Reports(marketplace=Marketplaces.DE).get_report_document('',
                                        decrypt=True, file=open('output.tsv', 'w+'))
    print(res)
    assert 'document' in res.payload


def test_get_report_document_n_decrypt():
    res = Reports().get_report_document('as', decrypt=False)
    print(res)
    assert 'document' not in res.payload


def test_create_report_schedule():
    res = Reports().create_report_schedule(reportType='GET_FLAT_FILE_OPEN_LISTINGS_DATA', period=Schedules.HOURS_8.value)
    assert res.errors is None
    assert 'reportScheduleId' in res.payload


def test_delete_schedule_by_id():
    res = Reports().delete_report_schedule('')
    print(res)
    assert res.errors is None


def test_get_schedule_by_id_existing_schedule():
    res = Reports().get_report_schedule('')
    print(res)
    assert res.errors is None


