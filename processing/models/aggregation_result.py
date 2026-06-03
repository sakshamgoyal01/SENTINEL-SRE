from pydantic import BaseModel

from processing.models.aggregated_event import (
    AggregatedEvent
)


class AggregationResult(BaseModel):

    triggered: bool = False

    aggregated_event: (
        AggregatedEvent | None
    ) = None