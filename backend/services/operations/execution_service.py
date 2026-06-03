from backend.services.base_service import (
    BaseService
)

from backend.models.operations.execution import (
    Execution
)


class ExecutionService(
    BaseService
):

    async def create_from_event(
        self,
        payload: dict,
    ) -> Execution:

        entity = Execution(
            **payload
        )

        return await (
            self.repository.create(
                entity
            )
        )