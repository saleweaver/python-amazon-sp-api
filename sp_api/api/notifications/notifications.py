from sp_api.base.helpers import sp_endpoint, fill_query_params
from sp_api.base import Client, Marketplaces, deprecated, NotificationType, ApiResponse


class Notifications(Client):
    """
    :link: https://github.com/amzn/selling-partner-api-docs/blob/main/references/notifications-api/notifications.md
    """

    grantless_scope = "sellingpartnerapi::notifications"

    @deprecated
    def add_subscription(self, notification_type: NotificationType or str, **kwargs):
        """
        add_subscription(self, notification_type, **kwargs) -> ApiResponse
        
        deprecated, use create_subscription
        
        Examples:
            literal blocks::
            
                Notifications().add_subscription("value")
        
        Args:
            notification_type:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """
        return self.create_subscription(notification_type, **kwargs)

    @sp_endpoint("/notifications/v1/subscriptions/{}", method="POST")
    def create_subscription(
        self,
        notification_type: NotificationType or str,
        destination_id: str = None,
        **kwargs
    ) -> ApiResponse:
        """
        create_subscription(self, notification_type, destination_id, **kwargs) -> ApiResponse
        
        Creates a subscription for the specified notification type to be delivered to the specified destination. Before you can subscribe, you must first create the destination by calling the `createDestination` operation. In cases where the specified notification type supports multiple payload versions, you can utilize this API to subscribe to a different payload version if you already have an existing subscription for a different payload version.
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       5
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                Notifications().create_subscription("value", "value")
        
        Args:
            body: CreateSubscriptionRequest | required
            param: object |
        
        Returns:
            ApiResponse
        """
        data = {
            "destinationId": kwargs.pop("destinationId", destination_id),
            "payloadVersion": kwargs.pop("payload_version", "1.0"),
        }
        return self._request(
            fill_query_params(
                kwargs.pop("path"),
                (
                    notification_type
                    if isinstance(notification_type, str)
                    else notification_type.value
                ),
            ),
            data={**kwargs, **data},
        )

    @sp_endpoint("/notifications/v1/subscriptions/{}")
    def get_subscription(
        self, notification_type: NotificationType or str, **kwargs
    ) -> ApiResponse:
        """
        get_subscription(self, notification_type, **kwargs) -> ApiResponse
        
        Returns information about subscription of the specified notification type and payload version. `payloadVersion` is an optional parameter. When `payloadVersion` is not provided, it will return latest payload version subscription's information. You can use this API to get subscription information when you do not have a subscription identifier.
        
        Examples:
            literal blocks::
            
                Notifications().get_subscription("value")
        
        Args:
            notification_type:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """
        return self._request(
            fill_query_params(
                kwargs.pop("path"),
                (
                    notification_type
                    if isinstance(notification_type, str)
                    else notification_type.value
                ),
            ),
            params={**kwargs},
        )

    @sp_endpoint("/notifications/v1/subscriptions/{}/{}", method="DELETE")
    def delete_notification_subscription(
        self, notification_type: NotificationType or str, subscription_id: str, **kwargs
    ) -> ApiResponse:
        """
        delete_notification_subscription(self, notification_type, subscription_id, **kwargs) -> ApiResponse
        
        Deletes the subscription indicated by the subscription identifier and notification type that you specify. The subscription identifier can be for any subscription associated with your application. After you successfully call this operation, notifications will stop being sent for the associated subscription. The `deleteSubscriptionById` operation is grantless. For more information, refer to [Grantless operations](https://developer-docs.amazon.com/sp-api/docs/grantless-operations).
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       5
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                Notifications().delete_notification_subscription("value", "value")
        
        Args:
            subscriptionId: object | required The identifier for the subscription that you want to delete.
            param: object |
        
        Returns:
            ApiResponse
        """
        return self._request(
            fill_query_params(
                kwargs.pop("path"),
                (
                    notification_type
                    if isinstance(notification_type, str)
                    else notification_type.value
                ),
                subscription_id,
            ),
            params={**kwargs},
        )

    @sp_endpoint(path="/notifications/v1/destinations", method="POST")
    def create_destination(
        self,
        name: str,
        arn: str = None,
        account_id: str = None,
        region: str = None,
        **kwargs
    ) -> ApiResponse:
        """
        create_destination(self, name, arn, account_id, region, **kwargs) -> ApiResponse
        
        Creates a destination resource to receive notifications. The createDestination API is grantless. For more information, see "Grantless operations" in the Selling Partner API Developer Guide.
        
        Examples:
            literal blocks::
            
                Notifications().create_destination("value", "value", "value", "value")
        
        Args:
            name:  | required
            arn:  | required
            account_id:  | required
            region:  | required
            **kwargs:
        
        Returns:
            ApiResponse
        """
        resource_name = "sqs" if not account_id else "eventBridge"
        region = region if region else self.region

        data = {
            "resourceSpecification": {
                resource_name: (
                    {"arn": arn}
                    if not account_id
                    else {"region": region, "accountId": account_id}
                )
            },
            "name": name,
        }

        return self._request_grantless_operation(
            kwargs.pop("path"), data={**kwargs, **data}
        )

    @sp_endpoint("/notifications/v1/destinations", method="GET")
    def get_destinations(self, **kwargs) -> ApiResponse:
        """
        get_destinations(self, **kwargs) -> ApiResponse
        
        Returns information about all destinations. The `getDestinations` operation is grantless. For more information, refer to [Grantless operations](https://developer-docs.amazon.com/sp-api/docs/grantless-operations).
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       5
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                Notifications().get_destinations()
        
        Args:
            **kwargs:
        
        Returns:
            ApiResponse
        """
        return self._request_grantless_operation(kwargs.pop("path"), params={**kwargs})

    @sp_endpoint("/notifications/v1/destinations/{}", method="GET")
    def get_destination(self, destination_id: str, **kwargs) -> ApiResponse:
        """
        get_destination(self, destination_id, **kwargs) -> ApiResponse
        
        Returns information about the destination that you specify. The `getDestination` operation is grantless. For more information, refer to [Grantless operations](https://developer-docs.amazon.com/sp-api/docs/grantless-operations).
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       5
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                Notifications().get_destination("value")
        
        Args:
            destinationId: object | required The identifier generated when you created the destination.
        
        Returns:
            ApiResponse
        """
        return self._request_grantless_operation(
            fill_query_params(kwargs.pop("path"), destination_id), params={**kwargs}
        )

    @sp_endpoint("/notifications/v1/destinations/{}", method="DELETE")
    def delete_destination(self, destination_id: str, **kwargs) -> ApiResponse:
        """
        delete_destination(self, destination_id, **kwargs) -> ApiResponse
        
        Deletes the destination that you specify. The `deleteDestination` operation is grantless. For more information, refer to [Grantless operations](https://developer-docs.amazon.com/sp-api/docs/grantless-operations).
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       5
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                Notifications().delete_destination("value")
        
        Args:
            destinationId: object | required The identifier for the destination that you want to delete.
        
        Returns:
            ApiResponse
        """
        return self._request_grantless_operation(
            fill_query_params(kwargs.pop("path"), destination_id), params={**kwargs}
        )



    @sp_endpoint("/notifications/v1/subscriptions/{}/{}", method="GET")
    def get_subscription_by_id(self, notificationType, subscriptionId, **kwargs) -> ApiResponse:
        """
        get_subscription_by_id(self, notificationType, subscriptionId, **kwargs) -> ApiResponse
        
        Returns information about a subscription for the specified notification type. The `getSubscriptionById` operation is grantless. For more information, refer to [Grantless operations](https://developer-docs.amazon.com/sp-api/docs/grantless-operations).
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       5
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                Notifications().get_subscription_by_id("value", "value")
        
        Args:
            subscriptionId: object | required The identifier for the subscription that you want to get.
            param: object |
        
        Returns:
            ApiResponse
        """
        return self._request(fill_query_params(kwargs.pop("path"), notificationType, subscriptionId), params=kwargs)
