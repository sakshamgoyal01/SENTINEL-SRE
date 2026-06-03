from datetime import datetime

from pydantic import BaseModel

from ai.models.escalation_target import (
    EscalationTarget
)


class EscalationRecord(
    BaseModel
):

    escalation_id: str

    service: str

    recovery_id: str

    escalation_reason: str

    target: EscalationTarget

    generated_at: datetime