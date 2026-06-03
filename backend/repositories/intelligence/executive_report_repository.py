from sqlalchemy.ext.asyncio import AsyncSession

from backend.models.intelligence.executive_report import (
    ExecutiveReport
)

from backend.repositories.base_repository import (
    BaseRepository
)


class ExecutiveReportRepository(
    BaseRepository[ExecutiveReport]
):

    def __init__(
        self,
        session: AsyncSession
    ):
        super().__init__(
            session=session,
            model=ExecutiveReport
        )