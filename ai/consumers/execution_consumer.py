import json
import logging

from kafka import KafkaConsumer

from ingestion.config.ingestion_settings import (
    settings
)

from ingestion.messaging.topics import (
    EXECUTION_RESULTS_TOPIC
)

from ai.models.execution_result import (
    ExecutionResult
)

from ai.verification.verification_engine import (
    VerificationEngine
)

from ai.publishers.verification_publisher import (
    VerificationPublisher
)

logger = logging.getLogger(
    "sentinel.ai.verification.consumer"
)

logging.basicConfig(
    level=logging.INFO
)


class ExecutionConsumer:

    def __init__(self):

        self.consumer = KafkaConsumer(

            EXECUTION_RESULTS_TOPIC,

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
                "sentinel-verification-agent"
            )
        )

        self.engine = (
            VerificationEngine()
        )

        self.publisher = (
            VerificationPublisher()
        )

    def start(self):

        logger.info(
            "Verification consumer started"
        )

        for message in self.consumer:

            try:

                execution = (
                    ExecutionResult(
                        **message.value
                    )
                )

                result = (

                    self.engine
                    .process(
                        execution
                    )
                )

                self.publisher.publish(
                    result
                )

            except Exception:

                logger.exception(
                    "Verification failed"
                )


if __name__ == "__main__":

    ExecutionConsumer().start()