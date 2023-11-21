
from enum import Enum


class IncludedData(str, Enum):
    SUMMARIES = 'summaries' # Summary details of the listing item.
    ATTRIBUTES = 'attributes' # JSON object containing structured listing item attribute data keyed by attribute name.
    ISSUES = 'issues' # Issues associated with the listing item.
    OFFERS = 'offers' # Current offers for the listing item.
    FULFILLMENT_AVAILABILITY = 'fulfillmentAvailability' # Fulfillment availability details for the listing item.
    PROCUREMENT = 'procurement' # Vendor procurement details for the listing item.
