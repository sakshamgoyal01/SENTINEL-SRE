from pydantic import Field

from ingestion.models.base_event import BaseEvent


class MetricEvent(BaseEvent):

    service: str

    metric_name: str

    value: float

    labels: dict = Field(default_factory=dict)

    unit: str | None = None