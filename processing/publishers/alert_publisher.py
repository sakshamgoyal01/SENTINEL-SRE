import logging

from ingestion.messaging.producer import (
    send_event
)

from ingestion.messaging.topics import (
    ALERTS_TOPIC
)


class AlertPublisher:

    def publish(
        self,
        event
    ) -> bool:

        send_event(
            ALERTS_TOPIC,
            event.model_dump()
        )

        return True