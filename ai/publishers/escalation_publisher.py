import logging

from ingestion.messaging.producer import (
    send_event
)

from ingestion.messaging.topics import (
    ESCALATION_TOPIC
)

logger = logging.getLogger(
    "sentinel.ai.escalation.publisher"
)


class EscalationPublisher:

    def publish(
        self,
        escalation
    ):

        send_event(

            ESCALATION_TOPIC,

            escalation.model_dump(
                mode="json"
            )
        )

        return True