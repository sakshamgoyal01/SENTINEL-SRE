from ai.audit.audit_builder import (
    AuditBuilder
)


class AuditAgent:

    def __init__(self):

        self.builder = (
            AuditBuilder()
        )

    def process(
        self,
        recovery_result
    ):

        return (

            self.builder
            .build_from_recovery(
                recovery_result
            )
        )