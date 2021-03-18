import requests
from sp_api.base import Client, sp_endpoint, Marketplaces, fill_query_params, ApiResponse

import zlib

from sp_api.base.helpers import encrypt_aes, decrypt_aes


class Feeds(Client):
    """
    The Selling Partner API for Feeds lets you upload data to Amazon on behalf of a selling partner.

    :link: https://github.com/amzn/selling-partner-api-docs/tree/main/references/feeds-api
    """

    @sp_endpoint('/feeds/2020-09-04/feeds', method='POST')
    def create_feed(self, feed_type: str, input_feed_document_id: str, **kwargs) -> ApiResponse:
        """
        create_feed(self, feed_type: str, input_feed_document_id: str, **kwargs) -> ApiResponse

        Creates a feed. Call `create_feed_document` to upload the feed first.
        `submit_feed` combines both.

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
        return self._request(kwargs.get('path'), data=data)

    @sp_endpoint('/feeds/2020-09-04/documents', method='POST')
    def create_feed_document(self, file, content_type='text/tsv', **kwargs) -> ApiResponse:
        """
        create_feed_document(self, file: File or FileLike, content_type='text/tsv', **kwargs) -> ApiResponse
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
            'contentType': kwargs.get('contentType', content_type)
        }
        response = self._request(kwargs.get('path'), data={**data, **kwargs})
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
        from sp_api.base.exceptions import SellingApiException
        raise SellingApiException(upload.headers)

    def submit_feed(self, feed_type, file, content_type='text/tsv', **kwargs) -> [ApiResponse, ApiResponse]:
        """
        submit_feed(self, feed_type: str, file: File or File like, content_type='text/tsv', **kwargs) -> [ApiResponse, ApiResponse]
        Combines `create_feed_document` and `create_feed`, uploads the encrypted file and sends the feed to amazon.

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
    def get_feed(self, feed_id: str, **kwargs) -> ApiResponse:
        """
        get_feed(self, feed_id: str, **kwargs) -> ApiResponse
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
        return self._request(fill_query_params(kwargs.pop('path'), feed_id), params=kwargs,
                             add_marketplace=False)

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
        response = self._request(fill_query_params(kwargs.pop('path'), feed_id), params=kwargs,
                                 add_marketplace=False)
        url = response.payload.get('url')
        decrypted = decrypt_aes(
            requests.get(url).content,
            response.payload.get('encryptionDetails').get('key'),
            response.payload.get('encryptionDetails').get('initializationVector')
        )

        if 'compressionAlgorithm' in response.payload:
            return zlib.decompress(bytearray(decrypted), 15 + 32).decode('iso-8859-1')
        return decrypted.decode('iso-8859-1')
