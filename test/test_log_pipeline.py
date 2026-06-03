from datetime import datetime

from ingestion.models.log_event import (
    LogEvent
)

from ingestion.models.metadata import (
    Metadata
)

from ingestion.models.enums import (
    SeverityLevel
)

from processing.processors.log_processor import (
    LogProcessor
)


def test_log_processor():

    metadata = Metadata(
        cluster="local",
        namespace="default",
        environment="dev",
        team="backend",
        region="local"
    )

    event = LogEvent(
        timestamp=datetime.utcnow(),
        source="loki",
        service="payment-service",
        severity=SeverityLevel.ERROR,
        message="database connection timeout",
        metadata=metadata
    )

    processor = LogProcessor()

    result = processor.process(
        event
    )

    assert result.success

    assert (
        result.event.event_type
        == "log"
    )

    assert (
        result.event.category
        == "availability"
    )

    assert (
        result.event.priority
        == "P2"
    )