from backend.services.base_service import (
    BaseService
)

from backend.models.intelligence.executive_report import (
    ExecutiveReport
)


class ExecutiveReportService(
    BaseService
):

    async def create_from_event(
        self,
        payload: dict,
    ) -> ExecutiveReport:

        entity = ExecutiveReport(
            **payload
        )

        return await (
            self.repository.create(
                entity
            )
        )