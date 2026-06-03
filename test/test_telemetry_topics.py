import asyncio
import uuid
from datetime import datetime
from datetime import UTC

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

    "sentinel.metrics": {

        "event_id": str(
            uuid.uuid4()
        ),

        "timestamp": datetime.now(
            UTC
        ),

        "source": "prometheus",

        "service":
            "payment-service",

        "metric_name":
            "cpu_usage",

        "value": 95.0,

        "labels": {
            "pod": "payment-1"
        },

        "unit": "percent",

        "cluster": "local",

        "environment": "dev",

        "namespace": "default",
    },

    "sentinel.logs": {

        "event_id": str(
            uuid.uuid4()
        ),

        "timestamp": datetime.now(
            UTC
        ),

        "source": "loki",

        "service":
            "payment-service",

        "severity":
            "CRITICAL",

        "message":
            "Database timeout",

        "trace_id":
            str(uuid.uuid4()),

        "span_id":
            str(uuid.uuid4()),

        "logger":
            "payment.logger",
    },

    "sentinel.traces": {

        "event_id": str(
            uuid.uuid4()
        ),

        "timestamp": datetime.now(
            UTC
        ),

        "source": "otel",

        "trace_id":
            str(uuid.uuid4()),

        "span_id":
            str(uuid.uuid4()),

        "parent_span_id":
            None,

        "service":
            "payment-service",

        "operation":
            "process_payment",

        "duration_ms":
            250.5,

        "status_code":
            500,
    },

    "sentinel.k8s.events": {

        "event_id": str(
            uuid.uuid4()
        ),

        "timestamp": datetime.now(
            UTC
        ),

        "source": "kubernetes",

        "reason":
            "FailedScheduling",

        "message":
            "Insufficient CPU",

        "event_type":
            "Warning",

        "involved_object": {

            "kind":
                "Pod",

            "name":
                "payment-pod"
        }
    },

    "sentinel.deployments": {

        "event_id": str(
            uuid.uuid4()
        ),

        "timestamp": datetime.now(
            UTC
        ),

        "source": "kubernetes",

        "deployment_name":
            "payment-service",

        "namespace":
            "default",

        "image":
            "payment:v1",

        "replicas":
            3,

        "available_replicas":
            3,

        "updated_replicas":
            3,

        "strategy":
            "RollingUpdate",
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
            "TESTING TELEMETRY TOPICS"
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
                "ALL TELEMETRY TOPICS VALIDATED"
            )

        else:

            print()
            print(
                "SOME TELEMETRY TOPICS FAILED"
            )


if __name__ == "__main__":

    asyncio.run(
        main()
    )