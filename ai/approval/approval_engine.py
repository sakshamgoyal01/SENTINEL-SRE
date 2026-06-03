from ai.approval.approval_agent import (
    ApprovalAgent
)


class ApprovalEngine:

    def __init__(self):

        self.agent = (
            ApprovalAgent()
        )

    def process(
        self,
        remediation_result
    ):

        return (

            self.agent
            .analyze(
                remediation_result
            )
        )