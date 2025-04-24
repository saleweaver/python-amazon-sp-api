import urllib.parse

from sp_api.base import Client, sp_endpoint, fill_query_params, ApiResponse


class ApplicationIntegrations(Client):
    """
    ApplicationIntegrations SP-API Client
    :link: 

    With the AppIntegrations API v2024-04-01, you can send notifications to Amazon Selling Partners and display the notifications in Seller Central.
    """


    @sp_endpoint('/appIntegrations/2024-04-01/notifications', method='POST')
    def create_notification(self, **kwargs) -> ApiResponse:
        """
        create_notification(self, **kwargs) -> ApiResponse

        Create a notification for sellers in Seller Central.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 5 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table indicates the default rate and burst values for this operation. Sellers whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

        Args:
        
                    body: | * REQUIRED {'description': 'The request for the `createNotification` operation.',
         'example': {'marketplaceId': 'ATVPDKIKX0DER', 'notificationParameters': {'priceValue': '200'}, 'templateId': 'PRICE_CHANGE'},
         'properties': {'marketplaceId': {'description': 'An encrypted marketplace identifier for the posted notification.', 'type': 'string'},
                        'notificationParameters': {'$ref': '#/definitions/NotificationParameters', 'description': 'The parameters specified in the template you used to onboard your application.'},
                        'templateId': {'description': 'The unique identifier of the notification template you used to onboard your application.', 'type': 'string'}},
         'required': ['templateId', 'notificationParameters'],
         'type': 'object'}


        Returns:
            ApiResponse:
        """
    
        return self._request(kwargs.pop('path'),  data=kwargs)
    

    @sp_endpoint('/appIntegrations/2024-04-01/notifications/deletion', method='POST')
    def delete_notifications(self, **kwargs) -> ApiResponse:
        """
        delete_notifications(self, **kwargs) -> ApiResponse

        Remove your application's notifications from the Appstore notifications dashboard.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 5 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table indicates the default rate and burst values for this operation. Sellers whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

                Args:

                    body: | * REQUIRED {'description': 'The request for the `deleteNotifications` operation.',
         'example': {'deletionReason': 'INCORRECT_CONTENT', 'templateId': 'PRICE_CHANGE'},
         'properties': {'deletionReason': {'description': 'The unique identifier that maps each notification status to a reason code.',
                                           'enum': ['INCORRECT_CONTENT', 'INCORRECT_RECIPIENT'],
                                           'type': 'string',
                                           'x-docgen-enum-table-extension': [{'description': "The notification's content is recognized to be incorrect.", 'value': 'INCORRECT_CONTENT'},
                                                                             {'description': 'The notification was sent to incorrect seller.', 'value': 'INCORRECT_RECIPIENT'}]},
                        'templateId': {'description': 'The unique identifier of the notification template you used to onboard your application.', 'type': 'string'}},
         'required': ['templateId', 'deletionReason'],
         'type': 'object'}


        Returns:
            ApiResponse:
        """
    
        return self._request(kwargs.pop('path'),  data=kwargs)
    

    @sp_endpoint('/appIntegrations/2024-04-01/notifications/{}/feedback', method='POST')
    def record_action_feedback(self, notificationId, **kwargs) -> ApiResponse:
        """
        record_action_feedback(self, notificationId, **kwargs) -> ApiResponse

        Records the seller's response to a notification.

        **Usage Plan:**

        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 1 | 5 |

        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The preceding table indicates the default rate and burst values for this operation. Sellers whose business demands require higher throughput may have higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).

                Args:

                    notificationId:string | * REQUIRED A `notificationId` uniquely identifies a notification.

                    body: | * REQUIRED {'description': 'The request for the `recordActionFeedback` operation.',
         'example': {'feedbackActionCode': 'SELLER_ACTION_COMPLETED'},
         'properties': {'feedbackActionCode': {'description': 'The unique identifier for each notification status.',
                                               'enum': ['SELLER_ACTION_COMPLETED'],
                                               'type': 'string',
                                               'x-docgen-enum-table-extension': [{'description': 'The seller completed the action attached to the posted notification.', 'value': 'SELLER_ACTION_COMPLETED'}]}},
         'required': ['feedbackActionCode'],
         'type': 'object'}


        Returns:
            ApiResponse:
        """
    
        return self._request(fill_query_params(kwargs.pop('path'), notificationId), data=kwargs)
    
