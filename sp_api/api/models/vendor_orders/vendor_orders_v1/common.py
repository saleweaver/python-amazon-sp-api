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


# Enum definitions
class UnitOfMeasureEnum(str, Enum):
    """Enum for unitOfMeasure"""

    CASES = "Cases"  # Packing of individual items into a case.
    EACHES = "Eaches"  # Individual items.


"""
ItemQuantity

Details of quantity ordered.
"""


class ItemQuantity(SpApiBaseModel):
    """Details of quantity ordered."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    amount: Annotated[
        Optional[int],
        Field(
            None, description="Acknowledged quantity. This value should not be zero."
        ),
    ]

    unit_of_measure: Annotated[
        Optional[UnitOfMeasureEnum],
        Field(
            None,
            validation_alias=AliasChoices("unitOfMeasure", "unit_of_measure"),
            serialization_alias="unitOfMeasure",
            description="Unit of measure for the acknowledged quantity.",
        ),
    ]

    unit_size: Annotated[
        Optional[int],
        Field(
            None,
            validation_alias=AliasChoices("unitSize", "unit_size"),
            serialization_alias="unitSize",
            description="The case size, in the event that we ordered using cases.",
        ),
    ]


"""
AcknowledgementStatusDetails

Details of item quantity ordered
"""


class AcknowledgementStatusDetails(SpApiBaseModel):
    """Details of item quantity ordered"""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    acknowledgement_date: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices(
                "acknowledgementDate", "acknowledgement_date"
            ),
            serialization_alias="acknowledgementDate",
            description="The date when the line item was confirmed by vendor. Must be in ISO-8601 date/time format.",
        ),
    ]

    accepted_quantity: Annotated[
        Optional["ItemQuantity"],
        Field(
            None,
            validation_alias=AliasChoices("acceptedQuantity", "accepted_quantity"),
            serialization_alias="acceptedQuantity",
            description="Item quantity accepted by vendor to be shipped.",
        ),
    ]

    rejected_quantity: Annotated[
        Optional["ItemQuantity"],
        Field(
            None,
            validation_alias=AliasChoices("rejectedQuantity", "rejected_quantity"),
            serialization_alias="rejectedQuantity",
            description="Item quantity rejected by vendor.",
        ),
    ]


"""
Address

Address of the party.
"""


class Address(SpApiBaseModel):
    """Address of the party."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    name: Annotated[
        str,
        Field(
            ...,
            description="The name of the person, business or institution at that address.",
        ),
    ]

    address_line1: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("addressLine1", "address_line1"),
            serialization_alias="addressLine1",
            description="First line of the address.",
        ),
    ]

    address_line2: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("addressLine2", "address_line2"),
            serialization_alias="addressLine2",
            description="Additional address information, if required.",
        ),
    ]

    address_line3: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("addressLine3", "address_line3"),
            serialization_alias="addressLine3",
            description="Additional address information, if required.",
        ),
    ]

    city: Annotated[
        Optional[str],
        Field(
            None,
            description="The city where the person, business or institution is located.",
        ),
    ]

    county: Annotated[
        Optional[str],
        Field(
            None,
            description="The county where person, business or institution is located.",
        ),
    ]

    district: Annotated[
        Optional[str],
        Field(
            None,
            description="The district where person, business or institution is located.",
        ),
    ]

    state_or_region: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("stateOrRegion", "state_or_region"),
            serialization_alias="stateOrRegion",
            description="The state or region where person, business or institution is located.",
        ),
    ]

    postal_code: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("postalCode", "postal_code"),
            serialization_alias="postalCode",
            description="The postal code of that address. It conatins a series of letters or digits or both, sometimes including spaces or punctuation.",
        ),
    ]

    country_code: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("countryCode", "country_code"),
            serialization_alias="countryCode",
            description="The two digit country code. In ISO 3166-1 alpha-2 format.",
        ),
    ]

    phone: Annotated[
        Optional[str],
        Field(
            None,
            description="The phone number of the person, business or institution located at that address.",
        ),
    ]


DateTimeInterval = str
"""Defines a date time interval according to ISO8601. Interval is separated by double hyphen (--)."""


Decimal = str
"""A decimal number with no loss of precision. Useful when precision loss is unacceptable, as with currencies. Follows RFC7159 for number representation. <br>**Pattern** : `^-?(0|([1-9]d*))(.d+)?([eE][+-]?d+)?$`."""


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
        str, Field(..., description="A message that describes the error condition.")
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
GetPurchaseOrderRequest

Request parameters for getPurchaseOrder
"""


class GetPurchaseOrderRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getPurchaseOrder
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    purchase_order_number: Annotated[
        str,
        PathParam(),
        Field(
            ...,
            validation_alias=AliasChoices(
                "purchaseOrderNumber", "purchase_order_number"
            ),
            serialization_alias="purchaseOrderNumber",
            description="[PATH] The purchase order identifier for the order that you want. Formatting Notes: 8-character alpha-numeric code.",
        ),
    ]


# Enum definitions
class MethodOfPaymentEnum(str, Enum):
    """Enum for methodOfPayment"""

    PAID_BY_BUYER = "PaidByBuyer"  # Buyer pays for shipping.
    COLLECT_ON_DELIVERY = "CollectOnDelivery"  # Buyer pays for shipping on delivery.
    DEFINED_BY_BUYER_AND_SELLER = "DefinedByBuyerAndSeller"  # Shipping costs paid as agreed upon between buyer and seller.
    FOB_PORT_OF_CALL = "FOBPortOfCall"  # Seller pays for transportation including loading and shipping.
    PREPAID_BY_SELLER = "PrepaidBySeller"  # Seller prepays for shipping.
    PAID_BY_SELLER = "PaidBySeller"  # Seller pays for shipping.


class InternationalCommercialTermsEnum(str, Enum):
    """Enum for internationalCommercialTerms"""

    EX_WORKS = "ExWorks"  # Places the maximum obligation on the buyer and minimum obligations on the seller. The seller makes the goods available at its premises. The buyer is responsible for all costs of the transportation of the shipment and bears all the risks for bringing the goods to their final destination.
    FREE_CARRIER = "FreeCarrier"  # The seller hands over the goods, cleared for export, into the disposal of the carrier (named by the buyer). The buyer pays for all the additional costs of transportation and risk passes when the goods are handed over to the carrier.
    FREE_ON_BOARD = "FreeOnBoard"  # Ocean shipments only. The seller must deliver the goods alongside the ship at the named port, and clear the goods for export. The buyer pays for all the additional costs of transportation and risk passes when the goods are alongside the ship.
    FREE_ALONG_SIDE_SHIP = "FreeAlongSideShip"  # Ocean shipments only. The seller must load the goods on board the vessel, cleared for export. The buyer pays for all the additional costs of transportation and risk passes when the goods are loaded on the ship.
    CARRIAGE_PAID_TO = "CarriagePaidTo"  # The seller pays for transportation to the named port of destination, but risk transfers to the buyer upon handing goods over to the first carrier. The buyer pays for all destination charges.
    COST_AND_FREIGHT = "CostAndFreight"  # Ocean shipments only. Seller pays for transportation to the named port of destination, but risk transfers to the buyer once the goods are loaded on the vessel. The buyer pays for all destination charges.
    CARRIAGE_AND_INSURANCE_PAID_TO = "CarriageAndInsurancePaidTo"  # Seller pays for transportation and insurance to the named port of destination, but risk transfers to the buyer upon handing goods over to the first carrier. The buyer pays for all destination charges.
    COST_INSURANCE_AND_FREIGHT = "CostInsuranceAndFreight"  # Ocean shipments only. Seller pays for transportation and insurance to the named port of destination, but risk transfers to the buyer once the goods are loaded on the vessel. The buyer pays for all destination charges.
    DELIVERED_AT_TERMINAL = "DeliveredAtTerminal"  # Seller pays for transportation up to the destination terminal, and risks up to the point that the goods are unloaded at the terminal. The buyer pays for import clearance, duties & taxes and delivery costs.
    DELIVERED_AT_PLACE = "DeliveredAtPlace"  # Seller pays for transportation to the named destination, and risk transfers at the point that the goods are ready for unloading by the buyer. The buyer pays for import clearance, duties & taxes and delivery costs.
    DELIVER_DUTY_PAID = "DeliverDutyPaid"  # Seller is responsible for delivering the goods to the named place in the country of the buyer, and pays all costs in bringing the goods to the destination including import duties and taxes. This term places the maximum obligations on the seller and minimum obligations on the buyer.


"""
ImportDetails

Import details for an import order.
"""


class ImportDetails(SpApiBaseModel):
    """Import details for an import order."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    method_of_payment: Annotated[
        Optional[MethodOfPaymentEnum],
        Field(
            None,
            validation_alias=AliasChoices("methodOfPayment", "method_of_payment"),
            serialization_alias="methodOfPayment",
            description="If the recipient requests, contains the shipment method of payment. This is for import PO's only.",
        ),
    ]

    international_commercial_terms: Annotated[
        Optional[InternationalCommercialTermsEnum],
        Field(
            None,
            validation_alias=AliasChoices(
                "internationalCommercialTerms", "international_commercial_terms"
            ),
            serialization_alias="internationalCommercialTerms",
            description="Incoterms (International Commercial Terms) are used to divide transaction costs and responsibilities between buyer and seller and reflect state-of-the-art transportation practices. This is for import purchase orders only. ",
        ),
    ]

    port_of_delivery: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("portOfDelivery", "port_of_delivery"),
            serialization_alias="portOfDelivery",
            description="The port where goods on an import purchase order must be delivered by the vendor. This should only be specified when the internationalCommercialTerms is FOB.",
        ),
    ]

    import_containers: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("importContainers", "import_containers"),
            serialization_alias="importContainers",
            description="Types and numbers of container(s) for import purchase orders. Can be a comma-separated list if the shipment has multiple containers. HC signifies a high-capacity container. Free-text field, limited to 64 characters. The format will be a comma-delimited list containing values of the type: $NUMBER_OF_CONTAINERS_OF_THIS_TYPE-$CONTAINER_TYPE. The list of values for the container type is: 40'(40-foot container), 40'HC (40-foot high-capacity container), 45', 45'HC, 30', 30'HC, 20', 20'HC.",
        ),
    ]

    shipping_instructions: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "shippingInstructions", "shipping_instructions"
            ),
            serialization_alias="shippingInstructions",
            description="Special instructions regarding the shipment. This field is for import purchase orders.",
        ),
    ]


# Enum definitions
class UnitOfMeasureEnum(str, Enum):
    """Enum for unitOfMeasure"""

    CASES = "Cases"  # Packing of individual items into a case.
    EACHES = "Eaches"  # Individual items.


"""
Money

An amount of money. Includes the currency code and an optional unit of measure for items priced by weight.
"""


class Money(SpApiBaseModel):
    """An amount of money. Includes the currency code and an optional unit of measure for items priced by weight."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    currency_code: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("currencyCode", "currency_code"),
            serialization_alias="currencyCode",
            description="Three digit currency code in ISO 4217 format. String of length 3.",
        ),
    ]

    amount: Annotated[
        Optional["Decimal"],
        Field(
            None,
        ),
    ]

    unit_of_measure: Annotated[
        Optional[UnitOfMeasureEnum],
        Field(
            None,
            validation_alias=AliasChoices("unitOfMeasure", "unit_of_measure"),
            serialization_alias="unitOfMeasure",
            description="The unit of measure for prices of items sold by weight. If this field is absent, the item is sold by eaches.",
        ),
    ]


"""
OrderItem

Represents an individual item in an order, including item details, quantities, pricing, and backorder information.
"""


class OrderItem(SpApiBaseModel):
    """Represents an individual item in an order, including item details, quantities, pricing, and backorder information."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    item_sequence_number: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("itemSequenceNumber", "item_sequence_number"),
            serialization_alias="itemSequenceNumber",
            description="Numbering of the item on the purchase order. The first item will be 1, the second 2, and so on.",
        ),
    ]

    amazon_product_identifier: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "amazonProductIdentifier", "amazon_product_identifier"
            ),
            serialization_alias="amazonProductIdentifier",
            description="Amazon Standard Identification Number (ASIN) of an item.",
        ),
    ]

    vendor_product_identifier: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "vendorProductIdentifier", "vendor_product_identifier"
            ),
            serialization_alias="vendorProductIdentifier",
            description="The vendor selected product identification of the item.",
        ),
    ]

    ordered_quantity: Annotated[
        "ItemQuantity",
        Field(
            ...,
            validation_alias=AliasChoices("orderedQuantity", "ordered_quantity"),
            serialization_alias="orderedQuantity",
            description="Item quantity ordered.",
        ),
    ]

    is_back_order_allowed: Annotated[
        bool,
        Field(
            ...,
            validation_alias=AliasChoices(
                "isBackOrderAllowed", "is_back_order_allowed"
            ),
            serialization_alias="isBackOrderAllowed",
            description="When true, we will accept backorder confirmations for this item.",
        ),
    ]

    net_cost: Annotated[
        Optional["Money"],
        Field(
            None,
            validation_alias=AliasChoices("netCost", "net_cost"),
            serialization_alias="netCost",
            description="The net cost of an item per each or weight unit.",
        ),
    ]

    list_price: Annotated[
        Optional["Money"],
        Field(
            None,
            validation_alias=AliasChoices("listPrice", "list_price"),
            serialization_alias="listPrice",
            description="The list price of an item per each or weight unit.",
        ),
    ]


# Enum definitions
class TaxRegistrationTypeEnum(str, Enum):
    """Enum for taxRegistrationType"""

    VAT = "VAT"  # Value-added tax.
    GST = "GST"  # Goods and Services tax.


"""
TaxRegistrationDetails

Tax registration details of the entity.
"""


class TaxRegistrationDetails(SpApiBaseModel):
    """Tax registration details of the entity."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    tax_registration_type: Annotated[
        TaxRegistrationTypeEnum,
        Field(
            ...,
            validation_alias=AliasChoices(
                "taxRegistrationType", "tax_registration_type"
            ),
            serialization_alias="taxRegistrationType",
            description="Tax registration type for the entity.",
        ),
    ]

    tax_registration_number: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices(
                "taxRegistrationNumber", "tax_registration_number"
            ),
            serialization_alias="taxRegistrationNumber",
            description="Tax registration number for the entity. For example, VAT ID.",
        ),
    ]


"""
PartyIdentification

Name, address and tax details of a party.
"""


class PartyIdentification(SpApiBaseModel):
    """Name, address and tax details of a party."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    party_id: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("partyId", "party_id"),
            serialization_alias="partyId",
            description="Assigned identification for the party. For example, warehouse code or vendor code. Please refer to specific party for more details.",
        ),
    ]

    address: Annotated[
        Optional["Address"],
        Field(None, description="Identification of the party by address."),
    ]

    tax_info: Annotated[
        Optional["TaxRegistrationDetails"],
        Field(
            None,
            validation_alias=AliasChoices("taxInfo", "tax_info"),
            serialization_alias="taxInfo",
            description="Tax registration details of the party.",
        ),
    ]


# Enum definitions
class PurchaseOrderTypeEnum(str, Enum):
    """Enum for purchaseOrderType"""

    REGULAR_ORDER = "RegularOrder"  # A regular purchase order is a method for placing orders for a one-time purchase and payment for line item goods that have a specific quantity and unit price.
    CONSIGNED_ORDER = "ConsignedOrder"  # A consignment purchase order is an agreement with a vendor that allows the product to be received, but the inventory still belong to the vendor until the product is used.
    NEW_PRODUCT_INTRODUCTION = (
        "NewProductIntroduction"  # A purchase order where a new product is introduced.
    )
    RUSH_ORDER = "RushOrder"  # Rush orders are purchases of goods that need to be processed and delivered by a certain date that is much sooner than the standard arrival date.


class PaymentMethodEnum(str, Enum):
    """Enum for paymentMethod"""

    INVOICE = "Invoice"  # An invoice payment is submitted by a business to pay for products and services purchased from vendors.
    CONSIGNMENT = "Consignment"  # A retail merchandiser acts as a consignor for goods supplied by the consignee. The consignor pays the consignee after the sale and keeps a percentage of the proceeds
    CREDIT_CARD = "CreditCard"  # Payment is made using a credit card.
    PREPAID = "Prepaid"  # Payment is prepaid.


"""
OrderDetails

Details of an order.
"""


class OrderDetails(SpApiBaseModel):
    """Details of an order."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    purchase_order_date: Annotated[
        datetime,
        Field(
            ...,
            validation_alias=AliasChoices("purchaseOrderDate", "purchase_order_date"),
            serialization_alias="purchaseOrderDate",
            description="The date the purchase order was placed. Must be in ISO-8601 date/time format.",
        ),
    ]

    purchase_order_changed_date: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices(
                "purchaseOrderChangedDate", "purchase_order_changed_date"
            ),
            serialization_alias="purchaseOrderChangedDate",
            description="The date when purchase order was last changed by Amazon after the order was placed. This date will be greater than 'purchaseOrderDate'. This means the PO data was changed on that date and vendors are required to fulfill the updated PO. The PO changes can be related to Item Quantity, Ship to Location, Ship Window etc. This field will not be present in orders that have not changed after creation. Must be in ISO-8601 date/time format.",
        ),
    ]

    purchase_order_state_changed_date: Annotated[
        datetime,
        Field(
            ...,
            validation_alias=AliasChoices(
                "purchaseOrderStateChangedDate", "purchase_order_state_changed_date"
            ),
            serialization_alias="purchaseOrderStateChangedDate",
            description="The date when current purchase order state was changed. Current purchase order state is available in the field 'purchaseOrderState'. Must be in ISO-8601 date/time format.",
        ),
    ]

    purchase_order_type: Annotated[
        Optional[PurchaseOrderTypeEnum],
        Field(
            None,
            validation_alias=AliasChoices("purchaseOrderType", "purchase_order_type"),
            serialization_alias="purchaseOrderType",
            description="Type of purchase order.",
        ),
    ]

    import_details: Annotated[
        Optional["ImportDetails"],
        Field(
            None,
            validation_alias=AliasChoices("importDetails", "import_details"),
            serialization_alias="importDetails",
            description="If the purchase order is an import order, the details for the import order.",
        ),
    ]

    deal_code: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("dealCode", "deal_code"),
            serialization_alias="dealCode",
            description="If requested by the recipient, this field will contain a promotional/deal number. The discount code line is optional. It is used to obtain a price discount on items on the order.",
        ),
    ]

    payment_method: Annotated[
        Optional[PaymentMethodEnum],
        Field(
            None,
            validation_alias=AliasChoices("paymentMethod", "payment_method"),
            serialization_alias="paymentMethod",
            description="Payment method used.",
        ),
    ]

    buying_party: Annotated[
        Optional["PartyIdentification"],
        Field(
            None,
            validation_alias=AliasChoices("buyingParty", "buying_party"),
            serialization_alias="buyingParty",
            description="Name/Address and tax details of the buying party.",
        ),
    ]

    selling_party: Annotated[
        Optional["PartyIdentification"],
        Field(
            None,
            validation_alias=AliasChoices("sellingParty", "selling_party"),
            serialization_alias="sellingParty",
            description="Name/Address and tax details of the selling party.",
        ),
    ]

    ship_to_party: Annotated[
        Optional["PartyIdentification"],
        Field(
            None,
            validation_alias=AliasChoices("shipToParty", "ship_to_party"),
            serialization_alias="shipToParty",
            description="Name/Address and tax details of the ship to party. Find a list of fulfillment center addresses for a region on the [Resources page of Amazon Vendor Central](https://vendorcentral.amazon.com/hz/vendor/members/support/help/node/GPZ88XH8HQM97ZV6).",
        ),
    ]

    bill_to_party: Annotated[
        Optional["PartyIdentification"],
        Field(
            None,
            validation_alias=AliasChoices("billToParty", "bill_to_party"),
            serialization_alias="billToParty",
            description="Name/Address and tax details of the bill to party.",
        ),
    ]

    ship_window: Annotated[
        Optional["DateTimeInterval"],
        Field(
            None,
            validation_alias=AliasChoices("shipWindow", "ship_window"),
            serialization_alias="shipWindow",
            description="This indicates the ship window. Format is start and end date separated by double hyphen (--). For example, 2007-03-01T13:00:00Z--2007-03-11T15:30:00Z.",
        ),
    ]

    delivery_window: Annotated[
        Optional["DateTimeInterval"],
        Field(
            None,
            validation_alias=AliasChoices("deliveryWindow", "delivery_window"),
            serialization_alias="deliveryWindow",
            description="This indicates the delivery window. Format is start and end date separated by double hyphen (--). For example, 2007-03-01T13:00:00Z--2007-03-11T15:30:00Z.",
        ),
    ]

    items: Annotated[
        List["OrderItem"],
        Field(..., description="A list of items in this purchase order."),
    ]


# Enum definitions
class PurchaseOrderStateEnum(str, Enum):
    """Enum for purchaseOrderState"""

    NEW = "New"  # Status of the orders that are newly created.
    ACKNOWLEDGED = "Acknowledged"  # Status of the orders acknowledged by vendors.
    CLOSED = "Closed"  # Status of the orders that are completed.


"""
Order

Represents an order placed by Amazon, including the purchase order number, current state, and order details.
"""


class Order(SpApiBaseModel):
    """Represents an order placed by Amazon, including the purchase order number, current state, and order details."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    purchase_order_number: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices(
                "purchaseOrderNumber", "purchase_order_number"
            ),
            serialization_alias="purchaseOrderNumber",
            description="The purchase order number for this order. Formatting Notes: 8-character alpha-numeric code.",
        ),
    ]

    purchase_order_state: Annotated[
        PurchaseOrderStateEnum,
        Field(
            ...,
            validation_alias=AliasChoices("purchaseOrderState", "purchase_order_state"),
            serialization_alias="purchaseOrderState",
            description="This field will contain the current state of the purchase order.",
        ),
    ]

    order_details: Annotated[
        Optional["OrderDetails"],
        Field(
            None,
            validation_alias=AliasChoices("orderDetails", "order_details"),
            serialization_alias="orderDetails",
            description="Details of an order.",
        ),
    ]


"""
GetPurchaseOrderResponse

The response schema for the getPurchaseOrder operation.
"""


class GetPurchaseOrderResponse(SpApiBaseModel):
    """The response schema for the getPurchaseOrder operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["Order"], Field(None, description="The details of the requested order")
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
        ),
    ]


# Enum definitions
class SortOrderEnum(str, Enum):
    """Enum for sortOrder"""

    ASC = "ASC"  # Sort in ascending order by purchase order creation date.
    DESC = "DESC"  # Sort in descending order by purchase order creation date.


class PoItemStateEnum(str, Enum):
    """Enum for poItemState"""

    CANCELLED = "Cancelled"  # Status for order items cancelled by vendors.


class PurchaseOrderStateEnum(str, Enum):
    """Enum for purchaseOrderState"""

    NEW = "New"  # Status of the orders that are newly created.
    ACKNOWLEDGED = "Acknowledged"  # Status of the orders acknowledged by vendors.
    CLOSED = "Closed"  # Status of the orders that are completed.


"""
GetPurchaseOrdersRequest

Request parameters for getPurchaseOrders
"""


class GetPurchaseOrdersRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getPurchaseOrders
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    limit: Annotated[
        Optional[int],
        QueryParam(),
        Field(
            None,
            description="[QUERY] The limit to the number of records returned. Default value is 100 records.",
        ),
    ]

    created_after: Annotated[
        Optional[datetime],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("createdAfter", "created_after"),
            serialization_alias="createdAfter",
            description="[QUERY] Purchase orders that became available after this time will be included in the result. Must be in ISO-8601 date/time format.",
        ),
    ]

    created_before: Annotated[
        Optional[datetime],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("createdBefore", "created_before"),
            serialization_alias="createdBefore",
            description="[QUERY] Purchase orders that became available before this time will be included in the result. Must be in ISO-8601 date/time format.",
        ),
    ]

    sort_order: Annotated[
        Optional[SortOrderEnum],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("sortOrder", "sort_order"),
            serialization_alias="sortOrder",
            description="[QUERY] Sort in ascending or descending order by purchase order creation date.",
        ),
    ]

    next_token: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("nextToken", "next_token"),
            serialization_alias="nextToken",
            description="[QUERY] Used for pagination when there is more purchase orders than the specified result size limit. The token value is returned in the previous API call",
        ),
    ]

    include_details: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("includeDetails", "include_details"),
            serialization_alias="includeDetails",
            description="[QUERY] When true, returns purchase orders with complete details. Otherwise, only purchase order numbers are returned. Default value is true.",
        ),
    ]

    changed_after: Annotated[
        Optional[datetime],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("changedAfter", "changed_after"),
            serialization_alias="changedAfter",
            description="[QUERY] Purchase orders that changed after this timestamp will be included in the result. Must be in ISO-8601 date/time format.",
        ),
    ]

    changed_before: Annotated[
        Optional[datetime],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("changedBefore", "changed_before"),
            serialization_alias="changedBefore",
            description="[QUERY] Purchase orders that changed before this timestamp will be included in the result. Must be in ISO-8601 date/time format.",
        ),
    ]

    po_item_state: Annotated[
        Optional[PoItemStateEnum],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("poItemState", "po_item_state"),
            serialization_alias="poItemState",
            description="[QUERY] Current state of the purchase order item. If this value is Cancelled, this API will return purchase orders which have one or more items cancelled by Amazon with updated item quantity as zero.",
        ),
    ]

    is_p_o_changed: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("isPOChanged", "is_p_o_changed"),
            serialization_alias="isPOChanged",
            description="[QUERY] When true, returns purchase orders which were modified after the order was placed. Vendors are required to pull the changed purchase order and fulfill the updated purchase order and not the original one. Default value is false.",
        ),
    ]

    purchase_order_state: Annotated[
        Optional[PurchaseOrderStateEnum],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("purchaseOrderState", "purchase_order_state"),
            serialization_alias="purchaseOrderState",
            description="[QUERY] Filters purchase orders based on the purchase order state.",
        ),
    ]

    ordering_vendor_code: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("orderingVendorCode", "ordering_vendor_code"),
            serialization_alias="orderingVendorCode",
            description="[QUERY] Filters purchase orders based on the specified ordering vendor code. This value should be same as 'sellingParty.partyId' in the purchase order. If not included in the filter, all purchase orders for all of the vendor codes that exist in the vendor group used to authorize the API client application are returned.",
        ),
    ]


"""
Pagination

The pagination elements required to retrieve the remaining data.
"""


class Pagination(SpApiBaseModel):
    """The pagination elements required to retrieve the remaining data."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    next_token: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("nextToken", "next_token"),
            serialization_alias="nextToken",
            description="A generated string used to pass information to your next request. If NextToken is returned, pass the value of NextToken to the next request. If NextToken is not returned, there are no more purchase order items to return.",
        ),
    ]


"""
OrderList

A list of orders returned as response.
"""


class OrderList(SpApiBaseModel):
    """A list of orders returned as response."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    pagination: Annotated[
        Optional["Pagination"],
        Field(
            None,
        ),
    ]

    orders: Annotated[
        Optional[List["Order"]],
        Field(None, description="Represents an individual order within the OrderList."),
    ]


"""
GetPurchaseOrdersResponse

The response schema for the getPurchaseOrders operation.
"""


class GetPurchaseOrdersResponse(SpApiBaseModel):
    """The response schema for the getPurchaseOrders operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["OrderList"], Field(None, description="A list of orders.")
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
        ),
    ]


# Enum definitions
class SortOrderEnum(str, Enum):
    """Enum for sortOrder"""

    ASC = "ASC"  # Sort in ascending order by purchase order creation date.
    DESC = "DESC"  # Sort in descending order by purchase order creation date.


class PurchaseOrderStatusEnum(str, Enum):
    """Enum for purchaseOrderStatus"""

    OPEN = "OPEN"  # Buyer has not yet received all of the items in the purchase order.
    CLOSED = "CLOSED"  # Buyer has received all of the items in the purchase order.


class ItemConfirmationStatusEnum(str, Enum):
    """Enum for itemConfirmationStatus"""

    ACCEPTED = "ACCEPTED"  # Provides a list of orders that has at least one item fully accepted by vendors.
    PARTIALLY_ACCEPTED = "PARTIALLY_ACCEPTED"  # Provides a list of orders that has at least one item partially accepted by vendors.
    REJECTED = "REJECTED"  # Provides a list of orders that has at least one item rejected by vendors.
    UNCONFIRMED = "UNCONFIRMED"  # Provides a list of orders that has at least one item yet to be confirmed by vendors.


class ItemReceiveStatusEnum(str, Enum):
    """Enum for itemReceiveStatus"""

    NOT_RECEIVED = "NOT_RECEIVED"  # Provides a list of orders that have at least one item not received by the buyer.
    PARTIALLY_RECEIVED = "PARTIALLY_RECEIVED"  # Provides a list of orders that have at least one item not received by the buyer.
    RECEIVED = "RECEIVED"  # Provides a list of orders that have at least one item fully received by the buyer.


"""
GetPurchaseOrdersStatusRequest

Request parameters for getPurchaseOrdersStatus
"""


class GetPurchaseOrdersStatusRequest(GetRequestSerializer, RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for getPurchaseOrdersStatus
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    limit: Annotated[
        Optional[int],
        QueryParam(),
        Field(
            None,
            description="[QUERY] The limit to the number of records returned. Default value is 100 records.",
        ),
    ]

    sort_order: Annotated[
        Optional[SortOrderEnum],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("sortOrder", "sort_order"),
            serialization_alias="sortOrder",
            description="[QUERY] Sort in ascending or descending order by purchase order creation date.",
        ),
    ]

    next_token: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("nextToken", "next_token"),
            serialization_alias="nextToken",
            description="[QUERY] Used for pagination when there are more purchase orders than the specified result size limit.",
        ),
    ]

    created_after: Annotated[
        Optional[datetime],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("createdAfter", "created_after"),
            serialization_alias="createdAfter",
            description="[QUERY] Purchase orders that became available after this timestamp will be included in the result. Must be in ISO-8601 date/time format.",
        ),
    ]

    created_before: Annotated[
        Optional[datetime],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("createdBefore", "created_before"),
            serialization_alias="createdBefore",
            description="[QUERY] Purchase orders that became available before this timestamp will be included in the result. Must be in ISO-8601 date/time format.",
        ),
    ]

    updated_after: Annotated[
        Optional[datetime],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("updatedAfter", "updated_after"),
            serialization_alias="updatedAfter",
            description="[QUERY] Purchase orders for which the last purchase order update happened after this timestamp will be included in the result. Must be in ISO-8601 date/time format.",
        ),
    ]

    updated_before: Annotated[
        Optional[datetime],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("updatedBefore", "updated_before"),
            serialization_alias="updatedBefore",
            description="[QUERY] Purchase orders for which the last purchase order update happened before this timestamp will be included in the result. Must be in ISO-8601 date/time format.",
        ),
    ]

    purchase_order_number: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices(
                "purchaseOrderNumber", "purchase_order_number"
            ),
            serialization_alias="purchaseOrderNumber",
            description="[QUERY] Provides purchase order status for the specified purchase order number.",
        ),
    ]

    purchase_order_status: Annotated[
        Optional[PurchaseOrderStatusEnum],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices(
                "purchaseOrderStatus", "purchase_order_status"
            ),
            serialization_alias="purchaseOrderStatus",
            description="[QUERY] Filters purchase orders based on the specified purchase order status. If not included in filter, this will return purchase orders for all statuses.",
        ),
    ]

    item_confirmation_status: Annotated[
        Optional[ItemConfirmationStatusEnum],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices(
                "itemConfirmationStatus", "item_confirmation_status"
            ),
            serialization_alias="itemConfirmationStatus",
            description="[QUERY] Filters purchase orders based on their item confirmation status. If the item confirmation status is not included in the filter, purchase orders for all confirmation statuses are included.",
        ),
    ]

    item_receive_status: Annotated[
        Optional[ItemReceiveStatusEnum],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("itemReceiveStatus", "item_receive_status"),
            serialization_alias="itemReceiveStatus",
            description="[QUERY] Filters purchase orders based on the purchase order's item receive status. If the item receive status is not included in the filter, purchase orders for all receive statuses are included.",
        ),
    ]

    ordering_vendor_code: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("orderingVendorCode", "ordering_vendor_code"),
            serialization_alias="orderingVendorCode",
            description="[QUERY] Filters purchase orders based on the specified ordering vendor code. This value should be same as 'sellingParty.partyId' in the purchase order. If not included in filter, all purchase orders for all the vendor codes that exist in the vendor group used to authorize API client application are returned.",
        ),
    ]

    ship_to_party_id: Annotated[
        Optional[str],
        QueryParam(),
        Field(
            None,
            validation_alias=AliasChoices("shipToPartyId", "ship_to_party_id"),
            serialization_alias="shipToPartyId",
            description="[QUERY] Filters purchase orders for a specific buyer's Fulfillment Center/warehouse by providing ship to location id here. This value should be same as 'shipToParty.partyId' in the purchase order. If not included in filter, this will return purchase orders for all the buyer's warehouses used for vendor group purchase orders.",
        ),
    ]


ItemStatus = List["OrderItemStatus"]
"""Detailed description of items order status."""


# Enum definitions
class PurchaseOrderStatusEnum(str, Enum):
    """Enum for purchaseOrderStatus"""

    OPEN = "OPEN"  # Buyer has not yet received all of the items in the purchase order.
    CLOSED = "CLOSED"  # Buyer has received all of the items in the purchase order.


"""
OrderStatus

Current status of a purchase order.
"""


class OrderStatus(SpApiBaseModel):
    """Current status of a purchase order."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    purchase_order_number: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices(
                "purchaseOrderNumber", "purchase_order_number"
            ),
            serialization_alias="purchaseOrderNumber",
            description="The buyer's purchase order number for this order. Formatting Notes: 8-character alpha-numeric code.",
        ),
    ]

    purchase_order_status: Annotated[
        PurchaseOrderStatusEnum,
        Field(
            ...,
            validation_alias=AliasChoices(
                "purchaseOrderStatus", "purchase_order_status"
            ),
            serialization_alias="purchaseOrderStatus",
            description="The status of the buyer's purchase order for this order.",
        ),
    ]

    purchase_order_date: Annotated[
        datetime,
        Field(
            ...,
            validation_alias=AliasChoices("purchaseOrderDate", "purchase_order_date"),
            serialization_alias="purchaseOrderDate",
            description="The date the purchase order was placed. Must be in ISO-8601 date/time format.",
        ),
    ]

    last_updated_date: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices("lastUpdatedDate", "last_updated_date"),
            serialization_alias="lastUpdatedDate",
            description="The date when the purchase order was last updated. Must be in ISO-8601 date/time format.",
        ),
    ]

    selling_party: Annotated[
        "PartyIdentification",
        Field(
            ...,
            validation_alias=AliasChoices("sellingParty", "selling_party"),
            serialization_alias="sellingParty",
            description="Name/Address and tax details of the selling party.",
        ),
    ]

    ship_to_party: Annotated[
        "PartyIdentification",
        Field(
            ...,
            validation_alias=AliasChoices("shipToParty", "ship_to_party"),
            serialization_alias="shipToParty",
            description="Name/Address and tax details of the ship to party. Find a list of fulfillment center addresses for a region on the [Resources page of Amazon Vendor Central](https://vendorcentral.amazon.com/hz/vendor/members/support/help/node/GPZ88XH8HQM97ZV6).",
        ),
    ]

    item_status: Annotated[
        "ItemStatus",
        Field(
            ...,
            validation_alias=AliasChoices("itemStatus", "item_status"),
            serialization_alias="itemStatus",
            description="Detailed order status.",
        ),
    ]


"""
OrderListStatus

A list of order statuses.
"""


class OrderListStatus(SpApiBaseModel):
    """A list of order statuses."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    pagination: Annotated[
        Optional["Pagination"],
        Field(
            None,
        ),
    ]

    orders_status: Annotated[
        Optional[List["OrderStatus"]],
        Field(
            None,
            validation_alias=AliasChoices("ordersStatus", "orders_status"),
            serialization_alias="ordersStatus",
            description="Represents an order status within the OrderListStatus.",
        ),
    ]


"""
GetPurchaseOrdersStatusResponse

The response schema for the getPurchaseOrdersStatus operation.
"""


class GetPurchaseOrdersStatusResponse(SpApiBaseModel):
    """The response schema for the getPurchaseOrdersStatus operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["OrderListStatus"],
        Field(None, description="Current status of list of purchase orders."),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
        ),
    ]


# Enum definitions
class AcknowledgementCodeEnum(str, Enum):
    """Enum for acknowledgementCode"""

    ACCEPTED = "Accepted"  # Vendor accepts to fulfill the order item(s).
    BACKORDERED = "Backordered"  # Vendor placed a backorder to fulfill the original order and provides a scheduledShipDate or scheduledDeliveryDate which is different than the expectedShipDate or expectedDeliveryDate provided in the purchase order.
    REJECTED = "Rejected"  # Vendor rejects to fulfill the order item(s).


class RejectionReasonEnum(str, Enum):
    """Enum for rejectionReason"""

    TEMPORARILY_UNAVAILABLE = (
        "TemporarilyUnavailable"  # Items are currently not available.
    )
    INVALID_PRODUCT_IDENTIFIER = (
        "InvalidProductIdentifier"  # Item cannot be found with the provided identifier.
    )
    OBSOLETE_PRODUCT = "ObsoleteProduct"  # Item is no longer sold.


"""
OrderItemAcknowledgement

Represents the acknowledgement details for an individual order item, including the acknowledgement code, acknowledged quantity, scheduled ship and delivery dates, and rejection reason (if applicable).
"""


class OrderItemAcknowledgement(SpApiBaseModel):
    """Represents the acknowledgement details for an individual order item, including the acknowledgement code, acknowledged quantity, scheduled ship and delivery dates, and rejection reason (if applicable)."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    acknowledgement_code: Annotated[
        AcknowledgementCodeEnum,
        Field(
            ...,
            validation_alias=AliasChoices(
                "acknowledgementCode", "acknowledgement_code"
            ),
            serialization_alias="acknowledgementCode",
            description="This indicates the acknowledgement code.",
        ),
    ]

    acknowledged_quantity: Annotated[
        "ItemQuantity",
        Field(
            ...,
            validation_alias=AliasChoices(
                "acknowledgedQuantity", "acknowledged_quantity"
            ),
            serialization_alias="acknowledgedQuantity",
            description="Details of quantity acknowledged with the above acknowledgement code.",
        ),
    ]

    scheduled_ship_date: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices("scheduledShipDate", "scheduled_ship_date"),
            serialization_alias="scheduledShipDate",
            description="Estimated ship date per line item. Must be in ISO-8601 date/time format.",
        ),
    ]

    scheduled_delivery_date: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices(
                "scheduledDeliveryDate", "scheduled_delivery_date"
            ),
            serialization_alias="scheduledDeliveryDate",
            description="Estimated delivery date per line item. Must be in ISO-8601 date/time format.",
        ),
    ]

    rejection_reason: Annotated[
        Optional[RejectionReasonEnum],
        Field(
            None,
            validation_alias=AliasChoices("rejectionReason", "rejection_reason"),
            serialization_alias="rejectionReason",
            description="Indicates the reason for rejection.",
        ),
    ]


"""
OrderAcknowledgementItem

Details of the item being acknowledged.
"""


class OrderAcknowledgementItem(SpApiBaseModel):
    """Details of the item being acknowledged."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    item_sequence_number: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("itemSequenceNumber", "item_sequence_number"),
            serialization_alias="itemSequenceNumber",
            description="Line item sequence number for the item.",
        ),
    ]

    amazon_product_identifier: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "amazonProductIdentifier", "amazon_product_identifier"
            ),
            serialization_alias="amazonProductIdentifier",
            description="Amazon Standard Identification Number (ASIN) of an item.",
        ),
    ]

    vendor_product_identifier: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "vendorProductIdentifier", "vendor_product_identifier"
            ),
            serialization_alias="vendorProductIdentifier",
            description="The vendor selected product identification of the item. Should be the same as was sent in the purchase order.",
        ),
    ]

    ordered_quantity: Annotated[
        "ItemQuantity",
        Field(
            ...,
            validation_alias=AliasChoices("orderedQuantity", "ordered_quantity"),
            serialization_alias="orderedQuantity",
            description="The quantity of this item ordered.",
        ),
    ]

    net_cost: Annotated[
        Optional["Money"],
        Field(
            None,
            validation_alias=AliasChoices("netCost", "net_cost"),
            serialization_alias="netCost",
            description="The net cost of an item per each or weight unit that must match the cost on the invoice. This is a required field. If left blank, Amazon systems will reject the file. Price information must not be zero or negative.",
        ),
    ]

    list_price: Annotated[
        Optional["Money"],
        Field(
            None,
            validation_alias=AliasChoices("listPrice", "list_price"),
            serialization_alias="listPrice",
            description="The list price of an item per each or weight unit. Required only if a vendor sells books at list price.",
        ),
    ]

    discount_multiplier: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("discountMultiplier", "discount_multiplier"),
            serialization_alias="discountMultiplier",
            description="The discount multiplier that should be applied to the price if a vendor sells books with a list price. This is a multiplier factor to arrive at a final discounted price. A multiplier of .90 would be the factor if a 10% discount is given.",
        ),
    ]

    item_acknowledgements: Annotated[
        List["OrderItemAcknowledgement"],
        Field(
            ...,
            validation_alias=AliasChoices(
                "itemAcknowledgements", "item_acknowledgements"
            ),
            serialization_alias="itemAcknowledgements",
            description="This is used to indicate acknowledged quantity.",
        ),
    ]


"""
OrderAcknowledgement

Represents an acknowledgement for an order, including the purchase order number, selling party details, acknowledgement date, and a list of acknowledged items.
"""


class OrderAcknowledgement(SpApiBaseModel):
    """Represents an acknowledgement for an order, including the purchase order number, selling party details, acknowledgement date, and a list of acknowledged items."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    purchase_order_number: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices(
                "purchaseOrderNumber", "purchase_order_number"
            ),
            serialization_alias="purchaseOrderNumber",
            description="The purchase order number. Formatting Notes: 8-character alpha-numeric code.",
        ),
    ]

    selling_party: Annotated[
        "PartyIdentification",
        Field(
            ...,
            validation_alias=AliasChoices("sellingParty", "selling_party"),
            serialization_alias="sellingParty",
            description="Name, address and tax details of the party receiving a shipment of products.",
        ),
    ]

    acknowledgement_date: Annotated[
        datetime,
        Field(
            ...,
            validation_alias=AliasChoices(
                "acknowledgementDate", "acknowledgement_date"
            ),
            serialization_alias="acknowledgementDate",
            description="The date and time when the purchase order is acknowledged, in ISO-8601 date/time format.",
        ),
    ]

    items: Annotated[
        List["OrderAcknowledgementItem"],
        Field(
            ...,
            description="A list of the items being acknowledged with associated details.",
        ),
    ]


"""
OrderItemStatus

Represents the current status of an order item, including acknowledgement and receiving details.
"""


class OrderItemStatus(SpApiBaseModel):
    """Represents the current status of an order item, including acknowledgement and receiving details."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    item_sequence_number: Annotated[
        str,
        Field(
            ...,
            validation_alias=AliasChoices("itemSequenceNumber", "item_sequence_number"),
            serialization_alias="itemSequenceNumber",
            description="Numbering of the item on the purchase order. The first item will be 1, the second 2, and so on.",
        ),
    ]

    buyer_product_identifier: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "buyerProductIdentifier", "buyer_product_identifier"
            ),
            serialization_alias="buyerProductIdentifier",
            description="Buyer's Standard Identification Number (ASIN) of an item.",
        ),
    ]

    vendor_product_identifier: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices(
                "vendorProductIdentifier", "vendor_product_identifier"
            ),
            serialization_alias="vendorProductIdentifier",
            description="The vendor selected product identification of the item.",
        ),
    ]

    net_cost: Annotated[
        Optional["Money"],
        Field(
            None,
            validation_alias=AliasChoices("netCost", "net_cost"),
            serialization_alias="netCost",
            description="The net cost of an item per each or weight unit.",
        ),
    ]

    list_price: Annotated[
        Optional["Money"],
        Field(
            None,
            validation_alias=AliasChoices("listPrice", "list_price"),
            serialization_alias="listPrice",
            description="The list price of an item per each or weight unit.",
        ),
    ]

    ordered_quantity: Annotated[
        Optional[Dict[str, Any]],
        Field(
            None,
            validation_alias=AliasChoices("orderedQuantity", "ordered_quantity"),
            serialization_alias="orderedQuantity",
            description="Ordered quantity information.",
        ),
    ]

    acknowledgement_status: Annotated[
        Optional[Dict[str, Any]],
        Field(
            None,
            validation_alias=AliasChoices(
                "acknowledgementStatus", "acknowledgement_status"
            ),
            serialization_alias="acknowledgementStatus",
            description="Acknowledgement status information.",
        ),
    ]

    receiving_status: Annotated[
        Optional[Dict[str, Any]],
        Field(
            None,
            validation_alias=AliasChoices("receivingStatus", "receiving_status"),
            serialization_alias="receivingStatus",
            description="Item receive status at the buyer's warehouse.",
        ),
    ]


"""
OrderedQuantityDetails

Details of item quantity ordered.
"""


class OrderedQuantityDetails(SpApiBaseModel):
    """Details of item quantity ordered."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    updated_date: Annotated[
        Optional[datetime],
        Field(
            None,
            validation_alias=AliasChoices("updatedDate", "updated_date"),
            serialization_alias="updatedDate",
            description="The date when the line item quantity was updated by buyer. Must be in ISO-8601 date/time format.",
        ),
    ]

    ordered_quantity: Annotated[
        Optional["ItemQuantity"],
        Field(
            None,
            validation_alias=AliasChoices("orderedQuantity", "ordered_quantity"),
            serialization_alias="orderedQuantity",
            description="Item quantity ordered.",
        ),
    ]

    cancelled_quantity: Annotated[
        Optional["ItemQuantity"],
        Field(
            None,
            validation_alias=AliasChoices("cancelledQuantity", "cancelled_quantity"),
            serialization_alias="cancelledQuantity",
            description="Item quantity ordered.",
        ),
    ]


"""
SubmitAcknowledgementRequestBody

The request schema for the submitAcknowledgment operation.
"""


class SubmitAcknowledgementRequestBody(SpApiBaseModel):
    """The request schema for the submitAcknowledgment operation."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    acknowledgements: Annotated[
        Optional[List["OrderAcknowledgement"]],
        Field(None, description="An array of order acknowledgements to be submitted."),
    ]


"""
SubmitAcknowledgementRequest

Request parameters for submitAcknowledgement
"""


class SubmitAcknowledgementRequest(RequestsBaseModel):
    """
    Request parameters for operation ID:
    Request parameters for submitAcknowledgement
    """

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    body: Annotated[
        "SubmitAcknowledgementRequestBody",
        BodyParam(),
        Field(
            ...,
            description="[BODY] Submits acknowledgements for one or more purchase orders from a vendor.",
        ),
    ]


"""
TransactionId

Response containing the transaction ID.
"""


class TransactionId(SpApiBaseModel):
    """Response containing the transaction ID."""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    transaction_id: Annotated[
        Optional[str],
        Field(
            None,
            validation_alias=AliasChoices("transactionId", "transaction_id"),
            serialization_alias="transactionId",
            description="GUID assigned by Amazon to identify this transaction. This value can be used with the Transaction Status API to return the status of this transaction.",
        ),
    ]


"""
SubmitAcknowledgementResponse

The response schema for the submitAcknowledgement operation
"""


class SubmitAcknowledgementResponse(SpApiBaseModel):
    """The response schema for the submitAcknowledgement operation"""

    model_config = ConfigDict(
        populate_by_name=True, serialize_by_alias=True, arbitrary_types_allowed=True
    )

    payload: Annotated[
        Optional["TransactionId"],
        Field(None, description="The payload for the submitAcknowledgement operation."),
    ]

    errors: Annotated[
        Optional["ErrorList"],
        Field(
            None,
        ),
    ]


# Rebuild models to resolve forward references
GetPurchaseOrdersResponse.model_rebuild()
GetPurchaseOrderResponse.model_rebuild()
OrderList.model_rebuild()
Pagination.model_rebuild()
Order.model_rebuild()
OrderDetails.model_rebuild()
ImportDetails.model_rebuild()
PartyIdentification.model_rebuild()
TaxRegistrationDetails.model_rebuild()
Address.model_rebuild()
OrderItem.model_rebuild()
Money.model_rebuild()
SubmitAcknowledgementResponse.model_rebuild()
TransactionId.model_rebuild()
SubmitAcknowledgementRequestBody.model_rebuild()
OrderAcknowledgement.model_rebuild()
OrderAcknowledgementItem.model_rebuild()
OrderItemAcknowledgement.model_rebuild()
ItemQuantity.model_rebuild()
GetPurchaseOrdersStatusResponse.model_rebuild()
OrderListStatus.model_rebuild()
OrderStatus.model_rebuild()
OrderItemStatus.model_rebuild()
OrderedQuantityDetails.model_rebuild()
AcknowledgementStatusDetails.model_rebuild()
Error.model_rebuild()
GetPurchaseOrdersRequest.model_rebuild()
GetPurchaseOrderRequest.model_rebuild()
SubmitAcknowledgementRequest.model_rebuild()
GetPurchaseOrdersStatusRequest.model_rebuild()
