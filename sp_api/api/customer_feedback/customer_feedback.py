from sp_api.base import Client, sp_endpoint, ApiResponse, fill_query_params


class CustomerFeedback(Client):
    """
    The Selling Partner API for CustomerFeedback - 2024-06-01

    The Selling Partner API for Customer Feedback (Customer Feedback API) provides information about customer reviews and returns at both the item and browse node level.
    """

    @sp_endpoint(
        "/customerFeedback/2024-06-01/items/{}/reviews/topics", method="GET"
    )
    def get_item_review_topics(
        self, asin, *args, **kwargs
    ) -> ApiResponse:
        """
        Retrieve an item's ten most positive and ten most negative review topics.
        """

        return self._request(
            fill_query_params(kwargs.pop('path'), asin), params=kwargs
        )

    @sp_endpoint("/customerFeedback/2024-06-01/items/{}/browseNode", method="GET")
    def get_item_browse_node(self, asin, *args, **kwargs) -> ApiResponse:
        """
        This API returns the associated browse node of the requested ASIN. A browse node is a location in a browse tree that is used for navigation, product classification, and website content on the Amazon retail website.
        """

        return self._request(
            fill_query_params(kwargs.pop('path'), asin), params=kwargs
        )


    @sp_endpoint(
        "/customerFeedback/2024-06-01/browseNodes/{}/reviews/topics",
        method="GET",
    )
    def get_browse_node_review_topics(
        self, browseNodeId, *args, **kwargs
    ) -> ApiResponse:
        """
        Retrieve a browse node's ten most positive and ten most negative review topics.
        """

        return self._request(
            fill_query_params(kwargs.pop('path'), browseNodeId), params=kwargs
        )


    @sp_endpoint(
        "/customerFeedback/2024-06-01/items/{}/reviews/trends", method="GET"
    )
    def get_item_review_trends(
        self, asin, *args, **kwargs
    ) -> ApiResponse:
        """
        Retrieve an item's positive and negative review trends for the past six months.
        """

        return self._request(
            fill_query_params(kwargs.pop('path'), asin), params=kwargs
        )


    @sp_endpoint(
        "/customerFeedback/2024-06-01/browseNodes/{}/reviews/trends",
        method="GET",
    )
    def get_browse_node_review_trends(
        self, browseNodeId, *args, **kwargs
    ) -> ApiResponse:
        """
        Retrieve the positive and negative review trends of items in a browse node for the past six months.
        """

        return self._request(
            fill_query_params(kwargs.pop('path'), browseNodeId), params=kwargs
        )

    @sp_endpoint(
        "/customerFeedback/2024-06-01/browseNodes/{}/returns/topics",
        method="GET",
    )
    def get_browse_node_return_topics(
        self, browseNodeId, *args, **kwargs
    ) -> ApiResponse:
        """
        Retrieve the topics that customers mention when they return items in a browse node.
        """

        return self._request(
            fill_query_params(kwargs.pop('path'), browseNodeId), params=kwargs
        )

    @sp_endpoint(
        "/customerFeedback/2024-06-01/browseNodes/{}/returns/trends",
        method="GET",
    )
    def get_browse_node_return_trends(
        self, browseNodeId, *args, **kwargs
    ) -> ApiResponse:
        """
        Retrieve the trends of topics that customers mention when they return items in a browse node.
        """

        return self._request(
            fill_query_params(kwargs.pop('path'), browseNodeId), params=kwargs
        )
