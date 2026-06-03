from ai.executive.executive_summary_agent import (
    ExecutiveSummaryAgent
)


class ExecutiveSummaryEngine:

    def __init__(self):

        self.agent = (
            ExecutiveSummaryAgent()
        )

    def process(
        self,
        knowledge_record
    ):

        return (

            self.agent
            .analyze(
                knowledge_record
            )
        )