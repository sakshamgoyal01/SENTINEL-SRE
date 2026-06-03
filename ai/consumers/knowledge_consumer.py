import json
import logging

from kafka import KafkaConsumer

from ingestion.config.ingestion_settings import (
    settings
)

from ingestion.messaging.topics import (
    KNOWLEDGE_TOPIC
)

from ai.models.knowledge_record import (
    KnowledgeRecord
)

from ai.executive.executive_summary_engine import (
    ExecutiveSummaryEngine
)

from ai.publishers.executive_summary_publisher import (
    ExecutiveSummaryPublisher
)

logger = logging.getLogger(
    "sentinel.ai.executive.consumer"
)

logging.basicConfig(
    level=logging.INFO
)


class KnowledgeConsumer:

    def __init__(self):

        self.consumer = KafkaConsumer(

            KNOWLEDGE_TOPIC,

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
                "sentinel-executive-agent"
            )
        )

        self.engine = (
            ExecutiveSummaryEngine()
        )

        self.publisher = (
            ExecutiveSummaryPublisher()
        )

    def start(self):

        logger.info(
            "Executive Summary consumer started"
        )

        for message in self.consumer:

            try:

                knowledge_record = (
                    KnowledgeRecord(
                        **message.value
                    )
                )

                report = (

                    self.engine
                    .process(
                        knowledge_record
                    )
                )

                self.publisher.publish(
                    report
                )

            except Exception:

                logger.exception(

                    "Executive summary generation failed"
                )


if __name__ == "__main__":

    KnowledgeConsumer().start()