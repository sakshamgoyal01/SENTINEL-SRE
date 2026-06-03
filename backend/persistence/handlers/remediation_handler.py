from backend.persistence.handlers.base_handler import (
    BasePersistenceHandler
)

from backend.services.intelligence.remediation_service import (
    RemediationService
)


class RemediationPersistenceHandler(
    BasePersistenceHandler
):

    def __init__(
        self,
        service: RemediationService,
    ):
        self.service = service

    async def persist(
        self,
        payload: dict,
    ) -> None:

        await self.service.create_from_event(
            payload
        )