import logging

from ingestion.messaging.producer import (
    send_event
)

from ingestion.messaging.topics import (
    INCIDENTS_TOPIC
)

logger = logging.getLogger(
    "sentinel.incident.publisher"
)


class IncidentPublisher:

    def publish(
        self,
        event
    ) -> bool:

        send_event(
            INCIDENTS_TOPIC,
            event.model_dump()
        )

        return True