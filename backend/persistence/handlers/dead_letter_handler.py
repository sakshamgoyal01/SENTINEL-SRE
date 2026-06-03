from backend.persistence.handlers.base_handler import (
    BasePersistenceHandler
)

from backend.services.system.dead_letter_service import (
    DeadLetterService
)


class DeadLetterPersistenceHandler(
    BasePersistenceHandler
):

    def __init__(
        self,
        service: DeadLetterService,
    ):
        self.service = service

    async def persist(
        self,
        payload: dict,
    ) -> None:

        await self.service.create_from_event(
            payload
        )