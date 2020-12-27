from enum import Enum


class Granularity(Enum):
    HOUR = 'Hour'
    DAY = 'Day'
    WEEK = 'Week'
    MONTH = 'Month'
    YEAR = 'Year'
    TOTAL = 'Total'


class BuyerType(Enum):
    B2B = 'B2B' # Business to business.
    B2C = 'B2C' # Business to customer.
    ALL = 'All' # Both of above


class FirstDayOfWeek(Enum):
    MO = 'Monday'
    SU = 'Sunday'


