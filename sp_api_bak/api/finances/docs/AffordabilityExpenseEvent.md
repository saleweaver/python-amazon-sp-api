# AffordabilityExpenseEvent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amazon_order_id** | **str** | An Amazon-defined identifier for an order. | [optional] 
**posted_date** | [**ModelDate**](ModelDate.md) |  | [optional] 
**marketplace_id** | **str** | An encrypted, Amazon-defined marketplace identifier. | [optional] 
**transaction_type** | **str** | Indicates the type of transaction.   Possible values:  * Charge - For an affordability promotion expense.  * Refund - For an affordability promotion expense reversal. | [optional] 
**base_expense** | [**Currency**](Currency.md) |  | [optional] 
**tax_type_cgst** | [**Currency**](Currency.md) |  | 
**tax_type_sgst** | [**Currency**](Currency.md) |  | 
**tax_type_igst** | [**Currency**](Currency.md) |  | 
**total_expense** | [**Currency**](Currency.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

