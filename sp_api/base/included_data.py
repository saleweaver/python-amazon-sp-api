from enum import Enum


class IncludedData(str, Enum):
    """
    Use ListingItemsIncludedData or CatalogItemsIncludedData instead.
    """

    #: Summary details of the listing item.
    SUMMARIES = "summaries"

    #: JSON object containing structured listing item attribute data keyed by attribute name.
    ATTRIBUTES = "attributes"

    #: Issues associated with the listing item.
    ISSUES = "issues"

    #: Current offers for the listing item.
    OFFERS = "offers"

    #: Fulfillment availability details for the listing item.
    FULFILLMENT_AVAILABILITY = "fulfillmentAvailability"

    #: Vendor procurement details for the listing item.
    PROCUREMENT = "procurement"

    #: Dimensions for an item in the Amazon catalog.
    DIMENSIONS = "dimensions"

    #: Identifiers associated with the item in the Amazon catalog, such as UPC and EAN identifiers.
    IDENTIFIERS = "identifiers"

    #: Images for an item in the Amazon catalog.
    IMAGES = "images"

    #: Product types associated with the Amazon catalog item.
    PRODUCT_TYPES = "productTypes"

    #: Relationship details of an Amazon catalog item (for example, variations).
    RELATIONSHIPS = "relationships"

    #: Sales ranks of an Amazon catalog item.
    SALES_RANKS = "salesRanks"

    #: Vendor details associated with an Amazon catalog item. Vendor details are available to vendors only.
    VENDOR_DETAILS = "vendorDetails"


class ListingItemsIncludedData(str, Enum):

    #: Summary details of the listing item.
    SUMMARIES = "summaries"

    #: JSON object containing structured listing item attribute data keyed by attribute name.
    ATTRIBUTES = "attributes"

    #: Issues associated with the listing item.
    ISSUES = "issues"

    #: Current offers for the listing item.
    OFFERS = "offers"

    #: Fulfillment availability details for the listing item.
    FULFILLMENT_AVAILABILITY = "fulfillmentAvailability"

    #: Vendor procurement details for the listing item.
    PROCUREMENT = "procurement"


class CatalogItemsIncludedData(str, Enum):

    #: A JSON object containing structured item attribute data keyed by attribute name.
    ATTRIBUTES = "attributes"

    #: Dimensions for an item in the Amazon catalog.
    DIMENSIONS = "dimensions"

    #: Identifiers associated with the item in the Amazon catalog, such as UPC and EAN identifiers.
    IDENTIFIERS = "identifiers"

    #: Images for an item in the Amazon catalog.
    IMAGES = "images"

    #: Product types associated with the Amazon catalog item.
    PRODUCT_TYPES = "productTypes"

    #: Relationship details of an Amazon catalog item (for example, variations).
    RELATIONSHIPS = "relationships"

    #: Sales ranks of an Amazon catalog item.
    SALES_RANKS = "salesRanks"

    #: Summary details of an Amazon catalog item.
    SUMMARIES = "summaries"

    #: Vendor details associated with an Amazon catalog item. Vendor details are available to vendors only.
    VENDOR_DETAILS = "vendorDetails"
