from datetime import datetime

from ingestion.models.trace_event import TraceEvent

from ingestion.models.metadata import Metadata

from ingestion.models.enums import EventSource


def parse_jaeger_trace(trace):

    spans = trace.get("spans", [])

    if not spans:

        return None

    first_span = spans[0]

    return TraceEvent(

        timestamp=datetime.utcnow(),

        source=EventSource.JAEGER,

        metadata=Metadata(
            cluster="sentinel-local",
            namespace="default",
            environment="development"
        ),

        trace_id=trace["traceID"],

        span_id=first_span["spanID"],

        service=first_span["processID"],

        operation=first_span["operationName"],

        duration_ms=(
            first_span["duration"] / 1000
        )
    )