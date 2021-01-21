import requests

from sp_api.api.notifications.models.delete_subscription_by_id_response import DeleteSubscriptionByIdResponse
from sp_api.api.notifications.models.get_subscription_by_id_response import GetSubscriptionByIdResponse
from sp_api.api.reports.models.create_report_response import CreateReportResponse
from sp_api.api.reports.models.create_report_schedule_response import CreateReportScheduleResponse
from sp_api.api.reports.models.create_report_schedule_specification import CreateReportScheduleSpecification
from sp_api.api.reports.models.get_report_document_response import GetReportDocumentResponse
from sp_api.api.reports.models.get_report_response import GetReportResponse
from sp_api.base import sp_endpoint, fill_query_params, SellingApiException
from sp_api.base import Client, Marketplaces
from sp_api.base.helpers import decrypt_aes


class Reports(Client):
    def __init__(self, marketplace=Marketplaces.US, refresh_token=None):
        super().__init__(marketplace, refresh_token)

    @sp_endpoint('/reports/2020-09-04/reports', method='POST')
    def create_report(self, **kwargs):
        """
        Creates a report.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0167 | 15 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        :param kwargs:
        :return:
        """
        return CreateReportResponse(
            **self._request(kwargs.pop('path'), data={**kwargs}).json()
        )

    @sp_endpoint('/reports/2020-09-04/reports/{}')
    def get_report(self, report_id, **kwargs):
        """
        Returns report details (including the reportDocumentId, if available) for the report that you specify.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2.0 | 15 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        :param report_id:
        :return:
        """
        return GetReportResponse(
            **self._request(fill_query_params(kwargs.pop('path'), report_id), add_marketplace=False).json()
        )

    @sp_endpoint('/reports/2020-09-04/documents/{}')
    def get_report_document(self, document_id, decrypt: bool = False, file=None, ** kwargs):
        """
        Returns the information required for retrieving a report document's contents. This includes a presigned URL for the report document as well as the information required to decrypt the document's contents.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0167 | 15 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        :param file: If passed, will save the document to the file specified. Only valid if decrypt=True
        :param decrypt:
        :param document_id:
        :param kwargs:
        :return:
        """
        res = self._request(fill_query_params(kwargs.pop('path'), document_id), add_marketplace=False).json()
        if decrypt:
            document = self.decrypt_report_document(
                    res.get('payload').get('url'),
                    res.get('payload').get('encryptionDetails').get('initializationVector'),
                    res.get('payload').get('encryptionDetails').get('key'),
                    res.get('payload').get('encryptionDetails').get('standard')
                )
            res.get('payload').update({
                'document': document
            })
            if file:
                file.write(document)
        return GetReportDocumentResponse(
            **res
        )

    @sp_endpoint('/reports/2020-09-04/schedules', method='POST')
    def create_report_schedule(self, **kwargs):
        """
        Creates a report schedule. If a report schedule with the same report type and marketplace IDs already exists, it will be cancelled and replaced with this one.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0222 | 10 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        :param kwargs:
        :return:
        """
        return CreateReportScheduleResponse(**self._request(kwargs.pop('path'), data=kwargs).json())

    @sp_endpoint('/reports/2020-09-04/schedules/{}', method='DELETE')
    def delete_report_schedule(self, schedule_id, **kwargs):
        """
        Cancels the report schedule that you specify.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0222 | 10 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        :param schedule_id:
        :param kwargs:
        :return:
        """
        return DeleteSubscriptionByIdResponse(
            **self._request(fill_query_params(kwargs.pop('path'), schedule_id), params=kwargs).json()
        )

    @sp_endpoint('/reports/2020-09-04/schedules/{}')
    def get_report_schedule(self, schedule_id, **kwargs):
        """
        Cancels the report schedule that you specify.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0222 | 10 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        :param schedule_id:
        :param kwargs:
        :return:
        """
        return GetSubscriptionByIdResponse(
            **self._request(fill_query_params(kwargs.pop('path'), schedule_id), params=kwargs).json()
        )

    @staticmethod
    def decrypt_report_document(url, initialization_vector, key, encryption_standard):
        """
        Decrypts a report document, currently AES encryption is implemented
        :param url:
        :param initialization_vector:
        :param key:
        :param encryption_standard:
        :return:
        """
        if encryption_standard == 'AES':
            return decrypt_aes(requests.get(url).content, key, initialization_vector).decode('iso-8859-1')
        raise SellingApiException([{
            'message': 'Only AES decryption is implemented. Contribute: https://github.com/saleweaver/python-sp-api'
        }])
