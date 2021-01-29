from sp_api.base.helpers import sp_endpoint, fill_query_params
from sp_api.api.notifications.models.create_destination_response import CreateDestinationResponse
from sp_api.api.notifications.models.create_subscription_response import CreateSubscriptionResponse
from sp_api.api.notifications.models.delete_destination_response import DeleteDestinationResponse
from sp_api.api.notifications.models.delete_subscription_by_id_response import DeleteSubscriptionByIdResponse
from sp_api.api.notifications.models.get_destination_response import GetDestinationResponse
from sp_api.api.notifications.models.get_destinations_response import GetDestinationsResponse
from sp_api.api.notifications.models.get_subscription_by_id_response import GetSubscriptionByIdResponse
from sp_api.api.notifications.models.get_subscription_response import GetSubscriptionResponse
from sp_api.base import Client, Marketplaces, deprecated, NotificationType


class Notifications(Client):
    """
    :link: https://github.com/amzn/selling-partner-api-docs/blob/main/references/notifications-api/notifications.md
    """
    def __init__(self, marketplace=Marketplaces.US, *, refresh_token=None, account='default', credentials=None):
        super().__init__(marketplace, refresh_token, account, credentials)

    @deprecated
    def add_subscription(self, notification_type: NotificationType or str, **kwargs):
        """deprecated, use create_subscription"""
        return self.create_subscription(notification_type, **kwargs)

    @sp_endpoint('/notifications/v1/subscriptions/{}', method='POST')
    def create_subscription(self, notification_type: NotificationType or str, destination_id: str = None, **kwargs) -> CreateSubscriptionResponse:
        """
        create_subscription(self, notification_type: NotificationType or str, destination_id: str = None, **kwargs) -> CreateSubscriptionResponse
        Creates a subscription for the specified notification type to be delivered to the specified destination.
        Before you can subscribe, you must first create the destination by calling the createDestination operation.

        **Usage Plan:**

        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       5
        ======================================  ==============

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            notification_type: NotificationType or str
            destination_id: str
            **kwargs:


        Returns:
            CreateSubscriptionResponse:

        """
        data = {
            'destinationId': kwargs.pop('destinationId', destination_id),
            'payloadVersion': kwargs.pop('payload_version', '1.0')
        }
        return CreateSubscriptionResponse(
            **self._request(fill_query_params(kwargs.pop('path'),
                                                                  notification_type if isinstance(notification_type,
                                                                                                  str) else notification_type.value),
                                                data={**kwargs, **data}).json()
        )

    @sp_endpoint('/notifications/v1/subscriptions/{}')
    def get_subscription(self, notification_type: NotificationType or str, **kwargs) -> GetSubscriptionResponse:
        """
        get_subscription(self, notification_type: NotificationType or str, **kwargs) -> GetSubscriptionResponse
        Returns information about subscriptions of the specified notification type. You can use this API to get subscription information when you do not have a subscription identifier.

        **Usage Plan:**

        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       5
        ======================================  ==============

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.


        Args:
            notification_type: NotificationType or str
            **kwargs:

        Returns:
            GetSubscriptionResponse:

        """
        return GetSubscriptionResponse(
            **self._request(fill_query_params(kwargs.pop('path'), notification_type if isinstance(notification_type, str) else notification_type.value),
                                                params={**kwargs}).json()
        )

    @sp_endpoint('/notifications/v1/subscriptions/{}/{}', method='DELETE')
    def delete_notification_subscription(self, notification_type: NotificationType or str, subscription_id: str, **kwargs) -> DeleteSubscriptionByIdResponse:
        """
        delete_notification_subscription(self, notification_type: NotificationType or str, subscription_id: str, **kwargs) -> DeleteSubscriptionByIdResponse
        Deletes the subscription indicated by the subscription identifier and notification type that you specify.
        The subscription identifier can be for any subscription associated with your application. After you successfully call this operation, notifications will stop being sent for the associated subscription. The deleteSubscriptionById API is grantless. For more information, see "Grantless operations" in the Selling Partner API Developer Guide.

        **Usage Plan:**

        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       5
        ======================================  ==============

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            notification_type: NotificationType or str
            subscription_id: str
            **kwargs:

        Returns:
            DeleteSubscriptionByIdResponse:

        """
        return DeleteSubscriptionByIdResponse(
            **self._request(
                fill_query_params(kwargs.pop('path'), notification_type if isinstance(notification_type, str) else notification_type.value, subscription_id),
                params={**kwargs}).json()
        )

    @sp_endpoint(path='/notifications/v1/destinations', method='POST')
    def create_destination(self, name: str, arn: str, **kwargs) -> CreateDestinationResponse:
        """
        create_destination(self, name: str, arn: str, **kwargs) -> CreateDestinationResponse
        Creates a destination resource to receive notifications. The createDestination API is grantless. For more information, see "Grantless operations" in the Selling Partner API Developer Guide.

        **Usage Plan:**

        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       5
        ======================================  ==============


        Args:
            name: str
            arn: str
            **kwargs:

        Returns:
            CreateDestinationResponse:

        """

        data = {
            'resourceSpecification': {
                'sqs': {
                    'arn': arn
                }
            },
            'name': name,
        }

        return CreateDestinationResponse(
            **self._request_grantless_operation(kwargs.pop('path'), data={**kwargs, **data}).json()
        )

    @sp_endpoint('/notifications/v1/destinations', method='GET')
    def get_destinations(self, **kwargs) -> GetDestinationsResponse:
        """
        get_destinations(self, **kwargs) -> GetDestinationsResponse
        Returns information about all destinations. The getDestinations API is grantless. For more information, see "Grantless operations" in the Selling Partner API Developer Guide.

        **Usage Plan:**

        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       5
        ======================================  ==============


        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            **kwargs:

        Returns:
            GetDestinationsResponse:

        """
        return GetDestinationsResponse(
            **self._request_grantless_operation(kwargs.pop('path'), params={**kwargs}).json()
        )

    @sp_endpoint('/notifications/v1/destinations/{}', method='GET')
    def get_destination(self, destination_id: str, **kwargs) -> GetDestinationResponse:
        """
        get_destination(self, destination_id: str, **kwargs) -> GetDestinationResponse
        Returns information about all destinations. The getDestinations API is grantless. For more information, see "Grantless operations" in the Selling Partner API Developer Guide.

        **Usage Plan:**

        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       5
        ======================================  ==============

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.


        Args:
            destination_id: str
            **kwargs:

        Returns:
            GetDestinationResponse:


        """
        return GetDestinationResponse(
            **self._request_grantless_operation(fill_query_params(kwargs.pop('path'), destination_id),
                                                params={**kwargs}).json()
        )

    @sp_endpoint('/notifications/v1/destinations/{}', method='DELETE')
    def delete_destination(self, destination_id: str, **kwargs) -> DeleteDestinationResponse:
        """
        delete_destination(self, destination_id: str, **kwargs) -> DeleteDestinationResponse
        Deletes the destination that you specify. The deleteDestination API is grantless. For more information, see "Grantless operations" in the Selling Partner API Developer Guide.

        **Usage Plan:**

        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       5
        ======================================  ==============

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            destination_id: str
            **kwargs:

        Returns:
            DeleteDestinationResponse:

        """
        return DeleteDestinationResponse(
            **self._request_grantless_operation(fill_query_params(kwargs.pop('path'), destination_id),
                                                params={**kwargs}).json()
        )
