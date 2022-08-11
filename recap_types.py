from typing import Any, Mapping, Optional, TypedDict, List


class BuildBaseUrlProps(TypedDict):
    url: str
    path: str
    query: Optional[Mapping[Any, Any]]


class RecapSearchResultResponseProps(TypedDict):
    absolute_url: str
    assignedTo: str
    assigned_to_id: int
    attachment_number: int
    attorney: List[str]
    attorney_id: List[int]
    caseName: str
    cause: str
    court: str
    court_citation_string: str
    court_exact: str
    court_id: str
    dateArgued: Optional[str]
    dateFiled: str
    dateTerminated: Optional[str]
    description: str
    docketNumber: str
    docket_absolute_url: str
    docket_entry_id: int
    docket_id: int
    document_number: int
    document_type: str
    entry_date_filed: str
    entry_number: int
    filepath_local: str
    firm: List[str]
    firm_id: List[int]
    id: int
    is_available: bool
    jurisdictionType: str
    juryDemand: str
    page_count: int
    party: List[str]
    party_id: List[int]
    referredTo: Optional[str]
    referred_to_id: Optional[str]
    short_description: str
    snippet: str
    suitNature: str
    timestamp: str


class RecapSearchResponseProps(TypedDict):
    count: int
    next: str
    previous: str or None
    results: List[RecapSearchResultResponseProps]
