from pydantic import BaseModel


class CreateRemediationRequest(BaseModel):
    remediation_id: str
    risk_id: str
    service: str
    priority: str
    plan: dict


class UpdateRemediationRequest(BaseModel):
    service: str | None = None
    priority: str | None = None
    plan: dict | None = None


class RemediationResponse(BaseModel):
    id: str
    remediation_id: str
    risk_id: str
    service: str
    priority: str
    plan: dict

    model_config = {
        "from_attributes": True
    }