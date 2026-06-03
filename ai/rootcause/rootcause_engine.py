from ai.rootcause.rootcause_agent import (
    RootCauseAgent
)


class RootCauseEngine:

    def __init__(self):

        self.agent = (
            RootCauseAgent()
        )

    def process(
        self,
        investigation_result
    ):

        return (
            self.agent
            .analyze(
                investigation_result
            )
        )