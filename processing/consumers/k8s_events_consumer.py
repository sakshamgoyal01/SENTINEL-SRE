import logging

from ingestion.messaging.consumer import (
    get_consumer
)

from ingestion.models.kubernetes_event import (
    KubernetesEvent
)

from processing.services.processing_pipeline import (
    ProcessingPipeline
)

logger = logging.getLogger(
    "sentinel.processing.k8s_consumer"
)


class KubernetesEventsConsumer:

    def __init__(self):

        self.pipeline = (
            ProcessingPipeline()
        )

    def start(self):

        consumer = get_consumer()

        logger.info(
            "Kubernetes consumer started."
        )

        for message in consumer:

            try:

                event = KubernetesEvent(
                    **message.value
                )

                self.pipeline.process_k8s(
                    event
                )

            except Exception as e:

                logger.exception(
                    f"Failed processing "
                    f"k8s event: {e}"
                )


if __name__ == "__main__":

    KubernetesEventsConsumer().start()