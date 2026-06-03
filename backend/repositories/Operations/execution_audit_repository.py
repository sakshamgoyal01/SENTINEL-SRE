from sqlalchemy.ext.asyncio import AsyncSession

from backend.models.operations.execution_audit import (
    ExecutionAudit
)

from backend.repositories.base_repository import (
    BaseRepository
)


class ExecutionAuditRepository(
    BaseRepository[ExecutionAudit]
):

    def __init__(
        self,
        session: AsyncSession
    ):
        super().__init__(
            session=session,
            model=ExecutionAudit
        )