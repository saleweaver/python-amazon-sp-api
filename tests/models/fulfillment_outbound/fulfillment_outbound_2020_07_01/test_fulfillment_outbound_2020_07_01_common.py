# Auto-generated tests for sp_api.api.models.fulfillment_outbound.fulfillment_outbound_2020_07_01.common.py
from datetime import datetime

import pytest
from sp_api.api.models.fulfillment_outbound.fulfillment_outbound_2020_07_01.common import (
    Address, Amount, AmountUnitOfMeasureEnum, CancelFulfillmentOrderRequest,
    CancelFulfillmentOrderResponse, CODSettings, CreateFulfillmentOrderItem,
    CreateFulfillmentOrderRequest, CreateFulfillmentOrderRequestBody,
    CreateFulfillmentOrderResponse, CreateFulfillmentReturnRequest,
    CreateFulfillmentReturnRequestBody, CreateFulfillmentReturnResponse,
    CreateFulfillmentReturnResult, CreateReturnItem, DateRange,
    DeliveryDocument, DeliveryInformation, DeliveryMessage, DeliveryOffer,
    DeliveryOffersRequest, DeliveryPolicy, DeliveryPreferences, DeliveryWindow,
    Destination, DropOffLocation, DropOffLocationTypeEnum, Error, Feature,
    FeatureSettings, FeatureSettingsFeatureFulfillmentPolicyEnum, FeatureSku,
    Fee, FeeNameEnum, FulfillmentOrder, FulfillmentOrderItem,
    FulfillmentPreview, FulfillmentPreviewItem,
    FulfillmentPreviewItemShippingWeightCalculationMethodEnum,
    FulfillmentPreviewShipment, FulfillmentShipment,
    FulfillmentShipmentFulfillmentShipmentStatusEnum, FulfillmentShipmentItem,
    FulfillmentShipmentPackage, GetDeliveryOffersProduct,
    GetDeliveryOffersRequestBody, GetDeliveryOffersResponse,
    GetDeliveryOffersResult, GetDeliveryOffersTerms,
    GetFeatureInventoryRequest, GetFeatureInventoryResponse,
    GetFeatureInventoryResult, GetFeatureSKURequest, GetFeatureSkuResponse,
    GetFeatureSkuResult, GetFeaturesRequest, GetFeaturesResponse,
    GetFeaturesResult, GetFulfillmentOrderRequest, GetFulfillmentOrderResponse,
    GetFulfillmentOrderResult, GetFulfillmentPreviewItem,
    GetFulfillmentPreviewRequest, GetFulfillmentPreviewRequestBody,
    GetFulfillmentPreviewResponse, GetFulfillmentPreviewResult,
    GetPackageTrackingDetailsRequest, GetPackageTrackingDetailsResponse,
    GetRequestSerializer, InvalidItemReason, InvalidReturnItem,
    ListAllFulfillmentOrdersRequest, ListAllFulfillmentOrdersResponse,
    ListAllFulfillmentOrdersResult, ListReturnReasonCodesRequest,
    ListReturnReasonCodesResponse, ListReturnReasonCodesResult, LockerDetails,
    Money, NotificationEmailList, Origin, PackageTrackingDetails,
    PaymentInformation, ProductIdentifier, ReasonCodeDetails,
    RequestsBaseModel, ReturnAuthorization, ReturnItem, ScheduledDeliveryInfo,
    SpApiBaseModel, StringList, SubmitFulfillmentOrderStatusUpdateRequest,
    SubmitFulfillmentOrderStatusUpdateRequestBody,
    SubmitFulfillmentOrderStatusUpdateResponse, TrackingAddress, TrackingEvent,
    UnfulfillablePreviewItem, UpdateFulfillmentOrderItem,
    UpdateFulfillmentOrderRequest, UpdateFulfillmentOrderRequestBody,
    UpdateFulfillmentOrderResponse, VariablePrecisionAddress, Weight,
    WeightUnitEnum)


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


def test_address_instantiates():
    """Instantiate Address with dummy data"""
    kwargs = {
        "name": "",
        "address_line1": "",
        "address_line2": None,
        "address_line3": None,
        "city": None,
        "district_or_county": None,
        "state_or_region": "",
        "postal_code": "",
        "country_code": "",
        "phone": None,
    }
    obj = Address(**kwargs)
    assert isinstance(obj, Address)


def test_amount_instantiates():
    """Instantiate Amount with dummy data"""
    kwargs = {
        "unit_of_measure": AmountUnitOfMeasureEnum.EACHES,
        "value": "",
    }
    obj = Amount(**kwargs)
    assert isinstance(obj, Amount)


def test_money_instantiates():
    """Instantiate Money with dummy data"""
    kwargs = {
        "currency_code": "",
        "value": "",
    }
    obj = Money(**kwargs)
    assert isinstance(obj, Money)


def test_codsettings_instantiates():
    """Instantiate CODSettings with dummy data"""
    kwargs = {
        "is_cod_required": False,
        "cod_charge": None,
        "cod_charge_tax": None,
        "shipping_charge": None,
        "shipping_charge_tax": None,
    }
    obj = CODSettings(**kwargs)
    assert isinstance(obj, CODSettings)


def test_cancelfulfillmentorderrequest_instantiates():
    """Instantiate CancelFulfillmentOrderRequest with dummy data"""
    kwargs = {
        "seller_fulfillment_order_id": "",
    }
    obj = CancelFulfillmentOrderRequest(**kwargs)
    assert isinstance(obj, CancelFulfillmentOrderRequest)


def test_cancelfulfillmentorderresponse_instantiates():
    """Instantiate CancelFulfillmentOrderResponse with dummy data"""
    kwargs = {
        "errors": None,
    }
    obj = CancelFulfillmentOrderResponse(**kwargs)
    assert isinstance(obj, CancelFulfillmentOrderResponse)


def test_createfulfillmentorderitem_instantiates():
    """Instantiate CreateFulfillmentOrderItem with dummy data"""
    kwargs = {
        "seller_sku": "",
        "seller_fulfillment_order_item_id": "",
        "quantity": 0,
        "gift_message": None,
        "displayable_comment": None,
        "fulfillment_network_sku": None,
        "per_unit_declared_value": None,
        "per_unit_price": None,
        "per_unit_tax": None,
    }
    obj = CreateFulfillmentOrderItem(**kwargs)
    assert isinstance(obj, CreateFulfillmentOrderItem)


def test_dropofflocation_instantiates():
    """Instantiate DropOffLocation with dummy data"""
    kwargs = {
        "type": DropOffLocationTypeEnum.FRONT_DOOR,
        "attributes": None,
    }
    obj = DropOffLocation(**kwargs)
    assert isinstance(obj, DropOffLocation)


def test_deliverypreferences_instantiates():
    """Instantiate DeliveryPreferences with dummy data"""
    kwargs = {
        "delivery_instructions": None,
        "drop_off_location": None,
    }
    obj = DeliveryPreferences(**kwargs)
    assert isinstance(obj, DeliveryPreferences)


def test_deliverywindow_instantiates():
    """Instantiate DeliveryWindow with dummy data"""
    kwargs = {
        "start_date": "",
        "end_date": "",
    }
    obj = DeliveryWindow(**kwargs)
    assert isinstance(obj, DeliveryWindow)


def test_featuresettings_instantiates():
    """Instantiate FeatureSettings with dummy data"""
    kwargs = {
        "feature_name": None,
        "feature_fulfillment_policy": None,
    }
    obj = FeatureSettings(**kwargs)
    assert isinstance(obj, FeatureSettings)


def test_notificationemaillist_instantiates():
    """Instantiate NotificationEmailList with dummy data"""
    kwargs = {}
    obj = NotificationEmailList(**kwargs)
    assert isinstance(obj, NotificationEmailList)


def test_createfulfillmentorderrequestbody_instantiates():
    """Instantiate CreateFulfillmentOrderRequestBody with dummy data"""
    kwargs = {
        "marketplace_id": None,
        "seller_fulfillment_order_id": "",
        "displayable_order_id": "",
        "displayable_order_date": "",
        "displayable_order_comment": "",
        "shipping_speed_category": "",
        "delivery_window": None,
        "destination_address": Address(
            **{
                "name": "",
                "address_line1": "",
                "address_line2": None,
                "address_line3": None,
                "city": None,
                "district_or_county": None,
                "state_or_region": "",
                "postal_code": "",
                "country_code": "",
                "phone": None,
            }
        ),
        "delivery_preferences": None,
        "fulfillment_action": None,
        "fulfillment_policy": None,
        "cod_settings": None,
        "ship_from_country_code": None,
        "notification_emails": None,
        "feature_constraints": None,
        "items": [],
        "payment_information": None,
    }
    obj = CreateFulfillmentOrderRequestBody(**kwargs)
    assert isinstance(obj, CreateFulfillmentOrderRequestBody)


def test_createfulfillmentorderrequest_instantiates():
    """Instantiate CreateFulfillmentOrderRequest with dummy data"""
    kwargs = {
        "body": CreateFulfillmentOrderRequestBody(
            **{
                "marketplace_id": None,
                "seller_fulfillment_order_id": "",
                "displayable_order_id": "",
                "displayable_order_date": "",
                "displayable_order_comment": "",
                "shipping_speed_category": "",
                "delivery_window": None,
                "destination_address": Address(
                    **{
                        "name": "",
                        "address_line1": "",
                        "address_line2": None,
                        "address_line3": None,
                        "city": None,
                        "district_or_county": None,
                        "state_or_region": "",
                        "postal_code": "",
                        "country_code": "",
                        "phone": None,
                    }
                ),
                "delivery_preferences": None,
                "fulfillment_action": None,
                "fulfillment_policy": None,
                "cod_settings": None,
                "ship_from_country_code": None,
                "notification_emails": None,
                "feature_constraints": None,
                "items": [],
                "payment_information": None,
            }
        ),
    }
    obj = CreateFulfillmentOrderRequest(**kwargs)
    assert isinstance(obj, CreateFulfillmentOrderRequest)


def test_createfulfillmentorderresponse_instantiates():
    """Instantiate CreateFulfillmentOrderResponse with dummy data"""
    kwargs = {
        "errors": None,
    }
    obj = CreateFulfillmentOrderResponse(**kwargs)
    assert isinstance(obj, CreateFulfillmentOrderResponse)


def test_createfulfillmentreturnrequestbody_instantiates():
    """Instantiate CreateFulfillmentReturnRequestBody with dummy data"""
    kwargs = {
        "items": [],
    }
    obj = CreateFulfillmentReturnRequestBody(**kwargs)
    assert isinstance(obj, CreateFulfillmentReturnRequestBody)


def test_createfulfillmentreturnrequest_instantiates():
    """Instantiate CreateFulfillmentReturnRequest with dummy data"""
    kwargs = {
        "body": CreateFulfillmentReturnRequestBody(**{"items": []}),
        "seller_fulfillment_order_id": "",
    }
    obj = CreateFulfillmentReturnRequest(**kwargs)
    assert isinstance(obj, CreateFulfillmentReturnRequest)


def test_createfulfillmentreturnresult_instantiates():
    """Instantiate CreateFulfillmentReturnResult with dummy data"""
    kwargs = {
        "return_items": None,
        "invalid_return_items": None,
        "return_authorizations": None,
    }
    obj = CreateFulfillmentReturnResult(**kwargs)
    assert isinstance(obj, CreateFulfillmentReturnResult)


def test_createfulfillmentreturnresponse_instantiates():
    """Instantiate CreateFulfillmentReturnResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = CreateFulfillmentReturnResponse(**kwargs)
    assert isinstance(obj, CreateFulfillmentReturnResponse)


def test_createreturnitem_instantiates():
    """Instantiate CreateReturnItem with dummy data"""
    kwargs = {
        "seller_return_item_id": "",
        "seller_fulfillment_order_item_id": "",
        "amazon_shipment_id": "",
        "return_reason_code": "",
        "return_comment": None,
    }
    obj = CreateReturnItem(**kwargs)
    assert isinstance(obj, CreateReturnItem)


def test_daterange_instantiates():
    """Instantiate DateRange with dummy data"""
    kwargs = {
        "earliest": "",
        "latest": "",
    }
    obj = DateRange(**kwargs)
    assert isinstance(obj, DateRange)


def test_deliverydocument_instantiates():
    """Instantiate DeliveryDocument with dummy data"""
    kwargs = {
        "document_type": "",
        "url": None,
    }
    obj = DeliveryDocument(**kwargs)
    assert isinstance(obj, DeliveryDocument)


def test_deliveryinformation_instantiates():
    """Instantiate DeliveryInformation with dummy data"""
    kwargs = {
        "delivery_document_list": None,
        "drop_off_location": None,
    }
    obj = DeliveryInformation(**kwargs)
    assert isinstance(obj, DeliveryInformation)


def test_deliverymessage_instantiates():
    """Instantiate DeliveryMessage with dummy data"""
    kwargs = {
        "text": None,
        "locale": None,
    }
    obj = DeliveryMessage(**kwargs)
    assert isinstance(obj, DeliveryMessage)


def test_deliverypolicy_instantiates():
    """Instantiate DeliveryPolicy with dummy data"""
    kwargs = {
        "message": None,
    }
    obj = DeliveryPolicy(**kwargs)
    assert isinstance(obj, DeliveryPolicy)


def test_deliveryoffer_instantiates():
    """Instantiate DeliveryOffer with dummy data"""
    kwargs = {
        "expires_at": None,
        "date_range": None,
        "policy": None,
    }
    obj = DeliveryOffer(**kwargs)
    assert isinstance(obj, DeliveryOffer)


def test_productidentifier_instantiates():
    """Instantiate ProductIdentifier with dummy data"""
    kwargs = {
        "merchant_sku": "",
    }
    obj = ProductIdentifier(**kwargs)
    assert isinstance(obj, ProductIdentifier)


def test_getdeliveryoffersproduct_instantiates():
    """Instantiate GetDeliveryOffersProduct with dummy data"""
    kwargs = {
        "product_identifier": ProductIdentifier(**{"merchant_sku": ""}),
        "amount": None,
    }
    obj = GetDeliveryOffersProduct(**kwargs)
    assert isinstance(obj, GetDeliveryOffersProduct)


def test_variableprecisionaddress_instantiates():
    """Instantiate VariablePrecisionAddress with dummy data"""
    kwargs = {
        "address_line1": None,
        "address_line2": None,
        "address_line3": None,
        "city": None,
        "district_or_county": None,
        "state_or_region": None,
        "postal_code": "",
        "country_code": "",
    }
    obj = VariablePrecisionAddress(**kwargs)
    assert isinstance(obj, VariablePrecisionAddress)


def test_destination_instantiates():
    """Instantiate Destination with dummy data"""
    kwargs = {
        "delivery_address": None,
        "ip_address": None,
    }
    obj = Destination(**kwargs)
    assert isinstance(obj, Destination)


def test_origin_instantiates():
    """Instantiate Origin with dummy data"""
    kwargs = {
        "country_code": "",
    }
    obj = Origin(**kwargs)
    assert isinstance(obj, Origin)


def test_getdeliveryoffersterms_instantiates():
    """Instantiate GetDeliveryOffersTerms with dummy data"""
    kwargs = {
        "origin": Origin(**{"country_code": ""}),
        "destination": Destination(**{"delivery_address": None, "ip_address": None}),
    }
    obj = GetDeliveryOffersTerms(**kwargs)
    assert isinstance(obj, GetDeliveryOffersTerms)


def test_getdeliveryoffersrequestbody_instantiates():
    """Instantiate GetDeliveryOffersRequestBody with dummy data"""
    kwargs = {
        "product": GetDeliveryOffersProduct(
            **{
                "product_identifier": ProductIdentifier(**{"merchant_sku": ""}),
                "amount": None,
            }
        ),
        "terms": GetDeliveryOffersTerms(
            **{
                "origin": Origin(**{"country_code": ""}),
                "destination": Destination(
                    **{"delivery_address": None, "ip_address": None}
                ),
            }
        ),
    }
    obj = GetDeliveryOffersRequestBody(**kwargs)
    assert isinstance(obj, GetDeliveryOffersRequestBody)


def test_deliveryoffersrequest_instantiates():
    """Instantiate DeliveryOffersRequest with dummy data"""
    kwargs = {
        "body": GetDeliveryOffersRequestBody(
            **{
                "product": GetDeliveryOffersProduct(
                    **{
                        "product_identifier": ProductIdentifier(**{"merchant_sku": ""}),
                        "amount": None,
                    }
                ),
                "terms": GetDeliveryOffersTerms(
                    **{
                        "origin": Origin(**{"country_code": ""}),
                        "destination": Destination(
                            **{"delivery_address": None, "ip_address": None}
                        ),
                    }
                ),
            }
        ),
    }
    obj = DeliveryOffersRequest(**kwargs)
    assert isinstance(obj, DeliveryOffersRequest)


def test_error_instantiates():
    """Instantiate Error with dummy data"""
    kwargs = {
        "code": "",
        "message": "",
        "details": None,
    }
    obj = Error(**kwargs)
    assert isinstance(obj, Error)


def test_feature_instantiates():
    """Instantiate Feature with dummy data"""
    kwargs = {
        "feature_name": "",
        "feature_description": "",
        "seller_eligible": None,
    }
    obj = Feature(**kwargs)
    assert isinstance(obj, Feature)


def test_featuresku_instantiates():
    """Instantiate FeatureSku with dummy data"""
    kwargs = {
        "seller_sku": None,
        "fn_sku": None,
        "asin": None,
        "sku_count": None,
        "overlapping_skus": None,
    }
    obj = FeatureSku(**kwargs)
    assert isinstance(obj, FeatureSku)


def test_fee_instantiates():
    """Instantiate Fee with dummy data"""
    kwargs = {
        "name": FeeNameEnum.FBA_PER_UNIT_FULFILLMENT_FEE,
        "amount": Money(**{"currency_code": "", "value": ""}),
    }
    obj = Fee(**kwargs)
    assert isinstance(obj, Fee)


def test_fulfillmentorder_instantiates():
    """Instantiate FulfillmentOrder with dummy data"""
    kwargs = {
        "seller_fulfillment_order_id": "",
        "marketplace_id": None,
        "displayable_order_id": "",
        "displayable_order_date": "",
        "displayable_order_comment": "",
        "shipping_speed_category": "",
        "delivery_window": None,
        "destination_address": Address(
            **{
                "name": "",
                "address_line1": "",
                "address_line2": None,
                "address_line3": None,
                "city": None,
                "district_or_county": None,
                "state_or_region": "",
                "postal_code": "",
                "country_code": "",
                "phone": None,
            }
        ),
        "fulfillment_action": None,
        "fulfillment_policy": None,
        "cod_settings": None,
        "received_date": "",
        "fulfillment_order_status": "",
        "status_updated_date": "",
        "notification_emails": None,
        "feature_constraints": None,
    }
    obj = FulfillmentOrder(**kwargs)
    assert isinstance(obj, FulfillmentOrder)


def test_fulfillmentorderitem_instantiates():
    """Instantiate FulfillmentOrderItem with dummy data"""
    kwargs = {
        "seller_sku": "",
        "seller_fulfillment_order_item_id": "",
        "quantity": 0,
        "gift_message": None,
        "displayable_comment": None,
        "fulfillment_network_sku": None,
        "order_item_disposition": None,
        "cancelled_quantity": 0,
        "unfulfillable_quantity": 0,
        "estimated_ship_date": None,
        "estimated_arrival_date": None,
        "per_unit_price": None,
        "per_unit_tax": None,
        "per_unit_declared_value": None,
    }
    obj = FulfillmentOrderItem(**kwargs)
    assert isinstance(obj, FulfillmentOrderItem)


def test_scheduleddeliveryinfo_instantiates():
    """Instantiate ScheduledDeliveryInfo with dummy data"""
    kwargs = {
        "delivery_time_zone": "",
        "delivery_windows": [],
    }
    obj = ScheduledDeliveryInfo(**kwargs)
    assert isinstance(obj, ScheduledDeliveryInfo)


def test_stringlist_instantiates():
    """Instantiate StringList with dummy data"""
    kwargs = {}
    obj = StringList(**kwargs)
    assert isinstance(obj, StringList)


def test_weight_instantiates():
    """Instantiate Weight with dummy data"""
    kwargs = {
        "unit": WeightUnitEnum.KG,
        "value": "",
    }
    obj = Weight(**kwargs)
    assert isinstance(obj, Weight)


def test_fulfillmentpreview_instantiates():
    """Instantiate FulfillmentPreview with dummy data"""
    kwargs = {
        "shipping_speed_category": "",
        "scheduled_delivery_info": None,
        "is_fulfillable": False,
        "is_c_o_d_capable": False,
        "estimated_shipping_weight": None,
        "estimated_fees": None,
        "fulfillment_preview_shipments": None,
        "unfulfillable_preview_items": None,
        "order_unfulfillable_reasons": None,
        "marketplace_id": None,
        "feature_constraints": None,
    }
    obj = FulfillmentPreview(**kwargs)
    assert isinstance(obj, FulfillmentPreview)


def test_fulfillmentpreviewitem_instantiates():
    """Instantiate FulfillmentPreviewItem with dummy data"""
    kwargs = {
        "seller_sku": "",
        "quantity": 0,
        "seller_fulfillment_order_item_id": "",
        "estimated_shipping_weight": None,
        "shipping_weight_calculation_method": None,
    }
    obj = FulfillmentPreviewItem(**kwargs)
    assert isinstance(obj, FulfillmentPreviewItem)


def test_fulfillmentpreviewshipment_instantiates():
    """Instantiate FulfillmentPreviewShipment with dummy data"""
    kwargs = {
        "earliest_ship_date": None,
        "latest_ship_date": None,
        "earliest_arrival_date": None,
        "latest_arrival_date": None,
        "shipping_notes": None,
        "fulfillment_preview_items": [],
    }
    obj = FulfillmentPreviewShipment(**kwargs)
    assert isinstance(obj, FulfillmentPreviewShipment)


def test_fulfillmentshipment_instantiates():
    """Instantiate FulfillmentShipment with dummy data"""
    kwargs = {
        "amazon_shipment_id": "",
        "fulfillment_center_id": "",
        "fulfillment_shipment_status": FulfillmentShipmentFulfillmentShipmentStatusEnum.PENDING,
        "shipping_date": None,
        "estimated_arrival_date": None,
        "shipping_notes": None,
        "fulfillment_shipment_item": [],
        "fulfillment_shipment_package": None,
    }
    obj = FulfillmentShipment(**kwargs)
    assert isinstance(obj, FulfillmentShipment)


def test_fulfillmentshipmentitem_instantiates():
    """Instantiate FulfillmentShipmentItem with dummy data"""
    kwargs = {
        "seller_sku": "",
        "seller_fulfillment_order_item_id": "",
        "quantity": 0,
        "package_number": None,
        "serial_number": None,
        "manufacturer_lot_codes": None,
    }
    obj = FulfillmentShipmentItem(**kwargs)
    assert isinstance(obj, FulfillmentShipmentItem)


def test_lockerdetails_instantiates():
    """Instantiate LockerDetails with dummy data"""
    kwargs = {
        "locker_number": None,
        "locker_access_code": None,
    }
    obj = LockerDetails(**kwargs)
    assert isinstance(obj, LockerDetails)


def test_fulfillmentshipmentpackage_instantiates():
    """Instantiate FulfillmentShipmentPackage with dummy data"""
    kwargs = {
        "package_number": 0,
        "carrier_code": "",
        "tracking_number": None,
        "estimated_arrival_date": None,
        "locker_details": None,
        "delivery_information": None,
    }
    obj = FulfillmentShipmentPackage(**kwargs)
    assert isinstance(obj, FulfillmentShipmentPackage)


def test_getdeliveryoffersresult_instantiates():
    """Instantiate GetDeliveryOffersResult with dummy data"""
    kwargs = {
        "delivery_offers": None,
    }
    obj = GetDeliveryOffersResult(**kwargs)
    assert isinstance(obj, GetDeliveryOffersResult)


def test_getdeliveryoffersresponse_instantiates():
    """Instantiate GetDeliveryOffersResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = GetDeliveryOffersResponse(**kwargs)
    assert isinstance(obj, GetDeliveryOffersResponse)


def test_getfeatureinventoryrequest_instantiates():
    """Instantiate GetFeatureInventoryRequest with dummy data"""
    kwargs = {
        "marketplace_id": None,
        "feature_name": "",
        "next_token": None,
        "query_start_date": None,
    }
    obj = GetFeatureInventoryRequest(**kwargs)
    assert isinstance(obj, GetFeatureInventoryRequest)


def test_getfeatureinventoryresult_instantiates():
    """Instantiate GetFeatureInventoryResult with dummy data"""
    kwargs = {
        "marketplace_id": None,
        "feature_name": "",
        "next_token": None,
        "feature_skus": None,
    }
    obj = GetFeatureInventoryResult(**kwargs)
    assert isinstance(obj, GetFeatureInventoryResult)


def test_getfeatureinventoryresponse_instantiates():
    """Instantiate GetFeatureInventoryResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = GetFeatureInventoryResponse(**kwargs)
    assert isinstance(obj, GetFeatureInventoryResponse)


def test_getfeatureskurequest_instantiates():
    """Instantiate GetFeatureSKURequest with dummy data"""
    kwargs = {
        "marketplace_id": None,
        "feature_name": "",
        "seller_sku": "",
    }
    obj = GetFeatureSKURequest(**kwargs)
    assert isinstance(obj, GetFeatureSKURequest)


def test_getfeatureskuresult_instantiates():
    """Instantiate GetFeatureSkuResult with dummy data"""
    kwargs = {
        "marketplace_id": None,
        "feature_name": "",
        "is_eligible": False,
        "ineligible_reasons": None,
        "sku_info": None,
    }
    obj = GetFeatureSkuResult(**kwargs)
    assert isinstance(obj, GetFeatureSkuResult)


def test_getfeatureskuresponse_instantiates():
    """Instantiate GetFeatureSkuResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = GetFeatureSkuResponse(**kwargs)
    assert isinstance(obj, GetFeatureSkuResponse)


def test_getfeaturesrequest_instantiates():
    """Instantiate GetFeaturesRequest with dummy data"""
    kwargs = {
        "marketplace_id": None,
    }
    obj = GetFeaturesRequest(**kwargs)
    assert isinstance(obj, GetFeaturesRequest)


def test_getfeaturesresult_instantiates():
    """Instantiate GetFeaturesResult with dummy data"""
    kwargs = {
        "features": [],
    }
    obj = GetFeaturesResult(**kwargs)
    assert isinstance(obj, GetFeaturesResult)


def test_getfeaturesresponse_instantiates():
    """Instantiate GetFeaturesResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = GetFeaturesResponse(**kwargs)
    assert isinstance(obj, GetFeaturesResponse)


def test_getfulfillmentorderrequest_instantiates():
    """Instantiate GetFulfillmentOrderRequest with dummy data"""
    kwargs = {
        "seller_fulfillment_order_id": "",
    }
    obj = GetFulfillmentOrderRequest(**kwargs)
    assert isinstance(obj, GetFulfillmentOrderRequest)


def test_getfulfillmentorderresult_instantiates():
    """Instantiate GetFulfillmentOrderResult with dummy data"""
    kwargs = {
        "fulfillment_order": FulfillmentOrder(
            **{
                "seller_fulfillment_order_id": "",
                "marketplace_id": None,
                "displayable_order_id": "",
                "displayable_order_date": "",
                "displayable_order_comment": "",
                "shipping_speed_category": "",
                "delivery_window": None,
                "destination_address": Address(
                    **{
                        "name": "",
                        "address_line1": "",
                        "address_line2": None,
                        "address_line3": None,
                        "city": None,
                        "district_or_county": None,
                        "state_or_region": "",
                        "postal_code": "",
                        "country_code": "",
                        "phone": None,
                    }
                ),
                "fulfillment_action": None,
                "fulfillment_policy": None,
                "cod_settings": None,
                "received_date": "",
                "fulfillment_order_status": "",
                "status_updated_date": "",
                "notification_emails": None,
                "feature_constraints": None,
            }
        ),
        "fulfillment_order_items": [],
        "fulfillment_shipments": None,
        "return_items": [],
        "return_authorizations": [],
        "payment_information": None,
    }
    obj = GetFulfillmentOrderResult(**kwargs)
    assert isinstance(obj, GetFulfillmentOrderResult)


def test_getfulfillmentorderresponse_instantiates():
    """Instantiate GetFulfillmentOrderResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = GetFulfillmentOrderResponse(**kwargs)
    assert isinstance(obj, GetFulfillmentOrderResponse)


def test_getfulfillmentpreviewitem_instantiates():
    """Instantiate GetFulfillmentPreviewItem with dummy data"""
    kwargs = {
        "seller_sku": "",
        "quantity": 0,
        "per_unit_declared_value": None,
        "seller_fulfillment_order_item_id": "",
    }
    obj = GetFulfillmentPreviewItem(**kwargs)
    assert isinstance(obj, GetFulfillmentPreviewItem)


def test_getfulfillmentpreviewrequestbody_instantiates():
    """Instantiate GetFulfillmentPreviewRequestBody with dummy data"""
    kwargs = {
        "marketplace_id": None,
        "address": Address(
            **{
                "name": "",
                "address_line1": "",
                "address_line2": None,
                "address_line3": None,
                "city": None,
                "district_or_county": None,
                "state_or_region": "",
                "postal_code": "",
                "country_code": "",
                "phone": None,
            }
        ),
        "items": [],
        "shipping_speed_categories": None,
        "include_c_o_d_fulfillment_preview": None,
        "include_delivery_windows": None,
        "feature_constraints": None,
    }
    obj = GetFulfillmentPreviewRequestBody(**kwargs)
    assert isinstance(obj, GetFulfillmentPreviewRequestBody)


def test_getfulfillmentpreviewrequest_instantiates():
    """Instantiate GetFulfillmentPreviewRequest with dummy data"""
    kwargs = {
        "body": GetFulfillmentPreviewRequestBody(
            **{
                "marketplace_id": None,
                "address": Address(
                    **{
                        "name": "",
                        "address_line1": "",
                        "address_line2": None,
                        "address_line3": None,
                        "city": None,
                        "district_or_county": None,
                        "state_or_region": "",
                        "postal_code": "",
                        "country_code": "",
                        "phone": None,
                    }
                ),
                "items": [],
                "shipping_speed_categories": None,
                "include_c_o_d_fulfillment_preview": None,
                "include_delivery_windows": None,
                "feature_constraints": None,
            }
        ),
    }
    obj = GetFulfillmentPreviewRequest(**kwargs)
    assert isinstance(obj, GetFulfillmentPreviewRequest)


def test_getfulfillmentpreviewresult_instantiates():
    """Instantiate GetFulfillmentPreviewResult with dummy data"""
    kwargs = {
        "fulfillment_previews": None,
    }
    obj = GetFulfillmentPreviewResult(**kwargs)
    assert isinstance(obj, GetFulfillmentPreviewResult)


def test_getfulfillmentpreviewresponse_instantiates():
    """Instantiate GetFulfillmentPreviewResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = GetFulfillmentPreviewResponse(**kwargs)
    assert isinstance(obj, GetFulfillmentPreviewResponse)


def test_getpackagetrackingdetailsrequest_instantiates():
    """Instantiate GetPackageTrackingDetailsRequest with dummy data"""
    kwargs = {
        "package_number": 0,
    }
    obj = GetPackageTrackingDetailsRequest(**kwargs)
    assert isinstance(obj, GetPackageTrackingDetailsRequest)


def test_trackingaddress_instantiates():
    """Instantiate TrackingAddress with dummy data"""
    kwargs = {
        "city": "",
        "state": "",
        "country": "",
    }
    obj = TrackingAddress(**kwargs)
    assert isinstance(obj, TrackingAddress)


def test_packagetrackingdetails_instantiates():
    """Instantiate PackageTrackingDetails with dummy data"""
    kwargs = {
        "package_number": 0,
        "tracking_number": None,
        "customer_tracking_link": None,
        "carrier_code": None,
        "carrier_phone_number": None,
        "carrier_u_r_l": None,
        "ship_date": None,
        "estimated_arrival_date": None,
        "ship_to_address": None,
        "current_status": None,
        "current_status_description": None,
        "delivery_window": None,
        "signed_for_by": None,
        "additional_location_info": None,
        "tracking_events": None,
    }
    obj = PackageTrackingDetails(**kwargs)
    assert isinstance(obj, PackageTrackingDetails)


def test_getpackagetrackingdetailsresponse_instantiates():
    """Instantiate GetPackageTrackingDetailsResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = GetPackageTrackingDetailsResponse(**kwargs)
    assert isinstance(obj, GetPackageTrackingDetailsResponse)


def test_invaliditemreason_instantiates():
    """Instantiate InvalidItemReason with dummy data"""
    kwargs = {
        "invalid_item_reason_code": "",
        "description": "",
    }
    obj = InvalidItemReason(**kwargs)
    assert isinstance(obj, InvalidItemReason)


def test_invalidreturnitem_instantiates():
    """Instantiate InvalidReturnItem with dummy data"""
    kwargs = {
        "seller_return_item_id": "",
        "seller_fulfillment_order_item_id": "",
        "invalid_item_reason": InvalidItemReason(
            **{"invalid_item_reason_code": "", "description": ""}
        ),
    }
    obj = InvalidReturnItem(**kwargs)
    assert isinstance(obj, InvalidReturnItem)


def test_listallfulfillmentordersrequest_instantiates():
    """Instantiate ListAllFulfillmentOrdersRequest with dummy data"""
    kwargs = {
        "query_start_date": None,
        "next_token": None,
    }
    obj = ListAllFulfillmentOrdersRequest(**kwargs)
    assert isinstance(obj, ListAllFulfillmentOrdersRequest)


def test_listallfulfillmentordersresult_instantiates():
    """Instantiate ListAllFulfillmentOrdersResult with dummy data"""
    kwargs = {
        "next_token": None,
        "fulfillment_orders": None,
    }
    obj = ListAllFulfillmentOrdersResult(**kwargs)
    assert isinstance(obj, ListAllFulfillmentOrdersResult)


def test_listallfulfillmentordersresponse_instantiates():
    """Instantiate ListAllFulfillmentOrdersResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = ListAllFulfillmentOrdersResponse(**kwargs)
    assert isinstance(obj, ListAllFulfillmentOrdersResponse)


def test_listreturnreasoncodesrequest_instantiates():
    """Instantiate ListReturnReasonCodesRequest with dummy data"""
    kwargs = {
        "seller_sku": "",
        "marketplace_id": None,
        "seller_fulfillment_order_id": None,
        "language": None,
    }
    obj = ListReturnReasonCodesRequest(**kwargs)
    assert isinstance(obj, ListReturnReasonCodesRequest)


def test_listreturnreasoncodesresult_instantiates():
    """Instantiate ListReturnReasonCodesResult with dummy data"""
    kwargs = {
        "reason_code_details": None,
    }
    obj = ListReturnReasonCodesResult(**kwargs)
    assert isinstance(obj, ListReturnReasonCodesResult)


def test_listreturnreasoncodesresponse_instantiates():
    """Instantiate ListReturnReasonCodesResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = ListReturnReasonCodesResponse(**kwargs)
    assert isinstance(obj, ListReturnReasonCodesResponse)


def test_paymentinformation_instantiates():
    """Instantiate PaymentInformation with dummy data"""
    kwargs = {
        "payment_transaction_id": "",
        "payment_mode": "",
        "payment_date": "",
    }
    obj = PaymentInformation(**kwargs)
    assert isinstance(obj, PaymentInformation)


def test_reasoncodedetails_instantiates():
    """Instantiate ReasonCodeDetails with dummy data"""
    kwargs = {
        "return_reason_code": "",
        "description": "",
        "translated_description": None,
    }
    obj = ReasonCodeDetails(**kwargs)
    assert isinstance(obj, ReasonCodeDetails)


def test_returnauthorization_instantiates():
    """Instantiate ReturnAuthorization with dummy data"""
    kwargs = {
        "return_authorization_id": "",
        "fulfillment_center_id": "",
        "return_to_address": Address(
            **{
                "name": "",
                "address_line1": "",
                "address_line2": None,
                "address_line3": None,
                "city": None,
                "district_or_county": None,
                "state_or_region": "",
                "postal_code": "",
                "country_code": "",
                "phone": None,
            }
        ),
        "amazon_rma_id": "",
        "rma_page_u_r_l": "",
    }
    obj = ReturnAuthorization(**kwargs)
    assert isinstance(obj, ReturnAuthorization)


def test_returnitem_instantiates():
    """Instantiate ReturnItem with dummy data"""
    kwargs = {
        "seller_return_item_id": "",
        "seller_fulfillment_order_item_id": "",
        "amazon_shipment_id": "",
        "seller_return_reason_code": "",
        "return_comment": None,
        "amazon_return_reason_code": None,
        "status": "",
        "status_changed_date": "",
        "return_authorization_id": None,
        "return_received_condition": None,
        "fulfillment_center_id": None,
    }
    obj = ReturnItem(**kwargs)
    assert isinstance(obj, ReturnItem)


def test_submitfulfillmentorderstatusupdaterequestbody_instantiates():
    """Instantiate SubmitFulfillmentOrderStatusUpdateRequestBody with dummy data"""
    kwargs = {
        "fulfillment_order_status": None,
    }
    obj = SubmitFulfillmentOrderStatusUpdateRequestBody(**kwargs)
    assert isinstance(obj, SubmitFulfillmentOrderStatusUpdateRequestBody)


def test_submitfulfillmentorderstatusupdaterequest_instantiates():
    """Instantiate SubmitFulfillmentOrderStatusUpdateRequest with dummy data"""
    kwargs = {
        "seller_fulfillment_order_id": "",
        "body": SubmitFulfillmentOrderStatusUpdateRequestBody(
            **{"fulfillment_order_status": None}
        ),
    }
    obj = SubmitFulfillmentOrderStatusUpdateRequest(**kwargs)
    assert isinstance(obj, SubmitFulfillmentOrderStatusUpdateRequest)


def test_submitfulfillmentorderstatusupdateresponse_instantiates():
    """Instantiate SubmitFulfillmentOrderStatusUpdateResponse with dummy data"""
    kwargs = {
        "errors": None,
    }
    obj = SubmitFulfillmentOrderStatusUpdateResponse(**kwargs)
    assert isinstance(obj, SubmitFulfillmentOrderStatusUpdateResponse)


def test_trackingevent_instantiates():
    """Instantiate TrackingEvent with dummy data"""
    kwargs = {
        "event_date": "",
        "event_address": TrackingAddress(**{"city": "", "state": "", "country": ""}),
        "event_code": "",
        "event_description": "",
    }
    obj = TrackingEvent(**kwargs)
    assert isinstance(obj, TrackingEvent)


def test_unfulfillablepreviewitem_instantiates():
    """Instantiate UnfulfillablePreviewItem with dummy data"""
    kwargs = {
        "seller_sku": "",
        "quantity": 0,
        "seller_fulfillment_order_item_id": "",
        "item_unfulfillable_reasons": None,
    }
    obj = UnfulfillablePreviewItem(**kwargs)
    assert isinstance(obj, UnfulfillablePreviewItem)


def test_updatefulfillmentorderitem_instantiates():
    """Instantiate UpdateFulfillmentOrderItem with dummy data"""
    kwargs = {
        "seller_sku": None,
        "seller_fulfillment_order_item_id": "",
        "quantity": 0,
        "gift_message": None,
        "displayable_comment": None,
        "fulfillment_network_sku": None,
        "order_item_disposition": None,
        "per_unit_declared_value": None,
        "per_unit_price": None,
        "per_unit_tax": None,
    }
    obj = UpdateFulfillmentOrderItem(**kwargs)
    assert isinstance(obj, UpdateFulfillmentOrderItem)


def test_updatefulfillmentorderrequestbody_instantiates():
    """Instantiate UpdateFulfillmentOrderRequestBody with dummy data"""
    kwargs = {
        "marketplace_id": None,
        "displayable_order_id": None,
        "displayable_order_date": None,
        "displayable_order_comment": None,
        "shipping_speed_category": None,
        "destination_address": None,
        "fulfillment_action": None,
        "fulfillment_policy": None,
        "ship_from_country_code": None,
        "notification_emails": None,
        "feature_constraints": None,
        "items": None,
    }
    obj = UpdateFulfillmentOrderRequestBody(**kwargs)
    assert isinstance(obj, UpdateFulfillmentOrderRequestBody)


def test_updatefulfillmentorderrequest_instantiates():
    """Instantiate UpdateFulfillmentOrderRequest with dummy data"""
    kwargs = {
        "body": UpdateFulfillmentOrderRequestBody(
            **{
                "marketplace_id": None,
                "displayable_order_id": None,
                "displayable_order_date": None,
                "displayable_order_comment": None,
                "shipping_speed_category": None,
                "destination_address": None,
                "fulfillment_action": None,
                "fulfillment_policy": None,
                "ship_from_country_code": None,
                "notification_emails": None,
                "feature_constraints": None,
                "items": None,
            }
        ),
        "seller_fulfillment_order_id": "",
    }
    obj = UpdateFulfillmentOrderRequest(**kwargs)
    assert isinstance(obj, UpdateFulfillmentOrderRequest)


def test_updatefulfillmentorderresponse_instantiates():
    """Instantiate UpdateFulfillmentOrderResponse with dummy data"""
    kwargs = {
        "errors": None,
    }
    obj = UpdateFulfillmentOrderResponse(**kwargs)
    assert isinstance(obj, UpdateFulfillmentOrderResponse)
