from ingestion.models.base_event import BaseEvent


class TraceEvent(BaseEvent):

    trace_id: str

    span_id: str

    parent_span_id: str | None = None

    service: str

    operation: str

    duration_ms: float

    status_code: int | None = None