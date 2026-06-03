from backend.services.base_service import (
    BaseService
)

from backend.models.intelligence.investigation import (
    Investigation
)


class InvestigationService(
    BaseService
):

    async def create_from_event(
        self,
        payload: dict,
    ) -> Investigation:

        investigation = Investigation(
            **payload
        )

        return await (
            self.repository.create(
                investigation
            )
        )