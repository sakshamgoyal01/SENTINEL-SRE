from backend.persistence.handlers.base_handler import (
    BasePersistenceHandler
)

from backend.services.intelligence.investigation_service import (
    InvestigationService
)


class InvestigationPersistenceHandler(
    BasePersistenceHandler
):

    def __init__(
        self,
        service: InvestigationService,
    ):
        self.service = service

    async def persist(
        self,
        payload: dict,
    ) -> None:

        await self.service.create_from_event(
            payload
        )