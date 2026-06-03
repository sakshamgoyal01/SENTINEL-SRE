import logging

from ingestion.messaging.producer import (
    send_event
)

from ingestion.messaging.topics import (
    PROCESSED_TELEMETRY_TOPIC
)

from processing.models.operational_event import (
    OperationalEvent
)

logger = logging.getLogger(
    "sentinel.processing.publisher"
)


class ProcessedEventPublisher:

    def publish(
        self,
        event: OperationalEvent
    ) -> bool:

        try:

            send_event(
                PROCESSED_TELEMETRY_TOPIC,
                event.model_dump()
            )

            logger.info(
                f"Published processed event "
                f"{event.event_id}"
            )

            return True

        except Exception as e:

            logger.exception(
                f"Failed publishing "
                f"processed event: {e}"
            )

            return False