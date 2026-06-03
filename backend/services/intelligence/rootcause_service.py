from backend.services.base_service import (
    BaseService
)

from backend.models.intelligence.root_cause import (
    RootCause
)


class RootCauseService(
    BaseService
):

    async def create_from_event(
        self,
        payload: dict,
    ) -> RootCause:

        entity = RootCause(
            **payload
        )

        return await (
            self.repository.create(
                entity
            )
        )