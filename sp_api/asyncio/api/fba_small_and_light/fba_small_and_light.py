import urllib.parse

from sp_api.base import ApiResponse, deprecated, fill_query_params, sp_endpoint
from sp_api.asyncio.base import AsyncBaseClient


class FbaSmallAndLight(AsyncBaseClient):
    """
    FbaSmallAndLight SP-API Client
    :link:

    The Selling Partner API for FBA Small and Light lets you help sellers manage their listings in the Small and Light program. The program reduces the cost of fulfilling orders for small and lightweight FBA inventory. You can enroll or remove items from the program and check item eligibility and enrollment status. You can also preview the estimated program fees charged to a seller for items sold while enrolled in the program.
    """

    @deprecated
    async def get_small_and_light_enrollment_by_seller_s_k_u(
        self, sellerSKU, **kwargs
    ) -> ApiResponse:
        return await self.get_small_and_light_enrollment_by_seller_sku(
            sellerSKU, **kwargs
        )

    @sp_endpoint("/fba/smallAndLight/v1/enrollments/{}", method="GET")
    async def get_small_and_light_enrollment_by_seller_sku(
        self, seller_sku, **kwargs
    ) -> ApiResponse:
        """
        get_small_and_light_enrollment_by_seller_sku(self, seller_sku, **kwargs) -> ApiResponse
        
        Returns the Small and Light enrollment status for the item indicated by the specified seller SKU in the specified marketplace.
        
        Examples:
            literal blocks::
            
                await FbaSmallAndLight().get_small_and_light_enrollment_by_seller_sku("value")
        
        Args:
            seller_sku:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), seller_sku), params=kwargs
        )

    @deprecated
    async def put_small_and_light_enrollment_by_seller_s_k_u(
        self, sellerSKU, **kwargs
    ) -> ApiResponse:
        return await self.put_small_and_light_enrollment_by_seller_sku(
            sellerSKU, **kwargs
        )

    @sp_endpoint("/fba/smallAndLight/v1/enrollments/{}", method="PUT")
    async def put_small_and_light_enrollment_by_seller_sku(
        self, seller_sku, **kwargs
    ) -> ApiResponse:
        """
        put_small_and_light_enrollment_by_seller_sku(self, seller_sku, **kwargs) -> ApiResponse
        
        Enrolls the item indicated by the specified seller SKU in the Small and Light program in the specified marketplace. If the item is not eligible, the ineligibility reasons are returned.
        
        Examples:
            literal blocks::
            
                await FbaSmallAndLight().put_small_and_light_enrollment_by_seller_sku("value")
        
        Args:
            seller_sku:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), seller_sku),
            params={
                "marketplaceIds": kwargs.get("marketplaceIds", self.marketplace_id),
                "method": kwargs.get("method", "PUT"),
            },
        )

    @deprecated
    async def delete_small_and_light_enrollment_by_seller_s_k_u(
        self, sellerSKU, **kwargs
    ) -> ApiResponse:
        return await self.delete_small_and_light_enrollment_by_seller_sku(
            sellerSKU, **kwargs
        )

    @sp_endpoint("/fba/smallAndLight/v1/enrollments/{}", method="DELETE")
    async def delete_small_and_light_enrollment_by_seller_sku(
        self, seller_sku, **kwargs
    ) -> ApiResponse:
        """
        delete_small_and_light_enrollment_by_seller_sku(self, seller_sku, **kwargs) -> ApiResponse
        
        Removes the item indicated by the specified seller SKU from the Small and Light program in the specified marketplace. If the item is not eligible for disenrollment, the ineligibility reasons are returned.
        
        Examples:
            literal blocks::
            
                await FbaSmallAndLight().delete_small_and_light_enrollment_by_seller_sku("value")
        
        Args:
            seller_sku:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), seller_sku), data=kwargs
        )

    @deprecated
    async def get_small_and_light_eligibility_by_seller_s_k_u(
        self, sellerSKU, **kwargs
    ) -> ApiResponse:
        return await self.get_small_and_light_eligibility_by_seller_sku(
            sellerSKU, **kwargs
        )

    @sp_endpoint("/fba/smallAndLight/v1/eligibilities/{}", method="GET")
    async def get_small_and_light_eligibility_by_seller_sku(
        self, seller_sku, **kwargs
    ) -> ApiResponse:
        """
        get_small_and_light_eligibility_by_seller_sku(self, seller_sku, **kwargs) -> ApiResponse
        
        Returns the Small and Light program eligibility status of the item indicated by the specified seller SKU in the specified marketplace. If the item is not eligible, the ineligibility reasons are returned.
        
        Examples:
            literal blocks::
            
                await FbaSmallAndLight().get_small_and_light_eligibility_by_seller_sku("value")
        
        Args:
            seller_sku:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """

        return await self._request(
            fill_query_params(kwargs.pop("path"), seller_sku), params=kwargs
        )

    @sp_endpoint("/fba/smallAndLight/v1/feePreviews", method="POST")
    async def get_small_and_light_fee_preview(self, **kwargs) -> ApiResponse:
        """
        get_small_and_light_fee_preview(self, **kwargs) -> ApiResponse
        
        Returns the Small and Light fee estimates for the specified items. You must include a marketplaceId parameter to retrieve the proper fee estimates for items to be sold in that marketplace. The ordering of items in the response will mirror the order of the items in the request. Duplicate ASIN/price combinations are removed.
        
        Examples:
            literal blocks::
            
                await FbaSmallAndLight().get_small_and_light_fee_preview()
        
        Args:
            **kwargs:
        
        Returns:
            ApiResponse
        """

        return await self._request(kwargs.pop("path"), data=kwargs)
