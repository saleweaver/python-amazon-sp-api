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
    def __init__(self, marketplace=Marketplaces.US, *, refresh_token=None):
        super().__init__(marketplace, refresh_token)

    @sp_endpoint('/feeds/2020-09-04/feeds', method='POST')
    def create_feed(self, feed_type, input_feed_document_id, **kwargs):
        data = {
            'feedType': feed_type,
            'inputFeedDocumentId': input_feed_document_id,
            **kwargs
        }
        return CreateFeedResponse(**self._request(kwargs.get('path'), data=data).json())

    @sp_endpoint('/feeds/2020-09-04/documents', method='POST')
    def create_feed_document(self, file, content_type='text/tsv', **kwargs):
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

    def submit_feed(self, feed_type, file, content_type='text/tsv', **kwargs):
        document_response = self.create_feed_document(file, content_type)
        return document_response, self.create_feed(feed_type, document_response.payload.get('feedDocumentId'), **kwargs)

    @sp_endpoint('/feeds/2020-09-04/feeds/{}')
    def get_feed(self, feed_id, **kwargs):
        return GetFeedResponse(**self._request(fill_query_params(kwargs.pop('path'), feed_id), params=kwargs,
                                               add_marketplace=False).json())

    @sp_endpoint('/feeds/2020-09-04/documents/{}')
    def get_feed_result_document(self, feed_id, **kwargs):
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
