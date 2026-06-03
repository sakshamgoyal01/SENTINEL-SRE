from ai.verification.verification_agent import (
    VerificationAgent
)


class VerificationEngine:

    def __init__(self):

        self.agent = (
            VerificationAgent()
        )

    def process(
        self,
        execution_result
    ):

        return (

            self.agent
            .verify(
                execution_result
            )
        )