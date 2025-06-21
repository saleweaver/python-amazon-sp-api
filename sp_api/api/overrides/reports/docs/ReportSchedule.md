# ReportSchedule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report_schedule_id** | **str** | The identifier for the report schedule. This identifier is unique only in combination with a seller ID. | 
**report_type** | **str** | The report type. | 
**marketplace_ids** | **list[str]** | A list of marketplace identifiers. The report document&#x27;s contents will contain data for all of the specified marketplaces, unless the report type indicates otherwise. | [optional] 
**report_options** | [**ReportOptions**](ReportOptions.md) |  | [optional] 
**period** | **str** | An ISO 8601 period value that indicates how often a report should be created. | 
**next_report_creation_time** | **datetime** | The date and time when the schedule will create its next report, in ISO 8601 date time format. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

