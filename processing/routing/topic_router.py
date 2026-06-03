from ingestion.messaging.topics import (
    INCIDENTS_TOPIC,
    ALERTS_TOPIC,
    REMEDIATION_TOPIC
)


class TopicRouter:

    TOPIC_MAP = {

        "incident":
            INCIDENTS_TOPIC,

        "alert":
            ALERTS_TOPIC,

        "remediation":
            REMEDIATION_TOPIC,

        "audit":
            "sentinel.audit"
    }

    def get_topic(
        self,
        destination: str
    ) -> str:

        return self.TOPIC_MAP[
            destination
        ]