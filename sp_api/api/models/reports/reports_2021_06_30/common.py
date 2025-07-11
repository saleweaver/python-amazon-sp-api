"""
Common models generated from Swagger/OpenAPI specification.

This file was auto-generated. Do not edit manually.

"""

from datetime import date, datetime
from enum import Enum, auto
from typing import Annotated, Any, Dict, List, Optional, Union
from uuid import UUID

from pydantic import AliasChoices, BaseModel, ConfigDict, Field

from .base_models import (BodyParam, GetRequestSerializer, PathParam,
                          QueryParam, RequestsBaseModel, SpApiBaseModel)

"""
CancelReportRequest

Request parameters for cancelReport
"""


class CancelReportRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for cancelReport
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    report_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("reportId", "report_id"),
            serialization_alias="reportId",
            description="[PATH] The identifier for the report. This identifier is unique only in combination with a seller ID.",
        ),
    ]


"""
CancelReportScheduleRequest

Request parameters for cancelReportSchedule
"""


class CancelReportScheduleRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for cancelReportSchedule
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    report_schedule_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("reportScheduleId", "report_schedule_id"),
            serialization_alias="reportScheduleId",
            description="[PATH] The identifier for the report schedule. This identifier is unique only in combination with a seller ID.",
        ),
    ]


"""
ReportOptions

Additional information passed to reports. This varies by report type.
"""


class ReportOptions(SpApiBaseModel):
    """Additional information passed to reports. This varies by report type."""

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow",
        serialize_by_alias=True,
        arbitrary_types_allowed=True,
    )


"""
CreateReportSpecification

Information required to create the report.
"""


class CreateReportSpecification(SpApiBaseModel):
    """Information required to create the report."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    report_options: Annotated[
        Optional["ReportOptions"],
        Field(
            None,
            validation_alias=AliasChoices("reportOptions", "report_options"),
            serialization_alias="reportOptions",
        ),
    ]

    report_type: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("reportType", "report_type"),
            serialization_alias="reportType",
            description="The report type. Refer to [Report Type Values](https://developer-docs.amazon.com/sp-api/docs/report-type-values) for more information.",
        ),
    ]

    data_start_time: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices("dataStartTime", "data_start_time"),
            serialization_alias="dataStartTime",
            description="The start of a date and time range, in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> date time format, used for selecting the data to report. The default is now. The value must be prior to or equal to the current date and time. Not all report types make use of this.",
        ),
    ]

    data_end_time: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices("dataEndTime", "data_end_time"),
            serialization_alias="dataEndTime",
            description="The end of a date and time range, in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> date time format, used for selecting the data to report. The default is now. The value must be prior to or equal to the current date and time. Not all report types make use of this.",
        ),
    ]

    marketplace_ids: Annotated[
        Optional[List["str"]],
        Field(
            None,
            validation_alias=AliasChoices("marketplaceIds", "marketplace_ids"),
            serialization_alias="marketplaceIds",
            description="A list of marketplace identifiers. The report document's contents will contain data for all of the specified marketplaces, unless the report type indicates otherwise.",
        ),
    ]


"""
CreateReportRequest

Request parameters for createReport
"""


class CreateReportRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for createReport
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    body: Annotated[
        "CreateReportSpecification",
        BodyParam(),
        Field(..., description="[BODY] Information required to create the report."),
    ]


"""
CreateReportResponse

The response schema.
"""


class CreateReportResponse(SpApiBaseModel):
    """The response schema."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    report_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("reportId", "report_id"),
            serialization_alias="reportId",
            description="The identifier for the report. This identifier is unique only in combination with a seller ID.",
        ),
    ]


# Enum definitions
class CreateReportScheduleSpecificationPeriodEnum(str, Enum):
    """Enum for period"""

    PT5_M = "PT5M"  # 5 minutes
    PT15_M = "PT15M"  # 15 minutes
    PT30_M = "PT30M"  # 30 minutes
    PT1_H = "PT1H"  # 1 hour
    PT2_H = "PT2H"  # 2 hours
    PT4_H = "PT4H"  # 4 hours
    PT8_H = "PT8H"  # 8 hours
    PT12_H = "PT12H"  # 12 hours
    P1_D = "P1D"  # 1 day
    P2_D = "P2D"  # 2 days
    P3_D = "P3D"  # 3 days
    PT84_H = "PT84H"  # 84 hours
    P7_D = "P7D"  # 7 days
    P14_D = "P14D"  # 14 days
    P15_D = "P15D"  # 15 days
    P18_D = "P18D"  # 18 days
    P30_D = "P30D"  # 30 days
    P1_M = "P1M"  # 1 month


"""
CreateReportScheduleSpecification

Information required to create the report schedule.
"""


class CreateReportScheduleSpecification(SpApiBaseModel):
    """Information required to create the report schedule."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    report_type: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("reportType", "report_type"),
            serialization_alias="reportType",
            description="The report type. Refer to [Report Type Values](https://developer-docs.amazon.com/sp-api/docs/report-type-values) for more information.",
        ),
    ]

    marketplace_ids: Annotated[
        Optional[List["str"]],
        Field(
            None,
            validation_alias=AliasChoices("marketplaceIds", "marketplace_ids"),
            serialization_alias="marketplaceIds",
            description="A list of marketplace identifiers for the report schedule.",
        ),
    ]

    report_options: Annotated[
        Optional["ReportOptions"],
        Field(
            None,
            validation_alias=AliasChoices("reportOptions", "report_options"),
            serialization_alias="reportOptions",
        ),
    ]

    period: Annotated[
        CreateReportScheduleSpecificationPeriodEnum,
        Field(
            ...,
            description="One of a set of predefined <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> periods that specifies how often a report should be created.",
        ),
    ]

    next_report_creation_time: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices(
                "nextReportCreationTime", "next_report_creation_time"
            ),
            serialization_alias="nextReportCreationTime",
            description="The date and time when the schedule will create its next report, in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> date time format.",
        ),
    ]


"""
CreateReportScheduleRequest

Request parameters for createReportSchedule
"""


class CreateReportScheduleRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for createReportSchedule
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    body: Annotated[
        "CreateReportScheduleSpecification",
        BodyParam(),
        Field(
            ...,
            description="[BODY] Information required to create the report schedule.",
        ),
    ]


"""
CreateReportScheduleResponse

Response schema.
"""


class CreateReportScheduleResponse(SpApiBaseModel):
    """Response schema."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    report_schedule_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("reportScheduleId", "report_schedule_id"),
            serialization_alias="reportScheduleId",
            description="The identifier for the report schedule. This identifier is unique only in combination with a seller ID.",
        ),
    ]


"""
Error

Error response returned when the request is unsuccessful.
"""


class Error(SpApiBaseModel):
    """Error response returned when the request is unsuccessful."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    code: Annotated[
        str,
        Field(
            ...,
            description="An error code that identifies the type of error that occurred.",
        ),
    ]

    message: Annotated[
        str, Field(..., description="A message that describes the error condition.")
    ]

    details: Annotated[
        Optional[str],
        Field(
            None,
            description="Additional details that can help the caller understand or fix the issue.",
        ),
    ]


"""
ErrorList

A list of error responses returned when a request is unsuccessful.
"""


class ErrorList(SpApiBaseModel):
    """A list of error responses returned when a request is unsuccessful."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    errors: Annotated[
        List["Error"],
        Field(
            ..., description="Error response returned when the request is unsuccessful."
        ),
    ]


"""
GetReportDocumentRequest

Request parameters for getReportDocument
"""


class GetReportDocumentRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getReportDocument
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    report_document_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("reportDocumentId", "report_document_id"),
            serialization_alias="reportDocumentId",
            description="[PATH] The identifier for the report document.",
        ),
    ]


"""
GetReportRequest

Request parameters for getReport
"""


class GetReportRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getReport
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    report_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("reportId", "report_id"),
            serialization_alias="reportId",
            description="[PATH] The identifier for the report. This identifier is unique only in combination with a seller ID.",
        ),
    ]


"""
GetReportScheduleRequest

Request parameters for getReportSchedule
"""


class GetReportScheduleRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getReportSchedule
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    report_schedule_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("reportScheduleId", "report_schedule_id"),
            serialization_alias="reportScheduleId",
            description="[PATH] The identifier for the report schedule. This identifier is unique only in combination with a seller ID.",
        ),
    ]


"""
GetReportSchedulesRequest

Request parameters for getReportSchedules
"""


class GetReportSchedulesRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getReportSchedules
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    report_types: Annotated[
        List["str"],
        QueryParam(),
        Field(
            ...,
            validation_alias=AliasChoices("reportTypes", "report_types"),
            serialization_alias="reportTypes",
            description="[QUERY] A list of report types used to filter report schedules. Refer to [Report Type Values](https://developer-docs.amazon.com/sp-api/docs/report-type-values) for more information.",
        ),
    ]


# Enum definitions
class GetReportsRequestProcessingStatusesEnum(str, Enum):
    """Enum for processingStatuses"""

    CANCELLED = "CANCELLED"  # The report was cancelled. There are two ways a report can be cancelled: an explicit cancellation request before the report starts processing, or an automatic cancellation if there is no data to return.
    DONE = "DONE"  # The report has completed processing.
    FATAL = "FATAL"  # The report was aborted due to a fatal error.
    IN_PROGRESS = "IN_PROGRESS"  # The report is being processed.
    IN_QUEUE = "IN_QUEUE"  # The report has not yet started processing. It may be waiting for another `IN_PROGRESS` report.


"""
GetReportsRequest

Request parameters for getReports
"""


class GetReportsRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getReports
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    report_types: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("reportTypes", "report_types"),
            serialization_alias="reportTypes",
            description="[QUERY] A list of report types used to filter reports. Refer to [Report Type Values](https://developer-docs.amazon.com/sp-api/docs/report-type-values) for more information. When reportTypes is provided, the other filter parameters (processingStatuses, marketplaceIds, createdSince, createdUntil) and pageSize may also be provided. Either reportTypes or nextToken is required.",
        ),
    ]

    processing_statuses: Annotated[
        Optional[List["GetReportsRequestProcessingStatusesEnum"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("processingStatuses", "processing_statuses"),
            serialization_alias="processingStatuses",
            description="[QUERY] A list of processing statuses used to filter reports.",
        ),
    ]

    marketplace_ids: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceIds", "marketplace_ids"),
            serialization_alias="marketplaceIds",
            description="[QUERY] A list of marketplace identifiers used to filter reports. The reports returned will match at least one of the marketplaces that you specify.",
        ),
    ]

    page_size: Annotated[
        Optional[int],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("pageSize", "page_size"),
            serialization_alias="pageSize",
            description="[QUERY] The maximum number of reports to return in a single call.",
        ),
    ]

    created_since: Annotated[
        Optional[datetime],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("createdSince", "created_since"),
            serialization_alias="createdSince",
            description="[QUERY] The earliest report creation date and time for reports to include in the response, in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> date time format. The default is 90 days ago. Reports are retained for a maximum of 90 days.",
        ),
    ]

    created_until: Annotated[
        Optional[datetime],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("createdUntil", "created_until"),
            serialization_alias="createdUntil",
            description="[QUERY] The latest report creation date and time for reports to include in the response, in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> date time format. The default is now.",
        ),
    ]

    next_token: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("nextToken", "next_token"),
            serialization_alias="nextToken",
            description="[QUERY] A string token returned in the response to your previous request. `nextToken` is returned when the number of results exceeds the specified `pageSize` value. To get the next page of results, call the `getReports` operation and include this token as the only parameter. Specifying `nextToken` with any other parameters will cause the request to fail.",
        ),
    ]


ReportList = List["Report"]
"""A list of reports."""


"""
GetReportsResponse

The response for the `getReports` operation.
"""


class GetReportsResponse(SpApiBaseModel):
    """The response for the `getReports` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    reports: Annotated["ReportList", Field(..., description="The reports.")]

    next_token: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("nextToken", "next_token"),
            serialization_alias="nextToken",
            description="Returned when the number of results exceeds `pageSize`. To get the next page of results, call `getReports` with this token as the only parameter.",
        ),
    ]


# Enum definitions
class ReportProcessingStatusEnum(str, Enum):
    """Enum for processingStatus"""

    CANCELLED = "CANCELLED"  # The report was cancelled. There are two ways a report can be cancelled: an explicit cancellation request before the report starts processing, or an automatic cancellation if there is no data to return.
    DONE = "DONE"  # The report has completed processing.
    FATAL = "FATAL"  # The report was aborted due to a fatal error.
    IN_PROGRESS = "IN_PROGRESS"  # The report is being processed.
    IN_QUEUE = "IN_QUEUE"  # The report has not yet started processing. It may be waiting for another `IN_PROGRESS` report.


"""
Report

Detailed information about the report.
"""


class Report(SpApiBaseModel):
    """Detailed information about the report."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    marketplace_ids: Annotated[
        Optional[List["str"]],
        Field(
            None,
            validation_alias=AliasChoices("marketplaceIds", "marketplace_ids"),
            serialization_alias="marketplaceIds",
            description="A list of marketplace identifiers for the report.",
        ),
    ]

    report_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("reportId", "report_id"),
            serialization_alias="reportId",
            description="The identifier for the report. This identifier is unique only in combination with a seller ID.",
        ),
    ]

    report_type: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("reportType", "report_type"),
            serialization_alias="reportType",
            description="The report type. Refer to [Report Type Values](https://developer-docs.amazon.com/sp-api/docs/report-type-values) for more information.",
        ),
    ]

    data_start_time: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices("dataStartTime", "data_start_time"),
            serialization_alias="dataStartTime",
            description="The start of a date and time range used for selecting the data to report.",
        ),
    ]

    data_end_time: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices("dataEndTime", "data_end_time"),
            serialization_alias="dataEndTime",
            description="The end of a date and time range used for selecting the data to report.",
        ),
    ]

    report_schedule_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("reportScheduleId", "report_schedule_id"),
            serialization_alias="reportScheduleId",
            description="The identifier of the report schedule that created this report (if any). This identifier is unique only in combination with a seller ID.",
        ),
    ]

    created_time: Annotated[
        datetime,
        Field(
            ...,
            validation_alias=AliasChoices("createdTime", "created_time"),
            serialization_alias="createdTime",
            description="The date and time when the report was created.",
        ),
    ]

    processing_status: Annotated[
        ReportProcessingStatusEnum,
        Field(
            ...,
            validation_alias=AliasChoices("processingStatus", "processing_status"),
            serialization_alias="processingStatus",
            description="The processing status of the report.",
        ),
    ]

    processing_start_time: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices(
                "processingStartTime", "processing_start_time"
            ),
            serialization_alias="processingStartTime",
            description="The date and time when the report processing started, in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> date time format.",
        ),
    ]

    processing_end_time: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices("processingEndTime", "processing_end_time"),
            serialization_alias="processingEndTime",
            description="The date and time when the report processing completed, in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> date time format.",
        ),
    ]

    report_document_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("reportDocumentId", "report_document_id"),
            serialization_alias="reportDocumentId",
            description="The identifier for the report document. Pass this into the `getReportDocument` operation to get the information you will need to retrieve the report document's contents.",
        ),
    ]


# Enum definitions
class ReportDocumentCompressionAlgorithmEnum(str, Enum):
    """Enum for compressionAlgorithm"""

    GZIP = "GZIP"  # The gzip compression algorithm.


"""
ReportDocument

Information required for the report document.
"""


class ReportDocument(SpApiBaseModel):
    """Information required for the report document."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    report_document_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("reportDocumentId", "report_document_id"),
            serialization_alias="reportDocumentId",
            description="The identifier for the report document. This identifier is unique only in combination with a seller ID.",
        ),
    ]

    url: Annotated[
        str,
        Field(
            ...,
            description="A presigned URL for the report document. If `compressionAlgorithm` is not returned, you can download the report directly from this URL. This URL expires after 5 minutes.",
        ),
    ]

    compression_algorithm: Annotated[
        Optional[ReportDocumentCompressionAlgorithmEnum],
        Field(
            None,
            validation_alias=AliasChoices(
                "compressionAlgorithm", "compression_algorithm"
            ),
            serialization_alias="compressionAlgorithm",
            description="If the report document contents have been compressed, the compression algorithm used is returned in this property and you must decompress the report when you download. Otherwise, you can download the report directly. Refer to [Step 2. Download the report](https://developer-docs.amazon.com/sp-api/docs/reports-api-v2021-06-30-retrieve-a-report#step-2-download-the-report) in the use case guide, where sample code is provided.",
        ),
    ]


"""
ReportSchedule

Detailed information about a report schedule.
"""


class ReportSchedule(SpApiBaseModel):
    """Detailed information about a report schedule."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    report_schedule_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("reportScheduleId", "report_schedule_id"),
            serialization_alias="reportScheduleId",
            description="The identifier for the report schedule. This identifier is unique only in combination with a seller ID.",
        ),
    ]

    report_type: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("reportType", "report_type"),
            serialization_alias="reportType",
            description="The report type. Refer to [Report Type Values](https://developer-docs.amazon.com/sp-api/docs/report-type-values) for more information.",
        ),
    ]

    marketplace_ids: Annotated[
        Optional[List["str"]],
        Field(
            None,
            validation_alias=AliasChoices("marketplaceIds", "marketplace_ids"),
            serialization_alias="marketplaceIds",
            description="A list of marketplace identifiers. The report document's contents will contain data for all of the specified marketplaces, unless the report type indicates otherwise.",
        ),
    ]

    report_options: Annotated[
        Optional["ReportOptions"],
        Field(
            None,
            validation_alias=AliasChoices("reportOptions", "report_options"),
            serialization_alias="reportOptions",
        ),
    ]

    period: Annotated[
        str,
        Field(
            ...,
            description="An <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> period value that indicates how often a report should be created.",
        ),
    ]

    next_report_creation_time: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices(
                "nextReportCreationTime", "next_report_creation_time"
            ),
            serialization_alias="nextReportCreationTime",
            description="The date and time when the schedule will create its next report, in <a href='https://developer-docs.amazon.com/sp-api/docs/iso-8601'>ISO 8601</a> date time format.",
        ),
    ]


"""
ReportScheduleList

A list of report schedules.
"""


class ReportScheduleList(SpApiBaseModel):
    """A list of report schedules."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    report_schedules: Annotated[
        List["ReportSchedule"],
        Field(
            ...,
            validation_alias=AliasChoices("reportSchedules", "report_schedules"),
            serialization_alias="reportSchedules",
            description="Detailed information about a report schedule.",
        ),
    ]


# Rebuild models to resolve forward references
ErrorList.model_rebuild()
Error.model_rebuild()
Report.model_rebuild()
CreateReportScheduleSpecification.model_rebuild()
CreateReportSpecification.model_rebuild()
ReportOptions.model_rebuild()
ReportSchedule.model_rebuild()
ReportScheduleList.model_rebuild()
CreateReportResponse.model_rebuild()
GetReportsResponse.model_rebuild()
CreateReportScheduleResponse.model_rebuild()
ReportDocument.model_rebuild()
GetReportsRequest.model_rebuild()
CreateReportRequest.model_rebuild()
CancelReportRequest.model_rebuild()
GetReportRequest.model_rebuild()
GetReportSchedulesRequest.model_rebuild()
CreateReportScheduleRequest.model_rebuild()
CancelReportScheduleRequest.model_rebuild()
GetReportScheduleRequest.model_rebuild()
GetReportDocumentRequest.model_rebuild()
