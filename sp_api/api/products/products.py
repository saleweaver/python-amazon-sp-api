import urllib.parse

from sp_api.api.products.models.get_pricing_response import GetPricingResponse
from sp_api.base import Client, Marketplaces, sp_endpoint


class Products(Client):
    def __init__(self, marketplace=Marketplaces.US, refresh_token=None):
        super().__init__(marketplace, refresh_token)

    def get_product_pricing_for_skus(self, seller_sku_list, **kwargs):
        """
        Returns pricing information for a seller's offer listings based on seller sku.

        :param seller_sku_list:
        :param kwargs:
        :return:
        """
        return self._create_get_pricing_request(seller_sku_list, 'Sku', **kwargs)

    def get_product_pricing_for_asins(self, asin_list, **kwargs):
        """
        Returns pricing information for a seller's offer listings based on ASIN.

        :param asin_list:
        :param kwargs:
        :return:
        """
        return self._create_get_pricing_request(asin_list, 'Asin', **kwargs)

    @sp_endpoint('/products/pricing/v0/price', method='GET')
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
                                    'MarketplaceId': self.marketplace_id}).json())
