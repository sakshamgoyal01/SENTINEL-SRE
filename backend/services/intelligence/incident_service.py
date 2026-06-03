from backend.services.base_service import (
    BaseService
)

from backend.models.intelligence.incident import (
    Incident
)


class IncidentService(
    BaseService
):

    async def create_from_event(
        self,
        payload: dict,
    ) -> Incident:

        incident = Incident(
            **payload
        )

        return await (
            self.repository.create(
                incident
            )
        )