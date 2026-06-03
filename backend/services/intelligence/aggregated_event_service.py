from backend.services.base_service import (
    BaseService
)

from backend.models.intelligence.aggregated_event import (
    AggregatedEvent
)


class AggregatedEventService(
    BaseService
):

    async def create_from_event(
        self,
        payload: dict,
    ) -> AggregatedEvent:

        entity = AggregatedEvent(
            aggregation_key=payload[
                "aggregation_key"
            ],
            category=payload[
                "category"
            ],
            severity=payload[
                "severity"
            ],
            count=payload[
                "count"
            ],
            services=payload[
                "services"
            ],
            summary=payload[
                "summary"
            ],
            created_at_event=payload.get(
                "created_at_event"
            ),
        )

        return await (
            self.repository.create(
                entity
            )
        )