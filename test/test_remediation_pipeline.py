from datetime import datetime

from ai.models.blast_radius import (
    BlastRadius
)

from ai.models.impact_assessment import (
    ImpactAssessment
)

from ai.models.risk_summary import (
    RiskSummary
)

from ai.models.risk_result import (
    RiskResult
)

from ai.remediation.remediation_engine import (
    RemediationEngine
)


def test_remediation_pipeline():

    risk_result = RiskResult(

        risk_id="risk-1",

        rootcause_id="rootcause-1",

        service="payment-service",

        priority="P1",

        blast_radius=BlastRadius(

            impacted_services=[
                "payment-service"
            ],

            impacted_regions=[
                "us-east-1"
            ],

            impacted_customers=10000,

            severity="CRITICAL"
        ),

        impact_assessment=ImpactAssessment(

            customer_impact="HIGH",

            business_impact="Revenue Impact",

            operational_impact=(
                "Dependency Failure"
            )
        ),

        risk_summary=RiskSummary(

            risk_level="CRITICAL",

            estimated_mttr_minutes=45,

            slo_risk_percent=95
        ),

        generated_at=(
            datetime.utcnow()
        )
    )

    engine = RemediationEngine()

    result = engine.process(
        risk_result
    )

    assert (
        result.plan.runbook
        ==
        "RUNBOOK_DEPENDENCY_FAILURE"
    )

    assert (
        len(
            result.plan.actions
        ) > 0
    )