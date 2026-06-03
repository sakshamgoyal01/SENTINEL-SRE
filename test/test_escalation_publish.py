# test_escalation_publish.py

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

from ai.publishers.escalation_publisher import (
    EscalationPublisher
)

recovery = RecoveryResult(

    recovery_id="test",

    verification_id="verify",

    service="payment-service",

    recovery_status="PLANNED",

    strategy=RecoveryStrategy(

        strategy_type="RESTART_DEPLOYMENT",

        confidence=90,

        reason="Recovery required"
    ),

    generated_at=datetime.utcnow()
)

record = (

    EscalationEngine()
    .process(
        recovery
    )
)

EscalationPublisher().publish(
    record
)