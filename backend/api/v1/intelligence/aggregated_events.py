from backend.api.read_only_router import ReadOnlyRouter
from backend.api.dependencies.aggregated_event import (
    get_aggregated_event_service
)
from backend.schemas.intelligence.aggregated_event import (
    AggregatedEventResponse
)

router = ReadOnlyRouter(
    service_dependency=get_aggregated_event_service,
    response_schema=AggregatedEventResponse,
    prefix="",
    tags=["Aggregated Events"],
).router