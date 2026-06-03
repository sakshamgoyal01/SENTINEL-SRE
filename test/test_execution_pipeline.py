from datetime import datetime

from ai.models.approval_action import (
    ApprovalAction
)

from ai.models.approval_decision import (
    ApprovalDecision
)

from ai.execution.execution_engine import (
    ExecutionEngine
)


def test_execution_pipeline():

    decision = ApprovalDecision(

        approval_id="approval-1",

        service="payment-service",

        approved=True,

        requires_human_approval=False,

        reason="Auto approved",

        actions=[

            ApprovalAction(

                action_type=
                "RESTART_POD",

                priority=
                "HIGH",

                automated=True
            )
        ],

        generated_at=(
            datetime.utcnow()
        )
    )

    result = (

        ExecutionEngine()
        .process(
            decision
        )
    )

    assert (
        result.executed
        is True
    )

    assert (
        result.status
        ==
        "SIMULATED_SUCCESS"
    )

    assert (
        result.mode
        ==
        "DRY_RUN"
    )

    assert (
        result.service
        ==
        "payment-service"
    )

    assert (
        len(
            result.actions
        )
        == 1
    )