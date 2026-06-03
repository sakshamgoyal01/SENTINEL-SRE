from ingestion.models.base_event import BaseEvent

class KubernetesEvent(BaseEvent):

    reason: str

    message: str

    event_type: str

    involved_object: dict