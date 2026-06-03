from sqlalchemy.ext.asyncio import AsyncSession

from backend.models.intelligence.remediation import (
    Remediation
)

from backend.repositories.base_repository import (
    BaseRepository
)


class RemediationRepository(
    BaseRepository[Remediation]
):

    def __init__(
        self,
        session: AsyncSession
    ):
        super().__init__(
            session=session,
            model=Remediation
        )