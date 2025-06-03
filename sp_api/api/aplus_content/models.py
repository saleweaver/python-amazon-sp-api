from sp_api.base import Client, sp_endpoint, fill_query_params, ApiResponse


class AplusContent(Client):

    @sp_endpoint("/aplus/2020-11-01/contentDocuments", method="GET")
    def search_content_documents(self, **kwargs) -> ApiResponse:

        return self._request(kwargs.pop("path"), params=kwargs)

    @sp_endpoint("/aplus/2020-11-01/contentDocuments", method="POST")
    def create_content_document(self, **kwargs) -> ApiResponse:

        return self._request(
            kwargs.pop("path"),
            data=kwargs.pop("body"),
            params=kwargs,
            add_marketplace=False,
        )

    @sp_endpoint("/aplus/2020-11-01/contentDocuments/{}", method="GET")
    def get_content_document(self, contentReferenceKey, **kwargs) -> ApiResponse:

        return self._request(
            fill_query_params(kwargs.pop("path"), contentReferenceKey), params=kwargs
        )

    @sp_endpoint("/aplus/2020-11-01/contentDocuments/{}", method="POST")
    def update_content_document(self, contentReferenceKey, **kwargs) -> ApiResponse:

        return self._request(
            fill_query_params(kwargs.pop("path"), contentReferenceKey),
            data=kwargs.pop("body"),
            params=kwargs,
            add_marketplace=False,
        )

    @sp_endpoint("/aplus/2020-11-01/contentDocuments/{}/asins", method="GET")
    def list_content_document_asin_relations(
        self, contentReferenceKey, **kwargs
    ) -> ApiResponse:

        return self._request(
            fill_query_params(kwargs.pop("path"), contentReferenceKey), params=kwargs
        )

    @sp_endpoint("/aplus/2020-11-01/contentDocuments/{}/asins", method="POST")
    def post_content_document_asin_relations(
        self, contentReferenceKey, **kwargs
    ) -> ApiResponse:

        return self._request(
            fill_query_params(kwargs.pop("path"), contentReferenceKey),
            data=kwargs.pop("body"),
            params=kwargs,
            add_marketplace=False,
        )

    @sp_endpoint("/aplus/2020-11-01/contentAsinValidations", method="POST")
    def validate_content_document_asin_relations(self, **kwargs) -> ApiResponse:
        return self._request(
            kwargs.pop("path"),
            data=kwargs.pop("body"),
            params=kwargs,
            add_marketplace=False,
        )

    @sp_endpoint("/aplus/2020-11-01/contentPublishRecords", method="GET")
    def search_content_publish_records(self, **kwargs) -> ApiResponse:
        return self._request(kwargs.pop("path"), params=kwargs)

    @sp_endpoint(
        "/aplus/2020-11-01/contentDocuments/{}/approvalSubmissions", method="POST"
    )
    def post_content_document_approval_submission(
        self, contentReferenceKey, **kwargs
    ) -> ApiResponse:
        return self._request(
            fill_query_params(kwargs.pop("path"), contentReferenceKey), params=kwargs
        )

    @sp_endpoint(
        "/aplus/2020-11-01/contentDocuments/{}/suspendSubmissions", method="POST"
    )
    def post_content_document_suspend_submission(
        self, contentReferenceKey, **kwargs
    ) -> ApiResponse:
        return self._request(
            fill_query_params(kwargs.pop("path"), contentReferenceKey), data=kwargs
        )
