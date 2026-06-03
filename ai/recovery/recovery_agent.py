import uuid

from datetime import datetime

from ai.models.recovery_result import (
    RecoveryResult
)

from ai.recovery.failure_analyzer import (
    FailureAnalyzer
)

from ai.recovery.strategy_selector import (
    StrategySelector
)

from ai.recovery.recovery_planner import (
    RecoveryPlanner
)


class RecoveryAgent:

    def __init__(self):

        self.analyzer = (
            FailureAnalyzer()
        )

        self.selector = (
            StrategySelector()
        )

        self.planner = (
            RecoveryPlanner()
        )

    def recover(
        self,
        verification_result
    ) -> RecoveryResult:

        failure_type = (

            self.analyzer
            .analyze(
                verification_result
            )
        )

        strategy = (

            self.selector
            .select(
                failure_type
            )
        )

        strategy = (

            self.planner
            .plan(
                strategy
            )
        )

        status = (
            "PLANNED"
            if strategy.strategy_type
            != "NO_ACTION"
            else "NOT_REQUIRED"
        )

        return RecoveryResult(

            recovery_id=str(
                uuid.uuid4()
            ),

            verification_id=(
                verification_result
                .verification_id
            ),

            service=(
                verification_result
                .service
            ),

            recovery_status=status,

            strategy=strategy,

            generated_at=(
                datetime.utcnow()
            )
        )
    