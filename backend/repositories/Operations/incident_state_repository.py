from sqlalchemy.ext.asyncio import AsyncSession

from backend.models.operations.incident_state import (
    IncidentState
)

from backend.repositories.base_repository import (
    BaseRepository
)


class IncidentStateRepository(
    BaseRepository[IncidentState]
):

    def __init__(
        self,
        session: AsyncSession
    ):
        super().__init__(
            session=session,
            model=IncidentState
        )