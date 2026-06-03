from datetime import datetime

from pydantic import BaseModel


class CreateKnowledgeRequest(BaseModel):
    knowledge_id: str
    service: str
    pattern: dict
    remediation: dict
    source_incident_type: str | None = None
    success_rate: float | None = None
    created_at_event: datetime


class UpdateKnowledgeRequest(BaseModel):
    pattern: dict | None = None
    remediation: dict | None = None
    source_incident_type: str | None = None
    success_rate: float | None = None


class KnowledgeResponse(BaseModel):
    id: str
    knowledge_id: str
    service: str
    pattern: dict
    remediation: dict
    source_incident_type: str | None
    success_rate: float | None
    created_at_event: datetime

    model_config = {
        "from_attributes": True
    }