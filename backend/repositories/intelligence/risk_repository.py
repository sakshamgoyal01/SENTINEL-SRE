from sqlalchemy.ext.asyncio import AsyncSession

from backend.models.intelligence.risk import Risk

from backend.repositories.base_repository import (
    BaseRepository
)


class RiskRepository(
    BaseRepository[Risk]
):

    def __init__(
        self,
        session: AsyncSession
    ):
        super().__init__(
            session=session,
            model=Risk
        )