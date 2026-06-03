from ai.remediation.remediation_agent import (
    RemediationAgent
)


class RemediationEngine:

    def __init__(self):

        self.agent = (
            RemediationAgent()
        )

    def process(
        self,
        risk_result
    ):

        return (

            self.agent
            .analyze(
                risk_result
            )
        )