import logging

from kafka import KafkaConsumer

from processing.models.prioritized_event import (
    PrioritizedEvent
)

from ingestion.config.ingestion_settings import (
    settings
)

from ingestion.messaging.topics import (
    INCIDENTS_TOPIC
)

from ai.investigation.investigation_engine import (
    InvestigationEngine
)

from ai.publishers.investigation_publisher import (
    InvestigationPublisher
)

logger = logging.getLogger(
    "sentinel.ai.incident_consumer"
)

logging.basicConfig(
    level=logging.INFO
)


class IncidentConsumer:

    def __init__(self):

        self.consumer = KafkaConsumer(

            INCIDENTS_TOPIC,

            bootstrap_servers=(
                settings
                .KAFKA_BOOTSTRAP_SERVERS
            ),

            value_deserializer=lambda m:
            __import__("json")
            .loads(
                m.decode("utf-8")
            ),

            auto_offset_reset="earliest",

            group_id=(
                "sentinel-investigation-agent"
            )
        )

        self.engine = (
            InvestigationEngine()
        )

        self.publisher = (
            InvestigationPublisher()
        )

    def start(self):

        logger.info(
            "Investigation consumer started"
        )

        for message in self.consumer:

            try:

                incident = (
                    PrioritizedEvent(
                        **message.value
                    )
                )

                result = (
                    self.engine.process(
                        incident
                    )
                )

                self.publisher.publish(
                    result
                )

            except Exception:

                logger.exception(
                    "Investigation failed"
                )


if __name__ == "__main__":

    IncidentConsumer().start()