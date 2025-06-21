from enum import Enum
from typing import Literal, overload

from sp_api.base import Client

from .application_integrations_v_2024_04_01 import \
    ApplicationIntegrations_V_2024_04_01

class ApplicationIntegrationsVersion(Enum):
    V_2024_04_01: Literal["2024-04-01"]

class ApplicationIntegrations(Client):
    # 1) No‐arg default → latest version
    @overload
    def __new__(cls) -> ApplicationIntegrations_V_2024_04_01: ...
    # 2024-04-01 explicit overload
    @overload
    def __new__(
        cls,
        version: Literal[ApplicationIntegrationsVersion.V_2024_04_01],
        *args,
        **kwargs,
    ) -> ApplicationIntegrations_V_2024_04_01: ...
    # fallback stub
    def __new__(
        cls, version=..., *args, **kwargs
    ) -> ApplicationIntegrations_V_2024_04_01: ...
