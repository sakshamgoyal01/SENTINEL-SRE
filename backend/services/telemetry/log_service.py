from backend.services.base_service import (
    BaseService
)

from backend.models.telemetry.log import Log


class LogService(
    BaseService
):

    async def create_from_event(
        self,
        payload: dict,
    ) -> Log:

        log = Log(
            event_id=payload["event_id"],
            timestamp=payload["timestamp"],
            service=payload["service"],
            severity=payload["severity"],
            message=payload["message"],
            trace_id=payload.get(
                "trace_id"
            ),
            span_id=payload.get(
                "span_id"
            ),
            logger=payload.get(
                "logger"
            ),
        )

        return await (
            self.repository.create(
                log
            )
        )