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

from ai.audit.audit_engine import (
    AuditEngine
)

from ai.publishers.audit_publisher import (
    AuditPublisher
)

logger = logging.getLogger(
    "sentinel.ai.audit.consumer"
)

logging.basicConfig(
    level=logging.INFO
)


class RecoveryConsumer:

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

            group_id=
            "sentinel-audit-agent"
        )

        self.engine = (
            AuditEngine()
        )

        self.publisher = (
            AuditPublisher()
        )

    def start(self):

        for message in self.consumer:

            recovery = (
                RecoveryResult(
                    **message.value
                )
            )

            audit = (

                self.engine
                .process(
                    recovery
                )
            )

            self.publisher.publish(
                audit
            )


if __name__ == "__main__":

    RecoveryConsumer().start()