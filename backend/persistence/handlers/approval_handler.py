from backend.persistence.handlers.base_handler import (
    BasePersistenceHandler
)

from backend.services.operations.approval_service import (
    ApprovalService
)


class ApprovalPersistenceHandler(
    BasePersistenceHandler
):

    def __init__(
        self,
        service: ApprovalService,
    ):
        self.service = service

    async def persist(
        self,
        payload: dict,
    ) -> None:

        await self.service.create_from_event(
            payload
        )