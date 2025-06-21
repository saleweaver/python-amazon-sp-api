from enum import Enum
from typing import Literal, overload

from sp_api.base import Client

from .application_management_v_2023_11_30 import \
    ApplicationManagement_V_2023_11_30

class ApplicationManagementVersion(Enum):
    V_2023_11_30: Literal["2023-11-30"]

class ApplicationManagement(Client):
    # 1) No‐arg default → latest version
    @overload
    def __new__(cls) -> ApplicationManagement_V_2023_11_30: ...
    # 2023-11-30 explicit overload
    @overload
    def __new__(
        cls,
        version: Literal[ApplicationManagementVersion.V_2023_11_30],
        *args,
        **kwargs,
    ) -> ApplicationManagement_V_2023_11_30: ...
    # fallback stub
    def __new__(
        cls, version=..., *args, **kwargs
    ) -> ApplicationManagement_V_2023_11_30: ...
