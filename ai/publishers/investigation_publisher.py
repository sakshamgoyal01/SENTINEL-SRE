import logging

from ingestion.messaging.producer import (
    send_event
)

from ingestion.messaging.topics import (
    INVESTIGATION_TOPIC
)

logger = logging.getLogger(
    "sentinel.ai.publisher"
)


class InvestigationPublisher:

    def publish(
        self,
        investigation_result
    ) -> bool:

        try:

            send_event(

                INVESTIGATION_TOPIC,

                investigation_result.model_dump(
                    mode="json"
                )
            )

            logger.info(

                "Published investigation %s",

                investigation_result.investigation_id
            )

            return True

        except Exception:

            logger.exception(
                "Failed to publish investigation"
            )

            return False