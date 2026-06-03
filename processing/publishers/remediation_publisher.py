from ingestion.messaging.producer import (
    send_event
)

from ingestion.messaging.topics import (
    REMEDIATION_TOPIC
)


class RemediationPublisher:

    def publish(
        self,
        event
    ) -> bool:

        send_event(
            REMEDIATION_TOPIC,
            event.model_dump()
        )

        return True