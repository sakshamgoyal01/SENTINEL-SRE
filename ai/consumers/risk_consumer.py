import json
import logging

from kafka import KafkaConsumer

from ingestion.config.ingestion_settings import (
    settings
)

from ingestion.messaging.topics import (
    RISK_TOPIC
)

from ai.models.risk_result import (
    RiskResult
)

from ai.remediation.remediation_engine import (
    RemediationEngine
)

from ai.publishers.remediation_publisher import (
    RemediationPublisher
)

logger = logging.getLogger(
    "sentinel.ai.remediation.consumer"
)

logging.basicConfig(
    level=logging.INFO
)


class RiskConsumer:

    def __init__(self):

        self.consumer = KafkaConsumer(

            RISK_TOPIC,

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
                "sentinel-remediation-agent"
            )
        )

        self.engine = (
            RemediationEngine()
        )

        self.publisher = (
            RemediationPublisher()
        )

    def start(self):

        logger.info(
            "Remediation consumer started"
        )

        for message in self.consumer:

            try:

                risk_result = (
                    RiskResult(
                        **message.value
                    )
                )

                result = (
                    self.engine.process(
                        risk_result
                    )
                )

                self.publisher.publish(
                    result
                )

            except Exception:

                logger.exception(
                    "Remediation generation failed"
                )


if __name__ == "__main__":

    RiskConsumer().start()