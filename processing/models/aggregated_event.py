from datetime import datetime
from pydantic import BaseModel


class AggregatedEvent(BaseModel):

    aggregation_key: str

    category: str

    severity: str

    count: int

    first_seen: datetime

    last_seen: datetime

    services: list[str]

    summary: str

    risk_score: float

    source_events: int