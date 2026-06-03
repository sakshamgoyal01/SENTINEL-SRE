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

from ai.approval.approval_engine import (
    ApprovalEngine
)

from ai.publishers.approval_publisher import (
    ApprovalPublisher
)

logger = logging.getLogger(
    "sentinel.ai.approval.consumer"
)

logging.basicConfig(
    level=logging.INFO
)


class RemediationApprovalConsumer:

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
                "sentinel-approval-agent"
            )
        )

        self.engine = (
            ApprovalEngine()
        )

        self.publisher = (
            ApprovalPublisher()
        )

    def start(self):

        logger.info(
            "Approval consumer started"
        )

        for message in self.consumer:

            try:

                remediation = (
                    RemediationResult(
                        **message.value
                    )
                )

                decision = (

                    self.engine
                    .process(
                        remediation
                    )
                )

                self.publisher.publish(
                    decision
                )

            except Exception:

                logger.exception(
                    "Approval generation failed"
                )


if __name__ == "__main__":

    RemediationApprovalConsumer().start()