import asyncio
import json
import uuid

from datetime import datetime

from kafka import KafkaProducer

TOPIC = (
    "sentinel.investigation.results"
)


def test_publish_investigation():

    producer = KafkaProducer(

        bootstrap_servers=[
            "localhost:9092"
        ],

        value_serializer=lambda v:
        json.dumps(v).encode(
            "utf-8"
        )
    )

    payload = {

        "investigation_id":
            str(uuid.uuid4()),

        "service":
            "payment-service",

        "severity":
            "CRITICAL",

        "priority":
            "P1",

        "summary":
            "Dependency timeout detected",

        "findings": [

            "Dependency Failure",

            "Database Timeout"
        ],

        "evidence": [

            {
                "evidence_type":
                    "LOG",

                "source":
                    "application",

                "description":
                    "Connection timeout observed",

                "confidence":
                    0.95
            }
        ],

        "timeline": [

            {
                "timestamp":
                    datetime.utcnow().isoformat(),

                "event_type":
                    "INCIDENT_START",

                "description":
                    "Incident started"
            }
        ],

        "confidence":
            0.95,

        "generated_at":
            datetime.utcnow().isoformat()
    }
    producer.send(
        TOPIC,
        payload
    )

    producer.flush()

    print(
        "Investigation event published."
    )


if __name__ == "__main__":

    test_publish_investigation()