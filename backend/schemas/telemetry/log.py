from pydantic import BaseModel


class CreateLogRequest(BaseModel):
    service: str
    level: str
    message: str
    trace_id: str | None = None
    span_id: str | None = None
    logger: str | None = None


class UpdateLogRequest(BaseModel):
    level: str | None = None
    message: str | None = None


class LogResponse(BaseModel):
    id: str
    service: str
    level: str
    message: str
    trace_id: str | None
    span_id: str | None

    model_config = {
        "from_attributes": True
    }