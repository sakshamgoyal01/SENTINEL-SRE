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


def test_knowledge_agent():

    remediation_result = RemediationResult(

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
                        "Verify downstream service"
                    ),

                    automated=False
                ),

                RemediationAction(

                    action_type=(
                        "ENABLE_CIRCUIT_BREAKER"
                    ),

                    priority="HIGH",

                    description=(
                        "Enable circuit breaker"
                    ),

                    automated=True
                )
            ]
        ),

        generated_at=(
            datetime.utcnow()
        )
    )

    engine = KnowledgeEngine()

    result = engine.process(
        remediation_result
    )

    assert (
        result.service
        == "payment-service"
    )

    assert (
        result.pattern
        .incident_type
        ==
        "SERVICE_DEPENDENCY"
    )

    assert (
        result.pattern
        .root_cause
        ==
        "DEPENDENCY_FAILURE"
    )

    assert (
        result.remediation
        .runbook
        ==
        "RUNBOOK_DEPENDENCY_FAILURE"
    )

    assert (
        result.remediation
        .successful
        is True
    )

    assert (
        result.remediation
        .automation_used
        is True
    )

    assert (
        "VERIFY_DEPENDENCY"
        in result.remediation.actions
    )

    assert (
        "ENABLE_CIRCUIT_BREAKER"
        in result.remediation.actions
    )