"""
Common models generated from Swagger/OpenAPI specification.

This file was auto-generated. Do not edit manually.

"""

from datetime import date, datetime
from enum import Enum, auto
from typing import Annotated, Any, Dict, List, Optional, Union
from uuid import UUID

from pydantic import AliasChoices, BaseModel, ConfigDict, Field

from .base_models import (BodyParam, GetRequestSerializer, PathParam,
                          QueryParam, RequestsBaseModel, SpApiBaseModel)

"""
BrowseNodeAllOccurrence

The browse node review occurrence metrics.
"""


class BrowseNodeAllOccurrence(SpApiBaseModel):
    """The browse node review occurrence metrics."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    top_twenty_five_percent_products: Annotated[
        float,
        Field(
            ...,
            validation_alias=AliasChoices(
                "topTwentyFivePercentProducts", "top_twenty_five_percent_products"
            ),
            serialization_alias="topTwentyFivePercentProducts",
            description="The percentage of reviews of the top 25 percent of products in the browse node that mention the topic.",
        ),
    ]

    all_products: Annotated[
        float,
        Field(
            ...,
            validation_alias=AliasChoices("allProducts", "all_products"),
            serialization_alias="allProducts",
            description="The percentage of reviews of products in the browse node that mention the topic.",
        ),
    ]


"""
BrowseNodeAllStarRatingImpact

The effects of a topic on the star ratings in a browse node.
"""


class BrowseNodeAllStarRatingImpact(SpApiBaseModel):
    """The effects of a topic on the star ratings in a browse node."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    top_twenty_five_percent_products: Annotated[
        float,
        Field(
            ...,
            validation_alias=AliasChoices(
                "topTwentyFivePercentProducts", "top_twenty_five_percent_products"
            ),
            serialization_alias="topTwentyFivePercentProducts",
            description="The effect of the topic on the star rating of the top 25 percent of products in the browse node. This value can be positive or negative.",
        ),
    ]

    all_products: Annotated[
        float,
        Field(
            ...,
            validation_alias=AliasChoices("allProducts", "all_products"),
            serialization_alias="allProducts",
            description="The effect of the topic on the star rating of all products in the browse node. This value can be positive or negative.",
        ),
    ]


"""
BrowseNodeOccurrence

The browse node review trend occurrence metrics.
"""


class BrowseNodeOccurrence(SpApiBaseModel):
    """The browse node review trend occurrence metrics."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    all_products: Annotated[
        float,
        Field(
            ...,
            validation_alias=AliasChoices("allProducts", "all_products"),
            serialization_alias="allProducts",
            description="The percentage of reviews of products in the browse node that mention a topic.",
        ),
    ]


"""
BrowseNodeResponse

The response for the `getItemBrowseNode` operation.
"""


class BrowseNodeResponse(SpApiBaseModel):
    """The response for the `getItemBrowseNode` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    browse_node_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("browseNodeId", "browse_node_id"),
            serialization_alias="browseNodeId",
            description="A browse node id is the unique identifier of a given browse node. A browse node is a location in a browse tree that is used for navigation, product classification, and website content.",
        ),
    ]

    display_name: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("displayName", "display_name"),
            serialization_alias="displayName",
            description="The display name of the browse node as visible on the Amazon retail website.",
        ),
    ]


"""
BrowseNodeTrendMetrics

A single browse node review or return trend metric.
"""


class BrowseNodeTrendMetrics(SpApiBaseModel):
    """A single browse node review or return trend metric."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    occurrence_percentage: Annotated[
        "BrowseNodeOccurrence",
        Field(
            ...,
            validation_alias=AliasChoices(
                "occurrencePercentage", "occurrence_percentage"
            ),
            serialization_alias="occurrencePercentage",
            description="The percentage of feedback that mentions the topic.",
        ),
    ]


"""
BrowseNodeReturnTopics

Topics from returns for all items in a browse node.
"""


class BrowseNodeReturnTopics(SpApiBaseModel):
    """Topics from returns for all items in a browse node."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    topic: Annotated[
        str, Field(..., description="The name of the return feedback topic .")
    ]

    browse_node_metrics: Annotated[
        "BrowseNodeTrendMetrics",
        Field(
            ...,
            validation_alias=AliasChoices("browseNodeMetrics", "browse_node_metrics"),
            serialization_alias="browseNodeMetrics",
            description="The browse node return topic metrics.",
        ),
    ]


"""
DateRange

A date range.
"""


class DateRange(SpApiBaseModel):
    """A date range."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    start_date: Annotated[
        datetime,
        Field(
            ...,
            validation_alias=AliasChoices("startDate", "start_date"),
            serialization_alias="startDate",
            description="The start date of the date range in ISO-8601 date/time format.",
        ),
    ]

    end_date: Annotated[
        datetime,
        Field(
            ...,
            validation_alias=AliasChoices("endDate", "end_date"),
            serialization_alias="endDate",
            description="The end date of the date range in ISO-8601 date/time format.",
        ),
    ]


"""
BrowseNodeReturnTopicsResponse

The response for the `getBrowseNodeReturnTopics` operation.
"""


class BrowseNodeReturnTopicsResponse(SpApiBaseModel):
    """The response for the `getBrowseNodeReturnTopics` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    browse_node_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("browseNodeId", "browse_node_id"),
            serialization_alias="browseNodeId",
            description="The requested browse node id. A browse node id is the unique identifier of a given browse node.",
        ),
    ]

    display_name: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("displayName", "display_name"),
            serialization_alias="displayName",
            description="The display name of the browse node, as visible on the Amazon retail website.",
        ),
    ]

    marketplace_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="The requested marketplace id.",
        ),
    ]

    country_code: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("countryCode", "country_code"),
            serialization_alias="countryCode",
            description="The two digit country code of requested marketplace id, in ISO 3166-1 alpha-2 format.",
        ),
    ]

    date_range: Annotated[
        "DateRange",
        Field(
            ...,
            validation_alias=AliasChoices("dateRange", "date_range"),
            serialization_alias="dateRange",
            description="The range of dates during which the returns were made.",
        ),
    ]

    topics: Annotated[
        List["BrowseNodeReturnTopics"],
        Field(..., description="The list of browse node return topics."),
    ]


"""
BrowseNodeReturnTrendPoint

The return metrics for a certain month.
"""


class BrowseNodeReturnTrendPoint(SpApiBaseModel):
    """The return metrics for a certain month."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    date_range: Annotated[
        "DateRange",
        Field(
            ...,
            validation_alias=AliasChoices("dateRange", "date_range"),
            serialization_alias="dateRange",
            description="The range of dates during which the returns were made.",
        ),
    ]

    browse_node_metrics: Annotated[
        "BrowseNodeTrendMetrics",
        Field(
            ...,
            validation_alias=AliasChoices("browseNodeMetrics", "browse_node_metrics"),
            serialization_alias="browseNodeMetrics",
            description="The browse node return metrics.",
        ),
    ]


"""
BrowseNodeReturnTrend

The trend of return topic metrics for all items in the requested browse node.
"""


class BrowseNodeReturnTrend(SpApiBaseModel):
    """The trend of return topic metrics for all items in the requested browse node."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    topic: Annotated[str, Field(..., description="The name of the topic.")]

    trend_metrics: Annotated[
        List["BrowseNodeReturnTrendPoint"],
        Field(
            ...,
            validation_alias=AliasChoices("trendMetrics", "trend_metrics"),
            serialization_alias="trendMetrics",
            description="The browse node return trend metrics.",
        ),
    ]


"""
BrowseNodeReturnTrendsResponse

The response for the `getBrowseNodeReturnTrends` operation.
"""


class BrowseNodeReturnTrendsResponse(SpApiBaseModel):
    """The response for the `getBrowseNodeReturnTrends` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    browse_node_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("browseNodeId", "browse_node_id"),
            serialization_alias="browseNodeId",
            description="The requested browse node id. A browse node id is the unique identifier of a given browse node.",
        ),
    ]

    display_name: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("displayName", "display_name"),
            serialization_alias="displayName",
            description="The display name of the browse node, as visible on the Amazon retail website.",
        ),
    ]

    marketplace_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="The requested marketplace id.",
        ),
    ]

    country_code: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("countryCode", "country_code"),
            serialization_alias="countryCode",
            description="The two digit country code of requested marketplace id, in ISO 3166-1 alpha-2 format.",
        ),
    ]

    date_range: Annotated[
        "DateRange",
        Field(
            ...,
            validation_alias=AliasChoices("dateRange", "date_range"),
            serialization_alias="dateRange",
            description="The range of dates during which the returns were made.",
        ),
    ]

    return_trends: Annotated[
        List["BrowseNodeReturnTrend"],
        Field(
            ...,
            validation_alias=AliasChoices("returnTrends", "return_trends"),
            serialization_alias="returnTrends",
            description="The browse node return trends.",
        ),
    ]


"""
BrowseNodeReviewSubtopicMetrics

The browse node review subtopic metrics.
"""


class BrowseNodeReviewSubtopicMetrics(SpApiBaseModel):
    """The browse node review subtopic metrics."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    occurrence_percentage: Annotated[
        float,
        Field(
            ...,
            validation_alias=AliasChoices(
                "occurrencePercentage", "occurrence_percentage"
            ),
            serialization_alias="occurrencePercentage",
            description="The percentage of reviews that mention the subtopic.",
        ),
    ]


"""
BrowseNodeReviewTopicMetrics

The browse node review topic metrics.
"""


class BrowseNodeReviewTopicMetrics(SpApiBaseModel):
    """The browse node review topic metrics."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    occurrence_percentage: Annotated[
        Optional["BrowseNodeAllOccurrence"],
        Field(
            None,
            validation_alias=AliasChoices(
                "occurrencePercentage", "occurrence_percentage"
            ),
            serialization_alias="occurrencePercentage",
            description="The percentage of reviews that mention a topic. This value is `null` if the topic isn't mentioned enough in the reviews.",
        ),
    ]

    star_rating_impact: Annotated[
        Optional["BrowseNodeAllStarRatingImpact"],
        Field(
            None,
            validation_alias=AliasChoices("starRatingImpact", "star_rating_impact"),
            serialization_alias="starRatingImpact",
            description="The effect a topic has on the browse node's star rating. This value is `null` if the topic doesn't affect the star rating of the browse node.",
        ),
    ]


"""
BrowseNodeSubtopic

The browse node review subtopic.
"""


class BrowseNodeSubtopic(SpApiBaseModel):
    """The browse node review subtopic."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    subtopic: Annotated[
        str, Field(..., description="The name of the browse node review subtopic.")
    ]

    metrics: Annotated[
        "BrowseNodeReviewSubtopicMetrics",
        Field(..., description="The browse node review subtopic metrics."),
    ]

    review_snippets: Annotated[
        Optional[List["str"]],
        Field(
            None,
            validation_alias=AliasChoices("reviewSnippets", "review_snippets"),
            serialization_alias="reviewSnippets",
            description="A list of up to three snippets from reviews that contain the topic. This value is `null` if there aren't enough review snippets for the subtopic.",
        ),
    ]


"""
BrowseNodeReviewTopic

The browse node review topic.
"""


class BrowseNodeReviewTopic(SpApiBaseModel):
    """The browse node review topic."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    topic: Annotated[str, Field(..., description="The name browse node review topic.")]

    browse_node_metrics: Annotated[
        "BrowseNodeReviewTopicMetrics",
        Field(
            ...,
            validation_alias=AliasChoices("browseNodeMetrics", "browse_node_metrics"),
            serialization_alias="browseNodeMetrics",
            description="The percentage of browse node reviews that mention the topic, and the effect the topic has on the star rating.",
        ),
    ]

    review_snippets: Annotated[
        Optional[List["str"]],
        Field(
            None,
            validation_alias=AliasChoices("reviewSnippets", "review_snippets"),
            serialization_alias="reviewSnippets",
            description="A list of up to three snippets from reviews that contain the topic. This value is `null` if there aren't enough review snippets for the topic.",
        ),
    ]

    subtopics: Annotated[
        Optional[List["BrowseNodeSubtopic"]],
        Field(
            None,
            description="A list of the five subtopics that occur most frequently. This value is `null` if there are no subtopics.",
        ),
    ]


"""
BrowseNodeReviewTopics

The 10 most positive and most negative review topics for all items in a browse node.
"""


class BrowseNodeReviewTopics(SpApiBaseModel):
    """The 10 most positive and most negative review topics for all items in a browse node."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    positive_topics: Annotated[
        Optional[List["BrowseNodeReviewTopic"]],
        Field(
            None,
            validation_alias=AliasChoices("positiveTopics", "positive_topics"),
            serialization_alias="positiveTopics",
            description="A list of the most positive review topics. When the `sortBy` query parameter is set to `MENTIONS`, the number of reviews of items within the requested browse node that mention the topic determine the topic's placement in the list. When `sortBy` is set to `STAR_RATING_IMPACT`, the effect that the topic has on the star rating of items within the requested browse node determine placement in the list. This value is `null` if there are not enough positive reviews for the requested browse node. **Max length:** 10",
        ),
    ]

    negative_topics: Annotated[
        Optional[List["BrowseNodeReviewTopic"]],
        Field(
            None,
            validation_alias=AliasChoices("negativeTopics", "negative_topics"),
            serialization_alias="negativeTopics",
            description="A list of the most negative review topics. When the `sortBy` query parameter is set to `MENTIONS`, the number of reviews of items within the requested browse node that mention the topic determine the topic's placement in the list. When `sortBy` is set to `STAR_RATING_IMPACT`, the effect that the topic has on the star rating of items within the requested browse node determine placement in the list. This value is `null` if there are not enough negative reviews for the requested browse node. **Max length:** 10",
        ),
    ]


"""
BrowseNodeReviewTopicsResponse

The response for the `getBrowseNodeReviewTopics` operation.
"""


class BrowseNodeReviewTopicsResponse(SpApiBaseModel):
    """The response for the `getBrowseNodeReviewTopics` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    browse_node_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("browseNodeId", "browse_node_id"),
            serialization_alias="browseNodeId",
            description="The requested browse node id. A browse node id is the unique identifier of a given browse node.",
        ),
    ]

    display_name: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("displayName", "display_name"),
            serialization_alias="displayName",
            description="The display name of the requested browse node id. The display name of the browse node as visible on the Amazon retail website.",
        ),
    ]

    marketplace_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="The requested marketplace id.",
        ),
    ]

    country_code: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("countryCode", "country_code"),
            serialization_alias="countryCode",
            description="The two digit country code of requested marketplace id, in ISO 3166-1 alpha-2 format.",
        ),
    ]

    date_range: Annotated[
        "DateRange",
        Field(
            ...,
            validation_alias=AliasChoices("dateRange", "date_range"),
            serialization_alias="dateRange",
            description="The range of dates in which the reviews were made.",
        ),
    ]

    topics: Annotated[
        "BrowseNodeReviewTopics",
        Field(
            ...,
            description="The most positive and most negative topics for all items in the browse node.",
        ),
    ]


"""
BrowseNodeReviewTrendMetrics

The browse node review topic metrics.
"""


class BrowseNodeReviewTrendMetrics(SpApiBaseModel):
    """The browse node review topic metrics."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    occurrence_percentage: Annotated[
        "BrowseNodeAllOccurrence",
        Field(
            ...,
            validation_alias=AliasChoices(
                "occurrencePercentage", "occurrence_percentage"
            ),
            serialization_alias="occurrencePercentage",
            description="The percent of reviews that mention the topic.",
        ),
    ]


"""
BrowseNodeReviewTrendPoint

The browse node's review metrics for a certain month.
"""


class BrowseNodeReviewTrendPoint(SpApiBaseModel):
    """The browse node's review metrics for a certain month."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    date_range: Annotated[
        "DateRange",
        Field(
            ...,
            validation_alias=AliasChoices("dateRange", "date_range"),
            serialization_alias="dateRange",
            description="The date range of the browse node review trend metric.",
        ),
    ]

    browse_node_metrics: Annotated[
        "BrowseNodeReviewTrendMetrics",
        Field(
            ...,
            validation_alias=AliasChoices("browseNodeMetrics", "browse_node_metrics"),
            serialization_alias="browseNodeMetrics",
            description="The browse node review trend metrics.",
        ),
    ]


"""
BrowseNodeReviewTrend

The trend of review topic metrics for all items in the requested browse node.
"""


class BrowseNodeReviewTrend(SpApiBaseModel):
    """The trend of review topic metrics for all items in the requested browse node."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    topic: Annotated[str, Field(..., description="The name of the topic.")]

    trend_metrics: Annotated[
        List["BrowseNodeReviewTrendPoint"],
        Field(
            ...,
            validation_alias=AliasChoices("trendMetrics", "trend_metrics"),
            serialization_alias="trendMetrics",
            description="The browse node's review trend metrics for the past six months.",
        ),
    ]


"""
BrowseNodeReviewTrends

The 10 most positive and most negative review topics for all items in a browse node.
"""


class BrowseNodeReviewTrends(SpApiBaseModel):
    """The 10 most positive and most negative review topics for all items in a browse node."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    positive_topics: Annotated[
        Optional[List["BrowseNodeReviewTrend"]],
        Field(
            None,
            validation_alias=AliasChoices("positiveTopics", "positive_topics"),
            serialization_alias="positiveTopics",
            description="The trends of the most positive review topics. The percentage of reviews that contain the topic across all products in the requested browse node determine the topic's placement in the list. This value is `null` if there aren't enough positive reviews for the requested browse node. **Max length:** 10",
        ),
    ]

    negative_topics: Annotated[
        Optional[List["BrowseNodeReviewTrend"]],
        Field(
            None,
            validation_alias=AliasChoices("negativeTopics", "negative_topics"),
            serialization_alias="negativeTopics",
            description="The trends of the most negative review topics. The percentage of reviews that contain the topic across all products in the requested browse node determine the topic's placement in the list. This value is `null` if there aren't enough positive reviews for the requested browse node. **Max length:** 10",
        ),
    ]


"""
BrowseNodeReviewTrendsResponse

The response for the `getBrowseNodeReviewTrends` operation.
"""


class BrowseNodeReviewTrendsResponse(SpApiBaseModel):
    """The response for the `getBrowseNodeReviewTrends` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    browse_node_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("browseNodeId", "browse_node_id"),
            serialization_alias="browseNodeId",
            description="The requested browse node id. A browse node id is the unique identifier of a given browse node.",
        ),
    ]

    display_name: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("displayName", "display_name"),
            serialization_alias="displayName",
            description="The display name of the requested browse node id. The display name of the browse node as visible on the Amazon retail website.",
        ),
    ]

    marketplace_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="The requested marketplace id.",
        ),
    ]

    country_code: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("countryCode", "country_code"),
            serialization_alias="countryCode",
            description="The two digit country code of requested marketplace id, in ISO 3166-1 alpha-2 format.",
        ),
    ]

    date_range: Annotated[
        "DateRange",
        Field(
            ...,
            validation_alias=AliasChoices("dateRange", "date_range"),
            serialization_alias="dateRange",
            description="The range of dates during which the reviews were made.",
        ),
    ]

    review_trends: Annotated[
        "BrowseNodeReviewTrends",
        Field(
            ...,
            validation_alias=AliasChoices("reviewTrends", "review_trends"),
            serialization_alias="reviewTrends",
            description="Browse Node review trends.",
        ),
    ]


"""
BrowseNodeStarRatingImpact

The effects of a topic on a browse node's star rating.
"""


class BrowseNodeStarRatingImpact(SpApiBaseModel):
    """The effects of a topic on a browse node's star rating."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    all_products: Annotated[
        float,
        Field(
            ...,
            validation_alias=AliasChoices("allProducts", "all_products"),
            serialization_alias="allProducts",
            description="The effect of the topic on the star rating for all products in this browse node. This value can be positive or negative.",
        ),
    ]


"""
ChildAsinMentionMetrics

The child ASIN review topic mention metrics.
"""


class ChildAsinMentionMetrics(SpApiBaseModel):
    """The child ASIN review topic mention metrics."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    asin: Annotated[
        str, Field(..., description="The child ASIN of the requested item.")
    ]

    number_of_mentions: Annotated[
        int,
        Field(
            ...,
            validation_alias=AliasChoices("numberOfMentions", "number_of_mentions"),
            serialization_alias="numberOfMentions",
            description="The number of times reviews of the child ASIN mention the topic.",
        ),
    ]


"""
ChildAsinMetrics

The review topic metrics for other child ASINs that have the same parent ASIN. This value is `null` if there isn't any child ASIN metric data.
"""


class ChildAsinMetrics(SpApiBaseModel):
    """The review topic metrics for other child ASINs that have the same parent ASIN. This value is `null` if there isn't any child ASIN metric data."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    most_mentions: Annotated[
        Optional["ChildAsinMentionMetrics"],
        Field(
            None,
            validation_alias=AliasChoices("mostMentions", "most_mentions"),
            serialization_alias="mostMentions",
            description="The child ASIN for which reviews mention the topic the greatest number of times, and the number of times reviews mention the topic. This value is `null` if there are no child ASIN metrics.",
        ),
    ]

    least_mentions: Annotated[
        Optional["ChildAsinMentionMetrics"],
        Field(
            None,
            validation_alias=AliasChoices("leastMentions", "least_mentions"),
            serialization_alias="leastMentions",
            description="The child ASIN for which reviews mention the topic the least number of times, and the number of times reviews mention the topic. This value is `null` if there are no child ASIN metrics.",
        ),
    ]


"""
Error

Error response returned when the request is unsuccessful.
"""


class Error(SpApiBaseModel):
    """Error response returned when the request is unsuccessful."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    code: Annotated[
        str,
        Field(
            ...,
            description="An error code that identifies the type of error that occurred.",
        ),
    ]

    message: Annotated[
        str, Field(..., description="A message that describes the error condition.")
    ]

    details: Annotated[
        Optional[str],
        Field(
            None,
            description="Additional details that can help the caller understand or fix the issue.",
        ),
    ]


"""
ErrorList

A list of error responses returned when a request is unsuccessful.
"""


class ErrorList(SpApiBaseModel):
    """A list of error responses returned when a request is unsuccessful."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    errors: Annotated[List["Error"], Field(..., description="List of errors.")]


"""
GetBrowseNodeReturnTopicsRequest

Request parameters for getBrowseNodeReturnTopics
"""


class GetBrowseNodeReturnTopicsRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getBrowseNodeReturnTopics
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    browse_node_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("browseNodeId", "browse_node_id"),
            serialization_alias="browseNodeId",
            description="[PATH] A browse node ID is a unique identifier for a browse node. A browse node is a named location in a browse tree that is used for navigation, product classification, and website content.",
        ),
    ]

    marketplace_id: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="[QUERY] The MarketplaceId is the globally unique identifier of a marketplace, you can refer to the marketplaceId here : https://developer-docs.amazon.com/sp-api/docs/marketplace-ids.",
        ),
    ]


"""
GetBrowseNodeReturnTrendsRequest

Request parameters for getBrowseNodeReturnTrends
"""


class GetBrowseNodeReturnTrendsRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getBrowseNodeReturnTrends
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    browse_node_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("browseNodeId", "browse_node_id"),
            serialization_alias="browseNodeId",
            description="[PATH] A browse node ID is a unique identifier of a browse node. A browse node is a named location in a browse tree that is used for navigation, product classification, and website content.",
        ),
    ]

    marketplace_id: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="[QUERY] The MarketplaceId is the globally unique identifier of a marketplace, you can refer to the marketplaceId here : https://developer-docs.amazon.com/sp-api/docs/marketplace-ids.",
        ),
    ]


"""
GetBrowseNodeReviewTopicsRequest

Request parameters for getBrowseNodeReviewTopics
"""


class GetBrowseNodeReviewTopicsRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getBrowseNodeReviewTopics
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    browse_node_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("browseNodeId", "browse_node_id"),
            serialization_alias="browseNodeId",
            description="[PATH] The ID of a browse node. A browse node is a named location in a browse tree that is used for navigation, product classification, and website content.",
        ),
    ]

    marketplace_id: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="[QUERY] The MarketplaceId is the globally unique identifier of a marketplace, you can refer to the marketplaceId here : https://developer-docs.amazon.com/sp-api/docs/marketplace-ids.",
        ),
    ]

    sort_by: Annotated[
        str,
        QueryParam(),
        Field(
            ...,
            validation_alias=AliasChoices("sortBy", "sort_by"),
            serialization_alias="sortBy",
            description="[QUERY] The metric by which to sort the data in the response.",
        ),
    ]


"""
GetBrowseNodeReviewTrendsRequest

Request parameters for getBrowseNodeReviewTrends
"""


class GetBrowseNodeReviewTrendsRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getBrowseNodeReviewTrends
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    browse_node_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("browseNodeId", "browse_node_id"),
            serialization_alias="browseNodeId",
            description="[PATH] A browse node ID is a unique identifier of a browse node. A browse node is a named location in a browse tree that is used for navigation, product classification, and website content.",
        ),
    ]

    marketplace_id: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="[QUERY] The marketplace ID is the globally unique identifier of a marketplace. For more information, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).",
        ),
    ]


"""
GetItemBrowseNodeRequest

Request parameters for getItemBrowseNode
"""


class GetItemBrowseNodeRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getItemBrowseNode
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    asin: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            description="[PATH] The Amazon Standard Identification Number (ASIN) is the unique identifier of a product within a marketplace.",
        ),
    ]

    marketplace_id: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="[QUERY] The MarketplaceId is the globally unique identifier of a marketplace, you can refer to the marketplaceId here : https://developer-docs.amazon.com/sp-api/docs/marketplace-ids.",
        ),
    ]


"""
GetItemReviewTopicsRequest

Request parameters for getItemReviewTopics
"""


class GetItemReviewTopicsRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getItemReviewTopics
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    asin: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            description="[PATH] The Amazon Standard Identification Number (ASIN) is the unique identifier of a product within a marketplace. The value must be a child ASIN.",
        ),
    ]

    marketplace_id: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="[QUERY] The MarketplaceId is the globally unique identifier of a marketplace, you can refer to the marketplaceId here : https://developer-docs.amazon.com/sp-api/docs/marketplace-ids.",
        ),
    ]

    sort_by: Annotated[
        str,
        QueryParam(),
        Field(
            ...,
            validation_alias=AliasChoices("sortBy", "sort_by"),
            serialization_alias="sortBy",
            description="[QUERY] The metric by which to sort data in the response.",
        ),
    ]


"""
GetItemReviewTrendsRequest

Request parameters for getItemReviewTrends
"""


class GetItemReviewTrendsRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getItemReviewTrends
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    asin: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            description="[PATH] The Amazon Standard Identification Number (ASIN) is the unique identifier of a product within a marketplace. This API takes child ASIN as an input.",
        ),
    ]

    marketplace_id: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="[QUERY] The MarketplaceId is the globally unique identifier of a marketplace, you can refer to the marketplaceId here : https://developer-docs.amazon.com/sp-api/docs/marketplace-ids.",
        ),
    ]


"""
ItemReviewBrowseNodeMetrics

The browse node review topic metrics.
"""


class ItemReviewBrowseNodeMetrics(SpApiBaseModel):
    """The browse node review topic metrics."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    occurrence_percentage: Annotated[
        Optional["BrowseNodeOccurrence"],
        Field(
            None,
            validation_alias=AliasChoices(
                "occurrencePercentage", "occurrence_percentage"
            ),
            serialization_alias="occurrencePercentage",
            description="The percentage of reviews that mention the topic. This value is `null` if reviews do not mention the topic frequently enough.",
        ),
    ]

    star_rating_impact: Annotated[
        Optional["BrowseNodeStarRatingImpact"],
        Field(
            None,
            validation_alias=AliasChoices("starRatingImpact", "star_rating_impact"),
            serialization_alias="starRatingImpact",
            description="The effect of the topic on the star rating of items in the browse node. This value is `null` if the topic does not affect the star rating of the browse node.",
        ),
    ]


"""
ItemReviewSubtopicMetrics

The item review subtopic metrics.
"""


class ItemReviewSubtopicMetrics(SpApiBaseModel):
    """The item review subtopic metrics."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    number_of_mentions: Annotated[
        int,
        Field(
            ...,
            validation_alias=AliasChoices("numberOfMentions", "number_of_mentions"),
            serialization_alias="numberOfMentions",
            description="The number of times that reviews mention the subtopic.",
        ),
    ]

    occurrence_percentage: Annotated[
        float,
        Field(
            ...,
            validation_alias=AliasChoices(
                "occurrencePercentage", "occurrence_percentage"
            ),
            serialization_alias="occurrencePercentage",
            description="The percentage of reviews that mention the subtopic.",
        ),
    ]


"""
ItemReviewSubtopic

Details of the subtopic for an item review topic.
"""


class ItemReviewSubtopic(SpApiBaseModel):
    """Details of the subtopic for an item review topic."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    subtopic: Annotated[str, Field(..., description="The name of the subtopic.")]

    metrics: Annotated[
        "ItemReviewSubtopicMetrics", Field(..., description="The subtopic metrics.")
    ]

    review_snippets: Annotated[
        Optional[List["str"]],
        Field(
            None,
            validation_alias=AliasChoices("reviewSnippets", "review_snippets"),
            serialization_alias="reviewSnippets",
            description="A list of up to three snippets from reviews that contain the subtopic. This value is `null` if there aren't enough review snippets for the subtopic.",
        ),
    ]


"""
ItemReviewTopicMetrics

The item review topic metrics.
"""


class ItemReviewTopicMetrics(SpApiBaseModel):
    """The item review topic metrics."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    number_of_mentions: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices("numberOfMentions", "number_of_mentions"),
            serialization_alias="numberOfMentions",
            description="The number of times that reviews mention the topic. This value is `null` if reviews do not mention the topic frequently enough.",
        ),
    ]

    occurrence_percentage: Annotated[
        Optional[float],
        Field(
            None,
            validation_alias=AliasChoices(
                "occurrencePercentage", "occurrence_percentage"
            ),
            serialization_alias="occurrencePercentage",
            description="The percentage of customer reviews that mention the topic. This value is `null` if reviews do not mention the topic frequently enough.",
        ),
    ]

    star_rating_impact: Annotated[
        Optional[float],
        Field(
            None,
            validation_alias=AliasChoices("starRatingImpact", "star_rating_impact"),
            serialization_alias="starRatingImpact",
            description="The effect of the topic on the star rating of the ASIN. This value can be positive or negative. This value is `null` if the topic does't affect the star rating of the ASIN.",
        ),
    ]


"""
ItemReviewTopic

Details of item review topic.
"""


class ItemReviewTopic(SpApiBaseModel):
    """Details of item review topic."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    topic: Annotated[str, Field(..., description="The name of the item review topic.")]

    asin_metrics: Annotated[
        "ItemReviewTopicMetrics",
        Field(
            ...,
            validation_alias=AliasChoices("asinMetrics", "asin_metrics"),
            serialization_alias="asinMetrics",
            description="The ASIN's review topic metrics.",
        ),
    ]

    parent_asin_metrics: Annotated[
        Optional["ItemReviewTopicMetrics"],
        Field(
            None,
            validation_alias=AliasChoices("parentAsinMetrics", "parent_asin_metrics"),
            serialization_alias="parentAsinMetrics",
            description="The parent ASIN's review topic metrics. This value is `null` if there isn't enough topic data for the parent ASIN.",
        ),
    ]

    browse_node_metrics: Annotated[
        Optional["ItemReviewBrowseNodeMetrics"],
        Field(
            None,
            validation_alias=AliasChoices("browseNodeMetrics", "browse_node_metrics"),
            serialization_alias="browseNodeMetrics",
            description="The browse node's review topic metrics. This value is `null` if there isn't enough topic data for the browse node.",
        ),
    ]

    child_asin_metrics: Annotated[
        Optional["ChildAsinMetrics"],
        Field(
            None,
            validation_alias=AliasChoices("childAsinMetrics", "child_asin_metrics"),
            serialization_alias="childAsinMetrics",
            description="The review topic metrics for other child ASINs that have the same parent ASIN. This value is `null` if there isn't any child ASIN metric data.",
        ),
    ]

    review_snippets: Annotated[
        Optional[List["str"]],
        Field(
            None,
            validation_alias=AliasChoices("reviewSnippets", "review_snippets"),
            serialization_alias="reviewSnippets",
            description="A list of up to three snippets from reviews that contain the topic. This value is `null` if there aren't enough review snippets for the topic.",
        ),
    ]

    subtopics: Annotated[
        Optional[List["ItemReviewSubtopic"]],
        Field(
            None,
            description="A list of up to five top subtopics for the topic. The percentage of customer reviews that mention the subtopic determine the topic's placement in the list. This value is `null` if there are no subtopics.",
        ),
    ]


"""
ItemReviewTopics

The top 10 positive and negative item review topics.
"""


class ItemReviewTopics(SpApiBaseModel):
    """The top 10 positive and negative item review topics."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    positive_topics: Annotated[
        Optional[List["ItemReviewTopic"]],
        Field(
            None,
            validation_alias=AliasChoices("positiveTopics", "positive_topics"),
            serialization_alias="positiveTopics",
            description="A list of the most positive review topics. When the `sortBy` query parameter is set to `MENTIONS`, the number of reviews that mention the topic determines the topic's placement in the list. When `sortBy` is set to `STAR_RATING_IMPACT`, the effect that the topic has on the star rating of the item determines placement in the list. This value is `null` if there are not enough positive reviews for the specified ASIN. **Max length:** 10",
        ),
    ]

    negative_topics: Annotated[
        Optional[List["ItemReviewTopic"]],
        Field(
            None,
            validation_alias=AliasChoices("negativeTopics", "negative_topics"),
            serialization_alias="negativeTopics",
            description="A list of the most negative review topics. When the `sortBy` query parameter is set to `MENTIONS`, the number of reviews that mention the topic determines the topic's placement in the list. When `sortBy` is set to `STAR_RATING_IMPACT`, the effect that the topic has on the star rating of the item determines placement in the list. This value is `null` if there are not enough negative reviews for the specified ASIN. **Max length:** 10",
        ),
    ]


"""
ItemReviewTopicsResponse

The response for the `getItemReviewTopics` operation.
"""


class ItemReviewTopicsResponse(SpApiBaseModel):
    """The response for the `getItemReviewTopics` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    asin: Annotated[
        str,
        Field(
            ...,
            description="The requested ASIN. The Amazon Standard Identification Number (ASIN) is the unique identifier of a product within a marketplace.",
        ),
    ]

    item_name: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("itemName", "item_name"),
            serialization_alias="itemName",
            description="The product title of the requested ASIN.",
        ),
    ]

    marketplace_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="The requested marketplace id.",
        ),
    ]

    country_code: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("countryCode", "country_code"),
            serialization_alias="countryCode",
            description="The two digit country code of the requested marketplace id, in ISO 3166-1 alpha-2 format.",
        ),
    ]

    date_range: Annotated[
        "DateRange",
        Field(
            ...,
            validation_alias=AliasChoices("dateRange", "date_range"),
            serialization_alias="dateRange",
            description="The date range of the item review topics.",
        ),
    ]

    topics: Annotated[
        "ItemReviewTopics",
        Field(..., description="The item review topics for the requested ASIN."),
    ]


"""
ReviewTrendMetrics

The item review trend metrics.
"""


class ReviewTrendMetrics(SpApiBaseModel):
    """The item review trend metrics."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    occurrence_percentage: Annotated[
        float,
        Field(
            ...,
            validation_alias=AliasChoices(
                "occurrencePercentage", "occurrence_percentage"
            ),
            serialization_alias="occurrencePercentage",
            description="The percentage of reviews that mention the topic.",
        ),
    ]


"""
ItemReviewTrendPoint

The review metrics for a certain month.
"""


class ItemReviewTrendPoint(SpApiBaseModel):
    """The review metrics for a certain month."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    date_range: Annotated[
        "DateRange",
        Field(
            ...,
            validation_alias=AliasChoices("dateRange", "date_range"),
            serialization_alias="dateRange",
            description="The date range of the item review trend metric.",
        ),
    ]

    asin_metrics: Annotated[
        "ReviewTrendMetrics",
        Field(
            ...,
            validation_alias=AliasChoices("asinMetrics", "asin_metrics"),
            serialization_alias="asinMetrics",
            description="The ASIN's review trend metrics.",
        ),
    ]

    parent_asin_metrics: Annotated[
        Optional["ReviewTrendMetrics"],
        Field(
            None,
            validation_alias=AliasChoices("parentAsinMetrics", "parent_asin_metrics"),
            serialization_alias="parentAsinMetrics",
            description="The parent ASIN's review trend metrics. This value is `null` if there isn't enough topic data for the parent ASIN.",
        ),
    ]

    browse_node_metrics: Annotated[
        Optional["BrowseNodeTrendMetrics"],
        Field(
            None,
            validation_alias=AliasChoices("browseNodeMetrics", "browse_node_metrics"),
            serialization_alias="browseNodeMetrics",
            description="The browse node's review trend metrics. This value is `null` if there isn't enough topic data for the browse node.",
        ),
    ]


"""
ItemReviewTrend

The trend of review topic metrics for the requested item.
"""


class ItemReviewTrend(SpApiBaseModel):
    """The trend of review topic metrics for the requested item."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    topic: Annotated[str, Field(..., description="The name of the item review topic.")]

    trend_metrics: Annotated[
        List["ItemReviewTrendPoint"],
        Field(
            ...,
            validation_alias=AliasChoices("trendMetrics", "trend_metrics"),
            serialization_alias="trendMetrics",
            description="The item's review trend metrics for the past six months.",
        ),
    ]


"""
ItemReviewTrends

The 10 most positive and most negative review topics for all items in a browse node.
"""


class ItemReviewTrends(SpApiBaseModel):
    """The 10 most positive and most negative review topics for all items in a browse node."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    positive_topics: Annotated[
        Optional[List["ItemReviewTrend"]],
        Field(
            None,
            validation_alias=AliasChoices("positiveTopics", "positive_topics"),
            serialization_alias="positiveTopics",
            description="A list of the most positive review topics. The percentage of reviews that contain the topic determines the topic's placement in the list. This value is `null` if there are not enough positive reviews for the specified ASIN. **Max length:** 10",
        ),
    ]

    negative_topics: Annotated[
        Optional[List["ItemReviewTrend"]],
        Field(
            None,
            validation_alias=AliasChoices("negativeTopics", "negative_topics"),
            serialization_alias="negativeTopics",
            description="A list of the most negative review topics. The percentage of reviews that contain the topic determines the topic's placement in the list. This value is `null` if there are not enough negative reviews for the specified ASIN. **Max length:** 10",
        ),
    ]


"""
ItemReviewTrendsResponse

The response for the `getItemReviewTrends` operation.
"""


class ItemReviewTrendsResponse(SpApiBaseModel):
    """The response for the `getItemReviewTrends` operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    asin: Annotated[
        str,
        Field(
            ...,
            description="The requested ASIN. The Amazon Standard Identification Number (ASIN) is the unique identifier of a product within a marketplace.",
        ),
    ]

    item_name: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("itemName", "item_name"),
            serialization_alias="itemName",
            description="The product title of the requested ASIN.",
        ),
    ]

    marketplace_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="The requested marketplace id.",
        ),
    ]

    country_code: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("countryCode", "country_code"),
            serialization_alias="countryCode",
            description="The two digit country code of the requested marketplace id, in ISO 3166-1 alpha-2 format.",
        ),
    ]

    date_range: Annotated[
        "DateRange",
        Field(
            ...,
            validation_alias=AliasChoices("dateRange", "date_range"),
            serialization_alias="dateRange",
            description="The range of dates in which the reviews were made.",
        ),
    ]

    review_trends: Annotated[
        "ItemReviewTrends",
        Field(
            ...,
            validation_alias=AliasChoices("reviewTrends", "review_trends"),
            serialization_alias="reviewTrends",
            description="The item review trends.",
        ),
    ]


# Rebuild models to resolve forward references
BrowseNodeResponse.model_rebuild()
ItemReviewTopicsResponse.model_rebuild()
ItemReviewTopics.model_rebuild()
ItemReviewTopic.model_rebuild()
ItemReviewSubtopic.model_rebuild()
BrowseNodeReviewSubtopicMetrics.model_rebuild()
ItemReviewSubtopicMetrics.model_rebuild()
ItemReviewBrowseNodeMetrics.model_rebuild()
ItemReviewTopicMetrics.model_rebuild()
ChildAsinMetrics.model_rebuild()
ChildAsinMentionMetrics.model_rebuild()
DateRange.model_rebuild()
BrowseNodeReviewTopicsResponse.model_rebuild()
BrowseNodeReviewTopics.model_rebuild()
BrowseNodeReviewTopic.model_rebuild()
BrowseNodeSubtopic.model_rebuild()
BrowseNodeReviewTopicMetrics.model_rebuild()
BrowseNodeOccurrence.model_rebuild()
BrowseNodeAllStarRatingImpact.model_rebuild()
BrowseNodeStarRatingImpact.model_rebuild()
ItemReviewTrendsResponse.model_rebuild()
ItemReviewTrends.model_rebuild()
ItemReviewTrend.model_rebuild()
ItemReviewTrendPoint.model_rebuild()
ReviewTrendMetrics.model_rebuild()
BrowseNodeReviewTrendsResponse.model_rebuild()
BrowseNodeReviewTrends.model_rebuild()
BrowseNodeReviewTrend.model_rebuild()
BrowseNodeReviewTrendPoint.model_rebuild()
BrowseNodeReviewTrendMetrics.model_rebuild()
BrowseNodeAllOccurrence.model_rebuild()
BrowseNodeReturnTopicsResponse.model_rebuild()
BrowseNodeReturnTopics.model_rebuild()
BrowseNodeReturnTrendsResponse.model_rebuild()
BrowseNodeReturnTrend.model_rebuild()
BrowseNodeReturnTrendPoint.model_rebuild()
BrowseNodeTrendMetrics.model_rebuild()
ErrorList.model_rebuild()
Error.model_rebuild()
GetItemReviewTopicsRequest.model_rebuild()
GetItemBrowseNodeRequest.model_rebuild()
GetBrowseNodeReviewTopicsRequest.model_rebuild()
GetItemReviewTrendsRequest.model_rebuild()
GetBrowseNodeReviewTrendsRequest.model_rebuild()
GetBrowseNodeReturnTopicsRequest.model_rebuild()
GetBrowseNodeReturnTrendsRequest.model_rebuild()
