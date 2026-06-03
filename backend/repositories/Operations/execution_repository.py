from sqlalchemy.ext.asyncio import AsyncSession

from backend.models.operations.execution import (
    Execution
)

from backend.repositories.base_repository import (
    BaseRepository
)


class ExecutionRepository(
    BaseRepository[Execution]
):

    def __init__(
        self,
        session: AsyncSession
    ):
        super().__init__(
            session=session,
            model=Execution
        )