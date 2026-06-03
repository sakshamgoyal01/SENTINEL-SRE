import json
import logging

from kafka import KafkaConsumer

from ingestion.config.ingestion_settings import (
    settings
)

from ingestion.messaging.topics import (
    APPROVED_ACTIONS_TOPIC
)

from ai.models.approval_decision import (
    ApprovalDecision
)

from ai.execution.execution_engine import (
    ExecutionEngine
)

from ai.publishers.execution_publisher import (
    ExecutionPublisher
)

logger = logging.getLogger(
    "sentinel.ai.execution.consumer"
)

logging.basicConfig(
    level=logging.INFO
)


class ApprovalConsumer:

    def __init__(self):

        self.consumer = KafkaConsumer(

            APPROVED_ACTIONS_TOPIC,

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
                "sentinel-execution-agent"
            )
        )

        self.engine = (
            ExecutionEngine()
        )

        self.publisher = (
            ExecutionPublisher()
        )

    def start(self):

        logger.info(
            "Execution consumer started"
        )

        for message in self.consumer:

            try:

                decision = (
                    ApprovalDecision(
                        **message.value
                    )
                )

                if not decision.approved:

                    logger.info(

                        "Approval denied. "
                        "Skipping execution."
                    )

                    continue

                result = (

                    self.engine
                    .process(
                        decision
                    )
                )

                self.publisher.publish(
                    result
                )

            except Exception:

                logger.exception(
                    "Execution failed"
                )


if __name__ == "__main__":

    ApprovalConsumer().start()