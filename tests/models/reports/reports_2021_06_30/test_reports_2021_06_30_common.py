# Auto-generated tests for sp_api.api.models.reports.reports_2021_06_30.common.py
from datetime import datetime

import pytest
from sp_api.api.models.reports.reports_2021_06_30.common import (
    CancelReportRequest, CancelReportScheduleRequest, CompressionAlgorithmEnum,
    CreateReportRequest, CreateReportResponse, CreateReportScheduleRequest,
    CreateReportScheduleResponse, CreateReportScheduleSpecification,
    CreateReportSpecification, Error, ErrorList, GetReportDocumentRequest,
    GetReportRequest, GetReportScheduleRequest, GetReportSchedulesRequest,
    GetReportsRequest, GetReportsResponse, GetRequestSerializer, PeriodEnum,
    ProcessingStatusEnum, ProcessingStatusesEnum, Report, ReportDocument,
    ReportOptions, ReportSchedule, ReportScheduleList, RequestsBaseModel,
    SpApiBaseModel)


def test_requestsbasemodel_instantiates():
    """Instantiate RequestsBaseModel with dummy data"""
    kwargs = {}
    obj = RequestsBaseModel(**kwargs)
    assert isinstance(obj, RequestsBaseModel)


def test_spapibasemodel_instantiates():
    """Instantiate SpApiBaseModel with dummy data"""
    kwargs = {}
    obj = SpApiBaseModel(**kwargs)
    assert isinstance(obj, SpApiBaseModel)


def test_getrequestserializer_instantiates():
    """Instantiate GetRequestSerializer with dummy data"""
    kwargs = {}
    obj = GetRequestSerializer(**kwargs)
    assert isinstance(obj, GetRequestSerializer)


def test_cancelreportrequest_instantiates():
    """Instantiate CancelReportRequest with dummy data"""
    kwargs = {
        "report_id": "",
    }
    obj = CancelReportRequest(**kwargs)
    assert isinstance(obj, CancelReportRequest)


def test_cancelreportschedulerequest_instantiates():
    """Instantiate CancelReportScheduleRequest with dummy data"""
    kwargs = {
        "report_schedule_id": "",
    }
    obj = CancelReportScheduleRequest(**kwargs)
    assert isinstance(obj, CancelReportScheduleRequest)


def test_reportoptions_instantiates():
    """Instantiate ReportOptions with dummy data"""
    kwargs = {}
    obj = ReportOptions(**kwargs)
    assert isinstance(obj, ReportOptions)


def test_createreportspecification_instantiates():
    """Instantiate CreateReportSpecification with dummy data"""
    kwargs = {
        "report_options": None,
        "report_type": "",
        "data_start_time": None,
        "data_end_time": None,
        "marketplace_ids": None,
    }
    obj = CreateReportSpecification(**kwargs)
    assert isinstance(obj, CreateReportSpecification)


def test_createreportrequest_instantiates():
    """Instantiate CreateReportRequest with dummy data"""
    kwargs = {
        "body": CreateReportSpecification(
            **{
                "report_options": None,
                "report_type": "",
                "data_start_time": None,
                "data_end_time": None,
                "marketplace_ids": None,
            }
        ),
    }
    obj = CreateReportRequest(**kwargs)
    assert isinstance(obj, CreateReportRequest)


def test_createreportresponse_instantiates():
    """Instantiate CreateReportResponse with dummy data"""
    kwargs = {
        "report_id": "",
    }
    obj = CreateReportResponse(**kwargs)
    assert isinstance(obj, CreateReportResponse)


def test_createreportschedulespecification_instantiates():
    """Instantiate CreateReportScheduleSpecification with dummy data"""
    kwargs = {
        "report_type": "",
        "marketplace_ids": None,
        "report_options": None,
        "period": PeriodEnum.PT5_M,
        "next_report_creation_time": None,
    }
    obj = CreateReportScheduleSpecification(**kwargs)
    assert isinstance(obj, CreateReportScheduleSpecification)


def test_createreportschedulerequest_instantiates():
    """Instantiate CreateReportScheduleRequest with dummy data"""
    kwargs = {
        "body": CreateReportScheduleSpecification(
            **{
                "report_type": "",
                "marketplace_ids": None,
                "report_options": None,
                "period": PeriodEnum.PT5_M,
                "next_report_creation_time": None,
            }
        ),
    }
    obj = CreateReportScheduleRequest(**kwargs)
    assert isinstance(obj, CreateReportScheduleRequest)


def test_createreportscheduleresponse_instantiates():
    """Instantiate CreateReportScheduleResponse with dummy data"""
    kwargs = {
        "report_schedule_id": "",
    }
    obj = CreateReportScheduleResponse(**kwargs)
    assert isinstance(obj, CreateReportScheduleResponse)


def test_error_instantiates():
    """Instantiate Error with dummy data"""
    kwargs = {
        "code": "",
        "message": "",
        "details": None,
    }
    obj = Error(**kwargs)
    assert isinstance(obj, Error)


def test_errorlist_instantiates():
    """Instantiate ErrorList with dummy data"""
    kwargs = {
        "errors": [],
    }
    obj = ErrorList(**kwargs)
    assert isinstance(obj, ErrorList)


def test_getreportdocumentrequest_instantiates():
    """Instantiate GetReportDocumentRequest with dummy data"""
    kwargs = {
        "report_document_id": "",
    }
    obj = GetReportDocumentRequest(**kwargs)
    assert isinstance(obj, GetReportDocumentRequest)


def test_getreportrequest_instantiates():
    """Instantiate GetReportRequest with dummy data"""
    kwargs = {
        "report_id": "",
    }
    obj = GetReportRequest(**kwargs)
    assert isinstance(obj, GetReportRequest)


def test_getreportschedulerequest_instantiates():
    """Instantiate GetReportScheduleRequest with dummy data"""
    kwargs = {
        "report_schedule_id": "",
    }
    obj = GetReportScheduleRequest(**kwargs)
    assert isinstance(obj, GetReportScheduleRequest)


def test_getreportschedulesrequest_instantiates():
    """Instantiate GetReportSchedulesRequest with dummy data"""
    kwargs = {
        "report_types": [],
    }
    obj = GetReportSchedulesRequest(**kwargs)
    assert isinstance(obj, GetReportSchedulesRequest)


def test_getreportsrequest_instantiates():
    """Instantiate GetReportsRequest with dummy data"""
    kwargs = {
        "report_types": None,
        "processing_statuses": None,
        "marketplace_ids": None,
        "page_size": None,
        "created_since": None,
        "created_until": None,
        "next_token": None,
    }
    obj = GetReportsRequest(**kwargs)
    assert isinstance(obj, GetReportsRequest)


def test_getreportsresponse_instantiates():
    """Instantiate GetReportsResponse with dummy data"""
    kwargs = {
        "reports": [],
        "next_token": None,
    }
    obj = GetReportsResponse(**kwargs)
    assert isinstance(obj, GetReportsResponse)


def test_report_instantiates():
    """Instantiate Report with dummy data"""
    kwargs = {
        "marketplace_ids": None,
        "report_id": "",
        "report_type": "",
        "data_start_time": None,
        "data_end_time": None,
        "report_schedule_id": None,
        "created_time": datetime(2000, 1, 1),
        "processing_status": ProcessingStatusEnum.CANCELLED,
        "processing_start_time": None,
        "processing_end_time": None,
        "report_document_id": None,
    }
    obj = Report(**kwargs)
    assert isinstance(obj, Report)


def test_reportdocument_instantiates():
    """Instantiate ReportDocument with dummy data"""
    kwargs = {
        "report_document_id": "",
        "url": "",
        "compression_algorithm": None,
    }
    obj = ReportDocument(**kwargs)
    assert isinstance(obj, ReportDocument)


def test_reportschedule_instantiates():
    """Instantiate ReportSchedule with dummy data"""
    kwargs = {
        "report_schedule_id": "",
        "report_type": "",
        "marketplace_ids": None,
        "report_options": None,
        "period": "",
        "next_report_creation_time": None,
    }
    obj = ReportSchedule(**kwargs)
    assert isinstance(obj, ReportSchedule)


def test_reportschedulelist_instantiates():
    """Instantiate ReportScheduleList with dummy data"""
    kwargs = {
        "report_schedules": [],
    }
    obj = ReportScheduleList(**kwargs)
    assert isinstance(obj, ReportScheduleList)
