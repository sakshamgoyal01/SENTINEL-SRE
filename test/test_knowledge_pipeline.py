from datetime import datetime

from ai.models.remediation_action import (
    RemediationAction
)

from ai.models.remediation_plan import (
    RemediationPlan
)

from ai.models.remediation_result import (
    RemediationResult
)

from ai.knowledge.knowledge_engine import (
    KnowledgeEngine
)


def test_knowledge_pipeline():

    remediation = RemediationResult(

        remediation_id="rem-1",

        risk_id="risk-1",

        service="payment-service",

        priority="P1",

        plan=RemediationPlan(

            runbook=(
                "RUNBOOK_DEPENDENCY_FAILURE"
            ),

            actions=[

                RemediationAction(

                    action_type=(
                        "VERIFY_DEPENDENCY"
                    ),

                    priority="IMMEDIATE",

                    description=(
                        "Verify dependency"
                    ),

                    automated=False
                )
            ]
        ),

        generated_at=(
            datetime.utcnow()
        )
    )

    engine = KnowledgeEngine()

    result = engine.process(
        remediation
    )

    assert (
        result.pattern
        .incident_type
        ==
        "SERVICE_DEPENDENCY"
    )

    assert (
        result.remediation
        .runbook
        ==
        "RUNBOOK_DEPENDENCY_FAILURE"
    )