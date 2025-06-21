from enum import Enum
from typing import Union, overload

from sp_api.base import Client

from .notifications_v_v1 import Notifications_V_v1


class NotificationsVersion(Enum):
    V_v1 = "v1"


class Notifications(Client):
    @overload
    def __new__(cls, *args, **kwargs) -> Notifications_V_v1: ...
    @overload
    def __new__(
        cls, version: NotificationsVersion.V_v1, *args, **kwargs
    ) -> Notifications_V_v1: ...
    def __new__(
        cls,
        version: Union[NotificationsVersion, str] = NotificationsVersion.V_v1,
        *args,
        **kwargs,
    ):
        if not isinstance(version, NotificationsVersion):
            try:
                version = NotificationsVersion(version)
            except ValueError:
                raise ValueError(f"Invalid version: {version!r}")
        if version == NotificationsVersion.V_v1:
            return Notifications_V_v1(*args, **kwargs)
        else:
            raise ValueError(f"Invalid version: {version}")
