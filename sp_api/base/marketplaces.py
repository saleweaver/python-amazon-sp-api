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
import sys
from enum import Enum
import os


class AwsEnv(Enum):
    PRODUCTION = "PRODUCTION"
    SANDBOX = "SANDBOX"


AWS_ENVIRONMENT = os.getenv("AWS_ENV", AwsEnv.PRODUCTION.name)
BASE_URL = "https://sellingpartnerapi"

if AwsEnv(AWS_ENVIRONMENT) == AwsEnv.SANDBOX:
    BASE_URL = "https://sandbox.sellingpartnerapi"


class Marketplaces(Enum):
    """Enumeration for MWS marketplaces, containing endpoints and marketplace IDs.
    Example, endpoint and ID for UK marketplace:
        endpoint = Marketplaces.UK.endpoint
        marketplace_id = Marketplaces.UK.marketplace_id
    """

    AE = ("{}-eu.amazon.com".format(BASE_URL), "A2VIGQ35RCS4UG", "eu-west-1")
    DE = ("{}-eu.amazon.com".format(BASE_URL), "A1PA6795UKMFR9", "eu-west-1")
    PL = ("{}-eu.amazon.com".format(BASE_URL), "A1C3SOZRARQ6R3", "eu-west-1")
    EG = ("{}-eu.amazon.com".format(BASE_URL), "ARBP9OOSHTCHU", "eu-west-1")
    ES = ("{}-eu.amazon.com".format(BASE_URL), "A1RKKUPIHCS9HS", "eu-west-1")
    FR = ("{}-eu.amazon.com".format(BASE_URL), "A13V1IB3VIYZZH", "eu-west-1")
    GB = ("{}-eu.amazon.com".format(BASE_URL), "A1F83G8C2ARO7P", "eu-west-1")
    IN = ("{}-eu.amazon.com".format(BASE_URL), "A21TJRUUN4KGV", "eu-west-1")
    IT = ("{}-eu.amazon.com".format(BASE_URL), "APJ6JRA9NG5V4", "eu-west-1")
    NL = ("{}-eu.amazon.com".format(BASE_URL), "A1805IZSGTT6HS", "eu-west-1")
    SA = ("{}-eu.amazon.com".format(BASE_URL), "A17E79C6D8DWNP", "eu-west-1")
    SE = ("{}-eu.amazon.com".format(BASE_URL), "A2NODRKZP88ZB9", "eu-west-1")
    TR = ("{}-eu.amazon.com".format(BASE_URL), "A33AVAJ2PDY3EV", "eu-west-1")
    UK = ("{}-eu.amazon.com".format(BASE_URL), "A1F83G8C2ARO7P", "eu-west-1")  # alias for GB

    AU = ("{}-fe.amazon.com".format(BASE_URL), "A39IBJ37TRP1C6", "us-west-2")
    JP = ("{}-fe.amazon.com".format(BASE_URL), "A1VC38T7YXB528", "us-west-2")
    SG = ("{}-fe.amazon.com".format(BASE_URL), "A19VAU5U5O7RUS", "us-west-2")

    US = ("{}-na.amazon.com".format(BASE_URL), "ATVPDKIKX0DER", "us-east-1")
    BR = ("{}-na.amazon.com".format(BASE_URL), "A2Q3Y263D00KWC", "us-east-1")
    CA = ("{}-na.amazon.com".format(BASE_URL), "A2EUQ1WTGCTBG2", "us-east-1")
    MX = ("{}-na.amazon.com".format(BASE_URL), "A1AM78C64UM0Y8", "us-east-1")

    def __init__(self, endpoint, marketplace_id, region):
        self.endpoint = endpoint
        self.marketplace_id = marketplace_id
        self.region = region
