import logging

from ingestion.messaging.producer import (
    send_event
)

from ingestion.messaging.topics import (
    AGGREGATED_EVENTS_TOPIC
)

logger = logging.getLogger(
    "sentinel.aggregation.publisher"
)


class AggregatedEventPublisher:

    def publish(
        self,
        event
    ) -> bool:

        try:

            send_event(

                AGGREGATED_EVENTS_TOPIC,

                event.model_dump()
            )

            logger.info(

                f"Published "
                f"aggregated event "
                f"{event.aggregation_key}"
            )

            return True

        except Exception as e:

            logger.exception(

                f"Aggregation publish "
                f"failed: {e}"
            )

            return False