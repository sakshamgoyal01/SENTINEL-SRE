from ingestion.models.base_event import BaseEvent

from ingestion.models.enums import SeverityLevel


class IncidentEvent(BaseEvent):

    incident_id: str

    service: str

    severity: SeverityLevel

    title: str

    description: str

    status: str = "open"

    root_metric: str | None = None

    correlated_events: list[str] = []

    suspected_cause: str | None = None