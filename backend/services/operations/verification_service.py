from backend.services.base_service import (
    BaseService
)

from backend.models.operations.verification import (
    Verification
)


class VerificationService(
    BaseService
):

    async def create_from_event(
        self,
        payload: dict,
    ) -> Verification:

        entity = Verification(
            **payload
        )

        return await (
            self.repository.create(
                entity
            )
        )