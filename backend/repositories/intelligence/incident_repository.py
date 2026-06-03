from sqlalchemy.ext.asyncio import AsyncSession

from backend.models.intelligence.incident import (
    Incident
)

from backend.repositories.base_repository import (
    BaseRepository
)


class IncidentRepository(
    BaseRepository[Incident]
):

    def __init__(
        self,
        session: AsyncSession
    ):
        super().__init__(
            session=session,
            model=Incident
        )
        