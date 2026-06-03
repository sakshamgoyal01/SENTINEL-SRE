from pydantic import BaseModel


class CreateVerificationRequest(BaseModel):
    verification_id: str
    execution_id: str
    service: str
    verified: bool
    health_status: str
    verification_result: str
    checks: list


class UpdateVerificationRequest(BaseModel):
    verified: bool | None = None
    health_status: str | None = None
    verification_result: str | None = None
    checks: list | None = None


class VerificationResponse(BaseModel):
    id: str
    verification_id: str
    execution_id: str
    service: str
    verified: bool
    health_status: str
    verification_result: str
    checks: list

    model_config = {
        "from_attributes": True
    }