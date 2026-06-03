from backend.services.base_service import (
    BaseService
)

from backend.models.telemetry.deployment import (
    Deployment
)


class DeploymentService(
    BaseService
):

    async def create_from_event(
        self,
        payload: dict,
    ) -> Deployment:

        deployment = Deployment(
            timestamp=payload["timestamp"],
            deployment_name=payload[
                "deployment_name"
            ],
            namespace=payload[
                "namespace"
            ],
            image=payload.get(
                "image"
            ),
            replicas=payload[
                "replicas"
            ],
            available_replicas=payload.get(
                "available_replicas"
            ),
            updated_replicas=payload.get(
                "updated_replicas"
            ),
            strategy=payload.get(
                "strategy"
            ),
        )

        return await (
            self.repository.create(
                deployment
            )
        )