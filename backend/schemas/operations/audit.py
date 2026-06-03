from pydantic import BaseModel


class CreateAuditRequest(BaseModel):
    audit_id: str
    service: str
    approval_id: str | None = None
    execution_id: str | None = None
    verification_id: str | None = None
    recovery_id: str | None = None
    status: str
    details: str


class UpdateAuditRequest(BaseModel):
    status: str | None = None
    details: str | None = None


class AuditResponse(BaseModel):
    id: str
    audit_id: str
    service: str
    approval_id: str | None
    execution_id: str | None
    verification_id: str | None
    recovery_id: str | None
    status: str
    details: str

    model_config = {
        "from_attributes": True
    }