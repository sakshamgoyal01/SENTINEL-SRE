from datetime import datetime

from pydantic import BaseModel

from ai.models.remediation_plan import (
    RemediationPlan
)


class RemediationResult(BaseModel):

    remediation_id: str

    risk_id: str

    service: str

    priority: str

    plan: RemediationPlan

    generated_at: datetime