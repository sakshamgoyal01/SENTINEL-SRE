import json
from datetime import datetime

from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers=["localhost:9092"],
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

payload = {
    "service": "payment-service",
    "metric_name": "cpu_usage",
    "metric_type": "gauge",
    "value": 75.5,
    "unit": "percent",
    "timestamp": datetime.utcnow().isoformat(),
    "labels": {
        "environment": "dev",
        "instance": "payment-service-1"
    }
}

producer.send(
    "sentinel.metrics",
    payload
)

producer.flush()

print("Valid metric published")