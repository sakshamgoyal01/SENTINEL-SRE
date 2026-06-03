from ai.risk.risk_agent import (
    RiskAgent
)


class RiskEngine:

    def __init__(self):

        self.agent = (
            RiskAgent()
        )

    def process(
        self,
        rootcause_result
    ):

        return (
            self.agent
            .analyze(
                rootcause_result
            )
        )