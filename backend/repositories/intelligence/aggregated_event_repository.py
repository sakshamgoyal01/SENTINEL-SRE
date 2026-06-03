from backend.models.intelligence.aggregated_event import (
    AggregatedEvent
)

from backend.repositories.base_repository import (
    BaseRepository
)


class AggregatedEventRepository(
    BaseRepository[AggregatedEvent]
):

    def __init__(
        self,
        session,
    ):
        super().__init__(
            session=session,
            model=AggregatedEvent,
        )