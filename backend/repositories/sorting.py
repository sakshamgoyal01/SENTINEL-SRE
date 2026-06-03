from dataclasses import dataclass


@dataclass(slots=True)
class SortParams:
    sort_by: str = "created_at"
    descending: bool = True