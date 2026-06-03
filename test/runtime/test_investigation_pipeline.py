from datetime import datetime

from processing.models.aggregated_event import (
    AggregatedEvent
)

from processing.models.prioritized_event import (
    PrioritizedEvent
)

from ai.investigation.investigation_engine import (
    InvestigationEngine
)


def test_investigation_pipeline():

    aggregated = AggregatedEvent(

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

        risk_score=95.0,

        source_events=100
    )

    incident = PrioritizedEvent(

        incident_priority="P1",

        impact_score=90.0,

        final_risk_score=95.0,

        requires_human_review=True,

        escalation_required=True,

        aggregated_event=aggregated
    )

    engine = InvestigationEngine()

    result = engine.process(
        incident
    )

    assert (
        result.service
        == "payment-service"
    )

    assert (
        result.priority
        == "P1"
    )

    assert (
        result.severity
        == "CRITICAL"
    )

    assert (
        result.confidence
        >= 90
    )