from pydantic import BaseModel


class CreateRecoveryRequest(BaseModel):
    recovery_id: str
    verification_id: str
    service: str
    recovery_status: str
    strategy: dict


class UpdateRecoveryRequest(BaseModel):
    recovery_status: str | None = None
    strategy: dict | None = None


class RecoveryResponse(BaseModel):
    id: str
    recovery_id: str
    verification_id: str
    service: str
    recovery_status: str
    strategy: dict

    model_config = {
        "from_attributes": True
    }