from backend.persistence.handlers.base_handler import (
    BasePersistenceHandler
)

from backend.services.telemetry.deployment_service import (
    DeploymentService
)


class DeploymentPersistenceHandler(
    BasePersistenceHandler
):

    def __init__(
        self,
        service: DeploymentService,
    ):
        self.service = service

    async def persist(
        self,
        payload: dict,
    ) -> None:

        await self.service.create_from_event(
            payload
        )