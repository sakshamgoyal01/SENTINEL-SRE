from ingestion.models.base_event import BaseEvent


class DeploymentEvent(BaseEvent):

    deployment_name: str

    namespace: str

    image: str | None = None

    replicas: int

    available_replicas: int | None = None

    updated_replicas: int | None = None

    strategy: str | None = None