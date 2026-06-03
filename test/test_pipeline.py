from datetime import datetime

from ingestion.models.metric_event import (
    MetricEvent
)

from ingestion.models.metadata import (
    Metadata
)

from processing.services.processing_pipeline import (
    ProcessingPipeline
)


def test_metric_pipeline():

    metadata = Metadata(

        cluster="local",

        namespace="default",

        environment="dev",

        team="backend",

        region="local"
    )

    metric = MetricEvent(

        metric_name="cpu_usage",

        value=95,

        service="payment-service",

        source="prometheus",

        timestamp=datetime.utcnow(),

        metadata=metadata
    )

    pipeline = ProcessingPipeline()

    result = pipeline.process_metric(
        metric
    )

    assert result is True