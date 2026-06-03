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


def test_investigation_agent():

    aggregated_event = AggregatedEvent(

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

    prioritized_event = PrioritizedEvent(

        incident_priority="P1",

        impact_score=90.0,

        final_risk_score=95.0,

        requires_human_review=True,

        escalation_required=True,

        aggregated_event=aggregated_event
    )

    engine = InvestigationEngine()

    result = engine.process(
        prioritized_event
    )

    assert (
        result.service
        == "payment-service"
    )

    assert (
        result.severity
        == "CRITICAL"
    )

    assert (
        result.priority
        == "P1"
    )

    assert (
        result.confidence
        == 100.0
    )

    assert (
        len(result.evidence)
        >= 3
    )

    assert (
        len(result.timeline)
        == 2
    )

    assert (
        "Critical incident detected"
        in result.findings
    )

    assert (
        "High risk score observed"
        in result.findings
    )

    assert (
        "Escalation required"
        in result.findings
    )

    assert (
        "Human review required"
        in result.findings
    )

    assert (
        "Large aggregation burst detected"
        in result.findings
    )