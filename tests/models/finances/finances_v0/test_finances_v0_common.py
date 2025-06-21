# Auto-generated tests for sp_api.api.models.finances.finances_v0.common.py
from datetime import datetime

import pytest
from sp_api.api.models.finances.finances_v0.common import (
    AdhocDisbursementEvent, AdjustmentEvent, AdjustmentItem,
    AffordabilityExpenseEvent, CapacityReservationBillingEvent,
    ChargeComponent, ChargeInstrument, ChargeRefundEvent,
    ChargeRefundTransaction, CouponPaymentEvent, Currency, DebtRecoveryEvent,
    DebtRecoveryItem, DirectPayment, Error, FailedAdhocDisbursementEvent,
    FBALiquidationEvent, FeeComponent, FinancialEventGroup, FinancialEvents,
    GetRequestSerializer, ImagingServicesFeeEvent,
    ListFinancialEventGroupsPayload, ListFinancialEventGroupsRequest,
    ListFinancialEventGroupsResponse, ListFinancialEventsByGroupIdRequest,
    ListFinancialEventsByOrderIdRequest, ListFinancialEventsPayload,
    ListFinancialEventsRequest, ListFinancialEventsResponse,
    LoanServicingEvent, NetworkComminglingTransactionEvent, PayWithAmazonEvent,
    ProductAdsPaymentEvent, Promotion, RemovalShipmentAdjustmentEvent,
    RemovalShipmentEvent, RemovalShipmentItem, RemovalShipmentItemAdjustment,
    RentalTransactionEvent, RequestsBaseModel, RetrochargeEvent,
    SAFETReimbursementEvent, SAFETReimbursementItem, SellerDealPaymentEvent,
    SellerReviewEnrollmentPaymentEvent, ServiceFeeEvent, ShipmentEvent,
    ShipmentItem, SolutionProviderCreditEvent, SpApiBaseModel,
    TaxWithheldComponent, TaxWithholdingEvent, TaxWithholdingPeriod,
    TDSReimbursementEvent, TrialShipmentEvent, ValueAddedServiceChargeEvent)


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


def test_currency_instantiates():
    """Instantiate Currency with dummy data"""
    kwargs = {
        "currency_code": None,
        "currency_amount": None,
    }
    obj = Currency(**kwargs)
    assert isinstance(obj, Currency)


def test_adhocdisbursementevent_instantiates():
    """Instantiate AdhocDisbursementEvent with dummy data"""
    kwargs = {
        "transaction_type": None,
        "posted_date": None,
        "transaction_id": None,
        "transaction_amount": None,
    }
    obj = AdhocDisbursementEvent(**kwargs)
    assert isinstance(obj, AdhocDisbursementEvent)


def test_adjustmentevent_instantiates():
    """Instantiate AdjustmentEvent with dummy data"""
    kwargs = {
        "adjustment_type": None,
        "posted_date": None,
        "store_name": None,
        "adjustment_amount": None,
        "adjustment_item_list": None,
    }
    obj = AdjustmentEvent(**kwargs)
    assert isinstance(obj, AdjustmentEvent)


def test_adjustmentitem_instantiates():
    """Instantiate AdjustmentItem with dummy data"""
    kwargs = {
        "quantity": None,
        "per_unit_amount": None,
        "total_amount": None,
        "seller_s_k_u": None,
        "fn_s_k_u": None,
        "product_description": None,
        "a_s_i_n": None,
        "transaction_number": None,
    }
    obj = AdjustmentItem(**kwargs)
    assert isinstance(obj, AdjustmentItem)


def test_affordabilityexpenseevent_instantiates():
    """Instantiate AffordabilityExpenseEvent with dummy data"""
    kwargs = {
        "amazon_order_id": None,
        "posted_date": None,
        "marketplace_id": None,
        "transaction_type": None,
        "base_expense": None,
        "tax_type_c_g_s_t": Currency(
            **{"currency_code": None, "currency_amount": None}
        ),
        "tax_type_s_g_s_t": Currency(
            **{"currency_code": None, "currency_amount": None}
        ),
        "tax_type_i_g_s_t": Currency(
            **{"currency_code": None, "currency_amount": None}
        ),
        "total_expense": None,
    }
    obj = AffordabilityExpenseEvent(**kwargs)
    assert isinstance(obj, AffordabilityExpenseEvent)


def test_capacityreservationbillingevent_instantiates():
    """Instantiate CapacityReservationBillingEvent with dummy data"""
    kwargs = {
        "transaction_type": None,
        "posted_date": None,
        "description": None,
        "transaction_amount": None,
    }
    obj = CapacityReservationBillingEvent(**kwargs)
    assert isinstance(obj, CapacityReservationBillingEvent)


def test_chargecomponent_instantiates():
    """Instantiate ChargeComponent with dummy data"""
    kwargs = {
        "charge_type": None,
        "charge_amount": None,
    }
    obj = ChargeComponent(**kwargs)
    assert isinstance(obj, ChargeComponent)


def test_chargeinstrument_instantiates():
    """Instantiate ChargeInstrument with dummy data"""
    kwargs = {
        "description": None,
        "tail": None,
        "amount": None,
    }
    obj = ChargeInstrument(**kwargs)
    assert isinstance(obj, ChargeInstrument)


def test_chargerefundevent_instantiates():
    """Instantiate ChargeRefundEvent with dummy data"""
    kwargs = {
        "posted_date": None,
        "reason_code": None,
        "reason_code_description": None,
        "charge_refund_transactions": None,
    }
    obj = ChargeRefundEvent(**kwargs)
    assert isinstance(obj, ChargeRefundEvent)


def test_chargerefundtransaction_instantiates():
    """Instantiate ChargeRefundTransaction with dummy data"""
    kwargs = {
        "charge_amount": None,
        "charge_type": None,
    }
    obj = ChargeRefundTransaction(**kwargs)
    assert isinstance(obj, ChargeRefundTransaction)


def test_feecomponent_instantiates():
    """Instantiate FeeComponent with dummy data"""
    kwargs = {
        "fee_type": None,
        "fee_amount": None,
    }
    obj = FeeComponent(**kwargs)
    assert isinstance(obj, FeeComponent)


def test_couponpaymentevent_instantiates():
    """Instantiate CouponPaymentEvent with dummy data"""
    kwargs = {
        "posted_date": None,
        "coupon_id": None,
        "seller_coupon_description": None,
        "clip_or_redemption_count": None,
        "payment_event_id": None,
        "fee_component": None,
        "charge_component": None,
        "total_amount": None,
    }
    obj = CouponPaymentEvent(**kwargs)
    assert isinstance(obj, CouponPaymentEvent)


def test_debtrecoveryevent_instantiates():
    """Instantiate DebtRecoveryEvent with dummy data"""
    kwargs = {
        "debt_recovery_type": None,
        "recovery_amount": None,
        "over_payment_credit": None,
        "debt_recovery_item_list": None,
        "charge_instrument_list": None,
    }
    obj = DebtRecoveryEvent(**kwargs)
    assert isinstance(obj, DebtRecoveryEvent)


def test_debtrecoveryitem_instantiates():
    """Instantiate DebtRecoveryItem with dummy data"""
    kwargs = {
        "recovery_amount": None,
        "original_amount": None,
        "group_begin_date": None,
        "group_end_date": None,
    }
    obj = DebtRecoveryItem(**kwargs)
    assert isinstance(obj, DebtRecoveryItem)


def test_directpayment_instantiates():
    """Instantiate DirectPayment with dummy data"""
    kwargs = {
        "direct_payment_type": None,
        "direct_payment_amount": None,
    }
    obj = DirectPayment(**kwargs)
    assert isinstance(obj, DirectPayment)


def test_error_instantiates():
    """Instantiate Error with dummy data"""
    kwargs = {
        "code": "",
        "message": "",
        "details": None,
    }
    obj = Error(**kwargs)
    assert isinstance(obj, Error)


def test_fbaliquidationevent_instantiates():
    """Instantiate FBALiquidationEvent with dummy data"""
    kwargs = {
        "posted_date": None,
        "original_removal_order_id": None,
        "liquidation_proceeds_amount": None,
        "liquidation_fee_amount": None,
    }
    obj = FBALiquidationEvent(**kwargs)
    assert isinstance(obj, FBALiquidationEvent)


def test_failedadhocdisbursementevent_instantiates():
    """Instantiate FailedAdhocDisbursementEvent with dummy data"""
    kwargs = {
        "funds_transfers_type": None,
        "transfer_id": None,
        "disbursement_id": None,
        "payment_disbursement_type": None,
        "status": None,
        "transfer_amount": None,
        "posted_date": None,
    }
    obj = FailedAdhocDisbursementEvent(**kwargs)
    assert isinstance(obj, FailedAdhocDisbursementEvent)


def test_financialeventgroup_instantiates():
    """Instantiate FinancialEventGroup with dummy data"""
    kwargs = {
        "financial_event_group_id": None,
        "processing_status": None,
        "fund_transfer_status": None,
        "original_total": None,
        "converted_total": None,
        "fund_transfer_date": None,
        "trace_id": None,
        "account_tail": None,
        "beginning_balance": None,
        "financial_event_group_start": None,
        "financial_event_group_end": None,
    }
    obj = FinancialEventGroup(**kwargs)
    assert isinstance(obj, FinancialEventGroup)


def test_financialevents_instantiates():
    """Instantiate FinancialEvents with dummy data"""
    kwargs = {
        "shipment_event_list": None,
        "shipment_settle_event_list": None,
        "refund_event_list": None,
        "guarantee_claim_event_list": None,
        "chargeback_event_list": None,
        "pay_with_amazon_event_list": None,
        "service_provider_credit_event_list": None,
        "retrocharge_event_list": None,
        "rental_transaction_event_list": None,
        "product_ads_payment_event_list": None,
        "service_fee_event_list": None,
        "seller_deal_payment_event_list": None,
        "debt_recovery_event_list": None,
        "loan_servicing_event_list": None,
        "adjustment_event_list": None,
        "s_a_f_e_t_reimbursement_event_list": None,
        "seller_review_enrollment_payment_event_list": None,
        "f_b_a_liquidation_event_list": None,
        "coupon_payment_event_list": None,
        "imaging_services_fee_event_list": None,
        "network_commingling_transaction_event_list": None,
        "affordability_expense_event_list": None,
        "affordability_expense_reversal_event_list": None,
        "removal_shipment_event_list": None,
        "removal_shipment_adjustment_event_list": None,
        "trial_shipment_event_list": None,
        "t_d_s_reimbursement_event_list": None,
        "adhoc_disbursement_event_list": None,
        "tax_withholding_event_list": None,
        "charge_refund_event_list": None,
        "failed_adhoc_disbursement_event_list": None,
        "value_added_service_charge_event_list": None,
        "capacity_reservation_billing_event_list": None,
    }
    obj = FinancialEvents(**kwargs)
    assert isinstance(obj, FinancialEvents)


def test_imagingservicesfeeevent_instantiates():
    """Instantiate ImagingServicesFeeEvent with dummy data"""
    kwargs = {
        "imaging_request_billing_item_i_d": None,
        "a_s_i_n": None,
        "posted_date": None,
        "fee_list": None,
    }
    obj = ImagingServicesFeeEvent(**kwargs)
    assert isinstance(obj, ImagingServicesFeeEvent)


def test_listfinancialeventgroupspayload_instantiates():
    """Instantiate ListFinancialEventGroupsPayload with dummy data"""
    kwargs = {
        "next_token": None,
        "financial_event_group_list": None,
    }
    obj = ListFinancialEventGroupsPayload(**kwargs)
    assert isinstance(obj, ListFinancialEventGroupsPayload)


def test_listfinancialeventgroupsrequest_instantiates():
    """Instantiate ListFinancialEventGroupsRequest with dummy data"""
    kwargs = {
        "max_results_per_page": None,
        "financial_event_group_started_before": None,
        "financial_event_group_started_after": None,
        "next_token": None,
    }
    obj = ListFinancialEventGroupsRequest(**kwargs)
    assert isinstance(obj, ListFinancialEventGroupsRequest)


def test_listfinancialeventgroupsresponse_instantiates():
    """Instantiate ListFinancialEventGroupsResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = ListFinancialEventGroupsResponse(**kwargs)
    assert isinstance(obj, ListFinancialEventGroupsResponse)


def test_listfinancialeventsbygroupidrequest_instantiates():
    """Instantiate ListFinancialEventsByGroupIdRequest with dummy data"""
    kwargs = {
        "max_results_per_page": None,
        "posted_after": None,
        "posted_before": None,
        "event_group_id": "",
        "next_token": None,
    }
    obj = ListFinancialEventsByGroupIdRequest(**kwargs)
    assert isinstance(obj, ListFinancialEventsByGroupIdRequest)


def test_listfinancialeventsbyorderidrequest_instantiates():
    """Instantiate ListFinancialEventsByOrderIdRequest with dummy data"""
    kwargs = {
        "order_id": "",
        "max_results_per_page": None,
        "next_token": None,
    }
    obj = ListFinancialEventsByOrderIdRequest(**kwargs)
    assert isinstance(obj, ListFinancialEventsByOrderIdRequest)


def test_listfinancialeventspayload_instantiates():
    """Instantiate ListFinancialEventsPayload with dummy data"""
    kwargs = {
        "next_token": None,
        "financial_events": None,
    }
    obj = ListFinancialEventsPayload(**kwargs)
    assert isinstance(obj, ListFinancialEventsPayload)


def test_listfinancialeventsrequest_instantiates():
    """Instantiate ListFinancialEventsRequest with dummy data"""
    kwargs = {
        "max_results_per_page": None,
        "posted_after": None,
        "posted_before": None,
        "next_token": None,
    }
    obj = ListFinancialEventsRequest(**kwargs)
    assert isinstance(obj, ListFinancialEventsRequest)


def test_listfinancialeventsresponse_instantiates():
    """Instantiate ListFinancialEventsResponse with dummy data"""
    kwargs = {
        "payload": None,
        "errors": None,
    }
    obj = ListFinancialEventsResponse(**kwargs)
    assert isinstance(obj, ListFinancialEventsResponse)


def test_loanservicingevent_instantiates():
    """Instantiate LoanServicingEvent with dummy data"""
    kwargs = {
        "loan_amount": None,
        "source_business_event_type": None,
    }
    obj = LoanServicingEvent(**kwargs)
    assert isinstance(obj, LoanServicingEvent)


def test_networkcomminglingtransactionevent_instantiates():
    """Instantiate NetworkComminglingTransactionEvent with dummy data"""
    kwargs = {
        "transaction_type": None,
        "posted_date": None,
        "net_co_transaction_i_d": None,
        "swap_reason": None,
        "a_s_i_n": None,
        "marketplace_id": None,
        "tax_exclusive_amount": None,
        "tax_amount": None,
    }
    obj = NetworkComminglingTransactionEvent(**kwargs)
    assert isinstance(obj, NetworkComminglingTransactionEvent)


def test_paywithamazonevent_instantiates():
    """Instantiate PayWithAmazonEvent with dummy data"""
    kwargs = {
        "seller_order_id": None,
        "transaction_posted_date": None,
        "business_object_type": None,
        "sales_channel": None,
        "charge": None,
        "fee_list": None,
        "payment_amount_type": None,
        "amount_description": None,
        "fulfillment_channel": None,
        "store_name": None,
    }
    obj = PayWithAmazonEvent(**kwargs)
    assert isinstance(obj, PayWithAmazonEvent)


def test_productadspaymentevent_instantiates():
    """Instantiate ProductAdsPaymentEvent with dummy data"""
    kwargs = {
        "posted_date": None,
        "transaction_type": None,
        "invoice_id": None,
        "base_value": None,
        "tax_value": None,
        "transaction_value": None,
    }
    obj = ProductAdsPaymentEvent(**kwargs)
    assert isinstance(obj, ProductAdsPaymentEvent)


def test_promotion_instantiates():
    """Instantiate Promotion with dummy data"""
    kwargs = {
        "promotion_type": None,
        "promotion_id": None,
        "promotion_amount": None,
    }
    obj = Promotion(**kwargs)
    assert isinstance(obj, Promotion)


def test_removalshipmentitemadjustment_instantiates():
    """Instantiate RemovalShipmentItemAdjustment with dummy data"""
    kwargs = {
        "removal_shipment_item_id": None,
        "tax_collection_model": None,
        "fulfillment_network_s_k_u": None,
        "adjusted_quantity": None,
        "revenue_adjustment": None,
        "tax_amount_adjustment": None,
        "tax_withheld_adjustment": None,
    }
    obj = RemovalShipmentItemAdjustment(**kwargs)
    assert isinstance(obj, RemovalShipmentItemAdjustment)


def test_removalshipmentadjustmentevent_instantiates():
    """Instantiate RemovalShipmentAdjustmentEvent with dummy data"""
    kwargs = {
        "posted_date": None,
        "adjustment_event_id": None,
        "merchant_order_id": None,
        "order_id": None,
        "transaction_type": None,
        "removal_shipment_item_adjustment_list": None,
    }
    obj = RemovalShipmentAdjustmentEvent(**kwargs)
    assert isinstance(obj, RemovalShipmentAdjustmentEvent)


def test_removalshipmentevent_instantiates():
    """Instantiate RemovalShipmentEvent with dummy data"""
    kwargs = {
        "posted_date": None,
        "merchant_order_id": None,
        "order_id": None,
        "transaction_type": None,
        "store_name": None,
        "removal_shipment_item_list": None,
    }
    obj = RemovalShipmentEvent(**kwargs)
    assert isinstance(obj, RemovalShipmentEvent)


def test_removalshipmentitem_instantiates():
    """Instantiate RemovalShipmentItem with dummy data"""
    kwargs = {
        "removal_shipment_item_id": None,
        "tax_collection_model": None,
        "fulfillment_network_s_k_u": None,
        "quantity": None,
        "revenue": None,
        "fee_amount": None,
        "tax_amount": None,
        "tax_withheld": None,
    }
    obj = RemovalShipmentItem(**kwargs)
    assert isinstance(obj, RemovalShipmentItem)


def test_rentaltransactionevent_instantiates():
    """Instantiate RentalTransactionEvent with dummy data"""
    kwargs = {
        "amazon_order_id": None,
        "rental_event_type": None,
        "extension_length": None,
        "posted_date": None,
        "rental_charge_list": None,
        "rental_fee_list": None,
        "marketplace_name": None,
        "rental_initial_value": None,
        "rental_reimbursement": None,
        "rental_tax_withheld_list": None,
    }
    obj = RentalTransactionEvent(**kwargs)
    assert isinstance(obj, RentalTransactionEvent)


def test_retrochargeevent_instantiates():
    """Instantiate RetrochargeEvent with dummy data"""
    kwargs = {
        "retrocharge_event_type": None,
        "amazon_order_id": None,
        "posted_date": None,
        "base_tax": None,
        "shipping_tax": None,
        "marketplace_name": None,
        "retrocharge_tax_withheld_list": None,
    }
    obj = RetrochargeEvent(**kwargs)
    assert isinstance(obj, RetrochargeEvent)


def test_safetreimbursementevent_instantiates():
    """Instantiate SAFETReimbursementEvent with dummy data"""
    kwargs = {
        "posted_date": None,
        "s_a_f_e_t_claim_id": None,
        "reimbursed_amount": None,
        "reason_code": None,
        "s_a_f_e_t_reimbursement_item_list": None,
    }
    obj = SAFETReimbursementEvent(**kwargs)
    assert isinstance(obj, SAFETReimbursementEvent)


def test_safetreimbursementitem_instantiates():
    """Instantiate SAFETReimbursementItem with dummy data"""
    kwargs = {
        "item_charge_list": None,
        "product_description": None,
        "quantity": None,
    }
    obj = SAFETReimbursementItem(**kwargs)
    assert isinstance(obj, SAFETReimbursementItem)


def test_sellerdealpaymentevent_instantiates():
    """Instantiate SellerDealPaymentEvent with dummy data"""
    kwargs = {
        "posted_date": None,
        "deal_id": None,
        "deal_description": None,
        "event_type": None,
        "fee_type": None,
        "fee_amount": None,
        "tax_amount": None,
        "total_amount": None,
    }
    obj = SellerDealPaymentEvent(**kwargs)
    assert isinstance(obj, SellerDealPaymentEvent)


def test_sellerreviewenrollmentpaymentevent_instantiates():
    """Instantiate SellerReviewEnrollmentPaymentEvent with dummy data"""
    kwargs = {
        "posted_date": None,
        "enrollment_id": None,
        "parent_a_s_i_n": None,
        "fee_component": None,
        "charge_component": None,
        "total_amount": None,
    }
    obj = SellerReviewEnrollmentPaymentEvent(**kwargs)
    assert isinstance(obj, SellerReviewEnrollmentPaymentEvent)


def test_servicefeeevent_instantiates():
    """Instantiate ServiceFeeEvent with dummy data"""
    kwargs = {
        "amazon_order_id": None,
        "fee_reason": None,
        "fee_list": None,
        "seller_s_k_u": None,
        "fn_s_k_u": None,
        "fee_description": None,
        "a_s_i_n": None,
        "store_name": None,
    }
    obj = ServiceFeeEvent(**kwargs)
    assert isinstance(obj, ServiceFeeEvent)


def test_shipmentevent_instantiates():
    """Instantiate ShipmentEvent with dummy data"""
    kwargs = {
        "amazon_order_id": None,
        "seller_order_id": None,
        "marketplace_name": None,
        "store_name": None,
        "order_charge_list": None,
        "order_charge_adjustment_list": None,
        "shipment_fee_list": None,
        "shipment_fee_adjustment_list": None,
        "order_fee_list": None,
        "order_fee_adjustment_list": None,
        "direct_payment_list": None,
        "posted_date": None,
        "shipment_item_list": None,
        "shipment_item_adjustment_list": None,
    }
    obj = ShipmentEvent(**kwargs)
    assert isinstance(obj, ShipmentEvent)


def test_shipmentitem_instantiates():
    """Instantiate ShipmentItem with dummy data"""
    kwargs = {
        "seller_s_k_u": None,
        "order_item_id": None,
        "order_adjustment_item_id": None,
        "quantity_shipped": None,
        "item_charge_list": None,
        "item_charge_adjustment_list": None,
        "item_fee_list": None,
        "item_fee_adjustment_list": None,
        "item_tax_withheld_list": None,
        "promotion_list": None,
        "promotion_adjustment_list": None,
        "cost_of_points_granted": None,
        "cost_of_points_returned": None,
    }
    obj = ShipmentItem(**kwargs)
    assert isinstance(obj, ShipmentItem)


def test_solutionprovidercreditevent_instantiates():
    """Instantiate SolutionProviderCreditEvent with dummy data"""
    kwargs = {
        "provider_transaction_type": None,
        "seller_order_id": None,
        "marketplace_id": None,
        "marketplace_country_code": None,
        "seller_id": None,
        "seller_store_name": None,
        "provider_id": None,
        "provider_store_name": None,
        "transaction_amount": None,
        "transaction_creation_date": None,
    }
    obj = SolutionProviderCreditEvent(**kwargs)
    assert isinstance(obj, SolutionProviderCreditEvent)


def test_tdsreimbursementevent_instantiates():
    """Instantiate TDSReimbursementEvent with dummy data"""
    kwargs = {
        "posted_date": None,
        "t_d_s_order_id": None,
        "reimbursed_amount": None,
    }
    obj = TDSReimbursementEvent(**kwargs)
    assert isinstance(obj, TDSReimbursementEvent)


def test_taxwithheldcomponent_instantiates():
    """Instantiate TaxWithheldComponent with dummy data"""
    kwargs = {
        "tax_collection_model": None,
        "taxes_withheld": None,
    }
    obj = TaxWithheldComponent(**kwargs)
    assert isinstance(obj, TaxWithheldComponent)


def test_taxwithholdingperiod_instantiates():
    """Instantiate TaxWithholdingPeriod with dummy data"""
    kwargs = {
        "start_date": None,
        "end_date": None,
    }
    obj = TaxWithholdingPeriod(**kwargs)
    assert isinstance(obj, TaxWithholdingPeriod)


def test_taxwithholdingevent_instantiates():
    """Instantiate TaxWithholdingEvent with dummy data"""
    kwargs = {
        "posted_date": None,
        "base_amount": None,
        "withheld_amount": None,
        "tax_withholding_period": None,
    }
    obj = TaxWithholdingEvent(**kwargs)
    assert isinstance(obj, TaxWithholdingEvent)


def test_trialshipmentevent_instantiates():
    """Instantiate TrialShipmentEvent with dummy data"""
    kwargs = {
        "amazon_order_id": None,
        "financial_event_group_id": None,
        "posted_date": None,
        "s_k_u": None,
        "fee_list": None,
    }
    obj = TrialShipmentEvent(**kwargs)
    assert isinstance(obj, TrialShipmentEvent)


def test_valueaddedservicechargeevent_instantiates():
    """Instantiate ValueAddedServiceChargeEvent with dummy data"""
    kwargs = {
        "transaction_type": None,
        "posted_date": None,
        "description": None,
        "transaction_amount": None,
    }
    obj = ValueAddedServiceChargeEvent(**kwargs)
    assert isinstance(obj, ValueAddedServiceChargeEvent)
