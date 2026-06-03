from pydantic import BaseModel


class RemediationAction(BaseModel):

    action_type: str

    priority: str

    description: str

    automated: bool