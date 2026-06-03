import logging

from ingestion.messaging.consumer import (
    get_consumer
)

from ingestion.models.deployment_event import (
    DeploymentEvent
)

from processing.services.processing_pipeline import (
    ProcessingPipeline
)

logger = logging.getLogger(
    "sentinel.processing.deployments_consumer"
)


class DeploymentsConsumer:

    def __init__(self):

        self.pipeline = (
            ProcessingPipeline()
        )

    def start(self):

        consumer = get_consumer()

        logger.info(
            "Deployments consumer started."
        )

        for message in consumer:

            try:

                deployment_event = (
                    DeploymentEvent(
                        **message.value
                    )
                )

                self.pipeline.process_deployment(
                    deployment_event
                )

            except Exception as e:

                logger.exception(
                    f"Failed processing "
                    f"deployment event: {e}"
                )


if __name__ == "__main__":

    DeploymentsConsumer().start()