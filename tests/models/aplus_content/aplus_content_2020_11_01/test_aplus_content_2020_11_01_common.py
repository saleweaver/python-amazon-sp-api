# Auto-generated tests for sp_api.api.models.aplus_content.aplus_content_2020_11_01.common.py
from datetime import datetime

import pytest
from sp_api.api.models.aplus_content.aplus_content_2020_11_01.common import (
    AplusPaginatedResponse, AplusResponse, AsinMetadata, ContentDocument,
    ContentMetadata, ContentMetadataRecord, ContentModule, ContentRecord,
    CreateContentDocumentRequest, Decorator, Error, ErrorList,
    GetContentDocumentRequest, GetContentDocumentResponse,
    GetRequestSerializer, ImageComponent, ImageCropSpecification,
    ImageDimensions, ImageOffsets, IncludedDataSetEnum, IntegerWithUnits,
    ListContentDocumentAsinRelationsRequest,
    ListContentDocumentAsinRelationsResponse, ParagraphComponent,
    PlainTextItem, PostContentDocumentApprovalSubmissionRequest,
    PostContentDocumentApprovalSubmissionResponse,
    PostContentDocumentAsinRelationsRequest,
    PostContentDocumentAsinRelationsRequestBody,
    PostContentDocumentAsinRelationsResponse, PostContentDocumentRequestBody,
    PostContentDocumentResponse, PostContentDocumentSuspendSubmissionRequest,
    PostContentDocumentSuspendSubmissionResponse, PublishRecord,
    RequestsBaseModel, SearchContentDocumentsRequest,
    SearchContentDocumentsResponse, SearchContentPublishRecordsRequest,
    SearchContentPublishRecordsResponse, SpApiBaseModel,
    StandardCompanyLogoModule, StandardComparisonProductBlock,
    StandardComparisonTableModule, StandardFourImageTextModule,
    StandardFourImageTextQuadrantModule, StandardHeaderImageTextModule,
    StandardHeaderTextListBlock, StandardImageCaptionBlock,
    StandardImageSidebarModule, StandardImageTextBlock,
    StandardImageTextCaptionBlock, StandardImageTextOverlayModule,
    StandardMultipleImageTextModule, StandardProductDescriptionModule,
    StandardSingleImageHighlightsModule, StandardSingleImageSpecsDetailModule,
    StandardSingleSideImageModule, StandardTechSpecsModule, StandardTextBlock,
    StandardTextListBlock, StandardTextModule, StandardTextPairBlock,
    StandardThreeImageTextModule, TextComponent, TextItem,
    UpdateContentDocumentRequest, ValidateContentDocumentAsinRelationsRequest,
    ValidateContentDocumentAsinRelationsResponse)


def test_requestsbasemodel_instantiates():
    """Instantiate RequestsBaseModel with dummy data"""
    kwargs = {}
    obj = RequestsBaseModel(**kwargs)
    assert isinstance(obj, RequestsBaseModel)


def test_spapibasemodel_instantiates():
    """Instantiate SpApiBaseModel with dummy data"""
    kwargs = {}
    obj = SpApiBaseModel(**kwargs)
    assert isinstance(obj, SpApiBaseModel)


def test_getrequestserializer_instantiates():
    """Instantiate GetRequestSerializer with dummy data"""
    kwargs = {}
    obj = GetRequestSerializer(**kwargs)
    assert isinstance(obj, GetRequestSerializer)


def test_apluspaginatedresponse_instantiates():
    """Instantiate AplusPaginatedResponse with dummy data"""
    kwargs = {}
    obj = AplusPaginatedResponse(**kwargs)
    assert isinstance(obj, AplusPaginatedResponse)


def test_aplusresponse_instantiates():
    """Instantiate AplusResponse with dummy data"""
    kwargs = {
        "warnings": None,
    }
    obj = AplusResponse(**kwargs)
    assert isinstance(obj, AplusResponse)


def test_asinmetadata_instantiates():
    """Instantiate AsinMetadata with dummy data"""
    kwargs = {
        "asin": "",
        "badge_set": None,
        "parent": None,
        "title": None,
        "image_url": None,
        "content_reference_key_set": None,
    }
    obj = AsinMetadata(**kwargs)
    assert isinstance(obj, AsinMetadata)


def test_contentdocument_instantiates():
    """Instantiate ContentDocument with dummy data"""
    kwargs = {
        "name": "",
        "content_type": "",
        "content_sub_type": None,
        "locale": "",
        "content_module_list": [],
    }
    obj = ContentDocument(**kwargs)
    assert isinstance(obj, ContentDocument)


def test_contentmetadata_instantiates():
    """Instantiate ContentMetadata with dummy data"""
    kwargs = {
        "name": "",
        "marketplace_id": None,
        "status": "",
        "badge_set": [],
        "update_time": datetime(2000, 1, 1),
    }
    obj = ContentMetadata(**kwargs)
    assert isinstance(obj, ContentMetadata)


def test_contentmetadatarecord_instantiates():
    """Instantiate ContentMetadataRecord with dummy data"""
    kwargs = {
        "content_reference_key": "",
        "content_metadata": ContentMetadata(
            **{
                "name": "",
                "marketplace_id": None,
                "status": "",
                "badge_set": [],
                "update_time": datetime(2000, 1, 1),
            }
        ),
    }
    obj = ContentMetadataRecord(**kwargs)
    assert isinstance(obj, ContentMetadataRecord)


def test_integerwithunits_instantiates():
    """Instantiate IntegerWithUnits with dummy data"""
    kwargs = {
        "value": 0,
        "units": "",
    }
    obj = IntegerWithUnits(**kwargs)
    assert isinstance(obj, IntegerWithUnits)


def test_imagedimensions_instantiates():
    """Instantiate ImageDimensions with dummy data"""
    kwargs = {
        "width": IntegerWithUnits(**{"value": 0, "units": ""}),
        "height": IntegerWithUnits(**{"value": 0, "units": ""}),
    }
    obj = ImageDimensions(**kwargs)
    assert isinstance(obj, ImageDimensions)


def test_imageoffsets_instantiates():
    """Instantiate ImageOffsets with dummy data"""
    kwargs = {
        "x": IntegerWithUnits(**{"value": 0, "units": ""}),
        "y": IntegerWithUnits(**{"value": 0, "units": ""}),
    }
    obj = ImageOffsets(**kwargs)
    assert isinstance(obj, ImageOffsets)


def test_imagecropspecification_instantiates():
    """Instantiate ImageCropSpecification with dummy data"""
    kwargs = {
        "size": ImageDimensions(
            **{
                "width": IntegerWithUnits(**{"value": 0, "units": ""}),
                "height": IntegerWithUnits(**{"value": 0, "units": ""}),
            }
        ),
        "offset": None,
    }
    obj = ImageCropSpecification(**kwargs)
    assert isinstance(obj, ImageCropSpecification)


def test_imagecomponent_instantiates():
    """Instantiate ImageComponent with dummy data"""
    kwargs = {
        "upload_destination_id": "",
        "image_crop_specification": ImageCropSpecification(
            **{
                "size": ImageDimensions(
                    **{
                        "width": IntegerWithUnits(**{"value": 0, "units": ""}),
                        "height": IntegerWithUnits(**{"value": 0, "units": ""}),
                    }
                ),
                "offset": None,
            }
        ),
        "alt_text": "",
    }
    obj = ImageComponent(**kwargs)
    assert isinstance(obj, ImageComponent)


def test_standardcompanylogomodule_instantiates():
    """Instantiate StandardCompanyLogoModule with dummy data"""
    kwargs = {
        "company_logo": ImageComponent(
            **{
                "upload_destination_id": "",
                "image_crop_specification": ImageCropSpecification(
                    **{
                        "size": ImageDimensions(
                            **{
                                "width": IntegerWithUnits(**{"value": 0, "units": ""}),
                                "height": IntegerWithUnits(**{"value": 0, "units": ""}),
                            }
                        ),
                        "offset": None,
                    }
                ),
                "alt_text": "",
            }
        ),
    }
    obj = StandardCompanyLogoModule(**kwargs)
    assert isinstance(obj, StandardCompanyLogoModule)


def test_plaintextitem_instantiates():
    """Instantiate PlainTextItem with dummy data"""
    kwargs = {
        "position": 0,
        "value": "",
    }
    obj = PlainTextItem(**kwargs)
    assert isinstance(obj, PlainTextItem)


def test_standardcomparisonproductblock_instantiates():
    """Instantiate StandardComparisonProductBlock with dummy data"""
    kwargs = {
        "position": 0,
        "image": None,
        "title": None,
        "asin": None,
        "highlight": None,
        "metrics": None,
    }
    obj = StandardComparisonProductBlock(**kwargs)
    assert isinstance(obj, StandardComparisonProductBlock)


def test_standardcomparisontablemodule_instantiates():
    """Instantiate StandardComparisonTableModule with dummy data"""
    kwargs = {
        "product_columns": None,
        "metric_row_labels": None,
    }
    obj = StandardComparisonTableModule(**kwargs)
    assert isinstance(obj, StandardComparisonTableModule)


def test_textcomponent_instantiates():
    """Instantiate TextComponent with dummy data"""
    kwargs = {
        "value": "",
        "decorator_set": None,
    }
    obj = TextComponent(**kwargs)
    assert isinstance(obj, TextComponent)


def test_paragraphcomponent_instantiates():
    """Instantiate ParagraphComponent with dummy data"""
    kwargs = {
        "text_list": [],
    }
    obj = ParagraphComponent(**kwargs)
    assert isinstance(obj, ParagraphComponent)


def test_standardimagetextblock_instantiates():
    """Instantiate StandardImageTextBlock with dummy data"""
    kwargs = {
        "image": None,
        "headline": None,
        "body": None,
    }
    obj = StandardImageTextBlock(**kwargs)
    assert isinstance(obj, StandardImageTextBlock)


def test_standardfourimagetextmodule_instantiates():
    """Instantiate StandardFourImageTextModule with dummy data"""
    kwargs = {
        "headline": None,
        "block1": None,
        "block2": None,
        "block3": None,
        "block4": None,
    }
    obj = StandardFourImageTextModule(**kwargs)
    assert isinstance(obj, StandardFourImageTextModule)


def test_standardfourimagetextquadrantmodule_instantiates():
    """Instantiate StandardFourImageTextQuadrantModule with dummy data"""
    kwargs = {
        "block1": StandardImageTextBlock(
            **{"image": None, "headline": None, "body": None}
        ),
        "block2": StandardImageTextBlock(
            **{"image": None, "headline": None, "body": None}
        ),
        "block3": StandardImageTextBlock(
            **{"image": None, "headline": None, "body": None}
        ),
        "block4": StandardImageTextBlock(
            **{"image": None, "headline": None, "body": None}
        ),
    }
    obj = StandardFourImageTextQuadrantModule(**kwargs)
    assert isinstance(obj, StandardFourImageTextQuadrantModule)


def test_standardheaderimagetextmodule_instantiates():
    """Instantiate StandardHeaderImageTextModule with dummy data"""
    kwargs = {
        "headline": None,
        "block": None,
    }
    obj = StandardHeaderImageTextModule(**kwargs)
    assert isinstance(obj, StandardHeaderImageTextModule)


def test_standardimagecaptionblock_instantiates():
    """Instantiate StandardImageCaptionBlock with dummy data"""
    kwargs = {
        "image": None,
        "caption": None,
    }
    obj = StandardImageCaptionBlock(**kwargs)
    assert isinstance(obj, StandardImageCaptionBlock)


def test_standardtextblock_instantiates():
    """Instantiate StandardTextBlock with dummy data"""
    kwargs = {
        "headline": None,
        "body": None,
    }
    obj = StandardTextBlock(**kwargs)
    assert isinstance(obj, StandardTextBlock)


def test_textitem_instantiates():
    """Instantiate TextItem with dummy data"""
    kwargs = {
        "position": 0,
        "text": TextComponent(**{"value": "", "decorator_set": None}),
    }
    obj = TextItem(**kwargs)
    assert isinstance(obj, TextItem)


def test_standardtextlistblock_instantiates():
    """Instantiate StandardTextListBlock with dummy data"""
    kwargs = {
        "text_list": [],
    }
    obj = StandardTextListBlock(**kwargs)
    assert isinstance(obj, StandardTextListBlock)


def test_standardimagesidebarmodule_instantiates():
    """Instantiate StandardImageSidebarModule with dummy data"""
    kwargs = {
        "headline": None,
        "image_caption_block": None,
        "description_text_block": None,
        "description_list_block": None,
        "sidebar_image_text_block": None,
        "sidebar_list_block": None,
    }
    obj = StandardImageSidebarModule(**kwargs)
    assert isinstance(obj, StandardImageSidebarModule)


def test_standardimagetextoverlaymodule_instantiates():
    """Instantiate StandardImageTextOverlayModule with dummy data"""
    kwargs = {
        "overlay_color_type": "",
        "block": None,
    }
    obj = StandardImageTextOverlayModule(**kwargs)
    assert isinstance(obj, StandardImageTextOverlayModule)


def test_standardimagetextcaptionblock_instantiates():
    """Instantiate StandardImageTextCaptionBlock with dummy data"""
    kwargs = {
        "block": None,
        "caption": None,
    }
    obj = StandardImageTextCaptionBlock(**kwargs)
    assert isinstance(obj, StandardImageTextCaptionBlock)


def test_standardmultipleimagetextmodule_instantiates():
    """Instantiate StandardMultipleImageTextModule with dummy data"""
    kwargs = {
        "blocks": None,
    }
    obj = StandardMultipleImageTextModule(**kwargs)
    assert isinstance(obj, StandardMultipleImageTextModule)


def test_standardproductdescriptionmodule_instantiates():
    """Instantiate StandardProductDescriptionModule with dummy data"""
    kwargs = {
        "body": ParagraphComponent(**{"text_list": []}),
    }
    obj = StandardProductDescriptionModule(**kwargs)
    assert isinstance(obj, StandardProductDescriptionModule)


def test_standardheadertextlistblock_instantiates():
    """Instantiate StandardHeaderTextListBlock with dummy data"""
    kwargs = {
        "headline": None,
        "block": None,
    }
    obj = StandardHeaderTextListBlock(**kwargs)
    assert isinstance(obj, StandardHeaderTextListBlock)


def test_standardsingleimagehighlightsmodule_instantiates():
    """Instantiate StandardSingleImageHighlightsModule with dummy data"""
    kwargs = {
        "image": None,
        "headline": None,
        "text_block1": None,
        "text_block2": None,
        "text_block3": None,
        "bulleted_list_block": None,
    }
    obj = StandardSingleImageHighlightsModule(**kwargs)
    assert isinstance(obj, StandardSingleImageHighlightsModule)


def test_standardsingleimagespecsdetailmodule_instantiates():
    """Instantiate StandardSingleImageSpecsDetailModule with dummy data"""
    kwargs = {
        "headline": None,
        "image": None,
        "description_headline": None,
        "description_block1": None,
        "description_block2": None,
        "specification_headline": None,
        "specification_list_block": None,
        "specification_text_block": None,
    }
    obj = StandardSingleImageSpecsDetailModule(**kwargs)
    assert isinstance(obj, StandardSingleImageSpecsDetailModule)


def test_standardsinglesideimagemodule_instantiates():
    """Instantiate StandardSingleSideImageModule with dummy data"""
    kwargs = {
        "image_position_type": "",
        "block": None,
    }
    obj = StandardSingleSideImageModule(**kwargs)
    assert isinstance(obj, StandardSingleSideImageModule)


def test_standardtextpairblock_instantiates():
    """Instantiate StandardTextPairBlock with dummy data"""
    kwargs = {
        "label": None,
        "description": None,
    }
    obj = StandardTextPairBlock(**kwargs)
    assert isinstance(obj, StandardTextPairBlock)


def test_standardtechspecsmodule_instantiates():
    """Instantiate StandardTechSpecsModule with dummy data"""
    kwargs = {
        "headline": None,
        "specification_list": [],
        "table_count": None,
    }
    obj = StandardTechSpecsModule(**kwargs)
    assert isinstance(obj, StandardTechSpecsModule)


def test_standardtextmodule_instantiates():
    """Instantiate StandardTextModule with dummy data"""
    kwargs = {
        "headline": None,
        "body": ParagraphComponent(**{"text_list": []}),
    }
    obj = StandardTextModule(**kwargs)
    assert isinstance(obj, StandardTextModule)


def test_standardthreeimagetextmodule_instantiates():
    """Instantiate StandardThreeImageTextModule with dummy data"""
    kwargs = {
        "headline": None,
        "block1": None,
        "block2": None,
        "block3": None,
    }
    obj = StandardThreeImageTextModule(**kwargs)
    assert isinstance(obj, StandardThreeImageTextModule)


def test_contentmodule_instantiates():
    """Instantiate ContentModule with dummy data"""
    kwargs = {
        "content_module_type": "",
        "standard_company_logo": None,
        "standard_comparison_table": None,
        "standard_four_image_text": None,
        "standard_four_image_text_quadrant": None,
        "standard_header_image_text": None,
        "standard_image_sidebar": None,
        "standard_image_text_overlay": None,
        "standard_multiple_image_text": None,
        "standard_product_description": None,
        "standard_single_image_highlights": None,
        "standard_single_image_specs_detail": None,
        "standard_single_side_image": None,
        "standard_tech_specs": None,
        "standard_text": None,
        "standard_three_image_text": None,
    }
    obj = ContentModule(**kwargs)
    assert isinstance(obj, ContentModule)


def test_contentrecord_instantiates():
    """Instantiate ContentRecord with dummy data"""
    kwargs = {
        "content_reference_key": "",
        "content_metadata": None,
        "content_document": None,
    }
    obj = ContentRecord(**kwargs)
    assert isinstance(obj, ContentRecord)


def test_postcontentdocumentrequestbody_instantiates():
    """Instantiate PostContentDocumentRequestBody with dummy data"""
    kwargs = {
        "content_document": ContentDocument(
            **{
                "name": "",
                "content_type": "",
                "content_sub_type": None,
                "locale": "",
                "content_module_list": [],
            }
        ),
    }
    obj = PostContentDocumentRequestBody(**kwargs)
    assert isinstance(obj, PostContentDocumentRequestBody)


def test_createcontentdocumentrequest_instantiates():
    """Instantiate CreateContentDocumentRequest with dummy data"""
    kwargs = {
        "marketplace_id": None,
        "post_content_document_request_body": PostContentDocumentRequestBody(
            **{
                "content_document": ContentDocument(
                    **{
                        "name": "",
                        "content_type": "",
                        "content_sub_type": None,
                        "locale": "",
                        "content_module_list": [],
                    }
                )
            }
        ),
    }
    obj = CreateContentDocumentRequest(**kwargs)
    assert isinstance(obj, CreateContentDocumentRequest)


def test_decorator_instantiates():
    """Instantiate Decorator with dummy data"""
    kwargs = {
        "type": None,
        "offset": None,
        "length": None,
        "depth": None,
    }
    obj = Decorator(**kwargs)
    assert isinstance(obj, Decorator)


def test_error_instantiates():
    """Instantiate Error with dummy data"""
    kwargs = {
        "code": "",
        "message": "",
        "details": None,
    }
    obj = Error(**kwargs)
    assert isinstance(obj, Error)


def test_errorlist_instantiates():
    """Instantiate ErrorList with dummy data"""
    kwargs = {
        "errors": [],
    }
    obj = ErrorList(**kwargs)
    assert isinstance(obj, ErrorList)


def test_getcontentdocumentrequest_instantiates():
    """Instantiate GetContentDocumentRequest with dummy data"""
    kwargs = {
        "content_reference_key": "",
        "marketplace_id": None,
        "included_data_set": [],
    }
    obj = GetContentDocumentRequest(**kwargs)
    assert isinstance(obj, GetContentDocumentRequest)


def test_getcontentdocumentresponse_instantiates():
    """Instantiate GetContentDocumentResponse with dummy data"""
    kwargs = {}
    obj = GetContentDocumentResponse(**kwargs)
    assert isinstance(obj, GetContentDocumentResponse)


def test_listcontentdocumentasinrelationsrequest_instantiates():
    """Instantiate ListContentDocumentAsinRelationsRequest with dummy data"""
    kwargs = {
        "content_reference_key": "",
        "marketplace_id": None,
        "included_data_set": None,
        "asin_set": None,
        "page_token": None,
    }
    obj = ListContentDocumentAsinRelationsRequest(**kwargs)
    assert isinstance(obj, ListContentDocumentAsinRelationsRequest)


def test_listcontentdocumentasinrelationsresponse_instantiates():
    """Instantiate ListContentDocumentAsinRelationsResponse with dummy data"""
    kwargs = {}
    obj = ListContentDocumentAsinRelationsResponse(**kwargs)
    assert isinstance(obj, ListContentDocumentAsinRelationsResponse)


def test_postcontentdocumentapprovalsubmissionrequest_instantiates():
    """Instantiate PostContentDocumentApprovalSubmissionRequest with dummy data"""
    kwargs = {
        "content_reference_key": "",
        "marketplace_id": None,
    }
    obj = PostContentDocumentApprovalSubmissionRequest(**kwargs)
    assert isinstance(obj, PostContentDocumentApprovalSubmissionRequest)


def test_postcontentdocumentapprovalsubmissionresponse_instantiates():
    """Instantiate PostContentDocumentApprovalSubmissionResponse with dummy data"""
    kwargs = {}
    obj = PostContentDocumentApprovalSubmissionResponse(**kwargs)
    assert isinstance(obj, PostContentDocumentApprovalSubmissionResponse)


def test_postcontentdocumentasinrelationsrequestbody_instantiates():
    """Instantiate PostContentDocumentAsinRelationsRequestBody with dummy data"""
    kwargs = {
        "asin_set": [],
    }
    obj = PostContentDocumentAsinRelationsRequestBody(**kwargs)
    assert isinstance(obj, PostContentDocumentAsinRelationsRequestBody)


def test_postcontentdocumentasinrelationsrequest_instantiates():
    """Instantiate PostContentDocumentAsinRelationsRequest with dummy data"""
    kwargs = {
        "content_reference_key": "",
        "marketplace_id": None,
        "post_content_document_asin_relations_request_body": PostContentDocumentAsinRelationsRequestBody(
            **{"asin_set": []}
        ),
    }
    obj = PostContentDocumentAsinRelationsRequest(**kwargs)
    assert isinstance(obj, PostContentDocumentAsinRelationsRequest)


def test_postcontentdocumentasinrelationsresponse_instantiates():
    """Instantiate PostContentDocumentAsinRelationsResponse with dummy data"""
    kwargs = {}
    obj = PostContentDocumentAsinRelationsResponse(**kwargs)
    assert isinstance(obj, PostContentDocumentAsinRelationsResponse)


def test_postcontentdocumentresponse_instantiates():
    """Instantiate PostContentDocumentResponse with dummy data"""
    kwargs = {}
    obj = PostContentDocumentResponse(**kwargs)
    assert isinstance(obj, PostContentDocumentResponse)


def test_postcontentdocumentsuspendsubmissionrequest_instantiates():
    """Instantiate PostContentDocumentSuspendSubmissionRequest with dummy data"""
    kwargs = {
        "content_reference_key": "",
        "marketplace_id": None,
    }
    obj = PostContentDocumentSuspendSubmissionRequest(**kwargs)
    assert isinstance(obj, PostContentDocumentSuspendSubmissionRequest)


def test_postcontentdocumentsuspendsubmissionresponse_instantiates():
    """Instantiate PostContentDocumentSuspendSubmissionResponse with dummy data"""
    kwargs = {}
    obj = PostContentDocumentSuspendSubmissionResponse(**kwargs)
    assert isinstance(obj, PostContentDocumentSuspendSubmissionResponse)


def test_publishrecord_instantiates():
    """Instantiate PublishRecord with dummy data"""
    kwargs = {
        "marketplace_id": None,
        "locale": "",
        "asin": "",
        "content_type": "",
        "content_sub_type": None,
        "content_reference_key": "",
    }
    obj = PublishRecord(**kwargs)
    assert isinstance(obj, PublishRecord)


def test_searchcontentdocumentsrequest_instantiates():
    """Instantiate SearchContentDocumentsRequest with dummy data"""
    kwargs = {
        "marketplace_id": None,
        "page_token": None,
    }
    obj = SearchContentDocumentsRequest(**kwargs)
    assert isinstance(obj, SearchContentDocumentsRequest)


def test_searchcontentdocumentsresponse_instantiates():
    """Instantiate SearchContentDocumentsResponse with dummy data"""
    kwargs = {}
    obj = SearchContentDocumentsResponse(**kwargs)
    assert isinstance(obj, SearchContentDocumentsResponse)


def test_searchcontentpublishrecordsrequest_instantiates():
    """Instantiate SearchContentPublishRecordsRequest with dummy data"""
    kwargs = {
        "marketplace_id": None,
        "asin": "",
        "page_token": None,
    }
    obj = SearchContentPublishRecordsRequest(**kwargs)
    assert isinstance(obj, SearchContentPublishRecordsRequest)


def test_searchcontentpublishrecordsresponse_instantiates():
    """Instantiate SearchContentPublishRecordsResponse with dummy data"""
    kwargs = {}
    obj = SearchContentPublishRecordsResponse(**kwargs)
    assert isinstance(obj, SearchContentPublishRecordsResponse)


def test_updatecontentdocumentrequest_instantiates():
    """Instantiate UpdateContentDocumentRequest with dummy data"""
    kwargs = {
        "content_reference_key": "",
        "marketplace_id": None,
        "post_content_document_request_body": PostContentDocumentRequestBody(
            **{
                "content_document": ContentDocument(
                    **{
                        "name": "",
                        "content_type": "",
                        "content_sub_type": None,
                        "locale": "",
                        "content_module_list": [],
                    }
                )
            }
        ),
    }
    obj = UpdateContentDocumentRequest(**kwargs)
    assert isinstance(obj, UpdateContentDocumentRequest)


def test_validatecontentdocumentasinrelationsrequest_instantiates():
    """Instantiate ValidateContentDocumentAsinRelationsRequest with dummy data"""
    kwargs = {
        "marketplace_id": None,
        "asin_set": None,
        "post_content_document_request_body": PostContentDocumentRequestBody(
            **{
                "content_document": ContentDocument(
                    **{
                        "name": "",
                        "content_type": "",
                        "content_sub_type": None,
                        "locale": "",
                        "content_module_list": [],
                    }
                )
            }
        ),
    }
    obj = ValidateContentDocumentAsinRelationsRequest(**kwargs)
    assert isinstance(obj, ValidateContentDocumentAsinRelationsRequest)


def test_validatecontentdocumentasinrelationsresponse_instantiates():
    """Instantiate ValidateContentDocumentAsinRelationsResponse with dummy data"""
    kwargs = {}
    obj = ValidateContentDocumentAsinRelationsResponse(**kwargs)
    assert isinstance(obj, ValidateContentDocumentAsinRelationsResponse)
