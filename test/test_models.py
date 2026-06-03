from datetime import datetime, timezone

from ingestion.models.metric_event import MetricEvent
from ingestion.models.log_event import LogEvent
from ingestion.models.trace_event import TraceEvent
from ingestion.models.metadata import Metadata
from ingestion.models.enums import EventSource


def test_metric_event():

    event = MetricEvent(
        timestamp=datetime.now(timezone.utc),
        source=EventSource.PROMETHEUS,
        metadata=Metadata(
            cluster="sentinel-local",
            namespace="monitoring",
            environment="development"
        ),
        service="payment-service",
        metric_name="cpu_usage",
        value=75.0
    )

    assert event.metric_name == "cpu_usage"


def test_log_event():

    event = LogEvent(
        timestamp=datetime.now(timezone.utc),
        source=EventSource.LOKI,
        metadata=Metadata(
            cluster="sentinel-local",
            namespace="default",
            environment="development"
        ),
        service="payment-service",
        severity="INFO",
        message="database error"
    )

    assert event.message == "database error"


def test_trace_event():

    event = TraceEvent(
        timestamp=datetime.now(timezone.utc),
        source=EventSource.JAEGER,
        metadata=Metadata(
            cluster="sentinel-local",
            namespace="default",
            environment="development"
        ),
        trace_id="abc123",
        span_id="span1",
        service="payment-service",
        operation="GET /payment",
        duration_ms=10.0
    )

    assert event.trace_id == "abc123"