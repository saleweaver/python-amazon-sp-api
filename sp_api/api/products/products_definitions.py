from enum import Enum
from typing import Optional, List, Dict, Union
from dataclasses import dataclass, asdict


class CompetitiveSummaryIncludedData(Enum):
    FEATURED_BUYING_OPTIONS = "featuredBuyingOptions"
    LOWEST_PRICED_OFFERS = "lowestPricedOffers"
    REFERENCE_PRICES = "referencePrices"


@dataclass
class ItemOffersRequest:
    """Implements definition: https://developer-docs.amazon.com/sp-api/docs/product-pricing-api-v0-reference
    #itemoffersrequest"""

    uri: str
    method: str
    MarketplaceId: str
    ItemCondition: str = None
    CustomerType: str = None
    headers: Dict = None


@dataclass
class GetItemOffersBatchRequest:
    """Implements definition: https://developer-docs.amazon.com/sp-api/docs/product-pricing-api-v0-reference
    #getitemoffersbatchrequest"""

    requests: Optional[List[Union[ItemOffersRequest, Dict]]] = None

    def __post_init__(self):
        self.requests = self.parse_requests(self.requests)

    def to_dict(self):
        return asdict(self)

    @staticmethod
    def parse_requests(requests) -> List[ItemOffersRequest]:
        parsed_requestes = []

        for request in requests:
            if isinstance(request, Dict):
                request = ItemOffersRequest(**request)

            if not isinstance(request, ItemOffersRequest):
                raise TypeError

            parsed_requestes.append(request)

        return parsed_requestes


@dataclass
class ListingOffersRequest:
    """Implements definition: https://developer-docs.amazon.com/sp-api/docs/product-pricing-api-v0-reference
    #listingoffersrequest"""

    uri: str
    MarketplaceId: str
    ItemCondition: str
    method: str = "GET"
    CustomerType: str = "Consumer"


@dataclass
class GetListingOffersBatchRequest:
    """Implements definition: https://developer-docs.amazon.com/sp-api/docs/product-pricing-api-v0-reference
    #getlistingoffersbatchrequest"""

    requests: Optional[List[Union[ListingOffersRequest, Dict]]] = None

    def __post_init__(self):
        self.requests = self.parse_requests(self.requests)

    def to_dict(self):
        return asdict(self)

    @staticmethod
    def parse_requests(requests) -> List[ListingOffersRequest]:
        parsed_requestes = []

        for request in requests:
            if isinstance(request, Dict):
                request = ListingOffersRequest(**request)

            if not isinstance(request, ListingOffersRequest):
                raise TypeError

            parsed_requestes.append(request)

        return parsed_requestes


@dataclass
class FeaturedOfferExpectedPriceRequest:
    """ Implements definition: https://developer-docs.amazon.com/sp-api/docs/product-pricing-api-v2022-05-01-reference
        #FeaturedOfferExpectedPriceRequest """
    marketplaceId: str
    sku: str
    uri: str = "/products/pricing/2022-05-01/offer/featuredOfferExpectedPrice"
    method: str = "GET"


@dataclass
class GetFeaturedOfferExpectedPriceBatch:
    """ Implements definition: https://developer-docs.amazon.com/sp-api/docs/product-pricing-api-v2022-05-01-reference
        #getFeaturedOfferExpectedPriceBatch """
    requests: Optional[List[Union[FeaturedOfferExpectedPriceRequest, Dict]]] = None

    def __post_init__(self):
        self.requests = self.parse_requests(self.requests)

    def to_dict(self):
        return asdict(self)

    @staticmethod
    def parse_requests(requests) -> List[FeaturedOfferExpectedPriceRequest]:
        parsed_requests = []

        for request in requests:
            if isinstance(request, Dict):
                request = FeaturedOfferExpectedPriceRequest(**request)

            if not isinstance(request, FeaturedOfferExpectedPriceRequest):
                raise TypeError

            parsed_requests.append(request)

        return parsed_requests


@dataclass
class CompetitiveSummaryRequest:
    """ Implements definition: https://developer-docs.amazon.com/sp-api/docs/product-pricing-api-v2022-05-01-reference
        #FeaturedOfferExpectedPriceRequest """
    marketplaceId: str
    asin: str
    includedData: List[CompetitiveSummaryIncludedData]
    uri: str = "/products/pricing/2022-05-01/items/competitiveSummary"
    method: str = "GET"


@dataclass
class GetCompetitiveSummaryBatch:
    """ Implements definition: https://developer-docs.amazon.com/sp-api/docs/product-pricing-api-v2022-05-01-reference
        #getCompetitiveSummary """
    requests: Optional[List[Union[CompetitiveSummaryRequest, Dict]]] = None

    def __post_init__(self):
        self.requests = self.parse_requests(self.requests)

    def to_dict(self):
        return asdict(self)

    @staticmethod
    def parse_requests(requests) -> List[CompetitiveSummaryRequest]:
        parsed_requests = []

        for request in requests:
            if isinstance(request, Dict):
                request = CompetitiveSummaryRequest(**request)

            if not isinstance(request, CompetitiveSummaryRequest):
                raise TypeError

            parsed_requests.append(request)

        return parsed_requests
