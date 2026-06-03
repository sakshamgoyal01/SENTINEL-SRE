from ai.recovery.recovery_agent import (
    RecoveryAgent
)


class RecoveryEngine:

    def __init__(self):

        self.agent = (
            RecoveryAgent()
        )

    def process(
        self,
        verification_result
    ):

        return (

            self.agent
            .recover(
                verification_result
            )
        )