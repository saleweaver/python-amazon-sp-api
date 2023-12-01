from enum import Enum


class IdentifiersType(str, Enum):
    ASIN = 'ASIN'       # doc: Amazon Standard Identification Number.
    EAN = 'EAN'         # doc: European Article Number.
    GTIN = 'GTIN'       # doc: Global Trade Item Number.
    ISBN = 'ISBN'       # doc: International Standard Book Number.
    JAN = 'JAN'         # doc: Japanese Article Number.
    MINSAN = 'MINSAN'   # doc: Minsan Code.
    SKU = 'SKU'         # doc: Stock Keeping Unit, a seller-specified identifier for an Amazon listing. Note: Must be accompanied by sellerId.
    UPC = 'UPC'         # doc: Universal Product Code.