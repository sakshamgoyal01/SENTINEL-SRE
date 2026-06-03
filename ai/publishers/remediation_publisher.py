import logging

from ingestion.messaging.producer import (
    send_event
)

from ingestion.messaging.topics import (
    REMEDIATION_TOPIC
)

logger = logging.getLogger(
    "sentinel.ai.remediation.publisher"
)


class RemediationPublisher:

    def publish(
        self,
        remediation_result
    ) -> bool:

        try:

            send_event(

                REMEDIATION_TOPIC,

                remediation_result.model_dump(
                    mode="json"
                )
            )

            logger.info(

                "Published remediation %s",

                remediation_result
                .remediation_id
            )

            return True

        except Exception:

            logger.exception(
                "Remediation publish failed"
            )

            return False