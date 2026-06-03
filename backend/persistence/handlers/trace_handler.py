from backend.persistence.handlers.base_handler import (
    BasePersistenceHandler
)

from backend.services.telemetry.trace_service import (
    TraceService
)


class TracePersistenceHandler(
    BasePersistenceHandler
):

    def __init__(
        self,
        service: TraceService,
    ):
        self.service = service

    async def persist(
        self,
        payload: dict,
    ) -> None:

        await self.service.create_from_event(
            payload
        )