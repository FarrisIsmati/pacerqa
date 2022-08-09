from typing import Any, Mapping, Optional, TypedDict


class BuildBaseUrlProps(TypedDict):
    url: str
    path: str
    query: Optional[Mapping[Any, Any]]
