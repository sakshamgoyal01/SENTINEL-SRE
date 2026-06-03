from datetime import datetime

from ai.models.verification_check import (
    VerificationCheck
)

from ai.models.verification_result import (
    VerificationResult
)

from ai.recovery.recovery_engine import (
    RecoveryEngine
)


def test_recovery_pipeline():

    verification = VerificationResult(

        verification_id="verify-1",

        execution_id="exec-1",

        service="payment-service",

        verified=False,

        health_status=
        "UNHEALTHY",

        verification_result=
        "FAILED",

        checks=[

            VerificationCheck(

                check_type=
                "health",

                passed=False,

                details=
                "Health failed"
            )
        ],

        generated_at=(
            datetime.utcnow()
        )
    )

    result = (

        RecoveryEngine()
        .process(
            verification
        )
    )

    assert (
        result.recovery_status
        ==
        "PLANNED"
    )

    assert (
        result.strategy
        .strategy_type
        ==
        "RESTART_DEPLOYMENT"
    )

    assert (
        result.service
        ==
        "payment-service"
    )