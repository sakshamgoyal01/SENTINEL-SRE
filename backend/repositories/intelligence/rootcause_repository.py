from sqlalchemy.ext.asyncio import AsyncSession

from backend.models.intelligence.root_cause import (
    RootCause
)

from backend.repositories.base_repository import (
    BaseRepository
)


class RootCauseRepository(
    BaseRepository[RootCause]
):

    def __init__(
        self,
        session: AsyncSession
    ):
        super().__init__(
            session=session,
            model=RootCause
        )