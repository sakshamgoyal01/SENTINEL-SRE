import asyncio
import uuid
from datetime import datetime, UTC

from backend.database.session import (
    SessionLocal
)

from backend.repositories.telemetry.metric_repository import (
    MetricRepository
)

from backend.repositories.intelligence.risk_repository import (
    RiskRepository
)

from backend.repositories.Operations.approval_repository import (
    ApprovalRepository
)

from backend.repositories.intelligence.alert_repository import (
    AlertRepository
)

from backend.models.telemetry.metric import (
    Metric
)

from backend.models.intelligence.risk import (
    Risk
)

from backend.models.operations.approval import (
    Approval
)

from backend.models.intelligence.alert import (
    Alert
)

from backend.repositories.pagination import (
    PaginationParams
)


async def test_metric(session):

    print("\n[Metric Repository]")

    repo = MetricRepository(session)

    entity = Metric(
        event_id=str(uuid.uuid4()),
        timestamp=datetime.now(UTC),
        source="test",
        service="payment-service",
        metric_name="cpu_usage",
        value=90.0,
        labels={},
    )

    created = await repo.create(entity)

    await session.commit()

    assert created.id is not None

    found = await repo.get_by_id(
        created.id
    )

    assert found is not None

    assert await repo.exists(
        created.id
    )

    total = await repo.count()

    print(f"Count: {total}")

    rows = await repo.list(
        PaginationParams()
    )

    print(f"Rows: {len(rows)}")

    await repo.delete(
        created.id
    )

    await session.commit()

    print("PASS")


async def test_risk(session):

    print("\n[Risk Repository]")

    repo = RiskRepository(session)

    entity = Risk(
        risk_id=str(uuid.uuid4()),
        rootcause_id="rootcause-test",
        service="payment-service",
        priority="P1",
        blast_radius={},
        impact_assessment={},
        risk_summary={},
    )

    created = await repo.create(entity)

    await session.commit()

    assert created.id is not None

    found = await repo.get_by_id(
        created.id
    )

    assert found is not None

    assert await repo.exists(
        created.id
    )

    total = await repo.count()

    print(f"Count: {total}")

    rows = await repo.list(
        PaginationParams()
    )

    print(f"Rows: {len(rows)}")

    await repo.delete(
        created.id
    )

    await session.commit()

    print("PASS")


async def test_approval(session):

    print("\n[Approval Repository]")

    repo = ApprovalRepository(session)

    entity = Approval(
        approval_id=str(
            uuid.uuid4()
        ),

        service="payment-service",

        approved=True,

        requires_human_approval=False,

        reason=(
            "Auto remediation "
            "approved"
        ),

        actions=[
            {
                "type":
                    "restart_pod",

                "target":
                    "payment-service"
            }
        ],

        generated_at=datetime.now(
            UTC
        ),
    )

    created = await repo.create(entity)

    await session.commit()

    assert created.id is not None

    found = await repo.get_by_id(
        created.id
    )

    assert found is not None

    assert await repo.exists(
        created.id
    )

    total = await repo.count()

    print(f"Count: {total}")

    rows = await repo.list(
        PaginationParams()
    )

    print(f"Rows: {len(rows)}")

    await repo.delete(
        created.id
    )

    await session.commit()

    print("PASS")


async def test_alert(session):

    print("\n[Alert Repository]")

    repo = AlertRepository(session)

    entity = Alert(
        alert_id=str(uuid.uuid4()),
        service="payment-service",
        severity="CRITICAL",
        title="CPU Alert",
        description="High CPU",
        status="OPEN",
        source="detector",
    )

    created = await repo.create(entity)

    await session.commit()

    assert created.id is not None

    found = await repo.get_by_id(
        created.id
    )

    assert found is not None

    assert await repo.exists(
        created.id
    )

    total = await repo.count()

    print(f"Count: {total}")

    rows = await repo.list(
        PaginationParams()
    )

    print(f"Rows: {len(rows)}")

    await repo.delete(
        created.id
    )

    await session.commit()

    print("PASS")


async def main():

    async with SessionLocal() as session:

        print(
            "\n=============================="
        )
        print(
            "TESTING REPOSITORY CRUD"
        )
        print(
            "=============================="
        )

        await test_metric(session)

        await test_risk(session)

        await test_approval(session)

        await test_alert(session)

        print(
            "\n=============================="
        )
        print(
            "ALL CRUD TESTS PASSED"
        )
        print(
            "=============================="
        )


if __name__ == "__main__":

    asyncio.run(main())