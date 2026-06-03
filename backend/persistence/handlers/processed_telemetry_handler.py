from backend.persistence.handlers.base_handler import (
    BasePersistenceHandler
)

from backend.services.telemetry.processed_telemetry_service import (
    ProcessedTelemetryService
)


class ProcessedTelemetryPersistenceHandler(
    BasePersistenceHandler
):

    def __init__(
        self,
        service: ProcessedTelemetryService,
    ):
        self.service = service

    async def persist(
        self,
        payload: dict,
    ) -> None:

        await self.service.create_from_event(
            payload
        )