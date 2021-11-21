import urllib.parse
import zlib
from collections import abc
from datetime import datetime

import requests

from sp_api.base import Client, sp_endpoint, fill_query_params, ApiResponse, Marketplaces


class ReportsV2(Client):
    """
    Reports SP-API Client
    :link: 

    The Selling Partner API for Reports lets you retrieve and manage a variety of reports that can help selling partners manage their businesses.
    """

    @sp_endpoint('/reports/2021-06-30/reports', method='GET')
    def get_reports(self, **kwargs) -> ApiResponse:
        """
        get_reports(self, **kwargs) -> ApiResponse

        Returns report details for the reports that match the filters that you specify.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 0.0222 | 10 |

For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

         Args:
        
            key reportTypes:array |  A list of report types used to filter reports. When reportTypes is provided, the other filter parameters (processingStatuses, marketplaceIds, createdSince, createdUntil) and pageSize may also be provided. Either reportTypes or nextToken is required.
        
            key processingStatuses:array |  A list of processing statuses used to filter reports.
        
            key marketplaceIds:array |  A list of marketplace identifiers used to filter reports. The reports returned will match at least one of the marketplaces that you specify.
        
            key pageSize:integer |  The maximum number of reports to return in a single call.
        
            key createdSince:string |  The earliest report creation date and time for reports to include in the response, in ISO 8601 date time format. The default is 90 days ago. Reports are retained for a maximum of 90 days.
        
            key createdUntil:string |  The latest report creation date and time for reports to include in the response, in ISO 8601 date time format. The default is now.
        
            key nextToken:string |  A string token returned in the response to your previous request. nextToken is returned when the number of results exceeds the specified pageSize value. To get the next page of results, call the getReports operation and include this token as the only parameter. Specifying nextToken with any other parameters will cause the request to fail.
        

         Returns:
            ApiResponse:
        """
        if kwargs.get('reportTypes', None) and isinstance(kwargs.get('reportTypes'), abc.Iterable):
            kwargs.update({'reportTypes': ','.join(kwargs.get('reportTypes'))})
        if kwargs.get('processingStatuses', None) and isinstance(kwargs.get('processingStatuses'), abc.Iterable):
            kwargs.update({'processingStatuses': ','.join(kwargs.get('processingStatuses'))})
        if kwargs.get('marketplaceIds', None) and isinstance(kwargs.get('marketplaceIds'), abc.Iterable):
            marketplaces = kwargs.get('marketplaceIds')
            if not isinstance(marketplaces, abc.Iterable):
                marketplaces = [marketplaces]
            kwargs.update({'marketplaceIds': ','.join(
                [m.marketplace_id if isinstance(m, Marketplaces) else m for m in marketplaces])})
        for k in ['createdSince', 'createdUntil']:
            if kwargs.get(k, None) and isinstance(kwargs.get(k), datetime):
                kwargs.update({k: kwargs.get(k).isoformat()})

        return self._request(kwargs.pop('path'), params=kwargs)

    @sp_endpoint('/reports/2021-06-30/reports', method='POST')
    def create_report(self, **kwargs) -> ApiResponse:
        """
        create_report(self, **kwargs) -> ApiResponse

        Creates a report.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 0.0167 | 15 |

For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

         Args:
        
            body: | * REQUIRED {'description': 'Information required to create the report.',
 'properties': {'dataEndTime': {'description': 'The end of a date and time range, in ISO 8601 date time format, used for selecting the data to report. The default is now. The value must be prior to or equal to the current date and time. Not all '
                                               'report types make use of this.',
                                'format': 'date-time',
                                'type': 'string'},
                'dataStartTime': {'description': 'The start of a date and time range, in ISO 8601 date time format, used for selecting the data to report. The default is now. The value must be prior to or equal to the current date and time. Not all '
                                                 'report types make use of this.',
                                  'format': 'date-time',
                                  'type': 'string'},
                'marketplaceIds': {'description': "A list of marketplace identifiers. The report document's contents will contain data for all of the specified marketplaces, unless the report type indicates otherwise.",
                                   'items': {'type': 'string'},
                                   'maxItems': 25,
                                   'minItems': 1,
                                   'type': 'array'},
                'reportOptions': {'$ref': '#/definitions/ReportOptions'},
                'reportType': {'description': 'The report type.', 'type': 'string'}},
 'required': ['marketplaceIds', 'reportType'],
 'type': 'object'}
        

         Returns:
            ApiResponse:
        """

        return self._request(kwargs.pop('path'), data=kwargs)

    @sp_endpoint('/reports/2021-06-30/reports/{}', method='DELETE')
    def cancel_report(self, reportId, **kwargs) -> ApiResponse:
        """
        cancel_report(self, reportId, **kwargs) -> ApiResponse

        Cancels the report that you specify. Only reports with processingStatus=IN_QUEUE can be cancelled. Cancelled reports are returned in subsequent calls to the getReport and getReports operations.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 0.0222 | 10 |

For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

         Args:
        
            reportId:string | * REQUIRED The identifier for the report. This identifier is unique only in combination with a seller ID.
        

         Returns:
            ApiResponse:
        """

        return self._request(fill_query_params(kwargs.pop('path'), reportId), data=kwargs)

    @sp_endpoint('/reports/2021-06-30/reports/{}', method='GET')
    def get_report(self, reportId, **kwargs) -> ApiResponse:
        """
        get_report(self, reportId, **kwargs) -> ApiResponse

        Returns report details (including the reportDocumentId, if available) for the report that you specify.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 2.0 | 15 |

For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

         Args:
        
            reportId:string | * REQUIRED The identifier for the report. This identifier is unique only in combination with a seller ID.
        

         Returns:
            ApiResponse:
        """

        return self._request(fill_query_params(kwargs.pop('path'), reportId), params=kwargs)

    @sp_endpoint('/reports/2021-06-30/schedules', method='GET')
    def get_report_schedules(self, **kwargs) -> ApiResponse:
        """
        get_report_schedules(self, **kwargs) -> ApiResponse

        Returns report schedule details that match the filters that you specify.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 0.0222 | 10 |

For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

         Args:
        
            key reportTypes:array | * REQUIRED A list of report types used to filter report schedules.
        

         Returns:
            ApiResponse:
        """
        if kwargs.get('reportTypes', None) and isinstance(kwargs.get('reportTypes'), abc.Iterable):
            kwargs.update({'reportTypes': ','.join(kwargs.get('reportTypes'))})

        return self._request(kwargs.pop('path'), params=kwargs)

    @sp_endpoint('/reports/2021-06-30/schedules', method='POST')
    def create_report_schedule(self, **kwargs) -> ApiResponse:
        """
        create_report_schedule(self, **kwargs) -> ApiResponse

        Creates a report schedule. If a report schedule with the same report type and marketplace IDs already exists, it will be cancelled and replaced with this one.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 0.0222 | 10 |

For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

         Args:
        
            body: | * REQUIRED {'properties': {'marketplaceIds': {'description': 'A list of marketplace identifiers for the report schedule.', 'items': {'type': 'string'}, 'maxItems': 25, 'minItems': 1, 'type': 'array'},
                'nextReportCreationTime': {'description': 'The date and time when the schedule will create its next report, in ISO 8601 date time format.', 'format': 'date-time', 'type': 'string'},
                'period': {'description': 'One of a set of predefined ISO 8601 periods that specifies how often a report should be created.',
                           'enum': ['PT5M', 'PT15M', 'PT30M', 'PT1H', 'PT2H', 'PT4H', 'PT8H', 'PT12H', 'P1D', 'P2D', 'P3D', 'PT84H', 'P7D', 'P14D', 'P15D', 'P18D', 'P30D', 'P1M'],
                           'type': 'string',
                           'x-docgen-enum-table-extension': [{'description': '5 minutes', 'value': 'PT5M'},
                                                             {'description': '15 minutes', 'value': 'PT15M'},
                                                             {'description': '30 minutes', 'value': 'PT30M'},
                                                             {'description': '1 hour', 'value': 'PT1H'},
                                                             {'description': '2 hours', 'value': 'PT2H'},
                                                             {'description': '4 hours', 'value': 'PT4H'},
                                                             {'description': '8 hours', 'value': 'PT8H'},
                                                             {'description': '12 hours', 'value': 'PT12H'},
                                                             {'description': '1 day', 'value': 'P1D'},
                                                             {'description': '2 days', 'value': 'P2D'},
                                                             {'description': '3 days', 'value': 'P3D'},
                                                             {'description': '84 hours', 'value': 'PT84H'},
                                                             {'description': '7 days', 'value': 'P7D'},
                                                             {'description': '14 days', 'value': 'P14D'},
                                                             {'description': '15 days', 'value': 'P15D'},
                                                             {'description': '18 days', 'value': 'P18D'},
                                                             {'description': '30 days', 'value': 'P30D'},
                                                             {'description': '1 month', 'value': 'P1M'}]},
                'reportOptions': {'$ref': '#/definitions/ReportOptions'},
                'reportType': {'description': 'The report type.', 'type': 'string'}},
 'required': ['marketplaceIds', 'period', 'reportType'],
 'type': 'object'}
        

         Returns:
            ApiResponse:
        """

        return self._request(kwargs.pop('path'), data=kwargs)

    @sp_endpoint('/reports/2021-06-30/schedules/{}', method='DELETE')
    def cancel_report_schedule(self, reportScheduleId, **kwargs) -> ApiResponse:
        """
        cancel_report_schedule(self, reportScheduleId, **kwargs) -> ApiResponse

        Cancels the report schedule that you specify.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 0.0222 | 10 |

For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

         Args:
        
            reportScheduleId:string | * REQUIRED The identifier for the report schedule. This identifier is unique only in combination with a seller ID.
        

         Returns:
            ApiResponse:
        """

        return self._request(fill_query_params(kwargs.pop('path'), reportScheduleId), data=kwargs)

    @sp_endpoint('/reports/2021-06-30/schedules/{}', method='GET')
    def get_report_schedule(self, reportScheduleId, **kwargs) -> ApiResponse:
        """
        get_report_schedule(self, reportScheduleId, **kwargs) -> ApiResponse

        Returns report schedule details for the report schedule that you specify.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 0.0222 | 10 |

For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

         Args:
        
            reportScheduleId:string | * REQUIRED The identifier for the report schedule. This identifier is unique only in combination with a seller ID.
        

         Returns:
            ApiResponse:
        """

        return self._request(fill_query_params(kwargs.pop('path'), reportScheduleId), params=kwargs)

    @sp_endpoint('/reports/2021-06-30/documents/{}', method='GET')
    def get_report_document(self, reportDocumentId, download: bool = False, file=None,
                            character_code: str = 'iso-8859-1', **kwargs) -> ApiResponse:
        """
        get_report_document(self, reportDocumentId, **kwargs) -> ApiResponse

        Returns the information required for retrieving a report document's contents.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 0.0167 | 15 |

For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

         Args:
        
            download: bool
            character_code:
            file: File(like)
            reportDocumentId:string | * REQUIRED The identifier for the report document.
        

         Returns:
            ApiResponse:
        """
        res = self._request(fill_query_params(kwargs.pop('path'), reportDocumentId), add_marketplace=False)
        if download or file or ('decrypt' in kwargs and kwargs['decrypt']):
            document = requests.get(res.payload.get('url')).content
            if 'compressionAlgorithm' in res.payload:
                document = zlib.decompress(bytearray(document), 15 + 32)
            document = document.decode(character_code)
            if download:
                res.payload.update({
                    'document': document
                })
            if file:
                file.write(document)
                file.seek(0)
        return res
