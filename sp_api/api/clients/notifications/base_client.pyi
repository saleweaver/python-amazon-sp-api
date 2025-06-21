from enum import Enum
from typing import Literal, overload

from sp_api.base import Client

from .notifications_v_v1 import Notifications_V_v1

class NotificationsVersion(Enum):
    V_v1: Literal["v1"]

class Notifications(Client):
    # 1) No‐arg default → latest version
    @overload
    def __new__(cls) -> Notifications_V_v1: ...
    # v1 explicit overload
    @overload
    def __new__(
        cls, version: Literal[NotificationsVersion.V_v1], *args, **kwargs
    ) -> Notifications_V_v1: ...
    # fallback stub
    def __new__(cls, version=..., *args, **kwargs) -> Notifications_V_v1: ...
