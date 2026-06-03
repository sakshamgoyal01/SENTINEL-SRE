import logging

from ingestion.messaging.producer import (
    send_event
)

from ingestion.messaging.topics import (
    EXECUTIVE_SUMMARY_TOPIC
)

logger = logging.getLogger(
    "sentinel.ai.executive.publisher"
)


class ExecutiveSummaryPublisher:

    def publish(
        self,
        report
    ) -> bool:

        try:

            send_event(

                EXECUTIVE_SUMMARY_TOPIC,

                report.model_dump(
                    mode="json"
                )
            )

            logger.info(

                "Published executive report %s",

                report.report_id
            )

            return True

        except Exception:

            logger.exception(

                "Executive report publish failed"
            )

            return False