from pydantic import BaseModel


class ApprovalAction(BaseModel):

    action_type: str

    priority: str

    automated: bool