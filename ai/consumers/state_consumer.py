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

from ai.state.state_engine import (
    StateEngine
)

from ai.publishers.state_publisher import (
    StatePublisher
)

logger = logging.getLogger(
    "sentinel.ai.state.consumer"
)

logging.basicConfig(
    level=logging.INFO
)


class StateConsumer:

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
                "sentinel-state-manager"
            )
        )

        self.engine = (
            StateEngine()
        )

        self.publisher = (
            StatePublisher()
        )

    def start(self):

        logger.info(
            "State consumer started"
        )

        for message in self.consumer:

            try:

                verification = (
                    VerificationResult(
                        **message.value
                    )
                )

                state = (

                    self.engine
                    .process(

                        incident_id=(
                            verification
                            .execution_id
                        ),

                        service=(
                            verification
                            .service
                        ),

                        topic=(
                            VERIFICATION_RESULTS_TOPIC
                        )
                    )
                )

                self.publisher.publish(
                    state
                )

            except Exception:

                logger.exception(
                    "State processing failed"
                )


if __name__ == "__main__":

    StateConsumer().start()