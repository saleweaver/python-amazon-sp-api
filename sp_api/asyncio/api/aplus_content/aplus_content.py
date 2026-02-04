import urllib.parse

from sp_api.base import ApiResponse, fill_query_params, sp_endpoint
from sp_api.asyncio.base import AsyncBaseClient


class AplusContent(AsyncBaseClient):
    """
    AplusContent SP-API Client
    :link:

    With the A+ Content API, you can build applications that help selling partners add rich marketing content to their Amazon product detail pages. A+ content helps selling partners share their brand and product story, which helps buyers make informed purchasing decisions. Selling partners assemble content by choosing from content modules and adding images and text.
    """

    @sp_endpoint("/aplus/2020-11-01/contentDocuments", method="GET")
    async def search_content_documents(self, **kwargs) -> ApiResponse:
        """
        search_content_documents(self, **kwargs) -> ApiResponse
        
        Returns a list of all A+ Content documents, including metadata, that are assigned to a selling partner. To get the actual contents of the A+ Content documents, call the `getContentDocument` operation.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        10                                      10
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await AplusContent().search_content_documents()
        
        Args:
            key marketplaceId: object | required The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).
            key pageToken: object |  A token that you use to fetch a specific page when there are multiple pages of results.
        
        Returns:
            ApiResponse
        """

        return await self._request(kwargs.pop("path"), params=kwargs)

    @sp_endpoint("/aplus/2020-11-01/contentDocuments", method="POST")
    async def create_content_document(self, **kwargs) -> ApiResponse:
        """
        create_content_document(self, **kwargs) -> ApiResponse
        
        Creates a new A+ Content document.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        10                                      10
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await AplusContent().create_content_document()
        
        Args:
            key marketplaceId: object | required The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).
            postContentDocumentRequest: PostContentDocumentRequest | required The content document request details.
        
        Returns:
            ApiResponse
        """

        return await self._request(
            kwargs.pop("path"),
            data=kwargs.pop("body"),
            params=kwargs,
            add_marketplace=False,
        )

    @sp_endpoint("/aplus/2020-11-01/contentDocuments/{}", method="GET")
    async def get_content_document(self, contentReferenceKey, **kwargs) -> ApiResponse:
        """
        get_content_document(self, contentReferenceKey, **kwargs) -> ApiResponse
        
        Returns an A+ Content document, if available.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        10                                      10
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await AplusContent().get_content_document("value")
        
        Args:
            contentReferenceKey: object | required The unique reference key for the A+ Content document. A content reference key cannot form a permalink and might change in the future. A content reference key is not guaranteed to match any A+ Content identifier.
            key marketplaceId: object | required The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).
            key includedDataSet: object | required The set of A+ Content data types to include in the response.
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), contentReferenceKey), params=kwargs
        )

    @sp_endpoint("/aplus/2020-11-01/contentDocuments/{}", method="POST")
    async def update_content_document(self, contentReferenceKey, **kwargs) -> ApiResponse:
        """
        update_content_document(self, contentReferenceKey, **kwargs) -> ApiResponse
        
        Updates an existing A+ Content document.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        10                                      10
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await AplusContent().update_content_document("value")
        
        Args:
            contentReferenceKey: object | required The unique reference key for the A+ Content document. A content reference key cannot form a permalink and might change in the future. A content reference key is not guaranteed to match any A+ Content identifier.
            key marketplaceId: object | required The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).
            postContentDocumentRequest: PostContentDocumentRequest | required The content document request details.
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), contentReferenceKey),
            data=kwargs.pop("body"),
            params=kwargs,
            add_marketplace=False,
        )

    @sp_endpoint("/aplus/2020-11-01/contentDocuments/{}/asins", method="GET")
    async def list_content_document_asin_relations(
        self, contentReferenceKey, **kwargs
    ) -> ApiResponse:
        """
        list_content_document_asin_relations(self, contentReferenceKey, **kwargs) -> ApiResponse
        
        Returns a list of ASINs that are related to the specified A+ Content document, if available. If you don't include the `asinSet` parameter, this operation returns all ASINs related to the content document.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        10                                      10
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await AplusContent().list_content_document_asin_relations("value")
        
        Args:
            contentReferenceKey: object | required The unique reference key for the A+ Content document. A content reference key cannot form a permalink and might change in the future. A content reference key is not guaranteed to match any A+ Content identifier.
            key marketplaceId: object | required The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).
            key includedDataSet: object |  The set of A+ Content data types to include in the response. If you don't include this parameter, the operation returns the related ASINs without metadata.
            key asinSet: object |  The set of ASINs.
            key pageToken: object |  A token that you use to fetch a specific page when there are multiple pages of results.
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), contentReferenceKey), params=kwargs
        )

    @sp_endpoint("/aplus/2020-11-01/contentDocuments/{}/asins", method="POST")
    async def post_content_document_asin_relations(
        self, contentReferenceKey, **kwargs
    ) -> ApiResponse:
        """
        post_content_document_asin_relations(self, contentReferenceKey, **kwargs) -> ApiResponse
        
        Replaces all ASINs related to the specified A+ Content document, if available. This operation can add or remove ASINs, depending on the current set of related ASINs. Removing an ASIN will suspend the content document from that ASIN.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        10                                      10
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await AplusContent().post_content_document_asin_relations("value")
        
        Args:
            contentReferenceKey: object | required The unique reference key for the A+ Content document. A content reference key cannot form a permalink and might change in the future. A content reference key is not guaranteed to match any A+ content identifier.
            key marketplaceId: object | required The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).
            postContentDocumentAsinRelationsRequest: PostContentDocumentAsinRelationsRequest | required The request details for the content document ASIN relations.
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), contentReferenceKey),
            data=kwargs.pop("body"),
            params=kwargs,
            add_marketplace=False,
        )

    @sp_endpoint("/aplus/2020-11-01/contentAsinValidations", method="POST")
    async def validate_content_document_asin_relations(self, **kwargs) -> ApiResponse:
        """
        validate_content_document_asin_relations(self, **kwargs) -> ApiResponse
        
        Checks if the A+ Content document is valid for use on a set of ASINs.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        10                                      10
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await AplusContent().validate_content_document_asin_relations()
        
        Args:
            key marketplaceId: object | required The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).
            key asinSet: object |  The set of ASINs.
            postContentDocumentRequest: PostContentDocumentRequest | required The content document request details.
        
        Returns:
            ApiResponse
        """

        return await self._request(
            kwargs.pop("path"),
            data=kwargs.pop("body"),
            params=kwargs,
            add_marketplace=False,
        )

    @sp_endpoint("/aplus/2020-11-01/contentPublishRecords", method="GET")
    async def search_content_publish_records(self, **kwargs) -> ApiResponse:
        """
        search_content_publish_records(self, **kwargs) -> ApiResponse
        
        Searches for A+ Content publishing records, if available.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        10                                      10
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await AplusContent().search_content_publish_records()
        
        Args:
            key marketplaceId: object | required The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).
            key asin: object | required The Amazon Standard Identification Number (ASIN) is the unique identifier of a product within a marketplace.
            key pageToken: object |  A token that you use to fetch a specific page when there are multiple pages of results.
        
        Returns:
            ApiResponse
        """

        return await self._request(kwargs.pop("path"), params=kwargs)

    @sp_endpoint(
        "/aplus/2020-11-01/contentDocuments/{}/approvalSubmissions", method="POST"
    )
    async def post_content_document_approval_submission(
        self, contentReferenceKey, **kwargs
    ) -> ApiResponse:
        """
        post_content_document_approval_submission(self, contentReferenceKey, **kwargs) -> ApiResponse
        
        Submits an A+ Content document for review, approval, and publishing.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        10                                      10
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await AplusContent().post_content_document_approval_submission("value")
        
        Args:
            contentReferenceKey: object | required The unique reference key for the A+ Content document. A content reference key cannot form a permalink and might change in the future. A content reference key is not guaranteed to match any A+ content identifier.
            key marketplaceId: object | required The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), contentReferenceKey), params=kwargs
        )

    @sp_endpoint(
        "/aplus/2020-11-01/contentDocuments/{}/suspendSubmissions", method="POST"
    )
    async def post_content_document_suspend_submission(
        self, contentReferenceKey, **kwargs
    ) -> ApiResponse:
        """
        post_content_document_suspend_submission(self, contentReferenceKey, **kwargs) -> ApiResponse
        
        Submits a request to suspend visible A+ Content. This doesn't delete the content document or the ASIN relations.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        10                                      10
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await AplusContent().post_content_document_suspend_submission("value")
        
        Args:
            contentReferenceKey: object | required The unique reference key for the A+ Content document. A content reference key cannot form a permalink and might change in the future. A content reference key is not guaranteed to match any A+ content identifier.
            key marketplaceId: object | required The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), contentReferenceKey), data=kwargs
        )