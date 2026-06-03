from datetime import datetime

from ingestion.models.metadata import (
    Metadata
)

from ingestion.models.trace_event import (
    TraceEvent
)

from processing.processors.trace_processor import (
    TraceProcessor
)


def test_trace_processor():

    metadata = Metadata(

        cluster="local",

        namespace="default",

        environment="dev",

        team="backend",

        region="local"
    )

    trace = TraceEvent(

        trace_id="trace-1",

        span_id="span-1",

        service="payment-service",

        operation="charge-card",

        duration_ms=1200,

        status_code=500,

        timestamp=datetime.utcnow(),

        source="jaeger",

        metadata=metadata
    )

    processor = TraceProcessor()

    result = processor.process(
        trace
    )

    assert result.success

    assert (
        result.event.event_type
        == "trace"
    )

    assert (
        result.event.severity
        == "CRITICAL"
    )

    assert (
        result.event.priority
        == "P1"
    )