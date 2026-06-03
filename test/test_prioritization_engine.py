from datetime import datetime

from processing.models.aggregated_event import (
    AggregatedEvent
)

from processing.prioritization.prioritization_engine import (
    PrioritizationEngine
)


def test_prioritization_engine():

    event = AggregatedEvent(

        aggregation_key="payment",

        category="availability",

        severity="CRITICAL",

        count=100,

        first_seen=datetime.utcnow(),

        last_seen=datetime.utcnow(),

        services=[
            "payment-service"
        ],

        summary="Timeout burst",

        risk_score=95,

        source_events=100
    )

    engine = (
        PrioritizationEngine()
    )

    result = (
        engine.prioritize(
            event
        )
    )

    assert (
        result.incident_priority
        == "P1"
    )

    assert (
        result.escalation_required
        is True
    )