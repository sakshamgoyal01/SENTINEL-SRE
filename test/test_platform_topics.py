import asyncio
import uuid

from backend.database.session import (
    SessionLocal
)

from backend.core.container import (
    Container
)

from backend.persistence.event_persistence_manager import (
    EventPersistenceManager
)


TEST_EVENTS = {

    "sentinel.processed.telemetry": {

        "event_id": str(
            uuid.uuid4()
        ),

        "event_type": "metric",

        "category":
            "performance",

        "severity":
            "CRITICAL",

        "priority":
            "P1",

        "risk_score":
            95.0,

        "service":
            "payment-service",

        "summary":
            "High CPU usage",

        "raw_event": {
            "metric_name":
                "cpu_usage"
        },
    },

    "sentinel.aggregated.events": {

        "aggregation_key":
            "payment-service",

        "category":
            "availability",

        "severity":
            "CRITICAL",

        "count":
            100,

        "services": [
            "payment-service"
        ],

        "summary":
            "Timeout burst",
    },

    "sentinel.alerts": {

        "alert_id": str(
            uuid.uuid4()
        ),

        "service":
            "payment-service",

        "severity":
            "CRITICAL",

        "title":
            "Payment Service Down",

        "description":
            "Service unavailable",

        "status":
            "OPEN",

        "source":
            "incident-detector",
    },

    "sentinel.dlq": {

        "dlq_id": str(
            uuid.uuid4()
        ),

        "source_topic":
            "sentinel.logs",

        "payload": {
            "service":
                "payment-service"
        },

        "error_message":
            "Parsing failed",
    },
}


async def main():

    async with SessionLocal() as session:

        container = Container(
            session
        )

        manager = (
            EventPersistenceManager
            .from_registry(
                container.get_handler_instances()
            )
        )

        print()
        print(
            "=" * 60
        )

        print(
            "TESTING PLATFORM TOPICS"
        )

        print(
            "=" * 60
        )

        passed = 0
        failed = 0

        for (
            topic,
            payload
        ) in TEST_EVENTS.items():

            try:

                await manager.persist_event(
                    topic=topic,
                    payload=payload,
                )

                await session.commit()

                passed += 1

                print(
                    f"[PASS] {topic}"
                )

            except Exception as exc:

                await session.rollback()

                failed += 1

                print(
                    f"[FAIL] {topic}"
                )

                print(
                    f"Reason: {exc}"
                )

        print()
        print(
            "=" * 60
        )

        print(
            f"PASSED : {passed}"
        )

        print(
            f"FAILED : {failed}"
        )

        print(
            "=" * 60
        )

        if failed == 0:

            print()
            print(
                "ALL PLATFORM TOPICS VALIDATED"
            )


if __name__ == "__main__":

    asyncio.run(
        main()
    )