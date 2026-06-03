from datetime import datetime

from ai.models.recovery_strategy import (
    RecoveryStrategy
)

from ai.models.recovery_result import (
    RecoveryResult
)

from ai.escalation.escalation_engine import (
    EscalationEngine
)


def test_escalation_engine():

    recovery = RecoveryResult(

        recovery_id="r1",

        verification_id="v1",

        service="payment-service",

        recovery_status=
        "PLANNED",

        strategy=RecoveryStrategy(

            strategy_type=
            "RESTART_DEPLOYMENT",

            confidence=90,

            reason=
            "Recovery required"
        ),

        generated_at=(
            datetime.utcnow()
        )
    )

    result = (

        EscalationEngine()
        .process(
            recovery
        )
    )

    assert (
        result.target.team
        ==
        "SRE_TEAM"
    )