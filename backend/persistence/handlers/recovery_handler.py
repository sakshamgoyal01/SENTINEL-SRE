from backend.persistence.handlers.base_handler import (
    BasePersistenceHandler
)

from backend.services.operations.recovery_service import (
    RecoveryService
)


class RecoveryPersistenceHandler(
    BasePersistenceHandler
):

    def __init__(
        self,
        service: RecoveryService,
    ):
        self.service = service

    async def persist(
        self,
        payload: dict,
    ) -> None:

        await self.service.create_from_event(
            payload
        )