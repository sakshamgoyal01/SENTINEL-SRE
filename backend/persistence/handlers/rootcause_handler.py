from backend.persistence.handlers.base_handler import (
    BasePersistenceHandler
)

from backend.services.intelligence.rootcause_service import (
    RootCauseService
)


class RootCausePersistenceHandler(
    BasePersistenceHandler
):

    def __init__(
        self,
        service: RootCauseService,
    ):
        self.service = service

    async def persist(
        self,
        payload: dict,
    ) -> None:

        await self.service.create_from_event(
            payload
        )