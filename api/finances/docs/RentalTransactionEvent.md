# RentalTransactionEvent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amazon_order_id** | **str** | An Amazon-defined identifier for an order. | [optional] 
**rental_event_type** | **str** | The type of rental event.  Possible values:  * RentalCustomerPayment-Buyout - Transaction type that represents when the customer wants to buy out a rented item.  * RentalCustomerPayment-Extension - Transaction type that represents when the customer wants to extend the rental period.  * RentalCustomerRefund-Buyout - Transaction type that represents when the customer requests a refund for the buyout of the rented item.  * RentalCustomerRefund-Extension - Transaction type that represents when the customer requests a refund over the extension on the rented item.  * RentalHandlingFee - Transaction type that represents the fee that Amazon charges sellers who rent through Amazon.  * RentalChargeFailureReimbursement - Transaction type that represents when Amazon sends money to the seller to compensate for a failed charge.  * RentalLostItemReimbursement - Transaction type that represents when Amazon sends money to the seller to compensate for a lost item. | [optional] 
**extension_length** | **int** | The number of days that the buyer extended an already rented item. This value is only returned for RentalCustomerPayment-Extension and RentalCustomerRefund-Extension events. | [optional] 
**posted_date** | [**ModelDate**](ModelDate.md) |  | [optional] 
**rental_charge_list** | [**ChargeComponentList**](ChargeComponentList.md) |  | [optional] 
**rental_fee_list** | [**FeeComponentList**](FeeComponentList.md) |  | [optional] 
**marketplace_name** | **str** | The name of the marketplace. | [optional] 
**rental_initial_value** | [**Currency**](Currency.md) |  | [optional] 
**rental_reimbursement** | [**Currency**](Currency.md) |  | [optional] 
**rental_tax_withheld_list** | [**TaxWithheldComponentList**](TaxWithheldComponentList.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

