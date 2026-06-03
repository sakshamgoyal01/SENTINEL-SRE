from ingestion.models.base_event import BaseEvent

from ingestion.models.enums import SeverityLevel


class LogEvent(BaseEvent):

    service: str

    severity: SeverityLevel

    message: str

    trace_id: str | None = None

    span_id: str | None = None

    logger: str | None = None