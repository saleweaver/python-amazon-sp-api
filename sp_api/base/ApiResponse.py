import pprint
from typing import Generic, TypeVar, Any, Union, Optional, get_args, get_origin
from pydantic import BaseModel

T = TypeVar("T")


class ApiResponse(Generic[T]):
    """
    Api Response

    Wrapper around all responses from the API.

    Examples:
        literal blocks::

            response = Orders().get_orders(CreatedAfter='TEST_CASE_200', MarketplaceIds=["ATVPDKIKX0DER"])

            print(response.payload) # original response data
            # Access one of `payload`s properties using `__getattr__`
            print(response.Orders) # Array of orders
            # Access one of `payload`s properties using `__call__`
            print(response('Orders')) # Array of orders
            # Shorthand for response.payload
            print(response()) # original response data

    Args:
        payload: dict or list | original response from Amazon
        errors: any | contains possible error messages
        pagination: any | information about an endpoints pagination
        headers: any | headers returned by the API
        rate_limit: number | The `x-amzn-RateLimit-Limit` header, if available
        next_token: str | The next token used to retrieve the next page, if any
        kwargs: any

    """

    def __init__(
        self,
        payload: Optional[Union[T, dict, list]] = None,
        errors: Any = None,
        pagination: Any = None,
        headers: Any = None,
        nextToken: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        self.payload = payload or kwargs
        self.payload: Union[T, dict, list]  # type: ignore
        self.errors = errors
        self.pagination = pagination
        self.headers = headers
        self.rate_limit = headers.get("x-amzn-RateLimit-Limit")
        try:
            self.next_token = (
                nextToken
                or self.payload.get("pagination", {}).get("nextToken", None)
                or self.payload.get("NextToken", None)
                or self.pagination.get("nextToken", None)
                or self.payload.get("nextPageToken", None)
                or self.payload.get("nextToken", None)
            )

        except AttributeError:
            self.next_token = None
        if kwargs != self.payload:
            self.kwargs = kwargs

    def __str__(self) -> str:
        return pprint.pformat(vars(self))

    def __call__(self, item: Optional[str] = None, **kwargs: Any) -> Union[T, Any]:
        if not item:
            return self.payload
        return self.payload.get(item)

    def __getattr__(self, item: str) -> Any:
        return self.payload.get(item)

    @property
    def payload_parsed(self) -> Optional[T]:
        """
        Return the payload parsed into the generic type T, if T is a Pydantic model or list thereof.
        """
        try:
            # Extract the runtime type argument T from __orig_class__
            model_type = get_args(self.__orig_class__)[0]
        except (AttributeError, IndexError):
            return self.payload  # no generic type info

        # If T is a Pydantic model, parse the payload into it
        if isinstance(model_type, type) and issubclass(model_type, BaseModel):
            return model_type.model_construct(**(self.payload or {}))

        # If T is a list of Pydantic models, parse each item
        origin = get_origin(model_type)
        if origin is list and isinstance(self.payload, list):
            inner_type = get_args(model_type)[0]
            if isinstance(inner_type, type) and issubclass(inner_type, BaseModel):
                return [inner_type.model_validate(**item) for item in self.payload]

        # Fallback: return the raw payload
        return self.payload  # type: ignore
