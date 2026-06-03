class EscalationEvaluator:

    def should_escalate(
        self,
        recovery_result
    ) -> bool:

        return (

            recovery_result
            .recovery_status
            ==
            "PLANNED"
        )