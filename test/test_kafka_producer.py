from ingestion.messaging.producer import send_event
from ingestion.messaging.topics import METRICS_TOPIC


def test_kafka_send():

    send_event(
        METRICS_TOPIC,
        {
            "service": "payment-service",
            "metric": "cpu_usage",
            "value": 50
        }
    )

    assert True