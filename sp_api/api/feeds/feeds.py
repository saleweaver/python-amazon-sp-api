import os
import struct
from io import BytesIO

import requests

from sp_api.api.feeds.models.create_feed_document_response import CreateFeedDocumentResponse
from sp_api.api.feeds.models.create_feed_response import CreateFeedResponse
from sp_api.api.feeds.models.get_feed_document_response import GetFeedDocumentResponse
from sp_api.api.feeds.models.get_feed_response import GetFeedResponse
from sp_api.base import Client, sp_endpoint, Marketplaces, fill_query_params, SellingApiException

import zlib

from sp_api.base.helpers import encrypt_aes, decrypt_aes


class Feeds(Client):
    """
    The Selling Partner API for Feeds lets you upload data to Amazon on behalf of a selling partner.

    :link: https://github.com/amzn/selling-partner-api-docs/tree/main/references/feeds-api
    """
    def __init__(self, marketplace=Marketplaces.US, *, refresh_token=None, account='default', credentials=None):
        super().__init__(marketplace, refresh_token, account, credentials)

    @sp_endpoint('/feeds/2020-09-04/feeds', method='POST')
    def create_feed(self, feed_type: str, input_feed_document_id: str, **kwargs) -> CreateFeedResponse:
        """
        create_feed(self, feed_type: str, input_feed_document_id: str, **kwargs) -> CreateFeedResponse

        Creates a feed. Encrypt and upload the contents of the feed document before calling this operation.

        **Usage Plan:**

        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        0.0083                                  15
        ======================================  ==============

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            feed_type: https://github.com/amzn/selling-partner-api-docs/blob/main/references/feeds-api/feedType_string_array_values.md
            input_feed_document_id: str
            **kwargs:

        Returns:
            CreateFeedResponse:
        """
        data = {
            'feedType': feed_type,
            'inputFeedDocumentId': input_feed_document_id,
            **kwargs
        }
        return CreateFeedResponse(**self._request(kwargs.get('path'), data=data).json())

    @sp_endpoint('/feeds/2020-09-04/documents', method='POST')
    def create_feed_document(self, file, content_type='text/tsv', **kwargs) -> CreateFeedDocumentResponse:
        """
        create_feed_document(self, file: File or FileLike, content_type='text/tsv', **kwargs) -> CreateFeedDocumentResponse
        Creates a feed document for the feed type that you specify.
        This method also encrypts and uploads the file you specify.

        **Usage Plan:**

        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        0.0083                                  15
        ======================================  ==============

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            file: File or File like object
            content_type: str
            **kwargs:

        Returns:
            CreateFeedDocumentResponse:

        """
        data = {
            'contentType': content_type
        }
        response = CreateFeedDocumentResponse(**self._request(kwargs.get('path'), data={**data, **kwargs}).json())
        upload = requests.put(
            response.payload.get('url'),
            data=encrypt_aes(file,
                             response.payload.get('encryptionDetails').get('key'),
                             response.payload.get('encryptionDetails').get('initializationVector')
                             ),
            headers={'Content-Type': content_type}
        )
        if 200 <= upload.status_code < 300:
            return response
        raise SellingApiException('Error uploading file')

    def submit_feed(self, feed_type, file, content_type='text/tsv', **kwargs) -> [CreateFeedDocumentResponse, CreateFeedResponse]:
        """
        submit_feed(self, feed_type: str, file: File or File like, content_type='text/tsv', **kwargs) -> [CreateFeedDocumentResponse, CreateFeedResponse]
        This method combines `create_feed_document` and `create_feed`.

        It uploads the encrypted file and sends the feed to amazon

        **Usage Plan:**

        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        0.0083                                  15
        ======================================  ==============


        Args:
            feed_type:
            file:
            content_type:
            **kwargs:

        Returns:
            [CreateFeedDocumentResponse, CreateFeedResponse]:
        """
        document_response = self.create_feed_document(file, content_type)
        return document_response, self.create_feed(feed_type, document_response.payload.get('feedDocumentId'), **kwargs)

    @sp_endpoint('/feeds/2020-09-04/feeds/{}')
    def get_feed(self, feed_id: str, **kwargs) -> GetFeedResponse:
        """
        get_feed(self, feed_id: str, **kwargs) -> GetFeedResponse
        Returns feed details (including the resultDocumentId, if available) for the feed that you specify.

        **Usage Plan:**

        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        2                                       15
        ======================================  ==============

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            feed_id: str
            **kwargs:

        Returns:
            GetFeedResponse:
        """
        return GetFeedResponse(**self._request(fill_query_params(kwargs.pop('path'), feed_id), params=kwargs,
                                               add_marketplace=False).json())

    @sp_endpoint('/feeds/2020-09-04/documents/{}')
    def get_feed_result_document(self, feed_id, **kwargs) -> str:
        """
        Returns the decrypted, unpacked FeedResponse

         **Usage Plan:**

        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        0.0222                                  10
        ======================================  ==============


        Args:
            feed_id: str
            **kwargs:

        Returns:
            str: The feed results' contents
        """
        response = GetFeedDocumentResponse(
            **self._request(fill_query_params(kwargs.pop('path'), feed_id), params=kwargs,
                            add_marketplace=False).json())
        url = response.payload.get('url')
        decrypted = decrypt_aes(
            requests.get(url).content,
            response.payload.get('encryptionDetails').get('key'),
            response.payload.get('encryptionDetails').get('initializationVector')
        )

        if 'compressionAlgorithm' in response.payload:
            return zlib.decompress(bytearray(decrypted), 15 + 32).decode('iso-8859-1')
        return decrypted.decode('iso-8859-1')
