from ai.audit.audit_agent import (
    AuditAgent
)


class AuditEngine:

    def __init__(self):

        self.agent = (
            AuditAgent()
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