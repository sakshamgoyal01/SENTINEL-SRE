import logging

from ingestion.messaging.producer import (
    send_event
)

from ingestion.messaging.topics import (
    EXECUTION_RESULTS_TOPIC
)

logger = logging.getLogger(
    "sentinel.ai.execution.publisher"
)


class ExecutionPublisher:

    def publish(
        self,
        execution_result
    ) -> bool:

        try:

            send_event(

                EXECUTION_RESULTS_TOPIC,

                execution_result.model_dump(
                    mode="json"
                )
            )

            logger.info(

                "Published execution %s",

                execution_result
                .execution_id
            )

            return True

        except Exception:

            logger.exception(

                "Execution publish failed"
            )

            return False