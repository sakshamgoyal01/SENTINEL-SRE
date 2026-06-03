from typing import Any, Dict

from ingestion.models.base_event import BaseEvent

from processing.models.operational_context import (
    OperationalContext
)


class OperationalEvent(BaseEvent):

    event_type: str

    category: str

    severity: str

    priority: str

    risk_score: float

    summary: str

    service: str
    event_family: str | None = None

    operational_type: str | None = None

    business_domain: str | None = None

    operational_context: OperationalContext

    raw_event: Dict[str, Any]