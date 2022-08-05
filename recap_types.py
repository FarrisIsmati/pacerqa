from typing import Any, Mapping, TypedDict


class BuildBaseUrlProps(TypedDict):
    url: str
    path: str
    query: Mapping[Any, Any]
