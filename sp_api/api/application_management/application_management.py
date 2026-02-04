from sp_api.base import Client, sp_endpoint, fill_query_params, ApiResponse


class ApplicationManagement(Client):
    """
    ApplicationManagement SP-API Client
    :link:

    The Selling Partner API for Application Management lets you programmatically update the client secret on registered applications.
    """
    grantless_scope = 'sellingpartnerapi::client_credential:rotation'

    @sp_endpoint("/applications/2023-11-30/clientSecret", method="POST")
    def rotate_application_client_secret(self, **kwargs) -> ApiResponse:
        """
        rotate_application_client_secret(self, **kwargs) -> ApiResponse
        
        Rotates application client secrets for a developer application. Developers must register a destination queue in the developer console before calling this operation. When this operation is called a new client secret is generated and sent to the developer-registered queue. For more information, refer to [Rotate your application client secret](https://developer-docs.amazon.com/sp-api/v0/docs/application-management-api-v2023-11-30-use-case-guide#tutorial-rotate-your-applications-client-secret).
        
        **Usage Plan:**
        
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        0.0167                                  1
        ======================================  ==============
        
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        
        Examples:
            literal blocks::
            
                ApplicationManagement().rotate_application_client_secret()
        
        Args:
            **kwargs:
        
        Returns:
            ApiResponse
        """

        return self._request_grantless_operation(kwargs.pop("path"), data=kwargs)
