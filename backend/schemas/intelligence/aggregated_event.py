from datetime import datetime

from pydantic import BaseModel


class AggregatedEventResponse(BaseModel):
    id: str
    aggregation_key: str
    category: str
    severity: str
    count: int
    services: list
    summary: str
    created_at_event: datetime | None

    model_config = {
        "from_attributes": True
    }