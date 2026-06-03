import logging

from ingestion.messaging.consumer import (
    get_consumer
)

from ingestion.models.log_event import (
    LogEvent
)

from processing.services.processing_pipeline import (
    ProcessingPipeline
)

logger = logging.getLogger(
    "sentinel.processing.logs_consumer"
)


class LogsConsumer:

    def __init__(self):

        self.pipeline = (
            ProcessingPipeline()
        )

    def start(self):

        consumer = get_consumer(
            "sentinel.logs",
            "sentinel-logs-consumer"
        )

        logger.info(
            "Logs consumer started."
        )

        for message in consumer:

            try:

                log_event = LogEvent(
                    **message.value
                )

                self.pipeline.process_log(
                    log_event
                )

            except Exception as e:

                logger.exception(
                    f"Failed processing "
                    f"log message: {e}"
                )


if __name__ == "__main__":

    LogsConsumer().start()