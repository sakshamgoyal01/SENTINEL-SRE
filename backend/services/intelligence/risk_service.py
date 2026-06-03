from backend.services.base_service import (
    BaseService
)

from backend.models.intelligence.risk import (
    Risk
)


class RiskService(
    BaseService
):

    async def create_from_event(
        self,
        payload: dict,
    ) -> Risk:
        risk = Risk(
            risk_id=payload["risk_id"],
            rootcause_id=payload["rootcause_id"],
            service=payload["service"],
            priority=payload["priority"],
            blast_radius=payload["blast_radius"],
            impact_assessment=payload["impact_assessment"],
            risk_summary=payload["risk_summary"],
        )

        return await (
            self.repository.create(
                risk
            )
        )