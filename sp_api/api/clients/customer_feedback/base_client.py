from enum import Enum
from typing import Union, overload

from sp_api.base import Client

from .customer_feedback_v_2024_06_01 import CustomerFeedback_V_2024_06_01


class CustomerFeedbackVersion(Enum):
    V_2024_06_01 = "2024-06-01"


class CustomerFeedback(Client):
    @overload
    def __new__(cls, *args, **kwargs) -> CustomerFeedback_V_2024_06_01: ...
    @overload
    def __new__(
        cls, version: CustomerFeedbackVersion.V_2024_06_01, *args, **kwargs
    ) -> CustomerFeedback_V_2024_06_01: ...
    def __new__(
        cls,
        version: Union[
            CustomerFeedbackVersion, str
        ] = CustomerFeedbackVersion.V_2024_06_01,
        *args,
        **kwargs,
    ):
        if not isinstance(version, CustomerFeedbackVersion):
            try:
                version = CustomerFeedbackVersion(version)
            except ValueError:
                raise ValueError(f"Invalid version: {version!r}")
        if version == CustomerFeedbackVersion.V_2024_06_01:
            return CustomerFeedback_V_2024_06_01(*args, **kwargs)
        else:
            raise ValueError(f"Invalid version: {version}")
