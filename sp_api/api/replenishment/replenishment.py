import urllib.parse

from sp_api.base import Client, sp_endpoint, fill_query_params, ApiResponse


class Replenishment(Client):
    """
    Replenishment SP-API Client
    :link:

    The Selling Partner API for Replenishment (Replenishment API) provides programmatic access to replenishment program metrics and offers. These programs provide recurring delivery of any replenishable item at a frequency chosen by the customer.

    The Replenishment API is available worldwide wherever Amazon Subscribe & Save is available or is supported. The API is available to vendors and FBA selling partners.
    """

    @sp_endpoint(
        "/replenishment/2022-11-07/sellingPartners/metrics/search", method="POST"
    )
    def get_selling_partner_metrics(self, **kwargs) -> ApiResponse:
        """
        get_selling_partner_metrics(self, **kwargs) -> ApiResponse
        
        Returns aggregated replenishment program metrics for a selling partner.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       1
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                Replenishment().get_selling_partner_metrics()
        
        Args:
            body: GetSellingPartnerMetricsRequest |  The request body for the `getSellingPartnerMetrics` operation.
        
        Returns:
            ApiResponse
        """

        return self._request(kwargs.pop("path"), data=kwargs)

    @sp_endpoint("/replenishment/2022-11-07/offers/metrics/search", method="POST")
    def list_offer_metrics(self, **kwargs) -> ApiResponse:
        """
        list_offer_metrics(self, **kwargs) -> ApiResponse
        
        Returns aggregated replenishment program metrics for a selling partner's offers.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       1
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                Replenishment().list_offer_metrics()
        
        Args:
            body: ListOfferMetricsRequest |  The request body for the `listOfferMetrics` operation.
        
        Returns:
            ApiResponse
        """

        return self._request(kwargs.pop("path"), data=kwargs)

    @sp_endpoint("/replenishment/2022-11-07/offers/search", method="POST")
    def list_offers(self, **kwargs) -> ApiResponse:
        """
        list_offers(self, **kwargs) -> ApiResponse
        
        Returns the details of a selling partner's replenishment program offers.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       1
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                Replenishment().list_offers()
        
        Args:
            body: ListOffersRequest |  The request body for the `listOffers` operation.
        
        Returns:
            ApiResponse
        """

        return self._request(kwargs.pop("path"), data=kwargs)
