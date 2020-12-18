# PayWithAmazonEvent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seller_order_id** | **str** | An order identifier that is specified by the seller. | [optional] 
**transaction_posted_date** | [**ModelDate**](ModelDate.md) |  | [optional] 
**business_object_type** | **str** | The type of business object. | [optional] 
**sales_channel** | **str** | The sales channel for the transaction. | [optional] 
**charge** | [**ChargeComponent**](ChargeComponent.md) |  | [optional] 
**fee_list** | [**FeeComponentList**](FeeComponentList.md) |  | [optional] 
**payment_amount_type** | **str** | The type of payment.  Possible values:  * Sales | [optional] 
**amount_description** | **str** | A short description of this payment event. | [optional] 
**fulfillment_channel** | **str** | The fulfillment channel.  Possible values:  * AFN - Amazon Fulfillment Network (Fulfillment by Amazon)  * MFN - Merchant Fulfillment Network (self-fulfilled) | [optional] 
**store_name** | **str** | The store name where the event occurred. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

