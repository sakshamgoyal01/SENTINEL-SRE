from datetime import datetime

from pydantic import BaseModel

from ai.models.blast_radius import (
    BlastRadius
)

from ai.models.impact_assessment import (
    ImpactAssessment
)

from ai.models.risk_summary import (
    RiskSummary
)


class RiskResult(BaseModel):

    risk_id: str

    rootcause_id: str

    service: str

    priority: str

    blast_radius: BlastRadius

    impact_assessment: ImpactAssessment

    risk_summary: RiskSummary

    generated_at: datetime