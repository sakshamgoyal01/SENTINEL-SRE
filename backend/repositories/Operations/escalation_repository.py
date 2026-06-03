from sqlalchemy.ext.asyncio import AsyncSession

from backend.models.operations.escalation import (
    Escalation
)

from backend.repositories.base_repository import (
    BaseRepository
)


class EscalationRepository(
    BaseRepository[Escalation]
):

    def __init__(
        self,
        session: AsyncSession
    ):
        super().__init__(
            session=session,
            model=Escalation
        )