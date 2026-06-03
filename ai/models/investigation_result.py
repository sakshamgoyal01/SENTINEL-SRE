from datetime import datetime
from pydantic import BaseModel

from ai.models.evidence import (
    Evidence
)

from ai.models.timeline_event import (
    TimelineEvent
)


class InvestigationResult(BaseModel):

    investigation_id: str

    service: str

    severity: str

    priority: str

    summary: str

    findings: list[str]

    evidence: list[Evidence]

    timeline: list[TimelineEvent]

    confidence: float

    generated_at: datetime