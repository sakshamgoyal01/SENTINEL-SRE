from ai.execution.execution_agent import (
    ExecutionAgent
)


class ExecutionEngine:

    def __init__(self):

        self.agent = (
            ExecutionAgent()
        )

    def process(
        self,
        approval_decision
    ):

        return (

            self.agent
            .execute(
                approval_decision
            )
        )