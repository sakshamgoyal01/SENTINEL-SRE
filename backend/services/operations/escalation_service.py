from backend.services.base_service import (
    BaseService
)

from backend.models.operations.escalation import (
    Escalation
)


class EscalationService(
    BaseService
):

    async def create_from_event(
        self,
        payload: dict,
    ) -> Escalation:

        entity = Escalation(
            **payload
        )

        return await (
            self.repository.create(
                entity
            )
        )