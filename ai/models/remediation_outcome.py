from pydantic import BaseModel


class RemediationOutcome(BaseModel):

    runbook: str

    actions: list[str]

    successful: bool

    automation_used: bool