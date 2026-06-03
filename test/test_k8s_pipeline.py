from datetime import datetime

from ingestion.models.metadata import (
    Metadata
)

from ingestion.models.kubernetes_event import (
    KubernetesEvent
)

from processing.processors.k8s_processor import (
    KubernetesProcessor
)


def test_k8s_processor():

    metadata = Metadata(

        cluster="local",

        namespace="default",

        environment="dev",

        team="backend",

        region="local"
    )

    event = KubernetesEvent(

        timestamp=datetime.utcnow(),

        source="kubernetes",

        metadata=metadata,

        reason="CrashLoopBackOff",

        message="Container restarting repeatedly",

        event_type="Warning",

        involved_object={

            "kind": "Pod",

            "name": "payment-pod"
        }
    )

    processor = KubernetesProcessor()

    result = processor.process(
        event
    )

    assert result.success

    assert (
        result.event.event_type
        == "k8s_event"
    )

    assert (
        result.event.severity
        == "CRITICAL"
    )

    assert (
        result.event.priority
        == "P1"
    )