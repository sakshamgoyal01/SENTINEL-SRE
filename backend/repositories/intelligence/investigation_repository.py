from sqlalchemy.ext.asyncio import AsyncSession

from backend.models.intelligence.investigation import (
    Investigation
)

from backend.repositories.base_repository import (
    BaseRepository
)


class InvestigationRepository(
    BaseRepository[Investigation]
):

    def __init__(
        self,
        session: AsyncSession
    ):
        super().__init__(
            session=session,
            model=Investigation
        )