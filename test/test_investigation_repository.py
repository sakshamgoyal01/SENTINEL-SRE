import asyncio
import uuid

from datetime import datetime

from backend.database.session import (
    AsyncSessionLocal
)

from backend.models.investigation import (
    Investigation
)

from backend.repositories.investigation_repository import (
    InvestigationRepository
)

import pytest

@pytest.mark.asyncio
async def test_repository():


    async with (
        AsyncSessionLocal()
        as session
    ):

        repo = (
            InvestigationRepository(
                session
            )
        )

        investigation = (
            Investigation(

                investigation_id=str(
                    uuid.uuid4()
                ),

                service=(
                    "payment-service"
                ),

                severity=(
                    "CRITICAL"
                ),

                priority=(
                    "P1"
                ),

                summary=(
                    "Payment service outage"
                ),

                findings=[
                    {
                        "type":
                        "dependency_failure"
                    }
                ],

                evidence=[
                    {
                        "source":
                        "logs"
                    }
                ],

                timeline=[
                    {
                        "event":
                        "incident_started"
                    }
                ],

                confidence=0.95,

                generated_at=(
                    datetime.utcnow()
                )
            )
        )

        saved = (
            await repo.create(
                investigation
            )
        )

        loaded = (
            await repo.get_by_id(
                saved.id
            )
        )

        assert (
            loaded
            is not None
        )

        assert (
            loaded.service
            ==
            "payment-service"
        )

        assert (
            loaded.priority
            ==
            "P1"
        )

        print(
            "Investigation saved:",
            loaded.id
        )


if __name__ == "__main__":

    asyncio.run(
        test_repository()
    )