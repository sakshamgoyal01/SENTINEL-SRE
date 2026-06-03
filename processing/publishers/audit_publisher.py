from ingestion.messaging.producer import (
    send_event
)

from ingestion.messaging.topics import (
    AUDIT_TOPIC
)


class AuditPublisher:

    def publish(
        self,
        event
    ) -> bool:

        send_event(
            AUDIT_TOPIC,
            event.model_dump()
        )

        return True