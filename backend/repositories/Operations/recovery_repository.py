from sqlalchemy.ext.asyncio import AsyncSession

from backend.models.operations.recovery import (
    Recovery
)

from backend.repositories.base_repository import (
    BaseRepository
)


class RecoveryRepository(
    BaseRepository[Recovery]
):

    def __init__(
        self,
        session: AsyncSession
    ):
        super().__init__(
            session=session,
            model=Recovery
        )