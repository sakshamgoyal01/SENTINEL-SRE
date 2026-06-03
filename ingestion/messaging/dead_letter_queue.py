from ingestion.messaging.producer import send_event

from ingestion.messaging.topics import DLQ_TOPIC


def send_to_dlq(event, reason):

    dlq_event = {

        "failed_event": event,

        "failure_reason": reason
    }

    send_event(DLQ_TOPIC, dlq_event)