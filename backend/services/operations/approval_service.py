from backend.services.base_service import (
    BaseService
)

from backend.models.operations.approval import (
    Approval
)


class ApprovalService(
    BaseService
):

    async def create_from_event(
        self,
        payload: dict,
    ) -> Approval:

        entity = Approval(
            **payload
        )

        return await (
            self.repository.create(
                entity
            )
        )