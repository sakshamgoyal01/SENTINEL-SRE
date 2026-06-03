import json
import logging

from kafka import KafkaConsumer

from ingestion.config.ingestion_settings import (
    settings
)

from ingestion.messaging.topics import (
    VERIFICATION_RESULTS_TOPIC
)

from ai.models.verification_result import (
    VerificationResult
)

from ai.recovery.recovery_engine import (
    RecoveryEngine
)

from ai.publishers.recovery_publisher import (
    RecoveryPublisher
)

logger = logging.getLogger(
    "sentinel.ai.recovery.consumer"
)

logging.basicConfig(
    level=logging.INFO
)


class VerificationConsumer:

    def __init__(self):

        self.consumer = KafkaConsumer(

            VERIFICATION_RESULTS_TOPIC,

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
                "sentinel-recovery-agent"
            )
        )

        self.engine = (
            RecoveryEngine()
        )

        self.publisher = (
            RecoveryPublisher()
        )

    def start(self):

        logger.info(
            "Recovery consumer started"
        )

        for message in self.consumer:

            try:

                verification = (
                    VerificationResult(
                        **message.value
                    )
                )

                result = (

                    self.engine
                    .process(
                        verification
                    )
                )

                self.publisher.publish(
                    result
                )

            except Exception:

                logger.exception(
                    "Recovery processing failed"
                )


if __name__ == "__main__":

    VerificationConsumer().start()