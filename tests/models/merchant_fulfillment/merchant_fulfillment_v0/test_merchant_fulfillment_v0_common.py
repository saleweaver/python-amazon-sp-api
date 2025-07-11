# Auto-generated tests for sp_api.api.models.merchant_fulfillment.merchant_fulfillment_v0.common.py
from datetime import datetime

import pytest
from sp_api.api.models.merchant_fulfillment.merchant_fulfillment_v0.common import (
    AdditionalInputs, AdditionalSellerInput, AdditionalSellerInputs, Address,
    AvailableCarrierWillPickUpOption, AvailableDeliveryExperienceOption,
    AvailableShippingServiceOptions, Benefits, CancelShipmentRequest,
    CancelShipmentResponse, Constraint, CreateShipmentRequest,
    CreateShipmentRequestBody, CreateShipmentResponse, CurrencyAmount,
    DangerousGoodsDetails, DangerousGoodsDetailsPackingGroupEnum,
    DangerousGoodsDetailsPackingInstructionEnum, Error, ExcludedBenefit,
    ExcludedBenefitReasonCodes, FileContents, GetAdditionalSellerInputsRequest,
    GetAdditionalSellerInputsRequestBody, GetAdditionalSellerInputsResponse,
    GetAdditionalSellerInputsResult, GetEligibleShipmentServicesRequest,
    GetEligibleShipmentServicesRequestBody,
    GetEligibleShipmentServicesResponse, GetEligibleShipmentServicesResult,
    GetRequestSerializer, GetShipmentRequest, GetShipmentResponse,
    IncludedBenefits, Item, ItemLevelFields, Label, LabelCustomization,
    LabelDimensions, LabelFormatOption, LabelFormatOptionRequestBody, Length,
    LiquidVolume, LiquidVolumeUnitEnum, PackageDimensions,
    RejectedShippingService, RequestsBaseModel, RestrictedSetValues,
    SellerInputDefinition, Shipment, ShipmentRequestDetails,
    ShippingOfferingFilter, ShippingService, ShippingServiceOptions,
    SpApiBaseModel, TemporarilyUnavailableCarrier,
    TermsAndConditionsNotAcceptedCarrier, Weight)


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
        "district_or_county": None,
        "email": "",
        "city": "",
        "state_or_province_code": None,
        "postal_code": "",
        "country_code": "",
        "phone": "",
    }
    obj = Address(**kwargs)
    assert isinstance(obj, Address)


def test_currencyamount_instantiates():
    """Instantiate CurrencyAmount with dummy data"""
    kwargs = {
        "currency_code": "",
        "amount": 0.0,
    }
    obj = CurrencyAmount(**kwargs)
    assert isinstance(obj, CurrencyAmount)


def test_length_instantiates():
    """Instantiate Length with dummy data"""
    kwargs = {
        "value": None,
        "unit": None,
    }
    obj = Length(**kwargs)
    assert isinstance(obj, Length)


def test_weight_instantiates():
    """Instantiate Weight with dummy data"""
    kwargs = {
        "value": 0.0,
        "unit": "",
    }
    obj = Weight(**kwargs)
    assert isinstance(obj, Weight)


def test_additionalsellerinput_instantiates():
    """Instantiate AdditionalSellerInput with dummy data"""
    kwargs = {
        "data_type": None,
        "value_as_string": None,
        "value_as_boolean": None,
        "value_as_integer": None,
        "value_as_timestamp": None,
        "value_as_address": None,
        "value_as_weight": None,
        "value_as_dimension": None,
        "value_as_currency": None,
    }
    obj = AdditionalSellerInput(**kwargs)
    assert isinstance(obj, AdditionalSellerInput)


def test_restrictedsetvalues_instantiates():
    """Instantiate RestrictedSetValues with dummy data"""
    kwargs = {}
    obj = RestrictedSetValues(**kwargs)
    assert isinstance(obj, RestrictedSetValues)


def test_sellerinputdefinition_instantiates():
    """Instantiate SellerInputDefinition with dummy data"""
    kwargs = {
        "is_required": False,
        "data_type": "",
        "constraints": [],
        "input_display_text": "",
        "input_target": None,
        "stored_value": AdditionalSellerInput(
            **{
                "data_type": None,
                "value_as_string": None,
                "value_as_boolean": None,
                "value_as_integer": None,
                "value_as_timestamp": None,
                "value_as_address": None,
                "value_as_weight": None,
                "value_as_dimension": None,
                "value_as_currency": None,
            }
        ),
        "restricted_set_values": None,
    }
    obj = SellerInputDefinition(**kwargs)
    assert isinstance(obj, SellerInputDefinition)


def test_additionalinputs_instantiates():
    """Instantiate AdditionalInputs with dummy data"""
    kwargs = {
        "additional_input_field_name": None,
        "seller_input_definition": None,
    }
    obj = AdditionalInputs(**kwargs)
    assert isinstance(obj, AdditionalInputs)


def test_additionalsellerinputs_instantiates():
    """Instantiate AdditionalSellerInputs with dummy data"""
    kwargs = {
        "additional_input_field_name": "",
        "additional_seller_input": AdditionalSellerInput(
            **{
                "data_type": None,
                "value_as_string": None,
                "value_as_boolean": None,
                "value_as_integer": None,
                "value_as_timestamp": None,
                "value_as_address": None,
                "value_as_weight": None,
                "value_as_dimension": None,
                "value_as_currency": None,
            }
        ),
    }
    obj = AdditionalSellerInputs(**kwargs)
    assert isinstance(obj, AdditionalSellerInputs)


def test_availablecarrierwillpickupoption_instantiates():
    """Instantiate AvailableCarrierWillPickUpOption with dummy data"""
    kwargs = {
        "carrier_will_pick_up_option": "",
        "charge": CurrencyAmount(**{"currency_code": "", "amount": 0.0}),
    }
    obj = AvailableCarrierWillPickUpOption(**kwargs)
    assert isinstance(obj, AvailableCarrierWillPickUpOption)


def test_availabledeliveryexperienceoption_instantiates():
    """Instantiate AvailableDeliveryExperienceOption with dummy data"""
    kwargs = {
        "delivery_experience_option": "",
        "charge": CurrencyAmount(**{"currency_code": "", "amount": 0.0}),
    }
    obj = AvailableDeliveryExperienceOption(**kwargs)
    assert isinstance(obj, AvailableDeliveryExperienceOption)


def test_availableshippingserviceoptions_instantiates():
    """Instantiate AvailableShippingServiceOptions with dummy data"""
    kwargs = {
        "available_carrier_will_pick_up_options": [],
        "available_delivery_experience_options": [],
    }
    obj = AvailableShippingServiceOptions(**kwargs)
    assert isinstance(obj, AvailableShippingServiceOptions)


def test_includedbenefits_instantiates():
    """Instantiate IncludedBenefits with dummy data"""
    kwargs = {}
    obj = IncludedBenefits(**kwargs)
    assert isinstance(obj, IncludedBenefits)


def test_benefits_instantiates():
    """Instantiate Benefits with dummy data"""
    kwargs = {
        "included_benefits": None,
        "excluded_benefits": None,
    }
    obj = Benefits(**kwargs)
    assert isinstance(obj, Benefits)


def test_cancelshipmentrequest_instantiates():
    """Instantiate CancelShipmentRequest with dummy data"""
    kwargs = {
        "shipment_id": "",
    }
    obj = CancelShipmentRequest(**kwargs)
    assert isinstance(obj, CancelShipmentRequest)


def test_filecontents_instantiates():
    """Instantiate FileContents with dummy data"""
    kwargs = {
        "contents": "",
        "file_type": "",
        "checksum": "",
    }
    obj = FileContents(**kwargs)
    assert isinstance(obj, FileContents)


def test_labeldimensions_instantiates():
    """Instantiate LabelDimensions with dummy data"""
    kwargs = {
        "length": 0.0,
        "width": 0.0,
        "unit": "",
    }
    obj = LabelDimensions(**kwargs)
    assert isinstance(obj, LabelDimensions)


def test_label_instantiates():
    """Instantiate Label with dummy data"""
    kwargs = {
        "custom_text_for_label": None,
        "dimensions": LabelDimensions(**{"length": 0.0, "width": 0.0, "unit": ""}),
        "file_contents": FileContents(
            **{"contents": "", "file_type": "", "checksum": ""}
        ),
        "label_format": None,
        "standard_id_for_label": None,
    }
    obj = Label(**kwargs)
    assert isinstance(obj, Label)


def test_packagedimensions_instantiates():
    """Instantiate PackageDimensions with dummy data"""
    kwargs = {
        "length": None,
        "width": None,
        "height": None,
        "unit": None,
        "predefined_package_dimensions": None,
    }
    obj = PackageDimensions(**kwargs)
    assert isinstance(obj, PackageDimensions)


def test_shippingserviceoptions_instantiates():
    """Instantiate ShippingServiceOptions with dummy data"""
    kwargs = {
        "delivery_experience": "",
        "declared_value": None,
        "carrier_will_pick_up": False,
        "carrier_will_pick_up_option": None,
        "label_format": None,
    }
    obj = ShippingServiceOptions(**kwargs)
    assert isinstance(obj, ShippingServiceOptions)


def test_shippingservice_instantiates():
    """Instantiate ShippingService with dummy data"""
    kwargs = {
        "shipping_service_name": "",
        "carrier_name": "",
        "shipping_service_id": "",
        "shipping_service_offer_id": "",
        "ship_date": "",
        "earliest_estimated_delivery_date": None,
        "latest_estimated_delivery_date": None,
        "rate": CurrencyAmount(**{"currency_code": "", "amount": 0.0}),
        "shipping_service_options": ShippingServiceOptions(
            **{
                "delivery_experience": "",
                "declared_value": None,
                "carrier_will_pick_up": False,
                "carrier_will_pick_up_option": None,
                "label_format": None,
            }
        ),
        "available_shipping_service_options": None,
        "available_label_formats": None,
        "available_format_options_for_label": None,
        "requires_additional_seller_inputs": False,
        "benefits": None,
    }
    obj = ShippingService(**kwargs)
    assert isinstance(obj, ShippingService)


def test_shipment_instantiates():
    """Instantiate Shipment with dummy data"""
    kwargs = {
        "shipment_id": "",
        "amazon_order_id": "",
        "seller_order_id": None,
        "item_list": [],
        "ship_from_address": Address(
            **{
                "name": "",
                "address_line1": "",
                "address_line2": None,
                "address_line3": None,
                "district_or_county": None,
                "email": "",
                "city": "",
                "state_or_province_code": None,
                "postal_code": "",
                "country_code": "",
                "phone": "",
            }
        ),
        "ship_to_address": Address(
            **{
                "name": "",
                "address_line1": "",
                "address_line2": None,
                "address_line3": None,
                "district_or_county": None,
                "email": "",
                "city": "",
                "state_or_province_code": None,
                "postal_code": "",
                "country_code": "",
                "phone": "",
            }
        ),
        "package_dimensions": PackageDimensions(
            **{
                "length": None,
                "width": None,
                "height": None,
                "unit": None,
                "predefined_package_dimensions": None,
            }
        ),
        "weight": Weight(**{"value": 0.0, "unit": ""}),
        "insurance": CurrencyAmount(**{"currency_code": "", "amount": 0.0}),
        "shipping_service": ShippingService(
            **{
                "shipping_service_name": "",
                "carrier_name": "",
                "shipping_service_id": "",
                "shipping_service_offer_id": "",
                "ship_date": "",
                "earliest_estimated_delivery_date": None,
                "latest_estimated_delivery_date": None,
                "rate": CurrencyAmount(**{"currency_code": "", "amount": 0.0}),
                "shipping_service_options": ShippingServiceOptions(
                    **{
                        "delivery_experience": "",
                        "declared_value": None,
                        "carrier_will_pick_up": False,
                        "carrier_will_pick_up_option": None,
                        "label_format": None,
                    }
                ),
                "available_shipping_service_options": None,
                "available_label_formats": None,
                "available_format_options_for_label": None,
                "requires_additional_seller_inputs": False,
                "benefits": None,
            }
        ),
        "label": Label(
            **{
                "custom_text_for_label": None,
                "dimensions": LabelDimensions(
                    **{"length": 0.0, "width": 0.0, "unit": ""}
                ),
                "file_contents": FileContents(
                    **{"contents": "", "file_type": "", "checksum": ""}
                ),
                "label_format": None,
                "standard_id_for_label": None,
            }
        ),
        "status": "",
        "tracking_id": None,
        "created_date": "",
        "last_updated_date": None,
    }
    obj = Shipment(**kwargs)
    assert isinstance(obj, Shipment)


def test_cancelshipmentresponse_instantiates():
    """Instantiate CancelShipmentResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = CancelShipmentResponse(**kwargs)
    assert isinstance(obj, CancelShipmentResponse)


def test_constraint_instantiates():
    """Instantiate Constraint with dummy data"""
    kwargs = {
        "validation_reg_ex": None,
        "validation_string": "",
    }
    obj = Constraint(**kwargs)
    assert isinstance(obj, Constraint)


def test_labelformatoptionrequestbody_instantiates():
    """Instantiate LabelFormatOptionRequestBody with dummy data"""
    kwargs = {
        "include_packing_slip_with_label": None,
    }
    obj = LabelFormatOptionRequestBody(**kwargs)
    assert isinstance(obj, LabelFormatOptionRequestBody)


def test_labelcustomization_instantiates():
    """Instantiate LabelCustomization with dummy data"""
    kwargs = {
        "custom_text_for_label": None,
        "standard_id_for_label": None,
    }
    obj = LabelCustomization(**kwargs)
    assert isinstance(obj, LabelCustomization)


def test_shipmentrequestdetails_instantiates():
    """Instantiate ShipmentRequestDetails with dummy data"""
    kwargs = {
        "amazon_order_id": "",
        "seller_order_id": None,
        "item_list": [],
        "ship_from_address": Address(
            **{
                "name": "",
                "address_line1": "",
                "address_line2": None,
                "address_line3": None,
                "district_or_county": None,
                "email": "",
                "city": "",
                "state_or_province_code": None,
                "postal_code": "",
                "country_code": "",
                "phone": "",
            }
        ),
        "package_dimensions": PackageDimensions(
            **{
                "length": None,
                "width": None,
                "height": None,
                "unit": None,
                "predefined_package_dimensions": None,
            }
        ),
        "weight": Weight(**{"value": 0.0, "unit": ""}),
        "must_arrive_by_date": None,
        "ship_date": None,
        "shipping_service_options": ShippingServiceOptions(
            **{
                "delivery_experience": "",
                "declared_value": None,
                "carrier_will_pick_up": False,
                "carrier_will_pick_up_option": None,
                "label_format": None,
            }
        ),
        "label_customization": None,
    }
    obj = ShipmentRequestDetails(**kwargs)
    assert isinstance(obj, ShipmentRequestDetails)


def test_createshipmentrequestbody_instantiates():
    """Instantiate CreateShipmentRequestBody with dummy data"""
    kwargs = {
        "shipment_request_details": ShipmentRequestDetails(
            **{
                "amazon_order_id": "",
                "seller_order_id": None,
                "item_list": [],
                "ship_from_address": Address(
                    **{
                        "name": "",
                        "address_line1": "",
                        "address_line2": None,
                        "address_line3": None,
                        "district_or_county": None,
                        "email": "",
                        "city": "",
                        "state_or_province_code": None,
                        "postal_code": "",
                        "country_code": "",
                        "phone": "",
                    }
                ),
                "package_dimensions": PackageDimensions(
                    **{
                        "length": None,
                        "width": None,
                        "height": None,
                        "unit": None,
                        "predefined_package_dimensions": None,
                    }
                ),
                "weight": Weight(**{"value": 0.0, "unit": ""}),
                "must_arrive_by_date": None,
                "ship_date": None,
                "shipping_service_options": ShippingServiceOptions(
                    **{
                        "delivery_experience": "",
                        "declared_value": None,
                        "carrier_will_pick_up": False,
                        "carrier_will_pick_up_option": None,
                        "label_format": None,
                    }
                ),
                "label_customization": None,
            }
        ),
        "shipping_service_id": "",
        "shipping_service_offer_id": None,
        "hazmat_type": None,
        "label_format_option": None,
        "shipment_level_seller_inputs_list": None,
    }
    obj = CreateShipmentRequestBody(**kwargs)
    assert isinstance(obj, CreateShipmentRequestBody)


def test_createshipmentrequest_instantiates():
    """Instantiate CreateShipmentRequest with dummy data"""
    kwargs = {
        "body": CreateShipmentRequestBody(
            **{
                "shipment_request_details": ShipmentRequestDetails(
                    **{
                        "amazon_order_id": "",
                        "seller_order_id": None,
                        "item_list": [],
                        "ship_from_address": Address(
                            **{
                                "name": "",
                                "address_line1": "",
                                "address_line2": None,
                                "address_line3": None,
                                "district_or_county": None,
                                "email": "",
                                "city": "",
                                "state_or_province_code": None,
                                "postal_code": "",
                                "country_code": "",
                                "phone": "",
                            }
                        ),
                        "package_dimensions": PackageDimensions(
                            **{
                                "length": None,
                                "width": None,
                                "height": None,
                                "unit": None,
                                "predefined_package_dimensions": None,
                            }
                        ),
                        "weight": Weight(**{"value": 0.0, "unit": ""}),
                        "must_arrive_by_date": None,
                        "ship_date": None,
                        "shipping_service_options": ShippingServiceOptions(
                            **{
                                "delivery_experience": "",
                                "declared_value": None,
                                "carrier_will_pick_up": False,
                                "carrier_will_pick_up_option": None,
                                "label_format": None,
                            }
                        ),
                        "label_customization": None,
                    }
                ),
                "shipping_service_id": "",
                "shipping_service_offer_id": None,
                "hazmat_type": None,
                "label_format_option": None,
                "shipment_level_seller_inputs_list": None,
            }
        ),
    }
    obj = CreateShipmentRequest(**kwargs)
    assert isinstance(obj, CreateShipmentRequest)


def test_createshipmentresponse_instantiates():
    """Instantiate CreateShipmentResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = CreateShipmentResponse(**kwargs)
    assert isinstance(obj, CreateShipmentResponse)


def test_dangerousgoodsdetails_instantiates():
    """Instantiate DangerousGoodsDetails with dummy data"""
    kwargs = {
        "united_nations_regulatory_id": None,
        "transportation_regulatory_class": None,
        "packing_group": None,
        "packing_instruction": None,
    }
    obj = DangerousGoodsDetails(**kwargs)
    assert isinstance(obj, DangerousGoodsDetails)


def test_error_instantiates():
    """Instantiate Error with dummy data"""
    kwargs = {
        "code": "",
        "message": "",
        "details": None,
    }
    obj = Error(**kwargs)
    assert isinstance(obj, Error)


def test_excludedbenefitreasoncodes_instantiates():
    """Instantiate ExcludedBenefitReasonCodes with dummy data"""
    kwargs = {}
    obj = ExcludedBenefitReasonCodes(**kwargs)
    assert isinstance(obj, ExcludedBenefitReasonCodes)


def test_excludedbenefit_instantiates():
    """Instantiate ExcludedBenefit with dummy data"""
    kwargs = {
        "benefit": None,
        "reason_codes": None,
    }
    obj = ExcludedBenefit(**kwargs)
    assert isinstance(obj, ExcludedBenefit)


def test_getadditionalsellerinputsrequestbody_instantiates():
    """Instantiate GetAdditionalSellerInputsRequestBody with dummy data"""
    kwargs = {
        "shipping_service_id": "",
        "ship_from_address": Address(
            **{
                "name": "",
                "address_line1": "",
                "address_line2": None,
                "address_line3": None,
                "district_or_county": None,
                "email": "",
                "city": "",
                "state_or_province_code": None,
                "postal_code": "",
                "country_code": "",
                "phone": "",
            }
        ),
        "order_id": "",
    }
    obj = GetAdditionalSellerInputsRequestBody(**kwargs)
    assert isinstance(obj, GetAdditionalSellerInputsRequestBody)


def test_getadditionalsellerinputsrequest_instantiates():
    """Instantiate GetAdditionalSellerInputsRequest with dummy data"""
    kwargs = {
        "body": GetAdditionalSellerInputsRequestBody(
            **{
                "shipping_service_id": "",
                "ship_from_address": Address(
                    **{
                        "name": "",
                        "address_line1": "",
                        "address_line2": None,
                        "address_line3": None,
                        "district_or_county": None,
                        "email": "",
                        "city": "",
                        "state_or_province_code": None,
                        "postal_code": "",
                        "country_code": "",
                        "phone": "",
                    }
                ),
                "order_id": "",
            }
        ),
    }
    obj = GetAdditionalSellerInputsRequest(**kwargs)
    assert isinstance(obj, GetAdditionalSellerInputsRequest)


def test_getadditionalsellerinputsresult_instantiates():
    """Instantiate GetAdditionalSellerInputsResult with dummy data"""
    kwargs = {
        "shipment_level_fields": None,
        "item_level_fields_list": None,
    }
    obj = GetAdditionalSellerInputsResult(**kwargs)
    assert isinstance(obj, GetAdditionalSellerInputsResult)


def test_getadditionalsellerinputsresponse_instantiates():
    """Instantiate GetAdditionalSellerInputsResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = GetAdditionalSellerInputsResponse(**kwargs)
    assert isinstance(obj, GetAdditionalSellerInputsResponse)


def test_shippingofferingfilter_instantiates():
    """Instantiate ShippingOfferingFilter with dummy data"""
    kwargs = {
        "include_packing_slip_with_label": None,
        "include_complex_shipping_options": None,
        "carrier_will_pick_up": None,
        "delivery_experience": None,
    }
    obj = ShippingOfferingFilter(**kwargs)
    assert isinstance(obj, ShippingOfferingFilter)


def test_geteligibleshipmentservicesrequestbody_instantiates():
    """Instantiate GetEligibleShipmentServicesRequestBody with dummy data"""
    kwargs = {
        "shipment_request_details": ShipmentRequestDetails(
            **{
                "amazon_order_id": "",
                "seller_order_id": None,
                "item_list": [],
                "ship_from_address": Address(
                    **{
                        "name": "",
                        "address_line1": "",
                        "address_line2": None,
                        "address_line3": None,
                        "district_or_county": None,
                        "email": "",
                        "city": "",
                        "state_or_province_code": None,
                        "postal_code": "",
                        "country_code": "",
                        "phone": "",
                    }
                ),
                "package_dimensions": PackageDimensions(
                    **{
                        "length": None,
                        "width": None,
                        "height": None,
                        "unit": None,
                        "predefined_package_dimensions": None,
                    }
                ),
                "weight": Weight(**{"value": 0.0, "unit": ""}),
                "must_arrive_by_date": None,
                "ship_date": None,
                "shipping_service_options": ShippingServiceOptions(
                    **{
                        "delivery_experience": "",
                        "declared_value": None,
                        "carrier_will_pick_up": False,
                        "carrier_will_pick_up_option": None,
                        "label_format": None,
                    }
                ),
                "label_customization": None,
            }
        ),
        "shipping_offering_filter": None,
    }
    obj = GetEligibleShipmentServicesRequestBody(**kwargs)
    assert isinstance(obj, GetEligibleShipmentServicesRequestBody)


def test_geteligibleshipmentservicesrequest_instantiates():
    """Instantiate GetEligibleShipmentServicesRequest with dummy data"""
    kwargs = {
        "body": GetEligibleShipmentServicesRequestBody(
            **{
                "shipment_request_details": ShipmentRequestDetails(
                    **{
                        "amazon_order_id": "",
                        "seller_order_id": None,
                        "item_list": [],
                        "ship_from_address": Address(
                            **{
                                "name": "",
                                "address_line1": "",
                                "address_line2": None,
                                "address_line3": None,
                                "district_or_county": None,
                                "email": "",
                                "city": "",
                                "state_or_province_code": None,
                                "postal_code": "",
                                "country_code": "",
                                "phone": "",
                            }
                        ),
                        "package_dimensions": PackageDimensions(
                            **{
                                "length": None,
                                "width": None,
                                "height": None,
                                "unit": None,
                                "predefined_package_dimensions": None,
                            }
                        ),
                        "weight": Weight(**{"value": 0.0, "unit": ""}),
                        "must_arrive_by_date": None,
                        "ship_date": None,
                        "shipping_service_options": ShippingServiceOptions(
                            **{
                                "delivery_experience": "",
                                "declared_value": None,
                                "carrier_will_pick_up": False,
                                "carrier_will_pick_up_option": None,
                                "label_format": None,
                            }
                        ),
                        "label_customization": None,
                    }
                ),
                "shipping_offering_filter": None,
            }
        ),
    }
    obj = GetEligibleShipmentServicesRequest(**kwargs)
    assert isinstance(obj, GetEligibleShipmentServicesRequest)


def test_geteligibleshipmentservicesresult_instantiates():
    """Instantiate GetEligibleShipmentServicesResult with dummy data"""
    kwargs = {
        "shipping_service_list": [],
        "rejected_shipping_service_list": None,
        "temporarily_unavailable_carrier_list": None,
        "terms_and_conditions_not_accepted_carrier_list": None,
    }
    obj = GetEligibleShipmentServicesResult(**kwargs)
    assert isinstance(obj, GetEligibleShipmentServicesResult)


def test_geteligibleshipmentservicesresponse_instantiates():
    """Instantiate GetEligibleShipmentServicesResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = GetEligibleShipmentServicesResponse(**kwargs)
    assert isinstance(obj, GetEligibleShipmentServicesResponse)


def test_getshipmentrequest_instantiates():
    """Instantiate GetShipmentRequest with dummy data"""
    kwargs = {
        "shipment_id": "",
    }
    obj = GetShipmentRequest(**kwargs)
    assert isinstance(obj, GetShipmentRequest)


def test_getshipmentresponse_instantiates():
    """Instantiate GetShipmentResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = GetShipmentResponse(**kwargs)
    assert isinstance(obj, GetShipmentResponse)


def test_liquidvolume_instantiates():
    """Instantiate LiquidVolume with dummy data"""
    kwargs = {
        "unit": LiquidVolumeUnitEnum.ML,
        "value": 0.0,
    }
    obj = LiquidVolume(**kwargs)
    assert isinstance(obj, LiquidVolume)


def test_item_instantiates():
    """Instantiate Item with dummy data"""
    kwargs = {
        "order_item_id": "",
        "quantity": 0,
        "item_weight": None,
        "item_description": None,
        "transparency_code_list": None,
        "item_level_seller_inputs_list": None,
        "liquid_volume": None,
        "is_hazmat": None,
        "dangerous_goods_details": None,
    }
    obj = Item(**kwargs)
    assert isinstance(obj, Item)


def test_itemlevelfields_instantiates():
    """Instantiate ItemLevelFields with dummy data"""
    kwargs = {
        "asin": "",
        "additional_inputs": [],
    }
    obj = ItemLevelFields(**kwargs)
    assert isinstance(obj, ItemLevelFields)


def test_labelformatoption_instantiates():
    """Instantiate LabelFormatOption with dummy data"""
    kwargs = {
        "include_packing_slip_with_label": None,
        "label_format": None,
    }
    obj = LabelFormatOption(**kwargs)
    assert isinstance(obj, LabelFormatOption)


def test_rejectedshippingservice_instantiates():
    """Instantiate RejectedShippingService with dummy data"""
    kwargs = {
        "carrier_name": "",
        "shipping_service_name": "",
        "shipping_service_id": "",
        "rejection_reason_code": "",
        "rejection_reason_message": None,
    }
    obj = RejectedShippingService(**kwargs)
    assert isinstance(obj, RejectedShippingService)


def test_temporarilyunavailablecarrier_instantiates():
    """Instantiate TemporarilyUnavailableCarrier with dummy data"""
    kwargs = {
        "carrier_name": "",
    }
    obj = TemporarilyUnavailableCarrier(**kwargs)
    assert isinstance(obj, TemporarilyUnavailableCarrier)


def test_termsandconditionsnotacceptedcarrier_instantiates():
    """Instantiate TermsAndConditionsNotAcceptedCarrier with dummy data"""
    kwargs = {
        "carrier_name": "",
    }
    obj = TermsAndConditionsNotAcceptedCarrier(**kwargs)
    assert isinstance(obj, TermsAndConditionsNotAcceptedCarrier)
