from ingestion.messaging.producer import (
    send_event
)

from ingestion.messaging.topics import (
    METRICS_TOPIC
)


send_event(

    METRICS_TOPIC,

    {
        "message": "Kafka test successful"
    }
)

print("Event sent.")