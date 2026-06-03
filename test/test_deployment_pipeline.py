from datetime import datetime

from ingestion.models.metadata import (
    Metadata
)

from ingestion.models.deployment_event import (
    DeploymentEvent
)

from processing.processors.deployment_processor import (
    DeploymentProcessor
)


def test_deployment_processor():

    metadata = Metadata(

        cluster="local",

        namespace="default",

        environment="dev",

        team="backend",

        region="local"
    )

    deployment = DeploymentEvent(

        deployment_name="payment-service",

        namespace="default",

        replicas=5,

        available_replicas=2,

        updated_replicas=2,

        strategy="RollingUpdate",

        timestamp=datetime.utcnow(),

        source="kubernetes",

        metadata=metadata
    )

    processor = DeploymentProcessor()

    result = processor.process(
        deployment
    )

    assert result.success

    assert (
        result.event.event_type
        == "deployment"
    )

    assert (
        result.event.severity
        == "WARNING"
    )

    assert (
        result.event.priority
        == "P3"
    )