# FinancialEventGroup

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**financial_event_group_id** | **str** | A unique identifier for the financial event group. | [optional] 
**processing_status** | **str** | The processing status of the financial event group indicates whether the balance of the financial event group is settled.  Possible values:  * Open  * Closed | [optional] 
**fund_transfer_status** | **str** | The status of the fund transfer. | [optional] 
**original_total** | [**Currency**](Currency.md) |  | [optional] 
**converted_total** | [**Currency**](Currency.md) |  | [optional] 
**fund_transfer_date** | [**ModelDate**](ModelDate.md) |  | [optional] 
**trace_id** | **str** | The trace identifier used by sellers to look up transactions externally. | [optional] 
**account_tail** | **str** | The account tail of the payment instrument. | [optional] 
**beginning_balance** | [**Currency**](Currency.md) |  | [optional] 
**financial_event_group_start** | [**ModelDate**](ModelDate.md) |  | [optional] 
**financial_event_group_end** | [**ModelDate**](ModelDate.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

