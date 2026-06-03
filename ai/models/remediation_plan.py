from pydantic import BaseModel

from ai.models.remediation_action import (
    RemediationAction
)


class RemediationPlan(BaseModel):

    runbook: str

    actions: list[RemediationAction]