from datetime import datetime

from ingestion.models.log_event import LogEvent

from ingestion.models.metadata import Metadata

from ingestion.models.enums import (
    EventSource,
    SeverityLevel
)


def parse_loki_log(stream, value):

    timestamp_ns, message = value

    return LogEvent(

        timestamp=datetime.utcnow(),

        source=EventSource.LOKI,

        metadata=Metadata(
            cluster="sentinel-local",
            namespace=stream.get(
                "namespace",
                "default"
            ),
            environment="development"
        ),

        service=stream.get(
            "job",
            "unknown-service"
        ),

        severity=SeverityLevel.INFO,

        message=message
    )