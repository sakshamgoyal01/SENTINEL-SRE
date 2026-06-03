from ai.investigation.investigation_agent import (
    InvestigationAgent
)


class InvestigationEngine:

    def __init__(self):

        self.agent = (
            InvestigationAgent()
        )

    def process(
        self,
        prioritized_event
    ):

        return (
            self.agent
            .investigate(
                prioritized_event
            )
        )