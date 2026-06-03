import logging

from ingestion.messaging.producer import (
    send_event
)

from ingestion.messaging.topics import (
    VERIFICATION_RESULTS_TOPIC
)

logger = logging.getLogger(
    "sentinel.ai.verification.publisher"
)


class VerificationPublisher:

    def publish(
        self,
        verification_result
    ) -> bool:

        try:

            send_event(

                VERIFICATION_RESULTS_TOPIC,

                verification_result.model_dump(
                    mode="json"
                )
            )

            logger.info(

                "Published verification %s",

                verification_result
                .verification_id
            )

            return True

        except Exception:

            logger.exception(

                "Verification publish failed"
            )

            return False