from backend.services.base_service import (
    BaseService
)

from backend.models.operations.incident_state import (
    IncidentState
)


class IncidentStateService(
    BaseService
):

    async def create_from_event(
        self,
        payload: dict,
    ) -> IncidentState:

        entity = IncidentState(
            **payload
        )

        return await (
            self.repository.create(
                entity
            )
        )