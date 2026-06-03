from datetime import datetime

from pydantic import BaseModel

from ai.models.approval_action import (
    ApprovalAction
)


class ApprovalDecision(BaseModel):

    approval_id: str

    service: str

    approved: bool

    requires_human_approval: bool

    reason: str

    actions: list[ApprovalAction]

    generated_at: datetime