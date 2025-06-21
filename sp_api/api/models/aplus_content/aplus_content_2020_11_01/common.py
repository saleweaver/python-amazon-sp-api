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
AplusPaginatedResponse

A token that you use to retrieve the next page of results. To get the next page of results, call the operation with this token and include the same arguments as the call that produced the token. To get a complete list, call this operation until `nextPageToken` is null. Note that this operation can return empty pages.
"""


class AplusPaginatedResponse(SpApiBaseModel):
    """A token that you use to retrieve the next page of results. To get the next page of results, call the operation with this token and include the same arguments as the call that produced the token. To get a complete list, call this operation until `nextPageToken` is null. Note that this operation can return empty pages."""

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow",
        serialize_by_alias=True,
        arbitrary_types_allowed=True,
    )


MessageSet = List["Error"]
"""A set of messages to the user, such as warnings or comments."""


"""
AplusResponse

The base response data for all A+ Content operations when a request is successful or partially successful. Individual operations can extend this with additional data.
"""


class AplusResponse(SpApiBaseModel):
    """The base response data for all A+ Content operations when a request is successful or partially successful. Individual operations can extend this with additional data."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    warnings: Annotated[
        Optional["MessageSet"],
        Field(
            None,
        ),
    ]


Asin = str
"""The Amazon Standard Identification Number (ASIN)."""


AsinBadge = str
"""A flag that provides additional information about an ASIN. This is contextual and can change depending on the request that generated it."""


AsinBadgeSet = List["AsinBadge"]
"""The set of ASIN badges."""


ContentReferenceKeySet = List["ContentReferenceKey"]
"""A set of content reference keys."""


"""
AsinMetadata

The A+ Content ASIN with additional metadata for content management. If you don't include the `includedDataSet` parameter in a call to the `listContentDocumentAsinRelations` operation, the related ASINs are returned without metadata.
"""


class AsinMetadata(SpApiBaseModel):
    """The A+ Content ASIN with additional metadata for content management. If you don't include the `includedDataSet` parameter in a call to the `listContentDocumentAsinRelations` operation, the related ASINs are returned without metadata."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    asin: Annotated[
        "Asin",
        Field(
            ...,
        ),
    ]

    badge_set: Annotated[
        Optional["AsinBadgeSet"],
        Field(
            None,
            validation_alias=AliasChoices("badgeSet", "badge_set"),
            serialization_alias="badgeSet",
        ),
    ]

    parent: Annotated[
        Optional["Asin"],
        Field(
            None,
        ),
    ]

    title: Annotated[
        Optional[str],
        Field(None, description="The title for the ASIN in the Amazon catalog."),
    ]

    image_url: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("imageUrl", "image_url"),
            serialization_alias="imageUrl",
            description="The default image for the ASIN in the Amazon catalog.",
        ),
    ]

    content_reference_key_set: Annotated[
        Optional["ContentReferenceKeySet"],
        Field(
            None,
            validation_alias=AliasChoices(
                "contentReferenceKeySet", "content_reference_key_set"
            ),
            serialization_alias="contentReferenceKeySet",
        ),
    ]


AsinMetadataSet = List["AsinMetadata"]
"""The set of ASIN metadata."""


AsinSet = List["Asin"]
"""The set of ASINs."""


ColorType = str
"""The relative color scheme of your content."""


ContentBadge = str
"""A flag that provides additional information about an A+ Content document."""


ContentBadgeSet = List["ContentBadge"]
"""The set of content badges."""


ContentModuleList = List["ContentModule"]
"""A list of A+ Content modules."""


ContentSubType = str
"""The A+ Content document subtype. This represents a special-purpose type of an A+ Content document. Not every A+ Content document type has a subtype, and subtypes can change at any time."""


ContentType = str
"""The A+ Content document type."""


LanguageTag = str
"""The IETF language tag, which supports the primary language subtag and one secondary language subtag. The secondary language subtag is usually a regional designation. This doesn't support subtags other than the primary and secondary subtags. **Pattern:** ^[a-z]{2,}-[A-Z0-9]{2,}$"""


"""
ContentDocument

The A+ Content document. This is the enhanced content that is published to product detail pages.
"""


class ContentDocument(SpApiBaseModel):
    """The A+ Content document. This is the enhanced content that is published to product detail pages."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    name: Annotated[str, Field(..., description="The A+ Content document name.")]

    content_type: Annotated[
        "ContentType",
        Field(
            ...,
            validation_alias=AliasChoices("contentType", "content_type"),
            serialization_alias="contentType",
        ),
    ]

    content_sub_type: Annotated[
        Optional["ContentSubType"],
        Field(
            None,
            validation_alias=AliasChoices("contentSubType", "content_sub_type"),
            serialization_alias="contentSubType",
        ),
    ]

    locale: Annotated[
        "LanguageTag",
        Field(
            ...,
        ),
    ]

    content_module_list: Annotated[
        "ContentModuleList",
        Field(
            ...,
            validation_alias=AliasChoices("contentModuleList", "content_module_list"),
            serialization_alias="contentModuleList",
        ),
    ]


ContentStatus = str
"""The submission status of the content document."""


MarketplaceId = str
"""The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids)."""


"""
ContentMetadata

The A+ Content document's metadata.
"""


class ContentMetadata(SpApiBaseModel):
    """The A+ Content document's metadata."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    name: Annotated[str, Field(..., description="The A+ Content document's name.")]

    marketplace_id: Annotated[
        Optional["MarketplaceId"],
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
        ),
    ]

    status: Annotated[
        "ContentStatus",
        Field(
            ...,
        ),
    ]

    badge_set: Annotated[
        "ContentBadgeSet",
        Field(
            ...,
            validation_alias=AliasChoices("badgeSet", "badge_set"),
            serialization_alias="badgeSet",
        ),
    ]

    update_time: Annotated[
        datetime,
        Field(
            ...,
            validation_alias=AliasChoices("updateTime", "update_time"),
            serialization_alias="updateTime",
            description="The approximate age of the A+ Content document and metadata.",
        ),
    ]


ContentReferenceKey = str
"""A unique reference key for the A+ Content document. A content reference key cannot form a permalink and might change in the future. A content reference key is not guaranteed to match any A+ content identifier."""


"""
ContentMetadataRecord

The metadata for an A+ Content document, with additional information for content management.
"""


class ContentMetadataRecord(SpApiBaseModel):
    """The metadata for an A+ Content document, with additional information for content management."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    content_reference_key: Annotated[
        "ContentReferenceKey",
        Field(
            ...,
            validation_alias=AliasChoices(
                "contentReferenceKey", "content_reference_key"
            ),
            serialization_alias="contentReferenceKey",
        ),
    ]

    content_metadata: Annotated[
        "ContentMetadata",
        Field(
            ...,
            validation_alias=AliasChoices("contentMetadata", "content_metadata"),
            serialization_alias="contentMetadata",
        ),
    ]


ContentMetadataRecordList = List["ContentMetadataRecord"]
"""A list of A+ Content metadata records."""


ContentModuleType = str
"""The type of A+ Content module."""


"""
IntegerWithUnits

A whole number dimension and its unit of measurement. For example, this can represent 100 pixels.
"""


class IntegerWithUnits(SpApiBaseModel):
    """A whole number dimension and its unit of measurement. For example, this can represent 100 pixels."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    value: Annotated[int, Field(..., description="The dimension value.")]

    units: Annotated[str, Field(..., description="The unit of measurement.")]


"""
ImageDimensions

The dimensions that extend from the top left corner of the image (this applies to cropped and uncropped images). `ImageDimensions` units must be in pixels.
"""


class ImageDimensions(SpApiBaseModel):
    """The dimensions that extend from the top left corner of the image (this applies to cropped and uncropped images). `ImageDimensions` units must be in pixels."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    width: Annotated[
        "IntegerWithUnits",
        Field(
            ...,
        ),
    ]

    height: Annotated[
        "IntegerWithUnits",
        Field(
            ...,
        ),
    ]


"""
ImageOffsets

The top left corner of the cropped image, specified in the original image's coordinate space.
"""


class ImageOffsets(SpApiBaseModel):
    """The top left corner of the cropped image, specified in the original image's coordinate space."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    x: Annotated[
        "IntegerWithUnits",
        Field(
            ...,
        ),
    ]

    y: Annotated[
        "IntegerWithUnits",
        Field(
            ...,
        ),
    ]


"""
ImageCropSpecification

The instructions for optionally cropping an image. If you don't want to crop the image, set the dimensions to the original image size. If the image is cropped and you don't include offset values, the coordinates of the top left corner of the cropped image are set to (0,0) by default.
"""


class ImageCropSpecification(SpApiBaseModel):
    """The instructions for optionally cropping an image. If you don't want to crop the image, set the dimensions to the original image size. If the image is cropped and you don't include offset values, the coordinates of the top left corner of the cropped image are set to (0,0) by default."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    size: Annotated[
        "ImageDimensions",
        Field(
            ...,
        ),
    ]

    offset: Annotated[
        Optional["ImageOffsets"],
        Field(
            None,
        ),
    ]


"""
ImageComponent

A reference to an image, hosted in the A+ Content media library.
"""


class ImageComponent(SpApiBaseModel):
    """A reference to an image, hosted in the A+ Content media library."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    upload_destination_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices(
                "uploadDestinationId", "upload_destination_id"
            ),
            serialization_alias="uploadDestinationId",
            description="This identifier is provided by the [Uploads API](https://developer-docs.amazon.com/sp-api/reference/welcome-to-api-references).",
        ),
    ]

    image_crop_specification: Annotated[
        "ImageCropSpecification",
        Field(
            ...,
            validation_alias=AliasChoices(
                "imageCropSpecification", "image_crop_specification"
            ),
            serialization_alias="imageCropSpecification",
        ),
    ]

    alt_text: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("altText", "alt_text"),
            serialization_alias="altText",
            description="The alternative text for the image.",
        ),
    ]


"""
StandardCompanyLogoModule

The standard company logo image.
"""


class StandardCompanyLogoModule(SpApiBaseModel):
    """The standard company logo image."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    company_logo: Annotated[
        "ImageComponent",
        Field(
            ...,
            validation_alias=AliasChoices("companyLogo", "company_logo"),
            serialization_alias="companyLogo",
        ),
    ]


"""
PlainTextItem

Plain positional text that is used in collections of brief labels and descriptors.
"""


class PlainTextItem(SpApiBaseModel):
    """Plain positional text that is used in collections of brief labels and descriptors."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    position: Annotated[
        int,
        Field(
            ...,
            description="The rank or index of this text item within the collection. Different items cannot occupy the same position within a single collection.",
        ),
    ]

    value: Annotated[str, Field(..., description="The actual plain text.")]


"""
StandardComparisonProductBlock

The A+ Content standard comparison product block.
"""


class StandardComparisonProductBlock(SpApiBaseModel):
    """The A+ Content standard comparison product block."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    position: Annotated[
        int,
        Field(
            ...,
            description="The rank or index of this comparison product block within the module. Different blocks cannot occupy the same position within a single module.",
        ),
    ]

    image: Annotated[
        Optional["ImageComponent"],
        Field(
            None,
        ),
    ]

    title: Annotated[
        Optional[str], Field(None, description="The comparison product title.")
    ]

    asin: Annotated[
        Optional["Asin"],
        Field(
            None,
        ),
    ]

    highlight: Annotated[
        Optional[bool],
        Field(
            None,
            description="When true, indicates that this content block is visually highlighted.",
        ),
    ]

    metrics: Annotated[
        Optional[List["PlainTextItem"]],
        Field(None, description="Comparison metrics for the product."),
    ]


"""
StandardComparisonTableModule

The standard product comparison table.
"""


class StandardComparisonTableModule(SpApiBaseModel):
    """The standard product comparison table."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    product_columns: Annotated[
        Optional[List["StandardComparisonProductBlock"]],
        Field(
            None,
            validation_alias=AliasChoices("productColumns", "product_columns"),
            serialization_alias="productColumns",
        ),
    ]

    metric_row_labels: Annotated[
        Optional[List["PlainTextItem"]],
        Field(
            None,
            validation_alias=AliasChoices("metricRowLabels", "metric_row_labels"),
            serialization_alias="metricRowLabels",
        ),
    ]


DecoratorSet = List["Decorator"]
"""A set of content decorators."""


"""
TextComponent

Rich text content.
"""


class TextComponent(SpApiBaseModel):
    """Rich text content."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    value: Annotated[str, Field(..., description="The actual plain text.")]

    decorator_set: Annotated[
        Optional["DecoratorSet"],
        Field(
            None,
            validation_alias=AliasChoices("decoratorSet", "decorator_set"),
            serialization_alias="decoratorSet",
        ),
    ]


"""
ParagraphComponent

A list of rich text content that is typically presented in a text box.
"""


class ParagraphComponent(SpApiBaseModel):
    """A list of rich text content that is typically presented in a text box."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    text_list: Annotated[
        List["TextComponent"],
        Field(
            ...,
            validation_alias=AliasChoices("textList", "text_list"),
            serialization_alias="textList",
        ),
    ]


"""
StandardImageTextBlock

The A+ Content standard image and text box block.
"""


class StandardImageTextBlock(SpApiBaseModel):
    """The A+ Content standard image and text box block."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    image: Annotated[
        Optional["ImageComponent"],
        Field(
            None,
        ),
    ]

    headline: Annotated[
        Optional["TextComponent"],
        Field(
            None,
        ),
    ]

    body: Annotated[
        Optional["ParagraphComponent"],
        Field(
            None,
        ),
    ]


"""
StandardFourImageTextModule

Four standard images with text, presented across a single row.
"""


class StandardFourImageTextModule(SpApiBaseModel):
    """Four standard images with text, presented across a single row."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    headline: Annotated[
        Optional["TextComponent"],
        Field(
            None,
        ),
    ]

    block1: Annotated[
        Optional["StandardImageTextBlock"],
        Field(
            None,
        ),
    ]

    block2: Annotated[
        Optional["StandardImageTextBlock"],
        Field(
            None,
        ),
    ]

    block3: Annotated[
        Optional["StandardImageTextBlock"],
        Field(
            None,
        ),
    ]

    block4: Annotated[
        Optional["StandardImageTextBlock"],
        Field(
            None,
        ),
    ]


"""
StandardFourImageTextQuadrantModule

Four standard images with text, presented on a grid of four quadrants.
"""


class StandardFourImageTextQuadrantModule(SpApiBaseModel):
    """Four standard images with text, presented on a grid of four quadrants."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    block1: Annotated[
        "StandardImageTextBlock",
        Field(
            ...,
        ),
    ]

    block2: Annotated[
        "StandardImageTextBlock",
        Field(
            ...,
        ),
    ]

    block3: Annotated[
        "StandardImageTextBlock",
        Field(
            ...,
        ),
    ]

    block4: Annotated[
        "StandardImageTextBlock",
        Field(
            ...,
        ),
    ]


"""
StandardHeaderImageTextModule

Standard headline text, an image, and body text.
"""


class StandardHeaderImageTextModule(SpApiBaseModel):
    """Standard headline text, an image, and body text."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    headline: Annotated[
        Optional["TextComponent"],
        Field(
            None,
        ),
    ]

    block: Annotated[
        Optional["StandardImageTextBlock"],
        Field(
            None,
        ),
    ]


"""
StandardImageCaptionBlock

The A+ Content standard image and caption block.
"""


class StandardImageCaptionBlock(SpApiBaseModel):
    """The A+ Content standard image and caption block."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    image: Annotated[
        Optional["ImageComponent"],
        Field(
            None,
        ),
    ]

    caption: Annotated[
        Optional["TextComponent"],
        Field(
            None,
        ),
    ]


"""
StandardTextBlock

The A+ Content standard text box block, which contains a paragraph and a headline.
"""


class StandardTextBlock(SpApiBaseModel):
    """The A+ Content standard text box block, which contains a paragraph and a headline."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    headline: Annotated[
        Optional["TextComponent"],
        Field(
            None,
        ),
    ]

    body: Annotated[
        Optional["ParagraphComponent"],
        Field(
            None,
        ),
    ]


"""
TextItem

Rich positional text that is usually presented as a collection of bullet points.
"""


class TextItem(SpApiBaseModel):
    """Rich positional text that is usually presented as a collection of bullet points."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    position: Annotated[
        int,
        Field(
            ...,
            description="The rank or index of this text item within the collection. Different items cannot occupy the same position within a single collection.",
        ),
    ]

    text: Annotated[
        "TextComponent",
        Field(
            ...,
        ),
    ]


"""
StandardTextListBlock

The A+ Content standard fixed-length list of text, usually presented as bullet points.
"""


class StandardTextListBlock(SpApiBaseModel):
    """The A+ Content standard fixed-length list of text, usually presented as bullet points."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    text_list: Annotated[
        List["TextItem"],
        Field(
            ...,
            validation_alias=AliasChoices("textList", "text_list"),
            serialization_alias="textList",
        ),
    ]


"""
StandardImageSidebarModule

Two images, two paragraphs, and two bulleted lists. One image is smaller and displayed in the sidebar.
"""


class StandardImageSidebarModule(SpApiBaseModel):
    """Two images, two paragraphs, and two bulleted lists. One image is smaller and displayed in the sidebar."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    headline: Annotated[
        Optional["TextComponent"],
        Field(
            None,
        ),
    ]

    image_caption_block: Annotated[
        Optional["StandardImageCaptionBlock"],
        Field(
            None,
            validation_alias=AliasChoices("imageCaptionBlock", "image_caption_block"),
            serialization_alias="imageCaptionBlock",
        ),
    ]

    description_text_block: Annotated[
        Optional["StandardTextBlock"],
        Field(
            None,
            validation_alias=AliasChoices(
                "descriptionTextBlock", "description_text_block"
            ),
            serialization_alias="descriptionTextBlock",
        ),
    ]

    description_list_block: Annotated[
        Optional["StandardTextListBlock"],
        Field(
            None,
            validation_alias=AliasChoices(
                "descriptionListBlock", "description_list_block"
            ),
            serialization_alias="descriptionListBlock",
        ),
    ]

    sidebar_image_text_block: Annotated[
        Optional["StandardImageTextBlock"],
        Field(
            None,
            validation_alias=AliasChoices(
                "sidebarImageTextBlock", "sidebar_image_text_block"
            ),
            serialization_alias="sidebarImageTextBlock",
        ),
    ]

    sidebar_list_block: Annotated[
        Optional["StandardTextListBlock"],
        Field(
            None,
            validation_alias=AliasChoices("sidebarListBlock", "sidebar_list_block"),
            serialization_alias="sidebarListBlock",
        ),
    ]


"""
StandardImageTextOverlayModule

A standard background image with a floating text box.
"""


class StandardImageTextOverlayModule(SpApiBaseModel):
    """A standard background image with a floating text box."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    overlay_color_type: Annotated[
        "ColorType",
        Field(
            ...,
            validation_alias=AliasChoices("overlayColorType", "overlay_color_type"),
            serialization_alias="overlayColorType",
        ),
    ]

    block: Annotated[
        Optional["StandardImageTextBlock"],
        Field(
            None,
        ),
    ]


"""
StandardImageTextCaptionBlock

The A+ Content standard image and text block, with a related caption. The caption might not display on all devices.
"""


class StandardImageTextCaptionBlock(SpApiBaseModel):
    """The A+ Content standard image and text block, with a related caption. The caption might not display on all devices."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    block: Annotated[
        Optional["StandardImageTextBlock"],
        Field(
            None,
        ),
    ]

    caption: Annotated[
        Optional["TextComponent"],
        Field(
            None,
        ),
    ]


"""
StandardMultipleImageTextModule

Standard images with text, presented one at a time. The user clicks on thumbnails to view each block.
"""


class StandardMultipleImageTextModule(SpApiBaseModel):
    """Standard images with text, presented one at a time. The user clicks on thumbnails to view each block."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    blocks: Annotated[
        Optional[List["StandardImageTextCaptionBlock"]],
        Field(
            None,
        ),
    ]


"""
StandardProductDescriptionModule

Standard product description text.
"""


class StandardProductDescriptionModule(SpApiBaseModel):
    """Standard product description text."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    body: Annotated[
        "ParagraphComponent",
        Field(
            ...,
        ),
    ]


"""
StandardHeaderTextListBlock

The A+ standard fixed-length list of text and a related headline.
"""


class StandardHeaderTextListBlock(SpApiBaseModel):
    """The A+ standard fixed-length list of text and a related headline."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    headline: Annotated[
        Optional["TextComponent"],
        Field(
            None,
        ),
    ]

    block: Annotated[
        Optional["StandardTextListBlock"],
        Field(
            None,
        ),
    ]


"""
StandardSingleImageHighlightsModule

A standard image with several paragraphs and a bulleted list.
"""


class StandardSingleImageHighlightsModule(SpApiBaseModel):
    """A standard image with several paragraphs and a bulleted list."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    image: Annotated[
        Optional["ImageComponent"],
        Field(
            None,
        ),
    ]

    headline: Annotated[
        Optional["TextComponent"],
        Field(
            None,
        ),
    ]

    text_block1: Annotated[
        Optional["StandardTextBlock"],
        Field(
            None,
            validation_alias=AliasChoices("textBlock1", "text_block1"),
            serialization_alias="textBlock1",
        ),
    ]

    text_block2: Annotated[
        Optional["StandardTextBlock"],
        Field(
            None,
            validation_alias=AliasChoices("textBlock2", "text_block2"),
            serialization_alias="textBlock2",
        ),
    ]

    text_block3: Annotated[
        Optional["StandardTextBlock"],
        Field(
            None,
            validation_alias=AliasChoices("textBlock3", "text_block3"),
            serialization_alias="textBlock3",
        ),
    ]

    bulleted_list_block: Annotated[
        Optional["StandardHeaderTextListBlock"],
        Field(
            None,
            validation_alias=AliasChoices("bulletedListBlock", "bulleted_list_block"),
            serialization_alias="bulletedListBlock",
        ),
    ]


"""
StandardSingleImageSpecsDetailModule

A standard image with paragraphs, a bulleted list, and extra space for technical details.
"""


class StandardSingleImageSpecsDetailModule(SpApiBaseModel):
    """A standard image with paragraphs, a bulleted list, and extra space for technical details."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    headline: Annotated[
        Optional["TextComponent"],
        Field(
            None,
        ),
    ]

    image: Annotated[
        Optional["ImageComponent"],
        Field(
            None,
        ),
    ]

    description_headline: Annotated[
        Optional["TextComponent"],
        Field(
            None,
            validation_alias=AliasChoices(
                "descriptionHeadline", "description_headline"
            ),
            serialization_alias="descriptionHeadline",
        ),
    ]

    description_block1: Annotated[
        Optional["StandardTextBlock"],
        Field(
            None,
            validation_alias=AliasChoices("descriptionBlock1", "description_block1"),
            serialization_alias="descriptionBlock1",
        ),
    ]

    description_block2: Annotated[
        Optional["StandardTextBlock"],
        Field(
            None,
            validation_alias=AliasChoices("descriptionBlock2", "description_block2"),
            serialization_alias="descriptionBlock2",
        ),
    ]

    specification_headline: Annotated[
        Optional["TextComponent"],
        Field(
            None,
            validation_alias=AliasChoices(
                "specificationHeadline", "specification_headline"
            ),
            serialization_alias="specificationHeadline",
        ),
    ]

    specification_list_block: Annotated[
        Optional["StandardHeaderTextListBlock"],
        Field(
            None,
            validation_alias=AliasChoices(
                "specificationListBlock", "specification_list_block"
            ),
            serialization_alias="specificationListBlock",
        ),
    ]

    specification_text_block: Annotated[
        Optional["StandardTextBlock"],
        Field(
            None,
            validation_alias=AliasChoices(
                "specificationTextBlock", "specification_text_block"
            ),
            serialization_alias="specificationTextBlock",
        ),
    ]


PositionType = str
"""The content's relative positioning."""


"""
StandardSingleSideImageModule

A standard headline and body text with an image on the side.
"""


class StandardSingleSideImageModule(SpApiBaseModel):
    """A standard headline and body text with an image on the side."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    image_position_type: Annotated[
        "PositionType",
        Field(
            ...,
            validation_alias=AliasChoices("imagePositionType", "image_position_type"),
            serialization_alias="imagePositionType",
        ),
    ]

    block: Annotated[
        Optional["StandardImageTextBlock"],
        Field(
            None,
        ),
    ]


"""
StandardTextPairBlock

The A+ Content standard label and description block, which contains a pair of text components.
"""


class StandardTextPairBlock(SpApiBaseModel):
    """The A+ Content standard label and description block, which contains a pair of text components."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    label: Annotated[
        Optional["TextComponent"],
        Field(
            None,
        ),
    ]

    description: Annotated[
        Optional["TextComponent"],
        Field(
            None,
        ),
    ]


"""
StandardTechSpecsModule

The standard table of technical feature names and definitions.
"""


class StandardTechSpecsModule(SpApiBaseModel):
    """The standard table of technical feature names and definitions."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    headline: Annotated[
        Optional["TextComponent"],
        Field(
            None,
        ),
    ]

    specification_list: Annotated[
        List["StandardTextPairBlock"],
        Field(
            ...,
            validation_alias=AliasChoices("specificationList", "specification_list"),
            serialization_alias="specificationList",
            description="The specification list.",
        ),
    ]

    table_count: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices("tableCount", "table_count"),
            serialization_alias="tableCount",
            description="The number of tables you want present. Features are evenly divided between the tables.",
        ),
    ]


"""
StandardTextModule

A standard headline and body text.
"""


class StandardTextModule(SpApiBaseModel):
    """A standard headline and body text."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    headline: Annotated[
        Optional["TextComponent"],
        Field(
            None,
        ),
    ]

    body: Annotated[
        "ParagraphComponent",
        Field(
            ...,
        ),
    ]


"""
StandardThreeImageTextModule

Three standard images with text, presented across a single row.
"""


class StandardThreeImageTextModule(SpApiBaseModel):
    """Three standard images with text, presented across a single row."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    headline: Annotated[
        Optional["TextComponent"],
        Field(
            None,
        ),
    ]

    block1: Annotated[
        Optional["StandardImageTextBlock"],
        Field(
            None,
        ),
    ]

    block2: Annotated[
        Optional["StandardImageTextBlock"],
        Field(
            None,
        ),
    ]

    block3: Annotated[
        Optional["StandardImageTextBlock"],
        Field(
            None,
        ),
    ]


"""
ContentModule

An A+ Content module. An A+ Content document is composed of content modules. The `contentModuleType` property selects which content module types to use.
"""


class ContentModule(SpApiBaseModel):
    """An A+ Content module. An A+ Content document is composed of content modules. The `contentModuleType` property selects which content module types to use."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    content_module_type: Annotated[
        "ContentModuleType",
        Field(
            ...,
            validation_alias=AliasChoices("contentModuleType", "content_module_type"),
            serialization_alias="contentModuleType",
        ),
    ]

    standard_company_logo: Annotated[
        Optional["StandardCompanyLogoModule"],
        Field(
            None,
            validation_alias=AliasChoices(
                "standardCompanyLogo", "standard_company_logo"
            ),
            serialization_alias="standardCompanyLogo",
        ),
    ]

    standard_comparison_table: Annotated[
        Optional["StandardComparisonTableModule"],
        Field(
            None,
            validation_alias=AliasChoices(
                "standardComparisonTable", "standard_comparison_table"
            ),
            serialization_alias="standardComparisonTable",
        ),
    ]

    standard_four_image_text: Annotated[
        Optional["StandardFourImageTextModule"],
        Field(
            None,
            validation_alias=AliasChoices(
                "standardFourImageText", "standard_four_image_text"
            ),
            serialization_alias="standardFourImageText",
        ),
    ]

    standard_four_image_text_quadrant: Annotated[
        Optional["StandardFourImageTextQuadrantModule"],
        Field(
            None,
            validation_alias=AliasChoices(
                "standardFourImageTextQuadrant", "standard_four_image_text_quadrant"
            ),
            serialization_alias="standardFourImageTextQuadrant",
        ),
    ]

    standard_header_image_text: Annotated[
        Optional["StandardHeaderImageTextModule"],
        Field(
            None,
            validation_alias=AliasChoices(
                "standardHeaderImageText", "standard_header_image_text"
            ),
            serialization_alias="standardHeaderImageText",
        ),
    ]

    standard_image_sidebar: Annotated[
        Optional["StandardImageSidebarModule"],
        Field(
            None,
            validation_alias=AliasChoices(
                "standardImageSidebar", "standard_image_sidebar"
            ),
            serialization_alias="standardImageSidebar",
        ),
    ]

    standard_image_text_overlay: Annotated[
        Optional["StandardImageTextOverlayModule"],
        Field(
            None,
            validation_alias=AliasChoices(
                "standardImageTextOverlay", "standard_image_text_overlay"
            ),
            serialization_alias="standardImageTextOverlay",
        ),
    ]

    standard_multiple_image_text: Annotated[
        Optional["StandardMultipleImageTextModule"],
        Field(
            None,
            validation_alias=AliasChoices(
                "standardMultipleImageText", "standard_multiple_image_text"
            ),
            serialization_alias="standardMultipleImageText",
        ),
    ]

    standard_product_description: Annotated[
        Optional["StandardProductDescriptionModule"],
        Field(
            None,
            validation_alias=AliasChoices(
                "standardProductDescription", "standard_product_description"
            ),
            serialization_alias="standardProductDescription",
        ),
    ]

    standard_single_image_highlights: Annotated[
        Optional["StandardSingleImageHighlightsModule"],
        Field(
            None,
            validation_alias=AliasChoices(
                "standardSingleImageHighlights", "standard_single_image_highlights"
            ),
            serialization_alias="standardSingleImageHighlights",
        ),
    ]

    standard_single_image_specs_detail: Annotated[
        Optional["StandardSingleImageSpecsDetailModule"],
        Field(
            None,
            validation_alias=AliasChoices(
                "standardSingleImageSpecsDetail", "standard_single_image_specs_detail"
            ),
            serialization_alias="standardSingleImageSpecsDetail",
        ),
    ]

    standard_single_side_image: Annotated[
        Optional["StandardSingleSideImageModule"],
        Field(
            None,
            validation_alias=AliasChoices(
                "standardSingleSideImage", "standard_single_side_image"
            ),
            serialization_alias="standardSingleSideImage",
        ),
    ]

    standard_tech_specs: Annotated[
        Optional["StandardTechSpecsModule"],
        Field(
            None,
            validation_alias=AliasChoices("standardTechSpecs", "standard_tech_specs"),
            serialization_alias="standardTechSpecs",
        ),
    ]

    standard_text: Annotated[
        Optional["StandardTextModule"],
        Field(
            None,
            validation_alias=AliasChoices("standardText", "standard_text"),
            serialization_alias="standardText",
        ),
    ]

    standard_three_image_text: Annotated[
        Optional["StandardThreeImageTextModule"],
        Field(
            None,
            validation_alias=AliasChoices(
                "standardThreeImageText", "standard_three_image_text"
            ),
            serialization_alias="standardThreeImageText",
        ),
    ]


"""
ContentRecord

A content document with additional information for content management.
"""


class ContentRecord(SpApiBaseModel):
    """A content document with additional information for content management."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    content_reference_key: Annotated[
        "ContentReferenceKey",
        Field(
            ...,
            validation_alias=AliasChoices(
                "contentReferenceKey", "content_reference_key"
            ),
            serialization_alias="contentReferenceKey",
        ),
    ]

    content_metadata: Annotated[
        Optional["ContentMetadata"],
        Field(
            None,
            validation_alias=AliasChoices("contentMetadata", "content_metadata"),
            serialization_alias="contentMetadata",
        ),
    ]

    content_document: Annotated[
        Optional["ContentDocument"],
        Field(
            None,
            validation_alias=AliasChoices("contentDocument", "content_document"),
            serialization_alias="contentDocument",
        ),
    ]


"""
PostContentDocumentRequestBody


"""


class PostContentDocumentRequestBody(SpApiBaseModel):
    """"""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    content_document: Annotated[
        "ContentDocument",
        Field(
            ...,
            validation_alias=AliasChoices("contentDocument", "content_document"),
            serialization_alias="contentDocument",
        ),
    ]


"""
CreateContentDocumentRequest

Request parameters for createContentDocument
"""


class CreateContentDocumentRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for createContentDocument
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    marketplace_id: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="[QUERY] The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).",
        ),
    ]

    post_content_document_request_body: Annotated[
        "PostContentDocumentRequestBody",
        BodyParam(),
        Field(
            ...,
            validation_alias=AliasChoices(
                "postContentDocumentRequestBody", "post_content_document_request_body"
            ),
            serialization_alias="postContentDocumentRequestBody",
            description="[BODY] The content document request details.",
        ),
    ]


DecoratorType = str
"""The type of rich text decorator."""


"""
Decorator

A decorator that is applied to a content string value in order to create rich text.
"""


class Decorator(SpApiBaseModel):
    """A decorator that is applied to a content string value in order to create rich text."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    type: Annotated[
        Optional["DecoratorType"],
        Field(
            None,
        ),
    ]

    offset: Annotated[
        Optional[int],
        Field(
            None,
            description="The starting value of this decorator within the content string. Use zero (`0`) for the first value.",
        ),
    ]

    length: Annotated[
        Optional[int],
        Field(
            None,
            description="The number of content characters to alter with this decorator. Decorators, such as line breaks, can have zero length and fit between characters.",
        ),
    ]

    depth: Annotated[
        Optional[int],
        Field(
            None,
            description="The relative intensity or variation of this decorator. Decorators, such as bullet-points, can have multiple indentation depths.",
        ),
    ]


"""
Error

The error response that is returned when the request is unsuccessful.
"""


class Error(SpApiBaseModel):
    """The error response that is returned when the request is unsuccessful."""

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

The error response that is returned when a request is unsuccessful.
"""


class ErrorList(SpApiBaseModel):
    """The error response that is returned when a request is unsuccessful."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    errors: Annotated[
        List["Error"],
        Field(
            ...,
            description="A list of error responses that are returned when a request is unsuccessful.",
        ),
    ]


# Enum definitions
class IncludedDataSetEnum(str, Enum):
    """Enum for includedDataSet"""

    METADATA = "METADATA"  # The content document's metadata.


"""
GetContentDocumentRequest

Request parameters for getContentDocument
"""


class GetContentDocumentRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getContentDocument
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    content_reference_key: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices(
                "contentReferenceKey", "content_reference_key"
            ),
            serialization_alias="contentReferenceKey",
            description="[PATH] The unique reference key for the A+ Content document. A content reference key cannot form a permalink and might change in the future. A content reference key is not guaranteed to match any A+ Content identifier.",
        ),
    ]

    marketplace_id: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="[QUERY] The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).",
        ),
    ]

    included_data_set: Annotated[
        List["IncludedDataSetEnum"],
        QueryParam(),
        Field(
            ...,
            validation_alias=AliasChoices("includedDataSet", "included_data_set"),
            serialization_alias="includedDataSet",
            description="[QUERY] The set of A+ Content data types to include in the response.",
        ),
    ]


"""
GetContentDocumentResponse


"""


class GetContentDocumentResponse(SpApiBaseModel):
    """"""

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow",
        serialize_by_alias=True,
        arbitrary_types_allowed=True,
    )


# Enum definitions
class IncludedDataSetEnum(str, Enum):
    """Enum for includedDataSet"""

    METADATA = "METADATA"  # The content document's metadata.


"""
ListContentDocumentAsinRelationsRequest

Request parameters for listContentDocumentAsinRelations
"""


class ListContentDocumentAsinRelationsRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for listContentDocumentAsinRelations
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    content_reference_key: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices(
                "contentReferenceKey", "content_reference_key"
            ),
            serialization_alias="contentReferenceKey",
            description="[PATH] The unique reference key for the A+ Content document. A content reference key cannot form a permalink and might change in the future. A content reference key is not guaranteed to match any A+ Content identifier.",
        ),
    ]

    marketplace_id: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="[QUERY] The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).",
        ),
    ]

    included_data_set: Annotated[
        Optional[List["IncludedDataSetEnum"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("includedDataSet", "included_data_set"),
            serialization_alias="includedDataSet",
            description="[QUERY] The set of A+ Content data types to include in the response. If you don't include this parameter, the operation returns the related ASINs without metadata.",
        ),
    ]

    asin_set: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("asinSet", "asin_set"),
            serialization_alias="asinSet",
            description="[QUERY] The set of ASINs.",
        ),
    ]

    page_token: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("pageToken", "page_token"),
            serialization_alias="pageToken",
            description="[QUERY] A token that you use to fetch a specific page when there are multiple pages of results.",
        ),
    ]


"""
ListContentDocumentAsinRelationsResponse


"""


class ListContentDocumentAsinRelationsResponse(SpApiBaseModel):
    """"""

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow",
        serialize_by_alias=True,
        arbitrary_types_allowed=True,
    )


PageToken = str
"""A token that you use to fetch a specific page when there are multiple pages of results."""


"""
PostContentDocumentApprovalSubmissionRequest

Request parameters for postContentDocumentApprovalSubmission
"""


class PostContentDocumentApprovalSubmissionRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for postContentDocumentApprovalSubmission
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    content_reference_key: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices(
                "contentReferenceKey", "content_reference_key"
            ),
            serialization_alias="contentReferenceKey",
            description="[PATH] The unique reference key for the A+ Content document. A content reference key cannot form a permalink and might change in the future. A content reference key is not guaranteed to match any A+ content identifier.",
        ),
    ]

    marketplace_id: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="[QUERY] The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).",
        ),
    ]


"""
PostContentDocumentApprovalSubmissionResponse


"""


class PostContentDocumentApprovalSubmissionResponse(SpApiBaseModel):
    """"""

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow",
        serialize_by_alias=True,
        arbitrary_types_allowed=True,
    )


"""
PostContentDocumentAsinRelationsRequestBody


"""


class PostContentDocumentAsinRelationsRequestBody(SpApiBaseModel):
    """"""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    asin_set: Annotated[
        "AsinSet",
        Field(
            ...,
            validation_alias=AliasChoices("asinSet", "asin_set"),
            serialization_alias="asinSet",
        ),
    ]


"""
PostContentDocumentAsinRelationsRequest

Request parameters for postContentDocumentAsinRelations
"""


class PostContentDocumentAsinRelationsRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for postContentDocumentAsinRelations
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    content_reference_key: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices(
                "contentReferenceKey", "content_reference_key"
            ),
            serialization_alias="contentReferenceKey",
            description="[PATH] The unique reference key for the A+ Content document. A content reference key cannot form a permalink and might change in the future. A content reference key is not guaranteed to match any A+ content identifier.",
        ),
    ]

    marketplace_id: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="[QUERY] The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).",
        ),
    ]

    post_content_document_asin_relations_request_body: Annotated[
        "PostContentDocumentAsinRelationsRequestBody",
        BodyParam(),
        Field(
            ...,
            validation_alias=AliasChoices(
                "postContentDocumentAsinRelationsRequestBody",
                "post_content_document_asin_relations_request_body",
            ),
            serialization_alias="postContentDocumentAsinRelationsRequestBody",
            description="[BODY] The request details for the content document ASIN relations.",
        ),
    ]


"""
PostContentDocumentAsinRelationsResponse


"""


class PostContentDocumentAsinRelationsResponse(SpApiBaseModel):
    """"""

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow",
        serialize_by_alias=True,
        arbitrary_types_allowed=True,
    )


"""
PostContentDocumentResponse


"""


class PostContentDocumentResponse(SpApiBaseModel):
    """"""

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow",
        serialize_by_alias=True,
        arbitrary_types_allowed=True,
    )


"""
PostContentDocumentSuspendSubmissionRequest

Request parameters for postContentDocumentSuspendSubmission
"""


class PostContentDocumentSuspendSubmissionRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for postContentDocumentSuspendSubmission
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    content_reference_key: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices(
                "contentReferenceKey", "content_reference_key"
            ),
            serialization_alias="contentReferenceKey",
            description="[PATH] The unique reference key for the A+ Content document. A content reference key cannot form a permalink and might change in the future. A content reference key is not guaranteed to match any A+ content identifier.",
        ),
    ]

    marketplace_id: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="[QUERY] The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).",
        ),
    ]


"""
PostContentDocumentSuspendSubmissionResponse


"""


class PostContentDocumentSuspendSubmissionResponse(SpApiBaseModel):
    """"""

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow",
        serialize_by_alias=True,
        arbitrary_types_allowed=True,
    )


"""
PublishRecord

The full context for an A+ Content publishing event.
"""


class PublishRecord(SpApiBaseModel):
    """The full context for an A+ Content publishing event."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    marketplace_id: Annotated[
        Optional["MarketplaceId"],
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
        ),
    ]

    locale: Annotated[
        "LanguageTag",
        Field(
            ...,
        ),
    ]

    asin: Annotated[
        "Asin",
        Field(
            ...,
        ),
    ]

    content_type: Annotated[
        "ContentType",
        Field(
            ...,
            validation_alias=AliasChoices("contentType", "content_type"),
            serialization_alias="contentType",
        ),
    ]

    content_sub_type: Annotated[
        Optional["ContentSubType"],
        Field(
            None,
            validation_alias=AliasChoices("contentSubType", "content_sub_type"),
            serialization_alias="contentSubType",
        ),
    ]

    content_reference_key: Annotated[
        "ContentReferenceKey",
        Field(
            ...,
            validation_alias=AliasChoices(
                "contentReferenceKey", "content_reference_key"
            ),
            serialization_alias="contentReferenceKey",
        ),
    ]


PublishRecordList = List["PublishRecord"]
"""A list of A+ Content publishing records."""


"""
SearchContentDocumentsRequest

Request parameters for searchContentDocuments
"""


class SearchContentDocumentsRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for searchContentDocuments
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    marketplace_id: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="[QUERY] The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).",
        ),
    ]

    page_token: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("pageToken", "page_token"),
            serialization_alias="pageToken",
            description="[QUERY] A token that you use to fetch a specific page when there are multiple pages of results.",
        ),
    ]


"""
SearchContentDocumentsResponse


"""


class SearchContentDocumentsResponse(SpApiBaseModel):
    """"""

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow",
        serialize_by_alias=True,
        arbitrary_types_allowed=True,
    )


"""
SearchContentPublishRecordsRequest

Request parameters for searchContentPublishRecords
"""


class SearchContentPublishRecordsRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for searchContentPublishRecords
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    marketplace_id: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="[QUERY] The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).",
        ),
    ]

    asin: Annotated[
        str,
        QueryParam(),
        Field(
            ...,
            description="[QUERY] The Amazon Standard Identification Number (ASIN) is the unique identifier of a product within a marketplace.",
        ),
    ]

    page_token: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("pageToken", "page_token"),
            serialization_alias="pageToken",
            description="[QUERY] A token that you use to fetch a specific page when there are multiple pages of results.",
        ),
    ]


"""
SearchContentPublishRecordsResponse


"""


class SearchContentPublishRecordsResponse(SpApiBaseModel):
    """"""

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow",
        serialize_by_alias=True,
        arbitrary_types_allowed=True,
    )


"""
UpdateContentDocumentRequest

Request parameters for updateContentDocument
"""


class UpdateContentDocumentRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for updateContentDocument
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    content_reference_key: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices(
                "contentReferenceKey", "content_reference_key"
            ),
            serialization_alias="contentReferenceKey",
            description="[PATH] The unique reference key for the A+ Content document. A content reference key cannot form a permalink and might change in the future. A content reference key is not guaranteed to match any A+ Content identifier.",
        ),
    ]

    marketplace_id: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="[QUERY] The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).",
        ),
    ]

    post_content_document_request_body: Annotated[
        "PostContentDocumentRequestBody",
        BodyParam(),
        Field(
            ...,
            validation_alias=AliasChoices(
                "postContentDocumentRequestBody", "post_content_document_request_body"
            ),
            serialization_alias="postContentDocumentRequestBody",
            description="[BODY] The content document request details.",
        ),
    ]


"""
ValidateContentDocumentAsinRelationsRequest

Request parameters for validateContentDocumentAsinRelations
"""


class ValidateContentDocumentAsinRelationsRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for validateContentDocumentAsinRelations
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    marketplace_id: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("marketplaceId", "marketplace_id"),
            serialization_alias="marketplaceId",
            description="[QUERY] The marketplace ID is the globally unique identifier of a marketplace. To find the ID for your marketplace, refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids).",
        ),
    ]

    asin_set: Annotated[
        Optional[List["str"]],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("asinSet", "asin_set"),
            serialization_alias="asinSet",
            description="[QUERY] The set of ASINs.",
        ),
    ]

    post_content_document_request_body: Annotated[
        "PostContentDocumentRequestBody",
        BodyParam(),
        Field(
            ...,
            validation_alias=AliasChoices(
                "postContentDocumentRequestBody", "post_content_document_request_body"
            ),
            serialization_alias="postContentDocumentRequestBody",
            description="[BODY] The content document request details.",
        ),
    ]


"""
ValidateContentDocumentAsinRelationsResponse


"""


class ValidateContentDocumentAsinRelationsResponse(SpApiBaseModel):
    """"""

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow",
        serialize_by_alias=True,
        arbitrary_types_allowed=True,
    )


# Rebuild models to resolve forward references
AplusResponse.model_rebuild()
AplusPaginatedResponse.model_rebuild()
ErrorList.model_rebuild()
Error.model_rebuild()
ContentMetadataRecord.model_rebuild()
ContentMetadata.model_rebuild()
AsinMetadata.model_rebuild()
PublishRecord.model_rebuild()
ImageCropSpecification.model_rebuild()
ImageDimensions.model_rebuild()
ImageOffsets.model_rebuild()
IntegerWithUnits.model_rebuild()
ContentRecord.model_rebuild()
ContentDocument.model_rebuild()
ContentModule.model_rebuild()
StandardCompanyLogoModule.model_rebuild()
StandardComparisonTableModule.model_rebuild()
StandardFourImageTextModule.model_rebuild()
StandardFourImageTextQuadrantModule.model_rebuild()
StandardHeaderImageTextModule.model_rebuild()
StandardImageSidebarModule.model_rebuild()
StandardImageTextOverlayModule.model_rebuild()
StandardMultipleImageTextModule.model_rebuild()
StandardProductDescriptionModule.model_rebuild()
StandardSingleImageHighlightsModule.model_rebuild()
StandardSingleImageSpecsDetailModule.model_rebuild()
StandardSingleSideImageModule.model_rebuild()
StandardTechSpecsModule.model_rebuild()
StandardTextModule.model_rebuild()
StandardThreeImageTextModule.model_rebuild()
StandardComparisonProductBlock.model_rebuild()
StandardHeaderTextListBlock.model_rebuild()
StandardTextListBlock.model_rebuild()
StandardImageTextCaptionBlock.model_rebuild()
StandardImageCaptionBlock.model_rebuild()
StandardImageTextBlock.model_rebuild()
StandardTextBlock.model_rebuild()
StandardTextPairBlock.model_rebuild()
TextItem.model_rebuild()
PlainTextItem.model_rebuild()
ImageComponent.model_rebuild()
ParagraphComponent.model_rebuild()
TextComponent.model_rebuild()
Decorator.model_rebuild()
SearchContentDocumentsResponse.model_rebuild()
GetContentDocumentResponse.model_rebuild()
PostContentDocumentRequestBody.model_rebuild()
PostContentDocumentResponse.model_rebuild()
ListContentDocumentAsinRelationsResponse.model_rebuild()
PostContentDocumentAsinRelationsRequestBody.model_rebuild()
PostContentDocumentAsinRelationsResponse.model_rebuild()
ValidateContentDocumentAsinRelationsResponse.model_rebuild()
SearchContentPublishRecordsResponse.model_rebuild()
PostContentDocumentApprovalSubmissionResponse.model_rebuild()
PostContentDocumentSuspendSubmissionResponse.model_rebuild()
SearchContentDocumentsRequest.model_rebuild()
CreateContentDocumentRequest.model_rebuild()
GetContentDocumentRequest.model_rebuild()
UpdateContentDocumentRequest.model_rebuild()
ListContentDocumentAsinRelationsRequest.model_rebuild()
PostContentDocumentAsinRelationsRequest.model_rebuild()
ValidateContentDocumentAsinRelationsRequest.model_rebuild()
SearchContentPublishRecordsRequest.model_rebuild()
PostContentDocumentApprovalSubmissionRequest.model_rebuild()
PostContentDocumentSuspendSubmissionRequest.model_rebuild()
