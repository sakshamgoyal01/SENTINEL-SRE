from backend.persistence.handlers.base_handler import (
    BasePersistenceHandler
)

from backend.services.telemetry.metric_service import (
    MetricService
)


class MetricPersistenceHandler(
    BasePersistenceHandler
):

    def __init__(
        self,
        service: MetricService,
    ):
        self.service = service

    async def persist(
        self,
        payload: dict,
    ) -> None:

        await self.service.create_from_event(
            payload
        )