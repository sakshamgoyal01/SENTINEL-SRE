from sqlalchemy.ext.asyncio import AsyncSession

from backend.models.telemetry.trace import Trace

from backend.repositories.base_repository import (
    BaseRepository
)


class TraceRepository(
    BaseRepository[Trace]
):

    def __init__(
        self,
        session: AsyncSession
    ):
        super().__init__(
            session=session,
            model=Trace
        )