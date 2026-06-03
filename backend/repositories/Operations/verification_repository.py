from sqlalchemy.ext.asyncio import AsyncSession

from backend.models.operations.verification import (
    Verification
)

from backend.repositories.base_repository import (
    BaseRepository
)


class VerificationRepository(
    BaseRepository[Verification]
):

    def __init__(
        self,
        session: AsyncSession
    ):
        super().__init__(
            session=session,
            model=Verification
        )