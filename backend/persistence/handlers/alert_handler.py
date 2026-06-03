from backend.persistence.handlers.base_handler import (
    BasePersistenceHandler
)

from backend.services.intelligence.alert_service import (
    AlertService
)


class AlertPersistenceHandler(
    BasePersistenceHandler
):

    def __init__(
        self,
        service: AlertService,
    ):
        self.service = service

    async def persist(
        self,
        payload: dict,
    ) -> None:

        await self.service.create_from_event(
            payload
        )