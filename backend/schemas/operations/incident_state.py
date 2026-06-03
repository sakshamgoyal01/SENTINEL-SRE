from datetime import datetime

from pydantic import BaseModel


class CreateIncidentStateRequest(BaseModel):
    incident_id: str
    service: str
    current_state: str
    source_topic: str
    updated_at_event: datetime


class UpdateIncidentStateRequest(BaseModel):
    current_state: str | None = None
    source_topic: str | None = None
    updated_at_event: datetime | None = None


class IncidentStateResponse(BaseModel):
    id: str
    incident_id: str
    service: str
    current_state: str
    source_topic: str
    updated_at_event: datetime

    model_config = {
        "from_attributes": True
    }