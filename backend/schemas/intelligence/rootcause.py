from pydantic import BaseModel


class CreateRootCauseRequest(BaseModel):
    rootcause_id: str
    investigation_id: str
    service: str
    severity: str
    priority: str
    root_cause: dict
    causal_chain: dict
    evidence: list
    confidence: float


class UpdateRootCauseRequest(BaseModel):
    service: str | None = None
    severity: str | None = None
    priority: str | None = None
    root_cause: dict | None = None
    causal_chain: dict | None = None
    evidence: list | None = None
    confidence: float | None = None


class RootCauseResponse(BaseModel):
    id: str
    rootcause_id: str
    investigation_id: str
    service: str
    severity: str
    priority: str
    root_cause: dict
    causal_chain: dict
    evidence: list
    confidence: float

    model_config = {
        "from_attributes": True
    }