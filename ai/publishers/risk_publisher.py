import logging

from ingestion.messaging.producer import (
    send_event
)

from ingestion.messaging.topics import (
    RISK_TOPIC
)

logger = logging.getLogger(
    "sentinel.ai.risk.publisher"
)


class RiskPublisher:

    def publish(
        self,
        risk_result
    ) -> bool:

        try:

            send_event(

                RISK_TOPIC,

                risk_result.model_dump(
                    mode="json"
                )
            )

            logger.info(

                "Published risk result %s",

                risk_result.risk_id
            )

            return True

        except Exception:

            logger.exception(
                "Risk publish failed"
            )

            return False