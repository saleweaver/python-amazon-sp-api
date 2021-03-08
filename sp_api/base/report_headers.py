"""
Enums for header row for report responses. See reportTypes.py for all available report requests.
"""

class ReportHeaders(str, Enum):
    """Headers will inherit from this class for optional type checking purposes."""
    pass

class MerchantListingsData(ReportHeaders):
    """Headers for GET_MERCHANT_LISTINGS_DATA report."""
    ITEM_NAME = 'item-name'
    LISTING_ID = 'listing-id'
    SELLER_SKU = 'seller-sku'
    PRICE = 'price'
    QUANTITY = 'quantity'
    OPEN_DATE = 'open-date'
    PRODUCT_ID_TYPE = 'product-id-type'
    ITEM_NOTE = 'item-note'
    ITEM_CONDITION = 'item-condition'
    WILL_SHIP_INTERNATIONALLY = 'will-ship-internationally'
    EXPEDITED_SHIPPING = 'expedited-shipping'
    PRODUCT_ID = 'product-id'
    PENDING_QUANTITY = 'pending-quantity'
    FULFILLMENT_CHANNEL = 'fulfillment-channel'
    BUSINESS_PRICE = 'Business Price'
    QUANTITY_PRICE_TYPE = 'Quantity Price Type'
    QUANTITY_LOWER_BOUND_1 = 'Quantity Lower Bound 1'
    QUANTITY_PRICE_1 = 'Quantity Price 1'
    QUANTITY_LOWER_BOUND_2 = 'Quantity Lower Bound 2'
    QUANTITY_PRICE_2 = 'Quantity Price 2'
    QUANTITY_LOWER_BOUND_3 = 'Quantity Lower Bound 3'
    QUANTITY_PRICE_3 = 'Quantity Price 3'
    QUANTITY_LOWER_BOUND_4 = 'Quantity Lower Bound 4'
    QUANTITY_PRICE_4 = 'Quantity Price 4'
    QUANTITY_LOWER_BOUND_5 = 'Quantity Lower Bound 5'
    QUANTITY_PRICE_5 = 'Quantity Price 5'
    MERCHANT_SHIPPING_GROUP = 'merchant-shipping-group'
    PROGRESSIVE_PRICE_TYPE = 'Progressive Price Type'
    PROGRESSIVE_LOWER_BOUND_1 = 'Progressive Lower Bound 1'
    PROGRESSIVE_PRICE_1 = 'Progressive Price 1'
    PROGRESSIVE_LOWER_BOUND_2 = 'Progressive Lower Bound 2'
    PROGRESSIVE_PRICE_2 = 'Progressive Price 2'
    PROGRESSIVE_LOWER_BOUND_3 = 'Progressive Lower Bound 3'
    PROGRESSIVE_PRICE_3 = 'Progressive Price 3'
    MINIMUM_ORDER_QUANTITY = 'Minimum order quantity'
    SELL_REMAINDER = 'Sell remainder'


class MerchantListingsAllData(ReportHeaders):
    """Headers for GET_MERCHANT_LISTINGS_ALL_DATA report."""
    ITEM_NAME = 'item-name'
    LISTING_ID = 'listing-id'
    SELLER_SKU = 'seller-sku'
    PRICE = 'price'
    QUANTITY = 'quantity'
    OPEN_DATE = 'open-date'
    PRODUCT_ID_TYPE = 'product-id-type'
    ITEM_NOTE = 'item-note'
    ITEM_CONDITION = 'item-condition'
    WILL_SHIP_INTERNATIONALLY = 'will-ship-internationally'
    EXPEDITED_SHIPPING = 'expedited-shipping'
    PRODUCT_ID = 'product-id'
    PENDING_QUANTITY = 'pending-quantity'
    FULFILLMENT_CHANNEL = 'fulfillment-channel'
    MERCHANT_SHIPPING_GROUP = 'merchant-shipping-group'
    STATUS = 'status'
    MINIMUM_ORDER_QUANTITY = 'Minimum order quantity'
    SELL_REMAINDER = 'Sell remainder'