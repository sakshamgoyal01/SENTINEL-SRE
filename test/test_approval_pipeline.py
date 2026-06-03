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

from ai.approval.approval_engine import (
    ApprovalEngine
)


def test_approval_pipeline():

    remediation = RemediationResult(

        remediation_id="1",

        risk_id="1",

        service="payment-service",

        priority="P4",

        plan=RemediationPlan(

            runbook="RUNBOOK",

            actions=[

                RemediationAction(

                    action_type=
                    "RESTART_POD",

                    priority=
                    "LOW",

                    description=
                    "Restart pod",

                    automated=True
                )
            ]
        ),

        generated_at=(
            datetime.utcnow()
        )
    )

    result = (

        ApprovalEngine()
        .process(
            remediation
        )
    )

    assert (
        result.approved
        is True
    )

    assert (
        result
        .requires_human_approval
        is False
    )

    assert (
        len(
            result.actions
        )
        == 1
    )