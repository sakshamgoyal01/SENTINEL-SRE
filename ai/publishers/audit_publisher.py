import logging

from ingestion.messaging.producer import (
    send_event
)

from ingestion.messaging.topics import (
    EXECUTION_AUDIT_TOPIC
)

logger = logging.getLogger(
    "sentinel.ai.audit.publisher"
)


class AuditPublisher:

    def publish(
        self,
        audit_record
    ) -> bool:

        try:

            send_event(

                EXECUTION_AUDIT_TOPIC,

                audit_record.model_dump(
                    mode="json"
                )
            )

            return True

        except Exception:

            logger.exception(
                "Audit publish failed"
            )

            return False