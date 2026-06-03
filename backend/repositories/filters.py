from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class FilterParams:

    search: str | None = None

    service: str | None = None

    status: str | None = None

    severity: str | None = None

    priority: str | None = None

    start_date: datetime | None = None

    end_date: datetime | None = None