from backend.persistence.handlers.base_handler import (
    BasePersistenceHandler
)

from backend.services.operations.verification_service import (
    VerificationService
)


class VerificationPersistenceHandler(
    BasePersistenceHandler
):

    def __init__(
        self,
        service: VerificationService,
    ):
        self.service = service

    async def persist(
        self,
        payload: dict,
    ) -> None:

        await self.service.create_from_event(
            payload
        )