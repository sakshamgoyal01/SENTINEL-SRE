from sqlalchemy.ext.asyncio import AsyncSession

from backend.models.intelligence.knowledge_record import (
    KnowledgeRecord
)

from backend.repositories.base_repository import (
    BaseRepository
)


class KnowledgeRepository(
    BaseRepository[KnowledgeRecord]
):

    def __init__(
        self,
        session: AsyncSession
    ):
        super().__init__(
            session=session,
            model=KnowledgeRecord
        )