import logging

from ingestion.messaging.consumer import (
    get_consumer
)

from ingestion.models.metric_event import (
    MetricEvent
)

from processing.services.processing_pipeline import ProcessingPipeline

logger = logging.getLogger(
    "sentinel.processing.metrics_consumer"
)


class MetricsConsumer:

    def __init__(self):

        self.pipeline = (
            ProcessingPipeline()
        )

    def start(self):

        consumer = get_consumer(
            "sentinel.metrics",
            "sentinel-metrics-consumer"
        )

        logger.info(
            "Metrics consumer started."
        )

        for message in consumer:

            try:

                print(
                    "\nRAW MESSAGE:",
                    message.value
                )

                metric_event = MetricEvent(
                    **message.value
                )

                print(
                    "SERVICE:",
                    metric_event.service
                )

                print(
                    "METRIC:",
                    metric_event.metric_name
                )

                self.pipeline.process_metric(
                    metric_event
                )

            except Exception as e:

                logger.exception(
                    f"Failed processing metric message: {e}"
                )

if __name__ == "__main__":

    consumer = MetricsConsumer()

    consumer.start()