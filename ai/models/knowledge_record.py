from datetime import datetime

from pydantic import BaseModel

from ai.models.incident_pattern import (
    IncidentPattern
)

from ai.models.remediation_outcome import (
    RemediationOutcome
)


class KnowledgeRecord(BaseModel):

    knowledge_id: str

    service: str

    pattern: IncidentPattern

    remediation: RemediationOutcome

    created_at: datetime