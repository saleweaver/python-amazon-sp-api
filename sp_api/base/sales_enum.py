from enum import Enum


class Granularity(str, Enum):
    HOUR = "Hour"
    DAY = "Day"
    WEEK = "Week"
    MONTH = "Month"
    YEAR = "Year"
    TOTAL = "Total"


class BuyerType(str, Enum):
    B2B = "B2B"  # doc: Business to business.
    B2C = "B2C"  # doc: Business to customer.
    ALL = "All"  # doc: Both of above


class FirstDayOfWeek(str, Enum):
    MO = "Monday"
    SU = "Sunday"
