import asyncio
from datetime import datetime

from backend.database.session import SessionLocal

from backend.models.intelligence.risk import Risk

from backend.repositories.intelligence.risk_repository import (
    RiskRepository
)

from backend.services.intelligence.risk_service import (
    RiskService
)

from backend.persistence.handlers.risk_handler import (
    RiskPersistenceHandler
)

from backend.persistence.event_persistence_manager import (
    EventPersistenceManager
)


class FakeManager:

    def __init__(
        self,
        handler,
    ):
        self.handler = handler

    async def persist_event(
        self,
        topic: str,
        payload: dict,
    ):
        await self.handler.persist(
            payload
        )


async def main():

    payload = {
        "risk_id": "risk-test-1",
        "rootcause_id": "root-test-1",
        "service": "payment-service",
        "priority": "P1",
        "blast_radius": {
            "services": [
                "checkout-service"
            ]
        },
        "impact_assessment": {
            "customer_impact": "HIGH"
        },
        "risk_summary": {
            "risk_level": "CRITICAL"
        },
        "generated_at": datetime.utcnow(),
    }

    async with SessionLocal() as session:

        repository = RiskRepository(
            session
        )

        service = RiskService(
            repository
        )

        handler = (
            RiskPersistenceHandler(
                service
            )
        )

        manager = FakeManager(
            handler
        )

        print(
            "Testing Persistence Manager..."
        )

        await manager.persist_event(
            topic="sentinel.risk.results",
            payload=payload,
        )

        await session.commit()

        saved = await repository.list()

        print(
            f"Rows found: {len(saved)}"
        )

        for row in saved:
            print(
                row.risk_id
            )


if __name__ == "__main__":
    asyncio.run(main())