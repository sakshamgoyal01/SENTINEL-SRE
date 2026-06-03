from backend.persistence.handlers.base_handler import (
    BasePersistenceHandler
)

from backend.services.intelligence.aggregated_event_service import (
    AggregatedEventService
)


class AggregatedEventPersistenceHandler(
    BasePersistenceHandler
):

    def __init__(
        self,
        service: AggregatedEventService,
    ):
        self.service = service

    async def persist(
        self,
        payload: dict,
    ) -> None:

        await self.service.create_from_event(
            payload
        )