"""
Country	marketplaceId	Country code
Canada	A2EUQ1WTGCTBG2	CA
United States of America	ATVPDKIKX0DER	US
Mexico	A1AM78C64UM0Y8	MX
Brazil	A2Q3Y263D00KWC	BR
Europe

Country	marketplaceId	Country code
Spain	A1RKKUPIHCS9HS	ES
United Kingdom	A1F83G8C2ARO7P	GB
France	A13V1IB3VIYZZH	FR
Netherlands	A1805IZSGTT6HS	NL
Germany	A1PA6795UKMFR9	DE
Italy	APJ6JRA9NG5V4	IT
Sweden	A2NODRKZP88ZB9	SE
Poland	A1C3SOZRARQ6R3	PL
Turkey	A33AVAJ2PDY3EV	TR
United Arab Emirates	A2VIGQ35RCS4UG	AE
India	A21TJRUUN4KGV	IN
Far East

Country	marketplaceId	Country code
Singapore	A19VAU5U5O7RUS	SG
Australia	A39IBJ37TRP1C6	AU
Japan	A1VC38T7YXB528	JP
"""
from enum import Enum


class Marketplaces(Enum):
    """Enumeration for MWS marketplaces, containing endpoints and marketplace IDs.
    Example, endpoint and ID for UK marketplace:
        endpoint = Marketplaces.UK.endpoint
        marketplace_id = Marketplaces.UK.marketplace_id
    """

    AE = ("https://sellingpartnerapi-eu.amazon.com", "A2VIGQ35RCS4UG")
    DE = ("https://sellingpartnerapi-eu.amazon.com", "A1PA6795UKMFR9")
    EG = ("https://sellingpartnerapi-eu.amazon.com", "ARBP9OOSHTCHU")
    ES = ("https://sellingpartnerapi-eu.amazon.com", "A1RKKUPIHCS9HS")
    FR = ("https://sellingpartnerapi-eu.amazon.com", "A13V1IB3VIYZZH")
    GB = ("https://sellingpartnerapi-eu.amazon.com", "A1F83G8C2ARO7P")
    IN = ("https://sellingpartnerapi-eu.amazon.com", "A21TJRUUN4KGV")
    IT = ("https://sellingpartnerapi-eu.amazon.com", "APJ6JRA9NG5V4")
    NL = ("https://sellingpartnerapi-eu.amazon.com", "A1805IZSGTT6HS")
    SA = ("https://sellingpartnerapi-eu.amazon.com", "A17E79C6D8DWNP")
    SE = ("https://sellingpartnerapi-eu.amazon.com", "A2NODRKZP88ZB9")
    TR = ("https://sellingpartnerapi-eu.amazon.com", "A33AVAJ2PDY3EV")
    UK = ("https://sellingpartnerapi-eu.amazon.com", "A1F83G8C2ARO7P")  # alias for GB
    
    AU = ("https://sellingpartnerapi-fe.amazon.com", "A39IBJ37TRP1C6")
    JP = ("https://sellingpartnerapi-fe.amazon.com", "A1VC38T7YXB528")
    SG = ("https://sellingpartnerapi-fe.amazon.com", "A19VAU5U5O7RUS")

    US = ("https://sellingpartnerapi-na.amazon.com", "ATVPDKIKX0DER")
    BR = ("https://sellingpartnerapi-na.amazon.com", "A2Q3Y263D00KWC")
    CA = ("https://sellingpartnerapi-na.amazon.com", "A2EUQ1WTGCTBG2")
    MX = ("https://sellingpartnerapi-na.amazon.com", "A1AM78C64UM0Y8")

    def __init__(self, endpoint, marketplace_id):
        """Easy dot access like: Marketplaces.endpoint ."""
        self.endpoint = endpoint
        self.marketplace_id = marketplace_id

