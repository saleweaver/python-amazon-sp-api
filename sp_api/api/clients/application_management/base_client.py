from enum import Enum
from typing import Union, overload

from sp_api.base import Client

from .application_management_v_2023_11_30 import \
    ApplicationManagement_V_2023_11_30


class ApplicationManagementVersion(Enum):
    V_2023_11_30 = "2023-11-30"


class ApplicationManagement(Client):
    @overload
    def __new__(cls, *args, **kwargs) -> ApplicationManagement_V_2023_11_30: ...
    @overload
    def __new__(
        cls, version: ApplicationManagementVersion.V_2023_11_30, *args, **kwargs
    ) -> ApplicationManagement_V_2023_11_30: ...
    def __new__(
        cls,
        version: Union[
            ApplicationManagementVersion, str
        ] = ApplicationManagementVersion.V_2023_11_30,
        *args,
        **kwargs,
    ):
        if not isinstance(version, ApplicationManagementVersion):
            try:
                version = ApplicationManagementVersion(version)
            except ValueError:
                raise ValueError(f"Invalid version: {version!r}")
        if version == ApplicationManagementVersion.V_2023_11_30:
            return ApplicationManagement_V_2023_11_30(*args, **kwargs)
        else:
            raise ValueError(f"Invalid version: {version}")
