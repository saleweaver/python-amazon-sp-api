from sp_api.base import ApiResponse, fill_query_params, sp_endpoint
from sp_api.asyncio.base import AsyncBaseClient


class CustomerFeedback(AsyncBaseClient):
    """
    The Selling Partner API for CustomerFeedback - 2024-06-01

    The Selling Partner API for Customer Feedback (Customer Feedback API) provides information about customer reviews and returns at both the item and browse node level.
    """

    @sp_endpoint(
        "/customerFeedback/2024-06-01/items/{}/reviews/topics", method="GET"
    )
    async def get_item_review_topics(
        self, asin, *args, **kwargs
    ) -> ApiResponse:
        """
        get_item_review_topics(self, asin, *args, **kwargs) -> ApiResponse
        
        Retrieve an item's ten most positive and ten most negative review topics.
        
        Examples:
            literal blocks::
            
                await CustomerFeedback().get_item_review_topics("value")
        
        Args:
            asin: object | required The Amazon Standard Identification Number (ASIN) is the unique identifier of a product within a marketplace. The value must be a child ASIN.
            key marketplaceId: object | required The MarketplaceId is the globally unique identifier of a marketplace, you can refer to the marketplaceId here : https://developer-docs.amazon.com/sp-api/docs/marketplace-ids.
            key sortBy: object | required The metric by which to sort data in the response.
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop('path'), asin), params=kwargs
        )

    @sp_endpoint("/customerFeedback/2024-06-01/items/{}/browseNode", method="GET")
    async def get_item_browse_node(self, asin, *args, **kwargs) -> ApiResponse:
        """
        get_item_browse_node(self, asin, *args, **kwargs) -> ApiResponse
        
        This API returns the associated browse node of the requested ASIN. A browse node is a location in a browse tree that is used for navigation, product classification, and website content on the Amazon retail website.
        
        Examples:
            literal blocks::
            
                await CustomerFeedback().get_item_browse_node("value")
        
        Args:
            asin: object | required The Amazon Standard Identification Number (ASIN) is the unique identifier of a product within a marketplace.
            key marketplaceId: object | required The MarketplaceId is the globally unique identifier of a marketplace, you can refer to the marketplaceId here : https://developer-docs.amazon.com/sp-api/docs/marketplace-ids.
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop('path'), asin), params=kwargs
        )


    @sp_endpoint(
        "/customerFeedback/2024-06-01/browseNodes/{}/reviews/topics",
        method="GET",
    )
    async def get_browse_node_review_topics(
        self, browseNodeId, *args, **kwargs
    ) -> ApiResponse:
        """
        get_browse_node_review_topics(self, browseNodeId, *args, **kwargs) -> ApiResponse
        
        Retrieve a browse node's ten most positive and ten most negative review topics.
        
        Examples:
            literal blocks::
            
                await CustomerFeedback().get_browse_node_review_topics("value")
        
        Args:
            browseNodeId: object | required The ID of a browse node. A browse node is a named location in a browse tree that is used for navigation, product classification, and website content.
            key marketplaceId: object | required The MarketplaceId is the globally unique identifier of a marketplace, you can refer to the marketplaceId here : https://developer-docs.amazon.com/sp-api/docs/marketplace-ids.
            key sortBy: object | required The metric by which to sort the data in the response.
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop('path'), browseNodeId), params=kwargs
        )


    @sp_endpoint(
        "/customerFeedback/2024-06-01/items/{}/reviews/trends", method="GET"
    )
    async def get_item_review_trends(
        self, asin, *args, **kwargs
    ) -> ApiResponse:
        """
        get_item_review_trends(self, asin, *args, **kwargs) -> ApiResponse
        
        Retrieve an item's positive and negative review trends for the past six months.
        
        Examples:
            literal blocks::
            
                await CustomerFeedback().get_item_review_trends("value")
        
        Args:
            asin: object | required The Amazon Standard Identification Number (ASIN) is the unique identifier of a product within a marketplace. This API takes child ASIN as an input.
            key marketplaceId: object | required The MarketplaceId is the globally unique identifier of a marketplace, you can refer to the marketplaceId here : https://developer-docs.amazon.com/sp-api/docs/marketplace-ids.
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop('path'), asin), params=kwargs
        )


    @sp_endpoint(
        "/customerFeedback/2024-06-01/browseNodes/{}/reviews/trends",
        method="GET",
    )
    async def get_browse_node_review_trends(
        self, browseNodeId, *args, **kwargs
    ) -> ApiResponse:
        """
        get_browse_node_review_trends(self, browseNodeId, *args, **kwargs) -> ApiResponse
        
        Retrieve the positive and negative review trends of items in a browse node for the past six months.
        
        Examples:
            literal blocks::
            
                await CustomerFeedback().get_browse_node_review_trends("value")
        
        Args:
            browseNodeId: object | required A browse node ID is a unique identifier of a browse node. A browse node is a named location in a browse tree that is used for navigation, product classification, and website content.
            key marketplaceId: object | required The marketplace ID is the globally unique identifier of a marketplace. For more information, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop('path'), browseNodeId), params=kwargs
        )

    @sp_endpoint(
        "/customerFeedback/2024-06-01/browseNodes/{}/returns/topics",
        method="GET",
    )
    async def get_browse_node_return_topics(
        self, browseNodeId, *args, **kwargs
    ) -> ApiResponse:
        """
        get_browse_node_return_topics(self, browseNodeId, *args, **kwargs) -> ApiResponse
        
        Retrieve the topics that customers mention when they return items in a browse node.
        
        Examples:
            literal blocks::
            
                await CustomerFeedback().get_browse_node_return_topics("value")
        
        Args:
            browseNodeId: object | required A browse node ID is a unique identifier for a browse node. A browse node is a named location in a browse tree that is used for navigation, product classification, and website content.
            key marketplaceId: object | required The MarketplaceId is the globally unique identifier of a marketplace, you can refer to the marketplaceId here : https://developer-docs.amazon.com/sp-api/docs/marketplace-ids.
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop('path'), browseNodeId), params=kwargs
        )

    @sp_endpoint(
        "/customerFeedback/2024-06-01/browseNodes/{}/returns/trends",
        method="GET",
    )
    async def get_browse_node_return_trends(
        self, browseNodeId, *args, **kwargs
    ) -> ApiResponse:
        """
        get_browse_node_return_trends(self, browseNodeId, *args, **kwargs) -> ApiResponse
        
        Retrieve the trends of topics that customers mention when they return items in a browse node.
        
        Examples:
            literal blocks::
            
                await CustomerFeedback().get_browse_node_return_trends("value")
        
        Args:
            browseNodeId: object | required A browse node ID is a unique identifier of a browse node. A browse node is a named location in a browse tree that is used for navigation, product classification, and website content.
            key marketplaceId: object | required The MarketplaceId is the globally unique identifier of a marketplace, you can refer to the marketplaceId here : https://developer-docs.amazon.com/sp-api/docs/marketplace-ids.
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop('path'), browseNodeId), params=kwargs
        )