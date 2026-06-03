from backend.persistence.handlers.base_handler import (
    BasePersistenceHandler
)

from backend.services.operations.escalation_service import (
    EscalationService
)


class EscalationPersistenceHandler(
    BasePersistenceHandler
):

    def __init__(
        self,
        service: EscalationService,
    ):
        self.service = service

    async def persist(
        self,
        payload: dict,
    ) -> None:

        await self.service.create_from_event(
            payload
        )