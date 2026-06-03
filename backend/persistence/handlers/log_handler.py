from backend.persistence.handlers.base_handler import (
    BasePersistenceHandler
)

from backend.services.telemetry.log_service import (
    LogService
)


class LogPersistenceHandler(
    BasePersistenceHandler
):

    def __init__(
        self,
        service: LogService,
    ):
        self.service = service

    async def persist(
        self,
        payload: dict,
    ) -> None:

        await self.service.create_from_event(
            payload
        )