from datetime import datetime

from ai.models.execution_action import (
    ExecutionAction
)

from ai.models.execution_result import (
    ExecutionResult
)

from ai.verification.verification_engine import (
    VerificationEngine
)


def test_verification_engine():

    execution = ExecutionResult(

        execution_id="exec-1",

        service="payment-service",

        executed=True,

        status="SIMULATED_SUCCESS",

        mode="DRY_RUN",

        actions=[

            ExecutionAction(

                action_type=
                "RESTART_POD",

                target=
                "payment-service",

                mode=
                "DRY_RUN"
            )
        ],

        generated_at=(
            datetime.utcnow()
        )
    )

    result = (

        VerificationEngine()
        .process(
            execution
        )
    )

    assert (
        result.verified
        is True
    )

    assert (
        result.health_status
        ==
        "HEALTHY"
    )

    assert (
        result.verification_result
        ==
        "SUCCESS"
    )

    assert (
        len(
            result.checks
        )
        == 4
    )