import json
import logging

from kafka import KafkaConsumer

from ingestion.config.ingestion_settings import (
    settings
)

from ingestion.messaging.topics import (
    ROOTCAUSE_TOPIC
)

from ai.models.rootcause_result import (
    RootCauseResult
)

from ai.risk.risk_engine import (
    RiskEngine
)

from ai.publishers.risk_publisher import (
    RiskPublisher
)

logger = logging.getLogger(
    "sentinel.ai.risk.consumer"
)

logging.basicConfig(
    level=logging.INFO
)


class RootCauseConsumer:

    def __init__(self):

        self.consumer = KafkaConsumer(

            ROOTCAUSE_TOPIC,

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
                "sentinel-risk-agent"
            )
        )

        self.engine = (
            RiskEngine()
        )

        self.publisher = (
            RiskPublisher()
        )

    def start(self):

        logger.info(
            "Risk consumer started"
        )

        for message in self.consumer:

            try:

                rootcause = (
                    RootCauseResult(
                        **message.value
                    )
                )

                result = (
                    self.engine.process(
                        rootcause
                    )
                )

                self.publisher.publish(
                    result
                )

            except Exception:

                logger.exception(
                    "Risk analysis failed"
                )


if __name__ == "__main__":

    RootCauseConsumer().start()