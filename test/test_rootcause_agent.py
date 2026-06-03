from datetime import datetime

from ai.models.evidence import (
    Evidence
)

from ai.models.timeline_event import (
    TimelineEvent
)

from ai.models.investigation_result import (
    InvestigationResult
)

from ai.rootcause.rootcause_engine import (
    RootCauseEngine
)


def test_rootcause_agent():

    investigation = InvestigationResult(

        investigation_id="investigation-1",

        service="payment-service",

        severity="CRITICAL",

        priority="P1",

        summary="Timeout burst",

        findings=[

            "Critical incident detected",

            "High risk score observed",

            "Escalation required"
        ],

        evidence=[

            Evidence(

                evidence_type="summary",

                source="aggregation",

                description=(
                    "Timeout burst"
                ),

                confidence=1.0
            )

        ],

        timeline=[

            TimelineEvent(

                timestamp=(
                    datetime.utcnow()
                ),

                event_type=(
                    "incident_start"
                ),

                description=(
                    "Incident detected"
                )
            )

        ],

        confidence=100.0,

        generated_at=(
            datetime.utcnow()
        )
    )

    engine = RootCauseEngine()

    result = engine.process(
        investigation
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

        result.root_cause
        .category
        == "Dependency Failure"
    )

    assert (

        "timeout"
        in result.root_cause
        .probable_cause
        .lower()
    )

    assert (

        result.confidence
        >= 80
    )

    assert (

        len(
            result.causal_chain.chain
        )
        > 0
    )

    assert (

        "Dependency latency increased"
        in result.causal_chain.chain
    )