from backend.persistence.handlers.base_handler import (
    BasePersistenceHandler
)

from backend.services.intelligence.incident_service import (
    IncidentService
)


class IncidentPersistenceHandler(
    BasePersistenceHandler
):

    def __init__(
        self,
        service: IncidentService,
    ):
        self.service = service

    async def persist(
        self,
        payload: dict,
    ) -> None:

        await self.service.create_from_event(
            payload
        )