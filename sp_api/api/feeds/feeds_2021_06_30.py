import zlib

import httpx

from sp_api.base import Client, sp_endpoint, fill_query_params, ApiResponse
from sp_api.util import should_add_marketplace


class FeedsV20210630(Client):
    """
    Feeds SP-API Client
    :link:

    The Selling Partner API for Feeds lets you upload data to Amazon on behalf of a selling partner.
    """

    @sp_endpoint("/feeds/2021-06-30/feeds", method="GET")
    def get_feeds(self, **kwargs) -> ApiResponse:
        """
        get_feeds(self, **kwargs) -> ApiResponse
        
        Returns feed details for the feeds that match the filters that you specify.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        0.0222                                  10
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                FeedsV20210630().get_feeds()
        
        Args:
            key feedTypes: object |  A list of feed types used to filter feeds. When feedTypes is provided, the other filter parameters (processingStatuses, marketplaceIds, createdSince, createdUntil) and pageSize may also be provided. Either feedTypes or nextToken is required.
            key marketplaceIds: object |  A list of marketplace identifiers used to filter feeds. The feeds returned will match at least one of the marketplaces that you specify.
            key pageSize: object |  The maximum number of feeds to return in a single call.
            key processingStatuses: object |  A list of processing statuses used to filter feeds.
            key createdSince: object |  The earliest feed creation date and time for feeds included in the response, in ISO 8601 format. The default is 90 days ago. Feeds are retained for a maximum of 90 days.
            key createdUntil: object |  The latest feed creation date and time for feeds included in the response, in ISO 8601 format. The default is now.
            key nextToken: object |  A string token returned in the response to your previous request. nextToken is returned when the number of results exceeds the specified pageSize value. To get the next page of results, call the getFeeds operation and include this token as the only parameter. Specifying nextToken with any other parameters will cause the request to fail.
        
        Returns:
            ApiResponse
        """

        add_marketplace = should_add_marketplace(kwargs, "nextToken")
        return self._request(
            kwargs.pop("path"), params=kwargs, add_marketplace=add_marketplace
        )

    def submit_feed(
        self, feed_type, file, content_type="text/tsv", **kwargs
    ) -> [ApiResponse, ApiResponse]:
        """
        submit_feed(self, feed_type, file, content_type, **kwargs) -> [ApiResponse, ApiResponse]
        
        Combines `create_feed_document` and `create_feed`, uploads the file and sends the feed to amazon.
        
        Examples:
            literal blocks::
            
                FeedsV20210630().submit_feed("value", "value", "value")
        
        Args:
            feed_type:  | required
            file:  | required
            content_type:  | required
            **kwargs:
        
        Returns:
            [ApiResponse, ApiResponse]
        """
        document_response = self.create_feed_document(file, content_type)
        return document_response, self.create_feed(
            feed_type, document_response.payload.get("feedDocumentId"), **kwargs
        )

    @sp_endpoint("/feeds/2021-06-30/feeds", method="POST")
    def create_feed(self, feed_type, input_feed_document_id, **kwargs) -> ApiResponse:
        """
        create_feed(self, feed_type, input_feed_document_id, **kwargs) -> ApiResponse
        
        Creates a feed. Upload the contents of the feed document before calling this operation.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        0.0083                                  15
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                FeedsV20210630().create_feed("value", "value")
        
        Args:
            body: CreateFeedSpecification | required Information required to create the feed.
        
        Returns:
            ApiResponse
        """
        data = {
            "feedType": feed_type,
            "inputFeedDocumentId": input_feed_document_id,
            **kwargs,
        }
        return self._request(kwargs.pop("path"), data=data)

    @sp_endpoint("/feeds/2021-06-30/feeds/{}", method="DELETE")
    def cancel_feed(self, feedId, **kwargs) -> ApiResponse:
        """
        cancel_feed(self, feedId, **kwargs) -> ApiResponse
        
        Cancels the feed that you specify. Only feeds with `processingStatus=IN_QUEUE` can be cancelled. Cancelled feeds are returned in subsequent calls to the [`getFeed`](https://developer-docs.amazon.com/sp-api/reference/getfeed) and [`getFeeds`](https://developer-docs.amazon.com/sp-api/reference/getfeeds) operations.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        2                                       15
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                FeedsV20210630().cancel_feed("value")
        
        Args:
            feedId: object | required The identifier for the feed. This identifier is unique only in combination with a seller ID.
        
        Returns:
            ApiResponse
        """

        return self._request(fill_query_params(kwargs.pop("path"), feedId), data=kwargs)

    @sp_endpoint("/feeds/2021-06-30/feeds/{}", method="GET")
    def get_feed(self, feedId, **kwargs) -> ApiResponse:
        """
        get_feed(self, feedId, **kwargs) -> ApiResponse
        
        Returns feed details (including the `resultDocumentId`, if available) for the feed that you specify.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        2                                       15
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                FeedsV20210630().get_feed("value")
        
        Args:
            feedId: object | required The identifier for the feed. This identifier is unique only in combination with a seller ID.
        
        Returns:
            ApiResponse
        """

        return self._request(
            fill_query_params(kwargs.pop("path"), feedId),
            params=kwargs,
            add_marketplace=False,
        )

    @sp_endpoint("/feeds/2021-06-30/documents", method="POST")
    def create_feed_document(self, file, content_type, **kwargs) -> ApiResponse:
        """
        create_feed_document(self, file, content_type, **kwargs) -> ApiResponse
        
        Creates a feed document for the feed type that you specify. This operation returns a presigned URL for uploading the feed document contents. It also returns a `feedDocumentId` value that you can pass in with a subsequent call to the [`createFeed`](https://developer-docs.amazon.com/sp-api/reference/createfeed) operation.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        0.5                                     15
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                FeedsV20210630().create_feed_document("value", "value")
        
        Args:
            body: CreateFeedDocumentSpecification | required Specifies the content type for the createFeedDocument operation.
        
        Returns:
            ApiResponse
        """
        data = {"contentType": kwargs.get("contentType", content_type)}
        response = self._request(kwargs.get("path"), data={**data, **kwargs})

        if file is None:
            return response

        upload_data = file.read()
        try:
            upload_data = upload_data.encode("iso-8859-1")
        except AttributeError:
            pass
        with httpx.Client() as client:
            upload = client.put(
                response.payload.get("url"),
                content=upload_data,
                headers={"Content-Type": content_type},
            )
        if 200 <= upload.status_code < 300:
            return response
        from sp_api.base.exceptions import SellingApiException

        raise SellingApiException(
            headers=upload.headers, error=upload.json().get("errors")
        )

    @sp_endpoint("/feeds/2021-06-30/documents/{}", method="GET")
    def get_feed_document(self, feedDocumentId, **kwargs) -> str:
        """
        get_feed_document(self, feedDocumentId, **kwargs) -> str
        
        Returns the information required for retrieving a feed document's contents.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        0.0222                                  10
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                FeedsV20210630().get_feed_document("value")
        
        Args:
            feedDocumentId: object | required The identifier of the feed document.
        
        Returns:
            str
        """

        return self.get_feed_result_document(feedDocumentId)

    @sp_endpoint("/feeds/2021-06-30/documents/{}", method="GET")
    def get_feed_result_document(self, feedDocumentId, **kwargs) -> str:
        """
        get_feed_result_document(self, feedDocumentId, **kwargs) -> str
        
        Returns the information required for retrieving a feed document's contents.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        0.0222                                  10
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                FeedsV20210630().get_feed_result_document("value")
        
        Args:
            feedDocumentId: object | required The identifier of the feed document.
        
        Returns:
            str
        """
        response = self._request(
            fill_query_params(kwargs.pop("path"), feedDocumentId),
            params=kwargs,
            add_marketplace=False,
        )
        url = response.payload.get("url")
        with httpx.Client() as client:
            doc_response = client.get(url)

        encoding = (
            doc_response.encoding
            if doc_response and doc_response.encoding
            else "iso-8859-1"
        )
        if encoding.lower() == "windows-31j":
            encoding = "cp932"

        content = doc_response.content
        if "compressionAlgorithm" in response.payload:
            try:
                return zlib.decompress(bytearray(content), 15 + 32).decode(encoding)
            except Exception:
                return content.decode(encoding)
        return content.decode(encoding)
