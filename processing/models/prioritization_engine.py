from pydantic import BaseModel

from processing.models.aggregated_event import (
    AggregatedEvent
)


class PrioritizedEvent(BaseModel):

    incident_priority: str

    impact_score: float

    final_risk_score: float

    requires_human_review: bool

    escalation_required: bool

    aggregated_event: AggregatedEvent