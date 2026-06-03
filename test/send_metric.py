from datetime import datetime

from ingestion.messaging.producer import send_event
from ingestion.messaging.topics import METRICS_TOPIC


metric = {
    "timestamp": datetime.utcnow().isoformat(),
    "source": "prometheus",
    "service": "payment-service",
    "metric_name": "cpu_usage",
    "value": 95,
    "metadata": {
        "cluster": "local",
        "namespace": "default",
        "environment": "dev",
        "team": "backend",
        "region": "local"
    }
}

send_event(
    METRICS_TOPIC,
    metric
)

print("Metric sent successfully")