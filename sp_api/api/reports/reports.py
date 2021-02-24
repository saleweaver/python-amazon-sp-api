from collections import abc
from datetime import datetime
import zlib

import requests

from sp_api.base import sp_endpoint, fill_query_params, SellingApiException, ApiResponse, ProcessingStatus, Marketplaces
from sp_api.base import Client
from sp_api.base.helpers import decrypt_aes


class Reports(Client):

    @sp_endpoint('/reports/2020-09-04/reports', method='POST')
    def create_report(self, **kwargs) -> ApiResponse:
        """
        create_report(self, **kwargs) -> ApiResponse

        See report types at
        :link: https://github.com/amzn/selling-partner-api-docs/blob/main/references/reports-api/reportType_string_array_values.md

        **Usage Plan:**

        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        0.0167                                  15
        ======================================  ==============


        Args:
            key reportOptions: optional	Additional information passed to reports. This varies by report type.	ReportOptions
            key reportType: required	The report type. :link: https://github.com/amzn/selling-partner-api-docs/blob/main/references/reports-api/reportType_string_array_values.md
            key dataStartTime: optional	The start of a date and time range, in ISO 8601 date time format, used for selecting the data to report. The default is now. The value must be prior to or equal to the current date and time. Not all report types make use of this.	string (date-time)
            key dataEndTime: optional	The end of a date and time range, in ISO 8601 date time format, used for selecting the data to report. The default is now. The value must be prior to or equal to the current date and time. Not all report types make use of this.	string (date-time)
            key marketplaceIds: optional, defaults to the client's marketplace  A list of marketplace identifiers. The report document's contents will contain data for all of the specified marketplaces, unless the report type indicates otherwise.	< string > array

        Returns:
            ApiResponse
        """
        return self._request(kwargs.pop('path'), data=kwargs)

    @sp_endpoint('/reports/2020-09-04/reports/{}')
    def get_report(self, report_id, **kwargs) -> ApiResponse:
        """
        get_report(self, report_id, **kwargs)
        Returns report details (including the reportDocumentId, if available) for the report that you specify.

        **Usage Plan:**

        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        2                                       15
        ======================================  ==============


        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            report_id: str

        Returns:
            ApiResponse

        """
        return self._request(fill_query_params(kwargs.pop('path'), report_id), add_marketplace=False)

    @sp_endpoint('/reports/2020-09-04/documents/{}')
    def get_report_document(self, document_id, decrypt: bool = False, file=None, ** kwargs) -> ApiResponse:
        """
        get_report_document(self, document_id, decrypt: bool = False, file=None, ** kwargs) -> ApiResponse
        Returns the information required for retrieving a report document's contents. This includes a presigned URL for the report document as well as the information required to decrypt the document's contents.

        If decrypt = True the report will automatically be loaded and decrypted/unpacked
        If file is set to a file (or file like object), the report's contents are written to the file


        **Usage Plan:**


        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        0.0167                                  15
        ======================================  ==============



        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            document_id: str | the document to load
            decrypt: bool | flag to automatically decrypt a report
            file: If passed, will save the document to the file specified. Only valid if decrypt=True

        Returns:
             ApiResponse
        """
        res = self._request(fill_query_params(kwargs.pop('path'), document_id), add_marketplace=False)
        if decrypt:
            document = self.decrypt_report_document(
                    res.payload.get('url'),
                    res.payload.get('encryptionDetails').get('initializationVector'),
                    res.payload.get('encryptionDetails').get('key'),
                    res.payload.get('encryptionDetails').get('standard'),
                    res.payload
                )
            res.payload.update({
                'document': document
            })
            if file:
                if isinstance(file, str):
                    with open(file, "w") as text_file:
                        text_file.write(document)
                else:
                    file.write(document)

        return res

    @sp_endpoint('/reports/2020-09-04/schedules', method='POST')
    def create_report_schedule(self, **kwargs) -> ApiResponse:
        """
        create_report_schedule(self, **kwargs) -> ApiResponse
        Creates a report schedule. If a report schedule with the same report type and marketplace IDs already exists, it will be cancelled and replaced with this one.

        **Usage Plan:**

        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        0.0222                                  10
        ======================================  ==============

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        :param kwargs:
        :return:
        """
        return self._request(kwargs.pop('path'), data=kwargs)

    @sp_endpoint('/reports/2020-09-04/schedules/{}', method='DELETE')
    def delete_report_schedule(self, schedule_id, **kwargs) -> ApiResponse:
        """
        delete_report_schedule(self, schedule_id, **kwargs) -> ApiResponse
        Cancels the report schedule that you specify.

        **Usage Plan:**

        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        0.0222                                  10
        ======================================  ==============

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            schedule_id: str
            kwargs:

        Returns:
            ApiResponse
        """
        return self._request(fill_query_params(kwargs.pop('path'), schedule_id), params=kwargs)

    @sp_endpoint('/reports/2020-09-04/schedules/{}')
    def get_report_schedule(self, schedule_id, **kwargs) -> ApiResponse:
        """
        Cancels the report schedule that you specify.

        **Usage Plan:**

        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        0.0222                                  10
        ======================================  ==============

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            schedule_id: str
            kwargs:

        Returns:
            ApiResponse
        """
        return self._request(fill_query_params(kwargs.pop('path'), schedule_id), params=kwargs)

    @sp_endpoint('/reports/2020-09-04/reports')
    def get_reports(self, **kwargs) -> ApiResponse:
        """
        get_reports(self, **kwargs) -> ApiResponse

        Returns report details for the reports that match the filters that you specify.

        **Usage Plan:**

        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        0.0222                                  10
        ======================================  ==============

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.


        Args:
            key reportTypes: str[] or ReportType[] | optional  A list of report types used to filter reports. When reportTypes is provided, the other filter parameters (processingStatuses, marketplaceIds, createdSince, createdUntil) and pageSize may also be provided. Either reportTypes or nextToken is required.
            key processingStatuses: str[] or ProcessingStatus[] optional	A list of processing statuses used to filter reports.
            key marketplaceIds: str[] or Marketplaces[] optional	A list of marketplace identifiers used to filter reports. The reports returned will match at least one of the marketplaces that you specify.
            key pageSize: int optional	The maximum number of reports to return in a single call.
            key createdSince: str or datetime optional	The earliest report creation date and time for reports to include in the response, in ISO 8601 date time format. The default is 90 days ago. Reports are retained for a maximum of 90 days.	string (date-time)	-
            key	createdUntil: str or datetime optional	The latest report creation date and time for reports to include in the response, in ISO 8601 date time format. The default is now.	string (date-time)	-
            key nextToken: str optional	A string token returned in the response to your previous request. nextToken is returned when the number of results exceeds the specified pageSize value. To get the next page of results, call the getReports operation and include this token as the only parameter. Specifying nextToken with any other parameters will cause the request to fail.	string	-


        Returns:
            ApiResponse
        """
        if kwargs.get('reportTypes', None) and isinstance(kwargs.get('reportTypes'), abc.Iterable):
            kwargs.update({'reportTypes': ','.join(kwargs.get('reportTypes'))})
        if kwargs.get('processingStatuses', None) and isinstance(kwargs.get('processingStatuses'), abc.Iterable):
            kwargs.update({'processingStatuses': ','.join(kwargs.get('processingStatuses'))})
        if kwargs.get('marketplaceIds', None) and isinstance(kwargs.get('marketplaceIds'), abc.Iterable):
            marketplaces = kwargs.get('marketplaceIds')
            if not isinstance(marketplaces, abc.Iterable):
                marketplaces = [marketplaces]
            kwargs.update({'marketplaceIds': ','.join([m.marketplace_id if isinstance(m, Marketplaces) else m for m in marketplaces])})
        for k in ['createdSince', 'createdUntil']:
            if kwargs.get(k, None) and isinstance(kwargs.get(k), datetime):
                kwargs.update({k: kwargs.get(k).isoformat()})

        return self._request(kwargs.pop('path'), params=kwargs, add_marketplace=False)

    @staticmethod
    def decrypt_report_document(url, initialization_vector, key, encryption_standard, payload):
        """
        Decrypts and unpacks a report document, currently AES encryption is implemented
        """
        if encryption_standard == 'AES':
            decrypted = decrypt_aes(requests.get(url).content, key, initialization_vector)
            if 'compressionAlgorithm' in payload:
                return zlib.decompress(bytearray(decrypted), 15 + 32).decode('iso-8859-1')
            return decrypted.decode('iso-8859-1')
        raise SellingApiException([{
            'message': 'Only AES decryption is implemented. Contribute: https://github.com/saleweaver/python-sp-api'
        }])
