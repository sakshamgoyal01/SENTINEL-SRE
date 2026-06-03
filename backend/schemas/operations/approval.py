from datetime import datetime

from pydantic import BaseModel


class CreateApprovalRequest(
    BaseModel
):

    approval_id: str

    service: str

    approved: bool

    requires_human_approval: bool

    reason: str

    actions: list

    generated_at: datetime


class UpdateApprovalRequest(
    BaseModel
):

    approved: bool | None = None

    reason: str | None = None


class ApprovalResponse(
    BaseModel
):

    id: str

    approval_id: str

    service: str

    approved: bool

    requires_human_approval: bool

    reason: str

    actions: list

    generated_at: datetime

    model_config = {
        "from_attributes": True
    }