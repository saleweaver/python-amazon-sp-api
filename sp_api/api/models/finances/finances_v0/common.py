"""
Common models generated from Swagger/OpenAPI specification.

This file was auto-generated. Do not edit manually.

"""

from datetime import date, datetime
from enum import Enum, auto
from typing import Annotated, Any, Dict, List, Optional, Union
from uuid import UUID

from pydantic import AliasChoices, BaseModel, ConfigDict, Field

from .base_models import (BodyParam, GetRequestSerializer, PathParam,
                          QueryParam, RequestsBaseModel, SpApiBaseModel)

BigDecimal = float
"""Fields with a schema type of BigDecimal are a signed decimal number (for example CurrencyAmount)."""


"""
Currency

A currency type and amount.
"""


class Currency(SpApiBaseModel):
    """A currency type and amount."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    currency_code: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("CurrencyCode", "currency_code"),
            serialization_alias="CurrencyCode",
            description="The three-digit currency code in ISO 4217 format.",
        ),
    ]

    currency_amount: Annotated[
        Optional["BigDecimal"],
        Field(
            None,
            validation_alias=AliasChoices("CurrencyAmount", "currency_amount"),
            serialization_alias="CurrencyAmount",
            description="The monetary value.",
        ),
    ]


Date = str
"""Fields with a schema type of date are in ISO 8601 date time format (for example GroupBeginDate)."""


"""
AdhocDisbursementEvent

An event related to an Adhoc Disbursement.
"""


class AdhocDisbursementEvent(SpApiBaseModel):
    """An event related to an Adhoc Disbursement."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    transaction_type: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("TransactionType", "transaction_type"),
            serialization_alias="TransactionType",
            description="Indicates the type of transaction. Example: 'Disbursed to Amazon Gift Card balance'",
        ),
    ]

    posted_date: Annotated[
        Optional["Date"],
        Field(
            None,
            validation_alias=AliasChoices("PostedDate", "posted_date"),
            serialization_alias="PostedDate",
            description="The date and time when the financial event was posted.",
        ),
    ]

    transaction_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("TransactionId", "transaction_id"),
            serialization_alias="TransactionId",
            description="The identifier for the transaction.",
        ),
    ]

    transaction_amount: Annotated[
        Optional["Currency"],
        Field(
            None,
            validation_alias=AliasChoices("TransactionAmount", "transaction_amount"),
            serialization_alias="TransactionAmount",
            description="The amount of the transaction.",
        ),
    ]


AdhocDisbursementEventList = List["AdhocDisbursementEvent"]
"""A list of `AdhocDisbursement` events."""


AdjustmentItemList = List["AdjustmentItem"]
"""A list of information about items in an adjustment to the seller's account."""


"""
AdjustmentEvent

An adjustment to the seller's account.
"""


class AdjustmentEvent(SpApiBaseModel):
    """An adjustment to the seller's account."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    adjustment_type: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("AdjustmentType", "adjustment_type"),
            serialization_alias="AdjustmentType",
            description="The type of adjustment. Possible values: * FBAInventoryReimbursement - An FBA inventory reimbursement to a seller's account. This occurs if a seller's inventory is damaged. * ReserveEvent - A reserve event that is generated at the time of a settlement period closing. This occurs when some money from a seller's account is held back. * PostageBilling - The amount paid by a seller for shipping labels. * PostageRefund - The reimbursement of shipping labels purchased for orders that were canceled or refunded. * LostOrDamagedReimbursement - An Amazon Easy Ship reimbursement to a seller's account for a package that we lost or damaged. * CanceledButPickedUpReimbursement - An Amazon Easy Ship reimbursement to a seller's account. This occurs when a package is picked up and the order is subsequently canceled. This value is used only in the India marketplace. * ReimbursementClawback - An Amazon Easy Ship reimbursement clawback from a seller's account. This occurs when a prior reimbursement is reversed. This value is used only in the India marketplace. * SellerRewards - An award credited to a seller's account for their participation in an offer in the Seller Rewards program. Applies only to the India marketplace.",
        ),
    ]

    posted_date: Annotated[
        Optional["Date"],
        Field(
            None,
            validation_alias=AliasChoices("PostedDate", "posted_date"),
            serialization_alias="PostedDate",
            description="The date and time when the financial event was posted.",
        ),
    ]

    store_name: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("StoreName", "store_name"),
            serialization_alias="StoreName",
            description="The name of the store where the event occurred.",
        ),
    ]

    adjustment_amount: Annotated[
        Optional["Currency"],
        Field(
            None,
            validation_alias=AliasChoices("AdjustmentAmount", "adjustment_amount"),
            serialization_alias="AdjustmentAmount",
            description="The amount adjusted as part of this event.",
        ),
    ]

    adjustment_item_list: Annotated[
        Optional["AdjustmentItemList"],
        Field(
            None,
            validation_alias=AliasChoices("AdjustmentItemList", "adjustment_item_list"),
            serialization_alias="AdjustmentItemList",
            description="A list of information about adjustments to an account.",
        ),
    ]


AdjustmentEventList = List["AdjustmentEvent"]
"""A list of adjustment event information for the seller's account."""


"""
AdjustmentItem

An item in an adjustment to the seller's account.
"""


class AdjustmentItem(SpApiBaseModel):
    """An item in an adjustment to the seller's account."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    quantity: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("Quantity", "quantity"),
            serialization_alias="Quantity",
            description="Represents the number of units in the seller's inventory when the AdustmentType is FBAInventoryReimbursement.",
        ),
    ]

    per_unit_amount: Annotated[
        Optional["Currency"],
        Field(
            None,
            validation_alias=AliasChoices("PerUnitAmount", "per_unit_amount"),
            serialization_alias="PerUnitAmount",
            description="The per unit value of the item.",
        ),
    ]

    total_amount: Annotated[
        Optional["Currency"],
        Field(
            None,
            validation_alias=AliasChoices("TotalAmount", "total_amount"),
            serialization_alias="TotalAmount",
            description="The total value of the item.",
        ),
    ]

    seller_s_k_u: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("SellerSKU", "seller_s_k_u"),
            serialization_alias="SellerSKU",
            description="The seller SKU of the item. The seller SKU is qualified by the seller's seller ID, which is included with every call to the Selling Partner API.",
        ),
    ]

    fn_s_k_u: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("FnSKU", "fn_s_k_u"),
            serialization_alias="FnSKU",
            description="A unique identifier assigned to products stored in and fulfilled from a fulfillment center.",
        ),
    ]

    product_description: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("ProductDescription", "product_description"),
            serialization_alias="ProductDescription",
            description="A short description of the item.",
        ),
    ]

    a_s_i_n: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("ASIN", "a_s_i_n"),
            serialization_alias="ASIN",
            description="The Amazon Standard Identification Number (ASIN) of the item.",
        ),
    ]

    transaction_number: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("TransactionNumber", "transaction_number"),
            serialization_alias="TransactionNumber",
            description="The transaction number that is related to the adjustment.",
        ),
    ]


"""
AffordabilityExpenseEvent

An expense related to an affordability promotion.
"""


class AffordabilityExpenseEvent(SpApiBaseModel):
    """An expense related to an affordability promotion."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    amazon_order_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("AmazonOrderId", "amazon_order_id"),
            serialization_alias="AmazonOrderId",
            description="An Amazon-defined identifier for an order.",
        ),
    ]

    posted_date: Annotated[
        Optional["Date"],
        Field(
            None,
            validation_alias=AliasChoices("PostedDate", "posted_date"),
            serialization_alias="PostedDate",
            description="The date and time when the financial event was created.",
        ),
    ]

    marketplace_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("MarketplaceId", "marketplace_id"),
            serialization_alias="MarketplaceId",
            description="An encrypted, Amazon-defined marketplace identifier.",
        ),
    ]

    transaction_type: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("TransactionType", "transaction_type"),
            serialization_alias="TransactionType",
            description="Indicates the type of transaction. Possible values: * Charge - For an affordability promotion expense. * Refund - For an affordability promotion expense reversal.",
        ),
    ]

    base_expense: Annotated[
        Optional["Currency"],
        Field(
            None,
            validation_alias=AliasChoices("BaseExpense", "base_expense"),
            serialization_alias="BaseExpense",
            description="The amount charged for clicks incurred under the Sponsored Products program.",
        ),
    ]

    tax_type_c_g_s_t: Annotated[
        "Currency",
        Field(
            ...,
            validation_alias=AliasChoices("TaxTypeCGST", "tax_type_c_g_s_t"),
            serialization_alias="TaxTypeCGST",
            description="Central Goods and Service Tax, charged and collected by the central government.",
        ),
    ]

    tax_type_s_g_s_t: Annotated[
        "Currency",
        Field(
            ...,
            validation_alias=AliasChoices("TaxTypeSGST", "tax_type_s_g_s_t"),
            serialization_alias="TaxTypeSGST",
            description="State Goods and Service Tax, charged and collected by the state government.",
        ),
    ]

    tax_type_i_g_s_t: Annotated[
        "Currency",
        Field(
            ...,
            validation_alias=AliasChoices("TaxTypeIGST", "tax_type_i_g_s_t"),
            serialization_alias="TaxTypeIGST",
            description="Integrated Goods and Service Tax, charged and collected by the central government.",
        ),
    ]

    total_expense: Annotated[
        Optional["Currency"],
        Field(
            None,
            validation_alias=AliasChoices("TotalExpense", "total_expense"),
            serialization_alias="TotalExpense",
            description="The total amount charged to the seller. TotalExpense = BaseExpense + TaxTypeIGST + TaxTypeCGST + TaxTypeSGST.",
        ),
    ]


AffordabilityExpenseEventList = List["AffordabilityExpenseEvent"]
"""A list of expense information related to an affordability promotion."""


"""
CapacityReservationBillingEvent

An event related to a capacity reservation billing charge.
"""


class CapacityReservationBillingEvent(SpApiBaseModel):
    """An event related to a capacity reservation billing charge."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    transaction_type: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("TransactionType", "transaction_type"),
            serialization_alias="TransactionType",
            description="Indicates the type of transaction. For example, FBA Inventory Fee",
        ),
    ]

    posted_date: Annotated[
        Optional["Date"],
        Field(
            None,
            validation_alias=AliasChoices("PostedDate", "posted_date"),
            serialization_alias="PostedDate",
            description="The date and time when the financial event was posted.",
        ),
    ]

    description: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("Description", "description"),
            serialization_alias="Description",
            description="A short description of the capacity reservation billing event.",
        ),
    ]

    transaction_amount: Annotated[
        Optional["Currency"],
        Field(
            None,
            validation_alias=AliasChoices("TransactionAmount", "transaction_amount"),
            serialization_alias="TransactionAmount",
            description="The amount of the capacity reservation billing event.",
        ),
    ]


CapacityReservationBillingEventList = List["CapacityReservationBillingEvent"]
"""A list of `CapacityReservationBillingEvent` events."""


"""
ChargeComponent

A charge on the seller's account. Possible values: * Principal - The selling price of the order item, equal to the selling price of the item multiplied by the quantity ordered. * Tax - The tax collected by the seller on the Principal. * MarketplaceFacilitatorTax-Principal - The tax withheld on the Principal. * MarketplaceFacilitatorTax-Shipping - The tax withheld on the ShippingCharge. * MarketplaceFacilitatorTax-Giftwrap - The tax withheld on the Giftwrap charge. * MarketplaceFacilitatorTax-Other - The tax withheld on other miscellaneous charges. * Discount - The promotional discount for an order item. * TaxDiscount - The tax amount deducted for promotional rebates. * CODItemCharge - The COD charge for an order item. * CODItemTaxCharge - The tax collected by the seller on a CODItemCharge. * CODOrderCharge - The COD charge for an order. * CODOrderTaxCharge - The tax collected by the seller on a CODOrderCharge. * CODShippingCharge - Shipping charges for a COD order. * CODShippingTaxCharge - The tax collected by the seller on a CODShippingCharge. * ShippingCharge - The shipping charge. * ShippingTax - The tax collected by the seller on a ShippingCharge. * Goodwill - The amount given to a buyer as a gesture of goodwill or to compensate for pain and suffering in the buying experience. * Giftwrap - The gift wrap charge. * GiftwrapTax - The tax collected by the seller on a Giftwrap charge. * RestockingFee - The charge applied to the buyer when returning a product in certain categories. * ReturnShipping - The amount given to the buyer to compensate for shipping the item back in the event we are at fault. * PointsFee - The value of Amazon Points deducted from the refund if the buyer does not have enough Amazon Points to cover the deduction. * GenericDeduction - A generic bad debt deduction. * FreeReplacementReturnShipping - The compensation for return shipping when a buyer receives the wrong item, requests a free replacement, and returns the incorrect item. * PaymentMethodFee - The fee collected for certain payment methods in certain marketplaces. * ExportCharge - The export duty that is charged when an item is shipped to an international destination as part of the Amazon Global program. * SAFE-TReimbursement - The SAFE-T claim amount for the item. * TCS-CGST - Tax Collected at Source (TCS) for Central Goods and Services Tax (CGST). * TCS-SGST - Tax Collected at Source for State Goods and Services Tax (SGST). * TCS-IGST - Tax Collected at Source for Integrated Goods and Services Tax (IGST). * TCS-UTGST - Tax Collected at Source for Union Territories Goods and Services Tax (UTGST).
"""


class ChargeComponent(SpApiBaseModel):
    """A charge on the seller's account. Possible values: * Principal - The selling price of the order item, equal to the selling price of the item multiplied by the quantity ordered. * Tax - The tax collected by the seller on the Principal. * MarketplaceFacilitatorTax-Principal - The tax withheld on the Principal. * MarketplaceFacilitatorTax-Shipping - The tax withheld on the ShippingCharge. * MarketplaceFacilitatorTax-Giftwrap - The tax withheld on the Giftwrap charge. * MarketplaceFacilitatorTax-Other - The tax withheld on other miscellaneous charges. * Discount - The promotional discount for an order item. * TaxDiscount - The tax amount deducted for promotional rebates. * CODItemCharge - The COD charge for an order item. * CODItemTaxCharge - The tax collected by the seller on a CODItemCharge. * CODOrderCharge - The COD charge for an order. * CODOrderTaxCharge - The tax collected by the seller on a CODOrderCharge. * CODShippingCharge - Shipping charges for a COD order. * CODShippingTaxCharge - The tax collected by the seller on a CODShippingCharge. * ShippingCharge - The shipping charge. * ShippingTax - The tax collected by the seller on a ShippingCharge. * Goodwill - The amount given to a buyer as a gesture of goodwill or to compensate for pain and suffering in the buying experience. * Giftwrap - The gift wrap charge. * GiftwrapTax - The tax collected by the seller on a Giftwrap charge. * RestockingFee - The charge applied to the buyer when returning a product in certain categories. * ReturnShipping - The amount given to the buyer to compensate for shipping the item back in the event we are at fault. * PointsFee - The value of Amazon Points deducted from the refund if the buyer does not have enough Amazon Points to cover the deduction. * GenericDeduction - A generic bad debt deduction. * FreeReplacementReturnShipping - The compensation for return shipping when a buyer receives the wrong item, requests a free replacement, and returns the incorrect item. * PaymentMethodFee - The fee collected for certain payment methods in certain marketplaces. * ExportCharge - The export duty that is charged when an item is shipped to an international destination as part of the Amazon Global program. * SAFE-TReimbursement - The SAFE-T claim amount for the item. * TCS-CGST - Tax Collected at Source (TCS) for Central Goods and Services Tax (CGST). * TCS-SGST - Tax Collected at Source for State Goods and Services Tax (SGST). * TCS-IGST - Tax Collected at Source for Integrated Goods and Services Tax (IGST). * TCS-UTGST - Tax Collected at Source for Union Territories Goods and Services Tax (UTGST)."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    charge_type: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("ChargeType", "charge_type"),
            serialization_alias="ChargeType",
            description="The type of charge.",
        ),
    ]

    charge_amount: Annotated[
        Optional["Currency"],
        Field(
            None,
            validation_alias=AliasChoices("ChargeAmount", "charge_amount"),
            serialization_alias="ChargeAmount",
            description="The amount of the charge.",
        ),
    ]


ChargeComponentList = List["ChargeComponent"]
"""A list of charge information on the seller's account."""


"""
ChargeInstrument

A payment instrument.
"""


class ChargeInstrument(SpApiBaseModel):
    """A payment instrument."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    description: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("Description", "description"),
            serialization_alias="Description",
            description="A short description of the charge instrument.",
        ),
    ]

    tail: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("Tail", "tail"),
            serialization_alias="Tail",
            description="The account tail (trailing digits) of the charge instrument.",
        ),
    ]

    amount: Annotated[
        Optional["Currency"],
        Field(
            None,
            validation_alias=AliasChoices("Amount", "amount"),
            serialization_alias="Amount",
            description="The amount charged to this charge instrument.",
        ),
    ]


ChargeInstrumentList = List["ChargeInstrument"]
"""A list of payment instruments."""


ChargeRefundTransactions = List["ChargeRefundTransaction"]
"""A list of `ChargeRefund` transactions"""


"""
ChargeRefundEvent

An event related to charge refund.
"""


class ChargeRefundEvent(SpApiBaseModel):
    """An event related to charge refund."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    posted_date: Annotated[
        Optional["Date"],
        Field(
            None,
            validation_alias=AliasChoices("PostedDate", "posted_date"),
            serialization_alias="PostedDate",
            description="The date and time when the financial event was posted.",
        ),
    ]

    reason_code: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("ReasonCode", "reason_code"),
            serialization_alias="ReasonCode",
            description="The reason given for a charge refund. Example: `SubscriptionFeeCorrection`",
        ),
    ]

    reason_code_description: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "ReasonCodeDescription", "reason_code_description"
            ),
            serialization_alias="ReasonCodeDescription",
            description="A description of the Reason Code. Example: `SubscriptionFeeCorrection`",
        ),
    ]

    charge_refund_transactions: Annotated[
        Optional["ChargeRefundTransactions"],
        Field(
            None,
            validation_alias=AliasChoices(
                "ChargeRefundTransactions", "charge_refund_transactions"
            ),
            serialization_alias="ChargeRefundTransactions",
            description="The amount of the charge refund credit.",
        ),
    ]


ChargeRefundEventList = List["ChargeRefundEvent"]
"""A list of charge refund events."""


"""
ChargeRefundTransaction

The charge refund transaction.
"""


class ChargeRefundTransaction(SpApiBaseModel):
    """The charge refund transaction."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    charge_amount: Annotated[
        Optional["Currency"],
        Field(
            None,
            validation_alias=AliasChoices("ChargeAmount", "charge_amount"),
            serialization_alias="ChargeAmount",
            description="The amount of the charge refund credit.",
        ),
    ]

    charge_type: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("ChargeType", "charge_type"),
            serialization_alias="ChargeType",
            description="The type of charge.",
        ),
    ]


"""
FeeComponent

A fee associated with the event.
"""


class FeeComponent(SpApiBaseModel):
    """A fee associated with the event."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    fee_type: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("FeeType", "fee_type"),
            serialization_alias="FeeType",
            description="The type of fee. For more information about Selling on Amazon fees, see [Selling on Amazon Fee Schedule](https://sellercentral.amazon.com/gp/help/200336920) on Seller Central. For more information about Fulfillment by Amazon fees, see [FBA features, services and fees](https://sellercentral.amazon.com/gp/help/201074400) on Seller Central.",
        ),
    ]

    fee_amount: Annotated[
        Optional["Currency"],
        Field(
            None,
            validation_alias=AliasChoices("FeeAmount", "fee_amount"),
            serialization_alias="FeeAmount",
            description="The amount of the fee.",
        ),
    ]


"""
CouponPaymentEvent

An event related to coupon payments.
"""


class CouponPaymentEvent(SpApiBaseModel):
    """An event related to coupon payments."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    posted_date: Annotated[
        Optional["Date"],
        Field(
            None,
            validation_alias=AliasChoices("PostedDate", "posted_date"),
            serialization_alias="PostedDate",
            description="The date and time when the financial event was posted.",
        ),
    ]

    coupon_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("CouponId", "coupon_id"),
            serialization_alias="CouponId",
            description="A coupon identifier.",
        ),
    ]

    seller_coupon_description: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "SellerCouponDescription", "seller_coupon_description"
            ),
            serialization_alias="SellerCouponDescription",
            description="The description provided by the seller when they created the coupon.",
        ),
    ]

    clip_or_redemption_count: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices(
                "ClipOrRedemptionCount", "clip_or_redemption_count"
            ),
            serialization_alias="ClipOrRedemptionCount",
            description="The number of coupon clips or redemptions.",
        ),
    ]

    payment_event_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("PaymentEventId", "payment_event_id"),
            serialization_alias="PaymentEventId",
            description="A payment event identifier.",
        ),
    ]

    fee_component: Annotated[
        Optional["FeeComponent"],
        Field(
            None,
            validation_alias=AliasChoices("FeeComponent", "fee_component"),
            serialization_alias="FeeComponent",
        ),
    ]

    charge_component: Annotated[
        Optional["ChargeComponent"],
        Field(
            None,
            validation_alias=AliasChoices("ChargeComponent", "charge_component"),
            serialization_alias="ChargeComponent",
        ),
    ]

    total_amount: Annotated[
        Optional["Currency"],
        Field(
            None,
            validation_alias=AliasChoices("TotalAmount", "total_amount"),
            serialization_alias="TotalAmount",
            description="The FeeComponent value plus the ChargeComponent value.",
        ),
    ]


CouponPaymentEventList = List["CouponPaymentEvent"]
"""A list of coupon payment event information."""


DebtRecoveryItemList = List["DebtRecoveryItem"]
"""A list of debt recovery item information."""


"""
DebtRecoveryEvent

A debt payment or debt adjustment.
"""


class DebtRecoveryEvent(SpApiBaseModel):
    """A debt payment or debt adjustment."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    debt_recovery_type: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("DebtRecoveryType", "debt_recovery_type"),
            serialization_alias="DebtRecoveryType",
            description="The debt recovery type. Possible values: * DebtPayment * DebtPaymentFailure * DebtAdjustment",
        ),
    ]

    recovery_amount: Annotated[
        Optional["Currency"],
        Field(
            None,
            validation_alias=AliasChoices("RecoveryAmount", "recovery_amount"),
            serialization_alias="RecoveryAmount",
            description="The amount applied for recovery.",
        ),
    ]

    over_payment_credit: Annotated[
        Optional["Currency"],
        Field(
            None,
            validation_alias=AliasChoices("OverPaymentCredit", "over_payment_credit"),
            serialization_alias="OverPaymentCredit",
            description="The amount returned for overpayment.",
        ),
    ]

    debt_recovery_item_list: Annotated[
        Optional["DebtRecoveryItemList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "DebtRecoveryItemList", "debt_recovery_item_list"
            ),
            serialization_alias="DebtRecoveryItemList",
        ),
    ]

    charge_instrument_list: Annotated[
        Optional["ChargeInstrumentList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "ChargeInstrumentList", "charge_instrument_list"
            ),
            serialization_alias="ChargeInstrumentList",
        ),
    ]


DebtRecoveryEventList = List["DebtRecoveryEvent"]
"""A list of debt recovery event information."""


"""
DebtRecoveryItem

An item of a debt payment or debt adjustment.
"""


class DebtRecoveryItem(SpApiBaseModel):
    """An item of a debt payment or debt adjustment."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    recovery_amount: Annotated[
        Optional["Currency"],
        Field(
            None,
            validation_alias=AliasChoices("RecoveryAmount", "recovery_amount"),
            serialization_alias="RecoveryAmount",
            description="The amount applied for the recovery item.",
        ),
    ]

    original_amount: Annotated[
        Optional["Currency"],
        Field(
            None,
            validation_alias=AliasChoices("OriginalAmount", "original_amount"),
            serialization_alias="OriginalAmount",
            description="The original debt amount.",
        ),
    ]

    group_begin_date: Annotated[
        Optional["Date"],
        Field(
            None,
            validation_alias=AliasChoices("GroupBeginDate", "group_begin_date"),
            serialization_alias="GroupBeginDate",
            description="The beginning date and time of the financial event group that contains the debt. In [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date time format.",
        ),
    ]

    group_end_date: Annotated[
        Optional["Date"],
        Field(
            None,
            validation_alias=AliasChoices("GroupEndDate", "group_end_date"),
            serialization_alias="GroupEndDate",
            description="The ending date and time of the financial event group that contains the debt. In [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date time format.",
        ),
    ]


"""
DirectPayment

A payment made directly to a seller.
"""


class DirectPayment(SpApiBaseModel):
    """A payment made directly to a seller."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    direct_payment_type: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("DirectPaymentType", "direct_payment_type"),
            serialization_alias="DirectPaymentType",
            description="The type of payment. Possible values: * StoredValueCardRevenue - The amount that is deducted from the seller's account because the seller received money through a stored value card. * StoredValueCardRefund - The amount that Amazon returns to the seller if the order that is bought using a stored value card is refunded. * PrivateLabelCreditCardRevenue - The amount that is deducted from the seller's account because the seller received money through a private label credit card offered by Amazon. * PrivateLabelCreditCardRefund - The amount that Amazon returns to the seller if the order that is bought using a private label credit card offered by Amazon is refunded. * CollectOnDeliveryRevenue - The COD amount that the seller collected directly from the buyer. * CollectOnDeliveryRefund - The amount that Amazon refunds to the buyer if an order paid for by COD is refunded.",
        ),
    ]

    direct_payment_amount: Annotated[
        Optional["Currency"],
        Field(
            None,
            validation_alias=AliasChoices(
                "DirectPaymentAmount", "direct_payment_amount"
            ),
            serialization_alias="DirectPaymentAmount",
            description="The amount of the direct payment.",
        ),
    ]


DirectPaymentList = List["DirectPayment"]
"""A list of direct payment information."""


"""
Error

Error response returned when the request is unsuccessful.
"""


class Error(SpApiBaseModel):
    """Error response returned when the request is unsuccessful."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    code: Annotated[
        str,
        Field(
            ...,
            description="An error code that identifies the type of error that occurred.",
        ),
    ]

    message: Annotated[
        str,
        Field(
            ...,
            description="A message that describes the error condition in a human-readable form.",
        ),
    ]

    details: Annotated[
        Optional[str],
        Field(
            None,
            description="Additional details that can help the caller understand or fix the issue.",
        ),
    ]


ErrorList = List["Error"]
"""A list of error responses returned when a request is unsuccessful."""


"""
FBALiquidationEvent

A payment event for Fulfillment by Amazon (FBA) inventory liquidation. This event is used only in the US marketplace.
"""


class FBALiquidationEvent(SpApiBaseModel):
    """A payment event for Fulfillment by Amazon (FBA) inventory liquidation. This event is used only in the US marketplace."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    posted_date: Annotated[
        Optional["Date"],
        Field(
            None,
            validation_alias=AliasChoices("PostedDate", "posted_date"),
            serialization_alias="PostedDate",
            description="The date and time when the financial event was posted.",
        ),
    ]

    original_removal_order_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "OriginalRemovalOrderId", "original_removal_order_id"
            ),
            serialization_alias="OriginalRemovalOrderId",
            description="The identifier for the original removal order.",
        ),
    ]

    liquidation_proceeds_amount: Annotated[
        Optional["Currency"],
        Field(
            None,
            validation_alias=AliasChoices(
                "LiquidationProceedsAmount", "liquidation_proceeds_amount"
            ),
            serialization_alias="LiquidationProceedsAmount",
            description="The amount paid by the liquidator for the seller's inventory. The seller receives this amount minus LiquidationFeeAmount.",
        ),
    ]

    liquidation_fee_amount: Annotated[
        Optional["Currency"],
        Field(
            None,
            validation_alias=AliasChoices(
                "LiquidationFeeAmount", "liquidation_fee_amount"
            ),
            serialization_alias="LiquidationFeeAmount",
            description="The fee charged to the seller by Amazon for liquidating the seller's FBA inventory.",
        ),
    ]


FBALiquidationEventList = List["FBALiquidationEvent"]
"""A list of FBA inventory liquidation payment events."""


"""
FailedAdhocDisbursementEvent

Failed ad hoc disbursement event list.
"""


class FailedAdhocDisbursementEvent(SpApiBaseModel):
    """Failed ad hoc disbursement event list."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    funds_transfers_type: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("FundsTransfersType", "funds_transfers_type"),
            serialization_alias="FundsTransfersType",
            description="The type of fund transfer. Example 'Refund'",
        ),
    ]

    transfer_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("TransferId", "transfer_id"),
            serialization_alias="TransferId",
            description="The transfer identifier.",
        ),
    ]

    disbursement_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("DisbursementId", "disbursement_id"),
            serialization_alias="DisbursementId",
            description="The disbursement identifier.",
        ),
    ]

    payment_disbursement_type: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "PaymentDisbursementType", "payment_disbursement_type"
            ),
            serialization_alias="PaymentDisbursementType",
            description="The type of payment for disbursement. Example `CREDIT_CARD`",
        ),
    ]

    status: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("Status", "status"),
            serialization_alias="Status",
            description="The status of the failed `AdhocDisbursement`. Example `HARD_DECLINED`",
        ),
    ]

    transfer_amount: Annotated[
        Optional["Currency"],
        Field(
            None,
            validation_alias=AliasChoices("TransferAmount", "transfer_amount"),
            serialization_alias="TransferAmount",
            description="The amount of the Adhoc Disbursement.",
        ),
    ]

    posted_date: Annotated[
        Optional["Date"],
        Field(
            None,
            validation_alias=AliasChoices("PostedDate", "posted_date"),
            serialization_alias="PostedDate",
            description="The date and time when the financial event was posted.",
        ),
    ]


FailedAdhocDisbursementEventList = List["FailedAdhocDisbursementEvent"]
"""A list of `FailedAdhocDisbursementEvent`s."""


FeeComponentList = List["FeeComponent"]
"""A list of fee component information."""


"""
FinancialEventGroup

Information related to a financial event group.
"""


class FinancialEventGroup(SpApiBaseModel):
    """Information related to a financial event group."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    financial_event_group_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "FinancialEventGroupId", "financial_event_group_id"
            ),
            serialization_alias="FinancialEventGroupId",
            description="A unique identifier for the financial event group.",
        ),
    ]

    processing_status: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("ProcessingStatus", "processing_status"),
            serialization_alias="ProcessingStatus",
            description="The processing status of the financial event group indicates whether the balance of the financial event group is settled. Possible values: * Open * Closed",
        ),
    ]

    fund_transfer_status: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("FundTransferStatus", "fund_transfer_status"),
            serialization_alias="FundTransferStatus",
            description="The status of the fund transfer.",
        ),
    ]

    original_total: Annotated[
        Optional["Currency"],
        Field(
            None,
            validation_alias=AliasChoices("OriginalTotal", "original_total"),
            serialization_alias="OriginalTotal",
            description="The total amount in the currency of the marketplace in which the transactions occurred. For a closed financial group, this is the total amount of a disbursement or a charge amount. For an open financial event group, this is the current balance.",
        ),
    ]

    converted_total: Annotated[
        Optional["Currency"],
        Field(
            None,
            validation_alias=AliasChoices("ConvertedTotal", "converted_total"),
            serialization_alias="ConvertedTotal",
            description="The total amount in the currency of the marketplace in which the funds were disbursed.",
        ),
    ]

    fund_transfer_date: Annotated[
        Optional["Date"],
        Field(
            None,
            validation_alias=AliasChoices("FundTransferDate", "fund_transfer_date"),
            serialization_alias="FundTransferDate",
            description="The date and time when the disbursement or charge was initiated. Only present for closed settlements. In [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date time format.",
        ),
    ]

    trace_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("TraceId", "trace_id"),
            serialization_alias="TraceId",
            description="The trace identifier used by sellers to look up transactions externally.",
        ),
    ]

    account_tail: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("AccountTail", "account_tail"),
            serialization_alias="AccountTail",
            description="The account tail of the payment instrument.",
        ),
    ]

    beginning_balance: Annotated[
        Optional["Currency"],
        Field(
            None,
            validation_alias=AliasChoices("BeginningBalance", "beginning_balance"),
            serialization_alias="BeginningBalance",
            description="The balance at the beginning of the settlement period.",
        ),
    ]

    financial_event_group_start: Annotated[
        Optional["Date"],
        Field(
            None,
            validation_alias=AliasChoices(
                "FinancialEventGroupStart", "financial_event_group_start"
            ),
            serialization_alias="FinancialEventGroupStart",
            description="The date and time at which the financial event group is opened. In [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date time format.",
        ),
    ]

    financial_event_group_end: Annotated[
        Optional["Date"],
        Field(
            None,
            validation_alias=AliasChoices(
                "FinancialEventGroupEnd", "financial_event_group_end"
            ),
            serialization_alias="FinancialEventGroupEnd",
            description="The date and time at which the financial event group is closed. In [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date time format.",
        ),
    ]


FinancialEventGroupList = List["FinancialEventGroup"]
"""A list of financial event group information."""


ImagingServicesFeeEventList = List["ImagingServicesFeeEvent"]
"""A list of fee events related to Amazon Imaging services."""


LoanServicingEventList = List["LoanServicingEvent"]
"""A list of loan servicing events."""


NetworkComminglingTransactionEventList = List["NetworkComminglingTransactionEvent"]
"""A list of network commingling transaction events."""


PayWithAmazonEventList = List["PayWithAmazonEvent"]
"""A list of events related to the seller's Pay with Amazon account."""


ProductAdsPaymentEventList = List["ProductAdsPaymentEvent"]
"""A list of sponsored products payment events."""


RemovalShipmentAdjustmentEventList = List["RemovalShipmentAdjustmentEvent"]
"""A comma-delimited list of Removal shipmentAdjustment details for FBA inventory."""


RemovalShipmentEventList = List["RemovalShipmentEvent"]
"""A list of removal shipment event information."""


RentalTransactionEventList = List["RentalTransactionEvent"]
"""A list of rental transaction event information."""


RetrochargeEventList = List["RetrochargeEvent"]
"""A list of information about Retrocharge or RetrochargeReversal events."""


SAFETReimbursementEventList = List["SAFETReimbursementEvent"]
"""A list of SAFETReimbursementEvents."""


SellerDealPaymentEventList = List["SellerDealPaymentEvent"]
"""A list of payment events for deal-related fees."""


SellerReviewEnrollmentPaymentEventList = List["SellerReviewEnrollmentPaymentEvent"]
"""A list of information about fee events for the Early Reviewer Program."""


ServiceFeeEventList = List["ServiceFeeEvent"]
"""A list of information about service fee events."""


ShipmentEventList = List["ShipmentEvent"]
"""A list of shipment event information."""


ShipmentSettleEventList = List["ShipmentEvent"]
"""A list of `ShipmentEvent` items."""


SolutionProviderCreditEventList = List["SolutionProviderCreditEvent"]
"""A list of information about solution provider credits."""


TDSReimbursementEventList = List["TDSReimbursementEvent"]
"""A list of `TDSReimbursementEvent` items."""


TaxWithholdingEventList = List["TaxWithholdingEvent"]
"""A list of `TaxWithholding` events."""


TrialShipmentEventList = List["TrialShipmentEvent"]
"""A list of information about trial shipment financial events."""


ValueAddedServiceChargeEventList = List["ValueAddedServiceChargeEvent"]
"""A list of `ValueAddedServiceCharge` events."""


"""
FinancialEvents

Contains all information related to a financial event.
"""


class FinancialEvents(SpApiBaseModel):
    """Contains all information related to a financial event."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    shipment_event_list: Annotated[
        Optional["ShipmentEventList"],
        Field(
            None,
            validation_alias=AliasChoices("ShipmentEventList", "shipment_event_list"),
            serialization_alias="ShipmentEventList",
            description="A list of shipment events.",
        ),
    ]

    shipment_settle_event_list: Annotated[
        Optional["ShipmentSettleEventList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "ShipmentSettleEventList", "shipment_settle_event_list"
            ),
            serialization_alias="ShipmentSettleEventList",
            description="A list of Shipment Settle events.",
        ),
    ]

    refund_event_list: Annotated[
        Optional["ShipmentEventList"],
        Field(
            None,
            validation_alias=AliasChoices("RefundEventList", "refund_event_list"),
            serialization_alias="RefundEventList",
            description="A list of refund events.",
        ),
    ]

    guarantee_claim_event_list: Annotated[
        Optional["ShipmentEventList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "GuaranteeClaimEventList", "guarantee_claim_event_list"
            ),
            serialization_alias="GuaranteeClaimEventList",
            description="A list of guarantee claim events.",
        ),
    ]

    chargeback_event_list: Annotated[
        Optional["ShipmentEventList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "ChargebackEventList", "chargeback_event_list"
            ),
            serialization_alias="ChargebackEventList",
            description="A list of chargeback events.",
        ),
    ]

    pay_with_amazon_event_list: Annotated[
        Optional["PayWithAmazonEventList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "PayWithAmazonEventList", "pay_with_amazon_event_list"
            ),
            serialization_alias="PayWithAmazonEventList",
        ),
    ]

    service_provider_credit_event_list: Annotated[
        Optional["SolutionProviderCreditEventList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "ServiceProviderCreditEventList", "service_provider_credit_event_list"
            ),
            serialization_alias="ServiceProviderCreditEventList",
        ),
    ]

    retrocharge_event_list: Annotated[
        Optional["RetrochargeEventList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "RetrochargeEventList", "retrocharge_event_list"
            ),
            serialization_alias="RetrochargeEventList",
        ),
    ]

    rental_transaction_event_list: Annotated[
        Optional["RentalTransactionEventList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "RentalTransactionEventList", "rental_transaction_event_list"
            ),
            serialization_alias="RentalTransactionEventList",
        ),
    ]

    product_ads_payment_event_list: Annotated[
        Optional["ProductAdsPaymentEventList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "ProductAdsPaymentEventList", "product_ads_payment_event_list"
            ),
            serialization_alias="ProductAdsPaymentEventList",
        ),
    ]

    service_fee_event_list: Annotated[
        Optional["ServiceFeeEventList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "ServiceFeeEventList", "service_fee_event_list"
            ),
            serialization_alias="ServiceFeeEventList",
        ),
    ]

    seller_deal_payment_event_list: Annotated[
        Optional["SellerDealPaymentEventList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "SellerDealPaymentEventList", "seller_deal_payment_event_list"
            ),
            serialization_alias="SellerDealPaymentEventList",
        ),
    ]

    debt_recovery_event_list: Annotated[
        Optional["DebtRecoveryEventList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "DebtRecoveryEventList", "debt_recovery_event_list"
            ),
            serialization_alias="DebtRecoveryEventList",
        ),
    ]

    loan_servicing_event_list: Annotated[
        Optional["LoanServicingEventList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "LoanServicingEventList", "loan_servicing_event_list"
            ),
            serialization_alias="LoanServicingEventList",
        ),
    ]

    adjustment_event_list: Annotated[
        Optional["AdjustmentEventList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "AdjustmentEventList", "adjustment_event_list"
            ),
            serialization_alias="AdjustmentEventList",
        ),
    ]

    s_a_f_e_t_reimbursement_event_list: Annotated[
        Optional["SAFETReimbursementEventList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "SAFETReimbursementEventList", "s_a_f_e_t_reimbursement_event_list"
            ),
            serialization_alias="SAFETReimbursementEventList",
        ),
    ]

    seller_review_enrollment_payment_event_list: Annotated[
        Optional["SellerReviewEnrollmentPaymentEventList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "SellerReviewEnrollmentPaymentEventList",
                "seller_review_enrollment_payment_event_list",
            ),
            serialization_alias="SellerReviewEnrollmentPaymentEventList",
        ),
    ]

    f_b_a_liquidation_event_list: Annotated[
        Optional["FBALiquidationEventList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "FBALiquidationEventList", "f_b_a_liquidation_event_list"
            ),
            serialization_alias="FBALiquidationEventList",
        ),
    ]

    coupon_payment_event_list: Annotated[
        Optional["CouponPaymentEventList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "CouponPaymentEventList", "coupon_payment_event_list"
            ),
            serialization_alias="CouponPaymentEventList",
        ),
    ]

    imaging_services_fee_event_list: Annotated[
        Optional["ImagingServicesFeeEventList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "ImagingServicesFeeEventList", "imaging_services_fee_event_list"
            ),
            serialization_alias="ImagingServicesFeeEventList",
        ),
    ]

    network_commingling_transaction_event_list: Annotated[
        Optional["NetworkComminglingTransactionEventList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "NetworkComminglingTransactionEventList",
                "network_commingling_transaction_event_list",
            ),
            serialization_alias="NetworkComminglingTransactionEventList",
        ),
    ]

    affordability_expense_event_list: Annotated[
        Optional["AffordabilityExpenseEventList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "AffordabilityExpenseEventList", "affordability_expense_event_list"
            ),
            serialization_alias="AffordabilityExpenseEventList",
        ),
    ]

    affordability_expense_reversal_event_list: Annotated[
        Optional["AffordabilityExpenseEventList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "AffordabilityExpenseReversalEventList",
                "affordability_expense_reversal_event_list",
            ),
            serialization_alias="AffordabilityExpenseReversalEventList",
        ),
    ]

    removal_shipment_event_list: Annotated[
        Optional["RemovalShipmentEventList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "RemovalShipmentEventList", "removal_shipment_event_list"
            ),
            serialization_alias="RemovalShipmentEventList",
        ),
    ]

    removal_shipment_adjustment_event_list: Annotated[
        Optional["RemovalShipmentAdjustmentEventList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "RemovalShipmentAdjustmentEventList",
                "removal_shipment_adjustment_event_list",
            ),
            serialization_alias="RemovalShipmentAdjustmentEventList",
        ),
    ]

    trial_shipment_event_list: Annotated[
        Optional["TrialShipmentEventList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "TrialShipmentEventList", "trial_shipment_event_list"
            ),
            serialization_alias="TrialShipmentEventList",
        ),
    ]

    t_d_s_reimbursement_event_list: Annotated[
        Optional["TDSReimbursementEventList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "TDSReimbursementEventList", "t_d_s_reimbursement_event_list"
            ),
            serialization_alias="TDSReimbursementEventList",
        ),
    ]

    adhoc_disbursement_event_list: Annotated[
        Optional["AdhocDisbursementEventList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "AdhocDisbursementEventList", "adhoc_disbursement_event_list"
            ),
            serialization_alias="AdhocDisbursementEventList",
        ),
    ]

    tax_withholding_event_list: Annotated[
        Optional["TaxWithholdingEventList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "TaxWithholdingEventList", "tax_withholding_event_list"
            ),
            serialization_alias="TaxWithholdingEventList",
        ),
    ]

    charge_refund_event_list: Annotated[
        Optional["ChargeRefundEventList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "ChargeRefundEventList", "charge_refund_event_list"
            ),
            serialization_alias="ChargeRefundEventList",
        ),
    ]

    failed_adhoc_disbursement_event_list: Annotated[
        Optional["FailedAdhocDisbursementEventList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "FailedAdhocDisbursementEventList",
                "failed_adhoc_disbursement_event_list",
            ),
            serialization_alias="FailedAdhocDisbursementEventList",
        ),
    ]

    value_added_service_charge_event_list: Annotated[
        Optional["ValueAddedServiceChargeEventList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "ValueAddedServiceChargeEventList",
                "value_added_service_charge_event_list",
            ),
            serialization_alias="ValueAddedServiceChargeEventList",
        ),
    ]

    capacity_reservation_billing_event_list: Annotated[
        Optional["CapacityReservationBillingEventList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "CapacityReservationBillingEventList",
                "capacity_reservation_billing_event_list",
            ),
            serialization_alias="CapacityReservationBillingEventList",
        ),
    ]


"""
ImagingServicesFeeEvent

A fee event related to Amazon Imaging services.
"""


class ImagingServicesFeeEvent(SpApiBaseModel):
    """A fee event related to Amazon Imaging services."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    imaging_request_billing_item_i_d: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "ImagingRequestBillingItemID", "imaging_request_billing_item_i_d"
            ),
            serialization_alias="ImagingRequestBillingItemID",
            description="The identifier for the imaging services request.",
        ),
    ]

    a_s_i_n: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("ASIN", "a_s_i_n"),
            serialization_alias="ASIN",
            description="The Amazon Standard Identification Number (ASIN) of the item for which the imaging service was requested.",
        ),
    ]

    posted_date: Annotated[
        Optional["Date"],
        Field(
            None,
            validation_alias=AliasChoices("PostedDate", "posted_date"),
            serialization_alias="PostedDate",
            description="The date and time when the financial event was posted.",
        ),
    ]

    fee_list: Annotated[
        Optional["FeeComponentList"],
        Field(
            None,
            validation_alias=AliasChoices("FeeList", "fee_list"),
            serialization_alias="FeeList",
            description="A list of fees associated with the event.",
        ),
    ]


"""
ListFinancialEventGroupsPayload

The payload for the listFinancialEventGroups operation.
"""


class ListFinancialEventGroupsPayload(SpApiBaseModel):
    """The payload for the listFinancialEventGroups operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    next_token: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("NextToken", "next_token"),
            serialization_alias="NextToken",
            description="When present and not empty, pass this string token in the next request to return the next response page.",
        ),
    ]

    financial_event_group_list: Annotated[
        Optional["FinancialEventGroupList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "FinancialEventGroupList", "financial_event_group_list"
            ),
            serialization_alias="FinancialEventGroupList",
        ),
    ]


"""
ListFinancialEventGroupsRequest

Request parameters for listFinancialEventGroups
"""


class ListFinancialEventGroupsRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for listFinancialEventGroups
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    max_results_per_page: Annotated[
        Optional[int],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("MaxResultsPerPage", "max_results_per_page"),
            serialization_alias="MaxResultsPerPage",
            description="[QUERY] The maximum number of results to return per page. If the response exceeds the maximum number of transactions or 10 MB, the API responds with 'InvalidInput'.",
        ),
    ]

    financial_event_group_started_before: Annotated[
        Optional[datetime],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices(
                "FinancialEventGroupStartedBefore",
                "financial_event_group_started_before",
            ),
            serialization_alias="FinancialEventGroupStartedBefore",
            description="[QUERY] A date used for selecting financial event groups that opened before (but not at) a specified date and time, in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) format. The date-time  must be later than FinancialEventGroupStartedAfter and no later than two minutes before the request was submitted. If FinancialEventGroupStartedAfter and FinancialEventGroupStartedBefore are more than 180 days apart, no financial event groups are returned.",
        ),
    ]

    financial_event_group_started_after: Annotated[
        Optional[datetime],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices(
                "FinancialEventGroupStartedAfter", "financial_event_group_started_after"
            ),
            serialization_alias="FinancialEventGroupStartedAfter",
            description="[QUERY] A date used for selecting financial event groups that opened after (or at) a specified date and time, in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) format. The date-time must be no later than two minutes before the request was submitted.",
        ),
    ]

    next_token: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("NextToken", "next_token"),
            serialization_alias="NextToken",
            description="[QUERY] A string token returned in the response of your previous request.",
        ),
    ]


"""
ListFinancialEventGroupsResponse

The response schema for the listFinancialEventGroups operation.
"""


class ListFinancialEventGroupsResponse(SpApiBaseModel):
    """The response schema for the listFinancialEventGroups operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["ListFinancialEventGroupsPayload"],
        Field(
            None, description="The payload for the listFinancialEventGroups operation."
        ),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
            description="One or more unexpected errors occurred during the listFinancialEventGroups operation.",
        ),
    ]


"""
ListFinancialEventsByGroupIdRequest

Request parameters for listFinancialEventsByGroupId
"""


class ListFinancialEventsByGroupIdRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for listFinancialEventsByGroupId
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    max_results_per_page: Annotated[
        Optional[int],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("MaxResultsPerPage", "max_results_per_page"),
            serialization_alias="MaxResultsPerPage",
            description="[QUERY] The maximum number of results to return per page. If the response exceeds the maximum number of transactions or 10 MB, the API responds with 'InvalidInput'.",
        ),
    ]

    posted_after: Annotated[
        Optional[datetime],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("PostedAfter", "posted_after"),
            serialization_alias="PostedAfter",
            description="[QUERY] A date used for selecting financial events posted after (or at) a specified time. The date-time **must** be more than two minutes before the time of the request, in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date time format.",
        ),
    ]

    posted_before: Annotated[
        Optional[datetime],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("PostedBefore", "posted_before"),
            serialization_alias="PostedBefore",
            description="[QUERY] A date used for selecting financial events posted before (but not at) a specified time. The date-time must be later than `PostedAfter` and no later than two minutes before the request was submitted, in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date time format. If `PostedAfter` and `PostedBefore` are more than 180 days apart, no financial events are returned. You must specify the `PostedAfter` parameter if you specify the `PostedBefore` parameter. Default: Now minus two minutes.",
        ),
    ]

    event_group_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("eventGroupId", "event_group_id"),
            serialization_alias="eventGroupId",
            description="[PATH] The identifier of the financial event group to which the events belong.",
        ),
    ]

    next_token: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("NextToken", "next_token"),
            serialization_alias="NextToken",
            description="[QUERY] A string token returned in the response of your previous request.",
        ),
    ]


"""
ListFinancialEventsByOrderIdRequest

Request parameters for listFinancialEventsByOrderId
"""


class ListFinancialEventsByOrderIdRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for listFinancialEventsByOrderId
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    order_id: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices("orderId", "order_id"),
            serialization_alias="orderId",
            description="[PATH] An Amazon-defined order identifier, in 3-7-7 format.",
        ),
    ]

    max_results_per_page: Annotated[
        Optional[int],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("MaxResultsPerPage", "max_results_per_page"),
            serialization_alias="MaxResultsPerPage",
            description="[QUERY] The maximum number of results to return per page. If the response exceeds the maximum number of transactions or 10 MB, the API responds with 'InvalidInput'.",
        ),
    ]

    next_token: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("NextToken", "next_token"),
            serialization_alias="NextToken",
            description="[QUERY] A string token returned in the response of your previous request.",
        ),
    ]


"""
ListFinancialEventsPayload

The payload for the listFinancialEvents operation.
"""


class ListFinancialEventsPayload(SpApiBaseModel):
    """The payload for the listFinancialEvents operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    next_token: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("NextToken", "next_token"),
            serialization_alias="NextToken",
            description="When present and not empty, pass this string token in the next request to return the next response page.",
        ),
    ]

    financial_events: Annotated[
        Optional["FinancialEvents"],
        Field(
            None,
            validation_alias=AliasChoices("FinancialEvents", "financial_events"),
            serialization_alias="FinancialEvents",
        ),
    ]


"""
ListFinancialEventsRequest

Request parameters for listFinancialEvents
"""


class ListFinancialEventsRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for listFinancialEvents
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    max_results_per_page: Annotated[
        Optional[int],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("MaxResultsPerPage", "max_results_per_page"),
            serialization_alias="MaxResultsPerPage",
            description="[QUERY] The maximum number of results to return per page. If the response exceeds the maximum number of transactions or 10 MB, the API responds with 'InvalidInput'.",
        ),
    ]

    posted_after: Annotated[
        Optional[datetime],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("PostedAfter", "posted_after"),
            serialization_alias="PostedAfter",
            description="[QUERY] A date used for selecting financial events posted after (or at) a specified time. The date-time must be no later than two minutes before the request was submitted, in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date time format.",
        ),
    ]

    posted_before: Annotated[
        Optional[datetime],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("PostedBefore", "posted_before"),
            serialization_alias="PostedBefore",
            description="[QUERY] A date used for selecting financial events posted before (but not at) a specified time. The date-time must be later than PostedAfter and no later than two minutes before the request was submitted, in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date time format. If PostedAfter and PostedBefore are more than 180 days apart, no financial events are returned. You must specify the PostedAfter parameter if you specify the PostedBefore parameter. Default: Now minus two minutes.",
        ),
    ]

    next_token: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("NextToken", "next_token"),
            serialization_alias="NextToken",
            description="[QUERY] A string token returned in the response of your previous request.",
        ),
    ]


"""
ListFinancialEventsResponse

The response schema for the listFinancialEvents operation.
"""


class ListFinancialEventsResponse(SpApiBaseModel):
    """The response schema for the listFinancialEvents operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["ListFinancialEventsPayload"],
        Field(None, description="The payload for the listFinancialEvents operation."),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
            description="One or more unexpected errors occurred during the listFinancialEvents operation.",
        ),
    ]


"""
LoanServicingEvent

A loan advance, loan payment, or loan refund.
"""


class LoanServicingEvent(SpApiBaseModel):
    """A loan advance, loan payment, or loan refund."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    loan_amount: Annotated[
        Optional["Currency"],
        Field(
            None,
            validation_alias=AliasChoices("LoanAmount", "loan_amount"),
            serialization_alias="LoanAmount",
            description="The amount of the loan.",
        ),
    ]

    source_business_event_type: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "SourceBusinessEventType", "source_business_event_type"
            ),
            serialization_alias="SourceBusinessEventType",
            description="The type of event. Possible values: * LoanAdvance * LoanPayment * LoanRefund",
        ),
    ]


"""
NetworkComminglingTransactionEvent

A network commingling transaction event.
"""


class NetworkComminglingTransactionEvent(SpApiBaseModel):
    """A network commingling transaction event."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    transaction_type: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("TransactionType", "transaction_type"),
            serialization_alias="TransactionType",
            description="The type of network item swap. Possible values: * NetCo - A Fulfillment by Amazon inventory pooling transaction. Available only in the India marketplace. * ComminglingVAT - A commingling VAT transaction. Available only in the UK, Spain, France, Germany, and Italy marketplaces.",
        ),
    ]

    posted_date: Annotated[
        Optional["Date"],
        Field(
            None,
            validation_alias=AliasChoices("PostedDate", "posted_date"),
            serialization_alias="PostedDate",
            description="The date and time when the financial event was posted.",
        ),
    ]

    net_co_transaction_i_d: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "NetCoTransactionID", "net_co_transaction_i_d"
            ),
            serialization_alias="NetCoTransactionID",
            description="The identifier for the network item swap.",
        ),
    ]

    swap_reason: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("SwapReason", "swap_reason"),
            serialization_alias="SwapReason",
            description="The reason for the network item swap.",
        ),
    ]

    a_s_i_n: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("ASIN", "a_s_i_n"),
            serialization_alias="ASIN",
            description="The Amazon Standard Identification Number (ASIN) of the swapped item.",
        ),
    ]

    marketplace_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("MarketplaceId", "marketplace_id"),
            serialization_alias="MarketplaceId",
            description="The marketplace in which the event took place.",
        ),
    ]

    tax_exclusive_amount: Annotated[
        Optional["Currency"],
        Field(
            None,
            validation_alias=AliasChoices("TaxExclusiveAmount", "tax_exclusive_amount"),
            serialization_alias="TaxExclusiveAmount",
            description="The price of the swapped item minus TaxAmount.",
        ),
    ]

    tax_amount: Annotated[
        Optional["Currency"],
        Field(
            None,
            validation_alias=AliasChoices("TaxAmount", "tax_amount"),
            serialization_alias="TaxAmount",
            description="The tax on the network item swap paid by the seller.",
        ),
    ]


"""
PayWithAmazonEvent

An event related to the seller's Pay with Amazon account.
"""


class PayWithAmazonEvent(SpApiBaseModel):
    """An event related to the seller's Pay with Amazon account."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    seller_order_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("SellerOrderId", "seller_order_id"),
            serialization_alias="SellerOrderId",
            description="An order identifier that is specified by the seller.",
        ),
    ]

    transaction_posted_date: Annotated[
        Optional["Date"],
        Field(
            None,
            validation_alias=AliasChoices(
                "TransactionPostedDate", "transaction_posted_date"
            ),
            serialization_alias="TransactionPostedDate",
            description="The date and time when the payment transaction is posted. In [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date time format.",
        ),
    ]

    business_object_type: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("BusinessObjectType", "business_object_type"),
            serialization_alias="BusinessObjectType",
            description="The type of business object.",
        ),
    ]

    sales_channel: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("SalesChannel", "sales_channel"),
            serialization_alias="SalesChannel",
            description="The sales channel for the transaction.",
        ),
    ]

    charge: Annotated[
        Optional["ChargeComponent"],
        Field(
            None,
            validation_alias=AliasChoices("Charge", "charge"),
            serialization_alias="Charge",
            description="The charge associated with the event.",
        ),
    ]

    fee_list: Annotated[
        Optional["FeeComponentList"],
        Field(
            None,
            validation_alias=AliasChoices("FeeList", "fee_list"),
            serialization_alias="FeeList",
            description="A list of fees associated with the event.",
        ),
    ]

    payment_amount_type: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("PaymentAmountType", "payment_amount_type"),
            serialization_alias="PaymentAmountType",
            description="The type of payment. Possible values: * Sales",
        ),
    ]

    amount_description: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("AmountDescription", "amount_description"),
            serialization_alias="AmountDescription",
            description="A short description of this payment event.",
        ),
    ]

    fulfillment_channel: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("FulfillmentChannel", "fulfillment_channel"),
            serialization_alias="FulfillmentChannel",
            description="The fulfillment channel. Possible values: * AFN - Amazon Fulfillment Network (Fulfillment by Amazon) * MFN - Merchant Fulfillment Network (self-fulfilled)",
        ),
    ]

    store_name: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("StoreName", "store_name"),
            serialization_alias="StoreName",
            description="The store name where the event occurred.",
        ),
    ]


"""
ProductAdsPaymentEvent

A Sponsored Products payment event.
"""


class ProductAdsPaymentEvent(SpApiBaseModel):
    """A Sponsored Products payment event."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    posted_date: Annotated[
        Optional["Date"],
        Field(
            None,
            validation_alias=AliasChoices("postedDate", "posted_date"),
            serialization_alias="postedDate",
            description="The date and time when the financial event was posted.",
        ),
    ]

    transaction_type: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("transactionType", "transaction_type"),
            serialization_alias="transactionType",
            description="Indicates if the transaction is for a charge or a refund. Possible values: * charge - Charge * refund - Refund",
        ),
    ]

    invoice_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("invoiceId", "invoice_id"),
            serialization_alias="invoiceId",
            description="Identifier for the invoice that the transaction appears in.",
        ),
    ]

    base_value: Annotated[
        Optional["Currency"],
        Field(
            None,
            validation_alias=AliasChoices("baseValue", "base_value"),
            serialization_alias="baseValue",
            description="Base amount of the transaction, before tax.",
        ),
    ]

    tax_value: Annotated[
        Optional["Currency"],
        Field(
            None,
            validation_alias=AliasChoices("taxValue", "tax_value"),
            serialization_alias="taxValue",
            description="Tax amount of the transaction.",
        ),
    ]

    transaction_value: Annotated[
        Optional["Currency"],
        Field(
            None,
            validation_alias=AliasChoices("transactionValue", "transaction_value"),
            serialization_alias="transactionValue",
            description="The total amount of the transaction. Equal to baseValue + taxValue.",
        ),
    ]


"""
Promotion

A promotion applied to an item.
"""


class Promotion(SpApiBaseModel):
    """A promotion applied to an item."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    promotion_type: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("PromotionType", "promotion_type"),
            serialization_alias="PromotionType",
            description="The type of promotion.",
        ),
    ]

    promotion_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("PromotionId", "promotion_id"),
            serialization_alias="PromotionId",
            description="The seller-specified identifier for the promotion.",
        ),
    ]

    promotion_amount: Annotated[
        Optional["Currency"],
        Field(
            None,
            validation_alias=AliasChoices("PromotionAmount", "promotion_amount"),
            serialization_alias="PromotionAmount",
            description="The amount of promotional discount applied to the item.",
        ),
    ]


PromotionList = List["Promotion"]
"""A list of promotions."""


"""
RemovalShipmentItemAdjustment

Item-level information for a removal shipment item adjustment.
"""


class RemovalShipmentItemAdjustment(SpApiBaseModel):
    """Item-level information for a removal shipment item adjustment."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    removal_shipment_item_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "RemovalShipmentItemId", "removal_shipment_item_id"
            ),
            serialization_alias="RemovalShipmentItemId",
            description="An identifier for an item in a removal shipment.",
        ),
    ]

    tax_collection_model: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("TaxCollectionModel", "tax_collection_model"),
            serialization_alias="TaxCollectionModel",
            description="The tax collection model applied to the item. Possible values: * MarketplaceFacilitator - Tax is withheld and remitted to the taxing authority by Amazon on behalf of the seller. * Standard - Tax is paid to the seller and not remitted to the taxing authority by Amazon.",
        ),
    ]

    fulfillment_network_s_k_u: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "FulfillmentNetworkSKU", "fulfillment_network_s_k_u"
            ),
            serialization_alias="FulfillmentNetworkSKU",
            description="The Amazon fulfillment network SKU for the item.",
        ),
    ]

    adjusted_quantity: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices("AdjustedQuantity", "adjusted_quantity"),
            serialization_alias="AdjustedQuantity",
            description="Adjusted quantity of removal shipmentItemAdjustment items.",
        ),
    ]

    revenue_adjustment: Annotated[
        Optional["Currency"],
        Field(
            None,
            validation_alias=AliasChoices("RevenueAdjustment", "revenue_adjustment"),
            serialization_alias="RevenueAdjustment",
            description="The total amount adjusted for disputed items.",
        ),
    ]

    tax_amount_adjustment: Annotated[
        Optional["Currency"],
        Field(
            None,
            validation_alias=AliasChoices(
                "TaxAmountAdjustment", "tax_amount_adjustment"
            ),
            serialization_alias="TaxAmountAdjustment",
            description="Adjustment on the Tax collected amount on the adjusted revenue.",
        ),
    ]

    tax_withheld_adjustment: Annotated[
        Optional["Currency"],
        Field(
            None,
            validation_alias=AliasChoices(
                "TaxWithheldAdjustment", "tax_withheld_adjustment"
            ),
            serialization_alias="TaxWithheldAdjustment",
            description="Adjustment the tax withheld and remitted to the taxing authority by Amazon on behalf of the seller. If TaxCollectionModel=MarketplaceFacilitator, then TaxWithheld=TaxAmount (except the TaxWithheld amount is a negative number). Otherwise TaxWithheld=0.",
        ),
    ]


"""
RemovalShipmentAdjustmentEvent

A financial adjustment event for FBA liquidated inventory. A positive value indicates money owed to Amazon by the buyer (for example, when the charge was incorrectly calculated as less than it should be). A negative value indicates a full or partial refund owed to the buyer (for example, when the buyer receives damaged items or fewer items than ordered).
"""


class RemovalShipmentAdjustmentEvent(SpApiBaseModel):
    """A financial adjustment event for FBA liquidated inventory. A positive value indicates money owed to Amazon by the buyer (for example, when the charge was incorrectly calculated as less than it should be). A negative value indicates a full or partial refund owed to the buyer (for example, when the buyer receives damaged items or fewer items than ordered)."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    posted_date: Annotated[
        Optional["Date"],
        Field(
            None,
            validation_alias=AliasChoices("PostedDate", "posted_date"),
            serialization_alias="PostedDate",
            description="The date when the financial event was posted.",
        ),
    ]

    adjustment_event_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("AdjustmentEventId", "adjustment_event_id"),
            serialization_alias="AdjustmentEventId",
            description="The unique identifier for the adjustment event.",
        ),
    ]

    merchant_order_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("MerchantOrderId", "merchant_order_id"),
            serialization_alias="MerchantOrderId",
            description="The merchant removal orderId.",
        ),
    ]

    order_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("OrderId", "order_id"),
            serialization_alias="OrderId",
            description="The orderId for shipping inventory.",
        ),
    ]

    transaction_type: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("TransactionType", "transaction_type"),
            serialization_alias="TransactionType",
            description="The type of removal order. Possible values: * WHOLESALE_LIQUIDATION.",
        ),
    ]

    removal_shipment_item_adjustment_list: Annotated[
        Optional[List["RemovalShipmentItemAdjustment"]],
        Field(
            None,
            validation_alias=AliasChoices(
                "RemovalShipmentItemAdjustmentList",
                "removal_shipment_item_adjustment_list",
            ),
            serialization_alias="RemovalShipmentItemAdjustmentList",
            description="A comma-delimited list of Removal shipmentItemAdjustment details for FBA inventory.",
        ),
    ]


RemovalShipmentItemList = List["RemovalShipmentItem"]
"""A list of information about removal shipment items."""


"""
RemovalShipmentEvent

A removal shipment event for a removal order.
"""


class RemovalShipmentEvent(SpApiBaseModel):
    """A removal shipment event for a removal order."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    posted_date: Annotated[
        Optional["Date"],
        Field(
            None,
            validation_alias=AliasChoices("PostedDate", "posted_date"),
            serialization_alias="PostedDate",
            description="The date and time when the financial event was posted.",
        ),
    ]

    merchant_order_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("MerchantOrderId", "merchant_order_id"),
            serialization_alias="MerchantOrderId",
            description="The merchant removal orderId.",
        ),
    ]

    order_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("OrderId", "order_id"),
            serialization_alias="OrderId",
            description="The identifier for the removal shipment order.",
        ),
    ]

    transaction_type: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("TransactionType", "transaction_type"),
            serialization_alias="TransactionType",
            description="The type of removal order. Possible values: * WHOLESALE_LIQUIDATION",
        ),
    ]

    store_name: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("StoreName", "store_name"),
            serialization_alias="StoreName",
            description="The name of the store where the event occurred.",
        ),
    ]

    removal_shipment_item_list: Annotated[
        Optional["RemovalShipmentItemList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "RemovalShipmentItemList", "removal_shipment_item_list"
            ),
            serialization_alias="RemovalShipmentItemList",
            description="A list of removal shipment items.",
        ),
    ]


"""
RemovalShipmentItem

Item-level information for a removal shipment.
"""


class RemovalShipmentItem(SpApiBaseModel):
    """Item-level information for a removal shipment."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    removal_shipment_item_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "RemovalShipmentItemId", "removal_shipment_item_id"
            ),
            serialization_alias="RemovalShipmentItemId",
            description="An identifier for an item in a removal shipment.",
        ),
    ]

    tax_collection_model: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("TaxCollectionModel", "tax_collection_model"),
            serialization_alias="TaxCollectionModel",
            description="The tax collection model applied to the item. Possible values: * MarketplaceFacilitator - Tax is withheld and remitted to the taxing authority by Amazon on behalf of the seller. * Standard - Tax is paid to the seller and not remitted to the taxing authority by Amazon.",
        ),
    ]

    fulfillment_network_s_k_u: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "FulfillmentNetworkSKU", "fulfillment_network_s_k_u"
            ),
            serialization_alias="FulfillmentNetworkSKU",
            description="The Amazon fulfillment network SKU for the item.",
        ),
    ]

    quantity: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices("Quantity", "quantity"),
            serialization_alias="Quantity",
            description="The quantity of the item.",
        ),
    ]

    revenue: Annotated[
        Optional["Currency"],
        Field(
            None,
            validation_alias=AliasChoices("Revenue", "revenue"),
            serialization_alias="Revenue",
            description="The total amount paid to the seller for the removed item.",
        ),
    ]

    fee_amount: Annotated[
        Optional["Currency"],
        Field(
            None,
            validation_alias=AliasChoices("FeeAmount", "fee_amount"),
            serialization_alias="FeeAmount",
            description="The fee that Amazon charged to the seller for the removal of the item. The amount is a negative number.",
        ),
    ]

    tax_amount: Annotated[
        Optional["Currency"],
        Field(
            None,
            validation_alias=AliasChoices("TaxAmount", "tax_amount"),
            serialization_alias="TaxAmount",
            description="Tax collected on the revenue.",
        ),
    ]

    tax_withheld: Annotated[
        Optional["Currency"],
        Field(
            None,
            validation_alias=AliasChoices("TaxWithheld", "tax_withheld"),
            serialization_alias="TaxWithheld",
            description="The tax withheld and remitted to the taxing authority by Amazon on behalf of the seller. If TaxCollectionModel=MarketplaceFacilitator, then TaxWithheld=TaxAmount (except the TaxWithheld amount is a negative number). Otherwise TaxWithheld=0.",
        ),
    ]


TaxWithheldComponentList = List["TaxWithheldComponent"]
"""A list of information about taxes withheld."""


"""
RentalTransactionEvent

An event related to a rental transaction.
"""


class RentalTransactionEvent(SpApiBaseModel):
    """An event related to a rental transaction."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    amazon_order_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("AmazonOrderId", "amazon_order_id"),
            serialization_alias="AmazonOrderId",
            description="An Amazon-defined identifier for an order.",
        ),
    ]

    rental_event_type: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("RentalEventType", "rental_event_type"),
            serialization_alias="RentalEventType",
            description="The type of rental event. Possible values: * RentalCustomerPayment-Buyout - Transaction type that represents when the customer wants to buy out a rented item. * RentalCustomerPayment-Extension - Transaction type that represents when the customer wants to extend the rental period. * RentalCustomerRefund-Buyout - Transaction type that represents when the customer requests a refund for the buyout of the rented item. * RentalCustomerRefund-Extension - Transaction type that represents when the customer requests a refund over the extension on the rented item. * RentalHandlingFee - Transaction type that represents the fee that Amazon charges sellers who rent through Amazon. * RentalChargeFailureReimbursement - Transaction type that represents when Amazon sends money to the seller to compensate for a failed charge. * RentalLostItemReimbursement - Transaction type that represents when Amazon sends money to the seller to compensate for a lost item.",
        ),
    ]

    extension_length: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices("ExtensionLength", "extension_length"),
            serialization_alias="ExtensionLength",
            description="The number of days that the buyer extended an already rented item. This value is only returned for RentalCustomerPayment-Extension and RentalCustomerRefund-Extension events.",
        ),
    ]

    posted_date: Annotated[
        Optional["Date"],
        Field(
            None,
            validation_alias=AliasChoices("PostedDate", "posted_date"),
            serialization_alias="PostedDate",
            description="The date and time when the financial event was posted.",
        ),
    ]

    rental_charge_list: Annotated[
        Optional["ChargeComponentList"],
        Field(
            None,
            validation_alias=AliasChoices("RentalChargeList", "rental_charge_list"),
            serialization_alias="RentalChargeList",
            description="A list of charges associated with the rental event.",
        ),
    ]

    rental_fee_list: Annotated[
        Optional["FeeComponentList"],
        Field(
            None,
            validation_alias=AliasChoices("RentalFeeList", "rental_fee_list"),
            serialization_alias="RentalFeeList",
            description="A list of fees associated with the rental event.",
        ),
    ]

    marketplace_name: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("MarketplaceName", "marketplace_name"),
            serialization_alias="MarketplaceName",
            description="The name of the marketplace.",
        ),
    ]

    rental_initial_value: Annotated[
        Optional["Currency"],
        Field(
            None,
            validation_alias=AliasChoices("RentalInitialValue", "rental_initial_value"),
            serialization_alias="RentalInitialValue",
            description="The amount of money the customer originally paid to rent the item. This value is only returned for RentalChargeFailureReimbursement and RentalLostItemReimbursement events.",
        ),
    ]

    rental_reimbursement: Annotated[
        Optional["Currency"],
        Field(
            None,
            validation_alias=AliasChoices(
                "RentalReimbursement", "rental_reimbursement"
            ),
            serialization_alias="RentalReimbursement",
            description="The amount of money Amazon sends the seller to compensate for a lost item or a failed charge. This value is only returned for RentalChargeFailureReimbursement and RentalLostItemReimbursement events.",
        ),
    ]

    rental_tax_withheld_list: Annotated[
        Optional["TaxWithheldComponentList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "RentalTaxWithheldList", "rental_tax_withheld_list"
            ),
            serialization_alias="RentalTaxWithheldList",
            description="A list of taxes withheld information for a rental item.",
        ),
    ]


"""
RetrochargeEvent

A retrocharge or retrocharge reversal.
"""


class RetrochargeEvent(SpApiBaseModel):
    """A retrocharge or retrocharge reversal."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    retrocharge_event_type: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "RetrochargeEventType", "retrocharge_event_type"
            ),
            serialization_alias="RetrochargeEventType",
            description="The type of event. Possible values: * Retrocharge * RetrochargeReversal",
        ),
    ]

    amazon_order_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("AmazonOrderId", "amazon_order_id"),
            serialization_alias="AmazonOrderId",
            description="An Amazon-defined identifier for an order.",
        ),
    ]

    posted_date: Annotated[
        Optional["Date"],
        Field(
            None,
            validation_alias=AliasChoices("PostedDate", "posted_date"),
            serialization_alias="PostedDate",
            description="The date and time when the financial event was posted.",
        ),
    ]

    base_tax: Annotated[
        Optional["Currency"],
        Field(
            None,
            validation_alias=AliasChoices("BaseTax", "base_tax"),
            serialization_alias="BaseTax",
            description="The base tax associated with the retrocharge event.",
        ),
    ]

    shipping_tax: Annotated[
        Optional["Currency"],
        Field(
            None,
            validation_alias=AliasChoices("ShippingTax", "shipping_tax"),
            serialization_alias="ShippingTax",
            description="The shipping tax associated with the retrocharge event.",
        ),
    ]

    marketplace_name: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("MarketplaceName", "marketplace_name"),
            serialization_alias="MarketplaceName",
            description="The name of the marketplace where the retrocharge event occurred.",
        ),
    ]

    retrocharge_tax_withheld_list: Annotated[
        Optional["TaxWithheldComponentList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "RetrochargeTaxWithheldList", "retrocharge_tax_withheld_list"
            ),
            serialization_alias="RetrochargeTaxWithheldList",
            description="A list of information about taxes withheld.",
        ),
    ]


SAFETReimbursementItemList = List["SAFETReimbursementItem"]
"""A list of SAFETReimbursementItems."""


"""
SAFETReimbursementEvent

A SAFE-T claim reimbursement on the seller's account.
"""


class SAFETReimbursementEvent(SpApiBaseModel):
    """A SAFE-T claim reimbursement on the seller's account."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    posted_date: Annotated[
        Optional["Date"],
        Field(
            None,
            validation_alias=AliasChoices("PostedDate", "posted_date"),
            serialization_alias="PostedDate",
            description="The date and time when the financial event was posted.",
        ),
    ]

    s_a_f_e_t_claim_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("SAFETClaimId", "s_a_f_e_t_claim_id"),
            serialization_alias="SAFETClaimId",
            description="A SAFE-T claim identifier.",
        ),
    ]

    reimbursed_amount: Annotated[
        Optional["Currency"],
        Field(
            None,
            validation_alias=AliasChoices("ReimbursedAmount", "reimbursed_amount"),
            serialization_alias="ReimbursedAmount",
            description="The amount of the reimbursement.",
        ),
    ]

    reason_code: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("ReasonCode", "reason_code"),
            serialization_alias="ReasonCode",
            description="Indicates why the seller was reimbursed.",
        ),
    ]

    s_a_f_e_t_reimbursement_item_list: Annotated[
        Optional["SAFETReimbursementItemList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "SAFETReimbursementItemList", "s_a_f_e_t_reimbursement_item_list"
            ),
            serialization_alias="SAFETReimbursementItemList",
        ),
    ]


"""
SAFETReimbursementItem

An item from a SAFE-T claim reimbursement.
"""


class SAFETReimbursementItem(SpApiBaseModel):
    """An item from a SAFE-T claim reimbursement."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    item_charge_list: Annotated[
        Optional["ChargeComponentList"],
        Field(
            None,
            validation_alias=AliasChoices("itemChargeList", "item_charge_list"),
            serialization_alias="itemChargeList",
            description="A list of charges associated with the item.",
        ),
    ]

    product_description: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("productDescription", "product_description"),
            serialization_alias="productDescription",
            description="The description of the item as shown on the product detail page on the retail website.",
        ),
    ]

    quantity: Annotated[
        Optional[str],
        Field(None, description="The number of units of the item being reimbursed."),
    ]


"""
SellerDealPaymentEvent

An event linked to the payment of a fee related to the specified deal.
"""


class SellerDealPaymentEvent(SpApiBaseModel):
    """An event linked to the payment of a fee related to the specified deal."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    posted_date: Annotated[
        Optional["Date"],
        Field(
            None,
            validation_alias=AliasChoices("postedDate", "posted_date"),
            serialization_alias="postedDate",
            description="The date and time when the financial event was posted.",
        ),
    ]

    deal_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("dealId", "deal_id"),
            serialization_alias="dealId",
            description="The unique identifier of the deal.",
        ),
    ]

    deal_description: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("dealDescription", "deal_description"),
            serialization_alias="dealDescription",
            description="The internal description of the deal.",
        ),
    ]

    event_type: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("eventType", "event_type"),
            serialization_alias="eventType",
            description="The type of event: SellerDealComplete.",
        ),
    ]

    fee_type: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("feeType", "fee_type"),
            serialization_alias="feeType",
            description="The type of fee: RunLightningDealFee.",
        ),
    ]

    fee_amount: Annotated[
        Optional["Currency"],
        Field(
            None,
            validation_alias=AliasChoices("feeAmount", "fee_amount"),
            serialization_alias="feeAmount",
            description="The monetary amount of the fee.",
        ),
    ]

    tax_amount: Annotated[
        Optional["Currency"],
        Field(
            None,
            validation_alias=AliasChoices("taxAmount", "tax_amount"),
            serialization_alias="taxAmount",
            description="The monetary amount of the tax applied.",
        ),
    ]

    total_amount: Annotated[
        Optional["Currency"],
        Field(
            None,
            validation_alias=AliasChoices("totalAmount", "total_amount"),
            serialization_alias="totalAmount",
            description="The total monetary amount paid.",
        ),
    ]


"""
SellerReviewEnrollmentPaymentEvent

A fee payment event for the Early Reviewer Program.
"""


class SellerReviewEnrollmentPaymentEvent(SpApiBaseModel):
    """A fee payment event for the Early Reviewer Program."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    posted_date: Annotated[
        Optional["Date"],
        Field(
            None,
            validation_alias=AliasChoices("PostedDate", "posted_date"),
            serialization_alias="PostedDate",
            description="The date and time when the financial event was posted.",
        ),
    ]

    enrollment_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("EnrollmentId", "enrollment_id"),
            serialization_alias="EnrollmentId",
            description="An enrollment identifier.",
        ),
    ]

    parent_a_s_i_n: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("ParentASIN", "parent_a_s_i_n"),
            serialization_alias="ParentASIN",
            description="The Amazon Standard Identification Number (ASIN) of the item that was enrolled in the Early Reviewer Program.",
        ),
    ]

    fee_component: Annotated[
        Optional["FeeComponent"],
        Field(
            None,
            validation_alias=AliasChoices("FeeComponent", "fee_component"),
            serialization_alias="FeeComponent",
        ),
    ]

    charge_component: Annotated[
        Optional["ChargeComponent"],
        Field(
            None,
            validation_alias=AliasChoices("ChargeComponent", "charge_component"),
            serialization_alias="ChargeComponent",
        ),
    ]

    total_amount: Annotated[
        Optional["Currency"],
        Field(
            None,
            validation_alias=AliasChoices("TotalAmount", "total_amount"),
            serialization_alias="TotalAmount",
            description="The FeeComponent value plus the ChargeComponent value.",
        ),
    ]


"""
ServiceFeeEvent

A service fee on the seller's account.
"""


class ServiceFeeEvent(SpApiBaseModel):
    """A service fee on the seller's account."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    amazon_order_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("AmazonOrderId", "amazon_order_id"),
            serialization_alias="AmazonOrderId",
            description="An Amazon-defined identifier for an order.",
        ),
    ]

    fee_reason: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("FeeReason", "fee_reason"),
            serialization_alias="FeeReason",
            description="A short description of the service fee reason.",
        ),
    ]

    fee_list: Annotated[
        Optional["FeeComponentList"],
        Field(
            None,
            validation_alias=AliasChoices("FeeList", "fee_list"),
            serialization_alias="FeeList",
            description="A list of fee components associated with the service fee.",
        ),
    ]

    seller_s_k_u: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("SellerSKU", "seller_s_k_u"),
            serialization_alias="SellerSKU",
            description="The seller SKU of the item. The seller SKU is qualified by the seller's seller ID, which is included with every call to the Selling Partner API.",
        ),
    ]

    fn_s_k_u: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("FnSKU", "fn_s_k_u"),
            serialization_alias="FnSKU",
            description="A unique identifier assigned by Amazon to products stored in and fulfilled from an Amazon fulfillment center.",
        ),
    ]

    fee_description: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("FeeDescription", "fee_description"),
            serialization_alias="FeeDescription",
            description="A short description of the service fee event.",
        ),
    ]

    a_s_i_n: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("ASIN", "a_s_i_n"),
            serialization_alias="ASIN",
            description="The Amazon Standard Identification Number (ASIN) of the item.",
        ),
    ]

    store_name: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("StoreName", "store_name"),
            serialization_alias="StoreName",
            description="The name of the store where the event occurred.",
        ),
    ]


ShipmentItemList = List["ShipmentItem"]
"""A list of shipment items."""


"""
ShipmentEvent

A shipment, refund, guarantee claim, or chargeback.
"""


class ShipmentEvent(SpApiBaseModel):
    """A shipment, refund, guarantee claim, or chargeback."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    amazon_order_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("AmazonOrderId", "amazon_order_id"),
            serialization_alias="AmazonOrderId",
            description="An Amazon-defined identifier for an order.",
        ),
    ]

    seller_order_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("SellerOrderId", "seller_order_id"),
            serialization_alias="SellerOrderId",
            description="A seller-defined identifier for an order.",
        ),
    ]

    marketplace_name: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("MarketplaceName", "marketplace_name"),
            serialization_alias="MarketplaceName",
            description="The name of the marketplace where the event occurred.",
        ),
    ]

    store_name: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("StoreName", "store_name"),
            serialization_alias="StoreName",
            description="The name of the store where the event occurred.",
        ),
    ]

    order_charge_list: Annotated[
        Optional["ChargeComponentList"],
        Field(
            None,
            validation_alias=AliasChoices("OrderChargeList", "order_charge_list"),
            serialization_alias="OrderChargeList",
            description="A list of order-level charges. These charges are applicable to Multi-Channel Fulfillment COD orders.",
        ),
    ]

    order_charge_adjustment_list: Annotated[
        Optional["ChargeComponentList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "OrderChargeAdjustmentList", "order_charge_adjustment_list"
            ),
            serialization_alias="OrderChargeAdjustmentList",
            description="A list of order-level charge adjustments. These adjustments are applicable to Multi-Channel Fulfillment COD orders.",
        ),
    ]

    shipment_fee_list: Annotated[
        Optional["FeeComponentList"],
        Field(
            None,
            validation_alias=AliasChoices("ShipmentFeeList", "shipment_fee_list"),
            serialization_alias="ShipmentFeeList",
            description="A list of shipment-level fees.",
        ),
    ]

    shipment_fee_adjustment_list: Annotated[
        Optional["FeeComponentList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "ShipmentFeeAdjustmentList", "shipment_fee_adjustment_list"
            ),
            serialization_alias="ShipmentFeeAdjustmentList",
            description="A list of shipment-level fee adjustments.",
        ),
    ]

    order_fee_list: Annotated[
        Optional["FeeComponentList"],
        Field(
            None,
            validation_alias=AliasChoices("OrderFeeList", "order_fee_list"),
            serialization_alias="OrderFeeList",
            description="A list of order-level fees. These charges are applicable to Multi-Channel Fulfillment orders.",
        ),
    ]

    order_fee_adjustment_list: Annotated[
        Optional["FeeComponentList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "OrderFeeAdjustmentList", "order_fee_adjustment_list"
            ),
            serialization_alias="OrderFeeAdjustmentList",
            description="A list of order-level fee adjustments. These adjustments are applicable to Multi-Channel Fulfillment orders.",
        ),
    ]

    direct_payment_list: Annotated[
        Optional["DirectPaymentList"],
        Field(
            None,
            validation_alias=AliasChoices("DirectPaymentList", "direct_payment_list"),
            serialization_alias="DirectPaymentList",
            description="A list of transactions where buyers pay Amazon through one of the credit cards offered by Amazon or where buyers pay a seller directly through COD.",
        ),
    ]

    posted_date: Annotated[
        Optional["Date"],
        Field(
            None,
            validation_alias=AliasChoices("PostedDate", "posted_date"),
            serialization_alias="PostedDate",
            description="The date and time when the financial event was posted.",
        ),
    ]

    shipment_item_list: Annotated[
        Optional["ShipmentItemList"],
        Field(
            None,
            validation_alias=AliasChoices("ShipmentItemList", "shipment_item_list"),
            serialization_alias="ShipmentItemList",
        ),
    ]

    shipment_item_adjustment_list: Annotated[
        Optional["ShipmentItemList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "ShipmentItemAdjustmentList", "shipment_item_adjustment_list"
            ),
            serialization_alias="ShipmentItemAdjustmentList",
            description="A list of shipment item adjustments.",
        ),
    ]


"""
ShipmentItem

An item of a shipment, refund, guarantee claim, or chargeback.
"""


class ShipmentItem(SpApiBaseModel):
    """An item of a shipment, refund, guarantee claim, or chargeback."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    seller_s_k_u: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("SellerSKU", "seller_s_k_u"),
            serialization_alias="SellerSKU",
            description="The seller SKU of the item. The seller SKU is qualified by the seller's seller ID, which is included with every call to the Selling Partner API.",
        ),
    ]

    order_item_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("OrderItemId", "order_item_id"),
            serialization_alias="OrderItemId",
            description="An Amazon-defined order item identifier.",
        ),
    ]

    order_adjustment_item_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "OrderAdjustmentItemId", "order_adjustment_item_id"
            ),
            serialization_alias="OrderAdjustmentItemId",
            description="An Amazon-defined order adjustment identifier defined for refunds, guarantee claims, and chargeback events.",
        ),
    ]

    quantity_shipped: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices("QuantityShipped", "quantity_shipped"),
            serialization_alias="QuantityShipped",
            description="The number of items shipped.",
        ),
    ]

    item_charge_list: Annotated[
        Optional["ChargeComponentList"],
        Field(
            None,
            validation_alias=AliasChoices("ItemChargeList", "item_charge_list"),
            serialization_alias="ItemChargeList",
            description="A list of charges associated with the shipment item.",
        ),
    ]

    item_charge_adjustment_list: Annotated[
        Optional["ChargeComponentList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "ItemChargeAdjustmentList", "item_charge_adjustment_list"
            ),
            serialization_alias="ItemChargeAdjustmentList",
            description="A list of charge adjustments associated with the shipment item. This value is only returned for refunds, guarantee claims, and chargeback events.",
        ),
    ]

    item_fee_list: Annotated[
        Optional["FeeComponentList"],
        Field(
            None,
            validation_alias=AliasChoices("ItemFeeList", "item_fee_list"),
            serialization_alias="ItemFeeList",
            description="A list of fees associated with the shipment item.",
        ),
    ]

    item_fee_adjustment_list: Annotated[
        Optional["FeeComponentList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "ItemFeeAdjustmentList", "item_fee_adjustment_list"
            ),
            serialization_alias="ItemFeeAdjustmentList",
            description="A list of fee adjustments associated with the shipment item. This value is only returned for refunds, guarantee claims, and chargeback events.",
        ),
    ]

    item_tax_withheld_list: Annotated[
        Optional["TaxWithheldComponentList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "ItemTaxWithheldList", "item_tax_withheld_list"
            ),
            serialization_alias="ItemTaxWithheldList",
            description="A list of taxes withheld information for a shipment item.",
        ),
    ]

    promotion_list: Annotated[
        Optional["PromotionList"],
        Field(
            None,
            validation_alias=AliasChoices("PromotionList", "promotion_list"),
            serialization_alias="PromotionList",
        ),
    ]

    promotion_adjustment_list: Annotated[
        Optional["PromotionList"],
        Field(
            None,
            validation_alias=AliasChoices(
                "PromotionAdjustmentList", "promotion_adjustment_list"
            ),
            serialization_alias="PromotionAdjustmentList",
            description="A list of promotion adjustments associated with the shipment item. This value is only returned for refunds, guarantee claims, and chargeback events.",
        ),
    ]

    cost_of_points_granted: Annotated[
        Optional["Currency"],
        Field(
            None,
            validation_alias=AliasChoices(
                "CostOfPointsGranted", "cost_of_points_granted"
            ),
            serialization_alias="CostOfPointsGranted",
            description="The cost of Amazon Points granted for a shipment item.",
        ),
    ]

    cost_of_points_returned: Annotated[
        Optional["Currency"],
        Field(
            None,
            validation_alias=AliasChoices(
                "CostOfPointsReturned", "cost_of_points_returned"
            ),
            serialization_alias="CostOfPointsReturned",
            description="The cost of Amazon Points returned for a shipment item. This value is only returned for refunds, guarantee claims, and chargeback events.",
        ),
    ]


"""
SolutionProviderCreditEvent

A credit given to a solution provider.
"""


class SolutionProviderCreditEvent(SpApiBaseModel):
    """A credit given to a solution provider."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    provider_transaction_type: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "ProviderTransactionType", "provider_transaction_type"
            ),
            serialization_alias="ProviderTransactionType",
            description="The transaction type.",
        ),
    ]

    seller_order_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("SellerOrderId", "seller_order_id"),
            serialization_alias="SellerOrderId",
            description="A seller-defined identifier for an order.",
        ),
    ]

    marketplace_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("MarketplaceId", "marketplace_id"),
            serialization_alias="MarketplaceId",
            description="The identifier of the marketplace where the order was placed.",
        ),
    ]

    marketplace_country_code: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "MarketplaceCountryCode", "marketplace_country_code"
            ),
            serialization_alias="MarketplaceCountryCode",
            description="The two-letter country code of the country associated with the marketplace where the order was placed.",
        ),
    ]

    seller_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("SellerId", "seller_id"),
            serialization_alias="SellerId",
            description="The Amazon-defined identifier of the seller.",
        ),
    ]

    seller_store_name: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("SellerStoreName", "seller_store_name"),
            serialization_alias="SellerStoreName",
            description="The store name where the payment event occurred.",
        ),
    ]

    provider_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("ProviderId", "provider_id"),
            serialization_alias="ProviderId",
            description="The Amazon-defined identifier of the solution provider.",
        ),
    ]

    provider_store_name: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("ProviderStoreName", "provider_store_name"),
            serialization_alias="ProviderStoreName",
            description="The store name where the payment event occurred.",
        ),
    ]

    transaction_amount: Annotated[
        Optional["Currency"],
        Field(
            None,
            validation_alias=AliasChoices("TransactionAmount", "transaction_amount"),
            serialization_alias="TransactionAmount",
            description="The amount of the credit.",
        ),
    ]

    transaction_creation_date: Annotated[
        Optional["Date"],
        Field(
            None,
            validation_alias=AliasChoices(
                "TransactionCreationDate", "transaction_creation_date"
            ),
            serialization_alias="TransactionCreationDate",
            description="The date and time that the credit transaction was created, in [ISO 8601](https://developer-docs.amazon.com/sp-api/docs/iso-8601) date time format.",
        ),
    ]


"""
TDSReimbursementEvent

An event related to a Tax-Deducted-at-Source (TDS) reimbursement.
"""


class TDSReimbursementEvent(SpApiBaseModel):
    """An event related to a Tax-Deducted-at-Source (TDS) reimbursement."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    posted_date: Annotated[
        Optional["Date"],
        Field(
            None,
            validation_alias=AliasChoices("PostedDate", "posted_date"),
            serialization_alias="PostedDate",
            description="The date and time when the financial event was posted.",
        ),
    ]

    t_d_s_order_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("TDSOrderId", "t_d_s_order_id"),
            serialization_alias="TDSOrderId",
            description="The Tax-Deducted-at-Source (TDS) identifier.",
        ),
    ]

    reimbursed_amount: Annotated[
        Optional["Currency"],
        Field(
            None,
            validation_alias=AliasChoices("ReimbursedAmount", "reimbursed_amount"),
            serialization_alias="ReimbursedAmount",
            description="The amount reimbursed.",
        ),
    ]


"""
TaxWithheldComponent

Information about the taxes withheld.
"""


class TaxWithheldComponent(SpApiBaseModel):
    """Information about the taxes withheld."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    tax_collection_model: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("TaxCollectionModel", "tax_collection_model"),
            serialization_alias="TaxCollectionModel",
            description="The tax collection model applied to the item. Possible values: * MarketplaceFacilitator - Tax is withheld and remitted to the taxing authority by Amazon on behalf of the seller. * Standard - Tax is paid to the seller and not remitted to the taxing authority by Amazon.",
        ),
    ]

    taxes_withheld: Annotated[
        Optional["ChargeComponentList"],
        Field(
            None,
            validation_alias=AliasChoices("TaxesWithheld", "taxes_withheld"),
            serialization_alias="TaxesWithheld",
            description="A list of charges that represent the types and amounts of taxes withheld.",
        ),
    ]


"""
TaxWithholdingPeriod

Period which taxwithholding on seller's account is calculated.
"""


class TaxWithholdingPeriod(SpApiBaseModel):
    """Period which taxwithholding on seller's account is calculated."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    start_date: Annotated[
        Optional["Date"],
        Field(
            None,
            validation_alias=AliasChoices("StartDate", "start_date"),
            serialization_alias="StartDate",
            description="Start of the time range.",
        ),
    ]

    end_date: Annotated[
        Optional["Date"],
        Field(
            None,
            validation_alias=AliasChoices("EndDate", "end_date"),
            serialization_alias="EndDate",
            description="End of the time range.",
        ),
    ]


"""
TaxWithholdingEvent

A TaxWithholding event on seller's account.
"""


class TaxWithholdingEvent(SpApiBaseModel):
    """A TaxWithholding event on seller's account."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    posted_date: Annotated[
        Optional["Date"],
        Field(
            None,
            validation_alias=AliasChoices("PostedDate", "posted_date"),
            serialization_alias="PostedDate",
            description="The date and time when the financial event was posted.",
        ),
    ]

    base_amount: Annotated[
        Optional["Currency"],
        Field(
            None,
            validation_alias=AliasChoices("BaseAmount", "base_amount"),
            serialization_alias="BaseAmount",
            description="The amount which tax was withheld against.",
        ),
    ]

    withheld_amount: Annotated[
        Optional["Currency"],
        Field(
            None,
            validation_alias=AliasChoices("WithheldAmount", "withheld_amount"),
            serialization_alias="WithheldAmount",
            description="The amount of the tax withholding deducted from seller's account.",
        ),
    ]

    tax_withholding_period: Annotated[
        Optional["TaxWithholdingPeriod"],
        Field(
            None,
            validation_alias=AliasChoices(
                "TaxWithholdingPeriod", "tax_withholding_period"
            ),
            serialization_alias="TaxWithholdingPeriod",
            description="Time period for which tax is withheld.",
        ),
    ]


"""
TrialShipmentEvent

An event related to a trial shipment.
"""


class TrialShipmentEvent(SpApiBaseModel):
    """An event related to a trial shipment."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    amazon_order_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("AmazonOrderId", "amazon_order_id"),
            serialization_alias="AmazonOrderId",
            description="An Amazon-defined identifier for an order.",
        ),
    ]

    financial_event_group_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "FinancialEventGroupId", "financial_event_group_id"
            ),
            serialization_alias="FinancialEventGroupId",
            description="The identifier of the financial event group.",
        ),
    ]

    posted_date: Annotated[
        Optional["Date"],
        Field(
            None,
            validation_alias=AliasChoices("PostedDate", "posted_date"),
            serialization_alias="PostedDate",
            description="The date and time when the financial event was posted.",
        ),
    ]

    s_k_u: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("SKU", "s_k_u"),
            serialization_alias="SKU",
            description="The seller SKU of the item. The seller SKU is qualified by the seller's seller ID, which is included with every call to the Selling Partner API.",
        ),
    ]

    fee_list: Annotated[
        Optional["FeeComponentList"],
        Field(
            None,
            validation_alias=AliasChoices("FeeList", "fee_list"),
            serialization_alias="FeeList",
            description="A list of fees charged by Amazon for trial shipments.",
        ),
    ]


"""
ValueAddedServiceChargeEvent

An event related to a value added service charge.
"""


class ValueAddedServiceChargeEvent(SpApiBaseModel):
    """An event related to a value added service charge."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    transaction_type: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("TransactionType", "transaction_type"),
            serialization_alias="TransactionType",
            description="Indicates the type of transaction. Example: 'Other Support Service fees'",
        ),
    ]

    posted_date: Annotated[
        Optional["Date"],
        Field(
            None,
            validation_alias=AliasChoices("PostedDate", "posted_date"),
            serialization_alias="PostedDate",
            description="The date and time when the financial event was posted.",
        ),
    ]

    description: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("Description", "description"),
            serialization_alias="Description",
            description="A short description of the service charge event.",
        ),
    ]

    transaction_amount: Annotated[
        Optional["Currency"],
        Field(
            None,
            validation_alias=AliasChoices("TransactionAmount", "transaction_amount"),
            serialization_alias="TransactionAmount",
            description="The amount of the service charge event.",
        ),
    ]


# Rebuild models to resolve forward references
AdhocDisbursementEvent.model_rebuild()
AdjustmentEvent.model_rebuild()
AdjustmentItem.model_rebuild()
AffordabilityExpenseEvent.model_rebuild()
ChargeComponent.model_rebuild()
ChargeInstrument.model_rebuild()
ChargeRefundEvent.model_rebuild()
ChargeRefundTransaction.model_rebuild()
CouponPaymentEvent.model_rebuild()
Currency.model_rebuild()
DebtRecoveryEvent.model_rebuild()
DebtRecoveryItem.model_rebuild()
DirectPayment.model_rebuild()
FailedAdhocDisbursementEvent.model_rebuild()
FBALiquidationEvent.model_rebuild()
FeeComponent.model_rebuild()
FinancialEventGroup.model_rebuild()
FinancialEvents.model_rebuild()
ImagingServicesFeeEvent.model_rebuild()
ListFinancialEventGroupsPayload.model_rebuild()
ListFinancialEventGroupsResponse.model_rebuild()
ListFinancialEventsPayload.model_rebuild()
ListFinancialEventsResponse.model_rebuild()
LoanServicingEvent.model_rebuild()
NetworkComminglingTransactionEvent.model_rebuild()
PayWithAmazonEvent.model_rebuild()
ProductAdsPaymentEvent.model_rebuild()
Promotion.model_rebuild()
RemovalShipmentEvent.model_rebuild()
RemovalShipmentItem.model_rebuild()
RemovalShipmentAdjustmentEvent.model_rebuild()
RemovalShipmentItemAdjustment.model_rebuild()
RentalTransactionEvent.model_rebuild()
RetrochargeEvent.model_rebuild()
SAFETReimbursementEvent.model_rebuild()
SAFETReimbursementItem.model_rebuild()
SellerDealPaymentEvent.model_rebuild()
SellerReviewEnrollmentPaymentEvent.model_rebuild()
ServiceFeeEvent.model_rebuild()
ShipmentEvent.model_rebuild()
ShipmentItem.model_rebuild()
SolutionProviderCreditEvent.model_rebuild()
TaxWithholdingPeriod.model_rebuild()
TaxWithholdingEvent.model_rebuild()
TaxWithheldComponent.model_rebuild()
TDSReimbursementEvent.model_rebuild()
TrialShipmentEvent.model_rebuild()
ValueAddedServiceChargeEvent.model_rebuild()
CapacityReservationBillingEvent.model_rebuild()
Error.model_rebuild()
ListFinancialEventGroupsRequest.model_rebuild()
ListFinancialEventsByGroupIdRequest.model_rebuild()
ListFinancialEventsByOrderIdRequest.model_rebuild()
ListFinancialEventsRequest.model_rebuild()
