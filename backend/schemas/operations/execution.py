from pydantic import BaseModel


class CreateExecutionRequest(BaseModel):
    execution_id: str
    approval_id: str | None = None
    service: str
    executed: bool
    status: str
    mode: str
    actions: list


class UpdateExecutionRequest(BaseModel):
    executed: bool | None = None
    status: str | None = None
    mode: str | None = None
    actions: list | None = None


class ExecutionResponse(BaseModel):
    id: str
    execution_id: str
    approval_id: str | None
    service: str
    executed: bool
    status: str
    mode: str
    actions: list

    model_config = {
        "from_attributes": True
    }