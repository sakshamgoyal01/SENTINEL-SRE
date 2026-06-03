import logging

from ingestion.messaging.producer import (
    send_event
)

from ingestion.messaging.topics import (
    INCIDENT_STATE_TOPIC
)

logger = logging.getLogger(
    "sentinel.ai.state.publisher"
)


class StatePublisher:

    def publish(
        self,
        state
    ) -> bool:

        try:

            send_event(

                INCIDENT_STATE_TOPIC,

                state.model_dump(
                    mode="json"
                )
            )

            logger.info(

                "Published state %s",

                state.current_state
            )

            return True

        except Exception:

            logger.exception(

                "State publish failed"
            )

            return False