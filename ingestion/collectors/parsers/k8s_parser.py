from datetime import datetime

from ingestion.models.kubernetes_event import KubernetesEvent
from ingestion.models.metadata import Metadata
from ingestion.models.enums import EventSource


def parse_k8s_event(event):

    return KubernetesEvent(

        timestamp=datetime.utcnow(),

        source=EventSource.KUBERNETES,

        metadata=Metadata(

            cluster="sentinel-local",

            namespace=(
                event.metadata.namespace
                or "default"
            ),

            environment="development",

            node=(
                event.source.component
                if event.source
                else None
            )
        ),

        reason=event.reason,

        message=event.message,

        type=event.type,

        involved_object={

            "kind": (
                event.involved_object.kind
            ),

            "name": (
                event.involved_object.name
            )
        }
    )