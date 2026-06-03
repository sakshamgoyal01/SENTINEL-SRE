from backend.persistence.handlers.base_handler import (
    BasePersistenceHandler
)

from backend.services.operations.audit_service import (
    AuditService
)


class AuditPersistenceHandler(
    BasePersistenceHandler
):

    def __init__(
        self,
        service: AuditService,
    ):
        self.service = service

    async def persist(
        self,
        payload: dict,
    ) -> None:

        await self.service.create_from_event(
            payload
        )