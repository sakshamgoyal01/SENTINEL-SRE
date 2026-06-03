from ingestion.messaging.healthcheck import (
    check_kafka_health
)


def test_kafka_health():

    result = check_kafka_health()

    assert result["status"] == "healthy"