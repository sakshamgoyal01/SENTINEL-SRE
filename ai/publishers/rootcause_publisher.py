import logging

from ingestion.messaging.producer import (
    send_event
)

from ingestion.messaging.topics import (
    ROOTCAUSE_TOPIC
)

logger = logging.getLogger(
    "sentinel.ai.rootcause.publisher"
)


class RootCausePublisher:

    def publish(
        self,
        rootcause_result
    ) -> bool:

        try:

            send_event(

                ROOTCAUSE_TOPIC,

                rootcause_result.model_dump(
                    mode="json"
                )
            )

            logger.info(

                "Published root cause %s",

                rootcause_result
                .rootcause_id
            )

            return True

        except Exception:

            logger.exception(

                "Failed to publish root cause"
            )

            return False