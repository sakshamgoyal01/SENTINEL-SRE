from sqlalchemy.ext.asyncio import AsyncSession

from backend.models.telemetry.log import Log

from backend.repositories.base_repository import (
    BaseRepository
)


class LogRepository(
    BaseRepository[Log]
):

    def __init__(
        self,
        session: AsyncSession
    ):
        super().__init__(
            session=session,
            model=Log
        )