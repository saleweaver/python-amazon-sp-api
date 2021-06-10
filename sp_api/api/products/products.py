import urllib.parse
from sp_api.base import ApiResponse, Client, fill_query_params, sp_endpoint


class Products(Client):
    """
    :link: https://github.com/amzn/selling-partner-api-docs/blob/main/references/product-pricing-api/productPricingV0.md
    """

    @sp_endpoint('/products/pricing/v0/price', method='GET')
    def get_product_pricing_for_skus(self, seller_sku_list: [str], item_condition=None, **kwargs) -> ApiResponse:
        """
        get_product_pricing_for_skus(self, seller_sku_list: [str], item_condition: str = None, **kwargs) -> ApiResponse
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
            ApiResponse:
        """
        if item_condition is not None:
            kwargs['ItemCondition'] = item_condition

        return self._create_get_pricing_request(seller_sku_list, 'Sku', **kwargs)

    @sp_endpoint('/products/pricing/v0/price', method='GET')
    def get_product_pricing_for_asins(self, asin_list: [str], item_condition=None, **kwargs) -> ApiResponse:
        """
        get_product_pricing_for_asins(self, asin_list: [str], item_condition=None, **kwargs) -> ApiResponse
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
        :return: ApiResponse
        """
        if item_condition is not None:
            kwargs['ItemCondition'] = item_condition

        return self._create_get_pricing_request(asin_list, 'Asin', **kwargs)

    @sp_endpoint('/products/pricing/v0/competitivePrice', method='GET')
    def get_competitive_pricing_for_skus(self, seller_sku_list: [str], **kwargs) -> ApiResponse:
        """
        get_competitive_pricing_for_skus(self, seller_sku_list, **kwargs) -> ApiResponse
        Returns competitive pricing information for a seller's offer listings based on Seller Sku

        **Usage Plan:**

        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       1
        ======================================  ==============


        :param seller_sku_list: [str]
        :param kwargs:
        :return: ApiResponse
        """
        return self._create_get_pricing_request(seller_sku_list, 'Sku', **kwargs)

    @sp_endpoint('/products/pricing/v0/competitivePrice', method='GET')
    def get_competitive_pricing_for_asins(self, asin_list: [str], **kwargs) -> ApiResponse:
        """
        get_competitive_pricing_for_asins(self, asin_list, **kwargs) -> ApiResponse
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

    @sp_endpoint('/products/pricing/v0/listings/{}/offers', method='GET')
    def get_listings_offer(self, seller_sku: str, **kwargs) -> ApiResponse:
        """
        get_listings_offer(self, seller_sku: str, **kwargs) -> ApiResponse
        Returns the lowest priced offers for a single SKU listing

        **Usage Plan:**

        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       1
        ======================================  ==============

        Args:
            :param seller_sku: str
            key ItemCondition: str | Possible values: New, Used, Collectible, Refurbished, Club.
            key MarketplaceId: str

        Returns:
            GetOffersResponse:

        """
        return self._request(fill_query_params(kwargs.pop('path'), seller_sku), params={**kwargs})       

    @sp_endpoint('/products/pricing/v0/items/{}/offers', method='GET')
    def get_item_offers(self, asin: str, **kwargs) -> ApiResponse:
        """
        get_item_offers(self, asin: str, **kwargs) -> ApiResponse
        Returns the lowest priced offers for a single item based on ASIN

        **Usage Plan:**

        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        5                                       10
        ======================================  ==============

        Args:
            :param seller_sku: str
            key ItemCondition: str | Possible values: New, Used, Collectible, Refurbished, Club.
            key MarketplaceId: str

        Returns:
            GetOffersResponse:

        """
        return self._request(fill_query_params(kwargs.pop('path'), asin), params={**kwargs})

    def _create_get_pricing_request(self, item_list, item_type, **kwargs):
        return self._request(kwargs.pop('path'),
                             params={**{f"{item_type}s": ','.join(
                                 [urllib.parse.quote_plus(s) for s in item_list])},
                                     'ItemType': item_type,
                                     **({'ItemCondition': kwargs.pop(
                                         'ItemCondition')} if 'ItemCondition' in kwargs else {}),
                                     'MarketplaceId': kwargs.get('MarketplaceId', self.marketplace_id)})
