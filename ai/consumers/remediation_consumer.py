import json
import logging

from kafka import KafkaConsumer

from ingestion.config.ingestion_settings import (
    settings
)

from ingestion.messaging.topics import (
    REMEDIATION_TOPIC
)

from ai.models.remediation_result import (
    RemediationResult
)

from ai.knowledge.knowledge_engine import (
    KnowledgeEngine
)

from ai.publishers.knowledge_publisher import (
    KnowledgePublisher
)

logger = logging.getLogger(
    "sentinel.ai.knowledge.consumer"
)

logging.basicConfig(
    level=logging.INFO
)


class RemediationConsumer:

    def __init__(self):

        self.consumer = KafkaConsumer(

            REMEDIATION_TOPIC,

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
                "sentinel-knowledge-agent"
            )
        )

        self.engine = (
            KnowledgeEngine()
        )

        self.publisher = (
            KnowledgePublisher()
        )

    def start(self):

        logger.info(
            "Knowledge consumer started"
        )

        for message in self.consumer:

            try:

                remediation = (
                    RemediationResult(
                        **message.value
                    )
                )

                result = (
                    self.engine.process(
                        remediation
                    )
                )

                self.publisher.publish(
                    result
                )

            except Exception:

                logger.exception(
                    "Knowledge generation failed"
                )


if __name__ == "__main__":

    RemediationConsumer().start()