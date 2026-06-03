import logging

from ingestion.messaging.producer import (
    send_event
)

from ingestion.messaging.topics import (
    KNOWLEDGE_TOPIC
)

logger = logging.getLogger(
    "sentinel.ai.knowledge.publisher"
)


class KnowledgePublisher:

    def publish(
        self,
        knowledge_record
    ) -> bool:

        try:

            send_event(

                KNOWLEDGE_TOPIC,

                knowledge_record.model_dump(
                    mode="json"
                )
            )

            logger.info(

                "Published knowledge record %s",

                knowledge_record
                .knowledge_id
            )

            return True

        except Exception:

            logger.exception(

                "Knowledge publish failed"
            )

            return False