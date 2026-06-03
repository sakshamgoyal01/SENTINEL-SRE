from backend.persistence.handlers.base_handler import (
    BasePersistenceHandler
)

from backend.services.intelligence.knowledge_service import (
    KnowledgeService
)


class KnowledgePersistenceHandler(
    BasePersistenceHandler
):

    def __init__(
        self,
        service: KnowledgeService,
    ):
        self.service = service

    async def persist(
        self,
        payload: dict,
    ) -> None:

        await self.service.create_from_event(
            payload
        )