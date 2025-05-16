from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Field, conint, constr, conlist

# Replace with actual import of RequestBaseModel
from your_project.base import RequestBaseModel

# Enums
class ContentType(str, Enum):
    EBC = "EBC"
    EMC = "EMC"

class ContentStatus(str, Enum):
    APPROVED = "APPROVED"
    DRAFT = "DRAFT"
    REJECTED = "REJECTED"
    SUBMITTED = "SUBMITTED"

class ContentBadge(str, Enum):
    BULK = "BULK"
    GENERATED = "GENERATED"
    LAUNCHPAD = "LAUNCHPAD"
    PREMIUM = "PREMIUM"
    STANDARD = "STANDARD"

class AsinBadge(str, Enum):
    BRAND_NOT_ELIGIBLE = "BRAND_NOT_ELIGIBLE"
    CATALOG_NOT_FOUND = "CATALOG_NOT_FOUND"
    CONTENT_NOT_PUBLISHED = "CONTENT_NOT_PUBLISHED"
    CONTENT_PUBLISHED = "CONTENT_PUBLISHED"

class ContentModuleType(str, Enum):
    STANDARD_COMPANY_LOGO = "STANDARD_COMPANY_LOGO"
    STANDARD_COMPARISON_TABLE = "STANDARD_COMPARISON_TABLE"
    STANDARD_FOUR_IMAGE_TEXT = "STANDARD_FOUR_IMAGE_TEXT"
    STANDARD_FOUR_IMAGE_TEXT_QUADRANT = "STANDARD_FOUR_IMAGE_TEXT_QUADRANT"
    STANDARD_HEADER_IMAGE_TEXT = "STANDARD_HEADER_IMAGE_TEXT"
    STANDARD_IMAGE_SIDEBAR = "STANDARD_IMAGE_SIDEBAR"
    STANDARD_IMAGE_TEXT_OVERLAY = "STANDARD_IMAGE_TEXT_OVERLAY"
    STANDARD_MULTIPLE_IMAGE_TEXT = "STANDARD_MULTIPLE_IMAGE_TEXT"
    STANDARD_PRODUCT_DESCRIPTION = "STANDARD_PRODUCT_DESCRIPTION"
    STANDARD_SINGLE_IMAGE_HIGHLIGHTS = "STANDARD_SINGLE_IMAGE_HIGHLIGHTS"
    STANDARD_SINGLE_IMAGE_SPECS_DETAIL = "STANDARD_SINGLE_IMAGE_SPECS_DETAIL"
    STANDARD_SINGLE_SIDE_IMAGE = "STANDARD_SINGLE_SIDE_IMAGE"
    STANDARD_TECH_SPECS = "STANDARD_TECH_SPECS"
    STANDARD_TEXT = "STANDARD_TEXT"
    STANDARD_THREE_IMAGE_TEXT = "STANDARD_THREE_IMAGE_TEXT"

class ColorType(str, Enum):
    DARK = "DARK"
    LIGHT = "LIGHT"

class PositionType(str, Enum):
    LEFT = "LEFT"
    RIGHT = "RIGHT"

class DecoratorType(str, Enum):
    LIST_ITEM = "LIST_ITEM"
    LIST_ORDERED = "LIST_ORDERED"
    LIST_UNORDERED = "LIST_UNORDERED"
    STYLE_BOLD = "STYLE_BOLD"
    STYLE_ITALIC = "STYLE_ITALIC"
    STYLE_LINEBREAK = "STYLE_LINEBREAK"
    STYLE_PARAGRAPH = "STYLE_PARAGRAPH"
    STYLE_UNDERLINE = "STYLE_UNDERLINE"

# Type Aliases
MarketplaceId = constr(min_length=1)
LanguageTag = constr(min_length=5, regex=r'^[a-z]{2,}-[A-Z0-9]{2,}$')
Asin = constr(min_length=10)
ContentReferenceKey = constr(min_length=1)
PageToken = constr(min_length=1)

MessageSet = List['Error']
ContentBadgeSet = List[ContentBadge]
AsinBadgeSet = List[AsinBadge]
AsinSet = conlist(Asin, unique_items=True)
ContentReferenceKeySet = List[ContentReferenceKey]

# Models
class Error(BaseModel):
    code: constr(min_length=1)
    message: constr(min_length=1)
    details: Optional[constr(min_length=1)] = None

class ErrorList(BaseModel):
    errors: List[Error]

class AplusResponse(BaseModel):
    warnings: Optional[MessageSet] = None

class AplusPaginatedResponse(AplusResponse):
    nextPageToken: Optional[PageToken] = None

class ContentMetadata(BaseModel):
    name: constr(min_length=1, max_length=100)
    marketplaceId: MarketplaceId
    status: ContentStatus
    badgeSet: ContentBadgeSet
    updateTime: str  # ISO datetime

class ContentMetadataRecord(BaseModel):
    contentReferenceKey: ContentReferenceKey
    contentMetadata: ContentMetadata

ContentMetadataRecordList = List[ContentMetadataRecord]

class ContentRecord(BaseModel):
    contentReferenceKey: ContentReferenceKey
    contentMetadata: Optional[ContentMetadata] = None
    contentDocument: Optional['ContentDocument'] = None

class ContentDocument(BaseModel):
    name: constr(min_length=1, max_length=100)
    contentType: ContentType
    contentSubType: Optional[constr(min_length=1)] = None
    locale: LanguageTag
    contentModuleList: List['ContentModule'] = Field(..., min_items=1, max_items=100)

PublishRecordList = List['PublishRecord']

class PublishRecord(BaseModel):
    marketplaceId: MarketplaceId
    locale: LanguageTag
    asin: Asin
    contentType: ContentType
    contentSubType: Optional[constr(min_length=1)] = None
    contentReferenceKey: ContentReferenceKey

class ImageDimensions(BaseModel):
    width: 'IntegerWithUnits'
    height: 'IntegerWithUnits'

class ImageOffsets(BaseModel):
    x: 'IntegerWithUnits'
    y: 'IntegerWithUnits'

class ImageCropSpecification(BaseModel):
    size: ImageDimensions
    offset: Optional[ImageOffsets] = None

class IntegerWithUnits(BaseModel):
    value: conint()
    units: str

class ImageComponent(BaseModel):
    uploadDestinationId: constr(min_length=1)
    imageCropSpecification: ImageCropSpecification
    altText: constr(min_length=1, max_length=100)

class TextComponent(BaseModel):
    value: constr(min_length=1, max_length=10000)
    decoratorSet: Optional[List['Decorator']] = None

class ParagraphComponent(BaseModel):
    textList: List[TextComponent] = Field(..., min_items=1, max_items=100)

class Decorator(BaseModel):
    type: DecoratorType
    offset: Optional[conint(ge=0)] = None
    length: Optional[conint(ge=0)] = None
    depth: Optional[conint(ge=0)] = None

DecoratorSet = List[Decorator]

# Content Modules
class StandardCompanyLogoModule(BaseModel):
    companyLogo: ImageComponent

class PlainTextItem(BaseModel):
    position: conint(ge=1, le=100)
    value: constr(min_length=1, max_length=250)

class StandardComparisonProductBlock(BaseModel):
    position: conint(ge=1, le=6)
    image: Optional[ImageComponent] = None
    title: Optional[constr(min_length=1, max_length=80)] = None
    asin: Optional[Asin] = None
    highlight: Optional[bool] = None
    metrics: Optional[List[PlainTextItem]] = None

class StandardComparisonTableModule(BaseModel):
    productColumns: Optional[List[StandardComparisonProductBlock]] = Field(None, max_items=6)
    metricRowLabels: Optional[List[PlainTextItem]] = Field(None, max_items=10)

class StandardImageTextBlock(BaseModel):
    image: Optional[ImageComponent] = None
    headline: Optional[TextComponent] = None
    body: Optional[ParagraphComponent] = None

class StandardFourImageTextModule(BaseModel):
    headline: Optional[TextComponent] = None
    block1: Optional[StandardImageTextBlock] = None
    block2: Optional[StandardImageTextBlock] = None
    block3: Optional[StandardImageTextBlock] = None
    block4: Optional[StandardImageTextBlock] = None

class StandardFourImageTextQuadrantModule(BaseModel):
    block1: StandardImageTextBlock
    block2: StandardImageTextBlock
    block3: StandardImageTextBlock
    block4: StandardImageTextBlock

class StandardHeaderImageTextModule(BaseModel):
    headline: Optional[TextComponent] = None
    block: Optional[StandardImageTextBlock] = None

class StandardTextBlock(BaseModel):
    headline: Optional[TextComponent] = None
    body: Optional[ParagraphComponent] = None

class StandardTextListBlock(BaseModel):
    textList: List[PlainTextItem] = Field(..., max_items=8)

class StandardHeaderTextListBlock(BaseModel):
    headline: Optional[TextComponent] = None
    block: Optional[StandardTextListBlock] = None

class StandardImageCaptionBlock(BaseModel):
    image: Optional[ImageComponent] = None
    caption: Optional[TextComponent] = None

class StandardImageSidebarModule(BaseModel):
    headline: Optional[TextComponent] = None
    imageCaptionBlock: Optional[StandardImageCaptionBlock] = None
    descriptionTextBlock: Optional[StandardTextBlock] = None
    descriptionListBlock: Optional[StandardTextListBlock] = None
    sidebarImageTextBlock: Optional[StandardImageTextBlock] = None
    sidebarListBlock: Optional[StandardTextListBlock] = None

class StandardImageTextOverlayModule(BaseModel):
    overlayColorType: ColorType
    block: Optional[StandardImageTextBlock] = None

class StandardImageTextCaptionBlock(BaseModel):
    block: Optional[StandardImageTextBlock] = None
    caption: Optional[TextComponent] = None

class StandardMultipleImageTextModule(BaseModel):
    blocks: Optional[List[StandardImageTextCaptionBlock]] = None

class StandardProductDescriptionModule(BaseModel):
    body: ParagraphComponent

class StandardSingleImageHighlightsModule(BaseModel):
    image: Optional[ImageComponent] = None
    headline: Optional[TextComponent] = None
    textBlock1: Optional[StandardTextBlock] = None
    textBlock2: Optional[StandardTextBlock] = None
    textBlock3: Optional[StandardTextBlock] = None
    bulletedListBlock: Optional[StandardHeaderTextListBlock] = None

class StandardSingleImageSpecsDetailModule(BaseModel):
    headline: Optional[TextComponent] = None
    image: Optional[ImageComponent] = None
    descriptionHeadline: Optional[TextComponent] = None
    descriptionBlock1: Optional[StandardTextBlock] = None
    descriptionBlock2: Optional[StandardTextBlock] = None
    specificationHeadline: Optional[TextComponent] = None
    specificationListBlock: Optional[StandardHeaderTextListBlock] = None
    specificationTextBlock: Optional[StandardTextBlock] = None

class StandardSingleSideImageModule(BaseModel):
    imagePositionType: PositionType
    block: Optional[StandardImageTextBlock] = None

class StandardTextPairBlock(BaseModel):
    label: Optional[TextComponent] = None
    description: Optional[TextComponent] = None

class StandardTechSpecsModule(BaseModel):
    headline: Optional[TextComponent] = None
    specificationList: List[StandardTextPairBlock] = Field(..., min_items=4, max_items=16)
    tableCount: Optional[conint(ge=1, le=2)] = None

class StandardTextModule(BaseModel):
    headline: Optional[TextComponent] = None
    body: ParagraphComponent

class StandardThreeImageTextModule(BaseModel):
    headline: Optional[TextComponent] = None
    block1: Optional[StandardImageTextBlock] = None
    block2: Optional[StandardImageTextBlock] = None
    block3: Optional[StandardImageTextBlock] = None

class ContentModule(BaseModel):
    contentModuleType: ContentModuleType
    standardCompanyLogo: Optional[StandardCompanyLogoModule] = None
    standardComparisonTable: Optional[StandardComparisonTableModule] = None
    standardFourImageText: Optional[StandardFourImageTextModule] = None
    standardFourImageTextQuadrant: Optional[StandardFourImageTextQuadrantModule] = None
    standardHeaderImageText: Optional[StandardHeaderImageTextModule] = None
    standardImageSidebar: Optional[StandardImageSidebarModule] = None
    standardImageTextOverlay: Optional[StandardImageTextOverlayModule] = None
    standardMultipleImageText: Optional[StandardMultipleImageTextModule] = None
    standardProductDescription: Optional[StandardProductDescriptionModule] = None
    standardSingleImageHighlights: Optional[StandardSingleImageHighlightsModule] = None
    standardSingleImageSpecsDetail: Optional[StandardSingleImageSpecsDetailModule] = None
    standardSingleSideImage: Optional[StandardSingleSideImageModule] = None
    standardTechSpecs: Optional[StandardTechSpecsModule] = None
    standardText: Optional[StandardTextModule] = None
    standardThreeImageText: Optional[StandardThreeImageTextModule] = None

ContentModuleList = List[ContentModule]

# Response Models
class SearchContentDocumentsResponse(AplusPaginatedResponse):
    contentMetadataRecords: ContentMetadataRecordList

class GetContentDocumentResponse(AplusResponse):
    contentRecord: ContentRecord

# Request Models
class PostContentDocumentRequest(RequestBaseModel):
    contentDocument: ContentDocument

class PostContentDocumentResponse(AplusResponse):
    contentReferenceKey: ContentReferenceKey

class ListContentDocumentAsinRelationsResponse(AplusPaginatedResponse):
    asinMetadataSet: List['AsinMetadata']

class AsinMetadata(BaseModel):
    asin: Asin
    badgeSet: Optional[AsinBadgeSet] = None
    parent: Optional[Asin] = None
    title: Optional[constr(min_length=1)] = None
    imageUrl: Optional[constr(min_length=1)] = None
    contentReferenceKeySet: Optional[ContentReferenceKeySet] = None

AsinMetadataSet = List[AsinMetadata]

class PostContentDocumentAsinRelationsRequest(RequestBaseModel):
    asinSet: AsinSet

class PostContentDocumentAsinRelationsResponse(AplusResponse):
    pass

class ValidateContentDocumentAsinRelationsResponse(AplusResponse, ErrorList):
    pass

class SearchContentPublishRecordsResponse(AplusPaginatedResponse):
    publishRecordList: PublishRecordList

class PostContentDocumentApprovalSubmissionResponse(AplusResponse):
    pass

class PostContentDocumentSuspendSubmissionResponse(AplusResponse):
    pass

# Required to support forward references
ContentRecord.update_forward_refs()
ContentDocument.update_forward_refs()
TextComponent.update_forward_refs()
Decorator.update_forward_refs()
StandardCompanyLogoModule.update_forward_refs()
StandardComparisonTableModule.update_forward_refs()
StandardImageTextBlock.update_forward_refs()
StandardFourImageTextModule.update_forward_refs()
StandardFourImageTextQuadrantModule.update_forward_refs()
StandardHeaderImageTextModule.update_forward_refs()
StandardTextBlock.update_forward_refs()
StandardTextListBlock.update_forward_refs()
StandardHeaderTextListBlock.update_forward_refs()
StandardImageCaptionBlock.update_forward_refs()
StandardImageSidebarModule.update_forward_refs()
StandardImageTextOverlayModule.update_forward_refs()
StandardImageTextCaptionBlock.update_forward_refs()
StandardMultipleImageTextModule.update_forward_refs()
StandardProductDescriptionModule.update_forward_refs()
StandardSingleImageHighlightsModule.update_forward_refs()
StandardSingleImageSpecsDetailModule.update_forward_refs()
StandardSingleSideImageModule.update_forward_refs()
StandardTechSpecsModule.update_forward_refs()
StandardTextModule.update_forward_refs()
StandardThreeImageTextModule.update_forward_refs()
ContentModule.update_forward_refs()
ListContentDocumentAsinRelationsResponse.update_forward_refs()
