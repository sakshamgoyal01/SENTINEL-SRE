from datetime import datetime

from ai.models.recovery_strategy import (
    RecoveryStrategy
)

from ai.models.recovery_result import (
    RecoveryResult
)

from ai.audit.audit_engine import (
    AuditEngine
)


def test_audit_engine():

    recovery = RecoveryResult(

        recovery_id="recovery-1",

        verification_id="verify-1",

        service="payment-service",

        recovery_status=
        "PLANNED",

        strategy=RecoveryStrategy(

            strategy_type=
            "RESTART_DEPLOYMENT",

            confidence=90.0,

            reason=
            "Recovery planned"
        ),

        generated_at=(
            datetime.utcnow()
        )
    )

    result = (

        AuditEngine()
        .process(
            recovery
        )
    )

    assert (
        result.service
        ==
        "payment-service"
    )

    assert (
        result.status
        ==
        "PLANNED"
    )

    assert (
        result.details
        ==
        "RESTART_DEPLOYMENT"
    )