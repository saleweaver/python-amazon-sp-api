from enum import Enum
from typing import Literal, overload

from sp_api.base import Client

from .messaging_v_v1 import Messaging_V_v1

class MessagingVersion(Enum):
    V_v1: Literal["v1"]

class Messaging(Client):
    # 1) No‐arg default → latest version
    @overload
    def __new__(cls) -> Messaging_V_v1: ...
    # v1 explicit overload
    @overload
    def __new__(
        cls, version: Literal[MessagingVersion.V_v1], *args, **kwargs
    ) -> Messaging_V_v1: ...
    # fallback stub
    def __new__(cls, version=..., *args, **kwargs) -> Messaging_V_v1: ...
