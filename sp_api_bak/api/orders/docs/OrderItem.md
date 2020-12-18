# OrderItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asin** | **str** | The Amazon Standard Identification Number (ASIN) of the item. | 
**seller_sku** | **str** | The seller stock keeping unit (SKU) of the item. | [optional] 
**order_item_id** | **str** | An Amazon-defined order item identifier. | 
**title** | **str** | The name of the item. | [optional] 
**quantity_ordered** | **int** | The number of items in the order.  | 
**quantity_shipped** | **int** | The number of items shipped. | [optional] 
**product_info** | [**ProductInfoDetail**](ProductInfoDetail.md) |  | [optional] 
**points_granted** | [**PointsGrantedDetail**](PointsGrantedDetail.md) |  | [optional] 
**item_price** | [**Money**](Money.md) |  | [optional] 
**shipping_price** | [**Money**](Money.md) |  | [optional] 
**item_tax** | [**Money**](Money.md) |  | [optional] 
**shipping_tax** | [**Money**](Money.md) |  | [optional] 
**shipping_discount** | [**Money**](Money.md) |  | [optional] 
**shipping_discount_tax** | [**Money**](Money.md) |  | [optional] 
**promotion_discount** | [**Money**](Money.md) |  | [optional] 
**promotion_discount_tax** | [**Money**](Money.md) |  | [optional] 
**promotion_ids** | [**PromotionIdList**](PromotionIdList.md) |  | [optional] 
**cod_fee** | [**Money**](Money.md) |  | [optional] 
**cod_fee_discount** | [**Money**](Money.md) |  | [optional] 
**is_gift** | **bool** | When true, the item is a gift. | [optional] 
**condition_note** | **str** | The condition of the item as described by the seller. | [optional] 
**condition_id** | **str** | The condition of the item.  Possible values: New, Used, Collectible, Refurbished, Preorder, Club. | [optional] 
**condition_subtype_id** | **str** | The subcondition of the item.  Possible values: New, Mint, Very Good, Good, Acceptable, Poor, Club, OEM, Warranty, Refurbished Warranty, Refurbished, Open Box, Any, Other. | [optional] 
**scheduled_delivery_start_date** | **str** | The start date of the scheduled delivery window in the time zone of the order destination. In ISO 8601 date time format. | [optional] 
**scheduled_delivery_end_date** | **str** | The end date of the scheduled delivery window in the time zone of the order destination. In ISO 8601 date time format. | [optional] 
**price_designation** | **str** | Indicates that the selling price is a special price that is available only for Amazon Business orders. For more information about the Amazon Business Seller Program, see the [Amazon Business website](https://www.amazon.com/b2b/info/amazon-business).   Possible values: BusinessPrice - A special price that is available only for Amazon Business orders. | [optional] 
**tax_collection** | [**TaxCollection**](TaxCollection.md) |  | [optional] 
**serial_number_required** | **bool** | When true, the product type for this item has a serial number.  Returned only for Amazon Easy Ship orders. | [optional] 
**is_transparency** | **bool** | When true, transparency codes are required. | [optional] 
**ioss_number** | **str** | The IOSS number of the seller. Sellers selling in the EU will be assigned a unique IOSS number that must be listed on all packages sent to the EU. | [optional] 
**deemed_reseller_category** | **str** | The category of deemed reseller. This applies to selling partners that are not based in the EU and is used to help them meet the VAT Deemed Reseller tax laws in the EU and UK. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

