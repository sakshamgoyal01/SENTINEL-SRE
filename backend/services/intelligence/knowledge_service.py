from backend.services.base_service import (
    BaseService
)

from backend.models.intelligence.knowledge_record import (
    KnowledgeRecord
)


class KnowledgeService(
    BaseService
):

    async def create_from_event(
        self,
        payload: dict,
    ) -> KnowledgeRecord:

        entity = KnowledgeRecord(
            **payload
        )

        return await (
            self.repository.create(
                entity
            )
        )