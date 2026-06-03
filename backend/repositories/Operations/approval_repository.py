from sqlalchemy.ext.asyncio import AsyncSession

from backend.models.operations.approval import (
    Approval
)

from backend.repositories.base_repository import (
    BaseRepository
)


class ApprovalRepository(
    BaseRepository[Approval]
):

    def __init__(
        self,
        session: AsyncSession
    ):
        super().__init__(
            session=session,
            model=Approval
        )