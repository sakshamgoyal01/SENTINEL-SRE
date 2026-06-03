import logging

from ingestion.messaging.consumer import (
    get_consumer
)

from ingestion.models.trace_event import (
    TraceEvent
)

from processing.services.processing_pipeline import (
    ProcessingPipeline
)

logger = logging.getLogger(
    "sentinel.processing.traces_consumer"
)


class TracesConsumer:

    def __init__(self):

        self.pipeline = (
            ProcessingPipeline()
        )

    def start(self):

        consumer = get_consumer(
            "sentinel.traces",
            "sentinel-traces-consumer"
        )

        logger.info(
            "Traces consumer started."
        )

        for message in consumer:

            try:

                trace_event = TraceEvent(
                    **message.value
                )

                self.pipeline.process_trace(
                    trace_event
                )

            except Exception as e:

                logger.exception(
                    f"Failed processing "
                    f"trace message: {e}"
                )


if __name__ == "__main__":

    TracesConsumer().start()