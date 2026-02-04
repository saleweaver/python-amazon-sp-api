from typing import Optional, List, Dict, Union

from sp_api.base import ApiResponse, Client, sp_endpoint
from sp_api.api.products.products_definitions import (
    GetCompetitiveSummaryBatch,
    GetFeaturedOfferExpectedPriceBatch,
)


class ProductsV20220501(Client):
    """
    :links:
        https://github.com/amzn/selling-partner-api-docs/blob/main/references/product-pricing-api/productPricingV0.md
        https://developer-docs.amazon.com/sp-api/docs/product-pricing-api-v2022-05-01-reference
    """

    @sp_endpoint('/batches/products/pricing/2022-05-01/offer/featuredOfferExpectedPrice', method='POST')
    def get_featured_offer_expected_price_batch(self, requests_: Optional[
        Union[List[Dict], GetFeaturedOfferExpectedPriceBatch]], **kwargs) -> ApiResponse:
        """
        get_featured_offer_expected_price_batch(self, requests_, **kwargs) -> ApiResponse
        
        Returns the set of responses that correspond to the batched list of up to 40 requests defined in the request body. The response for each successful (HTTP status code 200) request in the set includes the computed listing price at or below which a seller can expect to become the featured offer (before applicable promotions). This is called the featured offer expected price (FOEP). Featured offer is not guaranteed because competing offers might change. Other offers might be featured based on factors such as fulfillment capabilities to a specific customer. The response to an unsuccessful request includes the available error text.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        0.033                                   1
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                ProductsV20220501().get_featured_offer_expected_price_batch("value")
        
        Args:
            getFeaturedOfferExpectedPriceBatchRequestBody: GetFeaturedOfferExpectedPriceBatchRequest | required The batch of `getFeaturedOfferExpectedPrice` requests.
        
        Returns:
            ApiResponse
        """
        if isinstance(requests_, GetFeaturedOfferExpectedPriceBatch):
            get_featured_offer_expected_price_batch_request = requests_.to_dict()
        else:
            get_featured_offer_expected_price_batch_request = {"requests": requests_}

        return self._request(
            kwargs.pop('path'),
            data=get_featured_offer_expected_price_batch_request,
            params={**kwargs},
            add_marketplace=False
        )

    @sp_endpoint('/batches/products/pricing/2022-05-01/items/competitiveSummary', method='POST')
    def get_competitive_summary_batch(self, requests_: Optional[Union[List[Dict], GetCompetitiveSummaryBatch]], **kwargs) -> ApiResponse:
        """
        get_competitive_summary_batch(self, requests_, **kwargs) -> ApiResponse
        
        Returns the competitive summary response, including featured buying options for the ASIN and `marketplaceId` combination.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        0.033                                   1
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                ProductsV20220501().get_competitive_summary_batch("value")
        
        Args:
            requests: CompetitiveSummaryBatchRequest | required The batch of `getCompetitiveSummary` requests.
        
        Returns:
            ApiResponse
        """
        if isinstance(requests_, GetCompetitiveSummaryBatch):
            get_competitive_summary_batch_request = requests_.to_dict()
        else:
            get_competitive_summary_batch_request = {"requests": requests_}

        return self._request(
            kwargs.pop('path'),
            data=get_competitive_summary_batch_request,
            params={**kwargs},
            add_marketplace=False
        )
