from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "sentinel.dlq",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    enable_auto_commit=False,
    group_id=None,
    consumer_timeout_ms=5000,
    value_deserializer=lambda m:
        json.loads(m.decode("utf-8"))
)

print("Reading DLQ messages...\n")

found = False

for message in consumer:

    found = True

    print(
        json.dumps(
            message.value,
            indent=2
        )
    )

if not found:

    print(
        "No DLQ messages found."
    )