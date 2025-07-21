from enum import Enum
from typing import Literal, overload

from sp_api.base import Client

from .customer_feedback_v_2024_06_01 import CustomerFeedback_V_2024_06_01

class CustomerFeedbackVersion(Enum):
    V_2024_06_01: Literal["2024-06-01"]

class CustomerFeedback(Client):
    # 1) No‐arg default → latest version
    @overload
    def __new__(cls) -> CustomerFeedback_V_2024_06_01: ...
    # 2024-06-01 explicit overload
    @overload
    def __new__(
        cls, version: Literal[CustomerFeedbackVersion.V_2024_06_01], *args, **kwargs
    ) -> CustomerFeedback_V_2024_06_01: ...
    # fallback stub
    def __new__(cls, version=..., *args, **kwargs) -> CustomerFeedback_V_2024_06_01: ...
