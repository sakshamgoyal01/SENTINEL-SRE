from backend.persistence.handlers.base_handler import (
    BasePersistenceHandler
)

from backend.services.operations.execution_service import (
    ExecutionService
)


class ExecutionPersistenceHandler(
    BasePersistenceHandler
):

    def __init__(
        self,
        service: ExecutionService,
    ):
        self.service = service

    async def persist(
        self,
        payload: dict,
    ) -> None:

        await self.service.create_from_event(
            payload
        )