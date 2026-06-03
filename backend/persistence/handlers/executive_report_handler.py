from backend.persistence.handlers.base_handler import (
    BasePersistenceHandler
)

from backend.services.intelligence.executive_report_service import (
    ExecutiveReportService
)


class ExecutiveReportPersistenceHandler(
    BasePersistenceHandler
):

    def __init__(
        self,
        service: ExecutiveReportService,
    ):
        self.service = service

    async def persist(
        self,
        payload: dict,
    ) -> None:

        await self.service.create_from_event(
            payload
        )