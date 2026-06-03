import logging

from ingestion.messaging.producer import send_event

from ingestion.messaging.dead_letter_queue import (
    send_to_dlq
)

from ingestion.normalization.normalizer import (
    normalize_event
)

from ingestion.collectors.health.collector_health import (
    update_collector_health
)


logging.basicConfig(level=logging.INFO)

logger = logging.getLogger("sentinel.collector")


class BaseCollector:

    topic = None

    async def publish(self, event: dict):

        try:

            normalized_event = normalize_event(
                event
            )

            if not normalized_event:

                logger.warning(
                    "Duplicate or invalid event skipped."
                )

                return

            send_event(
                self.topic,
                normalized_event
            )

            update_collector_health(
                self.__class__.__name__,
                "healthy",
                events_processed=1
            )

            logger.info(
                f"Published event to {self.topic}"
            )

        except Exception as e:

            send_to_dlq(
                event,
                str(e)
            )

            update_collector_health(
                self.__class__.__name__,
                "failed",
                error=str(e)
            )

            logger.exception(
                f"Collector publish failed: {e}"
            )