import urllib.parse

from sp_api.base import ApiResponse, fill_query_params, sp_endpoint
from sp_api.asyncio.base import AsyncBaseClient


class ApplicationIntegrations(AsyncBaseClient):
    """
    ApplicationIntegrations SP-API Client
    :link: 

    With the AppIntegrations API v2024-04-01, you can send notifications to Amazon Selling Partners and display the notifications in Seller Central.
    """


    @sp_endpoint('/appIntegrations/2024-04-01/notifications', method='POST')
    async def create_notification(self, **kwargs) -> ApiResponse:
        """
        create_notification(self, **kwargs) -> ApiResponse
        
        Create a notification for sellers in Seller Central.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       5
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await ApplicationIntegrations().create_notification()
        
        Args:
            body: CreateNotificationRequest | required The request body for the `createNotification` operation.
        
        Returns:
            ApiResponse
        """
    
        return await self._request(kwargs.pop('path'), data=kwargs)
    

    @sp_endpoint('/appIntegrations/2024-04-01/notifications/deletion', method='POST')
    async def delete_notifications(self, **kwargs) -> ApiResponse:
        """
        delete_notifications(self, **kwargs) -> ApiResponse
        
        Remove your application's notifications from the Appstore notifications dashboard.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       5
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await ApplicationIntegrations().delete_notifications()
        
        Args:
            body: DeleteNotificationsRequest | required The request body for the `deleteNotifications` operation.
        
        Returns:
            ApiResponse
        """
    
        return await self._request(kwargs.pop('path'), data=kwargs)
    

    @sp_endpoint('/appIntegrations/2024-04-01/notifications/{}/feedback', method='POST')
    async def record_action_feedback(self, notificationId, **kwargs) -> ApiResponse:
        """
        record_action_feedback(self, notificationId, **kwargs) -> ApiResponse
        
        Records the seller's response to a notification.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       5
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                await ApplicationIntegrations().record_action_feedback("value")
        
        Args:
            notificationId: object | required A `notificationId` uniquely identifies a notification.
            body: RecordActionFeedbackRequest | required The request body for the `recordActionFeedback` operation.
        
        Returns:
            ApiResponse
        """
    
        return await self._request(fill_query_params(kwargs.pop('path'), notificationId), data=kwargs)
