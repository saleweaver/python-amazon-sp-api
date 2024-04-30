from typing import List, Dict

from sp_api.base import Client, sp_endpoint, ApiResponse


class ProductPricing(Client):
    """
    ProductPricing SP-API Client
    :link: https://developer-docs.amazon.com/sp-api/docs/product-pricing-api-v2022-05-01-reference

    The Selling Partner API for Pricing helps you programmatically retrieve product pricing and offer pricing information for Amazon Marketplace products.

For more information, refer to the [Product Pricing v2022-05-01 Use Case Guide](https://developer-docs.amazon.com/sp-api/docs/product-pricing-api-v2022-05-01-use-case-guide).
    """

    @sp_endpoint('/batches/products/pricing/2022-05-01/offer/featuredOfferExpectedPrice', method='POST')
    def get_featured_offer_expected_price_batch(self, requests_: List[Dict], **kwargs) -> ApiResponse:
        """
        get_featured_offer_expected_price_batch(self, **kwargs) -> ApiResponse

        Returns the set of responses that correspond to the batched list of up to 40 requests defined in the request
        body. The response for each successful (HTTP status code 200) request in the set includes the computed listing
        price at or below which a seller can expect to become the featured offer (before applicable promotions).
        This is called the featured offer expected price (FOEP). Featured offer is not guaranteed, because competing
        offers may change, and different offers may be featured based on other factors, including fulfillment
        capabilities to a specific customer. The response to an unsuccessful request includes the available error text.

        **Usage Plan:**

        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        .033                                    1
        ======================================  ==============

        Args:
            requests_: [dict] The request associated with the getFeaturedOfferExpectedPriceBatch API call.

        Returns:
            ApiResponse:
        """
    
        return self._request(kwargs.pop('path'),  data={"requests": requests_}, params={**kwargs})

    @sp_endpoint('/batches/products/pricing/2022-05-01/items/competitiveSummary', method='POST')
    def get_competitive_summary(self, requests_: List[Dict], **kwargs) -> ApiResponse:
        """
        get_competitive_summary(self, **kwargs) -> ApiResponse

        Returns the competitive summary response including featured buying options for the ASIN and `marketplaceId` combination.

        **Usage Plan:**

        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        .033                                    1
        ======================================  ==============

        Args:
            requests_: The request associated with the getCompetitiveSummary API call.

        Returns:
            ApiResponse:
        """
    
        return self._request(kwargs.pop('path'), data={"requests": requests_}, params={**kwargs})
