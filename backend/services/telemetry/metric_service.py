from backend.services.base_service import (
    BaseService
)

from backend.models.telemetry.metric import Metric


class MetricService(
    BaseService
):

    async def create_from_event(
        self,
        payload: dict,
    ) -> Metric:

        metric = Metric(
            event_id=payload["event_id"],
            timestamp=payload["timestamp"],
            source=payload["source"],
            service=payload["service"],
            metric_name=payload["metric_name"],
            value=payload["value"],
            labels=payload.get(
                "labels",
                {}
            ),
            unit=payload.get("unit"),
            cluster=payload.get(
                "cluster"
            ),
            environment=payload.get(
                "environment"
            ),
            namespace=payload.get(
                "namespace"
            ),
        )

        return await (
            self.repository.create(
                metric
            )
        )