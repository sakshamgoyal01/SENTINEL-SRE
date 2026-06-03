from datetime import datetime

from ai.models.root_cause import (
    RootCause
)

from ai.models.causal_chain import (
    CausalChain
)

from ai.models.rootcause_result import (
    RootCauseResult
)

from ai.risk.risk_engine import (
    RiskEngine
)


def test_risk_agent():

    rootcause_result = RootCauseResult(

        rootcause_id="rootcause-1",

        investigation_id="investigation-1",

        service="payment-service",

        severity="CRITICAL",

        priority="P1",

        root_cause=RootCause(

            category=(
                "Dependency Failure"
            ),

            probable_cause=(
                "Downstream dependency timeout"
            ),

            confidence=95.0
        ),

        causal_chain=CausalChain(

            chain=[

                "Dependency latency increased",

                "Application requests timed out",

                "Error volume increased",

                "Critical incident triggered"
            ]
        ),

        evidence=[

            "Dependency Failure",

            "Network Failure"
        ],

        confidence=95.0,

        generated_at=(
            datetime.utcnow()
        )
    )

    engine = RiskEngine()

    result = engine.process(
        rootcause_result
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

        result.blast_radius
        .impacted_customers
        == 10000
    )

    assert (

        len(

            result.blast_radius
            .impacted_services

        ) == 5
    )

    assert (

        result.impact_assessment
        .customer_impact
        == "HIGH"
    )

    assert (

        result.impact_assessment
        .business_impact
        == "Revenue Impact"
    )

    assert (

        result.risk_summary
        .risk_level
        == "CRITICAL"
    )

    assert (

        result.risk_summary
        .estimated_mttr_minutes
        == 45
    )

    assert (

        result.risk_summary
        .slo_risk_percent
        == 95.0
    )