from backend.services.base_service import (
    BaseService
)

from backend.models.intelligence.remediation import (
    Remediation
)


class RemediationService(
    BaseService
):

    async def create_from_event(
        self,
        payload: dict,
    ) -> Remediation:

        entity = Remediation(
            **payload
        )

        return await (
            self.repository.create(
                entity
            )
        )