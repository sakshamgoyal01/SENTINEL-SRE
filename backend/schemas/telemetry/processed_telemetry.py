from datetime import datetime

from pydantic import BaseModel


class ProcessedTelemetryResponse(BaseModel):
    id: str
    event_id: str
    event_type: str
    category: str
    severity: str
    priority: str
    risk_score: float
    service: str
    summary: str
    raw_event: dict
    created_at_event: datetime | None

    model_config = {
        "from_attributes": True
    }