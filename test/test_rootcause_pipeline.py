import json
from datetime import datetime
from uuid import uuid4

from kafka import KafkaProducer


TOPIC = (
    "sentinel.rootcause.results"
)


def main():

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

        "rootcause_id":
            str(uuid4()),

        "investigation_id":
            str(uuid4()),

        "service":
            "payment-service",

        "severity":
            "CRITICAL",

        "priority":
            "P1",

        "root_cause": {

            "cause_type":
                "DATABASE_FAILURE",

            "description":
                "Primary database unavailable",

            "confidence":
                0.95
        },

        "causal_chain": {

            "trigger":
                "DB Timeout",

            "sequence": [

                "Database Failure",

                "Connection Timeout",

                "API Errors"
            ]
        },

        "evidence": [

            "Database timeout detected",

            "Connection refused"
        ],

        "confidence":
            0.96,

        "generated_at":
            datetime.utcnow().isoformat()
    }

    producer.send(
        TOPIC,
        payload
    )

    producer.flush()

    print(
        "RootCause event published."
    )


if __name__ == "__main__":

    main()