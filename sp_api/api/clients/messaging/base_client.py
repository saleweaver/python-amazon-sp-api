from enum import Enum
from typing import Union, overload

from sp_api.base import Client

from .messaging_v_v1 import Messaging_V_v1


class MessagingVersion(Enum):
    V_v1 = "v1"


class Messaging(Client):
    @overload
    def __new__(cls, *args, **kwargs) -> Messaging_V_v1: ...
    @overload
    def __new__(
        cls, version: MessagingVersion.V_v1, *args, **kwargs
    ) -> Messaging_V_v1: ...
    def __new__(
        cls,
        version: Union[MessagingVersion, str] = MessagingVersion.V_v1,
        *args,
        **kwargs,
    ):
        if not isinstance(version, MessagingVersion):
            try:
                version = MessagingVersion(version)
            except ValueError:
                raise ValueError(f"Invalid version: {version!r}")
        if version == MessagingVersion.V_v1:
            return Messaging_V_v1(*args, **kwargs)
        else:
            raise ValueError(f"Invalid version: {version}")
