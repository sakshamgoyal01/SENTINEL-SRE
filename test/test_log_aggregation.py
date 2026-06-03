from datetime import datetime

from ingestion.models.metadata import Metadata

from processing.models.operational_context import (
    OperationalContext
)

from processing.models.operational_event import (
    OperationalEvent
)

from processing.aggregation.log_aggregator import (
    LogAggregator
)


def test_log_aggregation():

    metadata = Metadata(
        cluster="local",
        namespace="default",
        environment="dev",
        team="backend",
        region="local"
    )

    aggregator = LogAggregator()

    result = None

    for i in range(20):

        event = OperationalEvent(

            timestamp=datetime.utcnow(),

            source="loki",

            metadata=metadata,

            service="payment-service",

            event_type="log",

            category="availability",

            severity="CRITICAL",

            priority="P1",

            risk_score=95,

            summary="database timeout",

            operational_context=(
                OperationalContext(
                    environment="dev",
                    cluster="local",
                    namespace="default"
                )
            ),

            raw_event={}
        )

        result = aggregator.aggregate(
            event
        )

    assert result.triggered

    assert (
        result.aggregated_event.count
        == 20
    )