from backend.models.telemetry.processed_telemetry import (
    ProcessedTelemetry
)

from backend.repositories.base_repository import (
    BaseRepository
)


class ProcessedTelemetryRepository(
    BaseRepository[ProcessedTelemetry]
):

    def __init__(
        self,
        session,
    ):
        super().__init__(
            session=session,
            model=ProcessedTelemetry,
        )