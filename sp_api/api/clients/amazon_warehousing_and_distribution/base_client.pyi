from enum import Enum
from typing import Literal, overload

from sp_api.base import Client

from .amazon_warehousing_and_distribution_v_2024_05_09 import \
    AmazonWarehousingAndDistribution_V_2024_05_09

class AmazonWarehousingAndDistributionVersion(Enum):
    V_2024_05_09: Literal["2024-05-09"]

class AmazonWarehousingAndDistribution(Client):
    # 1) No‐arg default → latest version
    @overload
    def __new__(cls) -> AmazonWarehousingAndDistribution_V_2024_05_09: ...
    # 2024-05-09 explicit overload
    @overload
    def __new__(
        cls,
        version: Literal[AmazonWarehousingAndDistributionVersion.V_2024_05_09],
        *args,
        **kwargs,
    ) -> AmazonWarehousingAndDistribution_V_2024_05_09: ...
    # fallback stub
    def __new__(
        cls, version=..., *args, **kwargs
    ) -> AmazonWarehousingAndDistribution_V_2024_05_09: ...
