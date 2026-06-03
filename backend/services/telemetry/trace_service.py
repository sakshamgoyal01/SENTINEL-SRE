from backend.services.base_service import (
    BaseService
)

from backend.models.telemetry.trace import Trace


class TraceService(
    BaseService
):

    async def create_from_event(
        self,
        payload: dict,
    ) -> Trace:

        trace = Trace(
            timestamp=payload["timestamp"],
            trace_id=payload["trace_id"],
            span_id=payload["span_id"],
            parent_span_id=payload.get(
                "parent_span_id"
            ),
            service=payload["service"],
            operation=payload["operation"],
            duration_ms=payload[
                "duration_ms"
            ],
            status_code=payload.get(
                "status_code"
            ),
        )

        return await (
            self.repository.create(
                trace
            )
        )