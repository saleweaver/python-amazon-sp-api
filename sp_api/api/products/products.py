import urllib.parse

from sp_api.api.products.models.get_pricing_response import GetPricingResponse
from sp_api.base import Client, Marketplaces, sp_endpoint


class Products(Client):
    """
    :link: https://github.com/amzn/selling-partner-api-docs/blob/main/references/product-pricing-api/productPricingV0.md
    """

    def __init__(self, marketplace=Marketplaces.US, *, refresh_token=None, account='default', credentials=None):
        super().__init__(marketplace, refresh_token, account, credentials)

    @sp_endpoint('/products/pricing/v0/price', method='GET')
    def get_product_pricing_for_skus(self, seller_sku_list: [str], item_condition=None, **kwargs) -> GetPricingResponse:
        """
        get_product_pricing_for_skus(self, seller_sku_list: [str], item_condition: str = None, **kwargs) -> GetPricingResponse
        Returns pricing information for a seller's offer listings based on SKU.

        **Usage Plan:**

        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       1
        ======================================  ==============

        Args:

            seller_sku_list: [str]
            item_condition: str ("New", "Used", "Collectible", "Refurbished", "Club")
            **kwargs:

        Returns:
            GetPricingResponse:
        """
        if item_condition is not None:
            kwargs['ItemCondition'] = item_condition

        return self._create_get_pricing_request(seller_sku_list, 'Sku', **kwargs)

    @sp_endpoint('/products/pricing/v0/price', method='GET')
    def get_product_pricing_for_asins(self, asin_list: [str], item_condition=None, **kwargs) -> GetPricingResponse:
        """
        get_product_pricing_for_asins(self, asin_list: [str], item_condition=None, **kwargs) -> GetPricingResponse
        Returns pricing information for a seller's offer listings based on ASIN.

        **Usage Plan:**

        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       1
        ======================================  ==============


        :param asin_list: [str]
        :param item_condition: str ("New", "Used", "Collectible", "Refurbished", "Club")
           Filters the offer listings based on item condition. Possible values: New, Used, Collectible, Refurbished, Club.
           Available values : New, Used, Collectible, Refurbished, Club
        :param kwargs:
        :return:
        """
        if item_condition is not None:
            kwargs['ItemCondition'] = item_condition

        return self._create_get_pricing_request(asin_list, 'Asin', **kwargs)

    @sp_endpoint('/products/pricing/v0/competitivePrice', method='GET')
    def get_competitive_pricing_for_skus(self, seller_sku_list: [str], **kwargs):
        """
        get_competitive_pricing_for_skus(self, seller_sku_list, **kwargs)
        Returns competitive pricing information for a seller's offer listings based on Seller Sku

        **Usage Plan:**

        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       1
        ======================================  ==============


        :param seller_sku_list: [str]
        :param kwargs:
        :return:
        """
        return self._create_get_pricing_request(seller_sku_list, 'Sku', **kwargs)

    @sp_endpoint('/products/pricing/v0/competitivePrice', method='GET')
    def get_competitive_pricing_for_asins(self, asin_list: [str], **kwargs) -> GetPricingResponse:
        """
        get_competitive_pricing_for_asins(self, asin_list, **kwargs) -> GetPricingResponse
        Returns competitive pricing information for a seller's offer listings based on ASIN

        **Usage Plan:**

        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       1
        ======================================  ==============


        :param asin_list: [str]
        :param kwargs:
        :return:

        """
        return self._create_get_pricing_request(asin_list, 'Asin', **kwargs)

    def _create_get_pricing_request(self, item_list, item_type, **kwargs):
        """
        Returns pricing information for a seller's offer listings based on seller SKU or ASIN.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 1 |

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        :param item_list:
        :param item_type:
        :param kwargs:
        :return:
        """
        return GetPricingResponse(
            **self._request(kwargs.pop('path'),
                            params={**{f"{item_type}s": ','.join(
                                [urllib.parse.quote_plus(s) for s in item_list])},
                                    'ItemType': item_type,
                                    **({'ItemCondition': kwargs.pop('ItemCondition')} if 'ItemCondition' in kwargs else {}),
                                    'MarketplaceId': self.marketplace_id}).json())
