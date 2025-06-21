# Auto-generated tests for sp_api.api.models.orders.orders_v0.common.py
from datetime import datetime

import pytest
from sp_api.api.models.orders.orders_v0.common import (
    Address, AddressExtendedFields, AddressTypeEnum, AmazonPrograms,
    AssociatedItem, AutomatedShippingSettings, BusinessHours,
    BuyerCustomizedInfoDetail, BuyerInfo, BuyerInvoicePreferenceEnum,
    BuyerRequestedCancel, BuyerTaxInfo, BuyerTaxInformation,
    CodCollectionMethodEnum, ConfirmShipmentErrorResponse,
    ConfirmShipmentOrderItem, ConfirmShipmentRequest,
    ConfirmShipmentRequestBody, DayOfWeekEnum, DeemedResellerCategoryEnum,
    DeliveryPreferences, Error, ExceptionDates, ExportInfo, FieldTypeEnum,
    FulfillmentChannelEnum, FulfillmentInstruction, GetOrderAddressRequest,
    GetOrderAddressResponse, GetOrderBuyerInfoRequest,
    GetOrderBuyerInfoResponse, GetOrderItemsBuyerInfoRequest,
    GetOrderItemsBuyerInfoResponse, GetOrderItemsRequest,
    GetOrderItemsResponse, GetOrderRegulatedInfoRequest,
    GetOrderRegulatedInfoResponse, GetOrderRequest, GetOrderResponse,
    GetOrdersRequest, GetOrdersResponse, GetRequestSerializer, ItemBuyerInfo,
    MarketplaceTaxInfo, Measurement, ModelEnum, Money, OpenInterval,
    OpenTimeInterval, Order, OrderAddress, OrderBuyerInfo, OrderItem,
    OrderItemBuyerInfo, OrderItems, OrderItemsBuyerInfoList, OrderItemsList,
    OrderRegulatedInfo, OrdersList, OrderStatusEnum, OrderTypeEnum,
    PackageDetail, PaymentExecutionDetailItem, PaymentMethodDetailItemList,
    PaymentMethodEnum, PointsGrantedDetail, PreferredDeliveryTime,
    PrescriptionDetail, ProductInfoDetail, PromotionIdList,
    RegulatedInformation, RegulatedInformationField,
    RegulatedOrderVerificationStatus, RejectionReason, RequestsBaseModel,
    ResponsiblePartyEnum, ShippingConstraints, SpApiBaseModel,
    SubstitutionOption, SubstitutionPreferences, SubstitutionTypeEnum,
    TaxClassification, TaxCollection, UnitEnum,
    UpdateShipmentStatusErrorResponse, UpdateShipmentStatusRequest,
    UpdateShipmentStatusRequestBody, UpdateVerificationStatusErrorResponse,
    UpdateVerificationStatusRequest, UpdateVerificationStatusRequestBody,
    ValidVerificationDetail, VerificationDetails)


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


def test_addressextendedfields_instantiates():
    """Instantiate AddressExtendedFields with dummy data"""
    kwargs = {
        "street_name": None,
        "street_number": None,
        "complement": None,
        "neighborhood": None,
    }
    obj = AddressExtendedFields(**kwargs)
    assert isinstance(obj, AddressExtendedFields)


def test_address_instantiates():
    """Instantiate Address with dummy data"""
    kwargs = {
        "name": "",
        "company_name": None,
        "address_line1": None,
        "address_line2": None,
        "address_line3": None,
        "city": None,
        "county": None,
        "district": None,
        "state_or_region": None,
        "municipality": None,
        "postal_code": None,
        "country_code": None,
        "phone": None,
        "extended_fields": None,
        "address_type": None,
    }
    obj = Address(**kwargs)
    assert isinstance(obj, Address)


def test_amazonprograms_instantiates():
    """Instantiate AmazonPrograms with dummy data"""
    kwargs = {
        "programs": [],
    }
    obj = AmazonPrograms(**kwargs)
    assert isinstance(obj, AmazonPrograms)


def test_associateditem_instantiates():
    """Instantiate AssociatedItem with dummy data"""
    kwargs = {
        "order_id": None,
        "order_item_id": None,
        "association_type": None,
    }
    obj = AssociatedItem(**kwargs)
    assert isinstance(obj, AssociatedItem)


def test_automatedshippingsettings_instantiates():
    """Instantiate AutomatedShippingSettings with dummy data"""
    kwargs = {
        "has_automated_shipping_settings": None,
        "automated_carrier": None,
        "automated_ship_method": None,
    }
    obj = AutomatedShippingSettings(**kwargs)
    assert isinstance(obj, AutomatedShippingSettings)


def test_opentimeinterval_instantiates():
    """Instantiate OpenTimeInterval with dummy data"""
    kwargs = {
        "hour": None,
        "minute": None,
    }
    obj = OpenTimeInterval(**kwargs)
    assert isinstance(obj, OpenTimeInterval)


def test_openinterval_instantiates():
    """Instantiate OpenInterval with dummy data"""
    kwargs = {
        "start_time": None,
        "end_time": None,
    }
    obj = OpenInterval(**kwargs)
    assert isinstance(obj, OpenInterval)


def test_businesshours_instantiates():
    """Instantiate BusinessHours with dummy data"""
    kwargs = {
        "day_of_week": None,
        "open_intervals": None,
    }
    obj = BusinessHours(**kwargs)
    assert isinstance(obj, BusinessHours)


def test_buyercustomizedinfodetail_instantiates():
    """Instantiate BuyerCustomizedInfoDetail with dummy data"""
    kwargs = {
        "customized_u_r_l": None,
    }
    obj = BuyerCustomizedInfoDetail(**kwargs)
    assert isinstance(obj, BuyerCustomizedInfoDetail)


def test_taxclassification_instantiates():
    """Instantiate TaxClassification with dummy data"""
    kwargs = {
        "name": None,
        "value": None,
    }
    obj = TaxClassification(**kwargs)
    assert isinstance(obj, TaxClassification)


def test_buyertaxinfo_instantiates():
    """Instantiate BuyerTaxInfo with dummy data"""
    kwargs = {
        "company_legal_name": None,
        "taxing_region": None,
        "tax_classifications": None,
    }
    obj = BuyerTaxInfo(**kwargs)
    assert isinstance(obj, BuyerTaxInfo)


def test_buyerinfo_instantiates():
    """Instantiate BuyerInfo with dummy data"""
    kwargs = {
        "buyer_email": None,
        "buyer_name": None,
        "buyer_county": None,
        "buyer_tax_info": None,
        "purchase_order_number": None,
    }
    obj = BuyerInfo(**kwargs)
    assert isinstance(obj, BuyerInfo)


def test_buyerrequestedcancel_instantiates():
    """Instantiate BuyerRequestedCancel with dummy data"""
    kwargs = {
        "is_buyer_requested_cancel": None,
        "buyer_cancel_reason": None,
    }
    obj = BuyerRequestedCancel(**kwargs)
    assert isinstance(obj, BuyerRequestedCancel)


def test_buyertaxinformation_instantiates():
    """Instantiate BuyerTaxInformation with dummy data"""
    kwargs = {
        "buyer_legal_company_name": None,
        "buyer_business_address": None,
        "buyer_tax_registration_id": None,
        "buyer_tax_office": None,
    }
    obj = BuyerTaxInformation(**kwargs)
    assert isinstance(obj, BuyerTaxInformation)


def test_confirmshipmenterrorresponse_instantiates():
    """Instantiate ConfirmShipmentErrorResponse with dummy data"""
    kwargs = {
        "errors": None,
    }
    obj = ConfirmShipmentErrorResponse(**kwargs)
    assert isinstance(obj, ConfirmShipmentErrorResponse)


def test_confirmshipmentorderitem_instantiates():
    """Instantiate ConfirmShipmentOrderItem with dummy data"""
    kwargs = {
        "order_item_id": "",
        "quantity": 0,
        "transparency_codes": None,
    }
    obj = ConfirmShipmentOrderItem(**kwargs)
    assert isinstance(obj, ConfirmShipmentOrderItem)


def test_packagedetail_instantiates():
    """Instantiate PackageDetail with dummy data"""
    kwargs = {
        "package_reference_id": "",
        "carrier_code": "",
        "carrier_name": None,
        "shipping_method": None,
        "tracking_number": "",
        "ship_date": datetime(2000, 1, 1),
        "ship_from_supply_source_id": None,
        "order_items": [],
    }
    obj = PackageDetail(**kwargs)
    assert isinstance(obj, PackageDetail)


def test_confirmshipmentrequestbody_instantiates():
    """Instantiate ConfirmShipmentRequestBody with dummy data"""
    kwargs = {
        "package_detail": PackageDetail(
            **{
                "package_reference_id": "",
                "carrier_code": "",
                "carrier_name": None,
                "shipping_method": None,
                "tracking_number": "",
                "ship_date": datetime(2000, 1, 1),
                "ship_from_supply_source_id": None,
                "order_items": [],
            }
        ),
        "cod_collection_method": None,
        "marketplace_id": None,
    }
    obj = ConfirmShipmentRequestBody(**kwargs)
    assert isinstance(obj, ConfirmShipmentRequestBody)


def test_confirmshipmentrequest_instantiates():
    """Instantiate ConfirmShipmentRequest with dummy data"""
    kwargs = {
        "order_id": "",
        "payload": ConfirmShipmentRequestBody(
            **{
                "package_detail": PackageDetail(
                    **{
                        "package_reference_id": "",
                        "carrier_code": "",
                        "carrier_name": None,
                        "shipping_method": None,
                        "tracking_number": "",
                        "ship_date": datetime(2000, 1, 1),
                        "ship_from_supply_source_id": None,
                        "order_items": [],
                    }
                ),
                "cod_collection_method": None,
                "marketplace_id": None,
            }
        ),
    }
    obj = ConfirmShipmentRequest(**kwargs)
    assert isinstance(obj, ConfirmShipmentRequest)


def test_exceptiondates_instantiates():
    """Instantiate ExceptionDates with dummy data"""
    kwargs = {
        "exception_date": None,
        "is_open": None,
        "open_intervals": None,
    }
    obj = ExceptionDates(**kwargs)
    assert isinstance(obj, ExceptionDates)


def test_preferreddeliverytime_instantiates():
    """Instantiate PreferredDeliveryTime with dummy data"""
    kwargs = {
        "business_hours": None,
        "exception_dates": None,
    }
    obj = PreferredDeliveryTime(**kwargs)
    assert isinstance(obj, PreferredDeliveryTime)


def test_deliverypreferences_instantiates():
    """Instantiate DeliveryPreferences with dummy data"""
    kwargs = {
        "drop_off_location": None,
        "preferred_delivery_time": None,
        "other_attributes": None,
        "address_instructions": None,
    }
    obj = DeliveryPreferences(**kwargs)
    assert isinstance(obj, DeliveryPreferences)


def test_error_instantiates():
    """Instantiate Error with dummy data"""
    kwargs = {
        "code": "",
        "message": "",
        "details": None,
    }
    obj = Error(**kwargs)
    assert isinstance(obj, Error)


def test_money_instantiates():
    """Instantiate Money with dummy data"""
    kwargs = {
        "currency_code": None,
        "amount": None,
    }
    obj = Money(**kwargs)
    assert isinstance(obj, Money)


def test_exportinfo_instantiates():
    """Instantiate ExportInfo with dummy data"""
    kwargs = {
        "export_charge": None,
        "export_charge_model": None,
    }
    obj = ExportInfo(**kwargs)
    assert isinstance(obj, ExportInfo)


def test_fulfillmentinstruction_instantiates():
    """Instantiate FulfillmentInstruction with dummy data"""
    kwargs = {
        "fulfillment_supply_source_id": None,
    }
    obj = FulfillmentInstruction(**kwargs)
    assert isinstance(obj, FulfillmentInstruction)


def test_getorderaddressrequest_instantiates():
    """Instantiate GetOrderAddressRequest with dummy data"""
    kwargs = {
        "order_id": "",
    }
    obj = GetOrderAddressRequest(**kwargs)
    assert isinstance(obj, GetOrderAddressRequest)


def test_orderaddress_instantiates():
    """Instantiate OrderAddress with dummy data"""
    kwargs = {
        "amazon_order_id": "",
        "buyer_company_name": None,
        "shipping_address": None,
        "delivery_preferences": None,
    }
    obj = OrderAddress(**kwargs)
    assert isinstance(obj, OrderAddress)


def test_getorderaddressresponse_instantiates():
    """Instantiate GetOrderAddressResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = GetOrderAddressResponse(**kwargs)
    assert isinstance(obj, GetOrderAddressResponse)


def test_getorderbuyerinforequest_instantiates():
    """Instantiate GetOrderBuyerInfoRequest with dummy data"""
    kwargs = {
        "order_id": "",
    }
    obj = GetOrderBuyerInfoRequest(**kwargs)
    assert isinstance(obj, GetOrderBuyerInfoRequest)


def test_orderbuyerinfo_instantiates():
    """Instantiate OrderBuyerInfo with dummy data"""
    kwargs = {
        "amazon_order_id": "",
        "buyer_email": None,
        "buyer_name": None,
        "buyer_county": None,
        "buyer_tax_info": None,
        "purchase_order_number": None,
    }
    obj = OrderBuyerInfo(**kwargs)
    assert isinstance(obj, OrderBuyerInfo)


def test_getorderbuyerinforesponse_instantiates():
    """Instantiate GetOrderBuyerInfoResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = GetOrderBuyerInfoResponse(**kwargs)
    assert isinstance(obj, GetOrderBuyerInfoResponse)


def test_getorderitemsbuyerinforequest_instantiates():
    """Instantiate GetOrderItemsBuyerInfoRequest with dummy data"""
    kwargs = {
        "order_id": "",
        "next_token": None,
    }
    obj = GetOrderItemsBuyerInfoRequest(**kwargs)
    assert isinstance(obj, GetOrderItemsBuyerInfoRequest)


def test_orderitemsbuyerinfolist_instantiates():
    """Instantiate OrderItemsBuyerInfoList with dummy data"""
    kwargs = {
        "order_items": [],
        "next_token": None,
        "amazon_order_id": "",
    }
    obj = OrderItemsBuyerInfoList(**kwargs)
    assert isinstance(obj, OrderItemsBuyerInfoList)


def test_getorderitemsbuyerinforesponse_instantiates():
    """Instantiate GetOrderItemsBuyerInfoResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = GetOrderItemsBuyerInfoResponse(**kwargs)
    assert isinstance(obj, GetOrderItemsBuyerInfoResponse)


def test_getorderitemsrequest_instantiates():
    """Instantiate GetOrderItemsRequest with dummy data"""
    kwargs = {
        "order_id": "",
        "next_token": None,
    }
    obj = GetOrderItemsRequest(**kwargs)
    assert isinstance(obj, GetOrderItemsRequest)


def test_orderitemslist_instantiates():
    """Instantiate OrderItemsList with dummy data"""
    kwargs = {
        "order_items": [],
        "next_token": None,
        "amazon_order_id": "",
    }
    obj = OrderItemsList(**kwargs)
    assert isinstance(obj, OrderItemsList)


def test_getorderitemsresponse_instantiates():
    """Instantiate GetOrderItemsResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = GetOrderItemsResponse(**kwargs)
    assert isinstance(obj, GetOrderItemsResponse)


def test_getorderregulatedinforequest_instantiates():
    """Instantiate GetOrderRegulatedInfoRequest with dummy data"""
    kwargs = {
        "order_id": "",
    }
    obj = GetOrderRegulatedInfoRequest(**kwargs)
    assert isinstance(obj, GetOrderRegulatedInfoRequest)


def test_regulatedinformationfield_instantiates():
    """Instantiate RegulatedInformationField with dummy data"""
    kwargs = {
        "field_id": "",
        "field_label": "",
        "field_type": FieldTypeEnum.TEXT,
        "field_value": "",
    }
    obj = RegulatedInformationField(**kwargs)
    assert isinstance(obj, RegulatedInformationField)


def test_regulatedinformation_instantiates():
    """Instantiate RegulatedInformation with dummy data"""
    kwargs = {
        "fields": [],
    }
    obj = RegulatedInformation(**kwargs)
    assert isinstance(obj, RegulatedInformation)


def test_rejectionreason_instantiates():
    """Instantiate RejectionReason with dummy data"""
    kwargs = {
        "rejection_reason_id": "",
        "rejection_reason_description": "",
    }
    obj = RejectionReason(**kwargs)
    assert isinstance(obj, RejectionReason)


def test_validverificationdetail_instantiates():
    """Instantiate ValidVerificationDetail with dummy data"""
    kwargs = {
        "verification_detail_type": "",
        "valid_verification_statuses": [],
    }
    obj = ValidVerificationDetail(**kwargs)
    assert isinstance(obj, ValidVerificationDetail)


def test_regulatedorderverificationstatus_instantiates():
    """Instantiate RegulatedOrderVerificationStatus with dummy data"""
    kwargs = {
        "status": "",
        "requires_merchant_action": False,
        "valid_rejection_reasons": [],
        "rejection_reason": None,
        "review_date": None,
        "external_reviewer_id": None,
        "valid_verification_details": None,
    }
    obj = RegulatedOrderVerificationStatus(**kwargs)
    assert isinstance(obj, RegulatedOrderVerificationStatus)


def test_orderregulatedinfo_instantiates():
    """Instantiate OrderRegulatedInfo with dummy data"""
    kwargs = {
        "amazon_order_id": "",
        "regulated_information": RegulatedInformation(**{"fields": []}),
        "requires_dosage_label": False,
        "regulated_order_verification_status": RegulatedOrderVerificationStatus(
            **{
                "status": "",
                "requires_merchant_action": False,
                "valid_rejection_reasons": [],
                "rejection_reason": None,
                "review_date": None,
                "external_reviewer_id": None,
                "valid_verification_details": None,
            }
        ),
    }
    obj = OrderRegulatedInfo(**kwargs)
    assert isinstance(obj, OrderRegulatedInfo)


def test_getorderregulatedinforesponse_instantiates():
    """Instantiate GetOrderRegulatedInfoResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = GetOrderRegulatedInfoResponse(**kwargs)
    assert isinstance(obj, GetOrderRegulatedInfoResponse)


def test_getorderrequest_instantiates():
    """Instantiate GetOrderRequest with dummy data"""
    kwargs = {
        "order_id": "",
    }
    obj = GetOrderRequest(**kwargs)
    assert isinstance(obj, GetOrderRequest)


def test_marketplacetaxinfo_instantiates():
    """Instantiate MarketplaceTaxInfo with dummy data"""
    kwargs = {
        "tax_classifications": None,
    }
    obj = MarketplaceTaxInfo(**kwargs)
    assert isinstance(obj, MarketplaceTaxInfo)


def test_paymentmethoddetailitemlist_instantiates():
    """Instantiate PaymentMethodDetailItemList with dummy data"""
    kwargs = {}
    obj = PaymentMethodDetailItemList(**kwargs)
    assert isinstance(obj, PaymentMethodDetailItemList)


def test_order_instantiates():
    """Instantiate Order with dummy data"""
    kwargs = {
        "amazon_order_id": "",
        "seller_order_id": None,
        "purchase_date": "",
        "last_update_date": "",
        "order_status": OrderStatusEnum.PENDING,
        "fulfillment_channel": None,
        "sales_channel": None,
        "order_channel": None,
        "ship_service_level": None,
        "order_total": None,
        "number_of_items_shipped": None,
        "number_of_items_unshipped": None,
        "payment_execution_detail": None,
        "payment_method": None,
        "payment_method_details": None,
        "marketplace_id": None,
        "shipment_service_level_category": None,
        "easy_ship_shipment_status": None,
        "cba_displayable_shipping_label": None,
        "order_type": None,
        "earliest_ship_date": None,
        "latest_ship_date": None,
        "earliest_delivery_date": None,
        "latest_delivery_date": None,
        "is_business_order": None,
        "is_prime": None,
        "is_premium_order": None,
        "is_global_express_enabled": None,
        "replaced_order_id": None,
        "is_replacement_order": None,
        "promise_response_due_date": None,
        "is_estimated_ship_date_set": None,
        "is_sold_by_a_b": None,
        "is_i_b_a": None,
        "default_ship_from_location_address": None,
        "buyer_invoice_preference": None,
        "buyer_tax_information": None,
        "fulfillment_instruction": None,
        "is_i_s_p_u": None,
        "is_access_point_order": None,
        "marketplace_tax_info": None,
        "seller_display_name": None,
        "shipping_address": None,
        "buyer_info": None,
        "automated_shipping_settings": None,
        "has_regulated_items": None,
        "electronic_invoice_status": None,
    }
    obj = Order(**kwargs)
    assert isinstance(obj, Order)


def test_getorderresponse_instantiates():
    """Instantiate GetOrderResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = GetOrderResponse(**kwargs)
    assert isinstance(obj, GetOrderResponse)


def test_getordersrequest_instantiates():
    """Instantiate GetOrdersRequest with dummy data"""
    kwargs = {
        "created_after": None,
        "created_before": None,
        "last_updated_after": None,
        "last_updated_before": None,
        "order_statuses": None,
        "marketplace_ids": None,
        "fulfillment_channels": None,
        "payment_methods": None,
        "buyer_email": None,
        "seller_order_id": None,
        "max_results_per_page": None,
        "easy_ship_shipment_statuses": None,
        "electronic_invoice_statuses": None,
        "next_token": None,
        "amazon_order_ids": None,
        "actual_fulfillment_supply_source_id": None,
        "is_i_s_p_u": None,
        "store_chain_store_id": None,
        "earliest_delivery_date_before": None,
        "earliest_delivery_date_after": None,
        "latest_delivery_date_before": None,
        "latest_delivery_date_after": None,
    }
    obj = GetOrdersRequest(**kwargs)
    assert isinstance(obj, GetOrdersRequest)


def test_orderslist_instantiates():
    """Instantiate OrdersList with dummy data"""
    kwargs = {
        "orders": [],
        "next_token": None,
        "last_updated_before": None,
        "created_before": None,
    }
    obj = OrdersList(**kwargs)
    assert isinstance(obj, OrdersList)


def test_getordersresponse_instantiates():
    """Instantiate GetOrdersResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = GetOrdersResponse(**kwargs)
    assert isinstance(obj, GetOrdersResponse)


def test_itembuyerinfo_instantiates():
    """Instantiate ItemBuyerInfo with dummy data"""
    kwargs = {
        "buyer_customized_info": None,
        "gift_wrap_price": None,
        "gift_wrap_tax": None,
        "gift_message_text": None,
        "gift_wrap_level": None,
    }
    obj = ItemBuyerInfo(**kwargs)
    assert isinstance(obj, ItemBuyerInfo)


def test_measurement_instantiates():
    """Instantiate Measurement with dummy data"""
    kwargs = {
        "unit": UnitEnum.OUNCES,
        "value": 0.0,
    }
    obj = Measurement(**kwargs)
    assert isinstance(obj, Measurement)


def test_pointsgranteddetail_instantiates():
    """Instantiate PointsGrantedDetail with dummy data"""
    kwargs = {
        "points_number": None,
        "points_monetary_value": None,
    }
    obj = PointsGrantedDetail(**kwargs)
    assert isinstance(obj, PointsGrantedDetail)


def test_productinfodetail_instantiates():
    """Instantiate ProductInfoDetail with dummy data"""
    kwargs = {
        "number_of_items": None,
    }
    obj = ProductInfoDetail(**kwargs)
    assert isinstance(obj, ProductInfoDetail)


def test_promotionidlist_instantiates():
    """Instantiate PromotionIdList with dummy data"""
    kwargs = {}
    obj = PromotionIdList(**kwargs)
    assert isinstance(obj, PromotionIdList)


def test_shippingconstraints_instantiates():
    """Instantiate ShippingConstraints with dummy data"""
    kwargs = {
        "pallet_delivery": None,
        "signature_confirmation": None,
        "recipient_identity_verification": None,
        "recipient_age_verification": None,
    }
    obj = ShippingConstraints(**kwargs)
    assert isinstance(obj, ShippingConstraints)


def test_substitutionpreferences_instantiates():
    """Instantiate SubstitutionPreferences with dummy data"""
    kwargs = {
        "substitution_type": SubstitutionTypeEnum.CUSTOMER_PREFERENCE,
        "substitution_options": None,
    }
    obj = SubstitutionPreferences(**kwargs)
    assert isinstance(obj, SubstitutionPreferences)


def test_taxcollection_instantiates():
    """Instantiate TaxCollection with dummy data"""
    kwargs = {
        "model": None,
        "responsible_party": None,
    }
    obj = TaxCollection(**kwargs)
    assert isinstance(obj, TaxCollection)


def test_orderitem_instantiates():
    """Instantiate OrderItem with dummy data"""
    kwargs = {
        "a_s_i_n": "",
        "seller_s_k_u": None,
        "order_item_id": "",
        "associated_items": None,
        "title": None,
        "quantity_ordered": 0,
        "quantity_shipped": None,
        "product_info": None,
        "points_granted": None,
        "item_price": None,
        "shipping_price": None,
        "item_tax": None,
        "shipping_tax": None,
        "shipping_discount": None,
        "shipping_discount_tax": None,
        "promotion_discount": None,
        "promotion_discount_tax": None,
        "promotion_ids": None,
        "c_o_d_fee": None,
        "c_o_d_fee_discount": None,
        "is_gift": None,
        "condition_note": None,
        "condition_id": None,
        "condition_subtype_id": None,
        "scheduled_delivery_start_date": None,
        "scheduled_delivery_end_date": None,
        "price_designation": None,
        "tax_collection": None,
        "serial_number_required": None,
        "is_transparency": None,
        "ioss_number": None,
        "store_chain_store_id": None,
        "deemed_reseller_category": None,
        "buyer_info": None,
        "buyer_requested_cancel": None,
        "serial_numbers": None,
        "substitution_preferences": None,
        "measurement": None,
        "shipping_constraints": None,
        "amazon_programs": None,
        "export_info": None,
    }
    obj = OrderItem(**kwargs)
    assert isinstance(obj, OrderItem)


def test_orderitembuyerinfo_instantiates():
    """Instantiate OrderItemBuyerInfo with dummy data"""
    kwargs = {
        "order_item_id": "",
        "buyer_customized_info": None,
        "gift_wrap_price": None,
        "gift_wrap_tax": None,
        "gift_message_text": None,
        "gift_wrap_level": None,
    }
    obj = OrderItemBuyerInfo(**kwargs)
    assert isinstance(obj, OrderItemBuyerInfo)


def test_orderitems_instantiates():
    """Instantiate OrderItems with dummy data"""
    kwargs = {}
    obj = OrderItems(**kwargs)
    assert isinstance(obj, OrderItems)


def test_paymentexecutiondetailitem_instantiates():
    """Instantiate PaymentExecutionDetailItem with dummy data"""
    kwargs = {
        "payment": Money(**{"currency_code": None, "amount": None}),
        "payment_method": "",
    }
    obj = PaymentExecutionDetailItem(**kwargs)
    assert isinstance(obj, PaymentExecutionDetailItem)


def test_prescriptiondetail_instantiates():
    """Instantiate PrescriptionDetail with dummy data"""
    kwargs = {
        "prescription_id": "",
        "expiration_date": datetime(2000, 1, 1),
        "written_quantity": 0,
        "total_refills_authorized": 0,
        "refills_remaining": 0,
        "clinic_id": "",
        "usage_instructions": "",
    }
    obj = PrescriptionDetail(**kwargs)
    assert isinstance(obj, PrescriptionDetail)


def test_substitutionoption_instantiates():
    """Instantiate SubstitutionOption with dummy data"""
    kwargs = {
        "a_s_i_n": None,
        "quantity_ordered": None,
        "seller_s_k_u": None,
        "title": None,
        "measurement": None,
    }
    obj = SubstitutionOption(**kwargs)
    assert isinstance(obj, SubstitutionOption)


def test_updateshipmentstatuserrorresponse_instantiates():
    """Instantiate UpdateShipmentStatusErrorResponse with dummy data"""
    kwargs = {
        "errors": None,
    }
    obj = UpdateShipmentStatusErrorResponse(**kwargs)
    assert isinstance(obj, UpdateShipmentStatusErrorResponse)


def test_updateshipmentstatusrequestbody_instantiates():
    """Instantiate UpdateShipmentStatusRequestBody with dummy data"""
    kwargs = {
        "marketplace_id": None,
        "shipment_status": "",
        "order_items": None,
    }
    obj = UpdateShipmentStatusRequestBody(**kwargs)
    assert isinstance(obj, UpdateShipmentStatusRequestBody)


def test_updateshipmentstatusrequest_instantiates():
    """Instantiate UpdateShipmentStatusRequest with dummy data"""
    kwargs = {
        "order_id": "",
        "payload": UpdateShipmentStatusRequestBody(
            **{"marketplace_id": None, "shipment_status": "", "order_items": None}
        ),
    }
    obj = UpdateShipmentStatusRequest(**kwargs)
    assert isinstance(obj, UpdateShipmentStatusRequest)


def test_updateverificationstatuserrorresponse_instantiates():
    """Instantiate UpdateVerificationStatusErrorResponse with dummy data"""
    kwargs = {
        "errors": None,
    }
    obj = UpdateVerificationStatusErrorResponse(**kwargs)
    assert isinstance(obj, UpdateVerificationStatusErrorResponse)


def test_verificationdetails_instantiates():
    """Instantiate VerificationDetails with dummy data"""
    kwargs = {
        "prescription_detail": None,
    }
    obj = VerificationDetails(**kwargs)
    assert isinstance(obj, VerificationDetails)


def test_updateverificationstatusrequestbody_instantiates():
    """Instantiate UpdateVerificationStatusRequestBody with dummy data"""
    kwargs = {
        "status": None,
        "external_reviewer_id": "",
        "rejection_reason_id": None,
        "verification_details": None,
    }
    obj = UpdateVerificationStatusRequestBody(**kwargs)
    assert isinstance(obj, UpdateVerificationStatusRequestBody)


def test_updateverificationstatusrequest_instantiates():
    """Instantiate UpdateVerificationStatusRequest with dummy data"""
    kwargs = {
        "order_id": "",
        "payload": UpdateVerificationStatusRequestBody(
            **{
                "status": None,
                "external_reviewer_id": "",
                "rejection_reason_id": None,
                "verification_details": None,
            }
        ),
    }
    obj = UpdateVerificationStatusRequest(**kwargs)
    assert isinstance(obj, UpdateVerificationStatusRequest)
