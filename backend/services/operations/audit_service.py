from backend.services.base_service import (
    BaseService
)

from backend.models.operations.execution_audit import (
    ExecutionAudit
)


class AuditService(
    BaseService
):

    async def create_from_event(
        self,
        payload: dict,
    ) -> ExecutionAudit:

        entity = ExecutionAudit(
            **payload
        )

        return await (
            self.repository.create(
                entity
            )
        )