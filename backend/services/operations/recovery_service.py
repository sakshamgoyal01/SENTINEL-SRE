from backend.services.base_service import (
    BaseService
)

from backend.models.operations.recovery import (
    Recovery
)


class RecoveryService(
    BaseService
):

    async def create_from_event(
        self,
        payload: dict,
    ) -> Recovery:

        entity = Recovery(
            **payload
        )

        return await (
            self.repository.create(
                entity
            )
        )