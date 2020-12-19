import requests
from sp_api.api.reports.models.create_report_response import CreateReportResponse
from sp_api.api.reports.models.get_report_document_response import GetReportDocumentResponse
from sp_api.api.reports.models.get_report_response import GetReportResponse
from sp_api.base import sp_endpoint, fill_query_params, SellingApiException
from sp_api.base import Client, Marketplaces
import base64
from Crypto.Cipher import AES


def decrypt_aes(content, key, iv):
    key = base64.b64decode(key)
    iv = base64.b64decode(iv)
    decrypter = AES.new(key, AES.MODE_CBC, iv)
    return decrypter.decrypt(content).decode('utf-8')


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
            **self._request(fill_query_params(kwargs.pop('path'), report_id)).json()
        )

    @sp_endpoint('/reports/2020-09-04/documents/{}')
    def get_report_document(self, document_id, decrypt: bool = False, **kwargs):
        """
        Returns the information required for retrieving a report document's contents. This includes a presigned URL for the report document as well as the information required to decrypt the document's contents.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0167 | 15 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        :param decrypt:
        :param document_id:
        :param kwargs:
        :return:
        """
        res = self._request(fill_query_params(kwargs.pop('path'), document_id)).json()
        if decrypt:
            res.get('payload').update({
                'document': self.decrypt_report_document(
                    res.get('payload').get('url'),
                    res.get('payload').get('encryptionDetails').get('initializationVector'),
                    res.get('payload').get('encryptionDetails').get('key'),
                    res.get('payload').get('encryptionDetails').get('standard')
                )
            })
        return GetReportDocumentResponse(
            **res
        )

    @staticmethod
    def decrypt_report_document(url, initialization_vector, key, encryption_standard):
        if encryption_standard == 'AES':
            return decrypt_aes(requests.get(url).content, key, initialization_vector)
        raise SellingApiException([{
            'message': 'Only AES decryption is implemented. Contribute: https://github.com/saleweaver/python-sp-api'
        }])
