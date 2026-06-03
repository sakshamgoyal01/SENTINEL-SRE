from datetime import datetime

from ingestion.models.metric_event import MetricEvent

from ingestion.models.metadata import Metadata

from ingestion.models.enums import EventSource


def parse_prometheus_metric(raw_metric):

    metric = raw_metric["metric"]

    value = float(raw_metric["value"][1])

    return MetricEvent(

        timestamp=datetime.utcnow(),

        source=EventSource.PROMETHEUS,

        metadata=Metadata(
            cluster="sentinel-local",
            namespace="monitoring",
            environment="development"
        ),

        service=metric.get(
            "job",
            "infrastructure"
        ),

        metric_name=metric.get(
            "__name__",
            "cpu_usage"
        ),

        value=value,

        labels=metric
    )