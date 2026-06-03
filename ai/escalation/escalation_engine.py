from ai.escalation.escalation_agent import (
    EscalationAgent
)


class EscalationEngine:

    def __init__(self):

        self.agent = (
            EscalationAgent()
        )

    def process(
        self,
        recovery_result
    ):

        return (

            self.agent
            .process(
                recovery_result
            )
        )