from datetime import datetime

from processing.models.aggregated_event import (
    AggregatedEvent
)

from processing.models.prioritized_event import (
    PrioritizedEvent
)

from processing.routing.routing_manager import (
    RoutingManager
)


def test_routing_engine():

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

        risk_score=95,

        source_events=100
    )

    event = PrioritizedEvent(

        incident_priority="P1",

        impact_score=90,

        final_risk_score=95,

        requires_human_review=True,

        escalation_required=True,

        aggregated_event=aggregated
    )

    manager = RoutingManager()

    result = manager.route(
        event
    )

    assert result.routed

    assert "incident" in (
        result.destinations
    )

    assert "alert" in (
        result.destinations
    )