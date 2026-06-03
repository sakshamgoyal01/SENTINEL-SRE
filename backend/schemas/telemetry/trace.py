from pydantic import BaseModel


class CreateTraceRequest(BaseModel):
    trace_id: str
    span_id: str
    service: str
    operation: str
    duration_ms: float


class UpdateTraceRequest(BaseModel):
    operation: str | None = None
    duration_ms: float | None = None


class TraceResponse(BaseModel):
    id: str
    trace_id: str
    span_id: str
    service: str
    operation: str
    duration_ms: float

    model_config = {
        "from_attributes": True
    }