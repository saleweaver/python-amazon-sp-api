"""
Generated API client from Swagger/OpenAPI specification.
This file was auto-generated. Do not edit manually.
"""

import json
from typing import (Any, Dict, Generic, List, Optional, TypeVar, Union, cast,
                    overload)

import httpx
from pydantic import BaseModel
# Import all models
from sp_api.api.models.customer_feedback.customer_feedback_2024_06_01 import *
from sp_api.base import ApiResponse, Client, fill_query_params, sp_endpoint

T = TypeVar("T")


class CustomerFeedback_V_2024_06_01(Client):
    """
    The Selling Partner API for CustomerFeedback - 2024-06-01

    The Selling Partner API for Customer Feedback (Customer Feedback API) provides information about customer reviews and returns at both the item and browse node level.
    """

    @overload
    def get_item_review_topics(
        self, request: GetItemReviewTopicsRequest, *args, **kwargs
    ) -> ApiResponse[ItemReviewTopicsResponse]:
        """
        Retrieve an item's ten most positive and ten most negative review topics.
        """
        ...

    @sp_endpoint(
        "/customerFeedback/2024-06-01/items/{asin}/reviews/topics", method="GET"
    )
    def get_item_review_topics(
        self, *args, **kwargs
    ) -> ApiResponse[ItemReviewTopicsResponse]:
        """
        Retrieve an item's ten most positive and ten most negative review topics.
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, GetItemReviewTopicsRequest):
            request = GetItemReviewTopicsRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path, query=query, body=body, method=method, _type=ItemReviewTopicsResponse
        )

    @overload
    def get_item_browse_node(
        self, request: GetItemBrowseNodeRequest, *args, **kwargs
    ) -> ApiResponse[BrowseNodeResponse]:
        """
        This API returns the associated browse node of the requested ASIN. A browse node is a location in a browse tree that is used for navigation, product classification, and website content on the Amazon retail website.
        """
        ...

    @sp_endpoint("/customerFeedback/2024-06-01/items/{asin}/browseNode", method="GET")
    def get_item_browse_node(self, *args, **kwargs) -> ApiResponse[BrowseNodeResponse]:
        """
        This API returns the associated browse node of the requested ASIN. A browse node is a location in a browse tree that is used for navigation, product classification, and website content on the Amazon retail website.
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, GetItemBrowseNodeRequest):
            request = GetItemBrowseNodeRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path, query=query, body=body, method=method, _type=BrowseNodeResponse
        )

    @overload
    def get_browse_node_review_topics(
        self, request: GetBrowseNodeReviewTopicsRequest, *args, **kwargs
    ) -> ApiResponse[BrowseNodeReviewTopicsResponse]:
        """
        Retrieve a browse node's ten most positive and ten most negative review topics.
        """
        ...

    @sp_endpoint(
        "/customerFeedback/2024-06-01/browseNodes/{browseNodeId}/reviews/topics",
        method="GET",
    )
    def get_browse_node_review_topics(
        self, *args, **kwargs
    ) -> ApiResponse[BrowseNodeReviewTopicsResponse]:
        """
        Retrieve a browse node's ten most positive and ten most negative review topics.
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, GetBrowseNodeReviewTopicsRequest):
            request = GetBrowseNodeReviewTopicsRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path,
            query=query,
            body=body,
            method=method,
            _type=BrowseNodeReviewTopicsResponse,
        )

    @overload
    def get_item_review_trends(
        self, request: GetItemReviewTrendsRequest, *args, **kwargs
    ) -> ApiResponse[ItemReviewTrendsResponse]:
        """
        Retrieve an item's positive and negative review trends for the past six months.
        """
        ...

    @sp_endpoint(
        "/customerFeedback/2024-06-01/items/{asin}/reviews/trends", method="GET"
    )
    def get_item_review_trends(
        self, *args, **kwargs
    ) -> ApiResponse[ItemReviewTrendsResponse]:
        """
        Retrieve an item's positive and negative review trends for the past six months.
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, GetItemReviewTrendsRequest):
            request = GetItemReviewTrendsRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path, query=query, body=body, method=method, _type=ItemReviewTrendsResponse
        )

    @overload
    def get_browse_node_review_trends(
        self, request: GetBrowseNodeReviewTrendsRequest, *args, **kwargs
    ) -> ApiResponse[BrowseNodeReviewTrendsResponse]:
        """
        Retrieve the positive and negative review trends of items in a browse node for the past six months.
        """
        ...

    @sp_endpoint(
        "/customerFeedback/2024-06-01/browseNodes/{browseNodeId}/reviews/trends",
        method="GET",
    )
    def get_browse_node_review_trends(
        self, *args, **kwargs
    ) -> ApiResponse[BrowseNodeReviewTrendsResponse]:
        """
        Retrieve the positive and negative review trends of items in a browse node for the past six months.
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, GetBrowseNodeReviewTrendsRequest):
            request = GetBrowseNodeReviewTrendsRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path,
            query=query,
            body=body,
            method=method,
            _type=BrowseNodeReviewTrendsResponse,
        )

    @overload
    def get_browse_node_return_topics(
        self, request: GetBrowseNodeReturnTopicsRequest, *args, **kwargs
    ) -> ApiResponse[BrowseNodeReturnTopicsResponse]:
        """
        Retrieve the topics that customers mention when they return items in a browse node.
        """
        ...

    @sp_endpoint(
        "/customerFeedback/2024-06-01/browseNodes/{browseNodeId}/returns/topics",
        method="GET",
    )
    def get_browse_node_return_topics(
        self, *args, **kwargs
    ) -> ApiResponse[BrowseNodeReturnTopicsResponse]:
        """
        Retrieve the topics that customers mention when they return items in a browse node.
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, GetBrowseNodeReturnTopicsRequest):
            request = GetBrowseNodeReturnTopicsRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path,
            query=query,
            body=body,
            method=method,
            _type=BrowseNodeReturnTopicsResponse,
        )

    @overload
    def get_browse_node_return_trends(
        self, request: GetBrowseNodeReturnTrendsRequest, *args, **kwargs
    ) -> ApiResponse[BrowseNodeReturnTrendsResponse]:
        """
        Retrieve the trends of topics that customers mention when they return items in a browse node.
        """
        ...

    @sp_endpoint(
        "/customerFeedback/2024-06-01/browseNodes/{browseNodeId}/returns/trends",
        method="GET",
    )
    def get_browse_node_return_trends(
        self, *args, **kwargs
    ) -> ApiResponse[BrowseNodeReturnTrendsResponse]:
        """
        Retrieve the trends of topics that customers mention when they return items in a browse node.
        """
        path = kwargs.pop("path")
        method = kwargs.pop("method")
        request = args[0]
        if not isinstance(request, GetBrowseNodeReturnTrendsRequest):
            request = GetBrowseNodeReturnTrendsRequest(**kwargs)
        path, body, query = request.create_request(path, self.marketplace_id)

        return self._request(
            path,
            query=query,
            body=body,
            method=method,
            _type=BrowseNodeReturnTrendsResponse,
        )
