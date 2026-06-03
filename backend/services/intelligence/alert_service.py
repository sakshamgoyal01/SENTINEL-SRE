from backend.services.base_service import (
    BaseService
)

from backend.models.intelligence.alert import (
    Alert
)


class AlertService(
    BaseService
):

    async def create_from_event(
        self,
        payload: dict,
    ) -> Alert:

        entity = Alert(
            alert_id=payload[
                "alert_id"
            ],
            service=payload[
                "service"
            ],
            severity=payload[
                "severity"
            ],
            title=payload[
                "title"
            ],
            description=payload[
                "description"
            ],
            status=payload[
                "status"
            ],
            source=payload[
                "source"
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