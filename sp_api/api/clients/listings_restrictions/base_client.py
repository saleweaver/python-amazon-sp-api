from enum import Enum
from typing import Union, overload

from sp_api.base import Client

from .listings_restrictions_v_2021_08_01 import \
    ListingsRestrictions_V_2021_08_01


class ListingsRestrictionsVersion(Enum):
    V_2021_08_01 = "2021-08-01"


class ListingsRestrictions(Client):
    @overload
    def __new__(cls, *args, **kwargs) -> ListingsRestrictions_V_2021_08_01: ...
    @overload
    def __new__(
        cls, version: ListingsRestrictionsVersion.V_2021_08_01, *args, **kwargs
    ) -> ListingsRestrictions_V_2021_08_01: ...
    def __new__(
        cls,
        version: Union[
            ListingsRestrictionsVersion, str
        ] = ListingsRestrictionsVersion.V_2021_08_01,
        *args,
        **kwargs,
    ):
        if not isinstance(version, ListingsRestrictionsVersion):
            try:
                version = ListingsRestrictionsVersion(version)
            except ValueError:
                raise ValueError(f"Invalid version: {version!r}")
        if version == ListingsRestrictionsVersion.V_2021_08_01:
            return ListingsRestrictions_V_2021_08_01(*args, **kwargs)
        else:
            raise ValueError(f"Invalid version: {version}")
