"""
Base model classes for generated Pydantic v2 models.
"""

from enum import Enum
from typing import (Annotated, Any, Callable, Literal, Union, get_args,
                    get_origin, get_type_hints)

from pydantic import BaseModel, ConfigDict, field_serializer
from pydantic.main import IncEx
from sp_api.base import Marketplaces


def _unwrap_annotated(tp):
    """
    Return the underlying type of Annotated or Optional (Union[..., NoneType]).
    """
    origin = get_origin(tp)
    # unwrap Annotated[T, ...] -> T
    if origin is Annotated:
        tp = get_args(tp)[0]
    # unwrap Optional[T] -> T
    origin = get_origin(tp)
    if origin is Union:
        args = get_args(tp)
        # detect Optional[X] (Union[X, NoneType])
        non_none = [a for a in args if a is not type(None)]
        if len(non_none) == 1:
            tp = non_none[0]
    return tp


class GetRequestSerializer(BaseModel):
    @field_serializer("*", mode="plain")
    def _serialize_list(self, v):
        if isinstance(v, list):
            parts = []
            for item in v:
                if isinstance(item, Enum):
                    parts.append(item.value)
                else:
                    parts.append(str(item))
            return ",".join(parts)
        return v


class SpApiBaseModel(BaseModel):
    """
    Base Model for SP API pydantic models, used by all models
    """

    def model_dump(
        self,
        *,
        mode: Literal["json", "python"] | str = "json",
        include: IncEx | None = None,
        exclude: IncEx | None = None,
        context: Any | None = None,
        by_alias: bool | None = None,
        exclude_unset: bool = True,
        exclude_defaults: bool = False,
        exclude_none: bool = False,
        round_trip: bool = False,
        warnings: bool | Literal["none", "warn", "error"] = True,
        fallback: Callable[[Any], Any] | None = None,
        serialize_as_any: bool = False,
    ) -> dict[str, Any]:
        return super().model_dump(
            mode=mode,
            include=include,
            exclude=exclude,
            context=context,
            by_alias=by_alias,
            exclude_unset=exclude_unset,
            exclude_defaults=exclude_defaults,
            exclude_none=exclude_none,
            round_trip=round_trip,
            warnings=warnings,
            fallback=fallback,
            serialize_as_any=serialize_as_any,
        )


class PathParam:
    pass


class QueryParam:
    pass


class BodyParam:
    pass


class RequestsBaseModel(SpApiBaseModel):
    """
    Base model class for request models.

    This class can be customized with any special behavior needed for request models.
    """

    model_config = ConfigDict(
        populate_by_name=True,  # Allow populating models using original property names
        extra="ignore",  # Ignore extra fields in request payloads
    )

    def create_request(self, path: str, class_marketplace: Union[Marketplaces, str]):
        path_params: dict[str, Any] = {}
        body: dict[str, Any] = {}
        query: dict[str, Any] = {}

        hint_map = get_type_hints(type(self), include_extras=True)
        # auto-fill marketplace field if unset
        for field_name, hint in hint_map.items():
            # unwrap Annotated types to get the real annotation
            base_hint = _unwrap_annotated(hint)

            if "marketplace" in field_name.lower():
                if field_name not in self.model_fields_set:
                    origin = get_origin(base_hint)

                    # choose list or single value based on annotation
                    if origin is list:
                        val = [
                            (
                                class_marketplace.marketplace_id
                                if isinstance(class_marketplace, Enum)
                                else class_marketplace
                            )
                        ]
                    else:
                        val = (
                            class_marketplace.marketplace_id
                            if isinstance(class_marketplace, Enum)
                            else class_marketplace
                        )
                    # set attribute and mark as provided
                    setattr(self, field_name, val)
                    self.model_fields_set.add(field_name)
                break

        data = self.model_dump()

        dests: dict[type, dict] = {
            PathParam: path_params,
            QueryParam: query,
            BodyParam: body,
        }

        for field_name, hint in hint_map.items():
            # unwrap Annotated types to get the real annotation
            for meta in getattr(hint, "__metadata__", ()):
                dest = dests.get(type(meta), None)
                if dest is None:
                    continue
                info = self.model_fields[field_name]
                key = info.serialization_alias or field_name

                if field_name in self.model_fields_set:
                    dest[key] = data[key]
                elif not info.is_required:
                    val = getattr(self, field_name)
                    if val is not None:
                        dest[key] = val
                break

        return path.format(**path_params), body.get("body", body), query
