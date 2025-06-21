from enum import Enum
from typing import Union, overload

from sp_api.base import Client

from .amazon_warehousing_and_distribution_v_2024_05_09 import \
    AmazonWarehousingAndDistribution_V_2024_05_09


class AmazonWarehousingAndDistributionVersion(Enum):
    V_2024_05_09 = "2024-05-09"


class AmazonWarehousingAndDistribution(Client):
    @overload
    def __new__(
        cls, *args, **kwargs
    ) -> AmazonWarehousingAndDistribution_V_2024_05_09: ...
    @overload
    def __new__(
        cls,
        version: AmazonWarehousingAndDistributionVersion.V_2024_05_09,
        *args,
        **kwargs,
    ) -> AmazonWarehousingAndDistribution_V_2024_05_09: ...
    def __new__(
        cls,
        version: Union[
            AmazonWarehousingAndDistributionVersion, str
        ] = AmazonWarehousingAndDistributionVersion.V_2024_05_09,
        *args,
        **kwargs,
    ):
        if not isinstance(version, AmazonWarehousingAndDistributionVersion):
            try:
                version = AmazonWarehousingAndDistributionVersion(version)
            except ValueError:
                raise ValueError(f"Invalid version: {version!r}")
        if version == AmazonWarehousingAndDistributionVersion.V_2024_05_09:
            return AmazonWarehousingAndDistribution_V_2024_05_09(*args, **kwargs)
        else:
            raise ValueError(f"Invalid version: {version}")
