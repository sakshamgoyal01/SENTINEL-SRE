from backend.services.base_service import (
    BaseService
)

from backend.models.telemetry.kubernetes_event import (
    KubernetesEvent
)


class KubernetesService(
    BaseService
):

    async def create_from_event(
        self,
        payload: dict,
    ) -> KubernetesEvent:

        event = KubernetesEvent(
            timestamp=payload["timestamp"],
            reason=payload["reason"],
            message=payload["message"],
            event_type=payload[
                "event_type"
            ],
            involved_object=payload[
                "involved_object"
            ],
        )

        return await (
            self.repository.create(
                event
            )
        )