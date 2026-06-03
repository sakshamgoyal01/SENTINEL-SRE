import json
import logging

from kafka import KafkaConsumer

from ingestion.config.ingestion_settings import (
    settings
)

from ingestion.messaging.topics import (
    RECOVERY_RESULTS_TOPIC
)

from ai.models.recovery_result import (
    RecoveryResult
)

from ai.escalation.escalation_engine import (
    EscalationEngine
)

from ai.publishers.escalation_publisher import (
    EscalationPublisher
)

logger = logging.getLogger(
    "sentinel.ai.escalation.consumer"
)

logging.basicConfig(
    level=logging.INFO
)


class EscalationConsumer:

    def __init__(self):

        self.consumer = KafkaConsumer(

            RECOVERY_RESULTS_TOPIC,

            bootstrap_servers=(
                settings
                .KAFKA_BOOTSTRAP_SERVERS
            ),

            value_deserializer=lambda m:
            json.loads(
                m.decode("utf-8")
            ),

            auto_offset_reset="earliest",

            group_id=(
                "sentinel-escalation-agent"
            )
        )

        self.engine = (
            EscalationEngine()
        )

        self.publisher = (
            EscalationPublisher()
        )

    def start(self):

        logger.info(
            "Escalation consumer started"
        )

        for message in self.consumer:

            try:

                recovery = (
                    RecoveryResult(
                        **message.value
                    )
                )

                escalation = (

                    self.engine
                    .process(
                        recovery
                    )
                )

                if escalation is None:

                    logger.info(

                        "No escalation required"
                    )

                    continue

                self.publisher.publish(
                    escalation
                )

            except Exception:

                logger.exception(
                    "Escalation processing failed"
                )


if __name__ == "__main__":

    EscalationConsumer().start()