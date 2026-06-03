from pydantic import BaseModel


class CreateEscalationRequest(BaseModel):
    escalation_id: str
    recovery_id: str
    service: str
    escalation_reason: str
    target: dict


class UpdateEscalationRequest(BaseModel):
    escalation_reason: str | None = None
    target: dict | None = None


class EscalationResponse(BaseModel):
    id: str
    escalation_id: str
    recovery_id: str
    service: str
    escalation_reason: str
    target: dict

    model_config = {
        "from_attributes": True
    }