# Order

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amazon_order_id** | **str** | An Amazon-defined order identifier, in 3-7-7 format. | 
**seller_order_id** | **str** | A seller-defined order identifier. | [optional] 
**purchase_date** | **str** | The date when the order was created. | 
**last_update_date** | **str** | The date when the order was last updated.  Note: LastUpdateDate is returned with an incorrect date for orders that were last updated before 2009-04-01. | 
**order_status** | **str** | The current order status. | 
**fulfillment_channel** | **str** | Whether the order was fulfilled by Amazon (AFN) or by the seller (MFN). | [optional] 
**sales_channel** | **str** | The sales channel of the first item in the order. | [optional] 
**order_channel** | **str** | The order channel of the first item in the order. | [optional] 
**ship_service_level** | **str** | The shipment service level of the order. | [optional] 
**order_total** | [**Money**](Money.md) |  | [optional] 
**number_of_items_shipped** | **int** | The number of items shipped. | [optional] 
**number_of_items_unshipped** | **int** | The number of items unshipped. | [optional] 
**payment_execution_detail** | [**PaymentExecutionDetailItemList**](PaymentExecutionDetailItemList.md) |  | [optional] 
**payment_method** | **str** | The payment method for the order. This property is limited to Cash On Delivery (COD) and Convenience Store (CVS) payment methods. Unless you need the specific COD payment information provided by the PaymentExecutionDetailItem object, we recommend using the PaymentMethodDetails property to get payment method information. | [optional] 
**payment_method_details** | [**PaymentMethodDetailItemList**](PaymentMethodDetailItemList.md) |  | [optional] 
**marketplace_id** | **str** | The identifier for the marketplace where the order was placed. | [optional] 
**shipment_service_level_category** | **str** | The shipment service level category of the order.  Possible values: Expedited, FreeEconomy, NextDay, SameDay, SecondDay, Scheduled, Standard. | [optional] 
**easy_ship_shipment_status** | **str** | The status of the Amazon Easy Ship order. This property is included only for Amazon Easy Ship orders.  Possible values: PendingPickUp, LabelCanceled, PickedUp, OutForDelivery, Damaged, Delivered, RejectedByBuyer, Undeliverable, ReturnedToSeller, ReturningToSeller. | [optional] 
**cba_displayable_shipping_label** | **str** | Custom ship label for Checkout by Amazon (CBA). | [optional] 
**order_type** | **str** | The type of the order. | [optional] 
**earliest_ship_date** | **str** | The start of the time period within which you have committed to ship the order. In ISO 8601 date time format. Returned only for seller-fulfilled orders.  Note: EarliestShipDate might not be returned for orders placed before February 1, 2013. | [optional] 
**latest_ship_date** | **str** | The end of the time period within which you have committed to ship the order. In ISO 8601 date time format. Returned only for seller-fulfilled orders.  Note: LatestShipDate might not be returned for orders placed before February 1, 2013. | [optional] 
**earliest_delivery_date** | **str** | The start of the time period within which you have committed to fulfill the order. In ISO 8601 date time format. Returned only for seller-fulfilled orders. | [optional] 
**latest_delivery_date** | **str** | The end of the time period within which you have committed to fulfill the order. In ISO 8601 date time format. Returned only for seller-fulfilled orders that do not have a PendingAvailability, Pending, or Canceled status. | [optional] 
**is_business_order** | **bool** | When true, the order is an Amazon Business order. An Amazon Business order is an order where the buyer is a Verified Business Buyer. | [optional] 
**is_prime** | **bool** | When true, the order is a seller-fulfilled Amazon Prime order. | [optional] 
**is_premium_order** | **bool** | When true, the order has a Premium Shipping Service Level Agreement. For more information about Premium Shipping orders, see \&quot;Premium Shipping Options\&quot; in the Seller Central Help for your marketplace. | [optional] 
**is_global_express_enabled** | **bool** | When true, the order is a GlobalExpress order. | [optional] 
**replaced_order_id** | **str** | The order ID value for the order that is being replaced. Returned only if IsReplacementOrder &#x3D; true. | [optional] 
**is_replacement_order** | **bool** | When true, this is a replacement order. | [optional] 
**promise_response_due_date** | **str** | Indicates the date by which the seller must respond to the buyer with an estimated ship date. Returned only for Sourcing on Demand orders. | [optional] 
**is_estimated_ship_date_set** | **bool** | When true, the estimated ship date is set for the order. Returned only for Sourcing on Demand orders. | [optional] 
**is_sold_by_ab** | **bool** | When true, the item within this order was bought and re-sold by Amazon Business EU SARL (ABEU). By buying and instantly re-selling your items, ABEU becomes the seller of record, making your inventory available for sale to customers who would not otherwise purchase from a third-party seller. | [optional] 
**assigned_ship_from_location_address** | [**Address**](Address.md) |  | [optional] 
**fulfillment_instruction** | [**FulfillmentInstruction**](FulfillmentInstruction.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

