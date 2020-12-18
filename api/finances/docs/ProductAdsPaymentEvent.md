# ProductAdsPaymentEvent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**posted_date** | [**ModelDate**](ModelDate.md) |  | [optional] 
**transaction_type** | **str** | Indicates if the transaction is for a charge or a refund.  Possible values:  * charge - Charge  * refund - Refund | [optional] 
**invoice_id** | **str** | Identifier for the invoice that the transaction appears in. | [optional] 
**base_value** | [**Currency**](Currency.md) |  | [optional] 
**tax_value** | [**Currency**](Currency.md) |  | [optional] 
**transaction_value** | [**Currency**](Currency.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

