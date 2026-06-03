from ingestion.messaging.producer import (
    send_event
)

event = {

    "service": "payment-service",

    "severity": "ERROR",

    "message": "Synthetic failure event",

    "details": {
        "bad_object": object()
    }
}

send_event(
    "sentinel.dlq",
    event
)

print(
    "DLQ test completed."
)