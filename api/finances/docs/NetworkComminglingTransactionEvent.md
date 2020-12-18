# NetworkComminglingTransactionEvent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_type** | **str** | The type of network item swap.  Possible values:  * NetCo - A Fulfillment by Amazon inventory pooling transaction. Available only in the India marketplace.  * ComminglingVAT - A commingling VAT transaction. Available only in the UK, Spain, France, Germany, and Italy marketplaces. | [optional] 
**posted_date** | [**ModelDate**](ModelDate.md) |  | [optional] 
**net_co_transaction_id** | **str** | The identifier for the network item swap. | [optional] 
**swap_reason** | **str** | The reason for the network item swap. | [optional] 
**asin** | **str** | The Amazon Standard Identification Number (ASIN) of the swapped item. | [optional] 
**marketplace_id** | **str** | The marketplace in which the event took place. | [optional] 
**tax_exclusive_amount** | [**Currency**](Currency.md) |  | [optional] 
**tax_amount** | [**Currency**](Currency.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

