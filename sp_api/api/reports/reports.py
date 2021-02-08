import zlib

import requests

from sp_api.base import sp_endpoint, fill_query_params, SellingApiException, ApiResponse
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
