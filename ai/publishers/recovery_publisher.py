import logging

from ingestion.messaging.producer import (
    send_event
)

from ingestion.messaging.topics import (
    RECOVERY_RESULTS_TOPIC
)

logger = logging.getLogger(
    "sentinel.ai.recovery.publisher"
)


class RecoveryPublisher:

    def publish(
        self,
        recovery_result
    ) -> bool:

        try:

            send_event(

                RECOVERY_RESULTS_TOPIC,

                recovery_result.model_dump(
                    mode="json"
                )
            )

            logger.info(

                "Published recovery %s",

                recovery_result
                .recovery_id
            )

            return True

        except Exception:

            logger.exception(

                "Recovery publish failed"
            )

            return False