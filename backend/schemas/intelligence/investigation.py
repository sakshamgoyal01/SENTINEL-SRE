from pydantic import BaseModel


class CreateInvestigationRequest(BaseModel):
    investigation_id: str
    incident_id: str | None = None
    service: str
    severity: str
    priority: str
    findings: dict
    evidence: list
    confidence: float


class UpdateInvestigationRequest(BaseModel):
    incident_id: str | None = None
    service: str | None = None
    severity: str | None = None
    priority: str | None = None
    findings: dict | None = None
    evidence: list | None = None
    confidence: float | None = None


class InvestigationResponse(BaseModel):
    id: str
    investigation_id: str
    incident_id: str | None
    service: str
    severity: str
    priority: str
    findings: dict
    evidence: list
    confidence: float

    model_config = {
        "from_attributes": True
    }