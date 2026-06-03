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


def test_audit_pipeline():

    recovery = RecoveryResult(

        recovery_id="r1",

        verification_id="v1",

        service="payment-service",

        recovery_status="PLANNED",

        strategy=RecoveryStrategy(

            strategy_type=
            "RESTART_DEPLOYMENT",

            confidence=90,

            reason="test"
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
        result.status
        ==
        "PLANNED"
    )