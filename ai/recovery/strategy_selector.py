from ai.models.recovery_strategy import (
    RecoveryStrategy
)


class StrategySelector:

    def select(
        self,
        failure_type: str
    ) -> RecoveryStrategy:

        if failure_type == "UNHEALTHY":

            return RecoveryStrategy(

                strategy_type=
                "RESTART_DEPLOYMENT",

                confidence=90.0,

                reason=
                "Service remained unhealthy "
                "after execution"
            )

        return RecoveryStrategy(

            strategy_type=
            "NO_ACTION",

            confidence=100.0,

            reason=
            "Verification successful"
        )