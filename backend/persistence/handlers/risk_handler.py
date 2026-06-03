from backend.persistence.handlers.base_handler import (
    BasePersistenceHandler
)

from backend.services.intelligence.risk_service import (
    RiskService
)


class RiskPersistenceHandler(
    BasePersistenceHandler
):

    def __init__(
        self,
        service: RiskService,
    ):
        self.service = service

    async def persist(
        self,
        payload: dict,
    ) -> None:

        await self.service.create_from_event(
            payload
        )