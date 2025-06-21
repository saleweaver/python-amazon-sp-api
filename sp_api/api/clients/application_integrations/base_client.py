from enum import Enum
from typing import Union, overload

from sp_api.base import Client

from .application_integrations_v_2024_04_01 import \
    ApplicationIntegrations_V_2024_04_01


class ApplicationIntegrationsVersion(Enum):
    V_2024_04_01 = "2024-04-01"


class ApplicationIntegrations(Client):
    @overload
    def __new__(cls, *args, **kwargs) -> ApplicationIntegrations_V_2024_04_01: ...
    @overload
    def __new__(
        cls, version: ApplicationIntegrationsVersion.V_2024_04_01, *args, **kwargs
    ) -> ApplicationIntegrations_V_2024_04_01: ...
    def __new__(
        cls,
        version: Union[
            ApplicationIntegrationsVersion, str
        ] = ApplicationIntegrationsVersion.V_2024_04_01,
        *args,
        **kwargs,
    ):
        if not isinstance(version, ApplicationIntegrationsVersion):
            try:
                version = ApplicationIntegrationsVersion(version)
            except ValueError:
                raise ValueError(f"Invalid version: {version!r}")
        if version == ApplicationIntegrationsVersion.V_2024_04_01:
            return ApplicationIntegrations_V_2024_04_01(*args, **kwargs)
        else:
            raise ValueError(f"Invalid version: {version}")
