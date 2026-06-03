import logging

from ingestion.messaging.producer import (
    send_event
)

from ingestion.messaging.topics import (
    APPROVED_ACTIONS_TOPIC
)

logger = logging.getLogger(
    "sentinel.ai.approval.publisher"
)


class ApprovalPublisher:

    def publish(
        self,
        decision
    ) -> bool:

        try:

            send_event(

                APPROVED_ACTIONS_TOPIC,

                decision.model_dump(
                    mode="json"
                )
            )

            logger.info(

                "Published approval %s",

                decision.approval_id
            )

            return True

        except Exception:

            logger.exception(

                "Approval publish failed"
            )

            return False