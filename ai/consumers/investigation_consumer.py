import json
import logging

from kafka import KafkaConsumer

from ingestion.config.ingestion_settings import (
    settings
)

from ingestion.messaging.topics import (
    INVESTIGATION_TOPIC
)

from ai.models.investigation_result import (
    InvestigationResult
)

from ai.rootcause.rootcause_engine import (
    RootCauseEngine
)

from ai.publishers.rootcause_publisher import (
    RootCausePublisher
)

logger = logging.getLogger(
    "sentinel.ai.rootcause.consumer"
)

logging.basicConfig(
    level=logging.INFO
)


class InvestigationConsumer:

    def __init__(self):

        self.consumer = KafkaConsumer(

            INVESTIGATION_TOPIC,

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
                "sentinel-rootcause-agent"
            )
        )

        self.engine = (
            RootCauseEngine()
        )

        self.publisher = (
            RootCausePublisher()
        )

    def start(self):

        logger.info(
            "Root Cause consumer started"
        )

        for message in self.consumer:

            try:

                investigation = (
                    InvestigationResult(
                        **message.value
                    )
                )

                result = (
                    self.engine.process(
                        investigation
                    )
                )

                self.publisher.publish(
                    result
                )

            except Exception:

                logger.exception(
                    "Root cause analysis failed"
                )


if __name__ == "__main__":

    InvestigationConsumer().start()