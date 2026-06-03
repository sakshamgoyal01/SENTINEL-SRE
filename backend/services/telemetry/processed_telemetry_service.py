from backend.services.base_service import (
    BaseService
)

from backend.models.telemetry.processed_telemetry import (
    ProcessedTelemetry
)


class ProcessedTelemetryService(
    BaseService
):

    async def create_from_event(
        self,
        payload: dict,
    ) -> ProcessedTelemetry:

        entity = ProcessedTelemetry(
            event_id=payload["event_id"],
            event_type=payload["event_type"],
            category=payload["category"],
            severity=payload["severity"],
            priority=payload["priority"],
            risk_score=payload["risk_score"],
            service=payload["service"],
            summary=payload["summary"],
            raw_event=payload["raw_event"],
            created_at_event=payload.get(
                "created_at_event"
            ),
        )

        return await (
            self.repository.create(
                entity
            )
        )