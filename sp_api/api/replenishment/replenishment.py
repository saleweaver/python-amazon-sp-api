import urllib.parse

from sp_api.base import Client, sp_endpoint, fill_query_params, ApiResponse


class Replenishment(Client):
    """
    Replenishment SP-API Client
    :link: 

    The Selling Partner API for Replenishment (Replenishment API) provides programmatic access to replenishment program metrics and offers. These programs provide recurring delivery of any replenishable item at a frequency chosen by the customer.

    The Replenishment API is available worldwide wherever Amazon Subscribe & Save is available or is supported. The API is available to vendors and FBA selling partners.
    """

    @sp_endpoint('/replenishment/2022-11-07/sellingPartners/metrics/search', method='POST')
    def get_selling_partner_metrics(self, **kwargs) -> ApiResponse:
        """
        get_selling_partner_metrics(self, **kwargs) -> ApiResponse

        Returns aggregated replenishment program metrics for a selling partner. 

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 1 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:
        
            body: |  {'description': 'The request body for the `getSellingPartnerMetrics` operation.',
                     'properties': {'aggregationFrequency': {'$ref': '#/definitions/AggregationFrequency'},
                                    'marketplaceId': {'$ref': '#/definitions/MarketplaceId',
                                                      'description': 'The marketplace identifier. The supported marketplaces for both sellers and vendors are US, CA, ES, UK, FR, IT, IN, DE and JP. The supported marketplaces for vendors only are BR, AU, MX, AE and NL.  '
                                                                     'Refer to [Marketplace IDs](https://developer-docs.amazon.com/sp-api/docs/marketplace-ids) to find the identifier for the marketplace.'},
                                    'metrics': {'description': 'The list of metrics requested. If no metric value is provided, data for all of the metrics will be returned.',
                                                'items': {'$ref': '#/definitions/Metric'},
                                                'minItems': 1,
                                                'type': 'array',
                                                'uniqueItems': True},
                                    'programTypes': {'$ref': '#/definitions/ProgramTypes', 'description': 'The list of replenishment program types for which to return metrics.'},
                                    'timeInterval': {'$ref': '#/definitions/TimeInterval', 'description': 'A time interval used to compute metrics.'},
                                    'timePeriodType': {'$ref': '#/definitions/TimePeriodType'}},
                     'required': ['timeInterval', 'timePeriodType', 'programTypes', 'marketplaceId'],
                     'type': 'object'}


        Returns:
            ApiResponse:
        """

        return self._request(kwargs.pop('path'), data=kwargs)

    @sp_endpoint('/replenishment/2022-11-07/offers/metrics/search', method='POST')
    def list_offer_metrics(self, **kwargs) -> ApiResponse:
        """
        list_offer_metrics(self, **kwargs) -> ApiResponse

        Returns aggregated replenishment program metrics for a selling partner's offers.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 1 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:
        
            body: |  {'description': 'The request body for the `listOfferMetrics` operation.',
                     'properties': {'filters': {'$ref': '#/definitions/ListOfferMetricsRequestFilters',
                                                'description': 'Use these parameters to filter results. Any result must match all provided parameters. For any parameter that is an array, the result must match at least one element in the provided array.'},
                                    'pagination': {'$ref': '#/definitions/ListOfferMetricsRequestPagination', 'description': 'Use these parameters to paginate through the response.'},
                                    'sort': {'$ref': '#/definitions/ListOfferMetricsRequestSort', 'description': 'Use these parameters to sort the response.'}},
                     'required': ['pagination', 'filters'],
                     'type': 'object'}


        Returns:
            ApiResponse:
        """

        return self._request(kwargs.pop('path'), data=kwargs)

    @sp_endpoint('/replenishment/2022-11-07/offers/search', method='POST')
    def list_offers(self, **kwargs) -> ApiResponse:
        """
        list_offers(self, **kwargs) -> ApiResponse

        Returns the details of a selling partner's replenishment program offers. Note that this operation only supports sellers at this time.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 1 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:
        
            body: |  {'description': 'The request body for the `listOffers` operation.',
                     'properties': {'filters': {'$ref': '#/definitions/ListOffersRequestFilters',
                                                'description': 'Use these parameters to filter results. Any result must match all provided parameters. For any parameter that is an array, the result must match at least one element in the provided array.'},
                                    'pagination': {'$ref': '#/definitions/ListOffersRequestPagination', 'description': 'Use these parameters to paginate through the response.'},
                                    'sort': {'$ref': '#/definitions/ListOffersRequestSort', 'description': 'Use these parameters to sort the response.'}},
                     'required': ['pagination', 'filters'],
                     'type': 'object'}


        Returns:
            ApiResponse:
        """

        return self._request(kwargs.pop('path'), data=kwargs)
